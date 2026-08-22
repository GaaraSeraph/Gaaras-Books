#!/usr/bin/env python3
"""
Transmigration into Freedom, mechanische Kapitelpruefung.

Aufruf:  python3 check.py                   prueft alle Kapitel
         python3 check.py chapters/chNN-...  prueft eines
         python3 check.py --baseline         schreibt die Basislinie neu
         python3 check.py --ratchet          Rueckgabewert 1 nur bei Verschlechterung

Uebernommen von lot-fourteen, wo die Regeln autorenweit gelten: Bandwurmsaetze,
die DiGiorno-Abneigung ("not X, but Y"), "would rather", Gedankenstriche,
Fragezeichen-Verdacht, Ton-Etikett-Beats. Buch-spezifisch ergaenzt: KEIN Markdown
im Prosatext (nur die H1-Titelzeile). Entfallen sind die LF-Spezifika, die hier
nicht gelten: Oktober-Kalender/Datumszeilen, "Mistress"-Limit, Versions-Dateinamen.

Nicht mechanisch pruefbar und darum NICHT hier, sondern in docs/ + CLAUDE.md:
der Held luegt nie, und die Nachvollziehbarkeit der Inhalte.

Die Sperrklinke: mit --ratchet meldet check.py nur, wenn ein Kapitel MEHR Fehler
hat als in .check-baseline vermerkt. Altlast geduldet, Neuverschuldung nicht.

Rueckgabewert 1, wenn ein Fehler gefunden wurde. Warnungen aendern ihn nicht.
"""
import re
import sys
import glob
import os

NAME = re.compile(r"^ch(\d{2})-.+\.md$")
MAXWORDS = 2500

SELF_COMMENT = [
    "not going to pretend", "would like to be careful", "saying so before I say it",
    "am glad you called it", "I will say so",
]
TONE_LABEL = [
    "kept his voice", "kept her voice", "without any pressure anywhere",
    "let it be the size it was", "in no hurry at all",
]
QWORD = r"(?:Why|What|Who|When|Where|How|May I|Do you|Does|Can|Is|Are|Did|Would you|Then why|Have you|Will you)"


def check(path):
    with open(path, encoding="utf-8") as fh:
        t = fh.read()
    # Titelzeile (H1) vom Prosatext trennen; nur die Prosa wird auf Markdown geprueft.
    _title, _sep, body = t.partition("\n\n")
    errs, warns = [], []

    if re.search(r"[—–]", t):
        errs.append("Gedankenstrich gefunden. Nur Bindestriche.")

    # Continuity-Falle aus der Bibel: Attribute sind nur STR/DEX/CON/INT/WIS.
    # Es gibt KEIN Charisma, Glueck oder Aussehen (story-bible S2). Watchlist der
    # verbotenen Namen, nicht generisches Raten -> ein Rueckfall faellt auf,
    # harmlose Woerter nicht.
    ma = re.search(r"\b(CHA|Charisma|LUK|LUCK|Luck|APP|Appearance)\b", t)
    if ma:
        errs.append(f"Verbotenes Attribut '{ma.group(1)}' - es gibt nur "
                    f"STR/DEX/CON/INT/WIS (kein Charisma/Glueck/Aussehen).")

    # Kein Markdown im Prosatext. [ SYSTEM ]-Klammern und Bindestriche sind erlaubt.
    md_hits = [ln.strip() for ln in body.split("\n")
               if re.search(r"[*_`]", ln) or re.match(r"\s*(#|---|\*\*\*)", ln)]
    if md_hits:
        errs.append(f"Markdown im Prosatext ({len(md_hits)}x): {md_hits[0][:60]}")

    for s in re.split(r'(?<=[.!?"])\s+', body):
        # System-Ausgabe ([ LEVEL UP ], Statusbloecke) ist keine Prosa und hat
        # keine Satzzeichen -> sonst zaehlt der ganze Block als ein Riesensatz.
        if re.search(r"\[[^\]]{1,40}\]", s):
            continue
        n = len(s.split())
        if n >= 40:
            errs.append(f"Satz mit {n} Woertern: {s.strip()[:70]}...")

    n = len(re.findall(r"would rather|'d rather", t))
    if n > 1:
        errs.append(f'"would rather" steht {n} mal. Hoechstens einmal.')

    hits = re.findall(r".{0,45}\b(?:is not a|isn't a|it is not|It is not|That is not|was not a)\b.{0,45}", t)
    if len(hits) > 1:
        warns.append(f'DiGiorno "nicht X, sondern Y" moeglicherweise {len(hits)} mal:')
        for h in hits:
            warns.append("           ..." + h.replace("\n", " ").strip() + "...")

    for p in SELF_COMMENT:
        if t.count(p):
            warns.append(f'Selbstkommentar zur eigenen Redlichkeit: "{p}"')
    for p in TONE_LABEL:
        if t.count(p):
            warns.append(f'Beat etikettiert den Ton statt zu handeln: "{p}"')

    for q in re.findall(rf'^"{QWORD}[^?"]{{0,70}}\."$', t, flags=re.M):
        warns.append(f"Fragezeichen pruefen: {q}")

    wc = len(t.split())
    if wc > MAXWORDS:
        warns.append(f"{wc} Woerter, ueber dem Ziel von {MAXWORDS}.")

    if not os.path.exists(path[:-3] + ".txt"):
        warns.append("Keine .txt-Fassung. build.py laufen lassen.")

    return errs, warns


BASELINE = ".check-baseline"


def read_baseline(root):
    p = os.path.join(root, BASELINE)
    out = {}
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.split("#")[0].strip()
            if line:
                k, v = line.rsplit(None, 1)
                out[k.strip()] = int(v)
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    root = os.path.dirname(os.path.abspath(__file__))

    if args:
        files = args
    else:
        files = [f for f in sorted(glob.glob(os.path.join(root, "chapters", "ch*.md")))
                 if NAME.match(os.path.basename(f))]

    base = read_baseline(root)
    counts, bad, worse, better = {}, 0, [], []

    for f in sorted(files):
        key = os.path.basename(f)
        errs, warns = check(f)
        counts[key] = len(errs)
        if not errs and not warns:
            print(f"{key:<32} sauber")
            continue
        print(f"\n{key}")
        for e in errs:
            print("  FEHLER   " + e)
        for w in warns:
            print("  hinweis  " + w)
        if errs:
            bad += 1

    if "--baseline" in flags:
        with open(os.path.join(root, BASELINE), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("# Geduldeter Altbestand je Kapitel. Neu schreiben mit "
                     "python3 check.py --baseline\n")
            for k in sorted(counts):
                fh.write(f"{k}  {counts[k]}\n")
        print(f"\n{BASELINE} geschrieben.")
        sys.exit(0)

    for k, n in sorted(counts.items()):
        b = base.get(k)
        if b is None:
            continue
        if n > b:
            worse.append(f"{k}: {b} geduldet, jetzt {n}")
        elif n < b:
            better.append(f"{k}: {b} auf {n}")

    print(f"\n{len(files)} Kapitel geprueft, {bad} mit Fehlern.")
    if base:
        if better:
            print("Besser geworden:")
            for x in better:
                print("  " + x)
        if worse:
            print("SCHLECHTER GEWORDEN:")
            for x in worse:
                print("  " + x)
        else:
            print("Keine neue Verschuldung gegenueber der Basislinie.")
        if better:
            print("Basislinie nachziehen mit: python3 check.py --baseline")

    if "--ratchet" in flags:
        sys.exit(1 if worse else 0)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
