# Uebergabe: alle Kapitel von Band 2 auf ueberfluessige Szenen durchgehen

Geschrieben am Abend des 27.08. nach einem Lauf, der die fuenf Streichklassen
aus den CHOI-LISTEN abgearbeitet hat. **Der Auftrag fuer den naechsten Lauf ist
ein anderer und groesser: alle 83 Kapitel, Szene fuer Szene, auf
Daseinsberechtigung.**

Wer hier weitermacht, soll zwei Dinge nicht noch einmal tun muessen: die
Messungen von heute, und die zwei Denkfehler, die vier Klassen lang gekostet
haben.

---

## Der Auftrag

**411 Szenen in 83 Kapiteln.** Fuer jede eine Antwort auf eine einzige Frage:

> **Wofuer ist diese Szene da, und was faellt aus, wenn sie fehlt?**

Nicht: steht hier etwas Gutes drin. Das steht ueberall. Nicht: wiederholt sich
hier etwas. Das ist ein Nebenbefund. **Die Frage ist, ob der Text ohne sie
etwas verliert, das er nicht anderswo hat.**

Das Ergebnis je Szene gehoert in eine Tabelle in `doc/23-kuerzen.md`, mit
Kapitel, Szenennummer, Woertern, Aufgabe und Urteil. Erst wenn die Tabelle
steht, wird geschnitten.

---

## Wo der Band steht

| | |
|---|---|
| Band 2 | **83 Kapitel, 222.959 Woerter**, Nummern 1 bis 83 ohne Luecke |
| Szenen | **411** |
| `check.py` | 92 Kapitel geprueft, **0 Fehler**, keine Verschuldung |
| letzter Commit | `f00ba06`, gepusht, Arbeitsbaum sauber |
| gegen den Plan | **+22.538** ueber der Summe der Zielgroessen aus TEIL XII |

---

## Die zwei Fehler, die nicht wiederholt werden duerfen

**Erstens: nicht nach dem Geruest urteilen.** In diesem Band endet fast jede
Szene mit einer kursiven Notizbuchzeile. Wer Anfang und Ende liest, sieht
ueberall Buchfuehrung, waehrend im Rumpf das Argument steht. So sind am 27.08.
fuenf Kuerzungskandidaten entstanden und **alle fuenf waren falsch**, darunter
die zwei Zeugen aus dem Titel von Kapitel 29.

`werkzeug/szenen.py` gibt genau dieses Geruest aus. **Es taugt zum Finden und
nicht zum Urteilen.** Die Liste sagt, wo etwas steht, nicht ob es bleibt.

**Zweitens: einmalig ist nicht dasselbe wie gebraucht.** Bei Kapitel 29 Szene 1
habe ich zweimal geprueft, ob ihr Inhalt sonst irgendwo vorkommt, und daraus
geschlossen, sie sei unverzichtbar. Erst die Rueckfrage des Autors - *ist die
Szene relevant?* - hat die richtige Probe erzwungen: **welche spaetere Stelle
zeigt auf sie?** Fuer diese Szene waren es fuenf, eine davon in Kapitel 30. Fuer
den Byun-Block darin waren es null, und der ist danach gefallen.

**Die Probe ist also nicht Suche nach Wiederholung, sondern Suche nach
Rueckbezug.** Wer eine Szene streichen will, muss vorher wissen, wer auf sie
zeigt.

---

## Was heute schon gemessen ist und nicht wiederholt werden muss

### Die fuenf Streichklassen sind abgearbeitet

Zusammen **2.927 Woerter** gefunden gegen **rund 22.000** veranschlagte. Die
Klassen beschreiben Muster, und die Muster sind mit den neun gestrichenen
Kapiteln und den Umbauten groesstenteils verschwunden. Die Einzelbefunde stehen
in `doc/23-kuerzen.md`. **Die Klassen sind erledigt. Nicht noch einmal
anfangen.**

Drei Posten sind nachweislich nicht ausfuehrbar und das ist begruendet
festgehalten:

- **Kapitel 36** - der Ausschluss ist dort der Motor und nicht der Leerlauf, und
  das Kapitel liegt mit 2.135 auf seiner Zielgroesse von 2.150.
- **Kapitel 35, die Genehmigungsszene** - sie ist die **Aufloesung** der Klasse
  A und nicht ihr fuenfter Fall. Annie beendet das Muster darin ausdruecklich.
- **Kapitel 29 Szene 1** - fuenf spaetere Stellen zeigen darauf, eine davon in
  Kapitel 30, und die Regel darin ist die Voraussetzung der ganzen Klasse A.

### Die Zielgroessen sind gemessen

`werkzeug/plan.py` stellt jedes Kapitel neben seine Zielgroesse aus TEIL XII
(Nr. N = Kapitel N+24, deckt 25 bis 83 ab). **Das ist der beste Einstieg in den
neuen Auftrag**, weil es sagt, wo zu viel ist, bevor man liest:

```
Kap   Titel                                  ist    Ziel darueber
29    Two witnesses                         7419    2800    +4619
26    She has a list                        6836    3500    +3336
35    Somebody in Seoul pays for it         7988    5500    +2488
32    The man kitchens talk to              4062    2000    +2062
31    The one who asked a question          3587    2200    +1387
```

**Die ersten fuenf sind zusammen 13.892 von 22.538, also zweiundsechzig
Prozent. Und vier davon sind die vier Zusammenlegungen** - 26 aus 28+29, 29 aus
33+35, 32 aus 38+39, 35 aus 42+43.

**Sie sind aneinandergehaengt und nicht reduziert worden.** TEIL XII hatte
jedem eine Zielgroesse deutlich unter der Summe der zwei Teile gegeben. Beim
Zusammenlegen ist nur der erste Schritt ausgefuehrt worden.

`check.py` sagt unabhaengig davon dasselbe: 26, 29 und 35 liegen alle drei ueber
ihrer eigenen Spanne, die nach Erzaehltagen mitwaechst.

---

## Womit anzufangen ist

**Nicht bei Kapitel 1.** Die Szenen, die am ehesten ueberfluessig sind, sind die
grossen in den zu grossen Kapiteln. Zwei Einstiege, und der zweite ist der
bessere:

1. **Die fuenf Kapitel aus der Tabelle oben**, weil dort dreiundsechzig Prozent
   der ueberzaehligen Woerter liegen. **Kapitel 29 ist davon fertig geprueft**
   (Tabelle unten) und wartet auf eine Bauentscheidung, nicht auf einen Schnitt.
2. **Die Szenen ueber 1.500 Woertern**, quer durch den Band. Die groessten:

```
b2 35   3310W  Sang-hoon had chosen a table this time instead of a room
b2 41   2868W  Sang-hoon sent for him at ten in the morning, to his own office
b2 05   2792W  He took the coat off and put it over the arm of the chair
b2 33   2717W  Jang asked for the whole morning, and Annie gave it to him
b2 08   2574W  The yard is behind a fuel depot on the north side
b2 20   2541W  The front door of the house on the river is not locked
b2 09   2481W  "Three things," he said from the doorway
b2 26   2416W  The fourth stop is a road with a chemist on the corner
b2 26   2388W  There is no book at the door any more
b2 12   2313W  He went down to the small room at nine with nothing to say
```

Die Liste erzeugt man mit `werkzeug/szenen.py` ueber alle Kapitel.

**Die Kapitel 1 bis 24 stehen in keiner Zielgroessentabelle** - TEIL XII faengt
bei dem an, was heute Kapitel 25 ist. Sie muessen trotzdem durchgegangen werden,
nur ohne Zahl zum Vergleichen.

---

## Kapitel 29, fertig geprueft

Als Muster fuer die Tabelle, die entstehen soll, und weil das Kapitel den
groessten Ueberhang im Band hat.

| # | Tag | W | wofuer sie da ist | Urteil |
|---|---|---|---|---|
| 1 | Mi 3.6. | 1.498 | Uebergabe; Annies dritte Art Schreibtisch; **sein Name als Gefahr**; **die Regel**; **Jang wird eingesetzt** | traegt. Vier davon einmalig im Band, fuenf spaetere Stellen zeigen darauf |
| 2 | Do 4.6. | 2.170 | Notizbuch von Januar an; **die zwei Zeugen**, der Titel; **der Vier-Tage-Befehl** | traegt. Der Fund des Kapitels |
| 3 | Do abends | 100 | Licht unter der Tuer, er klopft | Scharnier |
| 4 | Do nachts | 1.599 | **die Halsbandszene** | traegt. In den Listen namentlich geschuetzt, *bleibt Wort fuer Wort* |
| 5 | Do 1 Uhr | 118 | die **Luecke im Notizbuch am 4. Juni**, die er nie erklaert | Scharnier, und der Beleg fuer Szene 4 |
| 6 | Fr 5.6. | 667 | Sang-hoon; das erste Nein am Telefon; **"Whose four days?"** | traegt |
| 7 | Fr | 331 | Annie beantwortet, wem die vier Tage gehoeren | **schwaechstes Glied**. Das einzige, wo Georgij nur nachtraegt |
| 8 | Fr | 912 | Jang: verschwendet oder ausgibt; Annie dreht es um | traegt. Der Schluss der Kette |

**Kein Ausschuss.** Vier Bewegungen - Uebergabe, Fund, Naehe, Kette. Die Kette
haengt an der Regel aus Szene 1, die Naehe an dem Satz aus Szene 2, und Szene 2
begruendet den Befehl mit Georgijs eigenem Satz aus Szene 1.

---

## Die offene Entscheidung, die dem Autor gehoert

**Kapitel 29 hatte die Datumszeile *Thursday 4 June* zweimal**, als einziges
Kapitel in hundertsiebzehn. Eine Naht aus dem Zusammenlegen von 33 und 35, die
beide diesen Tag erzaehlten. Sie ist am 27.08. zu einem Szenentrenner geworden.

**Das ist der Beweis, dass es nie ein Kapitel war, sondern zwei
aneinandergelegte.** Es liegt bei 7.419 gegen ein Ziel von 2.800 und ueber der
eigenen Spanne von `check.py`. Zwei Wege, und sie schliessen einander aus:

1. **Zurueck in zwei Kapitel teilen.** Zweimal rund 3.700, beide in der Spanne,
   nichts geht verloren. **Preis: die Nummerierung 1 bis 83 verschiebt sich**,
   und die Verweisarbeit vom 27.08. muss noch einmal laufen.
2. **Rund 4.600 herausschneiden.** Geht nur, indem entweder Szene 1 faellt -
   dann verschwinden Annies Regel, Jangs Einsatz und Georgijs Name als Gefahr -
   oder die Vier-Tage-Kette, die das Motiv des Kapitels traegt.

**Dieselbe Frage steht fuer 26, 32 und 35**, und sie ist dort nicht geprueft.
Wer den neuen Auftrag beginnt, sollte sie zuerst stellen: **ist das ein zu
langes Kapitel oder sind es zwei?**

---

## Werkzeuge

| | |
|---|---|
| `werkzeug/plan.py` | **neu am 27.08.** Jedes Kapitel gegen seine Zielgroesse aus TEIL XII |
| `werkzeug/szenen.py` | das Geruest eines Kapitels. **Zum Finden, nicht zum Urteilen** |
| `werkzeug/doppelt.py` | welche Aussage in **zwei Kapiteln** steht. Das richtige Werkzeug fuer Rueckbezuege |
| `werkzeug/doppelt-im-kapitel.py` | Absatzpaare innerhalb eines Kapitels |
| `werkzeug/kontinuitaet.py` | woertlich gleiche Saetze, feste Zahlen, Alter, Wochentage |
| `werkzeug/abendbericht.py` | welcher Schluss bei Annie etwas Neues bringt |
| `werkzeug/check.py` | das Mechanische. Nach **jedem** Schnitt laufen lassen |
| `werkzeug/build.py` | nach jedem Schnitt, erzeugt `paste/`, `read/`, `book-band-N.md` |

**Zwei Fallen im Werkzeug selbst:**

- Ein Schnitt erzeugt neue Fehler. Am 27.08. sind aus vier Kuerzungen zweimal
  Saetze ueber vierzig Woertern entstanden und einmal ein
  **Kontinuitaetsfehler**, den es vorher nicht gab: Sang-hoons Stapellauf wurde
  *"a shed at Yeongjong"* genannt, und Yeongjong ist Chairman Woos Schuppen.
  **`check.py` nach jedem Schnitt, und das Kapitel danach noch einmal lesen.**
- **Der Bash-Wrapper stolpert ueber Python-Heredocs mit Triple-Quotes.**
  Ersetzungsskripte als Datei ablegen und aufrufen, nicht als `<<'PYEND'`
  einspeisen. Und in Suchmustern **gerade** Apostrophe verwenden, der Text hat
  keine typographischen.

---

## Was ausserdem noch offen ist und nichts mit Szenen zu tun hat

- **166 Kapitelverweise** in `doc/` sind nicht nachgezogen, siehe
  `archiv/VERWEISE-OFFEN.md`. Davon 78 blanke `KNN` bis 34, wo das Band nicht
  aus dem Verweis hervorgeht.
- **Die Streichlisten in `CHOI-LISTEN.md` nennen alte Kapitelnummern** in der
  Form *"Kapitel 33"*. Diese Form ist nicht nachgezogen worden. Die Zuordnung
  steht in `archiv/UMNUMMERIERUNG.md`. Die Datei liegt ausserhalb des Repos, in
  `Downloads/`.
