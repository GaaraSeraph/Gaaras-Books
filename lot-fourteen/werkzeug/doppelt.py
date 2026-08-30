#!/usr/bin/env python3
"""doppelt.py - was steht zweimal da, und welcher Gespraechszug laeuft immer gleich.

Der Autor am 26.08.: *"guck was mehrfach behauptet wird und damit redundant
wird, und welche Gespraechspassagen redundant sind."* Das sind **zwei
verschiedene Fragen**, und sie brauchen zwei verschiedene Messungen.

`check.py` findet bereits woertliche Doubletten **innerhalb** eines Kapitels.
Das reicht nicht. Was dieses Buch zaeh macht, ist die Behauptung, die in
Kapitel 61 aufgestellt, in 72 wiederholt und in 84 noch einmal erklaert wird,
jedes Mal mit anderen Woertern. Woertlich stimmt keine Zeile mit einer anderen
ueberein, und der Leser hat es trotzdem dreimal gelesen.

    python3 doppelt.py                Behauptungen, die in mehreren Kapiteln stehen
    python3 doppelt.py --oeffner      womit Repliken anfangen, nach Haeufigkeit
    python3 doppelt.py --ketten       Gespraechszuege, die mehrfach gleich laufen
    python3 doppelt.py --nester       Behauptungen in drei oder mehr Kapiteln
    python3 doppelt.py --kapitel 78   nur ein Kapitel, gegen alle anderen

**Die Grenze, und sie ist dieselbe wie bei stimmen.py:** das Skript entscheidet
nicht, ob eine Wiederholung schaedlich ist. Manche sind Absicht - ein Motiv,
ein Rueckruf, ein Satz, den eine Figur zweimal sagen soll. Das Skript legt sie
nebeneinander und zaehlt, und **das Urteil bleibt Lesearbeit**. Ein Werkzeug,
das hier automatisch streicht, wuerde die besten Stellen des Buches zuerst
erwischen.
"""
import os
import re
import sys
from collections import Counter, defaultdict

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Wieviele der haeufigsten Wortformen als Fuellwort gelten. Bei 300 fallen
# "would", "because", "anything" heraus und "consignment", "guttering",
# "Gwangyang" bleiben drin - und nur die Letzteren machen eine Behauptung
# wiedererkennbar.
FUELLWOERTER = 300

WORT = re.compile(r"[a-z][a-z'-]*")
SATZ = re.compile(r'(?<=[.?!])\s+(?=[A-Z"*])')
REPLIK = re.compile(r'"([^"]{3,})"')


def kapitel():
    """Aktuelle Fassung jedes Kapitels: (Marke, Text)."""
    aus = []
    for ordner, band in (("chapters", "b1"), ("chapters-2", "b2"), ("chapters-3", "b3")):
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
            with open(os.path.join(pfad, neuste[num][1]), encoding="utf-8") as f:
                aus.append(("%s %02d" % (band, num), f.read()))
    return aus


def saetze(text):
    """Saetze ohne Kopfzeilen, Datumszeilen und Trenner."""
    aus = []
    for absatz in text.split("\n\n"):
        a = absatz.strip()
        if not a or a.startswith("#") or a.startswith("*") and a.endswith("*"):
            continue
        if a in ("* * *", "---") or a.startswith("## "):
            continue
        for s in SATZ.split(a.replace("\n", " ")):
            s = s.strip()
            if len(s.split()) >= 6:
                aus.append(s)
    return aus


def fuellwoerter(alle):
    z = Counter()
    for _, text in alle:
        z.update(WORT.findall(text.lower()))
    return set(w for w, _ in z.most_common(FUELLWOERTER))


def kern(satz, fuell):
    """Die Inhaltswoerter eines Satzes, ohne Fuellwoerter, als Menge."""
    return set(w for w in WORT.findall(satz.lower())
               if w not in fuell and len(w) > 2)


def behauptungen(nur=None, schwelle=0.55, mindest=4):
    """Satzpaare aus verschiedenen Kapiteln mit fast demselben Inhalt."""
    alle = kapitel()
    fuell = fuellwoerter(alle)

    eintraege = []
    for marke, text in alle:
        for s in saetze(text):
            k = kern(s, fuell)
            if len(k) >= mindest:
                eintraege.append((marke, s, k))

    # Ohne Index waeren das gut zweihundert Millionen Vergleiche. Verglichen
    # wird nur, was mindestens drei seltene Woerter teilt.
    index = defaultdict(list)
    for i, (_, _, k) in enumerate(eintraege):
        for w in k:
            index[w].append(i)

    gesehen, treffer = set(), []
    for i, (marke_i, satz_i, k_i) in enumerate(eintraege):
        if nur and marke_i != nur:
            continue
        kandidaten = Counter()
        for w in k_i:
            # Ein Wort, das in tausend Saetzen steht, trennt nichts.
            if len(index[w]) > 60:
                continue
            for j in index[w]:
                if j != i:
                    kandidaten[j] += 1
        for j, geteilt in kandidaten.items():
            if geteilt < 3:
                continue
            marke_j, satz_j, k_j = eintraege[j]
            if marke_j == marke_i:
                continue
            paar = tuple(sorted((i, j)))
            if paar in gesehen:
                continue
            gesehen.add(paar)
            jac = len(k_i & k_j) / float(len(k_i | k_j))
            if jac >= schwelle:
                treffer.append((jac, marke_i, satz_i, marke_j, satz_j))

    treffer.sort(reverse=True)
    if not treffer:
        print("Keine Behauptung steht zweimal, gemessen mit Schwelle %.2f." % schwelle)
        return 0

    print("BEHAUPTUNGEN, DIE IN ZWEI KAPITELN STEHEN (%d)\n" % len(treffer))
    print("Die Zahl links ist die Ueberlappung der Inhaltswoerter. Ab etwa 0.75")
    print("ist es dieselbe Aussage, darunter oft eine bewusste Wiederaufnahme.\n")
    for jac, m1, s1, m2, s2 in treffer[:80]:
        print("  %.2f  %s  %s" % (jac, m1, s1[:150]))
        print("        %s  %s\n" % (m2, s2[:150]))
    if len(treffer) > 80:
        print("  ... und %d weitere. Schwelle hochsetzen: --schwelle 0.7"
              % (len(treffer) - 80))
    return 0


def _oeffner(replik, n=2):
    w = WORT.findall(replik.lower())
    return " ".join(w[:n]) if len(w) >= n else None


def oeffner():
    """Womit Repliken anfangen. Ein Buch, in dem vierzig Repliken mit
    demselben Wortpaar beginnen, hat einen Bau und keine Figuren."""
    alle = kapitel()
    z = Counter()
    wo = defaultdict(set)
    gesamt = 0
    for marke, text in alle:
        for r in REPLIK.findall(text):
            o = _oeffner(r)
            if o:
                z[o] += 1
                wo[o].add(marke)
                gesamt += 1

    print("REPLIK-ANFAENGE (%d Repliken insgesamt)\n" % gesamt)
    print("  Anzahl  Kapitel  Anfang")
    for o, n in z.most_common(40):
        if n < 5:
            break
        print("  %6d  %7d  \"%s ...\"" % (n, len(wo[o]), o))
    print("\nEin Anfang, der in mehr als der Haelfte der Kapitel vorkommt, ist")
    print("kein Sprachzug mehr, sondern ein Geraeusch.")
    return 0


def ketten(mindestlaenge=3):
    """Gespraechszuege, die mehrfach in derselben Reihenfolge laufen.

    Jede Replik wird auf ihre ersten zwei Woerter reduziert. Wenn dieselbe
    Folge von drei oder mehr Reduktionen in mehreren Kapiteln vorkommt, laeuft
    dort derselbe Zug - unabhaengig davon, worueber geredet wird."""
    alle = kapitel()
    folgen = {}
    for marke, text in alle:
        red = [_oeffner(r) for r in REPLIK.findall(text)]
        red = [r for r in red if r]
        folgen[marke] = red

    fund = defaultdict(list)
    for marke, red in folgen.items():
        for n in range(mindestlaenge, mindestlaenge + 3):
            for i in range(len(red) - n + 1):
                fund[tuple(red[i:i + n])].append(marke)

    treffer = [(len(set(v)), len(v), k) for k, v in fund.items()
               if len(set(v)) >= 3]
    treffer.sort(reverse=True)

    if not treffer:
        print("Keine Gespraechskette laeuft in drei Kapiteln gleich.")
        return 0

    print("GESPRAECHSZUEGE, DIE MEHRFACH GLEICH LAUFEN\n")
    print("  Kapitel  Faelle  Zug")
    gezeigt = 0
    for kap, faelle, kette in treffer:
        if len(kette) < mindestlaenge:
            continue
        print("  %7d  %6d  %s" % (kap, faelle,
                                  "  ->  ".join('"%s ..."' % k for k in kette)))
        gezeigt += 1
        if gezeigt >= 30:
            break
    print("\nDrei Kapitel sind eine Gewohnheit. Zehn sind eine Maschine.")
    return 0



def nester(schwelle=0.62):
    """Behauptungen, die in **drei oder mehr** Kapiteln stehen.

    Ein Paar ist oft Absicht: eine Figur erfaehrt etwas und gibt es weiter.
    Ab dem dritten Mal ist es fast immer ein Bericht ueber einen Bericht, und
    der Leser hat die Tatsache laengst."""
    alle = kapitel()
    fuell = fuellwoerter(alle)
    eintraege = []
    for marke, text in alle:
        for s in saetze(text):
            k = kern(s, fuell)
            if len(k) >= 4:
                eintraege.append((marke, s, k))

    index = defaultdict(list)
    for i, (_, _, k) in enumerate(eintraege):
        for w in k:
            index[w].append(i)

    # Union-Find ueber die Paare: was mit was zusammenhaengt, ist ein Nest.
    eltern = list(range(len(eintraege)))

    def wurzel(i):
        while eltern[i] != i:
            eltern[i] = eltern[eltern[i]]
            i = eltern[i]
        return i

    gesehen = set()
    for i, (marke_i, _, k_i) in enumerate(eintraege):
        kandidaten = Counter()
        for w in k_i:
            if len(index[w]) > 60:
                continue
            for j in index[w]:
                if j > i:
                    kandidaten[j] += 1
        for j, geteilt in kandidaten.items():
            if geteilt < 3 or (i, j) in gesehen:
                continue
            gesehen.add((i, j))
            marke_j, _, k_j = eintraege[j]
            if marke_j == marke_i:
                continue
            if len(k_i & k_j) / float(len(k_i | k_j)) >= schwelle:
                a, b = wurzel(i), wurzel(j)
                if a != b:
                    eltern[a] = b

    gruppen = defaultdict(list)
    for i in range(len(eintraege)):
        gruppen[wurzel(i)].append(i)

    nest = []
    for _, mitglieder in gruppen.items():
        kaps = sorted(set(eintraege[i][0] for i in mitglieder))
        if len(kaps) >= 3:
            nest.append((len(kaps), kaps, mitglieder))
    nest.sort(reverse=True)

    if not nest:
        print("Keine Behauptung steht in drei Kapiteln.")
        return 0

    print("BEHAUPTUNGEN IN DREI ODER MEHR KAPITELN (%d Nester)\n" % len(nest))
    for n, kaps, mitglieder in nest:
        print("  %d Kapitel: %s" % (n, ", ".join(kaps)))
        for i in sorted(mitglieder, key=lambda x: eintraege[x][0]):
            print("      %s  %s" % (eintraege[i][0], eintraege[i][1][:130]))
        print()
    return 0

if __name__ == "__main__":
    if "--oeffner" in sys.argv:
        sys.exit(oeffner())
    if "--ketten" in sys.argv:
        sys.exit(ketten())
    if "--nester" in sys.argv:
        sys.exit(nester())
    nur = None
    if "--kapitel" in sys.argv:
        i = sys.argv.index("--kapitel")
        n = int(sys.argv[i + 1])
        nur = "b2 %02d" % n
    schwelle = 0.55
    if "--schwelle" in sys.argv:
        schwelle = float(sys.argv[sys.argv.index("--schwelle") + 1])
    sys.exit(behauptungen(nur, schwelle))
