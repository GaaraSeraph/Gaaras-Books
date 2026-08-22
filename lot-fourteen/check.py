#!/usr/bin/env python3
"""
Lot Fourteen, mechanische Kapitelpruefung.

Aufruf:  python3 check.py                   prueft alle aktuellen Kapitel
         python3 check.py chapters/chNN_...  prueft eines
         python3 check.py --baseline         schreibt die Basislinie neu
         python3 check.py --ratchet          Rueckgabewert 1 nur bei Verschlechterung

Die Sperrklinke: Der Stilrueckstand aus alten Kapiteln soll nicht jeden Lauf
rot faerben, denn eine Warnung, die immer feuert, liest niemand mehr. Mit
--ratchet meldet check.py nur, wenn ein Kapitel **mehr** Fehler hat als in
.check-baseline vermerkt. Damit ist Altlast geduldet und Neuverschuldung nicht.

Prueft nur, was ohne Urteil pruefbar ist. Alles andere steht in doc/01-craft.md
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
    # Szenentrenner raus. Sonst klebt "---" am folgenden Satz und zaehlt als
    # Wort: ein Satz mit neununddreissig Woertern wird dann als vierzig
    # gemeldet. Das hat in vier Kapiteln falsche Treffer erzeugt.
    body = re.sub(r"^-{3,}$", "", body, flags=re.M)
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

    # DiGiorno: "nicht X, sondern Y". Der alte Regex suchte blosse Verneinungen
    # ("is not a") und traf damit in Kapitel 5 vier harmlose Saetze auf einen
    # echten. Drei Griffe haben ihn geschaerft:
    #   1. Es muss eine ERSETZUNG folgen: ", but" oder ". It is" / ". That is".
    #   2. Kein "because". Jede Verneinung mit Begruendung ist ein normaler
    #      Kausalsatz und kein Kontrast.
    #   3. Beide Haelften im selben Absatz. Ueber einen Absatzumbruch hinweg
    #      zeigt das "It" zurueck, statt zu ersetzen - das war die groesste
    #      Quelle falscher Treffer.
    # Bleibt eine Warnung und wird kein Fehler: Sprachheuristik trifft nicht
    # sauber genug fuer ein Gate, und die Liste ist als Lesehinweis gemeint.
    digiorno = re.compile(
        r"\bnot\b[^.!?\n]{1,50}?(?:,[ ]+but\b|[.;][ ]+(?:It|That)\b'?s?(?:[ ]+(?:is|was))?)")
    hits = [m.group(0) for m in digiorno.finditer(t)]
    if len(hits) > 1:
        warns.append(f'"nicht X, sondern Y" {len(hits)} mal, Quote ist eine. '
                     f"Der Regex trifft etwa drei von vier, also einzeln ansehen:")
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
    # Spannen zuerst: "Days 27 to 28 · Thursday 30 to Friday 31 October".
    # Die Schleife darunter kann sie nicht lesen, weil words_to_int an
    # "27 to 28" None zurueckgibt. Ohne diesen Durchgang wurde die Zeile
    # stillschweigend uebersprungen und danach als fehlend gemeldet.
    for mm in re.finditer(r"Days ([A-Za-z0-9\-]+) to ([A-Za-z0-9\-]+) · "
                          r"([A-Za-z]+) (\d+) to ([A-Za-z]+) (\d+)", t):
        for d_raw, wd_txt, dd_txt in ((mm.group(1), mm.group(3), mm.group(4)),
                                      (mm.group(2), mm.group(5), mm.group(6))):
            d = words_to_int(d_raw)
            if not d:
                continue
            days.append(d)
            wd, dd, mo = expected(d)
            if wd_txt != wd or int(dd_txt) != dd:
                errs.append(f"Datumszeile: Tag {d} ist {wd}, der {dd}. {mo}, im Text steht "
                            f"{wd_txt} {dd_txt}")

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

    errs.extend(check_facts(t))

    fn = NAME.match(os.path.basename(path))
    hd = re.search(r"Version\s+(\d+)\.(\d+)\s", t)
    if fn and hd and (fn.group(2), fn.group(3)) != (hd.group(1), hd.group(2)):
        errs.append(f"Dateiname sagt v{fn.group(2)}.{fn.group(3)}, "
                    f"Kopfzeile sagt v{hd.group(1)}.{hd.group(2)}")

    return errs, warns


# ---------------------------------------------------------------- Zahlen

# Zahlwoerter, aus denen der Text seine Groessen baut. Ziffern kommen in der
# Prosa fast nicht vor, deshalb steht hier die ausgeschriebene Form zuerst.
NUMWORD = (r"(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
           r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|"
           r"twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|"
           r"thousand|million)")

# Eine Groesse ist eine Zahl plus das Substantiv dahinter: "eleven houses".
# Mehrteilige Zahlen ("two hundred and twenty") werden mitgenommen.
QUANTITY = re.compile(
    r"\b(" + NUMWORD + r"(?:[- ](?:and[- ])?" + NUMWORD + r")*)\s+([a-z]{3,})\b",
    re.I)

# Harte Konstanten. Bewusst ueberempfindlich.
#
# In einem Roman gehoert dasselbe Substantiv verschiedenen Subjekten: Georgij
# hat vier Sprachen, aber der Katalog in Kapitel 6 fuehrt ein anderes Los mit
# "two languages", und diese Pruefung kann den Unterschied nicht sehen. Sie
# feuert also gelegentlich auf richtigen Text.
#
# **Das ist hier vertretbar, und zwar wegen der Basislinie.** Ein berechtigter
# Treffer wird einmal angesehen und mit `--baseline` als Altbestand verbucht;
# danach schweigt er, und jeder NEUE Treffer im selben Kapitel blockiert
# trotzdem. Eine ueberempfindliche Pruefung mit Ventil faengt mehr als eine
# vorsichtige ohne. Ohne die Sperrklinke waere die Abwaegung umgekehrt.
#
# Regel beim Erweitern: nur Groessen, die im Kanon einen festen Wert haben.
# Nicht: Groessen, die von Szene zu Szene verschieden sein duerfen.
FACTS = [
    # (Substantiv, erlaubte Zahlen, wofuer die jeweilige Zahl steht)
    ("houses", {"eleven", "four"},
     "elf Platzierungen, vier mit vermerktem Grund"),
    ("cameras", {"twenty-four", "twenty-two", "two"},
     "vierundzwanzig gesamt, zweiundzwanzig auf der Wand, zwei zusaetzliche"),
    ("languages", {"four"},
     "Georgij hat vier"),
    ("screens", {"eight"},
     "acht Schirme im Monitorzimmer"),
    ("sheets", {"nine", "eight", "nineteen"},
     "neun an Jang, acht bei Annie, neunzehn bei Sang-hoon"),
]

# Watchlist statt Stoppliste. Der erste Versuch hat alles gezaehlt und alles
# ausser Zeitangaben gemeldet: 51 Groessen, davon "because", "behind",
# "entirely" - der Regex nimmt stumpf das Wort nach der Zahl, ohne zu wissen,
# ob es ein Substantiv ist. Ein Bericht, den niemand liest, ist keiner.
#
# Deshalb nur die Groessen, die im Kanon eine feste Zahl haben. Kurz halten:
# was hier fehlt, faellt nicht auf, was falsch drinsteht, kostet Vertrauen.
WATCH = {
    "cameras", "screens", "angles", "exits", "columns", "drawers",
    "houses", "placements", "returns", "languages",
    "names", "pages", "sheets", "lots", "buyers", "holdings", "charges",
    "metres", "cent", "million", "won", "tables", "covers", "routes",
    "staff", "security", "supervisors", "maids", "drivers",
}

# Zahlen, die im Buch bereits zu viel arbeiten (doc/01-craft.md, Abschnitt 6).
LOADED = ("eleven", "nine")


def quantities(text):
    """Liefert (Zahl, Substantiv, Zeilennummer) fuer jede Groesse im Text."""
    out = []
    for line_no, line in enumerate(text.split("\n"), 1):
        if line.startswith("#") or line.startswith("*Lot Fourteen"):
            continue
        for mm in QUANTITY.finditer(line):
            out.append((mm.group(1).lower().strip(), mm.group(2).lower(), line_no))
    return out


def check_facts(text):
    """Harte Konstanten. Gibt Fehlerzeilen zurueck. Siehe Kommentar bei FACTS:
    bewusst ueberempfindlich, weil die Basislinie berechtigte Treffer auffaengt."""
    errs = []
    for num, noun, line_no in quantities(text):
        for fact_noun, allowed, meaning in FACTS:
            if noun == fact_noun and num not in allowed:
                errs.append(f'Zeile {line_no}: "{num} {noun}" - Kanon kennt hier nur '
                            f'{", ".join(sorted(allowed))} ({meaning}). '
                            f'Anderes Subjekt? Dann mit --baseline verbuchen.')
    return errs


def numbers_report(files):
    """Querbericht ueber alle Kapitel. Meldet nichts als Fehler, sondern zeigt,
    wo dieselbe Groesse mit verschiedenen Zahlen dasteht. Die Entscheidung,
    ob das ein Widerspruch oder eine andere Bedeutung ist, kann kein Programm
    treffen - aber die Gegenueberstellung kann es liefern."""
    index = {}
    load = {}
    for path in files:
        key = os.path.basename(path)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for num, noun, line_no in quantities(text):
            index.setdefault(noun, {}).setdefault(num, []).append((key, line_no))
        low = text.lower()
        load[key] = {w: len(re.findall(rf"\b{w}\b", low)) for w in LOADED}

    print("=" * 72)
    print("GROESSEN MIT MEHR ALS EINER ZAHL")
    print("Kein Fehlerbericht. Gegenueberstellung zum Nachrechnen von Hand.")
    print("=" * 72)
    print("Oben steht, was am ehesten ein Widerspruch ist: wenige Nennungen,")
    print("aber verschiedene Zahlen. Wo eine Groesse dreissigmal vorkommt und")
    print("zehn Werte hat, ist das der Alltag des Textes und kein Fund.")

    # Nur Groessen, die in mehreren Kapiteln mit verschiedenen Zahlen stehen.
    # Zwei verschiedene Zahlen innerhalb eines Kapitels sind fast immer zwei
    # verschiedene Szenen ("drei Stuehle" hier, "acht Stuehle" dort). Wo eine
    # Groesse dagegen ueber Kapitelgrenzen hinweg schwankt, liegt der Verdacht.
    multi = {}
    for noun, werte in index.items():
        if noun not in WATCH or len(werte) < 2:
            continue
        multi[noun] = werte

    def verdacht(noun):
        werte = len(multi[noun])
        nennungen = sum(len(v) for v in multi[noun].values())
        # Je naeher an "jede Nennung eine andere Zahl", desto verdaechtiger.
        return (-(werte / nennungen), nennungen, noun)

    for noun in sorted(multi, key=verdacht):
        nennungen = sum(len(v) for v in multi[noun].values())
        print(f"\n{noun}  -  {len(multi[noun])} Zahlen auf {nennungen} Nennungen")
        for num in sorted(multi[noun], key=lambda x: -len(multi[noun][x])):
            wo = multi[noun][num]
            stellen = ", ".join(f"{k.split('_')[0]}:{l}" for k, l in wo[:6])
            mehr = f" (+{len(wo) - 6})" if len(wo) > 6 else ""
            print(f"    {num:<26} {len(wo):>2}x   {stellen}{mehr}")

    print("\n" + "=" * 72)
    print("AUSLASTUNG DER BELASTETEN ZAHLEN")
    print("doc/01-craft.md: elf und neun arbeiten im Buch bereits zu viel.")
    print("=" * 72)
    for key in sorted(load):
        zeile = "  ".join(f"{w} {load[key][w]:>2}" for w in LOADED)
        gesamt = sum(load[key].values())
        marke = "  <<<" if gesamt >= 12 else ""
        print(f"  {key.split('_')[0]:<6} {zeile}   Summe {gesamt:>2}{marke}")

    print(f"\n{len(index)} Groessen verfolgt, {len(multi)} davon mit mehr als einer Zahl.")


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
        best = {}
        # Relativ zum Skript, nicht zum aktuellen Verzeichnis: sonst findet der
        # Hook (der aus der Repo-Wurzel laeuft) keine Kapitel und die Sperrklinke
        # prueft ins Leere.
        for p in (glob.glob(os.path.join(root, "chapters", "ch*_en.md"))
                  or glob.glob(os.path.join(root, "ch*_en.md"))):
            m = NAME.match(os.path.basename(p))
            if not m:
                continue
            k, v = int(m.group(1)), (int(m.group(2)), int(m.group(3)))
            if k not in best or v > best[k][0]:
                best[k] = (v, p)
        files = [p for _, p in sorted(best.values(), key=lambda x: x[1])]

    if "--numbers" in flags:
        numbers_report(sorted(files))
        sys.exit(0)

    base = read_baseline(root)
    counts, bad, worse, better = {}, 0, [], []

    for f in sorted(files):
        key = os.path.basename(f)
        errs, warns = check(f)
        counts[key] = len(errs)
        if not errs and not warns:
            print(f"{key:<24} sauber")
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
