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

#### Block 2 - K05, K09, K12, K18, K20, K22, K23 (14 Kommentare)

**Zuerst eine Korrektur an meiner eigenen Messung, weil sie den Zuschnitt des
Durchgangs aendert.** Die Zahl aus dem Kopf dieses Blatts (Band 1 0,25 - Band 2
0,02) misst eine **enge Satzform** (*It was a payment on account.*), nicht das
Phaenomen. Breiter gemessen - Erzaehlerabsaetze ueber zwoelf Woertern, keine
Rede - steht es **Band 1 13,4 : Band 2 12,4 je 1000 Woerter**. Der Erzaehler ist
also **nicht verstummt**. Was auseinanderlaeuft, ist die Verteilung: Kapitel 1
bis 3 von Band 2 liegen bei 24,2 / 17,0 / 27,5 und brauchen nichts, waehrend
achtzehn Kapitel unter 8,0 liegen und zwei davon unter dem duennsten Kapitel von
Band 1 (K27, 4,0).

**Folge: keine Quote ueber 68 Kapitel.** Gearbeitet wird an den achtzehn duennen
und danach an einzelnen Stellen. K01-K04 und K06 wurden gelesen und
**absichtlich nicht angefasst** - sie benennen bereits (*"The trouble with a man
who has never said anything untrue is that he has also never had to be
believed."*, K04).

**Meldung 2 - Zahl, Datum oder Dauer in einem eingesetzten Satz**

| Kap | Eingesetzt | Woher |
|---|---|---|
| K18 | *"**Eight** of the **nine** lines described a man. The **ninth** described what he does."* | die neun Zeilen zaehlt das Kapitel selbst |
| K20 | *"He had promised her that answer on the **third of April**..."* | b2 K12 ist Tag 182, Fr 3. April; Annie sagt im selben Kapitel *"since the third of April"* |
| K23 | *"...**a woman of eighty-one**..."* → ersetzt, siehe unten | Mrs Sunwoo, im Kapitel |
| K23 | *"...the rule she had put on him **in March**."* | b2 K05, 11. Maerz: *"The price, before it is paid."* |

**Meldung 3 - Absoluta in eingesetzten Saetzen**

| Kap | Eingesetzt | Deckung |
|---|---|---|
| K05 | *"It was **the only** asset he had **ever** had, and it was not anything he had done."* | Georgij zwei Zeilen davor: *"It is the only true thing I have that is worth anything to you."* |
| K09 | *"She had corrected herself out loud in front of him, and **she does not do that**."* | die Korrektur steht auf der Seite (*"Do not look pleased."* → *"You are permitted to be pleased."*); die Gewohnheit ist Erzaehlerurteil |
| K09 | *"It was **the only** thing she said **all evening** about how it felt..."* | im Kapitel nachpruefbar |
| K12 | *"It was the nearest thing to a complaint he had **ever** made in that room..."* | **keine woertliche Deckung.** Siehe *Unsicher* |
| K22 | *"It is **the one** part of that minute Mr Byun **never** understood..."* | Byun selbst: *"the part I did not understand and have not understood since"* |
| K22 | *"...it makes **no difference whatever** to the man it is done to."* | Erzaehlersatz ohne Fakten. Siehe *Unsicher* |

**Meldung 1 und 4:** keine. Nichts gestrichen, keine festgelegte Zeile beruehrt.

**Gegenprobe `faktenspur.py --seit 3f274c2`:** fuenf Kapitel, alle oben
aufgeloest. K05 und K09 meldet sie gar nicht - dort steht in keinem der vier
Saetze eine Zahl.

**Unsicher**

- **K12** - *"the nearest thing to a complaint he had ever made in that room"*.
  Ein Superlativ ueber sechs Monate Dialog, den ich nicht ausgezaehlt habe. Wenn
  frueher eine deutlichere Klage steht, faellt der Satz.
- **K22** - *"The difference is whether the man doing it wants to, and it makes
  no difference whatever to the man it is done to."* **Der Satz beantwortet
  genau das, was Georgij eine Zeile vorher ausdruecklich nicht erklaert**
  (*"you have not got the first idea why, and I am not going to explain it to
  you"*). Das kann gewollt sein - der Leser bekommt, was Byun nicht bekommt -
  oder es nimmt der Verweigerung die Spitze. **Autorenentscheidung.**
- **K18, beim Schreiben selbst gefangen und ersetzt.** Erste Fassung: *"...and he
  had started running it before she finished the sentence."* Das widerspricht dem
  spaeteren *"He went at it on the stairs afterwards and did not get anywhere."*
  Jetzt: *"...and no way at all to check the answer."*
- **K23, ebenso.** Erste Fassung: *"He had handed a man to a woman of eighty-one
  ... Both halves were deliberate."* Damit haette der Erzaehler Mrs Sunwoos
  Lesart (*"You are inviting me to do something"*) gegen Georgijs ausdrueckliches
  Dementi bestaetigt. Jetzt steht nur, was auf der Seite steht: *"He had given
  her the address and the daughter-in-law's family without being asked for
  either."*

**Beides ist dieselbe Fehlerklasse wie in Block 1: der Erzaehlerkommentar
behauptet mehr, als die Szene hergibt.** Er wiegt schwerer als eine Figur, also
faellt es nicht auf, wenn er es tut.

#### Block 3 - K32, K40, K42, K48, K59, K62, K64, K65, K67 (17 Kommentare)

Damit sind **alle achtzehn Kapitel unter 8,0 durch** (K53 und K61 in Block 1,
K05/K09/K12/K18/K20/K22/K23 in Block 2, diese neun hier).

**Meldung 2 - Zahl, Datum oder Dauer in einem eingesetzten Satz**

| Kap | Eingesetzt | Woher |
|---|---|---|
| K42 | *"He had put a firm down to a friend for **six years**..."* | Sang-hoon im selben Absatz: *"I have put it down to him for six years."* |
| K59 | *"He was describing what had been done to him **in October**..."* | der vierte Oktober, sein eigenes Datum, quer durch beide Baende |
| K64 | *"It is the only promise anybody has made her in **four years**..."* | Ahn Jung-hee ging vor vier Jahren in das Haus, im selben Kapitel gesagt |

**Meldung 3 - Absoluta in eingesetzten Saetzen**

| Kap | Eingesetzt | Deckung |
|---|---|---|
| K32 | *"It is **the only** thing he said all morning that he had not decided on the bus."* | Erzaehlerurteil, keine woertliche Deckung |
| K32 | *"...kept back **the only** part of it that would have helped him."* | ihre eigene Zeile: *"and he does not get to have it"* |
| K40 | *"It is **the only** thing he said all morning that was about himself..."* | im Kapitel nachpruefbar |
| K48 | *"It was **the whole of** what he thought of the afternoon..."* | Erzaehlerurteil ueber Sang-hoon |
| K62 | *"It is **the only** thing anybody has found that will work on him..."* | siehe *Unsicher* - Behauptung ueber die ganze Handlung |
| K64 | *"It is **the only** promise anybody has made her in four years..."* | siehe *Unsicher* |
| K65 | *"It is **the only** sentence anybody has said to him this year that he is not allowed to agree with."* | Erzaehlerurteil |
| K67 | *"It is **the last thing** she is known to have decided..."* | siehe *Unsicher* - **die riskanteste von allen** |

**Meldung 1 und 4:** keine.

**Gegenprobe `faktenspur.py --seit 5579d07`:** acht Kapitel, jede Zeile oben
aufgeloest. K32 meldet sie nicht - dort steht in keinem der beiden Saetze eine
Zahl.

**Unsicher**

- **K67** - *"It is the last thing she is known to have decided, and it was
  about flowers."* Das ist eine Behauptung ueber den **Zeitstrahl**, nicht ueber
  die Szene: sie gilt nur, solange in keinem spaeteren Kapitel eine Entscheidung
  von ihr belegt ist. **Bitte gegen den Kalender pruefen.** Faellt sie, wird
  daraus *"It was the last thing she asked anybody for, and it was about
  flowers"* - oder der Satz geht ganz raus.
- **K62** - *"the only thing anybody has found that will work on him"*. Eine
  Aussage ueber den Stand der Handlung, nicht ueber die Zeile. Wenn spaeter ein
  zweiter Hebel auftaucht, ist der Satz falsch, ohne dass ihn jemand anfasst.
- **K64** - *"the only promise anybody has made her in four years"*. Deckung ist
  Sims eigenes *"She has never once asked me a question in four years"* plus die
  Feststellung, dass niemand sie besucht. Streng genommen ist es ein Schluss und
  kein Beleg.
- **K48** und **K32** - beide Saetze behaupten, was eine andere Figur denkt
  (Sang-hoon, Mrs Jeon). Innerhalb der Kameraregel liegen sie an der Kante.

**Nebenbefund, nicht von mir und keine der vier Klassen - aber es ist die
Klasse, die Euch am meisten kostet.** In `ch42`, an der Stelle
*"Then find out whether the woman Jang has been watching is the same woman this
trust was built for eleven years ago." Sang-hoon put one finger on the folder*:
der Begleitsatz gibt die Zeile **Sang-hoon**. Jang ist Hauspersonal, und ob
Sang-hoon dessen Namen kennt, steht nirgends. Die Zeile ist inhaltlich als
Anweisung an Georgij lesbar, also **kein sicherer Fund** - ich habe nichts
geaendert und trage sie hier ein.

