# -*- coding: utf-8 -*-
u"""Jede Altersangabe neben dem Tag, an dem sie faellt.

**Warum es dieses Skript gibt.** Am 28.08. ist Park Sang-hoon am
30. Dezember neunundfuenfzig gewesen und am 28. Juli davor sechzig. Fuenf
Monate, und niemand hat es gesehen - weil ein Alter richtig ist, wenn man es
schreibt, und stehenbleibt, waehrend die Szene sich im Kalender bewegt. Beim
Zusammenlegen und Umnummerieren von Band 2 ist diese Szene ans Jahresende
gerutscht und die Zahl ist mitgereist.

`doc/15-kalender.md` fuehrt eine Tabelle der Geburtstage. Die faengt den
Fall nicht: sie sagt, wann jemand aelter wird, aber sie legt die Angaben
nicht nebeneinander. Der Fehler ist nur sichtbar, wenn zwei Zahlen derselben
Figur mit ihren Tagen untereinander stehen.

**Die eine Pruefung, die ohne Urteil auskommt: ein Alter geht nie zurueck.**
Steht eine Figur an einem spaeteren Tag mit einer kleineren Zahl da, ist das
immer ein Fehler, ganz gleich, wo ihr Geburtstag liegt. Die zweite ist fast
so hart: zwischen zwei Angaben koennen nicht mehr Jahre liegen, als der
Kalender hergibt, plus eins fuer den Geburtstag dazwischen.

**Die erste Fassung hat am 28.08. geraten und musste zurueckgebaut werden.**
Sie nahm jeden Namen, der in derselben Zeile stand. Damit wurde *"a page
with Annie on it and a woman of eighty-one on it"* zu Annie mit einundachtzig
und *"not by my brother, not by Hana"* zu Hana mit dreissig. Neun Meldungen,
davon neun falsch. Eine solche Liste liest niemand zweimal.

**Drei Schranken sind daraus geworden:**

* Ein Name zaehlt nur, wenn er **ausserhalb der Anfuehrungszeichen** steht.
  Wer im Satz eines anderen erwaehnt wird, spricht nicht.
* *"a man of sixty"* wird gezaehlt und **nie zugeordnet**. Es gehoert
  niemandem, und geraten wird hier nicht.
* Rueckblickende Formen - *"since I was thirty"* - sind ausgeschlossen. Sie
  nennen ein Alter, das die Figur einmal hatte, nicht das, das sie hat.

    python werkzeug/alter.py
    python werkzeug/alter.py --alle    auch die ohne zuweisbaren Namen
    python werkzeug/alter.py --probe
"""
import contextlib
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.dirname(HIER)
sys.path.insert(0, HIER)
with contextlib.redirect_stdout(io.StringIO()):
    import register as REG                                # noqa: E402

EINER = u'''zero one two three four five six seven eight nine ten eleven twelve
thirteen fourteen fifteen sixteen seventeen eighteen nineteen'''.split()
ZEHNER = {u'twenty': 20, u'thirty': 30, u'forty': 40, u'fifty': 50,
          u'sixty': 60, u'seventy': 70, u'eighty': 80, u'ninety': 90}
WORT = u'|'.join(sorted(list(ZEHNER) + EINER, key=len, reverse=True))
ZAHL = u'(?:(?:%s)(?:-(?:%s))?)' % (WORT, u'|'.join(EINER[1:10]))

# Was aus einer Zahl eine Menge macht und kein Alter.
EINHEIT = (r'(?!\s*(?:years?|months?|weeks?|days?|hours?|minutes?|seconds?|'
           r'people|men|women|of them|per cent|million|billion|thousand|'
           r'trucks?|boxes|pages?|lots?|firms?|rooms?|times?|kilo|metres?|'
           r'seats?|places?|cards?|calls?|names?|lines?|entries|-odd))')

# Ein Alter, das die Figur JETZT hat. "I was" und "he was" fehlen mit
# Absicht: sie stehen fast immer in "since I was thirty".
JETZT = [re.compile(r'\bI am (%s)\b%s' % (ZAHL, EINHEIT), re.I),
         re.compile(r'\b(?:he|she) is (%s)\b%s' % (ZAHL, EINHEIT), re.I),
         re.compile(r'\bbeing (%s)\b%s' % (ZAHL, EINHEIT), re.I),
         re.compile(r'\bbe (%s)\b%s' % (ZAHL, EINHEIT), re.I),
         re.compile(r'\bturn(?:ed|ing|s)? (%s)\b%s' % (ZAHL, EINHEIT), re.I),
         re.compile(r'\baged (%s)\b%s' % (ZAHL, EINHEIT), re.I)]

# Zaehlbar, nie zuzuordnen.
ANONYM = re.compile(r'\ba (?:man|woman) of (%s)\b%s' % (ZAHL, EINHEIT), re.I)

ZITAT = re.compile(u'[“"][^”"]*[”"]')


def zahl(s):
    s = s.lower()
    if u'-' in s:
        a, b = s.split(u'-', 1)
        return ZEHNER.get(a, 0) + (EINER.index(b) if b in EINER else 0)
    if s in ZEHNER:
        return ZEHNER[s]
    return EINER.index(s) if s in EINER else None


def figuren():
    u"""Die Namen aus dem erzeugten Begegnungsregister.

    Erzeugt heisst: die Liste kann nicht davon abweichen, wer im Buch
    vorkommt. Eine von Hand gepflegte Namensliste haette genau das Problem,
    das dieses Skript sucht.
    """
    p = os.path.join(WURZEL, u'erzeugt', u'BEGEGNUNGEN.md')
    aus = []
    if not os.path.exists(p):
        return aus
    for z in io.open(p, encoding='utf-8').read().split(u'\n'):
        m = re.match(r'\|\s*([A-Z][^|]*?)\s*\|\s*\d+\s*\|', z)
        if m and m.group(1) != u'Figur':
            aus.append(m.group(1).strip())
    return aus


NAMEN = figuren()


def wer(zeile):
    u"""Genau ein bekannter Name ausserhalb der Anfuehrungszeichen."""
    draussen = ZITAT.sub(u' ', zeile)
    treffer = set()
    for n in NAMEN:
        kurz = n.split()[-1]
        if re.search(r'\b%s\b' % re.escape(n), draussen) or \
                (len(kurz) > 3 and re.search(r'\b%s\b' % re.escape(kurz), draussen)):
            treffer.add(n)
    return list(treffer)[0] if len(treffer) == 1 else None


def lauf(kaputt=None):
    mit, ohne = [], []
    for band, k, pfad, name in REG.kanon():
        zeilen = io.open(pfad, encoding='utf-8').read().split(u'\n')
        if kaputt and kaputt[0] == (band, k):
            zeilen = list(zeilen) + [u''] * kaputt[1]
            zeilen[kaputt[1] - 1] = kaputt[2]
        tag = None
        for i, z in enumerate(zeilen, 1):
            e = REG.kopfzeilen([z])
            if e and e[0][0]:
                tag = e[0][0][0]
            if tag is None or z.strip().startswith(u'#'):
                continue
            for m in ANONYM.finditer(z):
                a = zahl(m.group(1))
                if a and 16 <= a <= 99:
                    ohne.append((None, a, tag, band, k, i, z.strip()))
            for rx in JETZT:
                for m in rx.finditer(z):
                    a = zahl(m.group(1))
                    if a is None or not (16 <= a <= 99):
                        continue
                    vorn = z[max(0, m.start() - 30):m.start()].lower()
                    if re.search(r'\b(since|when|until|by the time)\b', vorn):
                        continue                      # ein frueheres Alter
                    f = wer(z)
                    (mit if f else ohne).append(
                        (f, a, tag, band, k, i, z.strip()))
    return mit, ohne


def widersprueche(mit):
    u"""Ein Alter, das zurueckgeht - oder schneller steigt als der Kalender."""
    aus, proFigur = [], {}
    for f, a, tag, band, k, i, z in mit:
        proFigur.setdefault(f, []).append((tag, a, band, k, i, z))
    for f in proFigur:
        liste = sorted(proFigur[f])
        for x in range(1, len(liste)):
            t0, a0 = liste[x - 1][0], liste[x - 1][1]
            t1, a1 = liste[x][0], liste[x][1]
            if a1 < a0:
                aus.append((f, u'geht zurueck', liste[x - 1], liste[x]))
            elif a1 - a0 > int((t1 - t0) / 365.25) + 1:
                aus.append((f, u'steigt zu schnell', liste[x - 1], liste[x]))
    return aus, proFigur


if __name__ == u'__main__':
    if u'--probe' in sys.argv:
        fehlt = []

        def melden(s1, s2):
            m1, _ = lauf(((1, 5), 60, s1))
            m2, _ = lauf(((1, 30), 60, s2))
            zus = [x for x in m1 if (x[3], x[4], x[5]) == (1, 5, 60)] + \
                  [x for x in m2 if (x[3], x[4], x[5]) == (1, 30, 60)]
            return widersprueche(zus)[0]

        A = u'"I am sixty," said Chairman Woo.'
        if not melden(A, u'"I am fifty-nine," said Chairman Woo.'):
            fehlt.append(u'Rueckgang nicht gemeldet')
        if melden(A, A):
            fehlt.append(u'Gleichstand gemeldet')
        if not melden(A, u'"I am seventy," said Chairman Woo.'):
            fehlt.append(u'Sprung nicht gemeldet')

        def einzeln(satz):
            m, o = lauf(((1, 5), 60, satz))
            return ([x for x in m if (x[3], x[4], x[5]) == (1, 5, 60)],
                    [x for x in o if (x[3], x[4], x[5]) == (1, 5, 60)])

        if einzeln(u'He was sixty years in that trade with Chairman Woo.')[0]:
            fehlt.append(u'"sixty years" als Alter gelesen')
        if einzeln(u'"I have done this since I was thirty," said Chairman Woo.')[0]:
            fehlt.append(u'"since I was thirty" als heutiges Alter gelesen')
        if einzeln(u'"Not by Chairman Woo, who is sixty," she said.')[0]:
            fehlt.append(u'Name innerhalb der Anfuehrungszeichen zugeordnet')
        m, o = einzeln(u'Chairman Woo watched a man of sixty cross the yard.')
        if m or not o:
            fehlt.append(u'"a man of sixty" wurde zugeordnet statt nur gezaehlt')
        if not NAMEN:
            fehlt.append(u'keine Namen geladen - build.py laufen lassen')

        print(u'Gegenprobe: %s'
              % (u'faengt Rueckgang und Sprung; laesst Gleichstand, Mengen, '
                 u'Rueckblicke, Zitatnamen und Namenlose'
                 if not fehlt else u'LUECKE - ' + u'; '.join(fehlt)))
        sys.exit(1 if fehlt else 0)

    mit, ohne = lauf()
    fehler, proFigur = widersprueche(mit)
    print(u'%d Namen aus dem Begegnungsregister.' % len(NAMEN))
    print(u'%d Altersangaben zuzuordnen, %d nicht.\n' % (len(mit), len(ohne)))

    for f in sorted(proFigur):
        liste = sorted(proFigur[f])
        if len(liste) < 2 and u'--alle' not in sys.argv:
            continue
        print(f)
        for tag, a, band, k, i, z in liste:
            print(u'    Tag %-4d %s   %2d   b%d ch%02d:%d'
                  % (tag, REG.datum(tag).strftime('%d %b %Y'), a, band, k, i))
        print(u'')

    print(u'=== Widersprueche: %d\n' % len(fehler))
    for f, art, a, b in fehler:
        print(u'!! %s: %s' % (f, art))
        for x in (a, b):
            print(u'   Tag %-4d %2d   b%d ch%02d:%d' % (x[0], x[1], x[2], x[3], x[4]))
            print(u'      %s' % x[5][:170])
        print(u'')

    if u'--alle' in sys.argv:
        print(u'=== nicht zuzuordnen, nur gezaehlt: %d\n' % len(ohne))
        for f, a, tag, band, k, i, z in sorted(ohne, key=lambda x: x[2]):
            print(u'   Tag %-4d %2d  b%d ch%02d:%d  %s'
                  % (tag, a, band, k, i, z[:115]))
