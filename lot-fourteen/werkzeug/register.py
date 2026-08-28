# -*- coding: utf-8 -*-
u"""Das Tagesregister: welcher Erzaehltag steht in welchem Kapitel.

Wozu. `check.py` prueft eine Datumszeile gegen den Kalender. Es kann nicht
sagen, ob ein Tag **fehlt**, ob zwei Kapitel denselben Tag beanspruchen, oder
ob ein Satz mitten im Text auf einen Tag zeigt, den es nicht gibt. Genau das
ist die Klasse, in der die Fehler sitzen, und genau dafuer ist dieses Register
da.

Es liest nur die Kapiteldateien und rechnet. Es entscheidet nichts.

Aufrufe:

    python werkzeug/register.py            Bericht auf die Konsole
    python werkzeug/register.py --schreiben erzeugt/REGISTER.md neu
    python werkzeug/register.py --luecken   nur die Loecher und Kollisionen
"""
import datetime
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.dirname(HIER)

TAG1 = datetime.date(2025, 10, 4)
DATEI = re.compile(r'^ch(\d+)_v(\d+)_(\d+)_en\.md$')

MONATE = [u'January', u'February', u'March', u'April', u'May', u'June', u'July',
          u'August', u'September', u'October', u'November', u'December']
WOCHENTAGE = [u'Monday', u'Tuesday', u'Wednesday', u'Thursday', u'Friday',
              u'Saturday', u'Sunday']

ZAHLWORT = {u'one': 1, u'two': 2, u'three': 3, u'four': 4, u'five': 5, u'six': 6,
            u'seven': 7, u'eight': 8, u'nine': 9, u'ten': 10, u'eleven': 11,
            u'twelve': 12, u'thirteen': 13, u'fourteen': 14, u'fifteen': 15,
            u'sixteen': 16, u'seventeen': 17, u'eighteen': 18, u'nineteen': 19,
            u'twenty': 20, u'thirty': 30, u'forty': 40, u'fifty': 50,
            u'sixty': 60, u'seventy': 70, u'eighty': 80, u'ninety': 90}

# *Day 22 - Saturday 25 October*  /  ## Day Two Hundred and Two - Monday 4 May
# *Days 27 to 28 - Thursday 30 to Friday 31 October*
KOPF = re.compile(
    r'^\s*(?:#+\s*|\*)?Days?\s+([A-Za-z0-9 \-]+?)\s*·\s*(.+?)\*?\s*$')
SPANNE = re.compile(r'^(.*?)\s+to\s+(.*)$')
DATUMTEIL = re.compile(r'([A-Za-z]+)\s+(\d{1,2})\s+([A-Za-z]+)')


def tagzahl(s):
    s = s.strip().lower()
    if s.isdigit():
        return int(s)
    gesamt = lauf = 0
    for w in re.split(r'[\s\-]+', s):
        if w in (u'and', u''):
            continue
        if w == u'hundred':
            lauf = (lauf or 1) * 100
            gesamt += lauf
            lauf = 0
            continue
        if w not in ZAHLWORT:
            return None
        lauf += ZAHLWORT[w]
    return (gesamt + lauf) or None


def datum(n):
    return TAG1 + datetime.timedelta(days=n - 1)


def kanon():
    u"""Hoechste Fassung je Kapitelnummer, je Band."""
    aus = []
    for ordner, band in ((u'chapters', 1), (u'chapters-2', 2)):
        hoechste = {}
        p = os.path.join(WURZEL, ordner)
        for name in os.listdir(p):
            m = DATEI.match(name)
            if m:
                k = int(m.group(1))
                v = (int(m.group(2)), int(m.group(3)))
                if k not in hoechste or v > hoechste[k][0]:
                    hoechste[k] = (v, name)
        for k in sorted(hoechste):
            aus.append((band, k, os.path.join(p, hoechste[k][1]), hoechste[k][1]))
    return aus


def kopfzeilen(zeilen):
    u"""(Tagnummern, Rohzeile, Zeilennummer) je Datumszeile."""
    aus = []
    for i, z in enumerate(zeilen, 1):
        m = KOPF.match(z)
        if not m:
            continue
        roh_tage, roh_datum = m.group(1), m.group(2)
        sp = SPANNE.match(roh_tage)
        if sp:
            a, b = tagzahl(sp.group(1)), tagzahl(sp.group(2))
            if a is None or b is None or b < a:
                aus.append((None, z.strip(), i))
                continue
            tage = list(range(a, b + 1))
        else:
            n = tagzahl(roh_tage)
            if n is None:
                aus.append((None, z.strip(), i))
                continue
            tage = [n]
        aus.append((tage, z.strip(), i, roh_datum))
    return aus


def sammeln():
    kapitel = []
    fehler = []
    for band, k, pfad, name in kanon():
        text = io.open(pfad, encoding='utf-8').read()
        zeilen = text.split(u'\n')
        titel = zeilen[0].lstrip(u'# ').strip() if zeilen else u''
        koepfe = kopfzeilen(zeilen)
        tage = []
        for eintrag in koepfe:
            if eintrag[0] is None:
                fehler.append((band, k, eintrag[2],
                               u'Datumszeile nicht lesbar: %s' % eintrag[1]))
                continue
            ns, roh, zeile, roh_datum = eintrag[0], eintrag[1], eintrag[2], eintrag[3]
            # Datum und Wochentag gegen den Kalender. Bei einer Spanne steht
            # der Monat nur einmal, hinten: "Sunday 14 to Tuesday 16 December".
            # Geprueft werden darum nur der erste und der letzte Tag, und der
            # Monat des ersten wird vom letzten geliehen, wenn er dort fehlt.
            teile = DATUMTEIL.findall(roh_datum)
            teile = [t for t in teile if t[2].capitalize() in MONATE
                     or t[2].lower() == u'to']
            paare = []
            if teile:
                monat_hinten = None
                for t in reversed(teile):
                    if t[2].capitalize() in MONATE:
                        monat_hinten = t[2]
                        break
                erst = teile[0]
                if erst[2].lower() == u'to' and monat_hinten:
                    erst = (erst[0], erst[1], monat_hinten)
                paare.append((ns[0], erst))
                if len(ns) > 1 and len(teile) > 1:
                    paare.append((ns[-1], teile[-1]))
            for n, (wt, tagz, mon) in paare:
                d = datum(n)
                ok = (wt.capitalize() == WOCHENTAGE[d.weekday()]
                      and int(tagz) == d.day
                      and mon.capitalize() == MONATE[d.month - 1])
                if not ok:
                    fehler.append(
                        (band, k, zeile,
                         u'Tag %d ist %s %d %s, Zeile sagt %s %s %s'
                         % (n, WOCHENTAGE[d.weekday()], d.day,
                            MONATE[d.month - 1], wt, tagz, mon)))
            tage.extend(ns)
        woerter = len(text.split())
        kapitel.append({u'band': band, u'nr': k, u'datei': name,
                        u'titel': titel, u'tage': tage, u'woerter': woerter})
    return kapitel, fehler


def bericht():
    kapitel, fehler = sammeln()
    besitzer = {}      # wem der Tag gehoert: dem Kapitel, in dem er anfaengt
    zuletzt = {}       # wer ihn zuletzt beansprucht hat, fuer die Nachbarschaft
    doppelt = []
    laeuft_weiter = []
    for kap in kapitel:
        for n in kap[u'tage']:
            hier = (kap[u'band'], kap[u'nr'])
            if n in besitzer:
                vorher = zuletzt[n]
                zuletzt[n] = hier
                # Ein Tag, der ueber eine Kapitelgrenze laeuft, ist der
                # Normalfall dieses Buches: der Galaabend steht in sechs
                # Kapiteln. Ein Tag in zwei NICHT benachbarten Kapiteln waere
                # ein Fehler.
                if vorher[0] == hier[0] and hier[1] - vorher[1] <= 1:
                    laeuft_weiter.append((n, vorher, hier))
                else:
                    doppelt.append((n, vorher, hier))
                # `besitzer` bleibt beim ersten. Ein Fortsetzungskapitel
                # uebernimmt den Tag nicht, sonst zeigt jeder Rueckblick auf
                # den eigenen Tag scheinbar nach vorn.
            else:
                besitzer[n] = hier
                zuletzt[n] = hier
    alle = sorted(besitzer)
    luecken = []
    if alle:
        for n in range(alle[0], alle[-1] + 1):
            if n not in besitzer:
                luecken.append(n)
    return kapitel, fehler, besitzer, doppelt, luecken, laeuft_weiter


def gruppen(ns):
    u"""[1,2,3,7,8] -> [(1,3),(7,8)]"""
    aus = []
    for n in sorted(ns):
        if aus and n == aus[-1][1] + 1:
            aus[-1][1] = n
        else:
            aus.append([n, n])
    return [tuple(x) for x in aus]


def schreiben(kapitel, fehler, besitzer, doppelt, luecken, laeuft_weiter):
    u"""erzeugt/REGISTER.md neu bauen. Erzeugte Datei, nie von Hand aendern."""
    z = []
    tage = sorted(besitzer)
    z.append(u'# Tagesregister')
    z.append(u'')
    z.append(u'**Erzeugt von `werkzeug/register.py`. Nicht von Hand bearbeiten.**')
    z.append(u'')
    z.append(u'Anker: Tag 1 = %s %d %s %d. %d Kapitel, %d belegte Erzaehltage, '
             u'Tag %d bis Tag %d.'
             % (WOCHENTAGE[TAG1.weekday()], TAG1.day, MONATE[TAG1.month - 1],
                TAG1.year, len(kapitel), len(tage), tage[0], tage[-1]))
    z.append(u'')
    z.append(u'Datumszeilen gegen den Kalender: **%s**.'
             % (u'%d Fehler' % len(fehler) if fehler else u'alle sauber'))
    for band, k, zeile, was in fehler:
        z.append(u'- `b%d ch%02d:%d` %s' % (band, k, zeile, was))
    z.append(u'')
    z.append(u'## Jeder erzaehlte Tag')
    z.append(u'')
    z.append(u'| Tag | Datum | Wochentag | Kapitel |')
    z.append(u'|---|---|---|---|')
    for n in tage:
        d = datum(n)
        b, k = besitzer[n]
        z.append(u'| %d | %d %s %d | %s | b%d ch%02d |'
                 % (n, d.day, MONATE[d.month - 1], d.year,
                    WOCHENTAGE[d.weekday()], b, k))
    z.append(u'')
    z.append(u'## Jedes Kapitel')
    z.append(u'')
    z.append(u'| Kapitel | Tage | Anzahl | Woerter | je Tag | Titel |')
    z.append(u'|---|---|---|---|---|---|')
    for kap in kapitel:
        t = kap[u'tage']
        st = u', '.join(u'%d' % a if a == b else u'%d bis %d' % (a, b)
                        for a, b in gruppen(t)) if t else u'-'
        z.append(u'| b%d ch%02d | %s | %d | %d | %s | %s |'
                 % (kap[u'band'], kap[u'nr'], st, len(t), kap[u'woerter'],
                    (u'%d' % (kap[u'woerter'] // len(t))) if t else u'-',
                    kap[u'titel']))
    z.append(u'')
    z.append(u'## Tage ueber eine Kapitelgrenze')
    z.append(u'')
    z.append(u'Der Normalfall dieses Buches. Der Galaabend steht in sechs '
             u'Kapiteln, das Essen am Tag 531 in drei.')
    z.append(u'')
    for n, a, b in laeuft_weiter:
        z.append(u'- Tag %d: b%d ch%02d nach b%d ch%02d' % (n, a[0], a[1], b[0], b[1]))
    if doppelt:
        z.append(u'')
        z.append(u'## Tage in nicht benachbarten Kapiteln')
        z.append(u'')
        z.append(u'**Das waere ein Fehler.**')
        z.append(u'')
        for n, a, b in doppelt:
            z.append(u'- Tag %d: b%d ch%02d und b%d ch%02d' % (n, a[0], a[1], b[0], b[1]))
    z.append(u'')
    ordner = os.path.join(WURZEL, u'erzeugt')
    if not os.path.isdir(ordner):
        os.makedirs(ordner)
    pfad = os.path.join(ordner, u'REGISTER.md')
    io.open(pfad, u'w', encoding=u'utf-8', newline=u'').write(u'\n'.join(z))
    print(u'erzeugt/REGISTER.md   %d Zeilen' % len(z))


def main():
    kapitel, fehler, besitzer, doppelt, luecken, laeuft_weiter = bericht()
    if u'--schreiben' in sys.argv:
        schreiben(kapitel, fehler, besitzer, doppelt, luecken, laeuft_weiter)
        return
    nur_luecken = u'--luecken' in sys.argv

    print(u'Tagesregister. Anker: Tag 1 = %s %d %s %d.'
          % (WOCHENTAGE[TAG1.weekday()], TAG1.day, MONATE[TAG1.month - 1],
             TAG1.year))
    tage = sorted(besitzer)
    print(u'%d Kapitel, %d Erzaehltage belegt, von Tag %d bis Tag %d (%s bis %s).'
          % (len(kapitel), len(tage), tage[0], tage[-1],
             datum(tage[0]).isoformat(), datum(tage[-1]).isoformat()))

    print(u'\n--- Datumszeilen gegen den Kalender: %s'
          % (u'%d Fehler' % len(fehler) if fehler else u'alle sauber'))
    for band, k, zeile, was in fehler:
        print(u'  b%d ch%02d:%d  %s' % (band, k, zeile, was))

    print(u'\n--- Tage in NICHT benachbarten Kapiteln (waere ein Fehler): %s'
          % (u'%d' % len(doppelt) if doppelt else u'keine'))
    for n, a, b in doppelt:
        print(u'  Tag %d: b%d ch%02d und b%d ch%02d' % (n, a[0], a[1], b[0], b[1]))
    print(u'--- Tage ueber eine Kapitelgrenze (Normalfall): %d' % len(laeuft_weiter))

    print(u'\n--- Nicht erzaehlte Tage im Bogen: %d von %d'
          % (len(luecken), tage[-1] - tage[0] + 1))
    if luecken:
        st = []
        for a, b in gruppen(luecken):
            st.append(u'%d' % a if a == b else u'%d-%d' % (a, b))
        print(u'  ' + u', '.join(st))

    if nur_luecken:
        return

    print(u'\n--- Kapitel, Tage, Woerter je Tag')
    for kap in kapitel:
        t = kap[u'tage']
        if not t:
            print(u'  b%d ch%02d  KEIN TAG   %5d W   %s'
                  % (kap[u'band'], kap[u'nr'], kap[u'woerter'], kap[u'titel'][:52]))
            continue
        st = u', '.join(u'%d' % a if a == b else u'%d-%d' % (a, b)
                        for a, b in gruppen(t))
        print(u'  b%d ch%02d  Tag %-11s %2d Tg %5d W  %5d W/Tag  %s'
              % (kap[u'band'], kap[u'nr'], st, len(t), kap[u'woerter'],
                 kap[u'woerter'] // len(t), kap[u'titel'][:46]))


if __name__ == u'__main__':
    main()
