#!/usr/bin/env python3
"""
Transmigration into Freedom, Build.

Aufruf:  python3 build.py            aus dem Projektordner
         python3 build.py <ordner>   von woanders

Kanon sind die Kapitel-`.md` in chapters/ (H1-Titelzeile, Leerzeile, Prosa).
Erzeugt daraus:
  chapters/chNN-slug.txt   Prosa ohne Titelzeile, zum Einfuegen in die Schreib-App
  book.md                  alle Kapitel am Stueck (Lesefassung)
  HANDBUCH.md              alle docs/-Dokumente am Stueck, mit Inhaltsverzeichnis
  MANIFEST.txt             Baubericht

Die `.txt` ist ABGELEITET: byteweise die `.md` ohne die Titelzeile. Sie wird bei
jedem Lauf neu erzeugt, damit `.md` und `.txt` nie auseinanderlaufen (das war
frueher die Sorte stiller Fehler, die niemandem auffaellt).

Kein Zeitstempel in den erzeugten Dateien (reproduzierbar -> kein Leerlauf-Commit
durch die GitHub Action). Alles UTF-8/LF, unabhaengig vom Betriebssystem.

Bricht ab, wenn ein Kapitel keine H1-Titelzeile hat oder eine Kapitelnummer fehlt.
"""
import re
import os
import sys
import glob

TITLE = "Transmigration into Freedom"
NAME = re.compile(r"^ch(\d{2})-.+\.md$")


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def write_text(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


DEAD_REF = re.compile(r"(?:canon|craft|log|plot)/[\w./-]+|docs?/[\w./-]+\.md")


def warn_dead_refs(root):
    """Meldet Verweise auf nicht existierende Dateien (canon//craft//log//plot/
    oder ein doc(s)/...md, das es nicht gibt). Nur Warnung, blockiert nicht --
    haelt die stale-Pfad-Klasse raus, die man sonst erst beim Nachschlagen merkt."""
    scan = [os.path.join(root, "CLAUDE.md")] + sorted(glob.glob(os.path.join(root, "doc*", "*.md")))
    seen = set()
    for f in scan:
        if not os.path.exists(f):
            continue
        for m in DEAD_REF.finditer(read_text(f)):
            ref = m.group(0)
            if not os.path.exists(os.path.join(root, ref)) and (f, ref) not in seen:
                seen.add((f, ref))
                print(f"  WARNUNG toter Verweis: {os.path.basename(f)} -> {ref}")


def find_chapters(chapdir):
    best, dups = {}, []
    for path in sorted(glob.glob(os.path.join(chapdir, "ch*.md"))):
        m = NAME.match(os.path.basename(path))
        if not m:
            continue
        num = int(m.group(1))
        if num in best:
            dups.append(num)
        best[num] = path
    return best, dups


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    chapdir = os.path.join(root, "chapters")
    if not os.path.isdir(chapdir):
        sys.exit(f"Kein Ordner {chapdir}.")

    best, dups = find_chapters(chapdir)
    if not best:
        sys.exit(f"Keine Kapiteldateien in {chapdir}.")

    problems = [f"Kapitel {n:02d}: mehrere Dateien mit derselben Nummer" for n in dups]

    chapters = []
    for num in sorted(best):
        path = best[num]
        text = read_text(path)
        title_block, sep, body = text.partition("\n\n")
        if not title_block.lstrip().startswith("# ") or not sep:
            problems.append(f"Kapitel {num:02d}: keine H1-Titelzeile + Leerzeile "
                            f"({os.path.basename(path)})")
            continue
        chapters.append((num, os.path.basename(path), title_block.strip(),
                         body, text.rstrip()))

    missing = sorted(set(range(1, max(best) + 1)) - set(best))
    if missing:
        problems.append("Fehlende Kapitel: " + ", ".join(f"{n:02d}" for n in missing))

    if problems:
        print("BUILD ABGEBROCHEN")
        for p in problems:
            print("  " + p)
        sys.exit(1)

    # .txt neu erzeugen: die .md ohne die Titelzeile.
    for num, fname, title, body, full in chapters:
        write_text(os.path.join(chapdir, fname[:-3] + ".txt"), body)

    total = sum(len(full.split()) for *_, full in chapters)
    rows = [f"| {n:02d} | {title.lstrip('# ').strip()} | {len(full.split()):,} |".replace(",", ".")
            for n, fn, title, body, full in chapters]
    head = [
        f"# {TITLE}",
        "",
        "*Sammelband. Wird nicht bearbeitet.*",
        "",
        f"{len(chapters)} Kapitel, {total:,} Woerter.".replace(",", "."),
        "",
        "Kanon sind die `.md` in `chapters/`. Die `.txt` daneben ist erzeugt.",
        "",
        "| Kap | Titel | Woerter |",
        "|---|---|---|",
    ] + rows
    write_text(os.path.join(root, "book.md"),
               "\n".join(head) + "\n\n---\n\n"
               + "\n\n---\n\n".join(full for *_, full in chapters) + "\n")

    ndocs = build_handbook(root, len(chapters))

    manifest = ["# Erzeugt von build.py. Ergebnis, nicht Eingabe.", ""]
    for n, fn, title, body, full in chapters:
        manifest.append(f"ch{n:02d}  {len(full.split()):>6} Woerter  {fn}")
    manifest.append("")
    manifest.append(f"Gesamt: {len(chapters)} Kapitel, {total} Woerter")
    manifest.append(f"Handbuch: {ndocs} Dokumente")
    write_text(os.path.join(root, "MANIFEST.txt"), "\n".join(manifest) + "\n")

    print(f"book.md         {len(chapters)} Kapitel, {total} Woerter")
    print(f"HANDBUCH.md     {ndocs} Dokumente")
    print(f"chapters/*.txt  {len(chapters)} Einfuegefassungen erzeugt")

    warn_dead_refs(root)


def build_handbook(root, nchapters):
    docdir = os.path.join(root, "docs")
    files = sorted(glob.glob(os.path.join(docdir, "*.md")))
    if not files:
        return 0
    toc, body = [], []
    for f in files:
        t = read_text(f).rstrip()
        title = t.split("\n", 1)[0].lstrip("# ").strip()
        anchor = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        toc.append(f"- [{title}](#{anchor})  ·  `docs/{os.path.basename(f)}`")
        body.append(t)
    total = sum(len(b.split()) for b in body)
    head = [
        f"# {TITLE}, Handbuch",
        "",
        "*Erzeugt aus `docs/`. Wird nicht bearbeitet.*",
        "",
        f"Kanon: {nchapters} Kapitel geschrieben (Stand aus dem Build, nicht von Hand).",
        f"Alle {len(files)} Dokumente am Stueck, {total:,} Woerter.".replace(",", "."),
        "Geaendert wird die Quelldatei in `docs/`, danach `python3 build.py`.",
        "",
        "## Inhalt",
        "",
    ] + toc
    write_text(os.path.join(root, "HANDBUCH.md"),
               "\n".join(head) + "\n\n---\n\n" + "\n\n---\n\n".join(body) + "\n")
    return len(files)


if __name__ == "__main__":
    main()
