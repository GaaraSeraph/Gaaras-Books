Lot Fourteen. Literarischer Roman, laufende Arbeit. Suedkorea, Gegenwart,
Chaebol-Milieu. Manuskript auf Englisch, Absprachen auf Deutsch.

<img src="cover/lot-fourteen.jpg" alt="Cover: Lot Fourteen" width="360">

    chapters/    die Kapitel von Band 1, chNN_vX_Y_en.md
    chapters-2/  die Kapitel von Band 2
    doc/         die Quelldokumente, nach Sorte nummeriert
    erzeugt/     alles, was build.py schreibt
    cover/       Coverbild

**Start mit CLAUDE.md.** Dort stehen zuerst die drei Ablageregeln, dann die
Formatregeln, die Stimme und die Kontinuitaets-Fallen.

## Die Ablage

Die **Zehnerstelle ist die Sorte**, und in jedem Block sind Nummern frei:

    1x  Kanon      was im Buch wahr ist        Praesens, nie datiert
    2x  Regeln     was beim Schreiben bindet   Imperativ, nie datiert
    3x  Plan       was noch geschehen soll     Futur, je Band
    4x  Verworfen  was schon abgelehnt wurde
        protokoll/ alles Datierte, append-only, gewinnt nie

**Bei einem Widerspruch gilt: Kanon vor Regel vor Plan.**

## Was wo steht

Lesefassung je Band: `book-band-1.md` und `book-band-2.md`. Alle Dokumente am
Stueck: `erzeugt/HANDBUCH.md`. **Welches Kapitel an welchem Tag spielt:
`erzeugt/KAPITEL.md`**, eine Zeile je Kapitel, aus den Kapitelkoepfen erzeugt.
Welche Datei gilt und wie lang sie ist: `erzeugt/MANIFEST.txt`. Was als
Naechstes kommt: `doc/31-plan-band-2.md`.

<!-- ZAHLEN -->

---

*Erzeugt von `build.py`. Nicht von Hand aendern.*

**16 Quelldokumente** in `doc/`, dazu das Archiv in `doc/protokoll/`.
**117 Kapitel, 327.529 Woerter.**
