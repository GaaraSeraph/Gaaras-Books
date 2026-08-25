#!/usr/bin/env python3
"""stimmen.py - misst, wie verschieden die Figuren tatsaechlich reden.

Der Befund in doc/12-stimmen.md ist mit der Hand gezaehlt worden. Dieses
Skript zaehlt ihn nach und haelt ihn aktuell, damit nach jedem Durchgang
nachpruefbar ist, ob sich etwas bewegt hat.

    python3 stimmen.py              die Tabelle ueber alle Sprecher
    python3 stimmen.py Jang         alle zugeordneten Zeilen einer Figur
    python3 stimmen.py --tics       wer welche der fuenf Haustics benutzt
    python3 stimmen.py --anrede     wer wen wie anredet

**Die zweite Grenze: Zweipersonenszenen.** Wo zwei Leute allein reden, laeuft
der Dialog im blossen Wechsel ohne Begleitsaetze. Kim Ye-rin hat in Band 1,
Kapitel 30 ein ganzes Kapitel und findet sich hier mit fuenf Zeilen. **Eine
niedrige Zahl heisst nicht wenig Text, sondern wenig Begleitsatz** - fuer solche
Figuren wird das Kapitel gelesen und nicht gezaehlt.

**Die Zuordnung ist die Falle, und sie hat mich schon zweimal erwischt.**
Ein Begleitsatz im Text ("said Mrs Seo") kann innerhalb einer fremden Replik
stehen, weil eine Figur eine andere zitiert. Deshalb wird die Replik nur
zugeordnet, wenn der Begleitsatz **ausserhalb** aller Anfuehrungszeichen der
Zeile steht. Wer das weglaesst, schreibt Georgijs Saetze in fremde Blaetter.
"""
import os
import re
import sys
import collections

FIGUREN = ["Georgij", "Annie", "Sang-hoon", "Hana", "Jang", "Woo", "Mrs Seo",
           "Ye-rin", "Sim", "Byun", "Chae", "Yeom", "Hwang", "Mrs Jeon", "Mrs Bae",
           "Mrs Gwak", "Sohn", "Ahn", "Koh", "Ji-won", "Do-yun", "Sung-ho", "Hong",
           "Kang", "Pyo", "Ku", "Bae"]

EINHEITEN = {
    "Jahre":    r"\b(year|years)\b",
    "Tage":     r"\b(day|days)\b",
    "Wochen":   r"\b(week|weeks)\b",
    "Monate":   r"\b(month|months)\b",
    "Minuten":  r"\b(minute|minutes|second|seconds|hour|hours)\b",
    "Geld":     r"\b(won|billion|million)\b",
    "Personen": r"\b(people|men|women|person|man|woman)\b",
    "Datum":    r"\b(January|February|March|April|May|June|July|August|"
                r"September|October|November|December)\b",
}

TICS = {
    "which-Satz":      r",\s*which (is|was|means|is not|is what|is how)\b",
    "Und-Kette":       r"\band\b[^.,]{3,40},?\s*\band\b[^.,]{3,40},?\s*\band\b",
    "Negativ-Def":     r"\bNot [a-z][^.]{0,30}\.\s+Not \b",
    "Selbstdiagnose":  r"\bI have (stopped|never been able to|got as far as|"
                       r"given up)\b",
    "Kontraktion":     r"\b\w+'(?:s|t|re|ve|ll|d|m)\b",
    "Ausrufezeichen":  r"!",
    "soziale Frage":   r",\s*(is it|isn't it|are you|aren't you)\?",
}


def kanon():
    """Hoechste Fassung je Kapitel, aus dem Verzeichnis und nie aus MANIFEST."""
    for band, d in (("b1", "chapters"), ("b2", "chapters-2")):
        best = {}
        for n in os.listdir(d):
            m = re.match(r"ch(\d+)_v(\d+)_(\d+)_en\.md$", n)
            if not m:
                continue
            ch = int(m.group(1))
            v = (int(m.group(2)), int(m.group(3)))
            if ch not in best or v > best[ch][0]:
                best[ch] = (v, os.path.join(d, n))
        for ch in sorted(best):
            yield band, ch, best[ch][1]


def ausserhalb(zeile, treffer):
    """Steht die Fundstelle ausserhalb aller Anfuehrungszeichen?"""
    return zeile[:treffer].count('"') % 2 == 0


def zeilen_je_figur():
    """(band, kapitel, replik) je Figur. Nur sichere Zuordnungen."""
    aus = collections.defaultdict(list)
    for band, ch, f in kanon():
        for zeile in open(f, encoding="utf-8").read().split("\n"):
            if '"' not in zeile:
                continue
            for fig in FIGUREN:
                # Ein Vorname oder Titel darf dazwischenstehen: "said Kim Ye-rin",
                # "said Chairman Woo", "said Park Sang-hoon", "said Mr Koh".
                pat = (r"(?:said|asked|shrugged|added|repeated) (?:[A-Z][a-z-]+ )?%s\b"
                       r"|\b(?:[A-Z][a-z-]+ )?%s (?:said|asked|shrugged|added|repeated)\b") % (
                    re.escape(fig), re.escape(fig))
                m = re.search(pat, zeile)
                if not m or not ausserhalb(zeile, m.start()):
                    continue
                for q in re.findall(r'"([^"]+)"', zeile):
                    aus[fig].append((band, ch, q))
                break
    return aus


def tabelle(daten):
    print("%-12s %6s %7s %6s %7s  %s" % ("Figur", "Zeilen", "Woerter", "Ø Satz", ">25 W", "zaehlt am dichtesten"))
    print("-" * 92)
    for fig in sorted(daten, key=lambda f: -len(daten[f])):
        qs = [q for _, _, q in daten[fig]]
        if len(qs) < 5:
            continue
        w = sum(len(q.split()) for q in qs)
        saetze = [s for q in qs for s in re.split(r"(?<=[.?!])\s+", q) if s.strip()]
        lang = sum(1 for s in saetze if len(s.split()) > 25)
        t = " ".join(qs)
        top = sorted(((len(re.findall(p, t)) / w * 1000, k)
                      for k, p in EINHEITEN.items()), reverse=True)[:2]
        print("%-12s %6d %7d %6.1f %6.0f%%  %s" % (
            fig, len(qs), w, w / len(saetze), lang / len(saetze) * 100,
            ", ".join("%s %.1f" % (k, v) for v, k in top)))


def tics(daten):
    print("%-12s %6s  %s" % ("Figur", "Woerter", "Haustics je 1000 Woerter"))
    print("-" * 92)
    for fig in sorted(daten, key=lambda f: -len(daten[f])):
        qs = [q for _, _, q in daten[fig]]
        if len(qs) < 5:
            continue
        w = sum(len(q.split()) for q in qs)
        t = " ".join(qs)
        teile = []
        for name, p in TICS.items():
            n = len(re.findall(p, t))
            if n:
                teile.append("%s %.1f" % (name, n / w * 1000))
        print("%-12s %6d  %s" % (fig, w, ", ".join(teile) or "-"))


def anrede(daten):
    formen = ["Mistress", "ma'am", "Chairman", "sir"]
    print("%-12s  %s" % ("Sprecher", "  ".join("%-9s" % f for f in formen)))
    print("-" * 60)
    for fig in sorted(daten, key=lambda f: -len(daten[f])):
        qs = [q for _, _, q in daten[fig]]
        if len(qs) < 5:
            continue
        t = " ".join(qs)
        zahlen = [t.count(f) for f in formen]
        if any(zahlen):
            print("%-12s  %s" % (fig, "  ".join("%-9d" % z for z in zahlen)))


def einzeln(daten, fig):
    treffer = [k for k in daten if k.lower() == fig.lower()]
    if not treffer:
        print("Kein Sprecher %r. Bekannt sind: %s" % (fig, ", ".join(sorted(daten))))
        return
    for band, ch, q in daten[treffer[0]]:
        print("  %s K%02d  %s" % (band, ch, q))
    print("\n  %d Repliken" % len(daten[treffer[0]]))


if __name__ == "__main__":
    daten = zeilen_je_figur()
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--tics":
        tics(daten)
    elif arg == "--anrede":
        anrede(daten)
    elif arg:
        einzeln(daten, arg)
    else:
        tabelle(daten)
