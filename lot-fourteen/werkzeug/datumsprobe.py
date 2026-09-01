# -*- coding: utf-8 -*-
u"""Jedes ausdrueckliche Datum im Fliesstext gegen das Tagesregister.

**WARNUNG, am 28.08. durch die Gegenprobe aufgedeckt.** Die urspruengliche
Frage dieses Skripts war: blickt ein Kapitel auf ein Datum zurueck, das ein
**spaeteres** Kapitel erzaehlt? Diese Pruefung ist **nicht ausloesbar**,
solange die Kapitel in Tagesreihenfolge stehen, und das tun alle
Kanonkapitel ohne Ausnahme. Ein Rueckblick loest immer auf ein frueheres
Kapitel auf. Eine
Null aus dieser Richtung beweist nichts.

Was das Skript darum **wirklich** leistet:

* Es zaehlt die Datumsangaben und sortiert sie danach, ob sie ueberhaupt
  pruefbar sind.
* Es prueft, ob die Kapitelreihenfolge der Tagesreihenfolge folgt. **Sobald
  ein Kapitel umdatiert wird, wird die Pruefung oben scharf**, und dann meldet
  sie.
* Es listet die Rueckblicke, fuer die es im Handlungsfenster keine
  Vergangenheit gibt. Das sind die einzigen, die ein Skript herausheben kann,
  und sie muessen von Hand entschieden werden.

Alles Weitere ist Urteil: ob die Behauptung an einem Datum zu dem passt, was
das Kapitel dieses Tages erzaehlt. Das Register sagt, welches Kapitel das ist.
Mehr kann es nicht, und mehr soll hier nicht behauptet werden.

Verfahren je Fundstelle:

1. Tag und Monat aus dem Satz lesen.
2. Das Jahr in der Richtung erschliessen, in die der Satz zeigt.
3. Auf eine Tagnummer ziehen.
4. Im Register nachsehen, welches Kapitel diesen Tag erzaehlt.
5. Meldung, wenn ein **Rueckblick** auf ein Kapitel zeigt, das **spaeter**
   gelesen wird als das, in dem er steht.

Was nicht entscheidbar ist, wird gezaehlt und nicht behauptet: Daten vor Tag 1
sind Vorgeschichte, und Daten an nicht erzaehlten Tagen sind Ereignisse, die
neben der Buehne stattfinden. Beides ist normal.

    python werkzeug/datumsprobe.py
    python werkzeug/datumsprobe.py --probe    Gegenprobe mit eingebautem Fehler
    python werkzeug/datumsprobe.py --alle     auch die nicht entscheidbaren
"""
import datetime
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import register as REG                                    # noqa: E402

TAG1 = REG.TAG1
MONATE = [m.lower() for m in REG.MONATE]
MO = u'|'.join(MONATE)

ORD = {}
for _i, _w in enumerate(u'''first second third fourth fifth sixth seventh eighth
ninth tenth eleventh twelfth thirteenth fourteenth fifteenth sixteenth
seventeenth eighteenth nineteenth twentieth'''.split(), 1):
    ORD[_w] = _i
for _i, _w in enumerate(u'first second third fourth fifth sixth seventh eighth ninth'.split(), 21):
    ORD[u'twenty-' + _w] = _i
ORD[u'thirtieth'] = 30
ORD[u'thirty-first'] = 31
OD = u'|'.join(sorted(ORD, key=len, reverse=True))

DATUM = re.compile(r'the\s+(%s)\s+of\s+(%s)' % (OD, MO), re.I)

RUECKBLICK = re.compile(
    r'\b(was|were|had|has been|went|came|told|said|signed|asked|paid|gave|'
    r'wrote|read|stood|sat|did|happened|arrived|left|since|ago|last)\b', re.I)
VORBLICK = re.compile(
    r"\b(will|shall|going to|is to|are to|am to|next|due|expects?|"
    r"expected to|'ll|would like|wants? to|plans?)\b", re.I)

# Ein ausdruecklicher Jahresabstand hebt die Naehe auf. "the second of June,
# four years ago" steht in einem Kapitel, in dem es einen zweiten Juni gibt,
# und ohne diese Zeilen zieht die Aufloesung genau darauf und meldet einen
# Fund, den der Text nicht macht.
ZAHLWORT = {u'one': 1, u'two': 2, u'three': 3, u'four': 4, u'five': 5,
            u'six': 6, u'seven': 7, u'eight': 8, u'nine': 9, u'ten': 10,
            u'eleven': 11, u'twelve': 12, u'twenty': 20, u'thirty': 30}
JAHRE_HER = re.compile(r'\b(%s|\d+)\s+years?\s+ago\b'
                       % u'|'.join(ZAHLWORT), re.I)
VORLETZTES = re.compile(r'\bthe year before last\b', re.I)
LETZTES = re.compile(r'\blast (?:year|spring|summer|autumn|winter)\b', re.I)

def handlungsfenster_bis():
    u"""Letztes Datum aus den kanonischen Kapitelkoepfen."""
    tage = []
    for _band, _kapitel, pfad, _name in REG.kanon():
        with io.open(pfad, encoding='utf-8') as f:
            zeilen = f.readlines()
        for eintrag in REG.kopfzeilen(zeilen):
            if eintrag[0]:
                tage.extend(eintrag[0])
    return REG.datum(max(tage)) if tage else TAG1


FENSTER_BIS = handlungsfenster_bis()


def jahresversatz(zeile):
    u"""Wie viele Jahre zurueck weist der Satz ausdruecklich?

    None heisst: keine Angabe, die Naehe entscheidet. Eine Zahl heisst, dass
    genau dieses Jahr gemeint ist und kein anderes.
    """
    m = JAHRE_HER.search(zeile)
    if m:
        w = m.group(1).lower()
        return ZAHLWORT.get(w, int(w) if w.isdigit() else None)
    if VORLETZTES.search(zeile):
        return 2
    if LETZTES.search(zeile):
        return 1
    return None


def naechster(kand, erster, letzter, rueck, vorblick):
    u"""Der Kandidat, der dem Kapitel am naechsten liegt.

    Die Richtung des Satzes schraenkt ein, sie waehlt aber nicht aus. Wer
    nur nach Richtung waehlt, springt ueber einen Kandidaten hinweg, der
    einen Tag daneben liegt: b2 ch18 spielt am 30. April und nennt den
    29. April, und die alte Fassung loeste das auf den 29. April des
    naechsten Jahres auf, weil der Vortag kein erzaehlter Tag ist.
    """
    def abstand(d):
        if d < erster:
            return (erster - d).days
        if d > letzter:
            return (d - letzter).days
        return 0

    eng = kand
    if rueck and not vorblick:
        eng = [d for d in kand if d <= letzter] or kand
    elif vorblick and not rueck:
        eng = [d for d in kand if d >= erster] or kand
    return min(eng, key=abstand)


def tagnummer(d):
    return (d - TAG1).days + 1


def lesereihenfolge(band, nr):
    return (band, nr)


def sammeln():
    u"""Register: Tag -> (Band, Kapitel), und die Tage je Kapitel."""
    kapitel, fehler, besitzer, doppelt, luecken, weiter = REG.bericht()
    return besitzer


def kandidaten(tag, monat):
    aus = []
    for jahr in range(TAG1.year, FENSTER_BIS.year + 1):
        try:
            d = datetime.date(jahr, monat, tag)
        except ValueError:
            continue
        if TAG1 <= d <= FENSTER_BIS:
            aus.append(d)
    return aus


def lauf(kaputt=None):
    besitzer = sammeln()
    treffer = {u'vorgeschichte': 0, u'nicht erzaehlt': 0, u'geprueft': 0}
    meldungen = []
    unklar = []

    for band, k, pfad, name in REG.kanon():
        zeilen = io.open(pfad, encoding='utf-8').read().split(u'\n')
        if kaputt and kaputt[0] == (band, k):
            zeilen = list(zeilen)
            while len(zeilen) <= kaputt[1]:
                zeilen.append(u'')
            zeilen[kaputt[1] - 1] = kaputt[2]
        koepfe = REG.kopfzeilen(zeilen)
        tage = []
        for e in koepfe:
            if e[0]:
                tage.extend(e[0])
        if not tage:
            continue
        erster, letzter = REG.datum(min(tage)), REG.datum(max(tage))

        for i, z in enumerate(zeilen, 1):
            if REG.KOPF.match(z.strip()) or z.strip().startswith(u'#'):
                continue
            rueck = bool(RUECKBLICK.search(z)) and not VORBLICK.search(z)
            for m in DATUM.finditer(z):
                tag = ORD[m.group(1).lower()]
                mon = MONATE.index(m.group(2).lower()) + 1
                kand = kandidaten(tag, mon)
                if not kand:
                    treffer[u'vorgeschichte'] += 1
                    continue
                versatz = jahresversatz(z)
                if versatz is not None:
                    # Der Satz nennt den Abstand selbst. Dann gilt er, und
                    # nicht die Naehe. Faellt das Jahr aus dem Fenster, ist es
                    # Vorgeschichte und keine Fundstelle.
                    ziel = [d for d in kand
                            if letzter.year - d.year == versatz
                            or erster.year - d.year == versatz]
                    if not ziel:
                        treffer[u'vorgeschichte'] += 1
                        continue
                    d = ziel[0]
                elif rueck and not [x for x in kand if x <= letzter]:
                    # Rueckblick auf einen Monatstag, den es vor diesem Kapitel
                    # im Handlungsfenster nicht gibt. Das ist entweder
                    # Vorgeschichte oder ein Fehler, und **das entscheidet kein
                    # Skript**. Wird aufgelistet, nicht gezaehlt als sauber.
                    unklar.append((band, k, i, m.group(0), z.strip()))
                    continue
                else:
                    # Die ROHEN Richtungen, nicht `rueck`. Ein Satz kann
                    # beides tun - "On the eighth of December I said this,
                    # and I am going to say it again now" - und dann darf
                    # keine Richtung gewinnen, sonst zieht der Vorwaertsteil
                    # ein Datum aus dem Vorjahr ins naechste.
                    d = naechster(kand, erster, letzter,
                                  bool(RUECKBLICK.search(z)),
                                  bool(VORBLICK.search(z)))
                n = tagnummer(d)
                if n not in besitzer:
                    treffer[u'nicht erzaehlt'] += 1
                    continue
                treffer[u'geprueft'] += 1
                qb, qk = besitzer[n]
                if rueck and lesereihenfolge(qb, qk) > lesereihenfolge(band, k):
                    meldungen.append((band, k, i, m.group(0), n, d, qb, qk,
                                      z.strip()))
    return treffer, meldungen, unklar


def chronologie(tausch=None):
    u"""Stehen die Kapitel in Tagesreihenfolge? Davon haengt ab, ob die
    Rueckblick-Pruefung ueberhaupt ausloesen kann.

    `tausch` setzt fuer die Gegenprobe einem Kapitel einen anderen Tag vor,
    ohne eine Datei anzufassen.
    """
    kapitel = REG.bericht()[0]
    folge = [(k[u'band'], k[u'nr'], min(k[u'tage'])) for k in kapitel if k[u'tage']]
    if tausch:
        folge = [(b, n, tausch.get((b, n), t)) for b, n, t in folge]
    return [(folge[i - 1], folge[i]) for i in range(1, len(folge))
            if folge[i][2] < folge[i - 1][2]]


if __name__ == u'__main__' and u'--probe' in sys.argv:
    # **Der Riegel `__main__` ist nicht Kosmetik.** Ohne ihn lief dieser Block
    # auch beim IMPORT, und weil `wochentag.py` und `spanne.py` dieses Modul
    # unter stummgeschalteter Ausgabe einlesen, beendete ihre eigene
    # Gegenprobe sich hier - lautlos, mit Rueckgabewert 0. Beide meldeten
    # daraufhin nichts und sahen aus, als waeren sie durchgelaufen. Am 28.08.
    # aufgefallen, weil eine Probe ploetzlich gar nichts mehr ausgab.
    #
    # Die alte Gegenprobe war wertlos und hat das am 28.08. auch gezeigt: sie
    # schob b1 ch05 einen Rueckblick auf den neunten Dezember unter und
    # erwartete eine Meldung. Es gibt aber im Fenster keinen neunten Dezember
    # VOR ch05, und damit ist der Fall von echter Vorgeschichte nicht zu
    # unterscheiden. Kein Skript kann das entscheiden, und die Probe hat nie
    # etwas anderes bewiesen, als dass sie nicht ausloest.
    #
    # Geprueft wird jetzt, was wirklich traegt.
    fehlt = []

    # A: Die Reihenfolgepruefung. Sie ist der Waechter, der die
    # Rueckblick-Pruefung ueberhaupt erst scharf machen wuerde. Ein Kapitel
    # wird umdatiert, und sie muss das melden.
    if not chronologie({(1, 5): 400}):          # Tagnummern, keine Daten
        fehlt.append(u'A: umdatiertes Kapitel nicht gemeldet')

    # B: Die Naehe schlaegt die Richtung. b2 ch18 spielt am 30. April und
    # nennt den 29. April. Bis zum 28.08. loeste das auf den 29. April des
    # Folgejahres auf, weil der Vortag kein erzaehlter Tag ist.
    tag = datetime.date(2026, 4, 30)
    if naechster(kandidaten(29, 4), tag, tag, False, False) \
            != datetime.date(2026, 4, 29):
        fehlt.append(u'B: Vortag wird uebersprungen')

    # B2: Ein Satz, der zurueck- UND vorausblickt, darf keiner Richtung
    # folgen. b1 ch32 spielt am 22. Dezember 2025 und sagt "On the eighth of
    # December I said this ... I am going to say it again now". Bis zum
    # 28.08. gewann "going to", und das Datum sprang ins Jahr darauf.
    dez = datetime.date(2025, 12, 22)
    if naechster(kandidaten(8, 12), dez, dez, True, True) \
            != datetime.date(2025, 12, 8):
        fehlt.append(u'B2: Satz mit beiden Richtungen folgt einer davon')

    # C: Ein ausdruecklicher Jahresabstand hebt die Naehe wieder auf, sonst
    # zieht "the second of June, four years ago" auf den zweiten Juni im Buch.
    if jahresversatz(u'It was the second of June, four years ago, and') != 4:
        fehlt.append(u'C: "four years ago" nicht erkannt')
    if jahresversatz(u'a woman wrote to you by name last spring') != 1:
        fehlt.append(u'C: "last spring" nicht erkannt')
    if jahresversatz(u'He came in at the far end.') is not None:
        fehlt.append(u'C: Jahresabstand erfunden, wo keiner steht')

    print(u'Gegenprobe: %s' % (u'alle drei greifen' if not fehlt
                               else u'LUECKE - ' + u'; '.join(fehlt)))
    sys.exit(1 if fehlt else 0)


if __name__ == u'__main__':
    # Auch der Bericht gehoert hinter den Riegel. Vorher lief die ganze
    # Auswertung bei jedem Import mit, und die einlesenden Skripte mussten
    # die Ausgabe wegdruecken - was dann auch den Abbruch oben verdeckte.
    treffer, meldungen, unklar = lauf()
    verstoesse = chronologie()
    print(u'Kapitel in Tagesreihenfolge: %s'
          % (u'ja, alle' if not verstoesse
             else u'NEIN, %d Sprung(e) zurueck' % len(verstoesse)))
    for a, b in verstoesse:
        print(u'  b%d ch%02d (ab Tag %d) vor b%d ch%02d (ab Tag %d)'
              % (a[0], a[1], a[2], b[0], b[1], b[2]))
    if not verstoesse:
        print(u'  Damit ist die Pruefung "Rueckblick auf ein spaeteres Kapitel"'
              u' nicht ausloesbar.\n  Sie wird scharf, sobald ein Kapitel'
              u' umdatiert wird.')
    print(u'')

    gesamt = sum(treffer.values())
    print(u'%d ausdrueckliche Datumsangaben im Fliesstext.\n' % gesamt)
    print(u'  %4d entscheidbar: der Tag steht im Register' % treffer[u'geprueft'])
    print(u'  %4d vor Tag 1: Vorgeschichte, nicht pruefbar'
          % treffer[u'vorgeschichte'])
    print(u'  %4d an einem nicht erzaehlten Tag: neben der Buehne, nicht pruefbar'
          % treffer[u'nicht erzaehlt'])
    print(u'  %4d Rueckblick ohne Vergangenheit im Fenster: von Hand ansehen'
          % len(unklar))

    print(u'\n=== FEHLER: Rueckblick auf ein spaeter erzaehltes Kapitel: %d\n'
          % len(meldungen))
    for band, k, i, roh, n, d, qb, qk, z in meldungen:
        print(u'b%d ch%02d:%d  "%s" = Tag %d, %s'
              % (band, k, i, roh, n, d.isoformat()))
        print(u'    erzaehlt wird dieser Tag erst in b%d ch%02d' % (qb, qk))
        print(u'    %s\n' % z[:180])

    print(u'=== NICHT ENTSCHEIDBAR: Vorgeschichte oder Fehler: %d\n' % len(unklar))
    for band, k, i, roh, z in unklar:
        print(u'b%d ch%02d:%d  "%s"' % (band, k, i, roh))
        print(u'    %s\n' % z[:180])
