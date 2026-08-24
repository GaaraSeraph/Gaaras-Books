# Arbeitsteilung: Stil und Inhalt

Ab dem 24.08. laufen drei getrennte Sitzungen an diesem Buch. Dieses Dokument
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

1. ~~**Band 1 ist nie durch eine vollstaendige Interpunktionsrunde
   gegangen.**~~ **Erledigt am 24.08.** Alle 235 Marken und 43 Punktfragen von
   Band 1 einzeln gegen die Machtlage geprueft, 37 Stellen gesetzt, 18
   Ermessensfaelle stehengelassen.

   **Und der Grund, warum es so lange keiner gesehen hat:** Die Zaehlung vom
   23.08. lief nur in **eine** Richtung. Alle drei damals behobenen Verstoesse
   waren Punkt-wird-Zeichen bei einer Bitte (*"May I ask you for something."*).
   Die Gegenrichtung - Zeichen-wird-Punkt bei einer Forderung - ist nie gesucht
   worden. Deshalb stand die Bitte-Klasse ueber beide Baende bei 29 zu 2 und die
   nackte Forderung in Band 1 bei 13 zu 1.

2. ~~**Die Kurve, und sie ist die eigentliche Frage.**~~ **Entschieden am
   24.08.: die Regel gilt rueckwirkend ab Kapitel 1.**

   Die Kurve war zur Haelfte kein Stilwille, sondern ungeprueftes Material. Die
   nackte Forderung mit Punkt taucht in Band 1 **erst ab Kapitel 16** auf
   (*"How much."*), danach in 23, 30, 32, 33 und 34 - sieben Stellen, alle
   hinten. Dieselbe Forderung mit Zeichen stand achtzehnmal, ab Kapitel 1.
   **Das ist dieselbe Naht, an der Georgijs Kontraktionen kippen, und sie liegt
   bei Kapitel 16/17.** Das Ohr hat beim Schreiben umgestellt, das Handbuch hat
   die Regel hinterher aufgeschrieben, und niemand hat nach vorn gezogen.

   Nach dem Durchgang steht die Markenquote von Band 1 bei 72 statt 85 Prozent,
   in den Kapiteln 1 bis 16 bei 82 statt 90. **Der Abstand zu Band 2 bleibt
   gross - 72 gegen 24 - und das ist richtig so:** in Band 1 ist Georgij neu und
   fragt fast pausenlos nach oben, in Band 2 hat er Stand und wird gefragt. Die
   Kurve ist also geblieben, aber sie ist jetzt verdient statt ungeprueft.

   Gegen die Grammatik entschieden, und das ausdruecklich: *Frage ist Frage,
   Zeichen dahinter* haette 159 Stellen umgedreht, davon 116 im fertigen Band 2,
   und den Abschnitt *"Punkt oder Fragezeichen"* aus `CLAUDE.md` entfernt.

3. **Band 1 hat keine Szenengrenzen.** Gezaehlt am 24.08.: Band 1 null, Band 2
   sechsunddreissig in vierundzwanzig Kapiteln.

   **Aber die Quelle, die hier stand, gibt es fuer Band 1 nicht.** In der
   Kapitelliste von `doc/05-continuity.md` tragen die Band-2-Zeilen achtundvierzig
   Szenenangaben, die Band-1-Zeilen **zwei**, und eine davon ist Kapitel 5. Es
   ist also nicht dieselbe Arbeit wie in Band 2 und kein Abschreiben von einer
   Liste, sondern Lesearbeit ueber vierunddreissig Kapitel. Ein Automatismus
   wurde versucht und verworfen, er traf vier von vierundvierzig Kapiteln.

4. **94 Fragezeichen-Verdachtsfaelle** meldet `check.py` ueber beide Baende. Jeder
   ist eine Entscheidung und keiner ein Fehler - das Skript entscheidet die
   Machtlage nicht und darf es nicht.

5. **Erzaehlerformeln**, und es ist ein Band-2-Problem: *"did not soften"*
   steht in 18 Kapiteln von Band 2 und in 5 von Band 1, *"did not look away"* in
   16 gegen 6. Zwei, die `check.py` nicht meldet: ***"not going to pretend"***
   steht in Band 1 **kein einziges Mal** und in Band 2 in neun Kapiteln, und
   ***"said it flatly"*** in 24 von 80 Kapiteln, also ueber der Schwelle von 19.
   Vollstaendig mit `python3 check.py --echoes`.

6. **Ermessensfaelle aus dem dritten Durchgang**, bewusst stehengelassen:
   Kapitel 13 Z.212 und Z.230 (Georgij bei Woo, dieselbe Haltung wie bei
   Sang-hoon in Kapitel 4, wo dieselben Fragen Marken tragen), Kapitel 22 Z.156,
   Kapitel 28 Z.236, Kapitel 35 Z.300, Kapitel 8 Z.256, Kapitel 36 Z.234.

7. **Kapitel 23, dritte Szenengrenze.** Die Dokumentation nennt drei Szenen, aber
   die dritte spielt im selben Raum wie die zweite. Gesetzt an Annies *"Now the
   other thing"* - das ist eine Ermessensfrage und gehoert angesehen.

8. **Das Komma-Mittel steht bei 25 und die Obergrenze ist zehn.** Gezaehlt am
   24.08. ueber beide Baende, Aussagen und Imperative herausgerechnet: fuenf in
   Band 1, **zwanzig in Band 2**. Es doppelt sich schon woertlich - *"What are
   you going to do,"* in Band 2, Kapitel 26 und 27, *"When,"* in 24 und 40,
   *"What,"* in 7 und 30. Aus der Ausnahme ist das dritte Register geworden.

9. **Drei mechanische Ausreisser**, jeder genau einmal im ganzen Buch und
   deshalb ohne Urteil entscheidbar: die einzigen Auslassungspunkte
   (`chapters/ch08_v3_5_en.md`, *"...Yes."*), der einzige typografische
   Apostroph (`ch14`, *o'clock*) und das einzige Semikolon (`ch27`).

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

**Aeltere Fassung, vom Stand zweier Sitzungen.** Wo sie dem Abschnitt *"Die
fuenf Regeln"* weiter unten widerspricht, gilt der untere - namentlich bei den
erzeugten Dateien: Regel 2 hier sagt *"wer commitet, baut zuletzt"*, die neuere
Regel 1 sagt, dass Erzeugtes am besten gar nicht mitcommittet wird, weil die
GitHub-Action bei jedem Push ohnehin neu baut.

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

---

## Drei Sitzungen, Stand 24.08.

Seit heute laufen drei: **Schreiben**, **Stil**, **Inhalt**. Dieser Abschnitt
sagt, woran sie sich tatsaechlich stossen und was dagegen hilft. Er ist aus
Schaden geschrieben - an einem Tag mussten drei Rebases von Hand aufgeloest
werden, und zwei Kapitel wurden gegen einen Kanon geschrieben, den es nicht mehr
gab.

### Was wirklich kollidiert

**Nicht die Prosa.** An keiner einzigen Textstelle sind sich zwei Sitzungen in
die Quere gekommen. Kollidiert sind drei Dinge, und alle drei sind loesbar:

1. **Die erzeugten Dateien.** `book-band-1.md`, `book-band-2.md`, `HANDBUCH.md`,
   `MANIFEST.txt`, `BEGEGNUNGEN.md`, `paste/`. Jede Sitzung baut beim Commit
   alles neu, und jeder Neubau beruehrt alle achtzig Kapitel. **Das war die
   Ursache von drei Konflikten an einem Tag.**
2. **Der Kanon.** Wenn die Inhaltssitzung Woos Alter oder Byuns Abgang aendert,
   ist das fuer die Schreibsitzung unsichtbar. Kapitel 43 und 44 sind so
   entstanden - mit drei Verweisen auf einen April, den es nicht mehr gab.
3. **Die Versionsnummern**, und dieser Punkt hat zwei Haelften.

   Die laute Haelfte: zwei Sitzungen setzen dasselbe Kapitel hoch und es
   entstehen zwei Dateien mit demselben neuen Namen. Git kann das nicht
   aufloesen, aber es zeigt es.

   **Die stille Haelfte ist die gefaehrliche, und sie ist am 24.08. passiert.**
   Die Stil-Sitzung hatte Kapitel 1 auf `v6.6` gesetzt, die Inhalts-Sitzung
   unabhaengig davon auf `v6.7`. Beide Dateien liegen nebeneinander, git meldet
   keinen Konflikt, der Merge geht glatt durch - und weil `build.py` immer die
   hoechste Nummer nimmt, verschwindet die Arbeit an `v6.6` aus jeder
   Lesefassung. Die Datei bleibt liegen und sieht heil aus. **Niemand bekommt
   eine Fehlermeldung.** Aufgefallen ist es nur, weil vor dem Push jemand
   nachgesehen hat, was der Fetch mitgebracht hatte.

   Merksatz: **Zwei gleiche Nummern sind ein Konflikt, zwei verschiedene sind
   ein Verlust.**

### Die fuenf Regeln

**1. Nur eine Sitzung committet Erzeugtes - am besten keine.** Die GitHub-Action
baut bei jedem Push auf `main` ohnehin neu und schreibt das Ergebnis zurueck. Wer
lokal baut, um zu pruefen, ist richtig; wer das Ergebnis mitcommittet, erzeugt
den naechsten Konflikt. **Damit faellt Ursache 1 ganz weg.**

**2. `git pull --rebase` vor jeder Sitzung, und nicht nur vor dem Push.** Die
Schreibsitzung liest danach `doc/05-continuity.md`, Abschnitt *"Korrigiert am
..."*. Zwei Minuten, und sie haetten die drei Aprils verhindert.

**3. Kurze Fenster.** Ein Block sind zwei bis drei Kapitel: lesen, reparieren,
Versionen hochsetzen, pushen. Zwischen Pull und Push liegt eine halbe Stunde und
nicht ein Nachmittag. Damit ist Ursache 3 fast ausgeschlossen, weil zwei
Sitzungen selten im selben halben Stunde dasselbe Kapitel hochsetzen.

**4. Ein Kapitel gehoert zur Zeit einer Sitzung.** Stil und Inhalt fassen beide
bestehende Kapitel an - das ist die einzige echte Ueberschneidung. Also nicht
gleichzeitig am selben Band: einer nimmt Band 1, der andere Band 2, oder sie
tauschen blockweise. Die Schreibsitzung faellt aus der Frage heraus, weil sie
neue Dateien anlegt und keine bestehenden aendert.

**Am 24.08. hat diese Regel nicht gehalten**, und zwar ohne boesen Willen: Stil
und Inhalt waren am selben Nachmittag beide in Band 1. Deshalb steht sie hier
mit einer Ergaenzung - **wer einen Band nimmt, schreibt es in `doc/07-next.md`
hinten hin, bevor er anfaengt.** Eine Zeile, mit Datum. Sonst ist die Regel eine
Absichtserklaerung und kein Verfahren.

**5. Ein Arbeitsbaum je Sitzung.** Das ist die Regel, ohne die die anderen vier
nichts wert sind. Am 24.08. liefen zwei Sitzungen in **demselben Verzeichnis**,
und das hat drei Sorten Schaden erzeugt, die alle nach etwas anderem aussahen:

- `MANIFEST.txt` nannte Kapitel, deren Datei die andere Sitzung gerade
  umbenannt hatte. Jedes Auswertungsskript, das der Liste glaubt, faellt darauf
  herein. **Wer den Kanon bestimmt, nimmt die hoechste `chNN_vX_Y_en.md` aus
  dem Verzeichnis und nicht `MANIFEST.txt`.**
- Ein `build.py` der einen Sitzung zog die halbfertigen Kapitel der anderen in
  die erzeugten Dateien.
- Ein Commit der einen Sitzung haette die uncommittete Arbeit der anderen
  mitgenommen, wenn er `git add -A` benutzt haette. Der Hook tut genau das mit
  den erzeugten Dateien.

**Also je Sitzung ein eigener Klon**, zum Beispiel `Gaaras-Books` fuer Inhalt
und `Gaaras-Books-stil` fuer Stil. Das kostet zehn Megabyte und beendet alle
drei Sorten auf einmal. Zwei Sitzungen in einem Verzeichnis sind kein
Sparmodell, sondern ein gemeinsamer Schreibtisch, auf dem beide gleichzeitig
radieren.

### Wenn es doch kollidiert

**Erzeugte Dateien werden nie von Hand aufgeloest.** `build.py` laufen lassen,
`git add`, `git rebase --continue`. Das dauert Sekunden und ist immer richtig,
weil die Dateien aus den Quellen folgen.

**Bei zwei gleichnamigen Kapitelversionen** gewinnt keine automatisch. Beide
Fassungen ansehen, die Aenderungen zusammenfuehren, **eine** neue Nummer
vergeben, und in `doc/05-continuity.md` eintragen, was zusammengelegt wurde.

**Wenn beim Fetch auffaellt, dass drueben schon hoeher gezaehlt wurde**, wird
nicht im geteilten Baum rebast - dort liegt fremde uncommittete Arbeit. Das
Verfahren, das am 24.08. funktioniert hat, in fuenf Schritten:

1. `git worktree add --detach <woanders> origin/main` - ein sauberer Baum,
   ohne den laufenden anzufassen.
2. Die eigenen Aenderungen dort **auf die fremde Fassung neu aufsetzen**, je
   eine Nummer hoeher. Nicht cherry-picken: das legt die eigene, niedrigere
   Nummer daneben und faellt genau in die stille Haelfte von oben.
3. `build.py`, `check.py`, ein Commit, pushen.
4. Im geteilten Baum `git reset --mixed origin/main` und `git checkout --`
   **nur** fuer die eigenen Pfade. Fremde uncommittete Arbeit bleibt unberuehrt.
5. Danach `git status` lesen und pruefen, ob dabei eine fremde Datei aus dem
   Baum gefallen ist. Am 24.08. war es `Choi Gespraech.txt`, und das faellt
   sonst erst auf, wenn es jemand mitloescht.

### Wer schreibt in welches Dokument

| Datei | Sitzung |
|---|---|
| `chapters-2/` neue Kapitel | Schreiben |
| bestehende Kapitel | Stil **oder** Inhalt, nach Regel 4 |
| `doc/01-craft.md` | Stil |
| `doc/05-continuity.md`, `doc/08-decisions.md` | Inhalt |
| `doc/06-plot.md` | Schreiben |
| `doc/07-next.md` | alle drei: Schreiben vorn, Pruefende hinten anhaengen |
| `doc/09-arbeitsteilung.md` | wer die Aufteilung aendert, und zwar bevor er sie aendert |

### Und der Uebergabepunkt

`doc/05-continuity.md` ist die Stelle, an der die drei einander erreichen. Dort
stehen die Kapitelliste, das Geburtstagsregister und die Liste der geaenderten
Kanonzahlen. **Wer etwas am Kanon aendert, traegt es dort ein, bevor er pusht.**
Wer schreibt, liest es, bevor er anfaengt. Alles andere ist Chatverlauf und damit
weg.

---

## Einstieg fuer den Stil-Chat, zum Kopieren

> Du uebernimmst Stil fuer *Lot Fourteen*. **Arbeite in einem eigenen Klon**,
> nicht in dem, in dem eine andere Sitzung laeuft - warum, steht unter Regel 5.
> Lies in dieser Reihenfolge: `lot-fourteen/CLAUDE.md`,
> `doc/09-arbeitsteilung.md`, `doc/01-craft.md` von vorn bis Abschnitt 2d.
> Inhaltliche Pruefung machst Du nicht - Zahlen, Daten, Wissensketten und
> Kanonfakten laufen in einer anderen Sitzung, und `doc/05-continuity.md` sagt
> Dir, was dort zuletzt geaendert wurde. Dein Ressort ist die linke Spalte oben:
> Satzzeichen, Satzlaenge, Tics, Erzaehlerformeln, Echos, Sprecherkette und
> Beats, Absatzbau, die zwei Trenner.
>
> Punkt 1 und 2 der offenen Liste sind erledigt. Die naechstgroessten Hebel sind
> die Erzaehlerformeln in Band 2 (Punkt 5), das Komma-Mittel zurueck auf zehn
> (Punkt 8) und die Szenengrenzen von Band 1 (Punkt 3). Bring Zahlen mit und
> keine Eindruecke - und wenn eine Zahl im Dokument nicht stimmt, zaehl nach und
> schreib sie um. Drei standen hier falsch.
