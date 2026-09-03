# Szenenfunktion, Kausalbruecken und Redundanz - Baende 1 bis 3

## Stand und Umfang

- Prueftag: 3. September 2026
- Git-Ausgang nach fuehrendem GitHub-Abgleich: `main` und `origin/main` auf
  `1454473`, Abstand `0/0`
- Kanon nach Umsetzung: Band 1 mit 34 Kapiteln und 100.788 Woertern,
  Band 2 mit 90 Kapiteln und 232.394 Woertern, Band 3 mit 2 Kapiteln und
  4.206 Woertern
- Gesamtumfang: 126 Kapitel, 337.388 Woerter
- Gelesen und gegengeprueft wurden die jeweils hoechsten Fassungen aller drei
  Baende. Band 1 wurde nach Abschluss des Band-2-Durchgangs mit derselben
  Fehlerklasse gegengeprueft.
- Hilfsmittel: `doppelt.py --nester`, `doppelt.py --ketten`,
  `doppelt.py --schwelle 0.7`, `doppelt.py --oeffner`, `heft.py --stellen`,
  `kuerzen.py --kandidaten`, `kuerzen.py --form`, `check.py --echoes`,
  `szenen.py`, Suchlaeufe auf Drucker/Reset/Terminal/Zeitserver.

## Fehlerdefinition und Gegenprobe

Ein sicherer Fehler liegt vor, wenn eine notwendige Kausalbruecke fehlt oder
eine Szene nur eine bereits vollstaendig ausgefuehrte Bewegung wiederholt.
Kein Fehler liegt vor, wenn eine Wiederholung die Ebene wechselt, eine neue
Entscheidung ausloest, ein spaeteres Echo bezahlt oder eine vorher nur
behauptete Tatsache koerperlich macht.

Die Gegenprobe lautete jeweils:

1. Was ist der Ausloeser der Szene?
2. Welche Entscheidung oder Erkenntnis wird in der Szene erzeugt?
3. Welche neue Lage bleibt nach der Szene uebrig?
4. Hat eine scheinbare Wiederholung eine andere Funktion als die erste Stelle?
5. Wird eine Abkuerzung nach der Kuerzung unverstaendlich, zu glatt oder zu
   technisch?

## Sichere Befunde und Umsetzung

### 1. Band 2, Kapitel 15 erklaerte die Listenmaschine zu breit

**Befund.** Die erste Szene von Kapitel 15 war funktional richtig, aber zu
ausfuehrlich. Sie musste nur tragen: Die Katalogseite aus Ulsan fuehrt zur
Mailingliste, die Mailingliste trifft auf Woos Port-Authority-Lunch, daraus
entsteht die Form von drei Namen. Die alte Fassung fuehrte Mapo, Spreadsheet,
Unternehmen ohne Person, Suchdauer und Zwischenurteile einzeln aus und blieb
dadurch laenger in der Maschine als noetig.

**Gegenprobe.** Die Szene bleibt nach der Kuerzung kausal vollstaendig:
Katalogseite in Ulsan -> Mailingliste des Hauses -> Abgleich mit den fuenf
Lunchnamen -> drei Ueberschneidungen -> noch keine Antwort, aber eine Form.
Der Ulsan-Anruf am Nachmittag braucht nur diesen Vorlauf, nicht die ganze
Arbeitsbeschreibung.

**Umsetzung.** Kapitel 15 wurde als `ch15_v1_7_en.md` angelegt. Die Fassung
verdichtet nur den ersten Block; die Telefonszene bleibt unveraendert.

- Build-Kapitelumfang: 1998 -> 1825 Woerter
- `szenen.py`-Prosazaehlung: 1954 -> 1785 Woerter
- Szene 1: 569 -> 400 Woerter
- Szene 2: 1378 Woerter, unveraendert

## Unsichere Befunde

### Drucker, Reset und geloeschte Beweise

Die Erinnerung an geloeschte Druckerbeweise gehoert nicht zum aktuellen Kanon
von Band 1 bis 3. Die Manuskripte enthalten nur harmlose Druckerstellen:
Katalog beim Drucker, ein Raum ueber einer Druckerei, Annies Einladung bei
einem Drucker in Jung-gu. Es gibt in diesen drei Baenden keinen belegten
Strang, in dem Beweise aus Druckern geloescht wurden, damit verschiedene
Maschinen an verschiedenen Tagen wie repariert oder resettet aussehen.

Die naechste Verwandtschaft steht im Plan zu Band 4: Ulsan Main Complex,
Teileausgabe, Tor 4, Lagerterminal, Etikettendrucker, Badgezeiten,
Kamerazeiten, Terminal-Neustart, Zeitserver-Neusetzen und nachgetragene
Freigaben. Dort ist die richtige Lesart nicht "Druckerbeweis geloescht",
sondern: lokale Leitung versucht, widersprechende Systemspuren als harmlose
IT-Stoerungen, Neustarts und Nachtraege zu normalisieren. Diese Linie bleibt
fuer Band 4 brauchbar, aber sie ist kein Kontinuitaetsfehler in Band 1 bis 3.

## Absichtliche Nichtumsetzung

- Band 1, Kapitel 4/5/17 bleibt: Kamera, Bowl und Choi-Echo sind
  Evidenzaufbau, Vertrauensbruch und spaete Auszahlung, nicht dieselbe Szene.
- Band 2, Kapitel 31/32/69 bleibt: Hwang, Jeon und Woo wiederholen nicht die
  gleiche Verhandlung, sondern verschieben Entscheidung, Machtlage und
  institutionellen Preis.
- Band 2, Kapitel 16/70/88 bleibt: Oks Route wird bewusst dreimal anders
  gelesen - Ahnung, Bericht, letzte Abrechnung.
- Band 2, Kapitel 41/48 bleibt: der Einbruch in das Gas-company-System und die
  Choi-Vorbereitung haben unterschiedliche Funktionen.
- Band 2, Kapitel 83/87 bleibt: Das Zertifikat wird zuerst als Serie
  zerstoert und spaeter Annie gegenueber moralisch abgerechnet.
- Band 2, Kapitel 90 bleibt unangetastet. Die Annie-Szene ist eine
  ausdruecklich freigegebene Autorenfassung.
- Band 3, Kapitel 2 bleibt: Die Trauerhalle ist kein Nachklang des Band-2-
  Endes, sondern fuehrt Gong als saubere Gegenmethode ein.
- Moon bleibt unangetastet. Die Autorensperren aus Blickwinkel 2 und 9 wurden
  nicht wieder geoeffnet.

## Begleitdokumente

Aktualisiert wurde `doc/24-pruefblickwinkel.md`: Blickwinkel 11 ist erledigt,
Blickwinkel 12 ist der naechste Durchgang. Lokal bereits veraenderte andere
Dokumente und erzeugte Dateien wurden nicht angefasst.

## Mechanische Pruefung

Die mechanische Pruefung wurde nach der Umsetzung ausgefuehrt:

- `szenen.py 15`: 1785 Woerter, zwei Szenen; Szene 1 400 Woerter, Szene 2
  1378 Woerter
- `check.py`: 126 Kapitel geprueft, zwei bekannte Bestandsfehler in Band 1,
  Kapitel 6 und 12; `check.py --ratchet`: keine neue Verschuldung gegenueber
  der Basislinie
- `zusagen.py --neu`: keine neue faellige Zusage
- Isolierter `build.py`-Lauf: alle 126 Kapitel und Versionskoepfe erfolgreich
  gebaut; Band 1 100.788, Band 2 232.394, Band 3 4.206, gesamt 337.388
  Woerter; die fremden lokalen Ausgabedateien im echten Repo blieben
  unberuehrt

## Naechster Blickwinkel

Nr. 12: **Zusagen, Motive und spaete Auszahlungen**.
