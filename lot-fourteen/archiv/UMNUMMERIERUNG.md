# Umnummerierung Band 2, 27.08.

Band 2 steht auf der Folge aus Teil XII, durchnummeriert von 1 bis 83.
Vorher waren es 82 Kapitel mit Nummern 1 bis 90 und acht Luecken. Der
Bestand liegt vollstaendig in `archiv/band-2-vor-umbau/`.

**Wofuer das hier da ist:** in `doc/` stehen rund 1.300 Verweise auf
Band-2-Kapitel, als `Band 2, Kapitel N` und als Kurzform `KNN`. Sie zeigen
alle noch auf die alte Nummerierung.

## Alt nach neu

| alt | neu | | alt | neu | | alt | neu | | alt | neu |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | | 2 | 2 | | 3 | 3 | | 4 | 4 |
| 5 | 5 | | 6 | 6 | | 7 | 7 | | 8 | 8 |
| 9 | 9 | | 10 | 10 | | 11 | 11 | | 12 | 12 |
| 13 | 13 | | 14 | 14 | | 15 | 15 | | 17 | 16 |
| 18 | 17 | | 19 | 18 | | 20 | 19 | | 21 | 20 |
| 22 | 21 | | 23 | 22 | | 24 | 23 | | 25 | 24 |
| 26 | 25 | | 28 | 26 | | 29 | 26 | | 31 | 27 |
| 32 | 28 | | 33 | 29 | | 35 | 29 | | 36 | 30 |
| 37 | 31 | | 38 | 32 | | 39 | 32 | | 40 | 33 |
| 41 | 34 | | 42 | 35 | | 43 | 35 | | 45 | 36 |
| 46 | 37 | | 47 | 38 | | 48 | 39 | | 49 | 40 |
| 50 | 41 | | 51 | 42 | | 52 | 43 | | 53 | 44 |
| 54 | 45 | | 55 | 46 | | 56 | 47 | | 58 | 48 |
| 60 | 49 | | 63 | 50 | | 64 | 51 | | 80 | 52 |
| 81 | 53 | | 82 | 54 | | 83 | 55 | | 84 | 56 |
| 85 | 57 | | 86 | 58 | | 87 | 59 | | 89 | 61 |

## Aufgegangen in umgebauten oder neu geschriebenen Kapiteln

| alt | neu | |
|---|---|---|
| ch57 | 63 | umgebaut |
| ch61 | 71 | umgebaut |
| ch62 | 72 | umgebaut |
| ch65 | 65 | umgebaut |
| ch66 | 66 | mit ch67 zusammen |
| ch67 | 68 | geteilt auf 66 und 68 |
| ch88 | 80 | Neubau |
| ch90 | 83 | geteilt auf 69, 73 und 83 |

## Entfaellt ganz

Kommt in der neuen Folge nicht vor, liegt im Archiv:

`ch69`, `ch70`, `ch71`, `ch72`, `ch73`, `ch74`, `ch75`, `ch76`, `ch77`

`ch78` ist nicht gestrichen - es wird Nummer 76, sobald es umdatiert und
gekuerzt ist.

## Zwei reservierte Plaetze

| Nr. | Was | Stand |
|---|---|---|
| 60 | *Sie faehrt zurueck* (Teil XII Nr. 36) | nicht geschrieben |
| 76 | *The only line out* (Teil XII Nr. 52, aus `ch78`) | muss umdatiert und gekuerzt werden |

Beide stehen in `werkzeug/build.py` unter `GESTRICHEN`, damit der Build
laeuft. **Die Eintraege gehoeren geloescht, sobald die Kapitel da sind.**

## Was noch offen ist

- Die acht Kuerzungen aus Teil XII sind **nicht** ausgefuehrt. Die Kapitel
  sind ungekuerzt mitgezogen: neu 28, 31, 33, 34, 40, 44, 49, 55.
- Die Umbenennungen aus Teil XII sind **nicht** ausgefuehrt. Jedes Kapitel
  hat seinen Titel behalten; nur die vier Zusammenlegungen haben einen
  neuen, weil zwei Kapitel nicht zwei Titel behalten koennen.
- `doc/05-continuity.md` fuehrt die Kapitelliste nach alten Nummern.
- `.check-baseline` hat b2-Schluessel nach alten Nummern.

---

# Nachtrag 28.08.: die Karte bis heute, und warum der Katalog nicht taugt

**Band 2 hat seit dem 28.08. fuenfundachtzig Kapitel.** `ch35` ist in drei
geteilt worden, und alle Nummern der Folge vom 27.08. ab 36 sind seither **um
zwei hoeher**.

## Alt nach HEUTE, am Text bewiesen

Nicht gerechnet, sondern gemessen: fuer jedes Kapitel in
`archiv/band-2-vor-umbau/` sind bis zu sechs lange Passagen aus der Mitte
genommen und im heutigen Kanon gesucht worden. Wo alle im selben Kapitel
landen, ist die Zeile belegt.

| alt | heute | | alt | heute | | alt | heute | | alt | heute |
|---|---|---|---|---|---|---|---|---|---|---|
| 1-15 | 1-15 | | 17 | 16 | | 18 | 17 | | 19 | 18 |
| 20 | 19 | | 21 | 20 | | 22 | 21 | | 23 | 22 |
| 24 | 23 | | 25 | 24 | | 26 | 25 | | 28 | 26 |
| 29 | 26 | | 31 | 27 | | 32 | 28 | | 33 | 29 |
| 35 | 29 | | 36 | 30 | | 37 | 31 | | 38 | 32 |
| 39 | 32 | | 40 | 33 | | 41 | 34 | | 42 | **35** |
| 43 | **36 und 37** | | 45 | 38 | | 46 | 39 | | 47 | 40 |
| 48 | 41 | | 49 | 42 | | 50 | 43 | | 51 | 44 |
| 52 | 45 | | 53 | 46 | | 54 | 47 | | 55 | 48 |
| 56 | 49 | | 57 | 65 | | 58 | 50 | | 60 | 51 |
| 61 | 73 | | 62 | 74 | | 63 | 52 | | 64 | 53 |
| 65 | 67 | | 66 | 68 | | 67 | 68 und 70 | | 78 | 78 |
| 80 | 54 | | 81 | 55 | | 82 | 56 | | 83 | 57 |
| 84 | 58 | | 85 | 59 | | 86 | 60 | | 87 | 61 |
| 89 | 63 | | 90 | **85** | | | | | | |

**Die Teilung vom 28.08. lief fast genau auf der alten Naht:** alt `ch42` ist
heute `ch35`, alt `ch43` verteilt sich auf `ch36` und `ch37`. Die
Zusammenlegung vom 27.08. hat zwei Kapitel verbunden, die drei Tage trugen.

**Nicht mehr im Buch:** alt `ch69` bis `ch77` und `ch88`. Ihr Text findet sich
nirgends im heutigen Kanon. Sie liegen in `archiv/band-2-vor-umbau/`.

## Warum `VERWEISE-OFFEN.md` nicht mechanisch abzuarbeiten ist

**Der Katalog etikettiert alle Kurzformen als *alt*, und das stimmt nicht.**
Nachgewiesen an zwei Faellen:

- **`K68`** ist eine Nummer vom **27.08.** Das Zitat *"I have been sent to be
  liked, four hundred times"* steht heute in `ch70`, und 68 plus zwei ist 70.
  In der **alten** Folge gab es bei 68 ueberhaupt kein Kapitel.
- **`K90`** ist eine **alte** Nummer. Das Zitat *"If the world points anything
  at you at all, I will burn the world down"* steht heute in `ch85`, und die
  alte 90 ist ueber die 83 vom 27.08. genau dort gelandet. In der Folge vom
  27.08. gab es keine 90.

**Zwei Nummerierungen unter einem Etikett, im selben Dokument.** Damit ist
jede Stelle einzeln zu entscheiden, und ein pauschaler Versatz waere falsch.

## Was der Durchgang vom 28.08. ergeben hat

Alle 166 Stellen maschinell angefasst, jede ueber ihr laengstes Zitat im
heutigen Kanon gesucht:

| | |
|---|---|
| **9** | Zitat gefunden, Kapitel steht fest |
| **14** | Zitat **nicht mehr im Buch**: der Verweis zeigt auf Archivtext |
| **143** | kein Zitat in der Zeile, nur Prosa |

**Die 143 brauchen den Absatz drumherum**, nicht die Zeile. Das ist Lesearbeit
und kein Skript.

**Und die 14 sind kein Umnummerierungsfall, sondern ein Inhaltsfall.** Saetze
wie *"Whoever's in that room is bored"* (alt K73) oder *"I told her the weather
might turn"* (alt K72) stehen in keinem Kapitel mehr. Wer sie in `12-stimmen.md`
als Beleg liest, belegt etwas mit Text, den es nicht gibt. Diese Stellen
gehoeren gekennzeichnet, nicht umnummeriert.
