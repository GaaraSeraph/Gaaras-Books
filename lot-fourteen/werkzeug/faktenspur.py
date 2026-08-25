# -*- coding: utf-8 -*-
"""
Faktenspur: was hat ein Stildurchgang wirklich angefasst.

Wozu. Ein Durchgang, der jede Aussage an `doc/12-stimmen.md` anpasst, schreibt
woertliche Rede um - und in woertlicher Rede stehen die Fakten. *"I am
fifty-nine"*, *"since I was twenty-six"*, *"it was Y who suggested the cards"*:
alles Stimme und alles Kanon. Danach das ganze Buch neu zu lesen kostet Tage.
Dieses Programm liest es nicht neu. Es vergleicht zwei Fassungen desselben
Kapitels und meldet nur, was sich an **Zahlen, Daten und Namen** bewegt hat.

Das geht nur, weil das Archiv alle alten Fassungen behaelt. Der Zustand vor dem
Durchgang muss nicht vorbereitet werden - er liegt schon da.

Was es NICHT kann: einen Satz beurteilen, dessen Zahlen gleich geblieben sind
und dessen Sinn sich gedreht hat. Dafuer gibt es `zuschreibung.py` und Lesen.
Siehe `doc/11-pruefen.md`.

Aufruf:
    python3 werkzeug/faktenspur.py                 lebende gegen vorige Fassung
    python3 werkzeug/faktenspur.py --seit <sha>    lebende gegen den Stand eines Commits
    python3 werkzeug/faktenspur.py --eichung       nur die Selbstprobe
"""
import io
import os
import re
import subprocess
import sys
import glob
from collections import Counter

ZAHLWORT = set(u"""one two three four five six seven eight nine ten eleven twelve thirteen
fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy
eighty ninety hundred thousand million billion half quarter
first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth thirteenth
fourteenth fifteenth sixteenth seventeenth eighteenth nineteenth twentieth thirtieth
january february march april june july august september october november december
monday tuesday wednesday thursday friday saturday sunday""".split())

# "may" ist als Monat unbrauchbar und als Modalverb haeufig - draussen lassen.

NAMEN = [u"Georgij", u"Annie", u"Jang", u"Seo", u"Baek", u"Ji-won", u"Eun-ju", u"Ku", u"Pyo",
         u"Woo", u"Hong", u"Kang", u"Hana", u"Sunwoo", u"Sang-hoon", u"Chae", u"Ye-rin",
         u"Sung-ho", u"Do-yun", u"Jeon", u"Hwang", u"Yeom", u"Ok", u"Byun", u"Byung-hee",
         u"Kwon", u"Cho", u"Choi", u"Sohn", u"Uhm", u"Shin", u"Yun", u"Tae-min", u"Bae",
         u"Ryu", u"Min-ho", u"Jae-won", u"Gil", u"Sim", u"Noh", u"Ahn", u"Im", u"Yeo",
         u"Oh", u"Gwak", u"Jung-hee", u"Dae-ho", u"Jae-sung", u"Mi-ja", u"Seo-yeon"]
NAMENSATZ = set(NAMEN)


def projektwurzel(start=None):
    d = os.path.dirname(os.path.abspath(start or __file__))
    for _ in range(4):
        if os.path.isdir(os.path.join(d, "chapters")) and os.path.isdir(os.path.join(d, "doc")):
            return d
        p = os.path.dirname(d)
        if p == d:
            break
        d = p
    return os.path.dirname(os.path.abspath(start or __file__))


def koerper(text):
    """Die vier Kopfzeilen weg. Sonst zaehlt die Versionsnummer als Fakt mit -
    eine fruehere Fassung hat genau daran 88 von 88 Kapiteln gemeldet."""
    return u"\n".join(text.split(u"\n")[4:])


def spur(text):
    """Zaehlt Zahlwoerter, Ziffern und Namen. Nichts sonst."""
    ws = re.findall(r"[A-Za-z][A-Za-z'-]*|\d+", koerper(text))
    aus = Counter()
    for w in ws:
        if w.isdigit():
            aus[w] += 1
        elif w.lower() in ZAHLWORT:
            aus[w.lower()] += 1
        elif w in NAMENSATZ:
            aus[w] += 1
    return aus


def unterschied(a, b):
    return sorted((w, a[w], b[w]) for w in set(a) | set(b) if a[w] != b[w])


def fassungen(ordner):
    per = {}
    for p in glob.glob(os.path.join(ordner, "ch*_v*_en.md")):
        b = os.path.basename(p)
        m = re.match(r"ch\d+_v(\d+)_(\d+)_en\.md", b)
        if not m:
            continue
        per.setdefault(b.split("_")[0], []).append(((int(m.group(1)), int(m.group(2))), p))
    return dict((c, sorted(v)) for c, v in per.items())


def lies(p):
    return io.open(p, encoding="utf-8").read()


def eichung(root):
    """Drei Proben an einem echten Kapitel.

    1. Dieselbe Fassung gegen sich selbst: nichts.
    2. Nur Interpunktion und Kontraktionen geaendert: nichts. Das ist der Fall,
       den ein Stildurchgang meistens macht, und er darf nicht laermen.
    3. Eine Zahl und ein Name geaendert: beides muss auffallen.
    """
    p = sorted(fassungen(os.path.join(root, "chapters")).values())[0][-1][1]
    t = lies(p)
    if unterschied(spur(t), spur(t)):
        return False, u"Fassung gegen sich selbst meldet etwas"
    stil = t.replace(u"do not", u"don't").replace(u"cannot", u"can't")
    stil = stil.replace(u" - ", u", ").replace(u"; ", u". ")
    if unterschied(spur(t), spur(stil)):
        return False, u"reine Stilaenderung schlaegt an"
    fakt = re.sub(r"\bfour\b", u"five", t, count=1)
    fakt = re.sub(r"\bAnnie\b", u"Hana", fakt, count=1)
    d = unterschied(spur(t), spur(fakt))
    if len(d) < 2:
        return False, u"geaenderte Zahl oder geaenderter Name faellt nicht auf"
    return True, os.path.basename(p)


def aus_git(root, sha, relpfad):
    try:
        roh = subprocess.check_output(["git", "show", "%s:%s" % (sha, relpfad)],
                                      cwd=root, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        return None
    return roh.decode("utf-8")


def vergleich_vorige(root):
    treffer = 0
    for band, d in ((u"B1", "chapters"), (u"B2", "chapters-2")):
        f = fassungen(os.path.join(root, d))
        for ch in sorted(f, key=lambda x: int(x[2:])):
            vs = f[ch]
            if len(vs) < 2:
                continue
            d2 = unterschied(spur(lies(vs[-2][1])), spur(lies(vs[-1][1])))
            if d2:
                treffer += 1
                print(u"%s %-5s v%d.%d -> v%d.%d" % (band, ch, vs[-2][0][0], vs[-2][0][1],
                                                     vs[-1][0][0], vs[-1][0][1]))
                for w, x, y in d2:
                    print(u"      %-14s %d -> %d" % (w, x, y))
    return treffer


def vergleich_seit(root, sha):
    treffer = 0
    vorher = {}
    for d in ("chapters", "chapters-2"):
        roh = subprocess.check_output(["git", "ls-tree", "--name-only", sha,
                                       "lot-fourteen/%s/" % d], cwd=os.path.dirname(root))
        for zeile in roh.decode("utf-8").split():
            m = re.search(r"(chapters(?:-2)?)/(ch\d+)_v(\d+)_(\d+)_en\.md$", zeile)
            if m:
                schluessel = (m.group(1), m.group(2))
                k = (int(m.group(3)), int(m.group(4)))
                if schluessel not in vorher or k > vorher[schluessel][0]:
                    vorher[schluessel] = (k, zeile)
    for band, d in ((u"B1", "chapters"), (u"B2", "chapters-2")):
        f = fassungen(os.path.join(root, d))
        for ch in sorted(f, key=lambda x: int(x[2:])):
            alt = vorher.get((d, ch))
            if not alt:
                print(u"%s %-5s neu seit %s - nicht vergleichbar, muss gelesen werden"
                      % (band, ch, sha[:7]))
                continue
            t_alt = aus_git(os.path.dirname(root), sha, alt[1])
            if t_alt is None:
                continue
            d2 = unterschied(spur(t_alt), spur(lies(f[ch][-1][1])))
            if d2:
                treffer += 1
                print(u"%s %-5s v%d.%d -> v%d.%d" % (band, ch, alt[0][0], alt[0][1],
                                                     f[ch][-1][0][0], f[ch][-1][0][1]))
                for w, x, y in d2:
                    print(u"      %-14s %d -> %d" % (w, x, y))
    return treffer


def main():
    root = projektwurzel()
    ok, was = eichung(root)
    print(u"Eichung: %s (%s)" % (u"bestanden" if ok else u"DURCHGEFALLEN", was))
    print(u"")
    if not ok:
        print(u"Kein Ergebnis. Ein ungeeichter Detektor meldet nichts.")
        return 2
    if u"--eichung" in sys.argv:
        return 0
    if u"--seit" in sys.argv:
        sha = sys.argv[sys.argv.index(u"--seit") + 1]
        n = vergleich_seit(root, sha)
        print(u"")
        print(u"%d Kapitel haben seit %s eine Zahl, ein Datum oder einen Namen bewegt."
              % (n, sha[:7]))
    else:
        n = vergleich_vorige(root)
        print(u"")
        print(u"%d Kapitel haben beim letzten Fassungssprung eine Zahl, ein Datum "
              u"oder einen Namen bewegt." % n)
    print(u"Jede Zeile ist zu lesen. Gleich gebliebene Zahlen heissen nicht, "
          u"dass der Sinn steht.")
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())
