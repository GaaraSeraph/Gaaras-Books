# -*- coding: utf-8 -*-
"""
Belege pruefen: jedes englische Zitat in den Dokumenten muss im Text stehen.

Fehlerklasse: *Ein Dokument, das das Buch aus dem Gedaechtnis zitiert.* Exemplar
war `doc/10-naehe.md`, wo ein Satz ueber einen Stuhl im Register stand, den es im
Buch nie gab. Ein Register, das erfindet, ist schlimmer als keines: es wird
geglaubt.

Signatur: ein Zitat in Anfuehrungszeichen, englisch, laenger als sechs Woerter,
das sich in keiner lebenden Kapitelfassung wiederfindet.

Die Eichung steht unten und laeuft bei jedem Start. Sie nimmt einen echten Satz
aus dem Buch (muss gefunden werden) und denselben Satz mit einem geaenderten Wort
(darf nicht gefunden werden). Faellt sie durch, meldet das Programm nichts -
siehe `doc/11-pruefen.md`, Schritt 3.
"""
import io, os, re, sys, glob

DEUTSCH = set(u"""der die das und nicht ist ein eine eines einem einen dass sich wird kann
auch sie ich den dem von fuer für aus wie oder nur noch mehr sind hat haben war waren
werden wenn aber schon nach vor bei mit zum zur ueber über sein seine ihre steht stehen
kapitel band satz zeile seite gilt gibt keine kein weil damit dann diese dieser dieses
man wer wo was warum nichts alles etwas immer nie jetzt hier dort ohne durch gegen""".split())

ENGLISCH = set(u"""the and of to in a is was that it he she they for on with as at but not
you i have has had do did not be been are were would could this his her him them my me""".split())


def projektwurzel(start=None):
    d = os.path.dirname(os.path.abspath(start or __file__))
    for _ in range(4):
        if os.path.isdir(os.path.join(d, "chapters")) and os.path.isdir(os.path.join(d, "doc")):
            return d
        p = os.path.dirname(d)
        if p == d:
            break
        d = p
    return os.path.dirname(os.path.abspath(start or __file__))


def lebende(ordner):
    best = {}
    for p in glob.glob(os.path.join(ordner, "ch*_v*_en.md")):
        b = os.path.basename(p)
        m = re.match(r"ch\d+_v(\d+)_(\d+)_en\.md", b)
        if not m:
            continue
        ch = b.split("_")[0]
        k = (int(m.group(1)), int(m.group(2)))
        if ch not in best or k > best[ch][0]:
            best[ch] = (k, p)
    return dict((c, v[1]) for c, v in best.items())


def norm(s):
    for a, b in ((u"\u2019", "'"), (u"\u2018", "'"), (u"\u201c", '"'), (u"\u201d", '"'),
                 (u"\u2014", "-"), (u"\u2013", "-"), (u"\u00b7", " "), (u"\u00a0", " ")):
        s = s.replace(a, b)
    s = s.replace("*", "").replace("_", "").replace(">", " ")
    return re.sub(r"\s+", " ", s).strip()


def korpus(root, alle=False):
    """alle=False: nur die lebenden Fassungen. alle=True: auch das Archiv.

    Der Unterschied traegt die ganze Meldung. Ein Zitat, das in einer alten
    Fassung steht, ist ein historisches Zitat und kein Fehler. Ein Zitat, das in
    KEINER Fassung steht, ist aus dem Gedaechtnis geschrieben.
    """
    teile = []
    for d in ("chapters", "chapters-2"):
        ordner = os.path.join(root, d)
        pfade = glob.glob(os.path.join(ordner, "ch*_v*_en.md")) if alle             else lebende(ordner).values()
        for p in pfade:
            teile.append(norm(io.open(p, encoding="utf-8").read()))
    return " || ".join(teile)


QUOTE = re.compile(u'[\u201c"]([^\u201c\u201d"]{30,400})[\u201d"]')


def englisch(q):
    w = re.findall(r"[a-zA-Z'-]+", q.lower())
    if len(w) < 7:
        return False
    de = sum(1 for x in w if x in DEUTSCH)
    en = sum(1 for x in w if x in ENGLISCH)
    return en >= 3 and en > de * 2


def zitate(pfad):
    txt = io.open(pfad, encoding="utf-8").read()
    for m in QUOTE.finditer(txt):
        q = m.group(1)
        if "|" in q or "###" in q or "](" in q:
            continue
        if not englisch(q):
            continue
        zeile = txt.count("\n", 0, m.start()) + 1
        yield zeile, q


N = 5


def woerter(s):
    return re.findall(r"[a-z0-9']+", norm(s).lower())


def ngramme(ws, n=N):
    return set(" ".join(ws[i:i + n]) for i in range(len(ws) - n + 1))


def deckung(q, korp):
    """Anteil der Woerter, die in einer Fuenfergruppe stehen, die es im Buch gibt.

    Nicht die Zeichenkette vergleichen und auch nicht blosse Fuenfergruppen
    zaehlen, sondern messen, wieviel vom Zitat sich im Buch wiederfindet. Drei
    echte Falschmeldungen der frueheren Fassungen haben das erzwungen:
      - ein grossgeschriebenes Bruchstueck: *"The shed roof should be done..."*
        gegen *"She said the shed roof should be done..."*;
      - eine wieder zusammengesetzte Replik mit Sprecherangabe darin:
        *"I would take that call, on a Sunday."* gegen
        *"I would take that call," said Mr Chae, "on a Sunday."* - dort liegen
        drei von vier Fuenfergruppen quer ueber die Naht;
      - Auslassungen mit drei Punkten.
    Alle drei sind richtig zitiert. Wer dagegen Wortgruppen erfindet, deckt
    grosse Teile seines eigenen Zitats nicht ab.
    """
    ws = woerter(q)
    if len(ws) < N + 2:
        return 1.0
    gedeckt = [False] * len(ws)
    for i in range(len(ws) - N + 1):
        if " ".join(ws[i:i + N]) in korp:
            for j in range(i, i + N):
                gedeckt[j] = True
    return float(sum(gedeckt)) / len(ws)


def steht_im_text(q, korp, grenze=0.55):
    return deckung(q, korp) >= grenze


def eichung(korp):
    """Vier Proben. Zwei muessen durchgehen, zwei muessen auffallen."""
    echt = "She said the shed roof should be done properly or not at all"
    bruch = "The shed roof should be done properly or not at all"
    geteilt = "I would take that call, on a Sunday."
    erfunden = "She said the shed roof should be measured by a man from Busan "                "who counts the nails and writes them in a book"
    proben = [(echt, False), (bruch, False), (geteilt, False), (erfunden, True)]
    for q, soll_auffallen in proben:
        auffaellig = not steht_im_text(q, korp)
        if auffaellig != soll_auffallen:
            return False, "Probe falsch beantwortet: " + q[:50]
    return True, "vier Proben, zwei davon Falschmeldungen von Fassung 1"


def main():
    root = projektwurzel()
    gesamt = ngramme(woerter(korpus(root)))
    archiv = ngramme(woerter(korpus(root, alle=True)))
    ok, was = eichung(gesamt)
    print("Eichung: %s (%s)" % ("bestanden" if ok else "DURCHGEFALLEN", was))
    print("")
    if not ok:
        print("Kein Ergebnis. Ein ungeeichter Detektor meldet nichts.")
        return 2
    zeigen = "-v" in sys.argv
    docs = sorted(glob.glob(os.path.join(root, "doc", "*.md")))
    docs += [os.path.join(root, "CLAUDE.md")]
    tot = fehl = veraltet = 0
    for d in docs:
        if not os.path.exists(d):
            continue
        bad, alt = [], 0
        for zeile, q in zitate(d):
            tot += 1
            if steht_im_text(q, gesamt):
                continue
            if steht_im_text(q, archiv):
                alt += 1
                continue
            bad.append((zeile, q))
        fehl += len(bad)
        veraltet += alt
        name = os.path.relpath(d, root).replace("\\", "/")
        if bad or alt:
            print("%-26s  erfunden %-4d  aus alten Fassungen %d"
                  % (name, len(bad), alt))
            if zeigen:
                for zeile, q in bad:
                    print("      Zeile %-5d %s" % (zeile, q[:140].replace(chr(10), " ")))
    print("")
    print("%d englische Zitate geprueft." % tot)
    print("%d stehen in KEINER Fassung - aus dem Gedaechtnis geschrieben." % fehl)
    print("%d stehen in einer ueberholten Fassung - Geschichte, kein Fehler." % veraltet)
    return 1 if fehl else 0


# ---------------------------------------------------------------------------
# Zweite Klasse: richtiges Zitat, falsches Kapitel.
#
# Ein Kapitelregister ordnet jedem Zitat eine Nummer zu. Die Nummer kann falsch
# sein, ohne dass am Zitat etwas auffaellt - der Satz steht ja im Buch. Signatur:
# das Zitat steht in genau einem Kapitel, und das ist nicht das, unter dem es im
# Dokument steht.
# ---------------------------------------------------------------------------

# Nur echte Registereintraege zaehlen als Marke - Listenzeilen der Form
#   - **Band 2, Kapitel 45** *Titel* (v1.1) - ...
# Eine Fassung, die einfach die zuletzt erwaehnte Kapitelnummer nahm, hat 312
# Treffer gemeldet: in Fliesstext wird staendig eine Nummer genannt, und danach
# lag jedes Zitat der naechsten zwanzig Absaetze angeblich falsch. Ungeeicht und
# unbrauchbar.
MARKE = re.compile(r"^- \*\*Band (1|2), Kapitel (\d+)\*\*", re.M)


def kapitelkorpora(root):
    aus = {}
    for band, d in (("1", "chapters"), ("2", "chapters-2")):
        for ch, p in lebende(os.path.join(root, d)).items():
            aus[(band, int(ch[2:]))] = ngramme(woerter(io.open(p, encoding="utf-8").read()))
    return aus


def wo_steht(q, korpora, grenze=0.55):
    return [k for k, g in korpora.items() if deckung(q, g) >= grenze]


def kapitelpruefung(root):
    korpora = kapitelkorpora(root)
    docs = sorted(glob.glob(os.path.join(root, "doc", "*.md")))
    treffer = 0
    for d in docs:
        txt = io.open(d, encoding="utf-8").read()
        marken = [(m.start(), m.group(1), int(m.group(2))) for m in MARKE.finditer(txt)]
        if not marken:
            continue
        bad = []
        for zeile, q in zitate(d):
            pos = sum(len(x) + 1 for x in txt.split(chr(10))[:zeile - 1])
            davor = [m for m in marken if m[0] <= pos]
            if not davor:
                continue
            # Nur was noch im Eintrag steht. Ohne diese Schranke wirkt die letzte
            # Marke des Registers bis ans Dateiende weiter und faerbt jedes Zitat
            # der Durchgangsprotokolle falsch ein - 61 Scheintreffer.
            if txt.count(chr(10), davor[-1][0], pos) > 40:
                continue
            band, kap = davor[-1][1], davor[-1][2]
            orte = wo_steht(q, korpora)
            if len(orte) == 1 and orte[0] != (band, kap):
                bad.append((zeile, band, kap, orte[0], q))
        if bad:
            treffer += len(bad)
            print("")
            print(os.path.relpath(d, root).replace(chr(92), "/"))
            for zeile, band, kap, ort, q in bad:
                print("  Zeile %-5d steht unter B%s %s, gehoert zu B%s %s"
                      % (zeile, band, kap, ort[0], ort[1]))
                print("        %s" % q[:130].replace(chr(10), " "))
    print("")
    print("%d Zitate stehen unter der falschen Kapitelnummer." % treffer)
    return treffer


if __name__ == "__main__":
    if "--kapitel" in sys.argv:
        root = projektwurzel()
        gesamt = ngramme(woerter(korpus(root)))
        ok, was = eichung(gesamt)
        print("Eichung: %s (%s)" % ("bestanden" if ok else "DURCHGEFALLEN", was))
        print("")
        sys.exit(2 if not ok else (1 if kapitelpruefung(root) else 0))
    sys.exit(main())
