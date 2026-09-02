# Figurenstimmen und Machtlage im Dialog - Baende 1 bis 3

## Stand und Umfang

- Prueftag: 2. September 2026
- Git-Ausgang nach fuehrendem GitHub-Abgleich: `main` und `origin/main` auf
  `0095abc`, Abstand `0/0`
- Kanon nach Umsetzung: Band 1 mit 34 Kapiteln und 100.788 Woertern,
  Band 2 mit 90 Kapiteln und 232.568 Woertern, Band 3 mit 2 Kapiteln und
  4.240 Woertern
- Gesamtumfang: 126 Kapitel, 337.596 Woerter
- Gelesen und gegengeprueft wurden die jeweils hoechsten Fassungen aller drei
  Baende sowie `doc/12-stimmen.md` und die aktiven Figurenblaetter.
- Hilfsmittel: `stimmen.py`, `sprechbefehl.py`, `anwesenheit.py`,
  `check.py`, `doppelt-im-kapitel.py` und die manuelle Sprecherzuordnung an
  jeder Fundstelle.

## Fehlerdefinition und Gegenprobe

Ein sicherer Fehler liegt vor, wenn mehrere Figuren denselben generischen
Sprechbefehl verwenden, obwohl Wortwahl, Satzbau, Beruf, Eigeninteresse oder
aktuelle Machtlage ihnen einen anderen Weg an die Auskunft geben. Dasselbe gilt,
wenn Georgij einen Menschen bestellt, obwohl seine gesetzte Stimme die Sache
benennt, oder wenn eine Nebenfigur nur Information abliefert und keinen eigenen
Preis, Zweck oder Widerstand in die Replik bringt.

Die Gegenprobe lautete jeweils:

1. Wer spricht tatsaechlich, auch wenn das Werkzeug an einer Szenenkante einen
   anderen Namen zuordnet?
2. Darf die Figur in dieser Machtlage eine Antwort erzwingen, oder kann sie nur
   Gegenstand, Frist, Preis, Zweck oder Luecke benennen?
3. Welche Maschine setzt `doc/12-stimmen.md` fuer diese Figur?
4. Veraendert der Ersatz Inhalt, Wissen, Entscheidung oder nur den Weg an die
   bereits gesetzte Auskunft?
5. Erzeugt der Ersatz im Kapitel einen neuen Tic, eine Wiederholung oder eine
   falsche Interpunktion?

## Sichere Befunde und Umsetzung

Der unmittelbare Ausgangswert waren 372 mechanische Sprechbefehle. Die
manuelle Zuordnung ergab **94 sichere Verstosse in 37 Kapiteln**:

- Band 1: 2 Stellen in 2 Kapiteln
- Band 2: 90 Stellen in 33 Kapiteln
- Band 3: 2 Stellen in 2 Kapiteln
- Sprecherverteilung: 47 bei Georgij, 47 bei Nebenfiguren

Georgij benennt nun regelmaessig den Gegenstand statt den Menschen: etwa
*"The arithmetic"*, *"What you signed"*, *"The schedule. From you"* oder
*"What you want, then"*. Wo eine Replik keinen eigenen Wert hatte, traegt der
vorhandene Beat oder, einmal in Kapitel 73, ein neuer Beat die Fortsetzung.

Die Nebenfiguren erhalten keinen gemeinsamen Ersatz. Nam Byung-hee zaehlt die
Teile. Mrs Jeon ordnet Name, Woche, Preis und Transaktion. Woo entfernt die
Form einer Antwort. Sim nennt den Preis spaeteren Herausfindens. Baek verlangt
eine Groessenangabe. Hwang arbeitet mit Akte, Kategorie und Raum. Choi setzt
eine Beziehung als bereits erkannt. Mr Ok bindet die Auskunft an das gemeinsame
Ritual an der Wand. Hana sagt, wohin sie die Worte tragen wird.

Geaendert wurden:

- Band 1: `ch07 v6.7`, `ch28 v1.12`
- Band 2: `ch10 v2.6`, `ch15 v1.6`, `ch18 v1.6`, `ch19 v1.12`,
  `ch22 v1.9`, `ch24 v1.6`, `ch27 v4.1`, `ch28 v4.1`, `ch29 v1.4`,
  `ch30 v2.1`, `ch59 v1.16`, `ch60 v1.9`, `ch61 v2.1`, `ch62 v1.5`,
  `ch63 v1.16`, `ch66 v1.5`, `ch68 v3.4`, `ch69 v3.6`, `ch70 v3.4`,
  `ch71 v3.3`, `ch73 v3.7`, `ch74 v3.2`, `ch75 v3.7`, `ch76 v3.5`,
  `ch79 v3.5`, `ch80 v3.5`, `ch81 v3.7`, `ch82 v1.6`, `ch83 v3.8`,
  `ch85 v3.4`, `ch86 v3.26`, `ch87 v3.26`, `ch88 v3.9`
- Band 3: `ch01 v1.6`, `ch02 v1.9`

Es wurde kein neuer Szenentrenner gesetzt. In Kapitel 73 steht ein Beat statt
einer Replik, weil Nam Byung-hee an dieser Stelle gerade keine Erlaubnis
abwartet. Mrs Has Rueckfrage in Kapitel 80 traegt als einzige neue Stelle ein
Fragezeichen; alle anderen Punktsetzungen folgen der bestehenden Machtlage.

## Bewusste Nichtumsetzung und Autorensperren

- Annie und Park Sang-hoon behalten den Sprechbefehl nach der
  Autorenentscheidung vom 26. August. Ihre Machtlage traegt ihn.
- Georgijs *"Say that I am yours"* in Band 2, Kapitel 6 bleibt die gesetzte
  Geluebdeausnahme. Dort wird keine Information verlangt.
- Moons *"Say the rest of it"* in Band 2, Kapitel 67 bleibt auf ausdrueckliche
  Autorenentscheidung unangetastet. Diese Stelle ist eine Autorensperre und
  darf nicht als offener Restfund erneut vorgeschlagen werden.

Nach der Umsetzung meldet `sprechbefehl.py` 278 Stellen. Davon ordnet es 213
direkt Annie oder Sang-hoon zu. Von 53 offenen Zuordnungen gehoeren 52 ebenfalls
ihnen und eine Moon. Von 12 Zuordnungen zu anderen Namen sind elf Fehler der
automatischen Wechselrechnung und eine die Geluebdeausnahme. Damit bleibt kein
freigegebener Befund offen.

## Gegenproben ohne Manuskriptaenderung

- Band 2, Annie und Georgij: keine neu eingefuehrten Kontraktionen; die
  werkzeugseitige banduebergreifende Tic-Ausgabe wurde nicht als lokaler Fund
  missverstanden.
- Sim: Der erste Ersatz verdoppelte zunaechst *"would rather"* in Kapitel 74.
  Die Rueckpruefung fing das ab; die neue Fassung nennt nun den bereits
  bezahlten Preis des spaeteren Herausfindens ohne den Tic zu wiederholen.
- Baek: Die Groessenmaschine bleibt erkennbar, wird in Kapitel 81 aber nicht
  als identische Formel wiederholt.
- Punkt und Fragezeichen: Die vorhandenen Werkzeughinweise wurden gegen die
  aktuelle Machtlage gelesen. Aus ihnen entstand ausser Mrs Has echter
  Rueckfrage kein sicherer Aenderungsbedarf.
- Band 1 und Band 3: Ausser den je zwei umgesetzten Stellen bestand kein
  breiterer Stimmendrift.

## Unsichere Befunde

Keine. Mehrdeutige Werkzeugzuordnungen wurden nicht automatisch umgeschrieben,
sondern an der Szene aufgeloest.

## Begleitdokumente

Aktualisiert wurden `doc/12-stimmen.md` und `doc/24-pruefblickwinkel.md`.
Lokal bereits veraenderte andere Dokumente und erzeugte Dateien wurden nicht
angefasst.

## Mechanische Pruefung

- `sprechbefehl.py`: 372 auf 278, exakt 94 freigegebene Stellen entfernt
- `check.py --ratchet`: keine neue Verschuldung gegenueber der Basislinie
- `zusagen.py --neu`: keine Zusage mit Frist fehlt im Zusagenbuch
- `doppelt-im-kapitel.py`: kein neuer kapitelinterner Satztreffer
- `build.py`: alle 126 Kapitel und Versionskoepfe erfolgreich gebaut
- `git diff --check`: ohne Befund
- Isolierter Build, damit fremde lokale Ausgabedateien unberuehrt bleiben:
  Band 1 100.788, Band 2 232.568, Band 3 4.240, gesamt 337.596 Woerter

## Naechster Blickwinkel

Nr. 10: **Perspektivnaehe und Erzaehlergewissheit**.
