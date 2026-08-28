# -*- coding: utf-8 -*-
u"""Jede Stelle, an der der Text einen Wochentag an ein Datum bindet.

Das ist die einzige Sorte Zeitangabe im Fliesstext, die ein Skript ohne
Urteil entscheiden kann: der Kalender weiss, welcher Tag der 29. April 2026
war, und der Satz behauptet es. Alles andere - "drei Wochen spaeter", "seit
dem Fruehjahr" - braucht einen Leser.

**Warum das eng gefasst ist.** Ein Wochentagsname allein ist keine
Behauptung. "I have been waiting on Monday since the twenty-first of
November" bindet nichts, und wer solche Zeilen einsammelt, bekommt eine
Liste, in der die echten Faelle untergehen. Geprueft werden nur Saetze, die
Datum und Wochentag ausdruecklich gleichsetzen.

Zwei Bezugsarten:

* **gebunden** - im Satz steht ein Datum, an das der Wochentag geheftet ist.
  Das Jahr kommt aus derselben Aufloesung wie in `datumsprobe.py`, also aus
  der Naehe zum Kapitel, nicht aus der Richtung des Satzes.
* **eigener Tag** - der Satz sagt "which is a Thursday" ohne Datum. Dann
  gilt der Tag des Kapitels, und das ist nur zulaessig, wenn das Kapitel
  genau einen Tag hat.

    python werkzeug/wochentag.py
    python werkzeug/wochentag.py --probe
"""
import contextlib
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
with contextlib.redirect_stdout(io.StringIO()):
    import register as REG                                 # noqa: E402
    import datumsprobe as DP                               # noqa: E402

TAGE = [u'Monday', u'Tuesday', u'Wednesday', u'Thursday', u'Friday',
        u'Saturday', u'Sunday']
WT = u'|'.join(TAGE)
D = DP.DATUM.pattern

# 1  "the ninth of March, which is a Monday"   /  ", which was a Monday"
GEBUNDEN_A = re.compile(r'(%s)\s*,?\s+which\s+(?:is|was)\s+an?\s+(%s)' % (D, WT), re.I)
# 2  "the ninth of March was a Monday"
GEBUNDEN_B = re.compile(r'(%s)\s+(?:is|was)\s+an?\s+(%s)' % (D, WT), re.I)
# 3  "Monday the ninth of March"  /  "on Monday, the ninth of March"
GEBUNDEN_C = re.compile(r'\b(%s)\s*,?\s+(%s)' % (WT, D), re.I)

# ohne Datum: der Satz heftet den Wochentag an den Tag, an dem er steht
EIGEN = re.compile(r'\bwhich\s+(?:is|was)\s+an?\s+(%s)\b' % WT, re.I)


def wochentag(d):
    return TAGE[d.weekday()]


def davor(tag, monat, letzter):
    u"""Das letzte Vorkommen von Tag und Monat vor dem Kapitel, auch
    ausserhalb des Handlungsfensters.

    Fuer die Wochentagsfrage ist Vorgeschichte kein Hindernis: der Kalender
    weiss auch, welcher Tag der 17. September 2025 war. `datumsprobe.py`
    laesst solche Faelle liegen, weil dort das ZIELKAPITEL gesucht wird und
    es keines gibt. Hier wird nur gerechnet.
    """
    import datetime
    for zurueck in range(0, 6):
        try:
            d = datetime.date(letzter.year - zurueck, monat, tag)
        except ValueError:
            continue
        if d <= letzter:
            return d
    return None


def aufloesen(zeile, roh, erster, letzter):
    u"""Ein Datum aus dem Satz auf einen Kalendertag ziehen."""
    m = DP.DATUM.search(roh)
    tag = DP.ORD[m.group(1).lower()]
    monat = DP.MONATE.index(m.group(2).lower()) + 1
    kand = DP.kandidaten(tag, monat)
    versatz = DP.jahresversatz(zeile)
    if versatz is not None:
        import datetime
        try:
            return datetime.date(letzter.year - versatz, monat, tag)
        except ValueError:
            return None
    rueck = bool(DP.RUECKBLICK.search(zeile)) and not DP.VORBLICK.search(zeile)
    if rueck and not [y for y in kand if y <= letzter]:
        return davor(tag, monat, letzter)
    if not kand:
        return davor(tag, monat, letzter) if rueck else None
    return DP.naechster(kand, erster, letzter,
                        bool(DP.RUECKBLICK.search(zeile)),
                        bool(DP.VORBLICK.search(zeile)))


def lauf(kaputt=None):
    aus = []
    for band, k, pfad, name in REG.kanon():
        zeilen = io.open(pfad, encoding='utf-8').read().split(u'\n')
        if kaputt and kaputt[0] == (band, k):
            zeilen = list(zeilen) + [u''] * kaputt[1]
            zeilen[kaputt[1] - 1] = kaputt[2]
        tage = []
        for e in REG.kopfzeilen(zeilen):
            if e[0]:
                tage.extend(e[0])
        if not tage:
            continue
        erster, letzter = REG.datum(min(tage)), REG.datum(max(tage))

        for i, z in enumerate(zeilen, 1):
            if REG.KOPF.match(z.strip()) or z.strip().startswith(u'#'):
                continue
            gefunden = []
            for rx, links in ((GEBUNDEN_A, True), (GEBUNDEN_B, True),
                              (GEBUNDEN_C, False)):
                for m in rx.finditer(z):
                    # Das Datum bringt zwei eigene Gruppen mit, darum liegt
                    # der Wochentag je nach Muster vorn oder hinten.
                    roh = m.group(1) if links else m.group(2)
                    tag = m.group(4) if links else m.group(1)
                    gefunden.append((roh, tag))
            for roh, tag in gefunden:
                d = aufloesen(z, roh, erster, letzter)
                if d is None:
                    continue
                aus.append((band, k, i, u'gebunden', roh, tag,
                            wochentag(d), d, z.strip()))
            if gefunden:
                continue
            if len(set(tage)) != 1:
                continue                    # mehrtaegig: kein eindeutiger Bezug
            for m in EIGEN.finditer(z):
                d = REG.datum(tage[0])
                aus.append((band, k, i, u'eigener Tag', u'-', m.group(1),
                            wochentag(d), d, z.strip()))
    return aus


if __name__ == u'__main__':
    if u'--probe' in sys.argv:
        # Jedes der drei Muster einmal falsch und einmal richtig. Der vierte
        # Oktober 2025 ist ein Samstag; b1 ch05 spielt in dessen Naehe, also
        # loest die Naehe auf dieses Jahr auf.
        MUSTER = [
            (u'A which-is', u'The fourth of October, which was a %s, held.'),
            (u'B war-ein',  u'The fourth of October was a %s, and he knew it.'),
            (u'C voran',    u'It happened on %s the fourth of October.'),
        ]
        fehlt = []
        for name, satz in MUSTER:
            def meldung(wt):
                return [t for t in lauf(((1, 5), 60, satz % wt))
                        if (t[0], t[1], t[2]) == (1, 5, 60)
                        and t[5].lower() != t[6].lower()]
            if not meldung(u'Tuesday'):
                fehlt.append(u'%s faengt den falschen nicht' % name)
            if meldung(u'Saturday'):
                fehlt.append(u'%s meldet den richtigen' % name)
        print(u'Gegenprobe: %s'
              % (u'alle drei Muster faengt den falschen und lassen den richtigen'
                 if not fehlt else u'LUECKE - ' + u'; '.join(fehlt)))
        sys.exit(1 if fehlt else 0)

    treffer = lauf()
    falsch = [t for t in treffer if t[5].lower() != t[6].lower()]
    print(u'%d Stellen binden einen Wochentag an einen Tag.\n' % len(treffer))
    for band, k, i, art, roh, gesagt, echt, d, z in treffer:
        zeichen = u'  ' if gesagt.lower() == echt.lower() else u'!!'
        print(u'%s b%d ch%02d:%-4d %-11s %s = %s%s'
              % (zeichen, band, k, i, art, d.isoformat(), gesagt,
                 u'' if gesagt.lower() == echt.lower()
                 else u'   ABER es ist ein %s' % echt))
        if zeichen == u'!!':
            print(u'      %s' % z[:170])
    print(u'\n=== falsche Wochentage: %d' % len(falsch))
