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

**`doc/13-zusagen.md` gehoert allen dreien und ist am 25.08. entstanden**, nachdem
der Pruefer zwei ueberfaellige Zusagen gefunden hatte, die beide im Text standen
und in keiner Liste: die fuenf Firmen aus Kapitel 12 (vier Monate erzaehlte Zeit)
und Annies *"You will in about a month"* aus Kapitel 5 (sechs Monate). Beide sind
in Kapitel 69 bezahlt.

**Der Ablauf ist ab jetzt:** wer ein Kapitel schreibt, laeuft danach
`python3 werkzeug/zusagen.py --neu` und traegt ein, was neu versprochen wurde.
Wer prueft, laeuft `zusagen.py` ohne Argument und sieht, was ueberfaellig ist.
**Beim ersten Lauf standen dort sofort zwei weitere Faelle**, die keiner von uns
gefunden hatte: Mrs Jeons vier Monate Geld aus Kapitel 32 und Annies
Wochen-Vorhersage aus Kapitel 59.

**`doc/12-stimmen.md` gehoert allen dreien.** Neu am 25.08., nach dem Befund des
Autors: *"Die Charaktere sind sehr austauschbar. Ausser mit Annie sind alle
Dialoge gleich."* Nachgemessen und bestaetigt: sieben Sprecher liegen zwischen
6,8 und 8,4 Woertern mittlerer Satzlaenge, und in 240.000 Woertern steht **kein
einziges Ausrufezeichen**. Das Dokument haelt je Figur die rhetorische Maschine,
das eigene Anliegen und die fuenf Haustics fest, die Georgij gehoeren.

**Fuer den Stil-Chat stehen dort zwei Praezisierungen, die er braucht:** die
Punkt-oder-Fragezeichen-Regel gilt fuer **Machttransaktionen** und nicht fuer
Geplauder - wer die soziale Frage einer Nachbarin auf einen Punkt korrigiert,
macht sie wieder zu Georgij. Und die Vierzig-Wort-Grenze ist fuer Georgijs
Register gebaut; unterhalb davon liegt Faktor vier ungenutzt.

**`doc/10-naehe.md` gehoert allen dreien.** Neu am 25.08. Es ist das Register
jeder koerperlichen Szene zwischen Annie und Georgij, chronologisch, mit der
Zeile, die tatsaechlich im Buch steht: der Boden, die Hand im Haar, der Nacken
und das Halsband, die kleinen Dinge, die drei grossen Szenen. Anlass waren vier
Rueckverweise in der Kette, die sich gegenseitig widersprachen (Kapitel 30, 35
und 55, alle am 25.08. korrigiert). **Wer eine Beruehrung schreibt oder prueft,
greift sie dort und zaehlt dort, und traegt eine neue im selben Commit nach.**

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

3. ~~**Band 1 hat keine Szenengrenzen.**~~ **Erledigt.** Vierundfuenfzig
   Grenzen in dreissig von vierunddreissig Kapiteln.

   Dichte zum Vergleich: Band 1 steht danach bei 1,59 Grenzen je Kapitel und
   0,53 je tausend Woerter, Band 2 bei 1,72 und 0,71. Band 1 ist also eher
   zurueckhaltend gesetzt und laesst sich leichter nachschaerfen als
   zurueckbauen. Ohne Grenze bleiben vier Kapitel: 2 und 11 sind je eine
   durchgehende Autofahrt, 14 und 27 teilen ueber Tageszeilen.

   **Wie es ging, und das ist der Teil, der beim naechsten Mal Zeit spart:**
   der Trenner stand ueberall schon da. Es war keine Frage, wo etwas
   eingefuegt wird, sondern welcher der 630 Takt-Trenner in Wahrheit ein
   Orts- oder Zeitwechsel ist. Ein Filter auf Zeit- und Ortsangaben hinter dem
   Trenner hat 148 Verdachtsfaelle geliefert und dabei die Ankunft in Kapitel 7
   uebersehen, weil *carpet* nicht in der Wortliste stand - **also am Ende alle
   630 einzeln angesehen.**

   **Und die Quelle, die hier stand, gibt es fuer Band 1 nicht.** In der
   Kapitelliste von `doc/05-continuity.md` tragen die Band-2-Zeilen achtundvierzig
   Szenenangaben, die Band-1-Zeilen **zwei**, und eine davon ist Kapitel 5. Es
   ist also nicht dieselbe Arbeit wie in Band 2 und kein Abschreiben von einer
   Liste, sondern Lesearbeit ueber vierunddreissig Kapitel. Ein Automatismus
   wurde versucht und verworfen, er traf vier von vierundvierzig Kapiteln.

4. **94 Fragezeichen-Verdachtsfaelle** meldet `check.py` ueber beide Baende. Jeder
   ist eine Entscheidung und keiner ein Fehler - das Skript entscheidet die
   Machtlage nicht und darf es nicht.

5. **Erzaehlerformeln.** *"did not soften"* und *"did not look away"* sind
   **in Band 2, Kapitel 1 bis 34 erledigt** (24.08., 39 Stellen: 25
   zusammengelegt, 10 neue Beats, 2 im Erzaehltext, 2 behalten). Beide stehen
   danach unter der Schwelle und fallen aus dem Bericht.

   **Offen bleiben zwei, die `check.py` nicht meldet:** ***"not going to
   pretend"*** steht in Band 1 **kein einziges Mal** und in Band 2 in neun
   Kapiteln, und ***"said it flatly"*** in 24 von 80 Kapiteln. Vollstaendig mit
   `python3 werkzeug/check.py --echoes`.

6. **Ermessensfaelle aus dem dritten Durchgang**, bewusst stehengelassen:
   Kapitel 13 Z.212 und Z.230 (Georgij bei Woo, dieselbe Haltung wie bei
   Sang-hoon in Kapitel 4, wo dieselben Fragen Marken tragen), Kapitel 22 Z.156,
   Kapitel 28 Z.236, Kapitel 35 Z.300, Kapitel 8 Z.256, Kapitel 36 Z.234.

7. **Kapitel 23, dritte Szenengrenze.** Die Dokumentation nennt drei Szenen, aber
   die dritte spielt im selben Raum wie die zweite. Gesetzt an Annies *"Now the
   other thing"* - das ist eine Ermessensfrage und gehoert angesehen.

8. **Das Komma-Mittel, und warum die Obergrenze zehn nicht stimmt.** Gezaehlt
   am 24.08. ueber beide Baende, Aussagen und Imperative herausgerechnet: 25
   Vorkommen, fuenf in Band 1 und zwanzig in Band 2.

   **Sechs davon sind aufgeloest** (Kapitel 12, 15, 20, 21, 24, 27 von Band 2).
   Wo der Sprecher aus dem Umfeld ohnehin eindeutig ist, faellt der Begleitsatz
   weg und es bleibt die nackte Forderung mit Punkt stehen, was die Hausform
   ist: aus *"What do I get," she said.* wird *"What do I get."* Dazu eine
   Umformulierung, weil *"What are you going to do,"* in Kapitel 26 aus
   Sang-hoons Mund und zwei Kapitel spaeter identisch aus ihrem kam.

   **Die uebrigen neunzehn bleiben, und der Grund gehoert ins Dokument:** Das
   Komma-Mittel ist keine Stilmarotte, es ist **der mechanische Preis des
   Punkt-Registers.** Eine Forderung traegt einen Punkt. Ein kleingeschriebener
   Redebegleitsatz vertraegt keinen Punkt vor sich. Wo also eine Forderung einen
   Begleitsatz braucht - weil kein Nachbarabsatz den Sprecher nennt -, gibt es
   genau drei Moeglichkeiten, und zwei davon sind schlechter:

   - Begleitsatz weglassen: der Sprecher wird unklar.
   - Fragezeichen setzen: die Regel aus `CLAUDE.md` bricht.
   - Komma setzen: das Mittel.

   **Je konsequenter das Punkt-Register laeuft, desto oefter kommt das Mittel
   also vor. Die Zahl zehn war eine Schaetzung aus der Zeit, als beides noch
   nicht zusammengedacht war.** Was bleibt, ist die woertliche Dopplung als
   Pruefpunkt: dieselbe Forderung aus zwei Muendern in benachbarten Kapiteln ist
   ein Fund, neunzehn Vorkommen ueber achtzig Kapitel sind keiner.

9. **Drei mechanische Ausreisser**, jeder genau einmal im ganzen Buch und
   deshalb ohne Urteil entscheidbar: die einzigen Auslassungspunkte
   (`chapters/ch08_v3_5_en.md`, *"...Yes."*), der einzige typografische
   Apostroph (`ch14`, *o'clock*) und das einzige Semikolon (`ch27`).

10. **Der Takt-Trenner ist keine Marke mehr.** Gezaehlt am 24.08. ueber den
    ganzen Kanon:

    | | Absaetze je Kapitel | Takt-Trenner je Kapitel | ein Trenner je |
    |---|---|---|---|
    | Band 1 | 143 | 16 | **8,5 Absaetze** |
    | Band 2, Kapitel 1 bis 34 | 101 | 53 | **1,9 Absaetze** |
    | Band 2, Kapitel 35 bis 56 | 100 | 90 | **1,1 Absaetze** |

    In Kapitel 50, 52 und 53 stehen 92 Trenner auf 94 Absaetze. **Ein Zeichen,
    das zwischen fast allem steht, unterscheidet nichts mehr.**

    **Und es ist nicht nur die Quelle.** `build.py` macht aus jedem `---` in der
    Einfuegefassung ein `* * *`. In `paste/band-2/ch52` steht damit ein
    Szenentrenner zwischen jeder einzelnen Replik - und die Einfuegefassung ist
    die, die auf die Plattform geht. Die HTML-Lesefassung desselben Kapitels hat
    zweiundneunzig `<hr>`.

    **Entschieden und erledigt am 25.08.** Der Autor hat die Entscheidung
    abgegeben (*"ist mir relativ egal, es muss halt gut sein"*), also steht
    hier, wie sie gefallen ist und woran.

    **Die Regel kam nicht aus dem Kopf, sondern aus Band 1.** Gemessen, an
    welcher Grenze ein Trenner steht:

    | vor einer Replik | Band 1 | Band 2 |
    |---|---|---|
    | Rede - Rede | 6 % | 68 % |
    | Erzaehlung - Rede | 8 % | 85 % |
    | Beat - Rede | 3 % | 80 % |

    | nach einer Replik | Band 1 | Band 2 |
    |---|---|---|
    | Rede - Erzaehlung | 35 % | 98 % |
    | Rede - Beat | 36 % | 99 % |

    **Band 1 waehlt, Band 2 nicht.** Bei achtzig bis neunundneunzig Prozent ist
    der Trenner kein Mittel mehr, sondern Zeichensetzung. Und die zwei hoechsten
    Werte von Band 1 stehen beide **hinter** einer Replik, die drei niedrigsten
    **davor**. Daraus die Regel, positiv:

    > **Der Takt-Trenner markiert die Stille nach einem Satz, nicht den Anlauf
    > zu einem. Er steht hinter einer Replik, nie unmittelbar davor.**

    **2742 Trenner entfernt, in allen 68 Kapiteln von Band 2.** Band 2 steht
    danach bei **einem je 3,1 Absaetzen** statt 1,4. Keine Prosa angefasst -
    `faktenspur.py` meldet null bewegte Zahlen, und der Unterschied zwischen
    alter und neuer Fassung sind ausschliesslich Leerzeilen.

    **Band 1 bleibt unangetastet, und das ist kein Versehen.** Dort stehen 145
    Trenner vor einer Replik, bei drei bis acht Prozent - also gewaehlt, und
    jeder von ihnen ist ein Themenwechsel: *"That one you may thank me for." /
    --- / "There is a second thing and it is smaller."* **Die Regel verbietet
    die Automatik, nicht die Wahl.**

    **Was bleibt und bewusst bleibt:** Band 2 steht bei 3,1 gegen Band 1s 8,4.
    Die restlichen Trenner sitzen alle hinter einer Replik oder zwischen zwei
    Erzaehlabsaetzen - also an Band 1s bevorzugten Stellen, nur dichter. Das ist
    eine andere Textur und kein Fehler mehr: Band 2 hat mehr Szenen, mehr
    Personen und kuerzere Beats. **Wer es weiter zurueckbauen will, muss lesen
    und nicht rechnen** - die verbleibenden 2220 sind nicht mehr mechanisch
    trennbar.

11. **Der Ton-etikettierende Beat, und das ist der grosse offene Posten.**
    Gezaehlt am 24.08. Die beiden Formeln aus Punkt 5 sind nicht die Krankheit,
    sondern zwei Mitglieder einer Familie: **ein eigener Satz, dessen einzige
    Aufgabe es ist, den Ton der eben gesprochenen Replik zu etikettieren.**

    | | |
    |---|---|
    | Vorkommen ueber beide Baende | **347** |
    | verschiedene Wendungen dafuer | **259** |
    | davon mit Sprecher davor | 243, also **3,7 je Kapitel in Band 1** und 2,5 in Band 2 |

    Die haeufigsten: *said it* (19), *did not soften it* (19), *said it flatly*
    (13), *said it plainly* (9), *said it perfectly evenly* (6), *said it out
    loud* (5).

    **Warum nie etwas angeschlagen hat:** `check.py` vergleicht Zeichenketten.
    259 Wendungen fuer einen Griff heissen, dass keine einzelne je eine Quote
    reisst. Es ist dieselbe Luecke, die `doc/01-craft.md` fuer *did not soften*
    beschreibt, nur eine Ebene hoeher - **nicht eine wiederholte Formel, sondern
    ein wiederholter Zug.**

    **Und es ist kein Altbestand.** In `ch40_v2_0` und `ch42_v2_0`, beide am
    24.08. geschrieben, steht er weiter: *"Jang said it without any
    defensiveness in it at all."*, *"He said it flatly."*, *"Georgij said it
    evenly."* Band 1 ist sogar dichter als Band 2. Das ist der Standard-Beat des
    Buchs, und die Schreibsitzung reproduziert ihn gerade weiter.

    **Dieselben Kapitel zeigen aber auch, was stattdessen geht** - klein,
    koerperlich, mit einem Gegenstand, der in der Szene schon liegt: *"Jang
    tapped the map once."*, *"He held up a second finger."*, *"He kept his hands
    flat on the desk."*, *"Georgij put one finger on the cloth and took it away
    again."*

    **Was zu entscheiden ist, und es ist keine Reparatur mehr, sondern eine
    Stilfrage:** ob eine Quote gilt, etwa hoechstens zwei je Kapitel. Das waeren
    rund 50 Eingriffe in Band 2 und 70 in Band 1, und es veraendert die
    Erzaehlstimme hoerbar. Deshalb steht es hier und ist nicht nebenbei gemacht
    worden.

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

1. **Die erzeugten Dateien.** `book-band-1.md`, `book-band-2.md`, `erzeugt/`
   (HANDBUCH, BEGEGNUNGEN, MANIFEST) und `paste/`. Jede Sitzung baut beim Commit
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
3. `werkzeug/build.py`, `werkzeug/check.py`, ein Commit, pushen.
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
| `doc/13-stilprotokoll.md` | **Stil**, waehrend des Durchgangs. Die Inhaltspruefung liest nur |
| `doc/11-pruefen.md` | wer prueft, und zwar sofort nachdem er etwas gelernt hat |
| `doc/09-arbeitsteilung.md` | wer die Aufteilung aendert, und zwar bevor er sie aendert |

### Und der zweite Uebergabepunkt: das Stilprotokoll

Seit dem 25.08. gibt es `doc/13-stilprotokoll.md`. **Ein Durchgang, der jede
Aussage an `doc/12-stimmen.md` anpasst, schreibt woertliche Rede um, und in
woertlicher Rede stehen die Fakten.** Ohne Protokoll muesste die
Inhaltspruefung danach hundert Kapitel neu lesen; mit Protokoll liest sie die
Zeilen, die sich bewegt haben.

Die Reihenfolge ist **erst Stil, dann Inhalt** - die Begruendung steht in
`doc/11-pruefen.md`. Kurz: wer zuletzt schreibt, hat recht, und das soll der
Inhalt sein; Befunde gegen einen Wortlaut, den es nicht mehr gibt, sind wertlos;
und Warten kostet nichts, weil das Archiv jede Fassung behaelt.

---

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
