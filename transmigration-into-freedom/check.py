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

# Kanon-Zahlen-Watchlist: feste Werte mit EINDEUTIGEM Subjekt (Watchlist, keine
# Stoppliste - keine harte Konstante auf ein nacktes Substantiv). Trifft der Regex
# ein anderes Subjekt ("third house"), faengt die Basislinie es auf. Nur Zahlen,
# die sich NICHT aendern - Gaaras eigene Level/Werte stehen in character-arc.md.
NUMWORD = (r"(?:thirty-nine|thirty-eight|thirty-five|\d+|one|two|three|four|five|"
           r"six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|"
           r"sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|"
           r"seventy|eighty|ninety)")
CANON_NUMBERS = [
    (re.compile(rf"\b({NUMWORD})\s+houses\b", re.I), {"forty", "40"}, "Oldstep hat vierzig Haeuser"),
    (re.compile(rf"\b({NUMWORD})\s+companies\b", re.I), {"thirty-nine", "39"}, "Gaara: 39 Firmen im alten Leben"),
    (re.compile(rf"\b({NUMWORD})\s+coins\b", re.I), {"eleven", "11"}, "elf Muenzen aus Teodors Beutel"),
    (re.compile(r"Marit[^.\n]{0,40}?\b(?:Level\s+|at\s+)(\d+)\b", re.I), {"6"}, "Marit ist Level 6"),
    # Preisleiter, ch20 auf der Strasse in den Wold. Recheneinheit ist die
    # Ziege, nicht die Muenze. Elf Muenzen = eine gute Ziege und etwas darueber.
    (re.compile(rf"\b({NUMWORD})\s+goats\b", re.I),
     {"four", "4", "forty", "40", "eight", "8", "twenty", "20", "thirty", "30"},
     "Preisleiter: Klinge 4, Milchkuh 8, Ochse 20, Pferd 30, Buch 40 Ziegen"),
    (re.compile(rf"skin of parchment[^.\n]{{0,30}}?\b({NUMWORD})\b", re.I),
     {"a", "one", "1"}, "eine Haut Pergament kostet eine Ziege"),
]


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

    for rx, allowed, why in CANON_NUMBERS:
        for mm in rx.finditer(t):
            if mm.group(1).lower() not in allowed:
                errs.append(f"Kanon-Zahl '{mm.group(0).strip()}' - {why} "
                            f"({' / '.join(sorted(allowed))}). Anderes Subjekt? "
                            f"Dann mit --baseline verbuchen.")

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

    # Erdkalender. Er ist seit Tagen in dieser Welt und kennt keine Wochentage,
    # und niemand in Oldstep nennt je einen. Gefunden in ch13 als einziger
    # Treffer in zwanzig Kapiteln, eingebaut beim Umschreiben der Byre-Szene.
    for w in re.findall(r"\b(Monday|Tuesday|Wednesday|Thursday|Friday|"
                        r"Saturday|Sunday|January|February|March|April|June|"
                        r"July|August|September|October|November|December)\b", t):
        errs.append(f'Erdkalender im Text: "{w}". Diese Welt hat keine Wochentage '
                    f'und keine Monatsnamen.')

    # DiGiorno ist nicht jede Verneinung, sondern die POINTEN-FORM: ein kurzer
    # verneinter Satz, direkt gefolgt von der positiven Auffuellung.
    # "It is not a stream. This is a floor." feuert. "Not much, and never about
    # herself." feuert nicht - das ist gewoehnliche Prosa und soll bleiben.
    digi = re.compile(
        r"((?:is not a|isn't a|it is not|It is not|That is not|That was not|"
        r"was not a|Not a |Not the |Not into|Not at )[^.!?\n]{0,45}[.!?])"
        r"\s+((?:This is|This was|A |An |The |Upward|Away)[^.!?\n]{0,45}[.!?,])")
    hits = digi.findall(t)
    if hits:
        warns.append(f'DiGiorno-Pointe {len(hits)} mal (der Autor will keine):')
        for a, b in hits:
            warns.append("           ..." + (a + " " + b).replace("\n", " ").strip() + "...")

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


STAT_KEYS = ["STR", "DEX", "CON", "INT", "WIS"]
RANKVAL = {"E": 1, "D": 2, "C": 3, "B": 4, "A": 5, "S": 6}


def _chapters_in_order(root):
    return [f for f in sorted(glob.glob(os.path.join(root, "chapters", "ch*.md")))
            if NAME.match(os.path.basename(f))]


def progression(root):
    """Rekonstruiert Status und Skills Kapitel fuer Kapitel aus den System-Bloecken
    ([ STATUS ], [ LEVEL UP ], [ ATTRIBUTES UPDATED ], [ SKILL ACQUIRED ]) und
    meldet, wenn ein Wert sich zurueckentwickelt, ein Skill im Rang faellt, oder
    ein "X: a to b"-Block bei einem anderen a anfaengt als dem, wo das vorige
    Kapitel aufgehoert hat (so ist "CON: 5 to 8" nach einem Kapitel mit CON 6
    monatelang durchgerutscht - der Endwert stimmte, die Rechnung nicht).
    Diese Labels stehen nur in den Bloecken, nicht in der Prosa - darum robust.
    Nachvollziehen (Verlauf) und durchsetzen (keine Regression) in einem."""
    state = {k: None for k in ("Level", "HPmax", "MPmax", *STAT_KEYS, "Class", "Race")}
    skills = {}
    rows, viols = [], []
    for path in _chapters_in_order(root):
        ch = os.path.basename(path)[:4]
        with open(path, encoding="utf-8") as fh:
            t = fh.read()
        upd = []
        for m in re.finditer(r"^Level:\s*(\d+)", t, re.M):
            upd.append(("Level", int(m.group(1))))
        def prev(key):
            """Letzter bekannter Wert: erst was in DIESEM Kapitel schon stand,
            sonst der Stand aus dem Kapitel davor."""
            for kk, vv in reversed(upd):
                if kk == key:
                    return vv
            return state.get(key)

        for key, lbl in (("HPmax", "HP"), ("MPmax", "MP")):
            # Gruppe 2 ist das Trennzeichen: "100/100" ist cur/max, "120 to 165"
            # ist eine Rechnung und hat darum einen pruefbaren Startwert.
            for m in re.finditer(rf"^{lbl}:\s*(\d+)\s*(/|to)\s*(\d+)", t, re.M):
                if m.group(2) == "to":
                    frm, p = int(m.group(1)), prev(key)
                    if isinstance(p, int) and frm != p:
                        viols.append(f"{ch}: {lbl}-Block rechnet ab {frm}, "
                                     f"zuletzt stand {p}")
                upd.append((key, int(m.group(3))))
        for k in STAT_KEYS:
            for m in re.finditer(rf"^{k}:\s*(\d+)(?:\s*to\s*(\d+))?", t, re.M):
                if m.group(2):
                    frm, p = int(m.group(1)), prev(k)
                    if isinstance(p, int) and frm != p:
                        viols.append(f"{ch}: {k}-Block rechnet ab {frm}, "
                                     f"zuletzt stand {p}")
                upd.append((k, int(m.group(2) or m.group(1))))
        for k in ("Class", "Race"):
            m = re.search(rf"^{k}:\s*([A-Za-z][A-Za-z ]*)$", t, re.M)
            if m:
                upd.append((k, m.group(1).strip()))
        # ACQUIRED nennt einen Rang, ADVANCED nennt "Rank E to Rank D". Ohne die
        # zweite Form bleibt jeder Aufstieg fuer das Skript unsichtbar.
        for m in re.finditer(r"\[ SKILL (?:ACQUIRED|ADVANCED) \][^\[]*?\n"
                             r"([A-Z][A-Za-z ]+?), Rank ([A-Z])"
                             r"(?:\s+to\s+Rank\s+([A-Z]))?", t):
            name = m.group(1).strip()
            rank = m.group(3) or m.group(2)
            if name in skills and RANKVAL.get(rank, 0) < RANKVAL.get(skills[name], 0):
                viols.append(f"{ch}: Skill {name} faellt {skills[name]} -> {rank}")
            skills[name] = rank
        for key, v in upd:
            old = state.get(key)
            if isinstance(v, int) and isinstance(old, int) and v < old:
                viols.append(f"{ch}: {key} faellt {old} -> {v} (darf nicht sinken)")
            state[key] = v
        rows.append((ch, dict(state), dict(skills)))
    return rows, viols


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

    if not args:
        rows, viols = progression(root)
        print("\nStatus- und Skill-Verlauf (aus den Kapitel-Bloecken rekonstruiert):")
        for ch, st, sk in rows:
            attrs = " ".join(f"{k}{st[k]}" for k in STAT_KEYS if st[k] is not None)
            skl = ", ".join(f"{n} {r}" for n, r in sk.items()) or "-"
            print(f"  {ch}  L{st['Level']}  HP{st['HPmax']} MP{st['MPmax']}  "
                  f"{attrs}  Class:{st['Class']}  Skills: {skl}")
        if viols:
            print("\nREGEL VERLETZT (Status/Skills: keine Rueckentwicklung, und ein Rechenblock muss dort anfangen, wo das vorige Kapitel aufhoert):")
            for v in viols:
                print("  " + v)

    if "--ratchet" in flags:
        sys.exit(1 if worse else 0)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
