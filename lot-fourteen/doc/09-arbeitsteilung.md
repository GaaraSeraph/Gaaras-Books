# Arbeitsteilung: Stil und Inhalt

Ab dem 24.08. laufen zwei getrennte Sitzungen an diesem Buch. Dieses Dokument
sagt, wer was hat, was schon geprueft ist, und was offen liegt. **Wer eine
Sitzung aufmacht, liest es zuerst und danach `doc/05-continuity.md`.**

---

## Warum getrennt

Der Grund ist Kontext, nicht Ordnung. Ein Kontrolldurchgang braucht das ganze
Buch im Kopf - fuer die vier Durchgaenge am 24.08. wurden alle 44 Kapitel von
Band 2 gelesen und Band 1 quergeprueft. Wer schreibt, braucht `doc/` und die
letzten drei Kapitel und soll nicht mit 98.000 Woertern Altbestand zugeschuettet
werden. `CLAUDE.md` sagt das ohnehin: *"Pruefauftraege an Agenten, fuer alles,
was das ganze Buch auf einmal braucht."*

---

## Wer was hat

| Der Stil-Chat | Der Inhalts-Chat |
|---|---|
| Punkt oder Fragezeichen (`CLAUDE.md`, eigener Abschnitt) | Zeitachse, Kalender, alle Zahlen |
| Das Komma-Mittel (*"Will I," Annie said.*) | Wissens- und Zusagenkette: woher hat eine Figur, was sie sagt |
| Kontraktionen (`doc/01-craft.md`, Abschnitt 2c) | Rueckbezuege und Zeitdeixis in der Rede |
| Satzlaenge, Tics, Erzaehlerformeln, Echos | Kanonfakten: Alter, Dienstzeiten, Daten, das Geburtstagsregister |
| Sprecherkette und Beats (Regel 5) | Widersprueche zwischen Band 1 und Band 2 |
| Absatzbau: zwei Sprecher in einem Absatz, fehlende Trenner | Ob eine Zusage eingeloest wird und eine angekuendigte Faelligkeit kommt |
| Die zwei Trenner: `---` Takt, `* * *` Szene | |

**Dokumente.** `doc/01-craft.md` gehoert dem Stil-Chat. `doc/05-continuity.md`
und `doc/08-decisions.md` gehoeren dem Inhalts-Chat. In `doc/07-next.md`
schreibt der Schreibende vorn (was kommt) und der Pruefende hinten (was offen
blieb).

---

## Schon geprueft am 24.08., Band 2 - nicht zweimal machen

- **Alle 28 Fragezeichen** einzeln gegen die Regel geprueft. Keines sitzt falsch.
  Zwei sind ausdruecklich gedeckt: Sang-hoons *"What do you have?"* (Kapitel 4)
  steht als Musterfall in `CLAUDE.md`, und Mrs Jeons *"Do you understand what you
  have just put on this table?"* (Kapitel 29) markiert der Text selbst als
  Abweichung.
- **98 fragegeformte Repliken mit Punkt** durchgesehen. Vier auf Zeichen
  geaendert, weil der andere in der naechsten Zeile nein sagt: Kapitel 10, 18,
  25 und 26. Dazu Byuns *"What do you want?"* in Kapitel 22.
- **Das Komma-Mittel**: 15 Vorkommen gezaehlt, drei zurueckgenommen, wo es keine
  Abfertigung war (Kapitel 17, 24, 25). **Rund zehn sind die Obergrenze, nicht
  der Anfang einer Gewohnheit.**
- **Kontraktionen**: Band 2 hat keine einzige eigene. Der einzige Treffer ist ein
  Zitat (Kapitel 10) und in `doc/01-craft.md` als Ausnahme verbucht.
- **Sprecherketten und Absatzbau**: Kapitel 36, 42 (zwei Stellen) und 44
  repariert.
- **Trenner**: 32 Szenengrenzen gesetzt, Mechanik in `build.py`, `reader.py` und
  `to_paste`.

---

## Offen fuer den Stil-Chat

1. **Band 1 ist nie durch eine vollstaendige Interpunktionsrunde gegangen.**
   `CLAUDE.md` verbucht eine Zaehlung am 23.08. ueber *"May I"* und drei behobene
   Verstoesse. Das ist eine Stichprobe, keine Pruefung jeder Marke.

2. **Die Kurve, und sie ist die eigentliche Frage.** Fragezeichen je Kapitel, nur
   Kanonfassungen gezaehlt:

   | | je Kapitel |
   |---|---|
   | Band 1, Kapitel 1 bis 16 | 7 bis 18 |
   | Band 1, Kapitel 17 bis 34 | 1 bis 8, fallend |
   | Band 2, 44 Kapitel | 28 insgesamt, also 0,6 |

   Das ist eine Bewegung und kein Fehler - dieselbe Richtung wie die
   Kontraktionen. Aber jemand muss entscheiden, ob die Naehe zu null in Band 2
   gewollt ist oder ob dem Buch die Register verrutscht sind. **Das ist die
   groesste offene Stilfrage und sie gehoert nicht ins Skript.**

3. **Band 1 hat keine Szenengrenzen.** 34 Kapitel, dieselbe Arbeit wie in Band 2,
   dieselbe Quelle: `doc/05-continuity.md` sagt je Kapitel, aus wie vielen Szenen
   es besteht. In Band 2 waren es 32 Grenzen. Ein Automatismus wurde versucht und
   verworfen, er traf vier von vierundvierzig Kapiteln.

4. **94 Fragezeichen-Verdachtsfaelle** meldet `check.py` ueber beide Baende. Jeder
   ist eine Entscheidung und keiner ein Fehler - das Skript entscheidet die
   Machtlage nicht und darf es nicht.

5. **Erzaehlerformeln**: 19 von 78 Kapiteln stehen ueber der Schwelle.
   *"did not soften"* in 23 Kapiteln, *"did not look away"* in 22. Vollstaendig
   mit `python3 check.py --echoes`.

6. **Ermessensfaelle aus dem dritten Durchgang**, bewusst stehengelassen:
   Kapitel 13 Z.212 und Z.230 (Georgij bei Woo, dieselbe Haltung wie bei
   Sang-hoon in Kapitel 4, wo dieselben Fragen Marken tragen), Kapitel 22 Z.156,
   Kapitel 28 Z.236, Kapitel 35 Z.300, Kapitel 8 Z.256, Kapitel 36 Z.234.

7. **Kapitel 23, dritte Szenengrenze.** Die Dokumentation nennt drei Szenen, aber
   die dritte spielt im selben Raum wie die zweite. Gesetzt an Annies *"Now the
   other thing"* - das ist eine Ermessensfrage und gehoert angesehen.

---

## Offen beim Inhalt

Damit der Stil-Chat weiss, was er liegen lassen darf:

- **Band 1 ist inhaltlich noch nie durchgegangen worden.** Die vier Durchgaenge
  vom 24.08. galten Band 2; Band 1 wurde nur dort geprueft, wo Band 2 auf es
  verweist.
- Die zwei alten `check.py`-Fehler in Band 1: *"two languages"* in Kapitel 6,
  *"two sheets"* zweimal in Kapitel 12.
- Drei angekuendigte Rechnungen, die nie kommen, und zwei Quellen, die aufhoeren
  benutzt zu werden - alles in `doc/07-next.md` unter dem Eintrag vom 24.08.

---

## Arbeitsregeln fuer zwei Sitzungen

Am 24.08. sind zwei Sitzungen zusammengestossen, und es lag **an keiner einzigen
Textstelle**. Kollidiert sind nur die erzeugten Dateien, weil jede Sitzung beim
Commit alles neu baut.

1. **Vor jeder Sitzung `git pull --rebase`.**
2. **Wer commitet, baut zuletzt.** Ein Konflikt in einer erzeugten Datei wird nie
   von Hand geloest: `build.py` laufen lassen, `git add`, weiter.
3. **Getrennte Reviere.** Neue Kapitel gehoeren dem Schreibenden, bestehende dem
   Pruefenden.
4. **`doc/05-continuity.md` ist der Uebergabepunkt.** Dort stehen unter
   *"Korrigiert am 24.08."* alle geaenderten Kanonzahlen und das
   Geburtstagsregister. Wer schreibt, liest die Datei zuerst - sonst schreibt er
   gegen einen Stand, den es nicht mehr gibt. Genau so sind Kapitel 43 und 44
   entstanden, mit drei Verweisen auf einen April, den es nicht gab.

---

## Einstieg fuer den Stil-Chat, zum Kopieren

> Du uebernimmst Stil und Interpunktion fuer *Lot Fourteen*. Lies in dieser
> Reihenfolge: `lot-fourteen/CLAUDE.md`, `doc/09-arbeitsteilung.md`,
> `doc/01-craft.md` von vorn bis Abschnitt 2d. Inhaltliche Pruefung machst Du
> nicht - Zahlen, Daten, Wissensketten und Kanonfakten laufen in einer anderen
> Sitzung, und `doc/05-continuity.md` sagt Dir, was dort zuletzt geaendert wurde.
> Faengst Du bei Punkt 2 der offenen Liste an, also bei der Frage, ob die Kurve
> der Fragezeichen gewollt ist, dann bring Zahlen mit und keine Eindruecke.
