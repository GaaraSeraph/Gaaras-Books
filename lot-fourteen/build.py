#!/usr/bin/env python3
"""
Lot Fourteen, Build.

Aufruf:  python3 build.py            aus dem Projektordner
         python3 build.py <ordner>   von woanders

Erzeugt aus den Quellen:
  paste/chNN_vX_Y_en_PASTE.txt   Einfuegefassungen ohne Markdown
  book.md                        alle Kapitel am Stueck
  HANDBUCH.md                    alle doc/-Dokumente am Stueck, mit Inhalt
  MANIFEST.txt                   Baubericht

Quellen sind chapters/ und doc/. Alles Erzeugte wird bei jedem Lauf
ueberschrieben und **nie** von Hand bearbeitet.

Die erzeugten Dateien tragen bewusst KEINEN Zeitstempel. Damit ist der Build
reproduzierbar: gleiche Quellen -> byteweise gleiche Ausgabe, egal auf welchem
Rechner oder Betriebssystem. So committet die GitHub Action nur bei echten
Aenderungen und nicht bei jedem Push. Wann zuletzt etwas geaendert wurde, zeigt
git bzw. GitHub pro Datei/Ordner ("last commit").

Alle Dateien werden als UTF-8 gelesen und mit LF geschrieben, unabhaengig vom
Betriebssystem (Windows-Standard waere sonst cp1252/CRLF -> Absturz an den
koreanischen Zeichen in doc/ und byteweise abweichende Ausgabe).

Bricht ab, wenn die Version im Dateinamen nicht der Kopfzeile entspricht oder
eine Kapitelnummer fehlt.
"""
import re
import os
import sys
import glob

NAME = re.compile(r"^ch(\d{2})_v(\d+)[._](\d+)_en\.md$")
HEAD = re.compile(r"Version\s+(\d+)\.(\d+)\s")

# Baende. Jeder Band hat ein eigenes Kapitelverzeichnis und faengt wieder bei
# Kapitel 1 an. Ein Band, dessen Ordner es nicht gibt oder der leer ist, wird
# uebersprungen - solange chapters-2/ leer ist, baut das hier wie vorher.
#
# Die Bandnummer steht bewusst NICHT in den Kapiteldateien. Sie ergibt sich aus
# dem Ordner und wird beim Bauen in die Titelzeile geschrieben. Stuende sie in
# den Dateien, muessten vierunddreissig Kapitel eine Fassung hochsetzen, damit
# oben ein Wort mehr steht - und sie koennte gegen den Ordner driften, in dem
# die Datei liegt. Was abgeleitet werden kann, wird abgeleitet.
BANDS = [
    (1, "chapters", "Book One"),
    (2, "chapters-2", "Book Two"),
]


def bands(root):
    """Die Baende, die es als Ordner mit Kapiteln darin wirklich gibt."""
    out = []
    for num, sub, label in BANDS:
        d = os.path.join(root, sub)
        if os.path.isdir(d) and glob.glob(os.path.join(d, "ch*_en.md")):
            out.append((num, d, label, sub))
    return out


def titled(label, text):
    """Bandnummer in die Titelzeile schreiben, und nur in die erste Zeile.

    Aus "# Chapter 15: Four thousand two hundred" wird
    "# Book One \u00b7 Chapter 15: Four thousand two hundred".
    Die Quelldatei bleibt unberuehrt."""
    lines = text.split("\n")
    if lines and lines[0].startswith("# "):
        lines[0] = "# %s \u00b7 %s" % (label, lines[0][2:].strip())
    return "\n".join(lines)


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def write_text(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def newest_chapters(chapdir):
    best = {}
    for path in glob.glob(os.path.join(chapdir, "ch*_en.md")):
        m = NAME.match(os.path.basename(path))
        if not m:
            continue
        num = int(m.group(1))
        ver = (int(m.group(2)), int(m.group(3)))
        if num not in best or ver > best[num][0]:
            best[num] = (ver, path)
    return best


def to_paste(md):
    t = re.sub(r"^#{1,3} ", "", md, flags=re.M)
    t = re.sub(r"\*\*([^*\n]+)\*\*", r"\1", t)
    t = re.sub(r"^\*(.+)\*$", r"\1", t, flags=re.M)
    t = re.sub(r"\*([^*\n]+)\*", r"\1", t)
    t = t.replace("\n---\n", "\n* * *\n")
    # Blockzitate: der Text eines Briefes, ohne die Markdown-Markierung.
    t = re.sub(r"^> ?", "", t, flags=re.M)
    # Kein Test auf ">": die Ersetzung darueber hat jedes davon entfernt.
    # Eine Klausel dafuer koennte hier nie ausloesen und saehe nur nach
    # Abdeckung aus.
    left = [l for l in t.split("\n")
            if ("*" in l or l.startswith("#")) and l.strip() != "* * *"]
    if left:
        raise ValueError("Markdown-Rest in der Paste-Fassung: " + left[0][:60])
    return t.rstrip() + "\n"


# Verweise auf Dateien, die es einmal gab. Die Dokumente wurden von
# canon//craft//log//plot/ und einer "story-bible" auf doc/01 bis doc/08
# umgebaut, und die Verweise sind nicht alle mitgezogen. So etwas verrottet
# still: es faellt erst auf, wenn jemand nachschlaegt und nichts findet.
REF = re.compile(r"(?:canon|craft|log|plot)/[\w./-]+|docs?/[\w./-]+\.md"
                 r"|\b\d\d-[\w-]+\.md")
# Dokumente, die es als Datei nicht mehr gibt, aber im Fliesstext weiterleben.
GHOST = re.compile(r"\bder Bibel\b|\bdie Bibel\b|\bBibel\b|story-bible", re.I)


def warn_dead_refs(root):
    """Warnt, blockiert nicht. Ein bewusst vorausweisender Verweis auf ein
    geplantes Dokument soll den Build nicht anhalten, aber sichtbar sein."""
    scan = [os.path.join(root, "CLAUDE.md")]
    scan += sorted(glob.glob(os.path.join(root, "doc", "*.md")))
    dead, ghosts = [], []
    for f in scan:
        if not os.path.exists(f):
            continue
        name = os.path.relpath(f, root).replace("\\", "/")
        for line_no, line in enumerate(read_text(f).split("\n"), 1):
            for m in REF.finditer(line):
                target = m.group(0)
                cand = [os.path.join(root, target),
                        os.path.join(root, "doc", os.path.basename(target))]
                if not any(os.path.exists(c) for c in cand):
                    dead.append(f"{name}:{line_no} -> {target}")
            if GHOST.search(line):
                ghosts.append(f"{name}:{line_no}")
    if dead:
        print(f"\nWARNUNG  {len(dead)} tote Dateiverweise:")
        for d in dead:
            print("  " + d)
    if ghosts:
        print(f"\nWARNUNG  {len(ghosts)} Verweise auf die Bibel, die es als Datei "
              f"nicht mehr gibt (umgebaut auf doc/01 bis doc/08):")
        for g in ghosts:
            print("  " + g)
    return len(dead) + len(ghosts)


# ---------------------------------------------------------------- Register

# Wer im Register gefuehrt wird. Der Schluessel ist der Name im Register, die
# Liste sind die Schreibweisen, unter denen die Figur im Text auftaucht.
# Georgij fehlt bewusst: er ist in jeder Begegnung, eine Liste seiner Nennungen
# waere die Liste aller Zeilen.
FIGURES = {
    "Annie": [r"Annie"],
    "Mrs Seo": [r"Mrs Seo"],
    "Ji-won": [r"Ji-won"],
    "Bae": [r"\bBae\b"],
    "Eun-ju": [r"Eun-ju"],
    "Mr Baek": [r"Mr Baek", r"\bBaek\b"],
    "Mr Yeo": [r"Mr Yeo", r"\bYeo\b"],
    "Tae-min": [r"Tae-min"],
    "Mr Ku": [r"Mr Ku"],
    "Mr Pyo": [r"Mr Pyo"],
    "Mrs Ahn": [r"Mrs Ahn"],
    "Mr Im": [r"Mr Im\b"],
    "Mr Noh": [r"Mr Noh", r"\bNoh\b"],
    "Jang": [r"\bJang\b"],
    "Hana": [r"\bHana\b"],
    "Kim Ye-rin": [r"Ye-rin"],
    "Kim Do-yun": [r"Do-yun"],
    "Park Sang-hoon": [r"Sang-hoon"],
    "Kang Ji-hoon": [r"\bKang\b"],
    "Choi Dae-ho": [r"Choi"],
    "Minister Min-ho": [r"Min-ho"],
    "Mr Hong": [r"\bHong\b"],
    "Chairman Woo": [r"\bWoo\b"],
    "Mrs Sunwoo": [r"Sunwoo"],
    "Nam Byung-hee": [r"Nam Byung-hee", r"Byung-hee"],
    "Shin": [r"\bShin\b"],
    "Mrs Jeon": [r"Mrs Jeon", r"\bJeon\b"],
    "Mr Hwang": [r"Mr Hwang", r"Hwang"],
    "Mrs Ryu": [r"\bRyu\b"],
    "Chef Bang": [r"\bBang\b"],
}

DATELINE = re.compile(r"Days? ([A-Za-z0-9\- ]+?) ·")
NUMS = re.compile(
    r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|"
    r"thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million)"
    r"(?:[- ](?:and[- ])?(?:one|two|three|four|five|six|seven|eight|nine|ten|"
    r"eleven|twelve|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|"
    r"hundred|thousand|million))*\b", re.I)

WORDNUM = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve "
    "thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split())}
WORDNUM.update({"thirty": 30, "forty": 40, "fifty": 50})


def day_of(raw):
    """'Twenty-Three' oder '27 to 28' -> 23 bzw. 27."""
    s = raw.strip().lower().replace("-", " ").split(" to ")[0].strip()
    if s.isdigit():
        return int(s)
    total = sum(WORDNUM[p] for p in s.split() if p in WORDNUM)
    return total or None


def ref(band, num):
    """Fundstelle ueber Baende hinweg eindeutig: b1ch15, b2ch01."""
    return f"b{band}ch{num:02d}"


def build_register(root, chapters):
    """Erzeugt BEGEGNUNGEN.md: wer wann wo vorkommt, mit Tag und Fundstelle.

    Das Geruest ist erzeugt und kann deshalb nicht driften. Was bei einer
    Begegnung gegeben oder genommen wurde, ist Urteil und gehoert nach
    doc/03-cast.md. Die Zahlenspalte ist der eigentliche Zweck: Figurenzahlen
    stehen hier nebeneinander, statt ueber siebzehn Kapitel verstreut."""
    found = {name: [] for name in FIGURES}
    pats = {n: [re.compile(p) for p in ps] for n, ps in FIGURES.items()}

    for band, blabel, num, ver, fname, text in chapters:
        lines = text.split("\n")
        day = None
        for i, line in enumerate(lines, 1):
            m = DATELINE.search(line)
            if m and (line.startswith("#") or line.startswith("*")):
                day = day_of(m.group(1)) or day
                continue
            if line.startswith("#") or line.startswith("*Lot Fourteen"):
                continue
            for name, ps in pats.items():
                if any(p.search(line) for p in ps):
                    zahlen = [z.group(0) for z in NUMS.finditer(line)]
                    # kein break: eine Zeile darf mehrere Figuren enthalten,
                    # und eine Begegnung zu zweit ist fuer beide eine.
                    found[name].append((day, band, num, i, line.strip(), zahlen))

    order = sorted(FIGURES, key=lambda n: (-len(found[n]), n))
    out = [
        "# Lot Fourteen, Begegnungsregister",
        "",
        "*Erzeugt aus `chapters/`. Wird nicht bearbeitet.*",
        "",
        "Wer wann vorkommt, mit Tag und Fundstelle. **Das Geruest ist erzeugt und",
        "kann deshalb nicht driften.** Was bei einer Begegnung gegeben, genommen",
        "oder verschwiegen wurde, ist Urteil und steht in `doc/03-cast.md`.",
        "",
        "Georgij fehlt: er ist in jeder Begegnung, seine Liste waere die Liste",
        "aller Zeilen.",
        "",
        "**Wozu die Zahlenspalte.** Figurenzahlen stehen hier nebeneinander statt",
        "ueber siebzehn Kapitel verstreut. Genau dort sassen die Widersprueche:",
        "Chairman Woo einundfuenfzig Jahre im Geschaeft an einer Stelle und sechzig",
        "an einer anderen, Mrs Ryu vier Minuten im Dokument und sechs im Text.",
        "",
        "## Uebersicht",
        "",
        "| Figur | Nennungen | Kapitel | erster Tag | letzter Tag |",
        "|---|---|---|---|---|",
    ]
    for name in order:
        eintraege = found[name]
        if not eintraege:
            out.append(f"| {name} | **0** | - | - | - |")
            continue
        kaps = sorted({(e[1], e[2]) for e in eintraege})
        tage = sorted({e[0] for e in eintraege if e[0]})
        spanne = (f"{ref(*kaps[0])}-{ref(*kaps[-1])}" if len(kaps) > 1
                  else ref(*kaps[0]))
        out.append(f"| {name} | {len(eintraege)} | {len(kaps)} ({spanne}) | "
                   f"{tage[0] if tage else '-'} | {tage[-1] if tage else '-'} |")

    for name in order:
        eintraege = found[name]
        out += ["", "---", "", f"## {name}", ""]
        if not eintraege:
            out.append("**Kommt im Text nicht vor.** Steht nur in `doc/`.")
            continue
        kaps = sorted({(e[1], e[2]) for e in eintraege})
        out.append(f"{len(eintraege)} Nennungen in {len(kaps)} Kapiteln.")
        out += ["", "| Tag | Fundstelle | Zeile |", "|---|---|---|"]
        for day, band, num, i, line, _ in eintraege:
            kurz = line if len(line) <= 90 else line[:88] + ".."
            kurz = kurz.replace("|", "\\|")
            out.append(f"| {day if day else '-'} | {ref(band, num)}:{i} | {kurz} |")
        mit_zahl = [(d, b, n, i, z) for d, b, n, i, l, z in eintraege if z]
        if mit_zahl:
            out += ["", f"### Zahlen in der Naehe von {name}", ""]
            for day, band, num, i, z in mit_zahl:
                out.append(f"- `{ref(band, num)}:{i}` (Tag {day if day else '?'}) - "
                           + ", ".join(sorted(set(x.lower() for x in z))))
    text = "\n".join(out) + "\n"
    write_text(os.path.join(root, "BEGEGNUNGEN.md"), text)
    return sum(1 for n in found if found[n]), text


def build_handbook(root, register=None):
    """Alle doc/-Dokumente am Stueck, plus das Begegnungsregister als letzter
    Teil. Das Register ist erzeugt und die acht Dokumente sind Quelle, aber
    beim Nachschlagen will man beides in einer Datei: wer eine Figurenszene
    schreibt, braucht die Beschreibung aus doc/03 und die Chronik aus dem
    Register nebeneinander."""
    docdir = os.path.join(root, "doc")
    files = sorted(glob.glob(os.path.join(docdir, "[0-9][0-9]-*.md")))
    if not files:
        return 0
    toc, body = [], []
    for f in files:
        t = read_text(f).rstrip()
        title = t.split("\n", 1)[0].lstrip("# ").strip()
        anchor = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        toc.append(f"- [{title}](#{anchor})  ·  `doc/{os.path.basename(f)}`")
        for line in t.split("\n"):
            if line.startswith("### "):
                sub = line[4:].strip()
                a = re.sub(r"[^a-z0-9]+", "-", sub.lower()).strip("-")
                toc.append(f"  - [{sub}](#{a})")
        body.append(t)

    nreg = 0
    if register:
        # Die Ueberschriften des Registers eine Stufe tiefer haengen, damit es
        # sich in die Gliederung einfuegt und das Inhaltsverzeichnis stimmt.
        reg = re.sub(r"^# ", "## ", register.rstrip(), flags=re.M)
        reg = re.sub(r"^## Lot Fourteen, Begegnungsregister",
                     "# Begegnungsregister", reg, count=1)
        reg = re.sub(r"^## ", "### ", reg, flags=re.M)
        reg = re.sub(r"^# Begegnungsregister", "# Begegnungsregister", reg, count=1)
        toc.append("- [Begegnungsregister](#begegnungsregister)  ·  "
                   "`BEGEGNUNGEN.md`, **erzeugt**")
        for line in reg.split("\n"):
            if line.startswith("### ") and not line.startswith("### Zahlen"):
                sub = line[4:].strip()
                a = re.sub(r"[^a-z0-9]+", "-", sub.lower()).strip("-")
                toc.append(f"  - [{sub}](#{a})")
        body.append(reg)
        nreg = 1

    total = sum(len(b.split()) for b in body)
    head = [
        "# Lot Fourteen, Handbuch",
        "",
        "*Erzeugt aus `doc/` und `chapters/`. Wird nicht bearbeitet.*",
        "",
        f"Alle {len(files)} Dokumente am Stueck plus das Begegnungsregister, "
        f"{total:,} Woerter.".replace(",", "."),
        "Geaendert wird die Quelldatei in `doc/`, danach `python3 build.py`.",
        "Das Register wird nirgends bearbeitet, es kommt aus den Kapiteln.",
        "",
        "## Inhalt",
        "",
    ] + toc
    write_text(os.path.join(root, "HANDBUCH.md"),
               "\n".join(head) + "\n\n---\n\n" + "\n\n---\n\n".join(body) + "\n")
    return len(files) + nreg


def build_reader(root, chapters):
    """read/ neu schreiben: je Kapitel eine Seite, dazu das ganze Buch.

    reader.py liegt neben build.py, nicht zwingend im uebergebenen root -
    der Hook ruft build.py mit dem Projektordner als Argument auf, und aus
    der Repo-Wurzel heraus faende ein Import ueber root nichts.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    if here not in sys.path:
        sys.path.insert(0, here)
    import reader

    readdir = os.path.join(root, "read")
    os.makedirs(readdir, exist_ok=True)
    for old in glob.glob(os.path.join(readdir, "*.html")):
        os.remove(old)
    for old in glob.glob(os.path.join(readdir, "band-*", "*.html")):
        os.remove(old)

    quads = [(fname, text + "\n", band, blabel)
             for band, blabel, _, _, fname, text in chapters]
    for fname, text, band, blabel in quads:
        d = os.path.join(readdir, f"band-{band}")
        os.makedirs(d, exist_ok=True)
        write_text(os.path.join(d, fname.replace(".md", ".html")),
                   reader.render(text, fname, blabel))
    write_text(os.path.join(readdir, "book.html"), reader.render_book(quads))
    return len(quads)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    pastedir = os.path.join(root, "paste")
    found = bands(root)
    if not found:
        sys.exit("Kein Band mit Kapiteln gefunden. Erwartet: "
                 + ", ".join(sub for _, sub, _ in BANDS))
    os.makedirs(pastedir, exist_ok=True)

    problems, chapters = [], []
    for band, chapdir, blabel, sub in found:
        best = newest_chapters(chapdir)
        for num in sorted(best):
            ver, path = best[num]
            text = read_text(path)
            h = HEAD.search(text)
            if not h:
                problems.append(f"Band {band}, Kapitel {num:02d}: "
                                f"keine Versionszeile im Text")
            elif (int(h.group(1)), int(h.group(2))) != ver:
                problems.append(
                    f"Band {band}, Kapitel {num:02d}: Dateiname sagt "
                    f"v{ver[0]}.{ver[1]}, Kopfzeile sagt "
                    f"v{h.group(1)}.{h.group(2)}")
            chapters.append((band, blabel, num, ver,
                             os.path.basename(path), text.rstrip()))
        missing = sorted(set(range(1, max(best) + 1)) - set(best))
        if missing:
            problems.append(f"Band {band}: fehlende Kapitel "
                            + ", ".join(f"{n:02d}" for n in missing))

    if problems:
        print("BUILD ABGEBROCHEN")
        for p in problems:
            print("  " + p)
        sys.exit(1)

    # Paste-Fassungen: erzeugt, nicht gepflegt. Veraltete verschwinden, und
    # zwar auch die aus der Zeit vor den Baenden, die flach in paste/ lagen.
    for old in glob.glob(os.path.join(pastedir, "*_PASTE.txt")):
        os.remove(old)
    for old in glob.glob(os.path.join(pastedir, "band-*", "*_PASTE.txt")):
        os.remove(old)
    for band, blabel, num, ver, fname, text in chapters:
        d = os.path.join(pastedir, f"band-{band}")
        os.makedirs(d, exist_ok=True)
        write_text(os.path.join(d, fname.replace(".md", "_PASTE.txt")),
                   to_paste(titled(blabel, text) + "\n"))

    # Lesefassungen. read/ ist nicht versioniert und wird bei jedem Build neu
    # geschrieben.
    nread = build_reader(root, chapters)

    total = sum(len(c[5].split()) for c in chapters)
    head = [
        "# Lot Fourteen",
        "",
        "*Sammelband. Wird nicht bearbeitet.*",
        "",
        "%s, %d Kapitel, %s Woerter."
        % ("1 Band" if len(found) == 1 else f"{len(found)} Baende",
           len(chapters), format(total, ",").replace(",", ".")),
        "",
        "Kanon sind die Dateien in "
        + ", ".join(f"`{sub}/`" for _, _, _, sub in found) + ".",
        "Je Kapitel wird automatisch die hoechste Versionsnummer genommen und",
        "gegen die Kopfzeile geprueft. **Die Bandnummer steht in keiner",
        "Kapiteldatei** - sie kommt aus dem Ordner und wird hier eingesetzt.",
        "",
        "| Band | Kap | Fassung | Woerter |",
        "|---|---|---|---|",
    ]
    for band, blabel, n, v, f, t in chapters:
        head.append("| %d | %02d | v%d.%d | %s |"
                    % (band, n, v[0], v[1],
                       format(len(t.split()), ",").replace(",", ".")))

    body = [titled(bl, t) for _, bl, _, _, _, t in chapters]
    write_text(os.path.join(root, "book.md"),
               "\n".join(head) + "\n\n---\n\n"
               + "\n\n---\n\n".join(body) + "\n")

    nfig, register = build_register(root, chapters)
    ndocs = build_handbook(root, register)

    manifest = ["# Erzeugt von build.py. Ergebnis, nicht Eingabe.", ""]
    for band, blabel, n, v, f, t in chapters:
        manifest.append(f"b{band}  ch{n:02d}  v{v[0]}.{v[1]:<5} "
                        f"{len(t.split()):>6} Woerter  {f}")
    manifest.append("")
    manifest.append("Gesamt: %s, %d Kapitel, %d Woerter"
                    % ("1 Band" if len(found) == 1 else f"{len(found)} Baende",
                       len(chapters), total))
    manifest.append(f"Handbuch: {ndocs} Dokumente")
    write_text(os.path.join(root, "MANIFEST.txt"), "\n".join(manifest) + "\n")

    for band, chapdir, blabel, sub in found:
        n = sum(1 for c in chapters if c[0] == band)
        w = sum(len(c[5].split()) for c in chapters if c[0] == band)
        print(f"{blabel:<9} {n:>2} Kapitel, {w:>6} Woerter   {sub}/")
    print(f"book.md        {len(chapters)} Kapitel, {total} Woerter")
    print(f"HANDBUCH.md    {ndocs} Dokumente")
    print(f"BEGEGNUNGEN.md {nfig} Figuren im Text")
    print(f"paste/         {len(chapters)} Einfuegefassungen")
    print(f"read/          {nread} Lesefassungen und book.html")

    warn_dead_refs(root)


if __name__ == "__main__":
    main()
