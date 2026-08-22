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
    left = [l for l in t.split("\n")
            if ("*" in l or l.startswith("#")) and l.strip() != "* * *"]
    if left:
        raise ValueError("Markdown-Rest in der Paste-Fassung: " + left[0][:60])
    return t.rstrip() + "\n"


def build_handbook(root):
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
    total = sum(len(b.split()) for b in body)
    head = [
        "# Lot Fourteen, Handbuch",
        "",
        "*Erzeugt aus `doc/`. Wird nicht bearbeitet.*",
        "",
        f"Alle {len(files)} Dokumente am Stueck, {total:,} Woerter.".replace(",", "."),
        "Geaendert wird die Quelldatei in `doc/`, danach `python3 build.py`.",
        "",
        "## Inhalt",
        "",
    ] + toc
    write_text(os.path.join(root, "HANDBUCH.md"),
               "\n".join(head) + "\n\n---\n\n" + "\n\n---\n\n".join(body) + "\n")
    return len(files)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    chapdir = os.path.join(root, "chapters")
    pastedir = os.path.join(root, "paste")
    if not os.path.isdir(chapdir):
        sys.exit(f"Kein Ordner {chapdir}.")
    os.makedirs(pastedir, exist_ok=True)

    best = newest_chapters(chapdir)
    if not best:
        sys.exit(f"Keine Kapiteldateien in {chapdir}.")

    problems, chapters = [], []
    for num in sorted(best):
        ver, path = best[num]
        text = read_text(path)
        h = HEAD.search(text)
        if not h:
            problems.append(f"Kapitel {num:02d}: keine Versionszeile im Text")
        elif (int(h.group(1)), int(h.group(2))) != ver:
            problems.append(f"Kapitel {num:02d}: Dateiname sagt v{ver[0]}.{ver[1]}, "
                            f"Kopfzeile sagt v{h.group(1)}.{h.group(2)}")
        chapters.append((num, ver, os.path.basename(path), text.rstrip()))

    missing = sorted(set(range(1, max(best) + 1)) - set(best))
    if missing:
        problems.append("Fehlende Kapitel: " + ", ".join(f"{n:02d}" for n in missing))

    if problems:
        print("BUILD ABGEBROCHEN")
        for p in problems:
            print("  " + p)
        sys.exit(1)

    # Paste-Fassungen: erzeugt, nicht gepflegt. Veraltete verschwinden.
    for old in glob.glob(os.path.join(pastedir, "*_PASTE.txt")):
        os.remove(old)
    for num, ver, fname, text in chapters:
        out = os.path.join(pastedir, fname.replace(".md", "_PASTE.txt"))
        write_text(out, to_paste(text + "\n"))

    total = sum(len(c[3].split()) for c in chapters)
    rows = [f"| {n:02d} | v{v[0]}.{v[1]} | {len(t.split()):,} |".replace(",", ".")
            for n, v, f, t in chapters]
    head = [
        "# Lot Fourteen",
        "",
        "*Sammelband. Wird nicht bearbeitet.*",
        "",
        f"{len(chapters)} Kapitel, {total:,} Woerter.".replace(",", "."),
        "",
        "Kanon sind die Dateien in `chapters/`. Je Kapitel wird automatisch die",
        "hoechste Versionsnummer genommen und gegen die Kopfzeile geprueft.",
        "",
        "| Kap | Fassung | Woerter |",
        "|---|---|---|",
    ] + rows
    write_text(os.path.join(root, "book.md"),
               "\n".join(head) + "\n\n---\n\n"
               + "\n\n---\n\n".join(c[3] for c in chapters) + "\n")

    ndocs = build_handbook(root)

    manifest = ["# Erzeugt von build.py. Ergebnis, nicht Eingabe.", ""]
    for n, v, f, t in chapters:
        manifest.append(f"ch{n:02d}  v{v[0]}.{v[1]:<5} {len(t.split()):>6} Woerter  {f}")
    manifest.append("")
    manifest.append(f"Gesamt: {len(chapters)} Kapitel, {total} Woerter")
    manifest.append(f"Handbuch: {ndocs} Dokumente")
    write_text(os.path.join(root, "MANIFEST.txt"), "\n".join(manifest) + "\n")

    print(f"book.md        {len(chapters)} Kapitel, {total} Woerter")
    print(f"HANDBUCH.md    {ndocs} Dokumente")
    print(f"paste/         {len(chapters)} Einfuegefassungen")


if __name__ == "__main__":
    main()
