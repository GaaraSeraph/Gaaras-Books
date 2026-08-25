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
- **b2 K61, Woos vier Tage.** Erster Entwurf des Schlusskommentars gab ihm ein
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
- **K18, beim Schreiben selbst gefangen und ersetzt.** Erster Entwurf: *"...and he
  had started running it before she finished the sentence."* Das widerspricht dem
  spaeteren *"He went at it on the stairs afterwards and did not get anywhere."*
  Jetzt: *"...and no way at all to check the answer."*
- **K23, ebenso.** Erster Entwurf: *"He had handed a man to a woman of eighty-one
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

#### Block 4 - K21, K28, K29, K30, K33, K50, K52, K63, K68 (13 Kommentare)

Die zweite Stufe: neun Kapitel zwischen 8,0 und 9,5. Weniger je Kapitel als in
Block 3, weil diese Kapitel den Erzaehler ueberwiegend schon haben - K30 endet
auf *"He has never done that in a room with her in it."*, K52 auf *"There is one
other man in this story who does not eat in front of the person he is working
on."* Dort wird nichts danebengesetzt.

**Meldung 2 - Zahl, Datum oder Dauer in einem eingesetzten Satz**

| Kap | Eingesetzt | Woher |
|---|---|---|
| K21 | *"That is the arithmetic he has been carrying **since April**..."* | Georgij: *"I have been trying since the twenty-third of April"* |
| K28 | *"...carried it up **three floors**..."* | Hwang sitzt im dritten Stock, im Kapitel |
| K50 | *"A solicitor got to it in **ninety seconds** ... and it had taken Georgij **five months**."* | *"He took about ninety seconds"*; Beginn 2. Maerz, Kapiteltag 28. Juli |
| K52 | *"...for **eleven years** ... **one page** and **nine minutes**."* | elf Jahre Blumen; Georgij spricht in neun Minuten einen Satz |
| K63 | *"He had spent **seven minutes**..."* | *"He took about seven."* |
| K63 | *"...a fact from when she was **nine**."* | Mr Ahn: *"She's been furious with me since she was nine."* |
| K68 | *"A man had found out at **sixty-three** what he was for..."* | Sim: *"I am sixty-three ... I have just found out what it was for."* |
| K68 | *"...the **two** words he did not use."* | *only* und *just*, im Kapitel benannt |

**Meldung 3 - Absoluta in eingesetzten Saetzen**

| Kap | Eingesetzt | Deckung |
|---|---|---|
| K21 | *"**Nobody** in that building had **ever** said it to him..."* | Erzaehlerurteil. Siehe *Unsicher* |
| K28 | *"...the **one** man in that building who would have known what it was."* | Hwang hebt alles auf und ist der Verwalter |
| K29 | *"...the **one** line that could end the house he lives in..."* | im Kapitel ausgefuehrt |
| K29 | *"...the **only** part of it that was ever hers."* | ihre eigene Zeile: *"I bought the book myself"* |
| K30 | *"...and **nobody** had asked her for either."* | im Wechsel nachpruefbar |
| K63 | *"...the **one** thing he owns that nobody could have taken off him..."* | seine eigene Zeile: *"Nobody knows that."* |

**Meldung 1 und 4:** keine.

**Gegenprobe `faktenspur.py --seit e6e4d76`:** sieben Kapitel, alles oben
aufgeloest. K30 und K33 meldet sie nicht - dort steht in keinem der zwei Saetze
eine Zahl.

**Unsicher**

- **K21** - *"Nobody in that building had ever said it to him, because everybody
  in that building had thought he was the improvement."* Behauptung ueber ein
  ganzes Haus ueber fuenf Monate. Traegt den Sinn, ist aber nicht belegbar.
- **K52, beim Gegenlesen ersetzt.** Erster Entwurf: *"...for eleven years without
  once having to think about it."* Das ist falsch: Sim sagt im selben Kapitel,
  er habe die Leute **selbst ausgesucht und sei zweimal hingefahren**. Jetzt:
  *"...and had never once been given a reason to ask."*
- **K63, beim Gegenlesen ersetzt, und das ist der Fund dieses Blocks.** Erste
  Fassung: *"It is the first thing he has said about her in either conversation
  that was not about the four years."* Gegengelesen an **b2 K56**, wo Mr Ahn
  sagt: *"I've told her everything since we were small."* **Der Superlativ war
  schlicht falsch**, und er wurde erst gefunden, weil ich ihn fuer dieses Blatt
  belegen wollte. Jetzt steht dort ein Satz ohne Superlativ.

**Damit zum dritten Mal dieselbe Fehlerklasse, und sie hat jetzt eine Form:**
der Erzaehlerkommentar greift ueber die Szene hinaus - auf ein anderes Kapitel,
auf ein ganzes Gebaeude, auf elf Jahre - und **niemandem faellt es auf, weil der
Erzaehler nicht widersprochen wird.** Die Gegenprobe, die es faengt, ist nicht
`faktenspur.py`: es ist der Zwang, fuer jedes Absolutum eine Fundstelle in
dieses Blatt zu schreiben.

#### Block 5 - der Rest von Band 2, und warum er fast leer ist (2 Kommentare)

**Die restlichen einundvierzig Kapitel sind durchgesehen und zwei davon
angefasst.** Das ist kein Abbruch, sondern der Befund.

Statt jedes Kapitel ganz zu lesen, ist gemessen worden, **wo der Leser am
laengsten allein ist**: die laengste Strecke aufeinanderfolgender Absaetze ohne
einen tragenden Erzaehlerabsatz. Die zwoelf laengsten Strecken sind dann von
Hand angesehen worden. Ergebnis: **jede einzelne landet auf einem
Erzaehlerabsatz**, und zwar auf einem guten -

> b2 K15: *"A man who says a true thing in a room and then does not act on it
> has made himself feel better and changed nothing whatever."*
> b2 K27: *"There was nothing available that was both true and small enough to
> survive being said."*
> b2 K07: *"There is no fault anywhere in that sentence. That is what makes it
> the worst one he has had all month."*

**Der Erzaehler steht dort, wo er hingehoert: am Ende der Strecke, nicht
mittendrin.** Danebenzuschreiben waere Polsterung.

Zweite Probe: **von einundzwanzig Kapiteln enden neunzehn auf Erzaehlung**, nur
K24 und K45 auf einer Figurenzeile. K24 traegt drei Absaetze vorher bereits
*"A table at half past twelve is a table at which somebody is going to have to
decide whether to eat."* - dort ist nichts offen. **K45 war offen**, und hat
einen bekommen.

**Die zwei Kommentare**

| Kap | Eingesetzt | Warum dort |
|---|---|---|
| K04 | *"He had said the worst thing a man in his position can say about himself, and he had said it to somebody with nothing to trade it to."* | die laengste Strecke des ganzen Bandes (30 Absaetze) landet erst zwei Repliken spaeter |
| K45 | *"She put two fingers on his wrist and then sent him to be decent to a stranger, and only one of those was an instruction."* | Kapitelschluss auf einer Figurenzeile, ohne Landung |

**Meldung 2:** K45 *two fingers* / *one* - beides steht in derselben Replik.
**Meldung 1, 3 und 4:** keine.

---

### Stand des Durchgangs

**Band 2 ist durch. 29 von 68 Kapiteln angefasst, 67 Saetze eingesetzt.**

| Block | Kapitel | Saetze | Auswahl nach |
|---|---|---|---|
| 1 | K53, K61 | 6 | Muster, vom Autor abgenommen |
| 2 | K05 K09 K12 K18 K20 K22 K23 | 14 | Erzaehlerdichte unter 8,0 |
| 3 | K32 K40 K42 K48 K59 K62 K64 K65 K67 | 17 | Erzaehlerdichte unter 8,0 |
| 4 | K21 K28 K29 K30 K33 K50 K52 K63 K68 | 13 | Erzaehlerdichte 8,0 bis 9,5 |
| 5 | K04, K45 | 2 | laengste erzaehlerfreie Strecke, Kapitelschluss ohne Landung |

**Die neununddreissig nicht angefassten Kapitel sind gelesen oder gemessen und
absichtlich so geblieben.**

**Vier eigene Saetze sind waehrend des Durchgangs als falsch erkannt und ersetzt
worden** (K61, K18, K23, K52, K63 - fuenf, genau genommen), **und alle fuenf
sind an derselben Stelle gefunden worden: beim Versuch, sie fuer dieses Blatt zu
belegen.** Kein Werkzeug hat einen davon gefunden. `faktenspur.py` kann sie
nicht finden, weil in vieren keine Zahl steht.

**Was noch offen ist:** die Absoluta unter *Unsicher* in Block 3 und 4,
insbesondere **K67** (*"the last thing she is known to have decided"*), das
gegen den Kalender geprueft gehoert. Und **Band 1 ist noch nicht angefasst** -
dort ist die Erzaehlerdichte hoeher (13,4 gegen 12,4) und das duennste Kapitel
liegt bei 4,0, also ist mit deutlich weniger zu rechnen als in Band 2.

---

### Durchgang Erzaehlerkommentare, Band 1 - Ausgangsstand `6c70e36`

Dasselbe Verfahren, dieselbe Form. **Vier von vierunddreissig Kapiteln
angefasst, sechs Saetze.** Das ist weniger als ein Fuenftel der Band-2-Quote,
und der Grund steht in der Messung: Band 1 hat 13,4 Erzaehlerabsaetze je 1000
Woerter gegen 12,4, und nur acht Kapitel liegen unter 9,5.

**Ein Befund, der die Auswahl geaendert hat.** Elf Band-1-Kapitel enden auf
einer Figurenzeile - in Band 2 waren es zwei, und dort war das eine Luecke. In
Band 1 ist es **Absicht und es traegt**:

> K01: *"Unless somebody buys him first."*
> K05: *"I went back and watched you not do it nine times."*
> K19: *"You have not got a house either. ... Then find somebody who has."*
> K28: *"It is exactly the same, and it came out well. Go to bed, Georgij."*
> K31: *"...one day it is going to get you into a room you should not be in."*

**Hinter keinen davon gehoert ein Erzaehlerabsatz.** Ein Kapitel, das so endet,
endet dort mit Absicht. Die Heuristik aus Band 5 ist hier also **kein
Fehlersignal, sondern eine Stilangabe** - und sie steht hier, damit sie nicht in
einem spaeteren Durchgang als Mangel gelesen wird.

**Gepruefte und absichtlich nicht angefasste Kapitel:** K11 (6,6), K19 (8,5),
K21 (9,2), K31 (9,4). K11 traegt bereits *"Georgij discovered that he would very
much rather have been shouted at."*, K19 *"There is a difference between a man
who is given a good reason and a man who finds one."*, K21 laendet auf vierzig
Minuten Hausbegehung, K31 auf Woos Schlusszeile.

**Die sechs Kommentare**

| Kap | Eingesetzt |
|---|---|
| K15 | *"Two women had settled what he is, across a table, in the third person, and neither of them had asked him."* |
| K27 | *"He owns nothing and can sign nothing, and for one afternoon that was the whole of his qualification."* |
| K27 | *"Nobody in it was going to owe anybody anything afterwards, which is not how the rest of the year has gone."* |
| K28 | *"She had told him that people have been covering for him all year, and she had put it where it would sting."* |
| K28 | *"He had told a woman a thing he has never told anybody, and she had answered by counting it."* |
| K30 | *"He had come out onto a terrace with a question and no answer to it, and she had supplied both the answer and the reason to take it."* |

**Meldung 2 - Zahl in einem eingesetzten Satz**

| Kap | Eingesetzt | Woher |
|---|---|---|
| K15 | *"...in the **third** person..."* | grammatischer Begriff, keine Angabe |
| K15 | *"**Two** women..."* | Annie und Hana, im Raum |
| K27 | *"...for **one** afternoon..."* | die sechs Stunden des Kapitels |

**Meldung 3 - Absoluta**

| Kap | Eingesetzt | Deckung |
|---|---|---|
| K27 | *"He owns **nothing** and can sign **nothing**..."* | Grundregel 2 in `CLAUDE.md` |
| K27 | *"**Nobody** in it was going to owe anybody anything..."* | Georgij: *"there is nothing in it for me at all"* |
| K28 | *"...a thing he has **never** told anybody..."* | seine eigene Zeile: *"In seventeen years, nobody in a house I was working in has wanted anything from me that was not work."* |

**Meldung 1 und 4:** keine gestrichen. **Eine eingesetzt** - siehe unten.

**Gegenprobe `faktenspur.py --seit 6c70e36`:** zwei Kapitel, beide oben
aufgeloest.

**Unsicher**

- **b1 K28, und das ist die einzige Meldung der Klasse 1 im ganzen Durchgang.**
  An der Stelle *"Then I will take both..."* / *"No."* / *"You are going to be
  the most solvent person in that room..."* standen **zwei Redebloecke Georgijs
  hintereinander ohne etwas Koerperliches dazwischen** - gegen Grundregel 5. Der
  Erzaehlerkommentar schliesst die Luecke und uebernimmt damit zugleich die
  Sprecherkennzeichnung. **Er ist also nicht nur Ton, und deshalb steht er hier.**
  Wenn er faellt, muss an seiner Stelle ein Beat stehen.
- **b1 K27** - *"which is not how the rest of the year has gone"*. Ein Urteil
  ueber siebenundsechzig Tage, aus Kapitel 27 heraus gesagt. Traegt, ist aber
  eine Aussage ueber das Buch und nicht ueber die Szene.

---

## Der Durchgang ist abgeschlossen

**102 Kapitel gemessen, 33 angefasst, 73 Saetze eingesetzt.**

| | Kapitel | angefasst | Saetze |
|---|---|---|---|
| Band 2 | 68 | 29 | 67 |
| Band 1 | 34 | 4 | 6 |

**Die Fehlerklasse dieses Durchgangs, in einem Satz:** *der Erzaehlerkommentar
behauptet mehr, als die Szene hergibt* - ein Motiv, das die Figur nicht hat, ein
Superlativ ueber ein anderes Kapitel, eine Absicht, die die Figur bestreitet.
**Sechsmal passiert, sechsmal gefunden, keinmal von einem Werkzeug.** Gefunden
wurde jeder einzelne beim Versuch, ihn fuer dieses Blatt zu belegen.

**Daraus die Empfehlung fuer den naechsten Durchgang dieser Art:** die Pflicht,
jedes Absolutum mit einer Fundstelle einzutragen, ist nicht die Buchhaltung
hinterher. **Sie ist die Pruefung.**

---

### Nachtrag: zwei Entscheidungen des Autors, und eine davon ist ein belegter Fehler

Beide Stellen standen unter *Unsicher* und sind vom Autor entschieden worden.

#### 1. b2 K22 - der Kommentar ist ersatzlos entfernt

> gestrichen: *"The difference is whether the man doing it wants to, and it
> makes no difference whatever to the man it is done to."*

**Er beantwortete, was Georgij eine Zeile vorher ausdruecklich verweigert**
(*"you have not got the first idea why, and I am not going to explain it to
you"*). Der Erzaehler hat die Verweigerung damit aufgehoben. `ch22` ist auf
v1.6, an der Stelle steht nichts mehr.

#### 2. b2 K67 - geprueft, widerlegt, ersetzt

> alt: *"It is the last thing she is known to have decided, and it was about
> flowers."*
> neu: *"She had finished deciding before she came up those stairs, and the only
> thing she had left to arrange was where the flowers went."*

**Der alte Satz behauptete den Zeitstrahl, und der Text widerspricht ihm an drei
Stellen, alle in b2 K40:**

| Fundstelle | Wortlaut |
|---|---|
| K40, Jangs dritte Vermutung | *"a person who is allowed to stand at a window and **choose when the light goes off** has more left than most of what I have seen"* |
| K40, Jangs Zaehlung | *"I have seen the light in it on **eleven of the sixteen nights**, always off by ten."* |
| K40, Kapitelschluss | *"a woman awake before six, in a building with a rota, is **not, whatever else is true about her, asleep to what is happening to her**."* |

Die dritte ist die schlimmste: **das ist der Erzaehler selbst, und er sagt das
Gegenteil.** Mein Satz in K67 haette also einen Erzaehlerabsatz gegen einen
anderen gestellt, elf Kapitel auseinander, und in beiden haette der Leser dem
Erzaehler geglaubt.

**Der Ersatz benutzt nur die Szene** - Mrs Ha: *"She had decided something and
she'd finished deciding it. There was nothing left in her about it at all."* -
und behauptet nichts ueber die elf Jahre danach.

**Auch mein eigener Rueckfall war unsicher** - ein verworfener Entwurf:

> *"the last thing she asked anybody for"*

Auch das ist eine Aussage ueber den Zeitstrahl, und die Blumen sind ausserdem
keine Bitte, sondern eine Anweisung (*"send them to the hospital in Mapo"*).
**Ein kleinerer Superlativ ist derselbe Fehler in leiser.**

#### Was das fuer die Fehlerklasse heisst

**Erster Anlauf, und er war falsch.** Ich hatte geschrieben: *ein
Erzaehlerkommentar darf nichts behaupten, was ausserhalb seiner eigenen Szene
liegt.* **Vom Autor zurueckgewiesen, und zu Recht:**

> *"Ein Kommentar darf Sachen behaupten, die ausserhalb seiner Szene liegen.
> Das ist der Charme dieses Buchs. Er darf nichts behaupten, was nicht stimmt,
> und claims muessen verifiziert sein gegenueber Sachen im Buch."*

Das ist auch die einzige Regel, die zu diesem Buch passt. Der Erzaehler greift
seit Kapitel 1 aus - *"the third time he has written his name in a book at a
door in eight weeks"*, *"which she has done perhaps three times since October
and never once in that room"*. **Der Griff ist das Mittel. Die Grenze ist nicht
seine Reichweite, sondern sein Beleg.** Also:

> **Ein Erzaehlerkommentar darf so weit ausgreifen, wie er will - ueber
> Kapitel, ueber Jahre, ueber die ganze Handlung. Jeder Griff muss am Text
> belegbar sein, und der Beleg gehoert in dieses Blatt.**

Der Unterschied ist praktisch und nicht akademisch: nach der falschen Regel
waeren zwei richtige Saetze gestrichen worden, und vier weitere waeren zu
Beobachtungen ohne Reichweite geschrumpft.
`faktenspur.py` hat keinen davon gefunden, `check.py` keinen, `belege.py`
keinen. Gefunden wurden sechs beim Belegen fuer dieses Blatt und **einer vom
Autor beim Lesen des Blatts** - was der eigentliche Zweck des Blatts ist.

#### Eine Falle in `belege.py`, gefunden beim Schreiben dieses Nachtrags

Die Vorschlagsmarke wird **nur in der letzten Zeile des Absatzes vor dem Zitat**
gelesen, nicht irgendwo im Absatz. `vorschlagszeilen()` setzt `vorlauf` bei
jeder nichtleeren Zeile neu, also loescht die zweite Zeile eines umgebrochenen
Absatzes die Marke aus der ersten wieder.

In einem Repo, in dem alle Dokumente auf achtzig Zeichen umgebrochen sind, ist
das die haeufigste Art, wie eine richtig gemeinte Markierung stillschweigend
nicht wirkt. Wer markiert, schreibt das Wort in die **letzte** Zeile vor dem
Zitat - oder `vorlauf` merkt sich die Marke bis zur naechsten Leerzeile.

**Nicht von mir geaendert**, `belege.py` gehoert der Pruefsitzung.

---

### Alle Unsicher-Punkte durchgeprueft

Auftrag des Autors. Massstab ist die korrigierte Regel: **nicht innerhalb der
Szene bleiben, sondern belegbar sein.** Vierzehn Stellen, drei Ergebnisse.

#### A. Haelt und bleibt, weil belegt

| Kap | Satz | Beleg |
|---|---|---|
| b2 K21 | *"**Nobody** in that building had **ever** said it to him, because **everybody** in that building had thought he was the improvement."* | Mrs Jeon, b2 K07: *"He is the most honest person I have ever worked for ... he has spent five months making them not a disgrace, and he is proud of it, and he has every right to be."* Georgij, b2 K10: *"That page exists because somebody made the house honest. **Nobody in it has understood that yet.**"* |
| b2 K05 | *"It was the **only asset he had ever had**, and it was not anything he had done."* | `CLAUDE.md` Grundregel 2 (er besitzt nichts); seine eigene Zeile im selben Wechsel: *"It is the only true thing I have that is worth anything to you."* |
| b2 K48 | *"It was **the whole of** what he thought of the afternoon..."* | Praezedenz im Buch fuer dieselbe Kamerafreiheit: b2 K42, *"Sang-hoon took that better than Georgij had expected, and worse than he let it show."* |
| b2 K09 | *"...and **she does not do that**."* | Hausformel des Erzaehlers, quer durch beide Baende (*"which she does perhaps twice a month"*, *"which is not a thing he does"*) |
| b2 K53 | *"...and it was **the largest one** the man had."* | **vom Autor abgenommen** |

**Beide zurueckgestellten Saetze waren vorher gestrichen worden** - unter der
falschen Regel. Sie stehen wieder drin.

#### B. Neu geschrieben: greift jetzt weiter aus als vorher **und** ist belegt

| Kap | vorher | jetzt | Beleg |
|---|---|---|---|
| b2 K12 | *"the nearest thing to a complaint he had ever made in that room"* - unbelegbarer Superlativ ueber acht Monate | *"**In March** he told her that his one asset is that other men want him. **Three weeks later** he told her whose hand he wants on it."* | b2 K05 ist der 11. Maerz, b2 K12 der 3. April - dreiundzwanzig Tage |
| b2 K64 | *"the only promise anybody has made her in four years"* - behauptet Kenntnis von allem, was ihr in vier Jahren gesagt wurde | *"It is the answer to **the first question she has asked him in four years**, and it is about a roof."* | Sim im selben Kapitel: *"She has never once asked me a question in four years ... she asked me one."* |
| b2 K65 | *"the only sentence anybody has said to him this year"* | *"**In March** she told him she had **never in her life told anybody anything the whole way through**. She had just done it, and she had done it to him."* | Mrs Sunwoo, b2 K10, woertlich |
| b1 K28 | *"people have been covering for him all year"* - es sind zehn Wochen, kein Jahr | *"He has been counting what everything costs **since October**, and she had just told him he has been counting **one side of it**."* | er kam am 4. Oktober; b1 K27, Tag davor: *"Ten on Saturday."* |

**Das ist der eigentliche Ertrag der Pruefung.** Die vier Saetze sind nicht
kleiner geworden, sondern groesser: drei von ihnen greifen jetzt ueber ein
anderes Kapitel hinweg, und jeder Griff hat eine Fundstelle.

#### C. Bleibt korrigiert, weil der alte Satz **nicht stimmte**

| Kap | falscher Satz | woran er scheitert |
|---|---|---|
| b2 K28 | *"...to **the one man in that building** who would have known what it was."* | Am 9. Januar sass **Mr Byun** noch in dem Gebaeude - sechsundzwanzig Jahre Register, er haette es besser gewusst als Hwang. Jetzt: *"to the man who keeps everything"* (Kapiteltitel, und Georgijs eigene Zeile) |
| b2 K29 | *"...**the only part of it** that was ever hers."* | Der Inhalt ist auch ihrer - sie hat ihn geschrieben. Jetzt: *"kept the book, which she had bought herself"* (ihre eigene Zeile) |
| b2 K32 | *"the only thing he said all morning that he had **not decided on the bus**"* | Der Bus steht im Kapitel, das Entscheiden darauf ist **erfunden** |
| b2 K32 | *"kept back the only part of it **that would have helped him**"* | Mr Hwang sagt ausdruecklich *"Not for him."* |
| b2 K40 | *"the **only** thing he said all morning that was about himself"* | Jang sagt im selben Gespraech *"Thirty years in this work ... I have stood outside two other buildings like this one."* |
| b2 K40 | *"...a different refusal from the one **on a landing**."* | Kein Sachfehler, ein Handwerksfehler: **Georgij sagt *landing* vierunddreissig Zeilen spaeter selbst**, und seine Zeile ist die bessere. Der Erzaehler nahm sie ihm vorweg |
| b2 K50 | *"...and it had taken **Georgij five months**."* | Georgij ist dort **nicht** angekommen: *"I do not know that yet ... I have two documents and a quantity of groceries."* |
| b2 K62 | *"the only thing anybody has found that will work on him"* | Widerspricht Georgij selbst in b2 K50: *"There is exactly one thing on this earth that will move that man ... It is finding out what the kind version was covering."* Das Abendessen ist die Folge, nicht der Hebel |
| b1 K28 | *"a thing he has **never told anybody**"* | Nicht pruefbar. Jetzt: *"He had given her two things and called it one, and she counted them"* - was Hana tatsaechlich tut, und es fuellt zugleich die Beat-Luecke |
| b1 K27 | *"...which is not how the rest of the year has gone."* | **Kein Wahrheitsproblem, ein Platzproblem:** der Satz stand hinter der letzten Zeile des Kapitels, und die ist eine Figurenpointe. Ersatzlos raus, nach demselben Befund, der fuer die elf Band-1-Schluesse gilt |

#### Bilanz

**Vierzehn geprueft: fuenf halten, vier sind groesser geworden, acht waren
falsch und sind es nicht mehr, einer ist aus Platzgruenden raus.**

Von den acht Fehlern hat **kein einziger** an einer Zahl gehangen, die
`faktenspur.py` sehen kann. Sechs hingen an einem **Superlativ** (*only*,
*never*, *nobody*, *the one*), einer an einer **erfundenen Handlung** (der Bus),
einer an einem **Widerspruch zu einer anderen Figur** (Hwangs *"Not for him"*).

**Daraus die Arbeitsregel, und sie ist enger als jede Zaehlung:** Steht in einem
Erzaehlerkommentar ein Superlativ, gehoert die Fundstelle daneben, bevor der
Satz ins Buch geht. Steht keine da, ist der Superlativ noch nicht wahr - er ist
nur noch nicht widerlegt.

**Gegenprobe `faktenspur.py --seit 1c9dde2`:** acht Kapitel. Aufgeloest: b1 K28
`october` +1, `one` +2, `two` +1 (*since October*, *one side of it*, *two
things*); b2 K12 `march` +1, `three` +1 (*In March ... Three weeks later*); b2
K64 `first` +1 (*the first question*); b2 K65 `march` +1 (*In March*); b2 K28,
K40, K62 je eine Zahl **weniger**, weil dort ein falscher Superlativ
verschwunden ist; b2 K50 tauscht *five months* und *ninety seconds* gegen
*thirty years*. **b2 K05 und K21 meldet sie gar nicht** - dort steht wieder
genau der Satz, der vorher schon dastand, und die beiden Zwischenfassungen aus
der falschen Regel sind geloescht statt committet. Aus demselben Grund tragen
die vier neu geschriebenen Kapitel die **naechste** Nummer und nicht die
uebernaechste: ein Zwischenschritt, den nie jemand lesen sollte, gehoert nicht
ins Archiv, weil `faktenspur.py` und `belege.py` beide gegen alte Fassungen
vergleichen.

---

### Band 1 vollstaendig durchgegangen - und das Ergebnis ist ein Nicht-Ergebnis

Auftrag: Band 1 genauso wie Band 2. Alle vierunddreissig Kapitel gelesen oder
gemessen. **Ergebnis: die vier bereits angefassten Kapitel waren die richtigen
vier, und es kommt keines dazu.**

Das ist keine Bequemlichkeit, sondern steht auf drei unabhaengigen Proben.

#### Probe 1: worauf landet die laengste reine Dialogkette

Fuer jedes Kapitel die laengste Folge aufeinanderfolgender Redeabsaetze ohne
einen einzigen Erzaehlerabsatz dazwischen - dort ist der Leser wirklich allein -
und dann der Absatz, der sie beendet.

**Vierunddreissig von vierunddreissig landen auf Erzaehlung.** Kein einziges
Kapitel laesst den Leser aus einer Dialogstrecke ins naechste fallen. Die
laengste Kette des Bandes ist fuenfzehn Repliken (K19), der Median acht - Band 2
hat neunzehn und sieben. **Strukturell sind die beiden Baende fast gleich.**

#### Probe 2: tragende Erzaehlerabsaetze

Absaetze ueber zwanzig Woertern, keine Rede - also die Saetze, die etwas
benennen statt einen Beat zu setzen.

| | tragende Absaetze | je 1000 Woerter | Kapitel ohne einen |
|---|---|---|---|
| Band 1 | 948 | **9,48** | keines |
| Band 2 | 1391 | 8,60 | keines |

**Und die sechs duennsten Band-1-Kapitel sind K27 (2,0), K28 (4,2), K15 (4,3),
K19 (5,0), K30 (5,1), K21 (5,9).** Vier davon sind genau die vier, die schon
angefasst sind - unabhaengig gefunden, ueber eine andere Messung als beim ersten
Mal. K19 und K21 sind zweimal gelesen worden und tragen sich.

#### Probe 3: gelesen

K01, K02, K03, K04, K06, K11-K15, K17-K20, K22-K28, K30, K32 ganz gelesen, der
Rest ueber Probe 1 und 2 geprueft. Beispiele fuer das, was dort ohnehin steht:

> K12: *"...the most carefully constructed sentence he had heard since the
> auctioneer said the word **unverifiable**."*
> K17: *"Somebody else had heard the difference before he did."*
> K20: *"He had been in eleven houses and had never once been unable to read a
> woman across a desk, and the difference now was not that she had become harder
> to read. It was that he had stopped assuming he could."*
> K23: *"A man who demonstrates that he can leave, and cannot, has demonstrated
> one thing only, and it is not the thing he meant."*

**Danebenzuschreiben waere in jedem dieser Faelle Polsterung gewesen.**

#### Bilanz des ganzen Durchgangs

**102 Kapitel gemessen, 33 angefasst, 71 Saetze im Buch.**

| | Kapitel | angefasst | Saetze |
|---|---|---|---|
| Band 2 | 68 | 29 | 65 |
| Band 1 | 34 | 4 | 6 |

---

### Nachtrag zur Pruefsitzung: meine eigenen Zahlen in doc/12

Der Einwand aus der Pruefsitzung ist angekommen und er trifft mich: **ein
falsches Blatt wird im Durchgang in hundert Kapitel geschrieben.** Bei Hana ist
genau das beinahe passiert.

Meine Beitraege zu `doc/12` sind groesstenteils **gemessen** und damit
mechanisch nachpruefbar. Nachgemessen am 25.08.:

| | stand da | misst jetzt |
|---|---|---|
| Mr Ahn, Kontraktionen je 1000 W | 96,6 | **106,7** |
| Woo, Kontraktionen je 1000 W | 4,1 | **4,2** |
| Mrs Ha | fehlte | **14,9** |

Beide Abweichungen kommen daher, dass seither Kapitel dazugekommen sind. **Der
Befehl steht jetzt neben der Tabelle** (`stimmen.py --tics`), damit
Nachmessen eine Minute kostet und keine Entscheidung ist.

**Was daran allgemein ist, und es ist eine dritte Sorte neben Zitat und
Behauptung:** eine **Messung** ist wahr zum Zeitpunkt der Messung und driftet
danach von selbst, ohne dass jemand etwas Falsches tut. `belege.py` findet sie
nicht, weil kein englisches Zitat darin steht. Die einzige Abwehr ist, den
Befehl danebenzuschreiben.

**Die riskanten Stellen in meinen Blaettern sind die *gelesenen*, nicht die
gemessenen** - Ye-rins Blatt steht ausdruecklich auf *"aus Band 1, Kapitel 30
gelesen und nicht gezaehlt"*, weil `stimmen.py` bei ihr nur fuenf Repliken
findet. Wer `doc/12` durchgeht, faengt dort an und nicht bei den Tabellen.

---

### doc/12 gegengelesen, die gelesenen Blaetter zuerst

Auftrag des Autors, nachdem die Pruefsitzung an Hanas Blatt eine erfundene
Selbstaussage gefunden hatte. Bisher zwei Blaetter durch - **Ye-rin und Jang -
und beide waren falsch, Jang auf eine Art, die bereits ins Buch geschrieben
worden war.**

#### Der schwerste Fund: ein Defekt in `stimmen.py`, und das Werkzeug ist meins

Der Kontraktionszaehler stand auf `\w+'(?:s|t|re|ve|ll|d|m)` und traf
**jeden Genitiv** - *Woo's*, *brother's*, *somebody's mother*. Wer viel ueber
fremdes Eigentum redet, sah aus wie jemand, der zusammenzieht.

**Die Standeslinie in `doc/12` war genau eine Aussage darueber, wer zusammenzieht,
und sie stand vollstaendig auf diesem Zaehler.**

| | stand in doc/12 | misst wirklich |
|---|---|---|
| Mr Ahn | 106,7 | **78,7** |
| **Mrs Seo** | **17,9** | **0** |
| Jang | 13,8 | **3,4** |
| Hana | 11,9 | 5,3 |
| **Mrs Gwak** | **10,2** | **0** |
| **Mr Chae** | **8,9** | **0** |
| Annie | 6,3 | 3,5 |
| Woo | 4,1 | 1,7 |
| Sang-hoon | 3,8 | 1,1 |
| Georgij | 3,4 | **2,5** |

**Drei Figuren standen bei zehn bis achtzehn und ziehen kein einziges Mal
zusammen.** Und Georgij zieht oefter zusammen als Woo und Sang-hoon - in der
alten Tabelle stand er ganz unten.

**Die Regel, die darauf stand, ist gefallen:** *"Wer nicht im Gewerbe ist, zieht
zusammen."* Mrs Seo fuehrt einen Haushalt, Mrs Gwak hat einen Blumenladen, beide
null. **Ein Durchgang nach dieser Regel haette drei Figuren ein Register
erfunden.**

**Was statt dessen dasteht und brauchbarer ist:** Mr Ahn 78,7, eine
Groessenordnung ueber allen; danach Rauschen; und **dreizehn benannte Figuren
bei exakt null**, quer ueber beide Baende. Die Null ist ein Verbot und keine
Tendenz.

`stimmen.py` ist repariert und eicht sich an acht Proben, darunter *the gravel's
been raked* gegen *the gravel's colour*.

#### Jang: vier Behauptungen, vier falsch - und eine hatte schon gewirkt

| Behauptung | Befund |
|---|---|
| *"Er zieht zusammen, in beiden Baenden."* | **Drei Kontraktionen im ganzen Buch**, alle drei in **einem** Wechsel ueber Kies in b1 K05. Sonst nirgends |
| *"Er ist der langsatzigste Sprecher des Buchs, alle anderen liegen bei sieben bis acht."* | Hwang 11,9 · Georgij und Sang-hoon 11,6 · Yeom 11,4 · **Jang 11,2** · Woo 11,0. Mittelfeld |
| *"Er laesst sich nicht einschenken."* | b1 K23: Georgij schenkt ihm mit beiden Haenden ein, er sagt *"You should not do that."* - **und trinkt es** |
| 45 Repliken, 721 Woerter, Ø 12,2, laengster 37 | jetzt 40 Repliken, 585 Woerter, Ø 11,2, 8 Prozent ueber 25 |

**Die erste hat bereits ins Buch gewirkt.** Auf sie hin sind in b2 K40 zwei
Kontraktionen in Jangs Repliken geschrieben worden. **Damit hat sich die
Behauptung selbst gemessen:** das Blatt sagte, er ziehe zusammen; ich machte ihn
zusammenziehen; das Werkzeug meldete danach, dass er zusammenzieht.
**Zurueckgenommen in ch40 v2.6.** Das *ma'am* bleibt - das ist die Entscheidung
des Autors und nicht meine Ableitung.

#### Ye-rin: fuenf Behauptungen, fuenf falsch

| Behauptung | Befund |
|---|---|
| *"Kein Titel, kein Name."* | Sie sagt **"Mr Georgij."** - einmal, an der Tuer, unmittelbar vor den zweiundzwanzig Minuten |
| *"Kein Wort ueber Gefuehle."* | *"I have disliked everything so far."* · *"You are very bad at selling things."* |
| *"keine Frage, die sie nicht selbst beantwortet"* | Sie stellt in b1 K30 mindestens acht und Georgij beantwortet die meisten |
| *"sie spricht nie zuerst aus sich selbst"* | In der zweiten Haelfte des Kapitels ausschliesslich aus sich selbst. **Der Wechsel ist ihr Bogen** |
| *"Wenn sie sich umdreht, ist das die Szene."* | Fuenfmal markiert, **zwei** davon Ereignisse |

**Die erste ist die gefaehrlichste, die dieser Durchgang gefunden hat.** Ein
Stildurchgang, der dem Blatt gefolgt waere, haette **"Mr Georgij." gestrichen** -
die einzige Anrede, die sie im ganzen Buch benutzt, und der Schluss des Kapitels.
Sie steht jetzt im Blatt als **festgelegt**.

Dazu die Ueberschrift: *"Kim Ye-rin (17 Repliken)"*. Die Terrassenszene in b1 K30
hat **117 Redeabsaetze im Wechsel**, also rund siebenundfuenfzig fuer sie - in
einem Kapitel. Die Falle steht woertlich in `CLAUDE.md` und hat trotzdem
funktioniert.

#### Was das ueber die Blaetter sagt

**Zwei gelesene Blaetter, neun falsche Behauptungen.** Keine davon war eine
Erfindung aus dem Nichts - jede war eine **Verallgemeinerung aus einer richtigen
Beobachtung**: Ye-rin benutzt fast nie eine Anrede, also *"kein Titel, kein
Name"*; Jang spricht knapp, also *"der langsatzigste"* (im Kopf gedreht und nie
nachgezaehlt).

**Die Fehlerklasse ist damit dieselbe wie bei den Erzaehlerkommentaren, und der
Massstab auch:** ein Blatt darf ueber die Szene hinausgreifen, aber jeder Griff
muss belegt sein. **Der Unterschied ist der Preis.** Ein falscher
Erzaehlerkommentar steht an einer Stelle. Ein falsches Blatt wird in hundert
Kapitel geschrieben, und bei Jang ist genau das schon passiert.

**Noch offen:** Mrs Seo, Yeom, Hwang, Mrs Jeon, Mrs Bae, Mrs Gwak, Mr Sohn,
Mr Koh, Mr Byun, Mr Chae, Sang-hoon, Hana.

---

### doc/12 vollstaendig gegengelesen - zwoelf Blaetter, dreiundzwanzig Fehler

Alle gelesenen Blaetter durch. **Kein einziges war ohne Fehler.** Zwei davon
hatten bereits ins Buch gewirkt und sind zurueckgenommen.

#### Was ins Buch gewirkt hatte

| Blatt | Behauptung | Was daraus im Buch wurde |
|---|---|---|
| Jang | *"Er zieht zusammen, in beiden Baenden"* | zwei Kontraktionen in b2 K40, von mir. **Zurueckgenommen, ch40 v2.6** |
| Mrs Seo | Standeslinie 17,9 | zwei Kontraktionen in b2 K34 und K37, von mir. **Zurueckgenommen, v1.4 und v2.4** |

**Beide Male hat sich die Behauptung selbst gemessen:** das Blatt sagte, die
Figur ziehe zusammen; ich machte sie zusammenziehen; das Werkzeug meldete danach,
dass sie zusammenzieht. Ohne diese Eingriffe hat **Mrs Seo im ganzen Buch keine
einzige** Kontraktion und **Jang drei**, alle drei in einem Wechsel ueber Kies in
b1 K05.

#### Die uebrigen Fehler

| Blatt | stand da | Befund |
|---|---|---|
| **Ye-rin** | *"Kein Titel, kein Name"* | Sie sagt **"Mr Georgij."** - der Schluss von b1 K30 |
| Ye-rin | *"Kein Wort ueber Gefuehle"* | *"I have disliked everything so far."* |
| Ye-rin | *"keine Frage, die sie nicht selbst beantwortet"* | mindestens acht, Georgij beantwortet die meisten |
| Ye-rin | *"spricht nie zuerst aus sich selbst"* | zweite Kapitelhaelfte ausschliesslich aus sich selbst |
| Ye-rin | *"wenn sie sich umdreht, ist das die Szene"* | fuenfmal markiert, zwei davon Ereignisse |
| Ye-rin | *"17 Repliken"* | rund **57 allein in b1 K30** |
| **Jang** | *"der langsatzigste Sprecher des Buchs"* | Mittelfeld: Hwang 11,9 · Georgij 11,6 · **Jang 11,2** |
| Jang | *"Er laesst sich nicht einschenken"* | b1 K23: *"You should not do that."* - **und trinkt es** |
| Jang | 45 Repliken, 721 W, Ø 12,2 | 40 Repliken, 585 W, Ø 11,2 |
| **Mrs Seo** | *"hoechste Personendichte, 20,5, fuenfmal Georgij"* | **17,5, vierter Platz**, doppelt Georgij |
| Mrs Seo | *"In neun Jahren nicht, was in dem Umschlag ist"* | steht nirgends. Ersetzt: **keine Frage in dreizehn Repliken** |
| Mrs Seo | zwei Beispielbloecke | **sieben erfundene Kontraktionen** fuer eine Figur, die keine hat |
| **Yeom** | *"Er lacht, was in diesem Buch fast niemand tut"* | im Buch wird **35 Mal** gelacht; **Yeom genau einmal** |
| **Hwang** | *"dichteste Datums- und Uhrzeitzaehlung"* | **haelt** - mit Schwelle ab 90 Woertern |
| **Mrs Gwak** | *"zweithoechster Jahreswert nach Sim"* | **hoechster**; Sim nicht unter den ersten fuenf |
| **Mrs Jeon** | *"die einzige Nebenfigur, die sagt, dass sie gehandhabt wird"* | Sang-hoon in b2 K42: *"You are managing me."* |
| Mrs Jeon | Zitat *"until the end"* | der Text sagt *"until the day it did"* |
| **Mr Byun** | *"hoechste Personendichte im Buch"* | zweiter, hinter Ahn (22,5 zu 22,0) |
| **Mr Koh** | *"Er darf: Kontraktionen"* | **keine einzige** in sieben Repliken |
| Mr Koh | 6 Repliken | 7 |
| **Mr Sohn** | Zitat mit which-Satz | **existiert in keiner lebenden Fassung.** Der Text hat zwei Hauptsaetze - besser, und das Blatt hat den Verstoss gelobt |
| Mr Sohn | 7 Repliken | 8 |
| **Hana** | *"dichteste Personenzaehlerin nach Mrs Seo"* | **siebter Platz** (13,2) |
| **Sang-hoon** | *"benotet die Aeusserung - das tut sonst niemand"* | **Yeoms Blatt sagt zwei Seiten weiter, dass er es auch tut**. Das Dokument widersprach sich selbst |

#### Und ein Fehler beim Korrigieren, der die Regel bestaetigt

Beim Berichtigen von Mrs Seos Personendichte habe ich **Mr Sohn mit 27,8 an die
Spitze gesetzt.** Das kam aus einem eigenen Hilfsskript mit lockererer
Sprecherzuordnung; `stimmen.py` misst ihn bei 9,3. **Dasselbe bei Hwang** (18,0
statt 16,3) und **bei Mrs Gwak** (Mr Baek als angeblicher Spitzenreiter, ein
Zuordnungsartefakt).

**Alle drei sind zurueckgenommen. Es gilt, was das Werkzeug im Repo sagt** - ein
Skript, das im Scratchpad liegt und einmal laeuft, ist keine Messung, sondern
eine Meinung mit Ziffern.

#### Die Fehlerklasse, und sie ist bei Blaettern anders als bei Kommentaren

**Dreiundzwanzig Fehler, und nur drei waren Erfindungen.** Die anderen zwanzig
sind zwei Sorten:

1. **Der Superlativ aus dem Kopf.** *Die hoechste, die einzige, der
   langsatzigste, das tut sonst niemand.* Neun Faelle. Jeder war eine richtige
   Beobachtung, die beim Aufschreiben eine Stufe zu weit gegangen ist.
2. **Die Messung, die gedriftet ist.** Sieben Faelle. Niemand hat etwas falsch
   gemacht - es sind Kapitel dazugekommen.

**Daraus die Regel fuer Blaetter, und sie ist strenger als die fuer
Erzaehlerkommentare:** ein Kommentar steht an einer Stelle im Buch, ein Blatt
wird in hundert Kapitel geschrieben. **Ein Superlativ in einem Stimmblatt braucht
die Rangfolge daneben, nicht nur eine Fundstelle** - sonst ist er nur noch nicht
widerlegt. Und **jede Zahl braucht den Befehl daneben**, mit dem man sie
nachrechnet.
