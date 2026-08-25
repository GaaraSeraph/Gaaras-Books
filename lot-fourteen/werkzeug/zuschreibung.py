# -*- coding: utf-8 -*-
"""
zuschreibung.py - sucht Zuschreibungsfehler: eine Tat, ein Gefuehl oder ein
Satz, der der falschen Person zugeschrieben ist.

    python3 zuschreibung.py --eichung     nur die Selbstpruefung
    python3 zuschreibung.py               Eichung, dann das ganze Buch

WARUM ES DIESES SKRIPT GIBT

Am 25.08. hat der Autor zwei Fehler gefunden, die check.py nicht sehen kann,
weil beide grammatisch, kalendarisch und zahlenmaessig einwandfrei sind:

  Band 2, Kapitel 38, Erzaehlung:
      "But Yeom sat at that table eleven months ago and lost forty thousand
       won at cards he does not remember agreeing to play."
  Achtzig Zeilen vorher, in woertlicher Rede, Sang-hoon:
      "I remember losing forty thousand won at cards I do not remember
       agreeing to play."

Dieselbe seltene Sache, zwei verschiedene Maenner. Der Absatz hob damit auch
die Schlussfolgerung des eigenen Kapitels auf, dass Y nicht Yeom ist.

WIE MAN AUS EINEM FUND EINEN STREIFZUG MACHT

  1. Der Fund ist ein Exemplar einer Klasse. Nicht reparieren und weitergehen,
     sondern fragen: wovon ist das ein Fall?
  2. Die Klasse bekommt eine mechanische Signatur.
  3. **Der Detektor wird gegen das bekannte Exemplar geeicht.** Feuert er dort
     nicht, ist er wertlos, egal wie klug er aussieht. Dieser Schritt ist der,
     den man auslaesst, und er ist der einzige, der etwas beweist.
  4. Erst dann laeuft er ueber alles - und ein leeres Ergebnis ist dann ein
     Ergebnis und keine Ausrede.

Die Eichung hier hat drei Anlaeufe gebraucht:
  - Fassung 1 nahm die Namen aus dem Satz. Sie fand den Fehler nicht, weil die
    eine Haelfte in woertlicher Rede steht und dort kein Name im Satz steht.
  - Fassung 2 nahm ein Fenster von Saetzen. Sie fand ihn immer noch nicht, weil
    Georgij in jedem Fenster steht und der Schnitt nie leer ist.
  - Fassung 3 fand die eigentliche Signatur:
        dieselbe seltene Wortfolge steht einmal in der ICH-FORM und einmal mit
        einem NAMEN daran.
    Genau so sieht der Fehler aus, und sonst sieht fast nichts so aus.
"""
import io, os, re, sys
from collections import defaultdict

NAMES = ["Georgij", "Annie", "Jang", "Mrs Seo", "Baek", "Ji-won", "Eun-ju", "Mr Ku", "Mr Pyo",
         "Woo", "Hong", "Kang", "Hana", "Sunwoo", "Sang-hoon", "Chae", "Ye-rin", "Sung-ho",
         "Do-yun", "Jeon", "Hwang", "Yeom", "Mr Ok", "Byun", "Nam Byung-hee", "Kwon", "Cho",
         "Choi", "Sohn", "Uhm", "Shin", "Yun", "Tae-min", "Bae", "Ryu", "Min-ho", "Jae-won",
         "Gil", "Sim", "Noh", "Mrs Ahn", "Mr Im", "Yeo", "Dr Oh", "Mrs Jeon", "Mrs Gwak"]

POV = set(["Georgij"])

STOP = set("""a an the and or but if of to in on at by for with from as is was are were be been
being it its he she they them him her his their this that these those there here not no nor so
than then when while which who whom whose what where why how all any both each few more most
other some such only own same too very can will just should now i you we me my your our said
one two three four five six seven eight nine ten had has have do does did done would could
about after again against because before between into over under up down out off""".split())

SPEAK = re.compile(r"(?:said|says|asked)\s+([A-Z][A-Za-z-]+(?:\s+[A-Z][A-Za-z-]+)?)"
                   r"|([A-Z][A-Za-z-]+(?:\s+[A-Z][A-Za-z-]+)?)\s+(?:said|says|asked)")
_WORD = {}


def projektwurzel(start=None):
    """Das Projektverzeichnis finden statt es anzunehmen.

    Die Skripte lagen bis zum 25.08. neben chapters/ und haben ihre Wurzel aus
    dem eigenen Dateipfad abgeleitet. Seit sie in werkzeug/ liegen, geht das
    nicht mehr. Statt eine feste Ebene hochzugehen, wird nach oben gesucht, bis
    ein Verzeichnis chapters/ UND doc/ enthaelt - dann laufen sie von ueberall.
    """
    import os
    d = os.path.dirname(os.path.abspath(start or __file__))
    for _ in range(4):
        if os.path.isdir(os.path.join(d, "chapters")) and os.path.isdir(os.path.join(d, "doc")):
            return d
        p = os.path.dirname(d)
        if p == d:
            break
        d = p
    return os.path.dirname(os.path.abspath(start or __file__))



def sentences(text):
    body = "\n".join(text.split("\n")[4:])
    body = body.replace("---", " ").replace("* * *", " ")
    return [p.strip() for p in re.split(r"(?<=[.!?])\s+", body) if len(p.strip()) > 25]


def names_in(s):
    out = set()
    for n in NAMES:
        if n not in _WORD:
            _WORD[n] = re.compile(r"(?<![A-Za-z-])" + re.escape(n) + r"(?![A-Za-z-])")
        if _WORD[n].search(s):
            out.add(n)
    return out - POV


def shingles(s, k):
    w = re.findall(r"[a-z][a-z'-]+", s.lower())
    return [" ".join(w[i:i + k]) for i in range(len(w) - k + 1)
            if sum(1 for x in w[i:i + k] if x in STOP) <= k - 2]


def speaker_near(sents, i, back=6):
    for j in range(i, max(-1, i - back), -1):
        m = SPEAK.search(sents[j])
        if m:
            nm = (m.group(1) or m.group(2)).split()[-1]
            for n in NAMES:
                if n.split()[-1] == nm:
                    return set([n]) - POV
    return set()


def suchen(paths, k=5, max_chapters=2):
    """Dieselbe seltene Wortfolge einmal in der Ich-Form, einmal mit Namen."""
    per = dict((p, sentences(io.open(p, encoding="utf-8").read())) for p in paths)
    corpus = defaultdict(set)
    for p, sents in per.items():
        for s in sents:
            for g in set(shingles(s, k)):
                corpus[g].add(p)
    out = []
    for p, sents in per.items():
        where = defaultdict(list)
        for i, s in enumerate(sents):
            for g in set(shingles(s, k)):
                where[g].append(i)
        for g, idxs in where.items():
            if len(idxs) < 2 or len(corpus[g]) > max_chapters:
                continue
            ich, named = [], []
            for i in idxs:
                own = names_in(sents[i])
                if own:
                    named.append((i, sorted(own)))
                elif re.search(r"\bI\b", sents[i]):
                    ich.append((i, sorted(speaker_near(sents, i))))
            if ich and named:
                out.append((p, g, ich, named, sents))
    return out


def live(d):
    best = {}
    for fn in os.listdir(d):
        m = re.match(r"ch(\d+)_v(\d+)_(\d+)_en\.md$", fn)
        if not m:
            continue
        ch, a, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if ch not in best or (a, b) > best[ch][0]:
            best[ch] = ((a, b), os.path.join(d, fn))
    return [best[c][1] for c in sorted(best)]


def eichung(root):
    """Der Detektor muss den bekannten Fund finden, sonst meldet er nichts."""
    probe = os.path.join(root, "chapters-2", "ch38_v2_0_en.md")
    if not os.path.exists(probe):
        print("  EICHUNG UEBERSPRUNGEN: das Belegexemplar %s ist nicht mehr da." % probe)
        print("  Ohne Eichung ist jedes Ergebnis dieses Skripts wertlos.")
        return False
    treffer = [g for _, g, _, _, _ in suchen([probe])]
    ok = any("forty thousand won at cards" in g or "remember agreeing to play" in g for g in treffer)
    print("  Eichung an Band 2, Kapitel 38 (Fassung vor der Korrektur): %s" % ("bestanden" if ok else "DURCHGEFALLEN"))
    for g in treffer:
        print("      gefunden: %s" % g)
    return ok


if __name__ == "__main__":
    root = projektwurzel()
    print("Zuschreibung")
    bestanden = eichung(root)
    if "--eichung" in sys.argv:
        sys.exit(0 if bestanden else 1)
    if not bestanden:
        print("\n  Der Detektor findet den Fehler nicht mehr, den er finden koennen muss.")
        print("  Es wird nichts gemeldet, weil ein Nichtfund jetzt nichts bedeutet.")
        sys.exit(1)
    files = live(os.path.join(root, "chapters")) + live(os.path.join(root, "chapters-2"))
    print("\n  %d Kapitel im Lauf." % len(files))
    hits = suchen(files)
    print("  %d Stellen zum Nachsehen.\n" % len(hits))
    for p, g, ich, named, sents in hits:
        print("%s   >>> %s" % (os.path.basename(p), g))
        for i, sp in ich:
            print("   ICH  (%s)  %s" % (",".join(sp) or "?", sents[i][:110]))
        for i, ns in named:
            print("   NAME (%s)  %s" % (",".join(ns), sents[i][:110]))
        print()
