#!/usr/bin/env python3
"""sprechbefehl.py - wer im Buch befiehlt zu reden, und wie oft.

**Der Befund vom 26.08.** (`doc/23-kuerzen.md`): von 10.555 Repliken fangen 577
mit einem Befehl zum Sprechen an - *"Say it"*, *"Say the whole of it"*, *"Say
why"*, *"Go on"*, *"Then say"* - und sie stehen in 113 von 123 Kapiteln. Das ist
kein Sprachzug mehr, sondern der Standardweg dieses Buches, eine Auskunft zu
verlangen, und **alle Figuren benutzen ihn**.

**Die Entscheidung des Autors, 26.08.:** *"Annie und Sang-hoon behalten ihn,
mach den Rest."* Bei diesen beiden traegt die Machtlage den Befehl. Bei allen
anderen wird er ersetzt.

Dieses Skript entscheidet nichts. Es **zeigt, wo die Stellen sind und wem sie
gehoeren**, damit der Ersatz je Figur geschrieben werden kann und nicht als
Suchen-und-Ersetzen ueber das ganze Buch laeuft.

    python3 sprechbefehl.py            Verteilung je Figur
    python3 sprechbefehl.py --liste    jede Stelle mit Kapitel und Zeile
    python3 sprechbefehl.py --figur X  nur diese Figur

**Die Zuordnung ist das Schwierige, und der Kopfkommentar von stimmen.py sagt
warum:** in Zweipersonenszenen laeuft der Dialog ohne Begleitsaetze. Wer nur
`said X` zaehlt, findet die Haelfte nicht. Dieses Skript nimmt deshalb den
Begleitsatz, wo einer dasteht, und **faellt sonst auf Abwechslung zurueck** -
in einer Szene mit genau zwei bekannten Sprechern gehoert eine Replik ohne
Begleitsatz dem, der zuletzt nicht dran war. Wo das nicht entscheidbar ist,
steht `?` und die Stelle wird von Hand angesehen.
"""
import os
import re
import sys
from collections import Counter, defaultdict

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Der Befehl selbst. "Tell me" ist derselbe Zug mit einem anderen Verb und
# gehoert dazu; "Go on" ist die Aufforderung weiterzureden und ebenfalls.
BEFEHL = re.compile(
    r'^\s*(?:and |then |now |but )?(?:say|tell me|go on)\b', re.I)

REPLIK = re.compile(r'"([^"]{2,})"')
BEGLEIT = re.compile(
    r'(?:said|asked|shrugged|added|repeated) (?:[A-Z][a-z-]+ )?([A-Z][A-Za-z-]+(?: [A-Z][a-z-]+)?)'
    r'|\b((?:Mr|Mrs|Chairman) [A-Z][a-z-]+|[A-Z][a-z-]+(?: [A-Z][a-z-]+)?) (?:said|asked|shrugged|added|repeated)\b')

# Wer im Buch ueberhaupt spricht. Alles andere ist ein Fehlgriff des Regex.
FIGUREN = {
    "Annie", "Georgij", "Sang-hoon", "Park Sang-hoon", "Woo", "Chairman Woo",
    "Sim", "Jang", "Hana", "Ye-rin", "Kim Ye-rin", "Do-yun", "Shin", "Mrs Seo",
    "Mr Ku", "Mr Ahn", "Mrs Jeon", "Mr Hwang", "Hwang", "Mrs Ha", "Mr Byun",
    "Mr Yeom", "Mrs Sunwoo", "Sunwoo", "Mr Ok", "Mr Koh", "Mr Tak", "Mr Pyeon",
    "Nam Byung-hee", "Baek Jun-ho", "Baek", "Ahn Jung-hee", "Choi", "Choi Dae-ho",
    "Mrs Bae", "Mrs Gwak", "Mr Noh", "Mr Yeo", "Moon Hae-sook", "Mr Kwon",
}

# Die beiden, die ihn behalten. Autorenentscheidung vom 26.08.
BEHALTEN = {"Annie", "Sang-hoon", "Park Sang-hoon"}


def kapitel():
    aus = []
    for ordner, band in (("chapters", "b1"), ("chapters-2", "b2")):
        pfad = os.path.join(WURZEL, ordner)
        if not os.path.isdir(pfad):
            continue
        neuste = {}
        for name in sorted(os.listdir(pfad)):
            m = re.match(r"ch(\d\d)_v(\d+)_(\d+)_en\.md$", name)
            if m:
                num, ver = int(m.group(1)), (int(m.group(2)), int(m.group(3)))
                if num not in neuste or ver > neuste[num][0]:
                    neuste[num] = (ver, name)
        for num in sorted(neuste):
            pfadname = os.path.join(pfad, neuste[num][1])
            with open(pfadname, encoding="utf-8") as f:
                aus.append(("%s %02d" % (band, num), neuste[num][1], f.read()))
    return aus


def _figur(name):
    if not name:
        return None
    name = name.strip()
    if name in FIGUREN:
        return name
    # "Chairman Woo" -> "Woo", "Park Sang-hoon" -> "Sang-hoon"
    teile = name.split()
    if teile and teile[-1] in FIGUREN:
        return teile[-1]
    return None


def sprecher_der_zeile(zeile):
    """Der Sprecher aus dem Begleitsatz, wenn einer dasteht."""
    # Nur ausserhalb der Anfuehrungszeichen suchen, sonst faengt man den
    # Begleitsatz eines Zitats innerhalb einer fremden Replik.
    aussen = REPLIK.sub(" ", zeile)
    m = BEGLEIT.search(aussen)
    if not m:
        return None
    return _figur(m.group(1) or m.group(2))


# Ein Absatz, der mit einem Figurennamen anfaengt, gehoert dieser Figur - das
# ist Regel 5 aus CLAUDE.md, rueckwaerts gelesen. "Annie picked up the pen and
# put it down again." leitet Annies Replik ein, auch ohne "said Annie".
BEAT = re.compile(
    r'^((?:Mr|Mrs|Chairman) [A-Z][a-z-]+|[A-Z][a-z-]+(?:-[a-z]+)?(?: [A-Z][a-z-]+)?)\s+'
    r'(?![A-Z])[a-z]')


def beat_figur(zeile):
    """Die Figur, die den Absatz anfaengt, wenn es eine ist."""
    m = BEAT.match(zeile.strip())
    return _figur(m.group(1)) if m else None


def _szenen(text):
    """Der Text, zerlegt in Szenen, jede Szene als Liste von (Zeilennr, Zeile)."""
    szenen, jetzt = [], []
    for nr, zeile in enumerate(text.split("\n"), 1):
        s = zeile.strip()
        if s in ("* * *", "---") or s.startswith("## ") or s.startswith("# "):
            if jetzt:
                szenen.append(jetzt)
            jetzt = []
            continue
        jetzt.append((nr, zeile))
    if jetzt:
        szenen.append(jetzt)
    return szenen


def _teilnehmer(szene, kapitel_getaggt):
    """Wer in dieser Szene spricht.

    Erst die Begleitsaetze der Szene. Reicht das nicht fuer zwei, wird aus den
    Begleitsaetzen des ganzen Kapitels aufgefuellt, und zuletzt mit Georgij:
    er ist die Blickpunktfigur, in fast jeder Szene der zweite Mensch im Raum,
    und bekommt gerade deshalb am seltensten einen Begleitsatz."""
    getaggt = []
    for _, zeile in szene:
        w = (sprecher_der_zeile(zeile) if REPLIK.search(zeile)
             else beat_figur(zeile))
        if w and w not in getaggt:
            getaggt.append(w)
    if len(getaggt) > 2:
        return getaggt, False          # mehr als zwei: nicht abwechselbar
    teilnehmer = list(getaggt)
    for w in kapitel_getaggt:
        if len(teilnehmer) >= 2:
            break
        if w not in teilnehmer:
            teilnehmer.append(w)
    if len(teilnehmer) < 2 and "Georgij" not in teilnehmer:
        teilnehmer.append("Georgij")
    return teilnehmer, len(teilnehmer) == 2


def stellen():
    """Jede Replik, die mit einem Sprechbefehl anfaengt, mit Sprecher.

    **Die Abwechslung laeuft von jedem bekannten Punkt aus in beide
    Richtungen.** Ein Begleitsatz in der Mitte einer Szene bestimmt damit auch
    die Repliken davor. Der erste Lauf am 26.08. hat nur vorwaerts gerechnet
    und brauchte einen Begleitsatz vor der ersten Replik - die gibt es selten,
    und deshalb blieben 516 von 672 Stellen unzugeordnet.

    **Wo drei oder mehr Sprecher einen Begleitsatz haben, wird nicht geraten.**
    Abwechslung ist dort keine Regel, sondern ein Wunsch."""
    aus = []
    for marke, datei, text in kapitel():
        kapitel_getaggt = []
        for zeile in text.split("\n"):
            w = sprecher_der_zeile(zeile) if REPLIK.search(zeile) else None
            if w and w not in kapitel_getaggt:
                kapitel_getaggt.append(w)

        for szene in _szenen(text):
            zuege = []                  # (Zeilennr, Repliken, Sprecher oder None)
            vorheriger_beat = None
            for nr, zeile in szene:
                repliken = REPLIK.findall(zeile)
                if not repliken:
                    if zeile.strip():
                        vorheriger_beat = beat_figur(zeile)
                    continue
                # 1. der Begleitsatz. 2. der eigene Absatzanfang. 3. der Beat
                # im Absatz davor. Alle drei sind dieselbe Auskunft in drei
                # Schreibweisen, und das Buch benutzt alle drei.
                wer = (sprecher_der_zeile(zeile)
                       or beat_figur(zeile)
                       or vorheriger_beat)
                vorheriger_beat = None
                zuege.append([nr, repliken, wer])
            if not zuege:
                continue

            teilnehmer, wechselbar = _teilnehmer(szene, kapitel_getaggt)
            bekannt = [i for i, z in enumerate(zuege) if z[2]]
            if wechselbar and bekannt:
                a, b = teilnehmer
                for i, zug in enumerate(zuege):
                    if zug[2]:
                        continue
                    # der naechstgelegene bekannte Zug entscheidet
                    k = min(bekannt, key=lambda j: abs(j - i))
                    basis = zuege[k][2]
                    if basis not in (a, b):
                        continue
                    gegen = b if basis == a else a
                    zug[2] = basis if (i - k) % 2 == 0 else gegen

            for nr, repliken, wer in zuege:
                for r in repliken:
                    if BEFEHL.match(r):
                        aus.append((marke, datei, nr, wer or "?", r))
    return aus


def verteilung():
    alle = stellen()
    z = Counter(w for _, _, _, w, _ in alle)
    kaps = defaultdict(set)
    for marke, _, _, w, _ in alle:
        kaps[w].add(marke)

    print("SPRECHBEFEHLE, NACH SPRECHER (%d Stellen)\n" % len(alle))
    print("  Anzahl  Kapitel  Sprecher")
    behalten = weg = unklar = 0
    for w, n in z.most_common():
        rest = "behaelt ihn" if w in BEHALTEN else (
            "von Hand ansehen" if w == "?" else "**ersetzen**")
        print("  %6d  %7d  %-16s %s" % (n, len(kaps[w]), w, rest))
        if w in BEHALTEN:
            behalten += n
        elif w == "?":
            unklar += n
        else:
            weg += n
    print("\n  %d bleiben (Annie, Sang-hoon), %d sind zu ersetzen, "
          "%d nicht zugeordnet." % (behalten, weg, unklar))
    return 0


def liste(nur=None):
    for marke, datei, nr, wer, r in stellen():
        if nur and wer != nur:
            continue
        if not nur and wer in BEHALTEN:
            continue
        print("  %s  Z%-4d  %-14s \"%s\"" % (marke, nr, wer, r[:96]))
    return 0


if __name__ == "__main__":
    if "--figur" in sys.argv:
        sys.exit(liste(sys.argv[sys.argv.index("--figur") + 1]))
    if "--liste" in sys.argv:
        sys.exit(liste())
    sys.exit(verteilung())
