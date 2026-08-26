# -*- coding: utf-8 -*-
"""anwesenheit.py - prueft, ob die Zuege einer Figur in ihrer eigenen Rede
tatsaechlich vorkommen.

    python3 anwesenheit.py            alle Figuren
    python3 anwesenheit.py Sim        eine Figur, mit Fundstellen
    python3 anwesenheit.py --eichung  nur die Selbstpruefung
    python3 anwesenheit.py --offen    welche Blaetter noch keine Probe haben

WARUM ES DIESES SKRIPT GIBT

Am 26.08. hat der Autor den Fehler unter allen anderen benannt: *"du
konzentrierst Dich bei den Markern zu sehr auf Abwesenheit und uebersiehst
mangelnde Anwesenheit von Charakterzuegen."*

`stimmen.py` misst Tics, `belege.py` prueft Zitate, `zuschreibung.py` sucht
vertauschte Taten. **Alle drei fragen, ob etwas Fremdes dasteht. Keines kann
melden, dass ein eigener Zug fehlt.** Sim war nach jeder dieser Pruefungen
sauber und klang trotzdem wie Georgij: in 71 Repliken stellt er **keine
einzige Frage**, obwohl seine ganze Methode das Fragen ist. Seine
Hoeflichkeit steht im Buch - aber in der Erzaehlung, in indirekter Rede und
in seinen eigenen Berichten ueber frueher, fast nie in der lebendigen Szene.

WIE EINE FIGUR EINE PROBE BEKOMMT

In `doc/12-stimmen.md` bekommt der Abschnitt der Figur eine Tabelle unter der
Ueberschrift **#### Anwesenheitsprobe**:

    | Zug | Muster | mind. |
    |---|---|---|
    | fragt nach einer konkreten Sache | `\b(Have you|How is|Is that)\b` | 1 |

Die Muster stehen in Backticks und sind Regexe auf die **eigene Rede** der
Figur. `mind.` ist die Untergrenze je Kapitel, in dem die Figur auftritt.

**Die Muster werden aus dem Text geholt und nicht erfunden.** Ein Muster, das
im Buch nirgends trifft, beschreibt keine Figur, sondern einen Wunsch - genau
deshalb meldet dieses Skript auch, wenn ein Muster **null** Treffer im ganzen
Buch hat.
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stimmen import zeilen_je_figur                      # noqa: E402

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLATT = os.path.join(WURZEL, "doc", "12-stimmen.md")

FRAGE = re.compile(
    r"(?:^|(?<=[.?!]) )\s*(?:And |So |Then |But |Or )?"
    r"(Who|What|Whose|When|Where|Why|How|Which|Are you|Is it|Is that|Did you"
    r"|Do you|Does|Have you|Has|Would you|Will you|Can you|Tell me)\b", re.I)


def proben():
    """{Figur: [(Zug, Regex, Mindestzahl)]} aus doc/12-stimmen.md."""
    if not os.path.exists(BLATT):
        return {}
    aus, fig, in_probe = {}, None, False
    for z in io.open(BLATT, encoding="utf-8").read().split("\n"):
        if z.startswith("### "):
            fig, in_probe = z[4:].strip(), False
        elif z.startswith("#### "):
            in_probe = "anwesenheitsprobe" in z.lower()
        elif in_probe and z.startswith("|") and "`" in z:
            # Der Regex enthaelt selbst Pipes. Erst herausnehmen, dann
            # die Zeile an den Tabellenstrichen zerlegen - sonst zerfaellt
            # das Muster in Spalten und die Mindestzahl ist Unsinn.
            m = re.search(r"`([^`]+)`", z)
            if not m:
                continue
            rest = z.replace(m.group(0), " MUSTER ")
            teile = [t.strip() for t in rest.strip("|").split("|")]
            if len(teile) < 3:
                continue
            try:
                mind = int(re.sub(r"\D", "", teile[2]) or 1)
            except ValueError:
                mind = 1
            aus.setdefault(fig, []).append((teile[0], m.group(1), mind))
    return aus


def kurzname(blattname, bekannt):
    """'Sim (dreissig Jahre Fixer, 63)' -> 'Sim', wie stimmen.py die Figur nennt."""
    for k in sorted(bekannt, key=len, reverse=True):
        if re.search(r"\b%s\b" % re.escape(k), blattname):
            return k
    return None


def eichung(daten):
    """Feste Proben aus dem Buch. Die Probe darf nicht davon abhaengen, wie der
    Text gerade aussieht - die erste Fassung hier pruefte, ob Sim null Fragen
    hat, und ging kaputt, sobald ich ihm eine gab. Eine Eichung, die eine
    Reparatur als Fehler meldet, misst die Reparatur und nicht das Werkzeug.
    """
    JA = ["Who is with her.", "How long.", "And where were you educated?",
          "Have you eaten today?", "What did the fund tell you?",
          "She asked me one. Why me."]
    NEIN = ["That is the first thing you learn and it is most of the trade.",
            "Go on.", "Say it.", "It is the first evening they have not.",
            "I have brought them anyway."]
    fehler = [s for s in JA if not FRAGE.search(s)]
    fehler += [s for s in NEIN if FRAGE.search(s)]
    print("Eichung: %s (%d Frageproben, %d Gegenproben)"
          % ("bestanden" if not fehler else "GESCHEITERT: " + fehler[0][:50],
             len(JA), len(NEIN)))
    return not fehler


def figur_report(daten, blattname, regeln, ausfuehrlich=False):
    kurz = kurzname(blattname, daten)
    if not kurz:
        return None
    rep = daten[kurz]
    kapitel = sorted({(b, c) for b, c, _ in rep})
    zeilen = []
    for zug, muster, mind in regeln:
        try:
            r = re.compile(muster, re.I)
        except re.error as e:
            zeilen.append(("  %-40s MUSTER KAPUTT: %s" % (zug[:40], e), True))
            continue
        treffer = [(b, c, q) for b, c, q in rep if r.search(q)]
        fehl = [k for k in kapitel
                if sum(1 for b, c, _ in treffer if (b, c) == k) < mind]
        marke = "" if not fehl else "  fehlt in %s" % ", ".join(
            "%s K%02d" % k for k in fehl[:6])
        zeilen.append(("  %-40s %2d Treffer, %d/%d Kapitel%s"
                       % (zug[:40], len(treffer),
                          len(kapitel) - len(fehl), len(kapitel), marke),
                       bool(fehl)))
        if ausfuehrlich:
            for b, c, q in treffer[:4]:
                zeilen.append(("      %s K%02d  %s" % (b, c, q[:88]), False))
    return kurz, len(rep), zeilen


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    daten = zeilen_je_figur()
    ok = eichung(daten)
    if "--eichung" in sys.argv:
        return 0 if ok else 1
    P = proben()
    print()

    if "--offen" in sys.argv:
        hat = {kurzname(n, daten) for n in P}
        offen = [(len(r), f) for f, r in daten.items()
                 if f not in hat and len(r) >= 5]
        print("Blaetter ohne Anwesenheitsprobe, nach Textmenge:")
        for n, f in sorted(offen, reverse=True):
            print("  %-14s %3d Repliken" % (f, n))
        return 0

    print("%-14s %6s  %s" % ("Figur", "Repl.", "Fragen je 100 Repliken"))
    print("-" * 62)
    for f, rep in sorted(daten.items(), key=lambda x: -len(x[1])):
        if len(rep) < 5 or (args and f.lower() not in [a.lower() for a in args]):
            continue
        n = sum(1 for _, _, q in rep if FRAGE.search(q))
        print("%-14s %6d  %5.1f %s" % (f, len(rep), n / len(rep) * 100,
                                       "#" * int(n / len(rep) * 100)))
    print()
    for blattname, regeln in sorted(P.items()):
        e = figur_report(daten, blattname, regeln, ausfuehrlich=bool(args))
        if not e:
            continue
        kurz, n, zeilen = e
        if args and kurz.lower() not in [a.lower() for a in args]:
            continue
        print("%s - %d Repliken" % (blattname, n))
        for text, _ in zeilen:
            print(text)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
