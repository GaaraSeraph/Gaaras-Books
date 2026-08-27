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
