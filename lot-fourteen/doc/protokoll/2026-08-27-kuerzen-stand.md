# Stand des Kuerzungslaufs am Abend des 27.08., und was als Naechstes zu tun ist

Geschrieben am Ende eines Laufs, der an die Kontextgrenze gekommen ist. Wer
hier weitermacht, soll nicht noch einmal herleiten muessen, was heute schon
gemessen worden ist — **und vor allem nicht noch einmal die zwei Fehler machen,
die diesen Nachmittag gekostet haben.**

---

## Wo der Band steht

Band 2 hat **83 Kapitel, Nummern 1 bis 83 ohne Luecke**, rund 220.900 Woerter
Kapiteltext. `check.py` meldet drei Fehler, und es sind dieselben drei
Zahlenkonstanten in `doc/`, die vorher schon dastanden. Alles ist committet und
gepusht, zuletzt `9ea2685`.

Die Szenenliste der vier Zusammenlegungen liegt als Seite unter
`https://claude.ai/code/artifact/ed0da4f1-54e1-4780-9317-be2c9b662e67`.

---

## Was als Naechstes zu tun ist

**Klasse C und Klasse D aus TEIL VI der CHOI-LISTEN, in dieser Reihenfolge.**
Beide sind vom Autor am 27.08. benannt worden, beide sind lokalisiert, und
zusammen sind es rund 8.000 Woerter.

### 1. Klasse C — Der Ausschluss, in Kapitel 32

Das frueher 38 und 39 gewesene Kapitel braucht **5.723 Woerter, um
festzustellen, dass Yeom nicht Y ist**. Die Vorgabe: *"Ein Ausschluss darf drei
Saetze kosten, nicht zwei Kapitel."* Ziel ~2.000, also **rund 3.700 weg**.

Was laut Liste bleiben muss: **der Begleiter, der isst**, und **der
April-Aufraeumer** — also die zwei Nebenfiguren, die der Ausschluss nebenbei
hervorbringt. Der Rest ist der Ausschluss selbst.

Dazu in derselben Klasse: die Lizenzsuche in **34** (~1.200 auf die Haelfte)
und die zwei Tage an K in **36** (~600).

### 2. Klasse D — Die Inventur

*Georgij legt Annie hin, was der Leser gerade gelesen hat.* Fuenf Stellen,
zusammen ~5.300:

| neu | Stelle | Woerter |
|---|---|---|
| **29** | Szene 1, alle Papiere auf dem Schreibtisch | ~2.200 |
| 28 | Nachgespraech ueber das fruehere Kapitel 29 | ~1.200 |
| 31 | Mrs Jeons Brief, Nachbereitung | ~800 |
| 32 | Bericht ueber die zwei Restaurants | ~600 |
| 35 | Bericht ueber Jangs Zahl | ~500 |

### 3. Klasse A — dreimal dieselbe Frage in Kapitel 29

Die Frage nach den vier Tagen faellt in einem Kapitel **dreimal**: Sang-hoon am
Telefon (~900), Jang im Garagengang (~700), Annie in der Garage (~500). **Das
Kapitel sagt es selbst**: *"had just asked him the same question Sang-hoon had
asked on the telephone that morning."* Eine bleibt.

Dazu *"You are not going in. Not yet."* in **33** (~500), *"Nothing happens to
Dr Oh today"* in **34** (~400), die Genehmigungsszene in **35** (~900).

### 4. Klasse E — zwei von vier Gestaendnisrunden

Von sieben Runden sind drei mit den gestrichenen Kapiteln weggefallen. Der Plan
will **zwei behalten**: das frueher 29 (jetzt **26**), weil es das erste ist und
Annie mit dem Preis antwortet, und das frueher 53 (jetzt **44**), *"I am the
February one"*. Also fallen **38** (die Blumen) und **40** (Mrs Bae), ~2.000.

---

## Was zuerst gelesen werden muss, und wo es steht

1. **`Downloads/CHOI-LISTEN.md`, TEIL VI, Abschnitt 6** (etwa Zeile 1031):
   *"Die Streichklassen: Namen und alle Stellen."* Fuenf Klassen mit Tabellen.
2. **Dieselbe Datei, TEIL II B** (etwa Zeile 170): die Streichliste je Kapitel
   mit Vorschlag und Ersparnis. **Genauer als alles, was heute neu gemessen
   worden ist.**
3. **`archiv/UMNUMMERIERUNG.md`** — beide Listen nennen **alte** Kapitelnummern.
   Ohne diese Zuordnung zeigt jede Angabe darin ins Falsche.
4. **`doc/23-kuerzen.md`** — das Verfahren, die drei Eingriffe, und der Eintrag
   vom 27.08. mit der Tabelle der fuenf Fehlurteile.
5. Und die Regel aus `CLAUDE.md`: **das betroffene Kapitel und die zwei davor
   lesen**, nicht die Zusammenfassung.

---

## Die zwei Fehler, die diesen Nachmittag gekostet haben

**Erstens: nicht nach Geruest urteilen.** Ich habe Anfang und Ende jeder Szene
gelesen und daraus fuenf Kuerzungskandidaten gebildet. Alle fuenf waren falsch.
**In diesem Band endet fast jede Szene mit einer kursiven Notizbuchzeile**, also
sieht jede nach Buchfuehrung aus, waehrend im Rumpf das Argument steht. Die
Tabelle mit allen fuenf steht in `doc/23-kuerzen.md`.

**Zweitens: nicht Szene fuer Szene fragen, ob etwas Gutes darin steht.** Das tut
jede. Die richtige Frage ist, **wofuer das Kapitel da ist**. 5.723 Woerter, um
zu zeigen, dass ein Mann nicht der Gesuchte ist, sind zu viel, gleichgueltig wie
gut die einzelnen Szenen sind. Und Wiederholung zaehlt man **ueber Szenen
hinweg** — dieselbe Frage dreimal in einem Kapitel sieht man in keiner
Einzelszene.

---

## Was nicht noch einmal gemacht werden muss

- **Die Abendberichte.** Gemessen und gelesen, Kapitel 25 bis 61 vollstaendig.
  Sie zahlen ein; dort faellt der Name, dort steht *"Twenty-two days"*, dort
  *"That is a seam."* Die 54 Prozent aus `doc/23-kuerzen.md` sind ein Artefakt
  der Messung: sie zaehlt jedes Kapitel mit, in dem ihr Name in den letzten
  1.200 Zeichen vorkommt, auch wenn Georgij allein am Notizbuch sitzt. Wirklich
  mit einer Szene bei ihr enden **40 Prozent**.
- **Die vier Zusammenlegungen als Redundanz.** `doppelt-im-kapitel.py` hat in
  35 vier echte Doppelungen gefunden, alle behoben, zusammen 67 Woerter. In 26,
  29 und 32 war jedes gemeldete Paar berechtigt.
- **Die Bandbreiten-Entscheidung fuer 26 und 35.** Sie bleiben ueber der Spanne.
  Begruendung in `doc/23-kuerzen.md`.

---

## Offene Faeden, die nichts mit Kuerzen zu tun haben

**Kapitelverweise in `doc/`.** 335 sind am 27.08. umgehaengt, 88 als `alt KNN`
markiert, **166 offen** — siehe `archiv/VERWEISE-OFFEN.md`. Davon 78 blanke
`KNN` bis 34, wo das Band nicht aus dem Verweis hervorgeht.

**Und eine Falle, die noch scharf ist:** die Streichliste und die
Streichklassen in `CHOI-LISTEN.md` nennen Kapitel in der Form *"Kapitel 33"*.
Diese Form ist **nicht** nachgezogen worden — nur `b2 KNN` und
`Band 2, Kapitel N`. Wer die Listen liest, liest alte Nummern.
`CHOI-LISTEN.md` liegt ausserdem ausserhalb des Repos, in `Downloads/`.

**`ch57` im Archiv** sagt an einer Stelle *"Twenty-four years ago"*, waehrend
fuenf andere Stellen im selben Kapitel *"twenty-three"* sagen. In der neuen
Fassung (Kapitel 63) ist es durchgezogen.

---

## Werkzeuge, die es seit heute gibt

| | |
|---|---|
| `werkzeug/kontinuitaet.py` | woertlich gleiche Saetze ueber Kapitel hinweg, feste Zahlen, Alter je Figur, Wochentage im Fliesstext |
| `werkzeug/doppelt-im-kapitel.py` | Absatzpaare mit denselben seltenen Woertern, innerhalb eines Kapitels |
| `werkzeug/szenen.py` | das Geruest eines Kapitels. **Taugt zum Finden, nicht zum Urteilen** |
| `werkzeug/abendbericht.py` | welcher Schluss bei Annie etwas Neues bringt |
| `werkzeug/umnummerieren.py` | der Vorgang vom 27.08., als Beleg |
| `werkzeug/verweise-nachziehen.py` | Kapitelverweise in `doc/` umhaengen |
