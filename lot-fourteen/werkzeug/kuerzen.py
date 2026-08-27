#!/usr/bin/env python3
"""kuerzen.py - welche Kapitel sind Kuerzungskandidaten, und welche nicht.

**Der Anlass steht in `doc/23-kuerzen.md`:** der Band wird zu Ende geschrieben
und danach gekuerzt, und die Gefahr dabei ist, dass nach Gefuehl gekuerzt wird.
Gemessen ist der Befund eindeutig - ueber achtzig Kapitel schwankt die
Erzaehlgeschwindigkeit um keine dreissig Prozent, achtzig von achtzig Kapiteln
spielen an genau einem Tag, und dreissig von achtzig enden im selben Zimmer mit
derselben Person. **Das Buch hat einen Gang.**

Dieses Werkzeug entscheidet **nicht**, was gekuerzt wird. Das ist Urteil und
steht in `doc/23-kuerzen.md`. Es beantwortet die eine Frage, die mechanisch
beantwortbar ist:

    **Traegt dieses Kapitel etwas, das nirgends sonst steht?**

Drei Kriterien, und sie kommen aus `doc/23-kuerzen.md`:

1. **Es bezahlt eine Zusage.** Aus `doc/13-zusagen.md`, Feld *eingeloest*.
2. **Es steht im Naehe-Register.** Aus `doc/10-naehe.md`.
3. **Es enthaelt einen Erstauftritt.** Aus `FIGURES` in `build.py`, ueber alle
   Kapitel beider Baende gerechnet.
4. **Es traegt einen Stimmbefund.** Aus `doc/12-stimmen.md`. Das vierte
   Kriterium ist absichtlich das schwaechste: dieses Dokument verweist auf 74
   der 114 Kapitel, also trennt es allein gar nichts. **Es rettet aber Kapitel,
   die die anderen drei uebersehen** - b2 K62 zum Beispiel traegt Annies
   einzigen Registerbruch im ganzen Buch und steht in keinem der ersten drei.

Ein Kapitel, auf das keins der drei zutrifft, ist ein **Kandidat**. Nicht mehr
und nicht weniger: es kann trotzdem unverzichtbar sein, weil es eine Wendung
traegt, die in keinem der drei Dokumente steht. **Deshalb heisst die Spalte
Kandidat und nicht Streichen.**

    python3 kuerzen.py              alle Kapitel, mit Befund
    python3 kuerzen.py --kandidaten nur die ohne Traglast
    python3 kuerzen.py --form       die Formzahlen: Dialoganteil, Szenen, Tage

**Die Grenze, und sie ist dieselbe wie bei allen Werkzeugen hier:** was nicht
in einem der vier Dokumente steht, sieht dieses Skript nicht. Wer ein Kapitel
streicht, weil es hier als Kandidat steht, ohne es gelesen zu haben, hat das
Werkzeug missverstanden.

**Und eine zweite Grenze, die beim Bau aufgefallen ist und bleibt:** ein
Verweis ohne Bandpraefix ist unsichtbar. `doc/12-stimmen.md` schreibt an
mehreren Stellen *"in Kapitel 62"* statt *"b2 K62"*, und ohne Band laesst sich
nicht entscheiden, welcher Band gemeint ist. **Raten waere schlimmer als
uebersehen**, also uebersieht dieses Skript sie. Wer die Kandidatenliste
abarbeitet, prueft jeden Treffer gegen `doc/15-kalender.md`, wo jedes Kapitel
beschrieben steht.
"""
import os
import re
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(WURZEL, "werkzeug"))

# Die Dokumente schreiben Kapitelverweise in drei Formen, und alle drei kommen
# vor: "B2 71", "b2ch71" und "b2 K71". Wer nur eine davon kennt, uebersieht ein
# ganzes Dokument - doc/12-stimmen.md benutzt fast nur die dritte, und in der
# ersten Fassung dieses Skripts stand K62 deshalb als Kandidat da, obwohl es
# Annies einzigen Registerbruch traegt.
KAPITEL_REF = re.compile(r"\b[Bb]([12])\s*(?:ch|K)?\s*(\d{1,2})\b")


def neuste_kapitel():
    """(band, nummer, pfad, text) je Kapitel, nur die hoechste Fassung."""
    aus = []
    for ordner, band in (("chapters", "B1"), ("chapters-2", "B2")):
        pfad = os.path.join(WURZEL, ordner)
        if not os.path.isdir(pfad):
            continue
        best = {}
        for name in sorted(os.listdir(pfad)):
            m = re.match(r"ch(\d\d)_v(\d+)_(\d+)_en\.md$", name)
            if not m:
                continue
            k = int(m.group(1))
            v = (int(m.group(2)), int(m.group(3)))
            if k not in best or v > best[k][0]:
                best[k] = (v, name)
        for k in sorted(best):
            p = os.path.join(pfad, best[k][1])
            with open(p, encoding="utf-8") as f:
                aus.append((band, k, p, f.read()))
    return aus


def referenzen(pfad, nur_feld=None):
    """Alle Kapitelverweise in einem Dokument, als Menge {("B2", 71), ...}.

    `nur_feld` schneidet jede Zeile am letzten Mitteltrenner ab, sodass nur
    das Feld *eingeloest* gelesen wird. Ohne das zaehlt im Schuldbuch auch das
    Kapitel mit, in dem die Zusage **gegeben** wurde, und das ist etwas
    anderes als Bezahlen.
    """
    voll = os.path.join(WURZEL, pfad)
    if not os.path.exists(voll):
        return set()
    treffer = set()
    with open(voll, encoding="utf-8") as f:
        for zeile in f:
            if nur_feld:
                teile = zeile.split(" · ")
                if len(teile) < 2:
                    continue
                zeile = teile[-1]
            for m in KAPITEL_REF.finditer(zeile):
                treffer.add(("B" + m.group(1), int(m.group(2))))
    return treffer


def erstauftritte(kaps):
    """{(band, nummer): [Figur, ...]} - wo eine Figur zum ersten Mal vorkommt."""
    try:
        from build import FIGURES
    except Exception:
        print("build.py nicht importierbar, Erstauftritte werden uebersprungen.")
        return {}
    gesehen = set()
    aus = {}
    for band, num, _pfad, text in kaps:
        for figur, muster in FIGURES.items():
            if figur in gesehen:
                continue
            if any(re.search(m, text) for m in muster):
                gesehen.add(figur)
                aus.setdefault((band, num), []).append(figur)
    return aus


def form(text):
    """Dialoganteil, Szenenzahl, Erzaehltage, Woerter."""
    zeilen = [z.strip() for z in text.split("\n") if z.strip()]
    inhalt = [z for z in zeilen
              if z not in ("---", "* * *")
              and not z.startswith("#")
              and not z.startswith("*Lot")]
    rede = [z for z in inhalt if z.startswith('"')]
    return {
        "dialog": (100.0 * len(rede) / len(inhalt)) if inhalt else 0.0,
        "szenen": sum(1 for z in zeilen if z == "* * *") + 1,
        "tage": len(re.findall(r"^## Days? ", text, re.M)),
        "woerter": len(text.split()),
    }


def lauf(nur_kandidaten=False, nur_form=False):
    kaps = neuste_kapitel()
    bezahlt = referenzen("doc/13-zusagen.md", nur_feld=True)
    naehe = referenzen("doc/10-naehe.md")
    stimme = referenzen("doc/12-stimmen.md")
    erst = erstauftritte(kaps)

    if nur_form:
        print("Kap      Dialog  Szenen  Tage  Woerter")
        for band, num, _p, text in kaps:
            f = form(text)
            print("%s %02d   %5.0f%%  %6d  %4d  %7d"
                  % (band, num, f["dialog"], f["szenen"], f["tage"], f["woerter"]))
        return 0

    kandidaten = []
    print("Kap     Zusage  Naehe  Stimme  Erstauftritt")
    for band, num, _p, text in kaps:
        z = (band, num) in bezahlt
        n = (band, num) in naehe
        s = (band, num) in stimme
        e = erst.get((band, num), [])
        traegt = z or n or s or e
        if not traegt:
            kandidaten.append((band, num, form(text)))
        if nur_kandidaten and traegt:
            continue
        print("%s %02d      %s      %s     %s   %s"
              % (band, num,
                 "ja " if z else "-  ",
                 "ja " if n else "-  ",
                 "ja " if s else "-  ",
                 ", ".join(e) if e else "-"))

    print()
    print("%d von %d Kapiteln tragen keins der vier Merkmale."
          % (len(kandidaten), len(kaps)))
    if kandidaten:
        woerter = sum(k[2]["woerter"] for k in kandidaten)
        print("Zusammen %d Woerter. **Das ist eine Leseliste und keine "
              "Streichliste.**" % woerter)
        print("Jeden Treffer gegen doc/15-kalender.md pruefen: ein Verweis "
              "ohne Bandpraefix ist hier unsichtbar.")
    return 0


if __name__ == "__main__":
    sys.exit(lauf(nur_kandidaten="--kandidaten" in sys.argv,
                  nur_form="--form" in sys.argv))
