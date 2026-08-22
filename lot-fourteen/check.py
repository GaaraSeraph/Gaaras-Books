#!/usr/bin/env python3
"""
Lot Fourteen, mechanische Kapitelpruefung.

Aufruf:  python3 check.py                  prueft alle aktuellen Kapitel
         python3 check.py chapters/ch17_v12_1_en.md prueft eines

Prueft nur, was ohne Urteil pruefbar ist. Alles andere steht in craft/04-review.md
und muss gelesen werden.

Rueckgabewert 1, wenn ein Fehler gefunden wurde. Warnungen aendern ihn nicht.
"""
import re
import sys
import glob
import os
import datetime

NAME = re.compile(r"^ch(\d{2})_v(\d+)[._](\d+)_en\.md$")

# Tag 1 ist Samstag, der 4. Oktober
DAY1 = datetime.date(2025, 10, 4)
WD = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
MON = {10: "October", 11: "November", 12: "December", 1: "January", 2: "February"}
NUM = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen "
    "fourteen fifteen sixteen seventeen eighteen nineteen twenty".split())}
NUM.update({"thirty": 30, "forty": 40, "fifty": 50})

SELF_COMMENT = [
    "not going to pretend", "would like to be careful", "saying so before I say it",
    "am glad you called it", "I will say so",
]
TONE_LABEL = [
    "kept his voice", "kept her voice", "without any pressure anywhere",
    "let it be the size it was", "in no hurry at all",
]
QWORD = r"(?:Why|What|Who|When|Where|How|May I|Do you|Does|Can|Is|Are|Did|Would you|Then why|Have you|Will you)"


def words_to_int(s):
    s = s.strip().lower().replace("-", " ")
    if s.isdigit():
        return int(s)
    total = 0
    for part in s.split():
        if part in NUM:
            total += NUM[part]
    return total or None


def expected(day):
    d = DAY1 + datetime.timedelta(days=day - 1)
    return WD[(day - 1) % 7], d.day, MON[d.month]


def check(path):
    with open(path, encoding="utf-8") as fh:
        t = fh.read()
    # Kopfblock abschneiden: Titel, Versionszeile, Datumszeile zaehlen nicht als Prosa
    body = re.sub(r"^#.*$", "", t, flags=re.M)
    body = re.sub(r"^\*Lot Fourteen.*$", "", body, flags=re.M)
    body = re.sub(r"^\*Days? .*$", "", body, flags=re.M)
    errs, warns = [], []

    if re.search(r"[\u2014\u2013]", t):
        errs.append("Gedankenstrich gefunden. Nur Bindestriche.")

    for s in re.split(r'(?<=[.!?"])\s+', body):
        n = len(s.split())
        if n >= 40:
            errs.append(f"Satz mit {n} Woertern: {s.strip()[:70]}...")

    m = len(re.findall(r"\bMistress\b", t))
    if m > 5:
        errs.append(f'"Mistress" steht {m} mal. Hoechstens fuenf.')

    hits = re.findall(r".{0,45}\b(?:is not a|isn't a|it is not|It is not|That is not|was not a)\b.{0,45}", t)
    if len(hits) > 1:
        warns.append(f'"nicht X, sondern Y" moeglicherweise {len(hits)} mal. '
                     f"Litotes wie \"It is not nothing\" zaehlen nicht mit:")
        for h in hits:
            warns.append("           ..." + h.replace("\n", " ").strip() + "...")

    n = len(re.findall(r"would rather|'d rather", t))
    if n > 1:
        errs.append(f'"would rather" steht {n} mal. Hoechstens einmal.')

    for p in SELF_COMMENT:
        if t.count(p):
            warns.append(f'Selbstkommentar zur eigenen Redlichkeit: "{p}"')
    for p in TONE_LABEL:
        if t.count(p):
            warns.append(f'Beat etikettiert den Ton statt zu handeln: "{p}"')

    for q in re.findall(rf'^"{QWORD}[^?"]{{0,70}}\."$', t, flags=re.M):
        warns.append(f"Fragezeichen pruefen: {q}")

    days = []
    for mm in re.finditer(r"Days? ([A-Za-z0-9\- ]+?) · ([A-Za-z]+) (\d+)(?: ([A-Za-z]+))?", t):
        d = words_to_int(mm.group(1))
        if not d:
            continue
        days.append(d)
        wd, dd, mo = expected(d)
        if mm.group(2) != wd or int(mm.group(3)) != dd:
            errs.append(f"Datumszeile: Tag {d} ist {wd}, der {dd}. {mo}, im Text steht "
                        f"{mm.group(2)} {mm.group(3)}")
    if not days:
        warns.append("Keine Datumszeile gefunden.")

    n = len(t.split())
    if n < 2000 or n > 4300:
        warns.append(f"{n} Woerter, ausserhalb der Spanne 2000 bis 4300.")

    paste = os.path.join(os.path.dirname(os.path.dirname(path)) or ".", "paste",
                         os.path.basename(path).replace(".md", "_PASTE.txt"))
    if not os.path.exists(paste):
        warns.append("Keine Paste-Fassung. build.py laufen lassen.")

    fn = NAME.match(os.path.basename(path))
    hd = re.search(r"Version\s+(\d+)\.(\d+)\s", t)
    if fn and hd and (fn.group(2), fn.group(3)) != (hd.group(1), hd.group(2)):
        errs.append(f"Dateiname sagt v{fn.group(2)}.{fn.group(3)}, "
                    f"Kopfzeile sagt v{hd.group(1)}.{hd.group(2)}")

    return errs, warns


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        best = {}
        for p in glob.glob("chapters/ch*_en.md") or glob.glob("ch*_en.md"):
            m = NAME.match(os.path.basename(p))
            if not m:
                continue
            k, v = int(m.group(1)), (int(m.group(2)), int(m.group(3)))
            if k not in best or v > best[k][0]:
                best[k] = (v, p)
        files = [p for _, p in sorted(best.values(), key=lambda x: x[1])]

    bad = 0
    for f in sorted(files):
        errs, warns = check(f)
        if not errs and not warns:
            print(f"{os.path.basename(f):<24} sauber")
            continue
        print(f"\n{os.path.basename(f)}")
        for e in errs:
            print("  FEHLER   " + e)
        for w in warns:
            print("  hinweis  " + w)
        if errs:
            bad += 1

    print(f"\n{len(files)} Kapitel geprueft, {bad} mit Fehlern.")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
