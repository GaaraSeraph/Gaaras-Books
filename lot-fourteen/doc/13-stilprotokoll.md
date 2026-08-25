# Stilprotokoll

**Wem es gehoert:** der Stilsitzung. Sie schreibt hier, die Inhaltspruefung
liest hier. Niemand sonst schreibt hinein - deshalb ist es eine eigene Datei und
nicht ein Abschnitt in `doc/05`, das schon zweimal kollidiert ist.

**Wozu.** Ein Durchgang, der jede Aussage an `doc/12-stimmen.md` anpasst,
schreibt woertliche Rede um. In woertlicher Rede stehen die Fakten: *"I am
fifty-nine"*, *"since I was twenty-six"*, *"it was Y who suggested the cards"*.
Ohne Protokoll muss die Inhaltspruefung danach hundert Kapitel neu lesen. Mit
Protokoll liest sie die Zeilen, die sich bewegt haben.

**Die Gegenprobe dazu** ist `werkzeug/faktenspur.py --seit <sha>`. Sie findet,
was an Zahlen, Daten und Namen anders ist. Sie findet **nicht**, was gleich
zaehlt und anders bedeutet. Genau dafuer ist dieses Blatt da.

---

## Ausgangsstand

**Vor dem Durchgang eintragen, in einer Zeile:**

    Durchgang <Name>, begonnen <Datum>, Ausgangsstand <sha>

Ohne den SHA ist `--seit` Raterei.

| Durchgang | Datum | Ausgangsstand | Kapitel | Stand |
|---|---|---|---|---|
| Erzaehlerkommentare, Band 2 | 25.08.2026 | `14a893e` | b2 K01-K68 | laeuft |

**Was dieser Durchgang tut, und warum er die vier Meldungen anders trifft als
erwartet.** Er schreibt **keine woertliche Rede um**. Er setzt Absaetze
*dazwischen*: der Erzaehler benennt wieder, was eine Szene zurueckhaelt.
Gemessen am 25.08.: Band 1 hat 25 solche Saetze (0,25 je 1000 Woerter), Band 2
hat 4 (0,02) - der Erzaehler ist nach Band 1 verstummt, und das Erklaeren ist
in die Muender der Figuren gewandert (Band 1 25:21, Band 2 4:46).

Daraus folgt fuer dieses Blatt:

- **Meldung 1** (Sprecherangaben) faellt fast weg - es wird nichts gestrichen.
- **Meldung 2 und 3 sind die schweren.** Jeder eingesetzte Satz ist eine **neue
  Tatsachenbehauptung des Erzaehlers**, und der Erzaehler wiegt schwerer als
  eine Figur. Steht darin eine Dauer (*four days*) oder ein Absolutum (*never*,
  *the largest*, *the whole of it*), steht sie unten - auch wenn ich sie aus
  dem Kapitel selbst genommen habe. **Woher ich sie habe, steht dabei.**
- **Meldung 4:** die festgelegten Zeilen in `doc/05` verbieten dem Erzaehler
  ausdruecklich, auf sie zu zeigen (*best-made thing*, *was nicht Arbeit war*,
  *die zwei Haende*). Alle drei liegen in Band 1. In Band 2 wird kein
  Kommentar in ihre Naehe gesetzt.

---

## Was gemeldet wird

Vier Sachen, und nur diese vier. Alles andere kostet die Inhaltspruefung nichts.

**1. Eine gestrichene oder eingesetzte Sprecherangabe.**
Kapitel, und die Zeile so, wie sie vorher dastand. Das ist die wichtigste der
vier: mit jeder gestrichenen Angabe haengt der Sprecher nur noch am Zusammenhang,
und *falscher Sprecher* ist eine belegte Fehlerklasse in diesem Buch.
Beispiel aus Kapitel 60: gestrichen wurde *"Georgij said it without any weight on
it."*

**2. Ein umformulierter Satz, in dem eine Zahl, ein Datum, ein Alter oder eine
Dauer steht.** Kapitel, vorher, nachher. Auch dann, wenn die Zahl selbst
gleich geblieben ist - *"four hours"* im Saal und *"four hours"* im Gebaeude sind
zwei verschiedene Angaben, und die Verwechslung hat schon einmal eine falsche
Korrektur ausgeloest.

**3. Eine angefasste absolute Behauptung.** *the first time*, *never*, *only*,
*since*, *not once*. Diese Saetze sind fast immer Kanon und fast nie nur Ton.

**4. Eine festgelegte Zeile, die das Stimmblatt aendern wollte.**
Die Liste steht in `doc/05-continuity.md` unter **Festgelegte Zeilen**.
**Nicht aendern - hier eintragen.** Ein Zuruecknehmen ist teurer als ein
Nichtanfassen, und der Autor entscheidet das, nicht das Stimmblatt.

**Nicht gemeldet wird:** Satzzeichen, Satzlaenge, Absatzbau, Tics,
Erzaehlerformeln, Echos, Beats, die zwei Trenner. Reiner Ton, kein Inhalt.

---

## Erfundene Repliken markieren

`doc/12-stimmen.md` erfindet absichtlich Sprache, um eine Stimme zu zeigen.
`werkzeug/belege.py` hat die zuerst als Falschzitate gezaehlt - zwanzig Stueck,
achtzehn davon Absicht. **Ein Wort im Absatz davor oder in der Ueberschrift**
genuegt, damit das Werkzeug sie richtig einsortiert: *Beispiel*, *Vorschlag*,
*Muster*, *Entwurf*, *Probe*, *so wuerde*, *nicht im Text*. Keine neue Syntax.

**Warum das nicht Kosmetik ist:** von den zwanzig blieb nach der Trennung einer
uebrig, und der war echt - Hanas Blatt stand auf einem Satz, den es im Buch
nicht gibt. Eine Zahl, die zu neunzig Prozent aus Absicht besteht, wird
ignoriert, und dann faellt der eine nicht mehr auf.

---

## Unsicher

Wo eine Stimmkorrektur den Sinn verschoben haben koennte, auch ohne dass eine
Zahl gewandert ist. Eine Zeile genuegt: Kapitel, Stelle, woran es liegt. Lieber
eine zu viel.

---

## Zwei Regeln, die nicht verhandelbar sind

**Keine Zahl, kein Name, kein Datum und kein Alter wird geaendert, damit ein
Satz besser klingt.** Wenn die Stimme es verlangt, bleibt die Zahl stehen und
die Forderung kommt in dieses Blatt.

**Keine Sprecherangabe wird gestrichen, wenn der Sprecher im selben Wechsel
nicht anders erkennbar ist.** Im Zweifel stehen lassen und unter *Unsicher*
eintragen.

---

## Durchgaenge

---

### Durchgang Erzaehlerkommentare, Band 2 - Ausgangsstand `14a893e`

Fortlaufend, blockweise. Form der Kommentare: kein Kursiv, ein bis zwei Saetze,
eigener Absatz hinter dem Beat, nennt die **Handlung** und nicht das Gefuehl,
sieht durch Georgij. Zwei bis drei je Kapitel.

#### Block 1 - K53, K61 (Muster, vom Autor abgenommen)

**Meldung 2 - Dauer in einem eingesetzten Satz**

| Kap | Eingesetzt | Woher die Zahl |
|---|---|---|
| b2 K61 | *"He had spent **four days** deciding which of the two people in this house he was entitled to hurt, and he had chosen the one who could carry it."* | Woo im selben Kapitel: *"it took me four days"*, *"I have had it four days"* |

**Meldung 3 - Absoluta in eingesetzten Saetzen**

| Kap | Eingesetzt | Deckung im Text |
|---|---|---|
| b2 K53 | *"He had **never** given anybody a date about himself."* | Georgij zwei Absaetze spaeter: *"I do not give anybody dates about myself. It is the one rule I have had since I was nineteen."* |
| b2 K53 | *"...and it was **the largest one** the man had."* | **keine woertliche Deckung** - Erzaehlerurteil ueber Mr Yeom. Siehe *Unsicher*. |
| b2 K61 | *"...**neither** of them had used a word that would have had to be explained afterwards."* | pruefbar am Wechsel selbst (Woo: *"I am not going to need it."* / Mrs Seo: *"There is a chair in the hall."*) |
| b2 K61 | *"That was **the whole of** the visit."* | Woos eigener Abgang: *"I am going to go home and be old."* |

**Meldung 1 und 4:** keine. Nichts gestrichen, keine festgelegte Zeile beruehrt.

**Gegenprobe `faktenspur.py --seit 14a893e`** meldet genau diese beiden Kapitel
und nichts sonst. Aufgeloest: `one` +2 in K53 (*the largest one*, *give one
away*); in K61 `four` +1 und `two` +1 (*four days*, *the two people in this
house*), `sunday` +1 und `one` +1 (*across a city on a Sunday*, *said properly
once*, *the one who could carry it*). **Alle aus dem Kapitel selbst.**

**Unsicher**

- **b2 K53, die Apologie-Stelle.** *"it was the largest one the man had"* ist ein
  Urteil ueber Mr Yeoms Innenleben, nicht ueber Georgijs Wahrnehmung. Das Buch
  steht sonst hinter Georgijs Auge. Wenn Du die Kamera streng willst, muss es
  *"and Georgij took it as the largest one the man had"* heissen.
- **b2 K61, Woos vier Tage.** Erste Fassung des Schlusskommentars gab ihm ein
  **falsches Motiv** (er habe es getragen, damit Georgij es nicht von jemand
  Schlimmerem hoere). Im Text wartet er die vier Tage, *"because I was waiting
  for the rest of it"*. Ersetzt durch das Motiv, das er selbst nennt: *"I have
  been in one room in my life where a name was said badly."* **Der Fehler ist
  nicht im Buch gelandet**, steht aber hier, weil er die Fehlerklasse dieses
  Durchgangs zeigt: **ein Erzaehlerkommentar erfindet ein Motiv, das die Figur
  nicht hat.**

