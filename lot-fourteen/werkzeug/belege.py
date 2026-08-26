# -*- coding: utf-8 -*-
"""
Belege pruefen: jedes englische Zitat in den Dokumenten muss im Text stehen.

Fehlerklasse: *Ein Dokument, das das Buch aus dem Gedaechtnis zitiert.* Exemplar
war `doc/10-naehe.md`, wo ein Satz ueber einen Stuhl im Register stand, den es im
Buch nie gab. Ein Register, das erfindet, ist schlimmer als keines: es wird
geglaubt.

Drei Sorten, und sie auseinanderzuhalten ist der ganze Wert des Programms:

  ohne Beleg      steht in keiner Fassung. Das ist der Fund.
  alte Fassung    steht in einer ueberholten Fassung. Geschichte, kein Fehler.
  Vorschlag       steht in einem Block, der Sprache vorschlaegt statt sie zu
                  belegen - *so wuerde Jang reden*. Absicht, kein Fehler.

Die dritte Sorte kam am 25.08. aus der Stilsitzung: `doc/12-stimmen.md` erfindet
absichtlich Repliken, und die als Falschzitate zu zaehlen treibt die Zahl so
hoch, dass sich alle daran gewoehnen, sie zu ignorieren. Dann faengt sie auch
das echte Falschzitat nicht mehr. Das ist Regel 8 in `doc/11-pruefen.md`.

Zweiter Modus: `--kapitel` prueft, ob ein Zitat unter der richtigen Kapitelnummer
steht. Ein Register kann eine Zeile richtig zitieren und falsch einordnen.

Die Eichung laeuft bei jedem Start und meldet nichts, wenn sie durchfaellt -
`doc/11-pruefen.md`, Schritt 3.
"""
import io
import os
import re
import sys
import glob

DEUTSCH = set(u"""der die das und nicht ist ein eine eines einem einen dass sich wird kann
auch sie ich den dem von fuer für aus wie oder nur noch mehr sind hat haben war waren
werden wenn aber schon nach vor bei mit zum zur ueber über sein seine ihre steht stehen
kapitel band satz zeile seite gilt gibt keine kein weil damit dann diese dieser dieses
man wer wo was warum nichts alles etwas immer nie jetzt hier dort ohne durch gegen""".split())

ENGLISCH = set(u"""the and of to in a is was that it he she they for on with as at but not
you i have has had do did be been are were would could this his her him them my me""".split())

VORSCHLAGSWORT = [u"vorschlag", u"beispiel", u"muster", u"entwurf", u"probe",
                  u"so würde", u"so wuerde", u"so klingt", u"nicht im text",
                  u"vom autor selbst", u"anläufe", u"anlaeufe",
                  u"keiner fassung", u"nicht gibt", u"gibt es nicht",
                  u"noch nicht im", u"ein vorschlag", u"sichere fassung"]

N = 5
GRENZE = 0.55


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
    for a, b in ((u"’", "'"), (u"‘", "'"), (u"“", '"'), (u"”", '"'),
                 (u"—", " "), (u"–", " "), (u"·", " "), (u" ", " ")):
        s = s.replace(a, b)
    return s.replace("*", "").replace("_", "").replace(">", " ")


def woerter(s):
    return re.findall(r"[a-z0-9']+", norm(s).lower())


def ngramme(ws, n=N):
    return set(" ".join(ws[i:i + n]) for i in range(len(ws) - n + 1))


def machen(texte):
    """Ein Korpus ist Wortkette UND Fuenfergruppen. Beides wird gebraucht."""
    ws = []
    for t in texte:
        ws.extend(woerter(t))
        ws.append(u"||")
    return {"wort": u" " + u" ".join(ws) + u" ", "ng": ngramme(ws)}


def korpus(root, alle=False):
    texte = []
    for d in ("chapters", "chapters-2"):
        ordner = os.path.join(root, d)
        pfade = glob.glob(os.path.join(ordner, "ch*_v*_en.md")) if alle \
            else list(lebende(ordner).values())
        for p in pfade:
            texte.append(io.open(p, encoding="utf-8").read())
    return machen(texte)


def deckung(q, K):
    """Anteil der Woerter, die in einer Fuenfergruppe stehen, die es im Buch gibt."""
    ws = woerter(q)
    if len(ws) < N + 2:
        return 0.0
    gedeckt = [False] * len(ws)
    for i in range(len(ws) - N + 1):
        if " ".join(ws[i:i + N]) in K["ng"]:
            for j in range(i, i + N):
                gedeckt[j] = True
    return float(sum(gedeckt)) / len(ws)


def stuecke_stehen(q, K):
    """Jedes Komma-Stueck von mindestens drei Woertern steht woertlich im Buch.

    Das faengt die wieder zusammengesetzte Replik, in der eine Sprecherangabe
    steckt. Zwei echte Falschmeldungen frueherer Fassungen:
        *"I would take that call, on a Sunday."*
      gegen  *"I would take that call," said Mr Chae, "on a Sunday."*
        *"That's a beautiful answer, and it isn't one."*
      gegen  *"That's a beautiful answer," said Hana, "and it isn't one."*
    Beim zweiten sitzt die Angabe nach dem vierten Wort - dort ueberlebt keine
    einzige Fuenfergruppe, und die Deckung allein war blind dafuer.
    """
    stuecke = re.split(r"[,;:]|\.\.\.|…", norm(q))
    lang = [woerter(s) for s in stuecke]
    lang = [w for w in lang if len(w) >= 3]
    if not lang:
        return False
    return all((u" " + u" ".join(w) + u" ") in K["wort"] for w in lang)


def steht_im_text(q, K):
    return deckung(q, K) >= GRENZE or stuecke_stehen(q, K)


QUOTE = re.compile(u'[“"]([^“”"]{30,400})[”"]')


def englisch(q):
    w = re.findall(r"[a-zA-Z'-]+", q.lower())
    if len(w) < 7:
        return False
    de = sum(1 for x in w if x in DEUTSCH)
    en = sum(1 for x in w if x in ENGLISCH)
    return en >= 3 and en > de * 2


def zitate_aus(txt):
    """Zitate blockweise suchen, nicht ueber das ganze Dokument.

    Anfuehrungszeichen paaren sich sonst ueber eine Blockgrenze hinweg: steht in
    einem Zitatblock erst *"Take the coat off," said Annie.* und in der naechsten
    Zeile *"He took the coat off..."*, dann faellt das schliessende Zeichen der
    ersten Zeile mit dem oeffnenden der zweiten zusammen, und dazwischen steht
    deutscher Fliesstext. Am 26.08. hat das in `doc/15-kuerzen.md` einen Fund
    gemeldet, obwohl beide Zitate echt sind und im richtigen Kapitel stehen.
    Eine Leerzeile, eine Ueberschrift oder ein leerer Zitatstrich trennt jetzt.
    """
    zeilen = txt.split(chr(10))

    def aus_block(block, start):
        if not block:
            return
        roh = chr(10).join(block)
        for m in QUOTE.finditer(roh):
            q = m.group(1)
            if "|" in q or "###" in q or "](" in q:
                continue
            if not englisch(q):
                continue
            yield start + roh.count(chr(10), 0, m.start()) + 1, q

    block, start = [], 0
    for i, l in enumerate(zeilen):
        if not l.strip() or l.strip() == ">" or l.startswith("#"):
            for x in aus_block(block, start):
                yield x
            block, start = [], i + 1
        else:
            if not block:
                start = i
            block.append(l)
    for x in aus_block(block, start):
        yield x


def vorschlagszeilen(txt):
    """Welche Zeilen stehen in einem Block, der Sprache vorschlaegt statt sie zu belegen.

    Absatzweise, in zwei Durchgaengen, und beides musste sein:
      - Eine Fassung setzte die Marke zeilenweise und verlor sie wieder, sobald
        der einleitende Absatz ueber zwei Zeilen lief. Fuenf von sieben
        Markierungen blieben wirkungslos.
      - Eine Fassung wertete den Absatz nur bis zur Zitatzeile aus. Damit fiel
        jeder Absatz durch, der das Zitat vorne traegt und erst danach sagt,
        dass es im Buch nicht steht - also genau die Korrekturen.
    Deshalb erst die Absaetze bilden, dann markieren.

    Kein neues Zeichen und keine neue Syntax; die Blaetter schreiben ohnehin
    *Ein Beispiel, ruhig* oder *steht noch nicht im Text*.
    """
    zeilen = txt.split(chr(10))
    bloecke = []          # (start, ende, text, ist_zitat)
    lauf, start, zitat = [], None, False
    for i, l in enumerate(zeilen):
        roh = l.strip()
        ist_q = l.lstrip().startswith(">")
        if not roh or l.startswith("#") or ist_q != zitat:
            if lauf:
                bloecke.append((start, i - 1, " ".join(lauf).lower(), zitat))
                lauf, start = [], None
        if not roh:
            continue
        if l.startswith("#"):
            bloecke.append((i, i, roh.lower(), None))
            zitat = False
            continue
        if start is None:
            start, zitat = i, ist_q
        lauf.append(roh)
    if lauf:
        bloecke.append((start, len(zeilen) - 1, " ".join(lauf).lower(), zitat))

    def markiert(s):
        return any(w in s for w in VORSCHLAGSWORT)

    aus = [False] * (len(zeilen) + 2)
    ueberschrift = False
    vorher = False        # der letzte Nicht-Zitat-Absatz war markiert
    for a, b, s, ist_q in bloecke:
        if ist_q is None:
            ueberschrift = markiert(s)
            vorher = False
            continue
        eigen = markiert(s)
        an = ueberschrift or eigen or (ist_q and vorher)
        for k in range(a, b + 1):
            aus[k + 1] = an
        if not ist_q:
            vorher = eigen
    return aus


def eichung(K):
    """Sechs Zitatproben und zwei Blockproben.

    Fuenf der sechs muessen schweigen, und jede der fuenf war einmal eine echte
    Falschmeldung dieses Programms.
    """
    proben = [
        (u"She said the shed roof should be done properly or not at all", False),
        (u"The shed roof should be done properly or not at all", False),
        (u"I would take that call, on a Sunday.", False),
        (u"That's a beautiful answer, and it isn't one.", False),
        (u"She said the shed roof... properly or not at all", False),
        (u"She said the shed roof should be measured by a man from Busan who "
         u"counts the nails and writes them in a book that nobody ever reads", True),
    ]
    for q, soll in proben:
        if (not steht_im_text(q, K)) != soll:
            return False, u"Probe falsch beantwortet: " + q[:52]
    a = u'## Ein Beispiel\n\n> "Nobody in this trade has ever said that to me."\n'
    if not vorschlagszeilen(a)[3]:
        return False, u"Vorschlagsblock nicht erkannt"
    b = u'## Kapitel 12{n}{n}> "Nobody in this trade has ever said that to me."{n}'.format(n=chr(10))
    if vorschlagszeilen(b)[3]:
        return False, u"gewoehnlicher Block faelschlich als Vorschlag gelesen"
    # Der einleitende Absatz laeuft ueber zwei Zeilen - die Marke muss halten.
    c = u'Ein Beispiel, und es ist{n}nur ein Muster:{n}{n}> "Nobody in this trade has ever said that to me."{n}'.format(n=chr(10))
    if not vorschlagszeilen(c)[4]:
        return False, u"mehrzeiliger Einleitungsabsatz verliert die Marke"
    # Das Zitat steht VORNE im Absatz, die Marke erst dahinter.
    d = u'Hier stand "Nobody in this trade has ever said that to me." als Beleg,{n}und der Satz steht in keiner Fassung.{n}'.format(n=chr(10))
    if not vorschlagszeilen(d)[1]:
        return False, u"Marke hinter dem Zitat wird nicht gesehen"
    return True, u"sechs Zitatproben, vier Blockproben"


def dokumente(root):
    d = sorted(glob.glob(os.path.join(root, "doc", "*.md")))
    return [x for x in d + [os.path.join(root, "CLAUDE.md")] if os.path.exists(x)]


def main():
    root = projektwurzel()
    live = korpus(root)
    archiv = korpus(root, alle=True)
    ok, was = eichung(live)
    print(u"Eichung: %s (%s)" % (u"bestanden" if ok else u"DURCHGEFALLEN", was))
    print(u"")
    if not ok:
        print(u"Kein Ergebnis. Ein ungeeichter Detektor meldet nichts.")
        return 2
    zeigen = "-v" in sys.argv
    tot = fehl = veraltet = vorschlaege = 0
    for d in dokumente(root):
        txt = io.open(d, encoding="utf-8").read()
        marke = vorschlagszeilen(txt)
        bad, alt, vor = [], 0, 0
        for zeile, q in zitate_aus(txt):
            tot += 1
            if steht_im_text(q, live):
                continue
            if steht_im_text(q, archiv):
                alt += 1
            elif zeile < len(marke) and marke[zeile]:
                vor += 1
            else:
                bad.append((zeile, q))
        fehl += len(bad)
        veraltet += alt
        vorschlaege += vor
        if bad or alt or vor:
            print(u"%-26s  ohne Beleg %-4d alte Fassung %-4d Vorschlag %d"
                  % (os.path.relpath(d, root).replace(chr(92), "/"), len(bad), alt, vor))
            for zeile, q in bad:
                print(u"      Zeile %-5d %s" % (zeile, q[:135].replace(chr(10), " ")))
            if zeigen and vor:
                print(u"      (%d Vorschlagszitate nicht aufgefuehrt)" % vor)
    print(u"")
    print(u"%d englische Zitate geprueft." % tot)
    print(u"%d ohne Beleg - stehen in keiner Fassung." % fehl)
    print(u"%d aus ueberholten Fassungen, %d aus Vorschlagsbloecken." % (veraltet, vorschlaege))
    return 1 if fehl else 0


# ---------------------------------------------------------------------------
# Zweite Klasse: richtiges Zitat, falsches Kapitel.
#
# Nur echte Registereintraege zaehlen als Marke - Listenzeilen der Form
#   - **Band 2, Kapitel 45** *Titel* (v1.1) - ...
# Eine Fassung, die einfach die zuletzt erwaehnte Kapitelnummer nahm, hat 312
# Treffer gemeldet: in Fliesstext wird staendig eine Nummer genannt, und danach
# lag jedes Zitat der naechsten zwanzig Absaetze angeblich falsch.
# ---------------------------------------------------------------------------
MARKE = re.compile(r"^- \*\*Band (1|2), Kapitel (\d+)\*\*", re.M)


def kapitelkorpora(root):
    aus = {}
    for band, d in (("1", "chapters"), ("2", "chapters-2")):
        for ch, p in lebende(os.path.join(root, d)).items():
            aus[(band, int(ch[2:]))] = machen([io.open(p, encoding="utf-8").read()])
    return aus


def kapitelpruefung(root):
    korpora = kapitelkorpora(root)
    treffer = 0
    for d in dokumente(root):
        txt = io.open(d, encoding="utf-8").read()
        marken = [(m.start(), m.group(1), int(m.group(2))) for m in MARKE.finditer(txt)]
        if not marken:
            continue
        marke = vorschlagszeilen(txt)
        bad = []
        for zeile, q in zitate_aus(txt):
            if zeile < len(marke) and marke[zeile]:
                continue
            pos = sum(len(x) + 1 for x in txt.split(chr(10))[:zeile - 1])
            davor = [m for m in marken if m[0] <= pos]
            # Nur was noch im Eintrag steht. Ohne diese Schranke wirkt die letzte
            # Marke bis ans Dateiende weiter und faerbt jedes Zitat der
            # Durchgangsprotokolle falsch ein - 61 Scheintreffer.
            if not davor or txt.count(chr(10), davor[-1][0], pos) > 40:
                continue
            orte = [k for k, K in korpora.items() if steht_im_text(q, K)]
            if len(orte) == 1 and orte[0] != (davor[-1][1], davor[-1][2]):
                bad.append((zeile, davor[-1][1], davor[-1][2], orte[0], q))
        if bad:
            treffer += len(bad)
            print(u"")
            print(os.path.relpath(d, root).replace(chr(92), "/"))
            for zeile, band, kap, ort, q in bad:
                print(u"  Zeile %-5d steht unter B%s %s, gehoert zu B%s %s"
                      % (zeile, band, kap, ort[0], ort[1]))
                print(u"        %s" % q[:125].replace(chr(10), " "))
    print(u"")
    print(u"%d Zitate stehen unter der falschen Kapitelnummer." % treffer)
    print(u"Jedes einzeln pruefen: ein Eintrag darf ein anderes Kapitel zitieren.")
    return treffer


if __name__ == "__main__":
    if "--kapitel" in sys.argv:
        wurzel = projektwurzel()
        gut, text = eichung(korpus(wurzel))
        print(u"Eichung: %s (%s)" % (u"bestanden" if gut else u"DURCHGEFALLEN", text))
        print(u"")
        sys.exit(2 if not gut else (1 if kapitelpruefung(wurzel) else 0))
    sys.exit(main())
