#!/usr/bin/env python3
"""heft.py - wird ins Heft geschrieben, oder wird etwas herausgeholt.

**Der Befund, der das noetig gemacht hat** (`doc/23-kuerzen.md`): Georgij fuehrt
das ganze Buch hindurch ein Notizbuch, und er schreibt hinein. Der Autor am
26.08.:

> *Wir suchen hier nach einem Mann, der nichts hinterlaesst, und diese Spuren
> zusammenzufassen ist legitim. Es fasst es fuer den Leser zusammen. Diese
> Notizen sollten aber irgendwann verwendet werden fuer die Detektivarbeit.*

**Genau das ist die Messung.** Nicht wie oft das Heft vorkommt, sondern das
Verhaeltnis: wie oft wird abgelegt, und wie oft wird geholt. Der Leser sieht
sonst ein Konto wachsen, von dem nie abgehoben wird, und deshalb fuehlt sich
die Arbeit nutzlos an, obwohl sie es nicht ist.

    python3 heft.py            das Verhaeltnis je Kapitel
    python3 heft.py --stellen  jede Fundstelle mit Zeile

**Die Grenze:** das Skript liest Formulierungen und nicht Absichten. Ein
*"he wrote it down"* ist sicher ein Ablegen; ein *"he read it again"* kann ein
Holen sein oder nur ein Blick. Die Spalte HOLEN ist deshalb eine Kandidatenliste
und keine Zaehlung, und jede Stelle wird von Hand angesehen.
"""
import os
import re
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ablegen: er schreibt etwas hinein.
ABLEGEN = re.compile(
    r'\bwrote (it|them|that|the|one|two|three|four|it down|all of it)\b'
    r'|\bwrote .{0,40}\bin (the|his) (book|notebook)\b'
    r'|\bin the book\b(?![a-z])'
    r'|\bput (it|that) in the (book|notebook)\b'
    r'|\bnotebook\b.{0,30}\b(shut|closed|away)\b', re.I)

# Holen: er nimmt heraus, was er abgelegt hat, und es tut etwas.
HOLEN = re.compile(
    r'\b(read|reads|re-read|went back to|looked up|turned back to|took out|'
    r'got out|opened) (his own|the|his) ?(notebook|book|four lines|own lines|'
    r'earlier|entries|pages?)\b'
    r'|\bhis own (four )?lines\b'
    r'|\bfrom (January|the beginning) forward\b'
    r'|\bas a document rather than as a source\b'
    # Das Holen steht im Buch oefter als Handlung da und nicht als Verb:
    # "open the notebook at a page that was already full", "opened it on that
    # table, at the January pages". Ein Detektor, der nur seine eigenen
    # Formulierungen findet, misst den Autor und nicht das Buch.
    r'|\bopen(ed)? (the |that |his )?(note)?book\b(?!.{0,20}\b(and wrote|to write)\b)'
    r'|\bat the January pages\b'
    # Am 30.08. ergaenzt, weil b3 ch01 eine Entnahme enthaelt, die keines
    # der bisherigen Muster gesehen hat: er holt ein altes Heft und
    # schlaegt eine datierte Seite auf. Ein Detektor, der nur die
    # Formulierungen von Band 1 kennt, misst den alten Text.
    r'|\bwent and got (a|the|his) (note)?book\b'
    r'|\bfound the page for\b'
    r'|\bback to that page\b'
    # Im Englischen darf das Partikel hinter das Objekt: *took the
    # notebook out*. Das Muster oben verlangte *took out the notebook*
    # und hat die haeufigere Stellung nicht gesehen.
    r'|\b(took|got) (the|his|it) (note)?book? ?out\b'
    r'(?!.{0,30}\b(and wrote|to write|and did not open)\b)'
    r'|\ba page that was already full\b', re.I)


def kapitel():
    aus = []
    for ordner, band in (("chapters", "b1"), ("chapters-2", "b2"), ("chapters-3", "b3")):
        pfad = os.path.join(WURZEL, ordner)
        if not os.path.isdir(pfad):
            continue
        neuste = {}
        for name in sorted(os.listdir(pfad)):
            m = re.match(r"ch(\d\d)_v(\d+)_(\d+)_en\.md$", name)
            if m:
                num = int(m.group(1))
                ver = (int(m.group(2)), int(m.group(3)))
                if num not in neuste or ver > neuste[num][0]:
                    neuste[num] = (ver, name)
        for num in sorted(neuste):
            with open(os.path.join(pfad, neuste[num][1]), encoding="utf-8") as f:
                aus.append(("%s %02d" % (band, num), neuste[num][1], f.read()))
    return aus


def lauf(stellen=False):
    ab_gesamt = hol_gesamt = 0
    ab_kap = hol_kap = 0
    zeilen = []
    for marke, datei, text in kapitel():
        a = h = 0
        for nr, zeile in enumerate(text.split("\n"), 1):
            for regex, art in ((ABLEGEN, 'ablegen'), (HOLEN, 'holen')):
                m = regex.search(zeile)
                if not m:
                    continue
                if art == 'ablegen':
                    a += 1
                else:
                    h += 1
                if stellen:
                    zeilen.append((marke, nr, art, zeile.strip()[:110]))
        ab_gesamt += a
        hol_gesamt += h
        if a:
            ab_kap += 1
        if h:
            hol_kap += 1
        if a or h:
            print("  %-7s  ablegen %2d   holen %2d %s"
                  % (marke, a, h, "  <== HOLT" if h else ""))

    print("\n  Ablegen: %d Stellen in %d Kapiteln" % (ab_gesamt, ab_kap))
    print("  Holen:   %d Stellen in %d Kapiteln" % (hol_gesamt, hol_kap))
    if hol_gesamt:
        print("\n  Verhaeltnis %.1f zu 1." % (float(ab_gesamt) / hol_gesamt))
    print("\n  **Ein Heft, in das nur hineingeschrieben wird, ist eine Bilanz.**")
    print("  Was es zu einem Werkzeug macht, ist die Stelle, an der etwas")
    print("  herausgeholt wird und die Antwort schon seit Monaten darin stand.")

    if stellen:
        print()
        for marke, nr, art, z in zeilen:
            print("  %-7s Z%-4d %-8s %s" % (marke, nr, art, z))
    return 0


if __name__ == "__main__":
    sys.exit(lauf("--stellen" in sys.argv))
