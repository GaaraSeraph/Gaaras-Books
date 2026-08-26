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

---

### doc/12, der Rest: die Regeln, die Achsen, der Index, die gemessenen Blaetter

Damit ist das Dokument ganz durch. **Achtzehn weitere Fehler**, und der schwerste
steht nicht in einem Blatt, sondern in einer Regel.

#### Der schwerste: sechs Anreden, die es angeblich nicht gibt

Achse 3 sagte: *"Er bekommt keinen einzigen Titel zurueck - es gibt im ganzen
Buch kein Rangwort fuer ihn."*

**Es gibt sechs, und sie stehen alle in den letzten fuenf Kapiteln von Band 1:**

| | wer |
|---|---|
| b1 K30 | **Kim Ye-rin**, an der Tuer - die erste |
| b1 K31 | **Hana**, *"Go home, Mr Georgij."* |
| b1 K32 | **Kim Ye-rin**, in der Auffahrt |
| b1 K33 | **Park Sang-hoon**, direkt nach Georgijs *"Chairman Park."* |
| b1 K33 | **Park Sang-hoon**, an der Tuer |
| b1 K34 | **Mr Chae** |

**Das ist ein Bogen und kein Ausrutscher.** Er faengt bei K30 an - bei der Frau,
die ihn zwanzig Minuten lang gar nicht angeredet hat - und danach tun es alle.
**Der Text macht laengst, was das Blatt als Aufgabe auswies**, und ein Durchgang
nach dem alten Eintrag haette alle sechs gestrichen. Jetzt festgelegt.

**Offene Frage an den Autor:** in Band 2 steht keine einzige mehr. Gewollt oder
abgerissen?

#### Der zweitschwerste: eine Figur stand verkehrt herum

Regel 2 sagte: *"Annie haelt nichts zurueck und das ist ihr Kennzeichen."*

Sie haelt **am meisten** zurueck von allen, und die Handlung beider Baende haengt
daran - der Name neunzehn Tage lang (b1 K12), die Weigerung (b1 K11, K34), die
achtundsechzig Tage (b2 K27), *"the smallest piece I could get away with"*
(b2 K18). **Ihr Kennzeichen ist nicht das Nichtzurueckhalten. Es ist, dass sie
das Zurueckhalten ansagt** - mit Frist, mit Grund, ohne Entschuldigung.

#### Ein Befund, der vorher nirgends stand

**Annie hoert in Band 2 auf, Woerter zusammenzuziehen - genau wie Georgij.**

| | Band 1 | Band 2 |
|---|---|---|
| Georgij | 34 | **0** |
| Annie | 18 | **0** |

Zwei Figuren, derselbe Bruch, an derselben Stelle, und keine Figur im Buch
bemerkt es. Georgijs Haelfte stand im Blatt, Annies nicht.

#### Die uebrigen

| Ort | stand da | Befund |
|---|---|---|
| Regel 2 | Mrs Seo und der Umschlag | **zweiter Fundort derselben Erfindung** |
| Regel 2 | Woo: *"Do not thank me"* | er sagt *"**Don't** thank me"* |
| Regel 3 | *"Keine Figur sagt das Warme"* | eine Ausnahme: Sim, b2 K52, und er markiert sie selbst |
| Regel 3 | Woo *"dreimal belegt"* | der Erzaehler sagt *"every time since October"* |
| Regel 6 | Mrs Seo nimmt die Glaeser weg | **einmal im Buch.** Ihre Gewohnheit ist das Tablett um sieben, fuenfmal |
| Achse 1 | *Kontraktionen wenige/viele* | aus dem defekten Zaehler. Der Haushalt zieht nirgends zusammen |
| Achse 1 | 34 Szenen mit zwei Angestellten | 36 **Kapitel**, nicht Szenen |
| Achse 2 | *Chairman* 24 Mal, immer von Georgij | **63 Mal**, auch von Jang und Kang |
| Achse 3 | *Mistress* 89 Mal | **103** |
| Achse 4 | die Ton-Beats *"sind verschwunden"* | *did not soften* steht 15 Mal, *did not look away* 18 Mal |
| Messstand | halbe Tabelle | Kontraktionswerte aus dem defekten Zaehler, vier Figuren standen mit Zahlen da, die es nicht gibt |
| Georgij | *"acht Woerter"* | Ø 11,6 |
| Annie | *"sieben Woerter"* | Ø 10,1 |
| Mrs Ha | *"vierhundert Hochzeiten"* | **411**, und ihre Berichtigung ist die Szene |
| Mrs Ha | *"zweite Zivilistin im Buch"* | vor ihr Gwak, Sohn, Byun, Koh |
| **Mrs Sunwoo** | *"Sie beendet nie einen Satz ganz"* | **Fehllesung.** Der Satz heisst *"never told anybody the whole of anything"* - das ist Auskunft, nicht Satzbau. Das Blatt haette ihr ein Stocken gegeben, das sie nicht hat |
| Index | Jang, Mrs Jeon, Mrs Seo | trugen **drei Maschinen, die ihre eigenen Blaetter zurueckgenommen hatten** |
| Index | Spalte *Repliken* | Warnung ergaenzt: in Zweipersonenstuecken misst sie Begleitsaetze und nicht Text |

**Geprueft und bestaetigt**, damit es nicht zweimal geprueft wird: Woo schuettelt
in elf *hand*-Stellen keine Hand (Sang-hoon gibt sie in b1 K16 ausdruecklich);
Sims falsche Tramnummer steht in b2 K52; Mr Ahns Alterswiderspruch ist im Text
selbst aufgeloest (*"he is never wrong about that by more than a year"*); Hongs
drei Namen sind Woo, Sunwoo und Choi; **alle vier Kollisionspaare halten** - in
keinem Kapitel sprechen beide.

**Aber drei Kapitel stehen an der Grenze:** b2 K34 und b2 K41 (Sang-hoon und
Yeom kommen beide vor, nur einer redet) und b2 K41 (Jang und Mrs Bae). **In K41
stehen zwei Paare gleichzeitig an der Grenze.**

#### Bilanz doc/12

**Einundzwanzig Blaetter und Abschnitte geprueft, einundvierzig Fehler.** Drei
davon hatten ins Buch gewirkt (Jangs und Mrs Seos Kontraktionen, zurueckgenommen).
Zwei haetten beim naechsten Durchgang etwas geloescht, das der Text richtig macht
(Ye-rins *"Mr Georgij."* und die sechs Anreden in Achse 3).

**Und die haeufigste Ursache ist keine Schlamperei, sondern eine Bewegung:** eine
richtige Beobachtung, die beim Aufschreiben eine Stufe zu weit geht. *Sie benutzt
fast nie eine Anrede* wird zu *kein Titel, kein Name*. *Er spricht knapp* wird zu
*der langsatzigste*. **Ein Stimmblatt ist genau da am gefaehrlichsten, wo es
gut formuliert ist.**

---

### Die Anrede fuer Georgij in Band 2 - vom Autor als Drift bestaetigt, repariert

Aus dem doc/12-Durchgang war eine Frage offengeblieben: *"Mr Georgij"* steht
sechsmal in b1 K30 bis K34 und in Band 2 kein einziges Mal. **Antwort des
Autors: keine Absicht.**

**Meldung 1 - eingesetzte Anreden in woertlicher Rede.** Zwei Stellen, beide in
**b2 K04** (ch04 v1.9), beide von **Park Sang-hoon** an Georgij:

| Zeile vorher | Zeile jetzt |
|---|---|
| *"I have thought about it since December and I have not moved off it..."* | *"**Mr Georgij.** I have thought about it since December..."* |
| *"I am telling you where I am." He had the door open and did not get in yet. "Four or five of these a year..."* | *"**Mr Georgij.**" He had the door open and did not get in yet. "I am telling you where I am. Four or five of these a year..."* |

**Warum genau diese zwei und keine anderen.** Die Anrede ist im Buch **ein
Paar** - einer gibt den Titel, der andere gibt ihn zurueck:

> b1 K33, beim Gruss: *"Chairman Park."* / *"Mr Georgij."*
> b1 K33, an der Tuer: *"Mr Georgij."* / *"Chairman."*

**In b2 K04 stand beide Male nur die eine Haelfte da.** Georgij sagt
*"Chairman."* und bekommt nichts zurueck - beim Gruss und an der Wagentuer, in
genau der Szene, in der Sang-hoon ihm das Groesste sagt, was er ihm im ganzen
Buch sagt (*"I have wanted to buy you twice and been told no twice, and both
times I went home and thought about the work and not about the price"*).

**Nicht gestreut.** Sang-hoon spricht in elf Band-2-Kapiteln; angefasst ist
eines, und zwar das erste. Stand jetzt: **Band 1 sechs, Band 2 zwei.**

**Meldung 2 und 3:** keine Zahl, kein Datum, kein Absolutum eingesetzt.
`faktenspur.py` meldet fuer ch04 nur `Georgij 20 -> 22` - die zwei Anreden.

**Meldung 4:** keine festgelegte Zeile beruehrt. Die Stelle ist mit dieser
Reparatur allerdings **selbst festgelegt worden** und steht so in `doc/12`:
**wer die Anrede einsetzt, setzt beide Haelften.**

**Unsicher:** in der zweiten Stelle ist *"I am telling you where I am."* aus dem
ersten in den zweiten Redeblock gerueckt, damit zwischen Sang-hoons beiden
Bloecken der koerperliche Beat steht (Grundregel 5). Der Satz sagt dasselbe an
derselben Stelle des Gedankens - aber es ist eine Umstellung und keine reine
Einfuegung, deshalb steht sie hier.

---

### Band 1: die Ton-Etiketten, und der Befund ist, dass Band 1 nicht das Problem war

**Zweiunddreissig reine Ton-Etiketten entfernt** aus einundzwanzig Kapiteln,
dazu eine doppelte Formel in b1 K18.

**Meldung 1 - gestrichene Beats.** Alle zweiunddreissig sind **Zusammenlegungen
zweier Redeteile**, kein Sprecherwechsel wird dadurch unklar - der Sprecher
steht in beiden Faellen im selben Absatz:

> vorher: *"I'm what it costs." He said it without any particular weight on it.
> "There's nothing else of mine anywhere in the world."*
> jetzt: *"I'm what it costs. There's nothing else of mine anywhere in the
> world."*

Zwei standen als **eigener Absatz** und sind ganz gefallen (b1 K26 *"He said it
without a single softening word in it anywhere."*, b1 K18 der doppelte).

**Meldung 2, 3 und 4:** keine. **Gegenprobe `faktenspur.py`:** sieben Kapitel,
und jede Meldung ist derselbe Posten - `Georgij` um eins oder zwei niedriger,
weil in den gestrichenen Beats sein Name stand.

**Was geblieben ist und warum.** Von 102 Stellen trugen 29 von sich aus etwas.
Von den uebrigen sind rund fuenfzehn ebenfalls stehengeblieben, weil sie nicht
den Ton angeben, sondern etwas anderes:

| bleibt | weil |
|---|---|
| *He said it kindly.* (b1 K02, nach dem Auge auf dem Kies) | Gegenueberstellung, und sie ist das Grauen |
| *He said it courteously.* (b1 K01) | Rueckgriff - sie hat ihm die Hoeflichkeit gerade verboten |
| *He said it immediately.* (b1 K18) | Tempo, und die Schnelligkeit ist die Antwort |
| *He said it to the water.* (b1 K24) | Richtung |
| *She said it again.* (b1 K24) | Wiederholung |
| *She said it to Annie and not to him.* (b1 K15) | Adressat |
| *She said it flatly and it was not flat underneath.* (b1 K31) | die zweite Haelfte |
| *She said it kindly. She was going to be kind about it for the rest of her life, and it was going to cost him every time.* (b1 K09) | der Satz danach |

**Kein einziger Beat wurde erfunden.**

**Stand:** Band 1 **69** Ton-Beats, 2,0 je Kapitel, **0,68 je 1000 Woerter**;
Band 2 **140**, 2,0 je Kapitel, 0,81. Erstmals gleichauf, und Band 1 ist die
duennere Haelfte.

#### Und der eigentliche Befund, der nicht Band 1 betrifft

| | Band 1 (34 Kap.) | Band 2 (70 Kap.) |
|---|---|---|
| *did not soften* | 5 | **12** |
| *did not look away* | 6 | **10** |
| *without any … in it at all* | **1** | **9** |

**In Band 2 stehen sie geballt in den neuesten Kapiteln: K67 bis K70 tragen
allein dreizehn der zweiundzwanzig.** *did not look away* steht achtmal in
diesen vier Kapiteln.

**Die Formel wird gerade neu angelegt, waehrend in `doc/09` steht, dass sie
abgebaut wird.** Das gehoert der Schreibsitzung, nicht dem Stil-Durchgang, und
es ist der Grund, warum Punkt 5 dort jetzt mit der Zahl statt mit einer Absicht
steht: **ein Posten, der nach jedem Durchgang wieder auflaeuft, ist keine
Aufraeumarbeit, sondern eine Gewohnheit beim Schreiben.**

---

### Fuenf Sprecher hatten kein Blatt, und die Ursache war ein Werkzeug

Frage des Autors: *"Haben wir alle Charaktere und ihre Sprecharten?"* **Nein.**

| fehlte | Repliken | wo |
|---|---|---|
| **Nam Byung-hee** | 10 | b2 K08, K11, K19 - **die Gegenspielerin des halben Bandes 2** |
| **Baek Jun-ho** | 14 | b2 K50, eine ganze Szene |
| **Kim Sung-ho** | 3 | b1 K26, K32 - der Vorsitzende der Familie |
| **Mr Ok** | 4 | b2 K17 |
| **Mr Ku** | 2 | b2 K14 |

**Die Ursache ist keine Nachlaessigkeit, sondern eine Kette:** `stimmen.py`
fuehrt in `FIGUREN` eine Namensliste. Wer dort fehlt, wird nicht zugeordnet -
also nicht gemessen - also steht er in keinem Index - also schreibt niemand ein
Blatt. **Nam Byung-hee war fuer das Werkzeug stumm, obwohl sie dreizehn Kapitel
lang die Handlung traegt.**

Ausserdem fehlten **Mrs Sunwoo** und **Shin**, die zwar ein Blatt hatten, aber
nie gemessen worden sind - deshalb stand in Mrs Sunwoos Ueberschrift eine Zahl
aus dem Index statt aus der Messung.

**Die Liste ist ergaenzt** (Nam Byung-hee, Baek, Ok, Shin, Sunwoo, Eun-ju, Yeo,
Uhm, Heo) und im Kopfkommentar steht jetzt, was passiert, wenn jemand fehlt.
`stimmen.py` zaehlt danach **30 Sprecher mit mindestens zwei Repliken**.

#### Und der dritte falsche Superlativ aus derselben Ursache

Jangs Blatt sagte *"der langsatzigste Sprecher des Buchs"*. Am 25.08. korrigiert
zu *"Hwang 11,9, Jang 11,2, Mittelfeld"*. **Auch das war falsch:** mit der
ergaenzten Liste misst **Baek Jun-ho 15,7 Woerter je Satz und 18 Prozent ueber
25 - beides der hoechste Wert im Buch**, mit grossem Abstand.

**Dreimal hat dieselbe Luecke einen falschen Superlativ erzeugt** (Jang zweimal,
Mrs Sunwoos Replikenzahl einmal). Eine Messung ist nur so gut wie die Liste, auf
der sie laeuft, und **die Liste stand nirgends unter Verdacht, weil sie im Code
steht und nicht im Dokument.**

#### Nebenher aufgeraeumt: zwei Dateien hiessen doc/13

Die Pruefsitzung hat `doc/13-zusagen.md` angelegt und in `CLAUDE.md` eingetragen,
waehrend dieses Blatt schon unter derselben Nummer lief (13-stilprotokoll). **Umbenannt in
`doc/14-stilprotokoll.md`**, Verweise in `doc/09` nachgezogen. `doc/13` gehoert
jetzt eindeutig dem Schuldbuch.

---

### Die fuenf neuen Blaetter gegengelesen, und wer sonst noch fehlt

**Auftrag: die fuenf wie die anderen pruefen, und nachsehen, ob jemand fehlt.**

#### Sechs Fehler in fuenf frisch geschriebenen Blaettern

| Blatt | stand da | Befund |
|---|---|---|
| **Nam Byung-hee** | *"Ihr erstes Wort ist **immer** die Zaehlung"* | In b2 K08, beim **ersten** Treffen, sagt sie *"You are not from here."* und *"Say your name."* Die Zaehlung faengt erst an, nachdem sie weiss, wer er ist - **ein Bogen, kein Tic** |
| Nam Byung-hee | *"eine der saubersten Stimmen im Buch"* | sagt wenig: **dreizehn von dreissig** Sprechern haben keinen Haustic. Ersetzt durch das, was belegbar ist - der Erzaehler in b2 K08: *"without any self-pity in it at all, which made it worse"* |
| **Baek Jun-ho** | *"mit Abstand vor Hwang (11,9)"* | zweiter ist **Mr Chae mit 12,4** |
| Baek Jun-ho | Jahre 22,5, *"ebenfalls der hoechste Wert"* | zweiter hinter Ye-rin (41,7 aus 24 Woertern). Hoechster **ab 90 Woertern** - Schwelle ergaenzt |
| **Kim Sung-ho** | *"Drei Repliken, und alle drei sind Anweisungen"* | **Fuenf**, und *"You work for the woman."* ist keine Anweisung. Eine Zeile in K26 gehoert **Georgij** und stand nur neben Sung-hos Namen |
| **Mr Ku** | *"Zwei Repliken, und beide sind Ereignisse"* | **eine**. Die zweite Fundstelle ist Erzaehlung - und die ist der eigentliche Auftritt, weil **nicht dasteht, was er gesagt hat** |
| **Mr Ok** | *"die vollstaendigste Personenbeschreibung im Buch"* | unbelegbarer Superlativ. Jetzt: die Beschreibung, aus der Georgij in b2 K18 die neun Zeilen zieht |

**Dabei ist Sung-hos Maschine erst sichtbar geworden.** Er urteilt ueber das, was
gerade passiert ist, und haengt eine Anweisung an, beides in einem Atemzug:
*"It was fair and he answered it." Sung-ho had not raised his voice. "Now sit
still."* Und er gibt Georgij am Ende von b1 K32 die Hand und haelt sie eine
Sekunde zu lang - **der Gegensatz zu Woo, der in beiden Baenden keine einzige
schuettelt.**

#### Fehlt sonst jemand: drei, und keiner braucht ein Stimmblatt

Ueber alle Namensformen im Buch geprueft, nicht nur ueber Begleitsaetze.

**Minister Min-ho (b1 K09) spricht nie**, und der Erzaehler sagt, dass das die
Figur ist: *"Min-ho said almost nothing. He asked two questions, both short."*
**Die zwei Fragen werden genannt und nicht wiedergegeben.** Vier Minuten, die das
Kapitel tragen, ohne ein Zitat. Eingetragen neben Choi Dae-ho, damit ihm niemand
versehentlich eine Replik gibt.

**Mrs Ryu (b1 K07)** antwortet nur in indirekter Rede. **Zehn weitere Namen**
werden genannt und sprechen nie - Mr Noh, Chef Bang Seung-min, Mrs Uhm, Miss Heo,
Mr Han, Min-a, Hyun-woo, Hye-jin, Mr Tak, Jae-sung. Alle aufgelistet, damit die
Liste beim naechsten Mal nicht wieder von vorn erarbeitet wird.

**Und zwei Namen sind keine zweiten Personen:** *Do Kyung-ae* ist Ahn Jung-hees
Deckname, *Moon Hae-sook* die Frau am Fenster.

#### Die neuen Kapitel

Band 2 steht inzwischen bei **K74**. In K69 bis K74 sprechen Ahn, Mrs Jeon,
Mr Kwon und Sim - **alle vier haben ein Blatt. Kein neuer Sprecher ohne
Eintrag.**

---

### Min-ho und Mrs Ryu gegengelesen: drei Fehler, und einer verdeckte den Beat

**Min-ho, geprueft ueber alle zehn Fundstellen** (b1 K09, K11, K12, K15).
**Null Zitate bestaetigt** - in keiner einzigen steht ein Wort von ihm in
Anfuehrungszeichen.

| stand da | Befund |
|---|---|
| das Zitat endete bei *"it cost him nothing to agree."* | **Der Satz geht weiter und endet besser:** *"…and he did not repeat it."* Ein Maechtiger, der einmal zustimmt und es nicht wiederholt |
| *"ein Mann, dessen Anwesenheit ein Kapitel traegt"* | **Zu gross.** Er traegt **vier Minuten** eines Kapitels, das Hana gehoert. Was zaehlt: die vier Minuten wirken in drei Kapiteln nach - b1 K15 zweimal, *"you were standing at my elbow being enchanting at a minister"* - **ohne dass er je zitiert wird** |

**Mrs Ryu: eine einzige Fundstelle im ganzen Buch**, b1 K07 Z166. Der Eintrag
sagte, sie antworte in indirekter Rede. **Das stimmt und es ist nicht der
Punkt** - und der Punkt stand zwei Zeilen weiter, ungelesen:

> *"Her face did not change very much. But **she talked to him for six minutes,
> and she was not a woman who gave six minutes**."*

**Ihre Figur ist eine Dauer.** Der ganze Wortwechsel wird zusammengefasst statt
zitiert, und das Ergebnis steht als **Zahl** da und nicht als Satz. Wer ihr eine
Replik gibt, muss die sechs Minuten aufgeben, und die sechs Minuten sind das
Einzige, was sie ist.

**Die Lehre, und sie gilt fuer alle drei Stummen:** bei einer Figur ohne Replik
steht ihr Blatt nicht in dem, was sie sagt, sondern in dem, was der Erzaehler
ueber sie **misst** - zwei Fragen, vier Minuten, sechs Minuten. **Wer nur nach
Anfuehrungszeichen sucht, findet bei ihnen nichts und schreibt deshalb nichts
auf.**

### Choi Dae-ho gegengelesen - vier Fehler, einer davon umgedreht

**Die Kernaussage haelt:** null Repliken, nachgezaehlt ueber alle 108 Kapitel
bei 22 Fundstellen auf seinen Namen. Der Eintrag sagte *"achtundneunzig
Kapitel"* - das Buch ist seither um zehn gewachsen.

| stand da | Befund |
|---|---|
| *"ausgerichtet von Sim und von **Yeom**"* | **Yeom steht auf der falschen Seite des Satzes, und das Buch berichtigt es selbst.** Georgij, b2 K38: *"That puts him **on the end of the sentence, not the one saying it**."* Yeom ist Empfaenger |
| *"viermal belegt"* | Die vier in b2 K53 sind **Empfaenger einer Methode**, nicht Belege einer Stimme. Belegt ist die Zeile in **zwei Muendern**: Choi selbst bei Mr Oks Mittagessen (b2 K17/K18), Sim bei Mrs Gwak, Yeom und Mrs Ha |
| *"Er stellt **genau eine** Frage"* | **Falsch.** Allein in Mr Oks Bericht vier: Ulsan-Kueste, die kleinen Betreiber, einer davon namentlich, die Kataloge. Singulaer an Woos Frage ist etwas anderes - sie fragt **nicht nach einem Geschaeft, sondern nach einer Verbindung**, und Woo sagt genau das: *"Not who I had told. Not who knew. Who I would telephone."* |
| *"**er isst nichts**"* | **Das Gegenteil dessen, was im Buch steht.** Annie, b2 K18: *"He eats a great deal, and he enjoys it, and he does it at his own table and nowhere else. **He does not eat in front of people he is working on.**"* |

**Der letzte ist der teuerste.** Ein Mann, der nichts isst, ist eine Marotte.
Ein Mann, der viel isst und ausgerechnet dann nicht, wenn er arbeitet, ist eine
**Landkarte** - Georgij benutzt sie in b2 K42 und K62, um zu bestimmen, wo Choi
gearbeitet hat. Wer dem alten Eintrag folgt, schreibt die Marotte und nimmt dem
Buch den Hebel.

**Und der zweite ist die Falle fuers Schreiben:** wer Choi endlich sprechen
laesst, muss wissen, dass *"It has been good to see you again"* **seine
Erfindung und Sims Werkzeug** ist. Beide benutzen sie, und wer das verwechselt,
gibt Choi eine Zeile, die im Buch fast immer ein anderer sagt.

*Unsicher:* keiner.

### Sim gegengelesen - eine neue Fehlerklasse: das Blatt hat aufgehoert zu lesen

**Alles Zitierte haelt.** *"Tips the room and not the person"* (b2 K41),
*"Says it is good to see people he has never met"* (b2 K31), Umschlag ohne
Quittung (K41, dann aus seinem eigenen Mund in K52), die falsche Tram-Nummer
mit Absicht (K52, und in K72 erklaert er sie selbst). Nichts erfunden.

**Und trotzdem ist das Blatt falsch, auf eine Art, die bei Choi nicht vorkam.**

| | |
|---|---|
| **Das Blatt zitiert** | b2 K31 und K41 |
| **Sim hat** | **65 Repliken - 64 davon in K52, K64, K68, K72, K74** |

Der Schlusssatz des Blattes lautete: *"Im schlimmsten Moment macht er den
Gastgeber weiter. Sein Bruch ist nicht Kaelte, sondern dass die Waerme
weiterlaeuft, wenn sie nichts mehr zu tun hat."* **Bis K41 stimmt das. In K52
tut das Buch das Gegenteil und markiert es ausdruecklich als den ersten Mal:**

> *"Do not do that." **It came out of him at last, and it was not loud, and it
> was the first thing he had said all evening that had not been arranged.**"*

> *"They have looked identical for thirty years," said Sim. "**Tonight is the
> first evening they have not.**"*

**Die Figur ist die Reihenfolge:** automatisch (K41) → gebrochen (K52 Z204) →
benannt und gewaehlt (K52 Z290, *"I would like to do it once more this
evening"*) → aufgegeben (K68, *"I would rather have nothing than go on being
it"*). Wer dem alten Blatt folgt, schreibt ihm die Waerme als Panzer, den er
nie ablegt - **und das Buch hat ihn vor dreiundzwanzig Kapiteln ablegen
lassen.**

**Der Unterschied zu allen bisherigen Funden:** Chois Blatt war eine richtige
Beobachtung, einen Schritt zu weit geschrieben. Sims Blatt war **richtig, als
es geschrieben wurde, und das Buch ist weitergegangen**. Kein Satz darin war je
falsch. Es ist trotzdem unbrauchbar.

**Daraus folgt eine Pruefung, die auf jedes Blatt gehoert und auf keinem steht:**

```
python3 werkzeug/stimmen.py <Figur> | tail -1     # wie viele Repliken
python3 werkzeug/stimmen.py <Figur> | awk '{print $1,$2}' | sort | uniq -c
```

**Wenn die Mehrheit der Repliken in Kapiteln steht, die das Blatt nicht
zitiert, ist das Blatt veraltet** - unabhaengig davon, ob ein einziger Satz
darin falsch ist. Bei Sim: 64 von 65.

*Unsicher:* keiner.

### Die Liste abgearbeitet: Ahn, Hwang, Byun, Sohn, Chae, Mrs Jeon, Yeom

**Zuerst eine Berichtigung an meinem eigenen Test.** Der Veralterungs-Test aus
dem Sim-Eintrag sucht in doc/12 nach dem Muster `b1 K12`. **Er misst damit, ob
ein Blatt Kapitel *nennt*, nicht ob es sie *gelesen* hat.** Hwang und Yeom sind
dadurch faelschlich als 100 % bzw. 56 % unzitiert gemeldet worden - Hwang
zitiert seine Kapitel woertlich, nur ohne Nummer, und Yeom nennt sie in einer
Aufzaehlung (*"b2 K24, K25, K34"*), von der das Muster nur den ersten Eintrag
sieht. **Der Test taugt zur Triage und nicht als Befund.** Beide Blaetter haben
jetzt die Nummern.

| Figur | Befund |
|---|---|
| **Mr Ahn** | Alles belegt, auch das riskanteste: *"he is thirty-nine"* sagt Annie in b2 K74 woertlich. **Aber "zieht zusammen" ist zu klein**: 73,9 Kontraktionen je 1000 Woerter, naechstbester Hana mit 5,3 - **Faktor vierzehn, die staerkste Stimmenmarke im Buch.** Und die Werkbank-Geste ist keine Marotte in K56, sondern eine Geste ueber drei Kapitel mit einem Mass: Vierteldrehung (K56), vier Zentimeter (K63), vier Zentimeter (K73). K63/K70/K73 fehlten ganz |
| **Ahn Jung-hee** | **Der Abschnitt widersprach sich selbst.** Kopf: *"hat im ganzen Buch noch nie gesprochen"*; Fliesstext dreissig Zeilen tiefer: beide Auftritte. Der Kopf war nie nachgezogen worden, und die beiden Auftritte standen in verkehrter Reihenfolge. **Der Kern stimmt schaerfer formuliert: es gibt kein einziges direktes Zitat von ihr**, beide Male gibt Sim sie wieder. Ausserdem sagt das Buch nicht *"viermal wiederholt"*, sondern **"four times, in four different ways"** - sie wiederholt nicht, sie formuliert um |
| **Mr Hwang** | **Vorbildlich.** Jedes Zitat woertlich, der Superlativ haelt (Daten 16,3 / Uhrzeiten 13,6, beide Platz eins ueber der Schwelle), und das Blatt nennt die Schwelle von selbst. Nur die **Verfolgerliste** war nach drei Wochen falsch - Mr Ahn von 11,2 auf 7,9 gefallen. Rangliste durch den Befehl ersetzt |
| **Mr Byun** | **Der Rang ist zum zweiten Mal gekippt.** Erst *"hoechster Wert im Buch"*, dann berichtigt zu *"zweithoechster, knapp hinter Mr Ahn mit 22,5"* - und weil Ahn inzwischen auf 15,8 steht, ist die **verworfene erste Fassung wieder richtig**. Byuns eigene 22,0 haben sich nie bewegt. Rang raus, Befehl rein |
| **Mr Sohn** | **Ein zusammengezogenes Zitat.** Das Blatt fuehrte *"…a bill paid in cash by a man who left before the coffee"* als einen Satz. Es sind zwei Repliken, und die Fuge ist die Stelle, wo er aufhoert zu berichten und anfaengt zu urteilen: **"People do not do that."** Das Verschmelzen hat ihm seinen einzigen Meinungssatz genommen |
| **Mr Chae** | **Beide Zahlen im Blatt falsch** - Kopf *14*, Text *7*. Von Hand sind es rund **siebzehn**: sieben in b1 K25, zehn in b1 K34 |
| **Mrs Jeon** | **Das Blatt endete bei K32 und hat b2 K71 nicht gesehen - sechzehn Repliken, ihr groesstes Kapitel.** 25 Repliken standen da, es sind 41. Alles Zitierte stimmt |
| **Mr Yeom** | **Eine erfundene Zahl:** *"ein Verkaeufer, der seit vierzig Jahren Leute an Tischen sitzen sieht."* **Yeoms Berufsdauer wird im Buch nirgends genannt.** Sie klang richtig, in einem Blatt, das sonst jede Zahl belegt |

#### Ein Loch im Werkzeug, und es ist die Ursache von Chaes zwei falschen Zahlen

`stimmen.py` sucht `said|asked|shrugged|added|repeated`. **Eine Replik mit
einem Handlungs-Begleitsatz ist unsichtbar:**

> *"That is what it was for." **Mr Chae closed the case** and did not open it
> again.*

In b1 K34 verliert Chae dadurch zehn Repliken. **Die Verbliste zu erweitern
hilft nicht** - ein Handlungsverb neben einer Replik sagt nicht, dass der
Handelnde spricht. Es gilt dasselbe wie bei Zweipersonenszenen: lesen, nicht
zaehlen. **Als dritte Grenze in `werkzeug/stimmen.py` dokumentiert**, neben der
Zuschreibungsfalle und den Zweipersonenszenen.

#### Was diese sieben zusammen zeigen

**Die haltbarsten Saetze sind die, die das Buch selbst formuliert** - *he is
never wrong about that by more than a year*, *he is thirty-nine*, *four times,
in four different ways*, *that puts him on the end of the sentence*. Kein
einziger davon ist beim Gegenlesen gefallen.

**Gefallen sind fast nur Zahlen, die einen Rang behaupten** - Byuns Platz
zweimal, Hwangs Verfolger, Chaes Repliken zweimal, Mrs Jeons 25, Yeoms vierzig
Jahre. **Ein Rang ist keine Eigenschaft der Figur, sondern eine Aussage ueber
alle anderen**, und die anderen aendern sich mit jedem geschriebenen Kapitel.
Deshalb steht in diesen Blaettern jetzt der Befehl, wo vorher die Ziffer stand.

*Unsicher:* Chaes siebzehn Repliken sind von Hand gezaehlt und nicht vom
Werkzeug bestaetigt - das Werkzeug kann es nicht. Bei einer Zweipersonenszene
haengt die Zuordnung am Wechsel, und wenn ich mich um eine Replik verzaehlt
habe, ist es diese.

## Durchgang: geschriebene Rede gegen die Stimmblaetter

**Auftrag, wie ich ihn verstanden habe:** nicht die Blaetter am Text pruefen
(das war der Lauf davor), sondern **den geschriebenen Text an den Blaettern** -
jede schon geschriebene Replik soll so klingen, wie doc/12 die Figur beschreibt.
Vereinbart: Messbares und ausdruecklich Verbotenes ziehe ich still nach, alles
Inhaltliche wird gemeldet. Reihenfolge: Nebenfiguren zuerst.

### Das Ergebnis zuerst, weil es kurz ist

**Kein einziges der ausdruecklichen Verbote wird im geschriebenen Text
gebrochen.** Geprueft gegen ihr eigenes Blatt: Jang, Mrs Seo, Mrs Bae, Hwang,
Sang-hoon, Hana, Ye-rin, Nam Byung-hee, Baek, Sung-ho, Byun, Koh, Kwon, Mrs Ha,
Mrs Gwak, Kang, Hong, Sunwoo, Chae, Sohn, Woo.

| Verbot | geprueft | Befund |
|---|---|---|
| Hwang: kein which-Satz, keine Und-Kette | 24 Repliken | **null** |
| Hana: keine Negativ-Def, kein which, keine Selbstdiagnose | 63 | **null von dreien** |
| Sang-hoon: keine Selbstdiagnose | 116 | **null** |
| Ye-rin: keine Kontraktion, kein which, keine Und-Kette | 5 + ungetaggt | **null** |
| Nam Byung-hee, Baek: keine Kontraktionen, keine Tics | 10 / 14 | **null** |
| Koh: kein which-Satz | 7 | **null** - die vier which-Saetze in K37 gehoeren dem **Erzaehler**, nicht ihm |
| Mrs Seo: keine Negativ-Definition | 13 | **null**. Ihr which-Satz *"which she does not do"* ist von ihrem Blatt ausdruecklich erlaubt |
| Byun: keine Moral ohne Erbfolge | 11 | haelt. *"Nobody was hurt"* steht nackt und wird nicht ausgebaut |
| Sung-ho: begruendet nicht | 3 | haelt |
| Kwon: Negativ-Definition | 18 | **erlaubt** - *"Er stellt fest, wann etwas nicht passiert ist"* ist laut Blatt seine Maschine |
| Jang: Kontraktionen | 40 | die drei im Buch stehen alle im Kies-Wechsel b1 K05, wie das Blatt sagt |

**Damit ist an keiner geschriebenen Replik etwas zu aendern gewesen.** Die
Abweichungen sitzen alle auf der anderen Seite - in der Buchhaltung der
Blaetter.

### Was dabei doch zu berichtigen war

| Ort | Befund |
|---|---|
| **`stimmen.py`, which-Zaehler** | Das Muster war `,\s*which (is\|was\|means\|...)` und **hat genau die Beispiele nicht gefunden, die doc/12 als Beleg zitiert** - Mrs Seos *"which she does not do"*, Chaes *"which I did not enquire into"*. Beide standen mit "keine Tics" in der Tabelle, waehrend ihr Blatt den Tic als ihre Maschine zitiert. Verbreitert auf jeden nachgestellten which-Satz |
| **Park Sang-hoon** | *"3,3 je 1000 Woertern, die hoechste Rate im Buch, zehnmal Georgijs 0,3"* - **falsch, und doc/12 widerlegt sich selbst**: wenige Abschnitte weiter steht Byuns 5,5 als "hoechster Wert im Buch". Breit gemessen: Chae 8,9 · Mrs Seo 8,8 · Byun 5,5 · Ahn 2,6 · Sang-hoon 2,2 · Georgij 0,7. Haltbar ist: **der hoechste unter den Vielrednern** |
| **Mr Kwon** | Kopf sagte 14 Repliken, es sind **18** (b2 K69 ist dazugekommen) |
| **Mr Hong** | Kopf sagte 10 Repliken, zugeordnet sind **7** |
| **Tic-Tabelle** | Als **Momentaufnahme vom 25.08.** gekennzeichnet. Sie haelt fest, was berichtigt wurde; die Werte selbst wandern (Ahn 72,1 → 73,9, Annie 3,5 → 2,9) |

### Zwei Sachfragen an den Inhalts-Chat, nicht von mir zu entscheiden

1. **b2 K34** benutzt dieselbe Wendung zweimal mit verschiedenem Bezug:
   *"…two people who had never met Choi Dae-ho in their lives"* (die
   **Empfaenger**) und vierzig Zeilen weiter *"Two people, four years and one
   telephone number apart, **who each told** a stranger…"* (die **Sprecher**).
   Der zweite Absatz ist Georgijs Zerlegung bei halbem Wissen und darf das -
   aber die gleiche Formel mit gedrehtem Bezug ist eine Stolperstelle.
2. **Mr Byun** hat mit 5,5 den zweithoechsten which-Wert unter den
   Nebenfiguren, und **sein Blatt erwaehnt den Tic mit keinem Wort.** Entweder
   gehoert er ihm (dann ins Blatt) oder nicht (dann ist es ein Eingriff in
   Inhalt und Haltung, den ich nicht allein mache).

*Unsicher:* Mrs Bae hat nur drei zugeordnete Repliken; ihr Auftritt in b2 K10
laeuft als Zweipersonenszene ohne Begleitsaetze. Ihr Verbot (sich
rechtfertigen, um Verstaendnis bitten, Gefuehlswort) haelt in dem, was
zugeordnet ist - die ungetaggten Zeilen habe ich gelesen und nichts gefunden,
aber gezaehlt ist es nicht.

### Der Durchgang fortgesetzt: alle uebrigen Figuren

Georgij und Annie sind vom Autor freigegeben. Geprueft wurden alle anderen -
Blatt-Maschine gegen die tatsaechlichen Repliken, nicht nur die Verbote.

#### Der eine Textbefund, und er ist eine Entscheidung des Autors

**Dieselbe Wechselrede steht zweimal, als Echo ueber die Bandgrenze, und sie ist
nicht identisch:**

| | |
|---|---|
| b1 K13 | *"Thank you, Chairman." / "**Don't** thank me. I have not given you a name."* |
| b2 K57 | *"Thank you, Chairman." / "**Do not** thank me. I have not given you a name."* |

Gleicher Stichsatz, gleiche Antwort, **eine Kontraktion Unterschied**. Beide
Lesarten sind vertretbar: b1 K13 ist Woos einziges Kapitel mit Kontraktionen
(drei Stueck, alle dort), in b2 K57 zieht er kein einziges Mal zusammen - das
kann Register sein oder Versehen. **Ein wiederholter Satz ist keine Marotte,
darum nicht angefasst.** Entscheidung liegt beim Autor.

#### Zwei Stellen, an denen die mechanische Regel Schaden angerichtet haette

**1. Woos Negativdefinition in b2 K57 muss stehen bleiben.** Sein Blatt sagt
"gehoert ihm nicht", zwei Stellen wurden ersetzt - und die Messung zeigt noch
0,9. Das ist kein Rueckfall:

> *"He asked me who I would telephone if it went badly." **Woo said it exactly,
> in the way of a man repeating something he has repeated to himself.** "Not who
> I had told. Not who knew. Who I would telephone."*

**Das ist Choi Dae-hos Frage in Woos Mund**, und der Begleitsatz sagt es. Wer
die Regel mechanisch anwendet, loescht die einzige belegte Frage Chois, die
nicht nach einem Geschaeft fragt. Als Ausnahme ins Blatt geschrieben.

**2. Sang-hoons Und-Kette.** Sein Blatt sagte oben *"Verboten: die Und-Kette"*
und drei Absaetze weiter *"Er darf: die Und-Kette - er sortiert damit Beweise"*.
**Der Text gibt der zweiten Fassung recht.** Er hat genau zwei im Buch, und
beide tun dasselbe: drei Sachen aufzaehlen und dann den Augenblick datieren, in
dem sie zusammenkamen (*"and I have never once put those three facts in a row
until this minute"*). Ein Durchgang nach der alten Regel haette beide
gestrichen - also die zwei Stellen, an denen der Mann merkt, was er acht Jahre
nicht gesehen hat. Verbot gestrichen.

#### Weitere Blattfehler, alle ohne Folgen im Text

| Ort | Befund |
|---|---|
| **doc/12, Eingangsdiagnose** | Das Beispiel fuer *"jede Figur endet in Georgijs Stimme"* zitiert **b2 K52 v1.0**. Der Kanon ist v1.4, und dort steht Sims eigenes Register: *"I was glad to. **I would like you to have heard me say that part.**"* **Die Stelle ist im Buch laengst repariert**; die Diagnose stand noch als offener Befund |
| **Sang-hoon** | Kopf sagte *101 Repliken, 26 Kapitel* - es sind **116 in 15**. Und das Protokoll-Zitat *"I would like it on the record that I gave you the chance"* **gibt es nicht**: es ist eine Zusammenfassung, als Zitat gesetzt. Die echte Zeile ist haerter, weil sie die Ablehnung mitprotokolliert - *"…that I gave it to you and that you did not."* |
| **Sang-hoon, zweite Kollision** | Die Protokoll-Formel gehoert ihm nicht allein: **Georgij benutzt sie ebenfalls zweimal** (b2 K40, b2 K41). Trennung: Sang-hoon protokolliert eine **gegebene Gelegenheit**, Georgij **sein eigenes Bemerken** |
| **Woo** | *"eine seiner zwei Kontraktionen"* - es sind **drei**, alle in b1 K13. `stimmen.py` sieht *"Don't thank me"* nicht, weil die Replik ohne Begleitsatz dasteht |
| **Anredeabschnitt** | *"Sang-hoon spricht in elf Kapiteln"* → **fuenfzehn** |

#### Was gehalten hat

**Woo schuettelt in beiden Baenden keine einzige Hand** - jede Fundstelle ist
seine eigene Hand auf Tisch, Stuhl oder Autodach. **Baeks Jahre-Dichte 22,5 ist
Platz eins** ueber der Schwelle. **Sung-ho stellt in seinen drei Repliken keine
Frage. Mr Ku hat genau eine. Koh hat keine Kontraktion. Jang hat keine
Und-Kette.** Hana zieht zusammen und zaehlt Menschen, wie ihr Blatt es
verlangt, und benutzt keine der drei ihr verbotenen Formen.

**Und der Zitatpruefer gibt fuer doc/12 null unbelegte Zitate.** Die vier aus
ueberholten Fassungen sind jetzt alle vier ausdruecklich als Geschichte
markiert.

**Moon Hae-sook und Mr Tak sprechen noch nicht** - ihre Blaetter sind vorab
geschrieben. Da ist nichts anzugleichen, solange keine Replik existiert.

*Unsicher:* keiner.

### Gedankenstriche: 69 ersetzt, und die Regel stand laengst da

**Gemessen vor dem Eingriff:**

| Ort | Treffer | |
|---|---|---|
| `chapters/`, `chapters-2/` | **0** | **Das Buch war sauber.** Kein einziger Gedankenstrich in 109 Kapiteln |
| `doc/*.md` | **69** | in acht Dateien |
| `erzeugt/` | 69 | dieselben, aus doc erzeugt |
| `paste/` | 1131 | **nicht angefasst** - das sind die 377 Szenentrenner, drei Geviertstriche, von `build.py` aus `* * *` erzeugt. Struktur, kein Satzzeichen |
| `werkzeug/belege.py` | 2 | **nicht angefasst** - Normalisierungstabelle, mit der der Zitatpruefer Striche aus fremden Zitaten raeumt. Wer sie ersetzt, macht den Pruefer blind |

**Die Regel gab es schon:** `doc/01-craft.md`, Abschnitt 5 - *"Keine
Gedankenstriche, nur Bindestriche."* Sie wurde im Buch eingehalten und in den
Dokumenten nie geprueft.

**Vor dem Ersetzen die Formen gezaehlt**, weil ein Strich, der an einem Wort
klebt, anders ersetzt werden muss als einer zwischen Leerzeichen:

| Form | Anzahl |
|---|---|
| ` - ` zwischen Leerzeichen | 48 |
| ` -` am Zeilenende | 18 |
| ` -,` vor Komma | 2 |
| in Backticks | 1 |

**Kein einziger Fall klebte an einem Wort**, also war der direkte Austausch
ueberall richtig.

**Eine Stelle war heikel und ist geprueft worden.** In `doc/13-zusagen.md` ist
der Strich kein Satzzeichen, sondern ein **Platzhalter im maschinenlesbaren
Format**: *"Eingeloest: das Kapitel, das sie bezahlt, oder `-`."* Die Felder
selbst trennt `zusagen.py` mit `·` und nicht mit einem Strich, und das Skript
enthaelt den Geviertstrich nirgends literal - das Feld ist frei. Ersetzt,
Definitionszeile mitgezogen, `zusagen.py` laeuft unveraendert (BEZAHLT 23).

**Damit es nicht wiederkommt:** `check.py` hat jetzt `striche_report()` und
meldet bei jedem Lauf jede Fundstelle in `doc/` mit Datei und Zeile. **Es
blockiert nicht** - ein Schreib-Durchgang soll nicht an einem Satzzeichen
haengenbleiben. Gegengeprueft mit einer Probedatei: meldet Geviert- und
Halbgeviertstrich, ignoriert den Bindestrich.

*Unsicher:* keiner.

**Ein eigener Fehler beim Push, und er gehoert hierher.** Beim Rebase kollidierte
`doc/10-naehe.md` - kein generiertes File, sondern ein Dokument der anderen
Sitzung. Mein `git add -A` hat den Konflikt **mitsamt den Markern** eingecheckt.
Sofort bemerkt und behoben: Inhalt der anderen Sitzung uebernommen, mein
Strichtausch darauf angewandt (`bb8dc90`).

**Die Lehre:** die Regel *"generierte Dateien nie von Hand aufloesen, `build.py`
laufen lassen"* verleitet dazu, im Rebase pauschal `git add -A` zu tippen. Das
ist nur fuer `erzeugt/` und `read/` richtig. **Bei jedem anderen Konflikt erst
`git status --short | grep '^UU'` lesen** - und wenn eine Datei dabei ist, die
niemand erzeugt, von Hand entscheiden, wessen Inhalt gilt.

## Takt und Szene: der Strich gehoert nur an den Szenenwechsel

**Der Autor am 25.08.:** ein Takt ist leerer Platz, ein Strich gehoert an den
vollstaendigen Szenenwechsel. **Der Quelltext war bereits richtig** - er
unterscheidet die beiden sauber. **Falsch waren die zwei Renderer**, und beide
haben aus dem Takt eine sichtbare Marke gemacht:

| Quelle | Lesefassung vorher | Einfuegefassung vorher | jetzt |
|---|---|---|---|
| `---` Takt | `· · ·`, drei zentrierte Punkte | `* * *` | **Weissraum, keine Marke** |
| `* * *` Szene | 1px-Linie | drei Geviertstriche | unveraendert |

**Das waren 579 Marken in Band 1 und 2972 in Band 2**, an jeder Stelle, an der
nur eine Atempause stehen sollte.

**Und die Abstufung stand auf dem Kopf.** Mit dem Ornament mass der Takt 6,0rem
und der vollstaendige Szenenwechsel 5,3rem - **der Beat riss weiter auf als der
Szenenwechsel.** Jetzt im Browser nachgemessen:

| | |
|---|---|
| Absatz | 18,4 px |
| **Takt** | **38,4 px** - reiner Weissraum, `height:0`, kein `::after` |
| **Szene** | **85,8 px** plus die 1px-Linie |

**Kein einziges Kapitel angefasst.** `faktenspur.py` meldet null bewegte Zahlen,
Daten und Namen; geaendert haben sich nur `werkzeug/reader.py`,
`werkzeug/build.py` und die daraus erzeugten Fassungen. **Das ist der ganze
Punkt: es war nie ein Textfehler, sondern zweimal dieselbe Entscheidung im
Werkzeug.**

**Sicherung gegen den Rueckfall.** `to_paste()` hatte in seinem Selbsttest eine
Ausnahme fuer `* * *`. Die war nach dieser Aenderung nicht nur tot - sie haette
eine wieder auftauchende Takt-Marke stillschweigend durchgelassen. Ausnahme
gestrichen: **faellt in der Einfuegefassung noch ein Sternchen an, bricht der
Build.** Gegengeprueft - eine echte Szene laeuft durch, eine verrutschte Marke
bricht.

*Unsicher:* keiner. Die Sache ist im Browser nachgemessen und nicht geschaetzt.

## Sim: Verhalten und Satzbau ausgearbeitet, nach dem Jang-Muster

**Der Autor am 26.08.: *"Sim klingt immer noch wie Georgij."* Er hat recht, und
mein Durchgang davor konnte das gar nicht finden.** Ich hatte geprueft, ob eine
Figur ein **ausdrueckliches Verbot** aus ihrem Blatt bricht. Sim hat in seinem
Blatt kein Verbot, und die Tic-Messung meldet bei ihm eine leere Zeile. **Er ist
durch den Test gefallen, ohne dass der Test etwas an ihm gemessen haette.**
"Kein Verstoss" hiess bei ihm nur "nichts zu pruefen".

### Der Nachweis

Gemessen wurde, welche Vier-Wort-Wendungen im ganzen Buch **nur Georgij und Sim**
benutzen und sonst niemand. Vier Treffer, alle in Sims neuesten Kapiteln:

| Georgij | Sim, geliehen |
|---|---|
| b2 K18 *"And there is a second half"* | b2 K74 *"There is a second half and you have not asked for it"* |
| b2 K21 *"There is one more thing and it is not an argument"* | b2 K72 *"There is one more thing and it is mine and not hers"* |
| b2 K19 *"neither of them is a comfort"* | b2 K72 *"two voices … and neither of them was his"* |
| b2 K19 *"he is not the one who wrote the letter"* | b2 K64 *"a question and it is not the one you are braced for"* |

**Drei der vier eroeffnen einen Takt und werden mit *"Go on."* beantwortet.**
Das ist der Rhythmus eines Mannes, der Auskunft dosiert - und **Sim dosiert
nicht**, das ist seine ganze Figur.

**Dieselbe Diagnose steht seit dem 25.08. im Musterfall dieses Dokuments**, ueber
die Frau mit der Giesskanne: *"Das ist Georgijs Maschine mit Blumentoepfen
darin."* Bei Sim war es Georgijs Maschine mit einem Blumenstrauss in der Hand.

### Die Maschine, die dort haette stehen muessen

**Er richtet dem anderen die Bequemlichkeit im Voraus ein, ungefragt, und
benennt die Einrichtung dann laut - damit sie keine Schuld wird.**

> *"It is a box in Jongno and it is raining on me, and I have put in more than I
> need, so do not talk quickly on my account."* (K72)
> *"I gave her three places to. … She did not take one of them."* (K72)

Er zaehlt **die Ausgaenge, die er anderen gebaut hat**, nicht Jahre und nicht
Daten. Sein Blatt hat jetzt Maschine, Anliegen, Georgij-Abgrenzung, Koerper,
Wie-mit-wem, warm, unter Druck, vier Beispiele und eine Probe - nach dem Muster
von Jang.

### Die vier Zeilen im Text

| Kapitel | vorher | jetzt |
|---|---|---|
| b2 K64 v1.6 | *"I have a question and it is not the one you are braced for"* | *"You have been getting ready for a different question"* |
| b2 K64 v1.6 | *"There is one more thing," … "and you will not like it."* | *"You will not like the last of it," … "and I am going to give it to you anyway."* |
| b2 K72 v1.1 | *"…two voices on that telephone and neither of them was his"* | *"…that telephone has had two voices on it, and I had not heard this one before"* |
| b2 K72 v1.1 | *"There is one more thing and it is mine and not hers"* | *"What is left is mine and not hers"* |
| b2 K74 v1.2 | *"There is a second half and you have not asked for it"* | *"You have not asked me for the rest of it"* |

*"you have not asked"* bleibt ueberall stehen. Bei Georgij markiert es, dass er
etwas **hat**; bei Sim, dass er wartet, geben zu duerfen. Gleicher Wortlaut,
umgekehrter Zug.

### Ein Beinahe-Schaden, und er gehoert protokolliert

Meine erste Fassung fuer K72 lautete *"This was a third."* **`faktenspur.py` hat
`third 2 -> 3` gemeldet, und die Meldung war kein Rauschen.** In demselben
Kapitel, achtzig Zeilen spaeter, ist *"the third"* die **dritte Nachricht von
Ahn Jung-hee**, und Georgij leitet ihre Existenz daraus ab, dass Sim sie noch
nicht gesagt hat:

> *"And the third." / "Say why you think there is a third." / "Because you have
> not said it yet and you have said everything else in the order it happened."*

Eine zweite, konkurrierende Dritte davor haette die Ableitung stumpf gemacht.
Zurueckgenommen; K72 bewegt jetzt **keine einzige Zahl**. **Die Lehre: ein
Stiltausch, der ein Zahlwort einfuehrt, ist kein Stiltausch.**

Die zwei verbliebenen Meldungen sind geprueft und harmlos: in K64 fallen zwei
*one* weg, beide Pronomen bzw. Mengenwort; in K74 fallen *second* und *half*
zusammen mit dem geliehenen Rahmen weg, und es gibt im Kapitel keine
Rueckbindung darauf.

*Unsicher:* keiner.

### Nachtrag: der Rahmen kommt von selbst zurueck, und ich habe ihn selbst einmal ersetzt

**Zwei Dinge in der Gegenprobe nach dem Eingriff.**

**1. Kapitel 77 ist waehrend der Arbeit dazugekommen, und es steht schon wieder
drin:** *"There is a last thing and it is not information," said Sim.* /
*"Go on."* - derselbe Rahmen wie Georgijs *"There is one more thing and it is
not an argument"* (b2 K21). **Das ist kein Aufraeumen, das ist eine Sperre, die
gefehlt hat**; sie steht jetzt in Sims Blatt. Berichtigt zu *"The last of it is
not information."* (ch77 v1.1)

**2. Meine eigene Ersetzung war die naechste Anleihe.** Fuer K72 hatte ich
*"What is left is mine and not hers"* geschrieben - und **`what is left is` ist
Georgijs Wendung**, zweimal belegt (b1 K28, b2 K10). Ich habe einen
Georgij-Rahmen gegen einen anderen getauscht und es erst in der Gegenprobe
gesehen. Berichtigt zu *"The next part is mine and not hers."* (ch72 v1.2)

**Die Lehre, und sie gilt fuer jede weitere Figur:** nach einem Stiltausch wird
die Messung **noch einmal** gefahren, gegen die neue Fassung. Ein Ersatz, der
aus demselben Kopf kommt wie das Problem, ist wahrscheinlich dasselbe Problem.

**Stand jetzt:** von vier geliehenen Wendungen ist **eine** uebrig,
*"it to you because"* - und die steht in einer Zeile, die ich nicht angefasst
habe (*"I am going to give it to you, because I have spent two days working out
why it has been sitting on me"*, K74). Der Wortlaut ist geteilt, der Zug nicht:
Georgij gibt her, was **schlimmer** ist, Sim gibt her, was er **schuldet**.
Bleibt stehen. `faktenspur.py` meldet **null** bewegte Zahlen, Daten und Namen.

### Nachgefragt: war es distinktiv genug? Nein, und die Probe hat es gezeigt

**Der Autor am 26.08.: *"ist das immer schon distinktiv genug, was Du gemacht
hast?"*** Ich habe die Probe, die ich fuer Sims Blatt geschrieben hatte, gegen
**meine eigenen Berichtigungen** laufen lassen. Ergebnis im ersten Anlauf:

| Ort | meine Zeile | Sim-Marker |
|---|---|---|
| K64 | *"You have been getting ready for a different question"* | Zustand des anderen |
| K64 | *"…and I am going to give it to you anyway"* | benennt die Gabe |
| K72 | *"…that telephone has had two voices on it, and I had not heard this one before"* | **KEINER** |
| K72 | *"The next part is mine and not hers"* | **KEINER** |
| K74 | *"You have not asked me for the rest of it"* | wartet zu geben |

**Zwei von fuenf trugen nichts.** Ich hatte Georgij herausgenommen und nichts
von Sim hineingesetzt - neutral statt geliehen, und neutral ist keine Stimme.
**Georgij herausnehmen ist die halbe Arbeit**; dieser Satz steht jetzt in der
Probe auf seinem Blatt.

**Nachgebessert, und diesmal die Kandidaten vorher gemessen statt hinterher:**

| Ort | jetzt | Marker |
|---|---|---|
| K72 | *"You will want the voice before anything else"* | Zustand des anderen |
| K72 | *"…and I have thought about whether to bring it"* | Einrichtung vorher |
| K77 | *"The last of it is not information. I am telling you anyway"* | benennt die Gabe |

**6 von 6 tragen jetzt einen im Text belegten Marker.** Geteilt mit Georgij ist
noch **eine** Wendung, *"it to you because"* - und die steht in einer Zeile, die
ich nicht geschrieben habe.

**Zwei Lehren fuer die uebrigen Figuren.**

1. **Der Vorab-Test.** Ein Ersatzsatz wird gegen den Korpus gemessen, **bevor**
   er ins Kapitel geht: welche seiner Vier-Wort-Wendungen benutzt Georgij und
   sonst niemand. Mein erster Ersatz *"What is left is mine and not hers"* war
   selbst Georgij, mein zweiter brachte *"and you will not"* zurueck. Beide
   haette der Vorab-Test gestoppt.
2. **Die grobe Messung taugt nicht.** Gegen Georgijs 13 000 Woerter trifft fast
   jede gaengige Wortfolge. Gezaehlt wird nur, was **Georgij benutzt und sonst
   kein Sprecher** - das ist das Signal, alles andere ist Englisch.

*Unsicher:* keiner. Die Marker sind alle am Text belegt und stehen als Tabelle
auf Sims Blatt.

## Der Methodenfehler: ich habe nur auf Abwesenheit geprueft

**Der Autor am 26.08.: *"du konzentrierst Dich bei den Markern zu sehr auf
Abwesenheit und uebersiehst mangelnde Anwesenheit von Charakterzuegen."*** Das
ist der Fehler unter allen anderen. Jede Pruefung in diesem Protokoll fragt
bisher: **steht hier etwas Fremdes** - ein gebrochenes Verbot, eine geliehene
Wendung, ein Tic, der nicht ihrer ist. **Keine davon kann melden, dass ein
eigener Zug fehlt.** Deshalb konnte Sim bei mir "sauber" sein und trotzdem
falsch klingen.

### Was die Anwesenheitspruefung sofort findet

**In 71 zugeordneten Repliken stellt Sim keine einzige Frage.** Weder mit
Zeichen noch in Fragesyntax mit Punkt, wie das Buch sie sonst schreibt. Fragen
je 100 Repliken:

| | |
|---|---|
| Koh, Hong, Mr Chae | 14,3 |
| Mrs Ha, Mr Sohn | 12,5 |
| Woo, Mr Ahn | 5,7 |
| Annie 4,9 · Georgij 4,0 | |
| **Sim** | **0,0** |

**Der Mann, dessen Methode das Fragen ist, steht als Einziger bei null.**

### Und die Hoeflichkeit ist da - aber nicht in seinem Mund

| Stelle | Form |
|---|---|
| K52 *"He had asked her about the walk from the station…"* | **Erzaehlung** |
| K52 *"About the heating. About whether the second bathroom was worth doing."* | **sein Bericht** |
| K72 *"I told her the weather might turn. I told her the gutters."* | **sein Bericht** |
| K77 *"…he hoped somebody in that building owned a chair."* | **indirekte Rede** |

**Lebendig, an den Anwesenden gerichtet und konkret ist es genau zweimal:** die
Suppe in K52 (*"I have ordered it for both of us and you are under no obligation
to touch it"*) und die Telefonzelle in K72 (*"I have put in more than I need, so
do not talk quickly on my account"*). Dazu der Tee in K64, den der Erzaehler
mittraegt: *"it was at the right temperature, which meant he had timed it."*

**In der lebendigen Rede diagnostiziert er stattdessen** - *"You have not
slept." "You will not want these." "You have come with something."* Das ist
nicht falsch, aber es ist **Georgijs Haltung**, und meine Berichtigungen haben
sie noch verstaerkt. Ich habe eine Messgroesse optimiert und die Figur verloren.

### Was daraus folgt

**Sims Blatt hat jetzt eine Anwesenheitsprobe:** eine Sim-Szene, in der er nicht
mindestens einmal nach einer konkreten Sache fragt oder eine anbietet, ist keine
Sim-Szene. Konkret heisst der Koerper und die Umstaende des anderen, nicht sein
Fall. Mit einer Zwei-Spalten-Tabelle, was ihm gehoert und was Diagnose ist.

**Und die Stelle, an der der Autor es vermisst hat, ist gefunden und behoben.**
b2 K74 machte auf mit *"You have come with something and you are not going to
make me guess"* - keine Frage, kein Angebot, kein Blick auf den Mann. Jetzt
(ch74 v1.3):

> *"Have you eaten today." **Sim had the cup out before he had finished asking,
> and he did not wait for the answer.** "You have come with something and you are
> not going to make me guess."*

Die Diagnose bleibt - sie steht jetzt **hinter** der Hoeflichkeit und nicht an
ihrer Stelle. `faktenspur.py` meldet null bewegte Zahlen, `check.py` keinen
Fragezeichen-Hinweis auf die neue Zeile.

**Fuer jede weitere Figur gilt ab jetzt beides:** was darf nicht drinstehen -
und **was muss drinstehen**. Die zweite Frage ist die schwerere und die, die
zaehlt.

*Unsicher:* keiner.

## Der Mechanismus: werkzeug/anwesenheit.py

**Auf die Frage des Autors am 26.08. - *"Hast Du einen Mechanismus
festgezurrt, damit eigener Charakter bei den anderen auch aufgebaut wird?"* -
war die ehrliche Antwort nein.** Die Anwesenheitspruefung stand als Prosa auf
Sims Blatt, und Prosa rechnet niemand nach. Jetzt steht sie im Werkzeug.

**Wie eine Figur eine Probe bekommt.** Ihr Abschnitt in `doc/12-stimmen.md`
bekommt eine Tabelle unter `#### Anwesenheitsprobe`:

    | Zug | Muster | mind. |
    |---|---|---|
    | stellt die Urheberschaft richtig | `...regex...` | 1 |

`anwesenheit.py` liest sie, misst gegen die **eigene Rede** der Figur und
meldet, in welchen Kapiteln der Zug fehlt. `--offen` listet die Blaetter, die
noch keine Probe haben, nach Textmenge.

**Geeicht auf sechs Frage- und fuenf Gegenproben aus dem Buch.** Die erste
Fassung der Eichung prueфte, ob Sim null Fragen hat - und schlug fehl, sobald
ich ihm eine gab. **Eine Eichung, die eine Reparatur als Fehler meldet, misst
die Reparatur und nicht das Werkzeug.** Ersetzt durch feste Proben.

**Drei eigene Fehler beim Bau, alle gefunden, weil die Eichung lief:**

| Fehler | Symptom |
|---|---|
| `\b` als Steuerzeichen in die Datei geschrieben | sechs Muster trafen nichts |
| Tabellenzeile an `\|` zerlegt, waehrend der Regex selbst Pipes enthaelt | Mindestzahl war Unsinn |
| `FRAGE` ohne `re.I` und ohne fuehrende Konjunktion | *"And where were you educated?"* fiel durch - **das haette bei jeder Figur zu wenig gezaehlt** |

### Erster Testfall: Mrs Ha, vorher und nachher

**Vorher** - ihr Blatt hatte Maschine, Anliegen und den Kontraktionsrang, aber
keine Probe. Das Werkzeug konnte ueber sie genau eine Zahl sagen: 6,2 Fragen je
100 Repliken.

**Nachher** - und der Befund ist besser als erwartet. **Ihr distinktivster Zug
stand nicht auf ihrem Blatt:**

| Zug | Mrs Ha | Georgij, Annie, Sang-hoon, Woo, Sim, Hana, Mrs Jeon, Jang, Ahn |
|---|---|---|
| **stellt die Urheberschaft richtig** | **3 Treffer** | **alle 0 %** |
| gibt woertliche Rede weiter | 3 | 0-3 % |
| benennt die Luege | 1 | 0-1 % |
| zaehlt in Ware und Wochentagen | 4 | 0-2 % |

> *"On the Monday. **Not the mother, not a cousin, not the hall. Her.**"*
> *"She was at the fitting. **I did the fitting.**"*
> *"Eleven tables' worth. **I put them in the van myself** on the Tuesday."*

**Jede Berichtigung dreht sich um dieselbe Frage: wer hat es wirklich gemacht.**
Bei einer Frau, der das Geschaeft weggenommen wurde und deren Arbeit unter
fremdem Namen weiterlief, sind Anliegen und Maschine **dieselbe Sache**. Das
stand nirgends und steht jetzt auf ihrem Blatt.

**Alle fuenf Zuege sind bei ihr anwesend, 1/1 Kapitel.** Sie ist der Gegenfall
zu Sim: eine Figur, die ihre eigene Probe von selbst besteht.

**Grenze, und sie gehoert in den Bericht:** Mrs Ha spricht bisher in **einem**
Kapitel. `mind.` misst je Kapitel, also ist das eine Stichprobe von eins. Die
Probe wird erst scharf, wenn sie ein zweites Mal auftritt - und genau dafuer
steht sie jetzt schon da.

*Unsicher:* keiner.

## Mrs Ha: der Skyrim-Test, und warum meine erste Messung ein Artefakt war

**Der Autor: *"Aktuell ist die eine Fragenbeantwortungsmaschine, die nach einer
KI klingt aus 2016"*, spaeter praeziser: *"sie klingt wie ein NPC aus Skyrim.
Sie soll klingen wie ein NPC aus Baldur's Gate 3."***

**ALTE ERGEBNISSE** (auf dem Index, 16 Repliken):

| | Mrs Ha | Hong | Woo | Sang-hoon | Sim |
|---|---|---|---|---|---|
| spricht den Anwesenden an | **12 %** | 57 % | 40 % | 38 % | 32 % |
| steht in der Gegenwart | **25 %** | 43 % | 51 % | 65 % | 51 % |

**Das war falsch, und zwar systematisch.** `stimmen.py` kennt 16 ihrer
Repliken; **die Szene hat 39**. Die 16 sind die mit Begleitsatz - und **eine
Replik mit Begleitsatz ist ueberdurchschnittlich oft eine schlichte Antwort**,
weil die lebendigen Zeilen im blossen Wechsel ohne Tag laufen.

**NEUE ERGEBNISSE** (ueber die ganze Szene, 39 Repliken): Anrede **41 %**,
Gegenwart **44 %**, Urteil 31 %, Raum 28 %. Mittelfeld, nicht Schlusslicht.
**Wer eine Zweipersonenszene ueber den Index misst, misst systematisch das
flachste Drittel der Figur.**

### Was dann wirklich fehlt

Auch nach Drittelung der Szene liess sich nichts finden - die Mitte ist so gut
wie der Anfang (*"You said one and then you asked four, and I'm going to let
you, because it's the first interesting afternoon I've had since February"*).
**Der Befund kam erst mit dem Bild des Autors.**

**In 39 Repliken stellt sie genau eine Frage, und die geht ueber sie selbst**
(*"Do you know how many I've done."*). Sie fragt ihn **kein einziges Mal**, wer
er ist, warum ihn das angeht, was er damit vorhat oder was jetzt mit der Frau
geschieht.

**Und das Kapitel legt ihr die Gelegenheit ausdruecklich hin.** Georgijs erster
Satz im Zimmer: *"…and **then I am going to answer any question you ask me**, and
then I am going to go."* **Sie nimmt das Angebot nie an.**

**Das ist der Unterschied in einer Zeile:** der Dialogbaum bietet den
Rueckkanal an, und der NPC benutzt ihn nicht. Sie urteilt ueber ihn, sie
verlangt von ihm, sie wechselt die Position - **sie befragt ihn nur nicht.**

### Was daraus im Werkzeug steht

Ihre Anwesenheitsprobe hat jetzt **befragt ihn zurueck** als scharfe Zeile, und
`anwesenheit.py` meldet sie mit **0 Treffern**. Dazu die Warnung zur
Index-Verzerrung, die fuer jede Zweipersonenszene gilt.

**Ein eigener Fehler dabei:** meine Einfuegung ist zuerst in **Sims** Abschnitt
gelandet und hat dessen Probe ueberschrieben - mein Suchkriterium hat die
naechste Ueberschrift genommen statt der in ihrem Abschnitt. Mit
`git checkout` zurueckgesetzt und sauber wiederholt. **Eine Einfuegung, die
eine Ueberschrift sucht, muss die Grenzen des Abschnitts kennen.**

*Unsicher:* keiner.

### Berichtigung und der Eingriff in b2 K67

**Zuerst eine Berichtigung an mir selbst: sie fragt doch.** Am Schluss, an der
Tuer - *"Is she alive."* - und der Erzaehler markiert es sogar: *"At the door
she asked the question he had been waiting for since the boxes."* Mein
Fragemuster hatte `Is it|Is that`, aber nicht `Is she`. **Zum dritten Mal in
dieser Sitzung war ein Befund ein Messfehler**, und zum dritten Mal war es
meiner.

**Was bleibt, ist praeziser:** sie fragt nach **der Frau** und kein einziges Mal
nach **ihm**. In 39 Repliken geht eine Frage ueber ihr Gegenueber, und die
handelt von ihr selbst (*"Do you know how many I've done."*).

**Die Stelle lag offen da** - sie schenkt ihm die Extrafragen, statt sie zu
berechnen: *"You said one and then you asked four, and I'm going to let you."*
Jetzt (ch67 v1.4) nimmt sie Georgijs eigenes Angebot an und laesst ihn zahlen:

> *"…and I'm going to let you, because it's the first interesting afternoon
> I've had since February." **She did not sit back. "You also said you'd answer
> anything I asked. I'll have mine now and not at the door. Who pays you?"***
>
> ***"A woman in Seoul," said Georgij. "I am not going to give you her name, and
> that is the only thing I am keeping from you today."***
>
> ***"Then she's getting her money's worth."*** *Mrs Ha sat back. "She was the
> calmest person in this room…"*

Gemessen ueber die Szene: Fragen ueber ihn **1 → 2**, und die neue kostet ihn
etwas. `faktenspur.py` meldet nur *Georgij 18 → 19* - das ist der neue
Begleitsatz und keine bewegte Tatsache.

**Ist sie damit ein BG3-NPC? Nicht durch eine Zeile.** Was sie schon hatte:
sie urteilt ueber den Wortwechsel, sie verlangt, sie wechselt im Lauf der Szene
die Position, sie hat einen eigenen Einsatz. Was gefehlt hat, war der
**Rueckkanal** - der ist jetzt da.

**Was weiter fehlt, und es ist benennbar:** in BG3 aendert *deine Antwort*, was
du bekommst. Hier verdient Georgijs Antwort ein Lob (*"Then she's getting her
money's worth"*), aber sie aendert nicht, **was Mrs Ha danach hergibt**. Der
naechste Schritt waere, dass eine schlechtere Antwort ihr eine Auskunft
gekostet haette.

*Unsicher:* ob *"A woman in Seoul"* Georgij zu viel preisgibt - er haelt Annie
sonst streng zurueck. Der Name bleibt drin nicht drin, aber die Existenz einer
Auftraggeberin ist neu gesagt. **Das gehoert vom Inhalts-Chat geprueft.**

## Fragezeichen: 150 gesetzt, 6 stehen gelassen

**Die Regel stand seit dem 24.08. in `doc/01-craft.md`:** *"Steht er in
Fragesyntax oder ist er eine verkuerzte Frage, kommt ein Fragezeichen hin, egal
wie kalt er ist."* **Das Buch hat sie 156-mal nicht befolgt.**

**Gearbeitet wurde auf `check.py`s eigener Liste**, nicht auf einem Muster von
mir - ihr Ausdruck verlangt, dass die **ganze** Replik die Frage ist
(`^"QWORD[^?"]{0,70}\."$`). Ein selbstgebautes Muster haette Deklarativsaetze
mit Fragewort am Anfang mitgerissen.

**150 gesetzt, in 70 Kapiteln. Sechs bleiben, und jeder einzeln begruendet:**

| Stelle | warum |
|---|---|
| b1 K01 *"When he bought the boy."* | Antwort auf *"When."*, Aussagesatz |
| b1 K09 *"Whatever I was given."* | Aussagesatz |
| b1 K24 *"What you paid me in on the gravel…"* | Aussagesatz, wh-Satz ist das Subjekt |
| b1 K26 *"What she wants is shares, security…"* | dito |
| b2 K18 *"What it changes is you."* | dito |
| **b1 K34 *"Is that all of it."*** | **vom Handwerksdokument ausdruecklich gesetzt** - die Gegenprobe zu Georgijs *"That is all of it?"* drei Seiten davor. *"Umgestellt ist Forderung."* |

`check.py` meldet danach genau diese sechs. **`faktenspur.py`: null bewegte
Zahlen, Daten und Namen.**

## Mrs Ha: die Antwort aendert, was sie hergibt

**Der zweite Teil der BG3-Mechanik.** Bisher verdiente Georgijs Antwort ein Lob,
aber sie aenderte nichts. Jetzt macht sie den Zustandswechsel ausdruecklich -
mit dem Gegenfall, der ihn erst sichtbar macht:

> *"Then she's getting her money's worth." Mrs Ha sat back. **"If you'd said
> insurance, you'd have had the wedding and the door. You can have the afternoon
> instead."** "She was the calmest person in this room…"*

**Der Gegenfall ist das Ganze.** Ohne ihn ist eine Belohnung nur Freundlichkeit;
mit ihm war das Gespraech ein Zustand, den seine Antwort verschoben hat. Und er
bindet zurueck an ihre erste Zeile an der Tuer - *"You are not from the
insurance."* - und an ihre eigene Waehrung, *"the first interesting afternoon
I've had since February."*

`faktenspur.py`: null bewegte Zahlen.

*Unsicher:* weiterhin nur *"A woman in Seoul"* - dass Georgij die Existenz einer
Auftraggeberin ueberhaupt einraeumt, gehoert vom Inhalts-Chat geprueft.

### Berichtigung: meine eigene Zeile war geklaut und war NPC-Gelaber

**Der Autor zu meiner Fassung *"If you'd said insurance, you'd have had the
wedding and the door"*: NPC-Gelaber, geklaut von Georgij.** Beides stimmt, und
beides haette ich vor dem Schreiben gemessen, wenn ich meine eigene Regel
befolgt haette.

**Geklaut:** das Konterfaktische *"haettest du X, dann haettest du Y"* gehoert
Georgij - **10 der 13 Vorkommen im ganzen Buch**, darunter b2 K06 *"you would
have had to answer it as one"*. Ich habe Sim vier solcher Anleihen ausgetrieben
und Mrs Ha am selben Tag eine neue gegeben.

**NPC-Gelaber, und das ist der schwerere Fehler:** die Zeile **erklaert den
Mechanismus, statt ihn zu vollziehen**. Ein BG3-NPC sagt nicht, was du bei
schlechterer Antwort bekommen haettest - er gibt dir einfach mehr. Wer den
Zweig ausspricht, hat den Dialogbaum sichtbar gemacht.

**Jetzt (ch67 v1.7) wird er vollzogen.** Die Szene zaehlt seine Fragen von
Anfang an mit - *"One question."* · *"That's your second question."* · *"You
said one and then you asked four"* - und nach seiner geraden Antwort:

> *"Then she's getting her money's worth." Mrs Ha sat back. **"Ask what you like
> now. I've stopped counting.** She was the calmest person in this room…"*

**Sie hoert auf zu zaehlen. Das ist der Zustandswechsel, und es steht kein Wort
darueber da.** Vorab gemessen: keine der vier Kandidatenfassungen enthaelt eine
Wendung, die Georgij benutzt. `faktenspur.py`: null bewegte Zahlen.

**Die Lehre, zum zweiten Mal notiert und diesmal hoffentlich behalten:** ein
Ersatz wird gemessen, **bevor** er ins Kapitel geht. Und: **wenn eine Figur die
Regel des Gespraechs ausspricht, ist es keine Figur mehr.**
