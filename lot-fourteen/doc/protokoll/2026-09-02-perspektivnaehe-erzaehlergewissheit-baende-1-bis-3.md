# Perspektivnaehe und Erzaehlergewissheit - Baende 1 bis 3

## Stand und Umfang

- Prueftag: 2. September 2026
- Git-Ausgang nach fuehrendem GitHub-Abgleich: `main` und `origin/main` auf
  `0a8837b`, Abstand `0/0`
- Kanon nach Umsetzung: Band 1 mit 34 Kapiteln und 100.788 Woertern,
  Band 2 mit 90 Kapiteln und 232.567 Woertern, Band 3 mit 2 Kapiteln und
  4.206 Woertern
- Gesamtumfang: 126 Kapitel, 337.561 Woerter
- Gelesen und gegengeprueft wurden die jeweils hoechsten Fassungen aller drei
  Baende. Band 3, Kapitel 1 und 2 wurden wegen des Banduebergangs voll gelesen.
- Hilfsmittel: Suchlaeufe auf mentale Zuschreibungen, spaetere Vorausblenden,
  absolute Erzaehlerwoerter, `zuschreibung.py`, `check.py --ratchet`,
  `faktenspur.py`, `doppelt-im-kapitel.py` und `zusagen.py --neu`.

## Fehlerdefinition und Gegenprobe

Ein sicherer Fehler liegt vor, wenn ein naher Absatz ohne Signal allwissend
wird, eine Vermutung grammatisch als Tatsache erscheint oder ein Superlativ
mehr weiss, als der Roman zeigen kann. Kein Fehler liegt vor, wenn der
Erzaehler sichtbar einen Ueberblick setzt, eine spaetere Vorausblende benutzt
oder aus belegten Beobachtungen schliesst.

Die Gegenprobe lautete jeweils:

1. Gehoert der Satz zu Wahrnehmung, Schluss, Erinnerung, Erzaehlerueberblick
   oder Vorausblende?
2. Kann die Figur den behaupteten inneren Zustand, die Vollstaendigkeit oder
   die spaetere Folge in diesem Moment wissen?
3. Ist die Gewissheit im Kanon belegt, oder behauptet der Satz mehr als die
   Szene tragen kann?
4. Wird die Stelle durch ein Signal wie Beobachtung, Notiz, spaeteres Wissen
   oder institutionelle Kenntnis gedeckt?
5. Bleibt nach einer weicheren Fassung derselbe Druck erhalten, ohne Wissen zu
   erfinden?

## Sichere Befunde und Umsetzung

### 1. Choi Dae-hos Beschreibbarkeit war zu absolut

**Befund.** Band 2, Kapitel 85 sagte, das Lesen eines Raums sei das einzige,
was je jemand ueber Choi Dae-ho beschreiben konnte. Das ist als absoluter
Superlativ zu hart: Kapitel 17 hatte bereits acht Zeilen ueber den Mann und
eine ueber seine Methode gesetzt.

**Umsetzung.** Die Stelle bindet den Abstand nun an Georgijs neun Zeilen und
an seine aktuelle Beobachtung, nicht an alles, was je ueber Choi gesagt werden
konnte.

Geaendert: `b2 ch85 v3.5`.

### 2. Choi Dae-hos Lebensgewohnheit wurde zu allwissend behauptet

**Befund.** Band 2, Kapitel 86 sagte, Choi habe in seinem ganzen Leben nie
jemandem in einem fremden Raum etwas angeboten. Das behauptet ungesehene
Privatraeume.

**Umsetzung.** Die neue Fassung bleibt bei Georgijs Kenntnisstand: Nichts, was
er gelernt hat, stellt Choi auf die anbietende Seite eines fremden Tisches.

Geaendert: `b2 ch86 v3.27`.

### 3. Der Trauerhallensatz kann fremde Gesichter nicht vollstaendig wissen

**Befund.** Band 3, Kapitel 2 sagte, Georgij sei der einzige Mann in der Halle,
der sein Gesicht nicht auf Trauer arrangierte. Das legt innere Absicht fuer
alle anderen Maenner in einer neunzigkoepfigen Halle fest.

**Umsetzung.** Die neue Fassung bleibt bei Georgijs eigener Handlung und
entfernt den Anspruch auf das Innenleben der Halle.

Geaendert: `b3 ch02 v1.10`.

### 4. Gong Doo-hyuns Einladung war national zu absolut formuliert

**Befund.** Band 3, Kapitel 2 sagte, alle seien gekommen, weil sie gefragt
wurden, und der Fragende sei der eine Mann in der Republik Korea, der niemandem
etwas geben koenne. Der erste Teil behauptete neunzig Motive; der zweite Teil
setzte einen faktisch fraglichen nationalen Superlativ.

**Umsetzung.** Die neue Fassung haertet den Kern: Sie kamen, als er fragte.
Das ist fuer Gong staerker, weil keine Gegenleistung erklaert werden muss.

Geaendert: `b3 ch02 v1.10`.

## Absichtliche Nichtumsetzung

- Band 1 hat in diesem Durchgang keinen sicheren neuen Befund ergeben.
- Band 2, Kapitel 53 bleibt: Die Ahn-Zuschreibung wird unmittelbar durch ihre
  eigene Erzaehlung getragen und ist kein heimlicher Kopfwechsel.
- Band 2, Kapitel 87 bleibt: Die Perspektive ist bewusst panoramatisch
  signalisiert.
- Band 2, Kapitel 89 bleibt: Die Montage rechnet Rueck- und Vorauswissen
  sichtbar ueber den Erzaehler ab.
- Band 2, Kapitel 90 bleibt unangetastet. Die Annie-Szene ist eine ausdruecklich
  freigegebene Autorenfassung.
- Moon bleibt unangetastet. Die Autorensperren aus Blickwinkel 2 und 9 wurden
  nicht wieder geoeffnet.

## Unsichere Befunde

Keine. Stellen mit starkem Erzaehlerueberblick wurden nicht automatisch
entschaerft, wenn die Prosa ihren Abstand zur Szene sichtbar macht oder der
Kanon die Gewissheit deckt.

## Begleitdokumente

Aktualisiert wurde `doc/24-pruefblickwinkel.md`. Die Regel fuer
Manuskriptaenderungen ist dort jetzt eindeutig: immer erst praesentieren, dann
nach ausdruecklicher Freigabe umschreiben. Lokal bereits veraenderte andere
Dokumente und erzeugte Dateien wurden nicht angefasst.

## Mechanische Pruefung

- `check.py --ratchet`: keine neue Verschuldung gegenueber der Basislinie;
  die zwei bekannten Basisfehler in Band 1, Kapitel 6 und 12 bleiben
  unveraendert
- `zuschreibung.py`: Eichung bestanden, 126 Kapitel, 61 Stellen zum Nachsehen
- `faktenspur.py`: erwartete Bewegungen im letzten Fassungssprung fuer
  `b2 ch85`, `b2 ch86` und `b3 ch02`; die uebrigen Meldungen gehoeren zu
  aelteren letzten Fassungsspruengen im Bestand
- `doppelt-im-kapitel.py`: kein neuer kapitelinterner Treffer
- `zusagen.py --neu`: keine Zusage mit Frist fehlt im Buch
- Isolierter `build.py`-Lauf: alle 126 Kapitel und Versionskoepfe erfolgreich
  gebaut; Band 1 100.788, Band 2 232.567, Band 3 4.206, gesamt 337.561
  Woerter; die fremden lokalen Ausgabedateien im echten Repo blieben
  unberuehrt

## Naechster Blickwinkel

Nr. 11: **Szenenfunktion, Kausalbruecken und Redundanz**.
