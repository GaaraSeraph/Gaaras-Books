# Der Umbau der Ablage, beschlossen am 27.08.

**Der Autor am 27.08.:** *"Das ist chaotisch und sinnlos. Die Inhalte aller
dieser Dokumente sind zum Teil sinnlos verteilt auf verschiedene Dokumente in
einer unverstaendlichen Reihenfolge und Gruppierung. Vieles der docs ist
redundant."*

## Was gemessen wurde, bevor irgendetwas vorgeschlagen wurde

**1. Die Dokumentation war so lang wie der Roman.** `doc/` waren **251.071
Woerter**, das Buch **319.574**. Das erzeugte `HANDBUCH.md` kam mit dem
Register auf **322.283** und war damit **laenger als der Roman selbst**.

**2. Das groesste Objekt im Baum war eine zweite Nacherzaehlung des Buches.**
`doc/05-continuity.md`, Abschnitt *Stand der Kapitel*: **42.576 Woerter unter
einer einzigen H3-Ueberschrift**, 1.586 Zeilen ohne eine Zwischenueberschrift,
von Hand gefuehrt. **Er hoerte bei Band 2, Kapitel 45 auf. Das Buch hat 90.**

**3. Niemand wusste, wie viele Dokumente es gibt.** `doc/00-readme` sagte *"die
acht Quelldokumente"*. `CLAUDE.md` sagte an einer Stelle *"die zehn
Quelldokumente"* und druckte eine Tabelle mit vierzehn. `HANDBUCH.md` sagte
achtzehn. `MANIFEST.txt` sagte neunzehn. **Vier Zahlen an vier Stellen, alle
falsch ausser einer.** Das passiert nur, wenn von Hand gezaehlt wird.

**4. Kein Dokument hatte Vorrang.** *Sim* stand in **11 von 18** Dokumenten,
*Halsband* in 10, *Fragezeichen* in 8. Eine allgemeine Vorrangregel gab es
nicht, nur drei einzeln ausgehandelte. Als `doc/16` und `CLAUDE.md` sich bei
den Fragezeichen widersprachen, musste das ueber **200 Zeilen in `doc/07`**
ausgefochten werden, weil kein Satz irgendwo sagte, wer gewinnt.

**5. Rund 93.000 Woerter waren Sitzungsprotokoll oder Nacherzaehlung**, also
37 Prozent: `doc/14` ganz (19.919), der datierte Schwanz von `doc/07`
(13.386), von `doc/05` (6.279), von `doc/15` (5.597), dazu `doc/16`, die
datierten Eintraege in `doc/08` und der Kapitelindex.

## Die Diagnose, und sie ist eine einzige

**Die Dokumente waren nach Thema benannt und nach Datum gewachsen.** Jedes fing
als Sachdokument an und wurde zum Sitzungstagebuch ueber sein Thema. Deshalb
stand die Sache unter ihrer eigenen Geschichte begraben, und deshalb las sie
niemand mehr.

Das war kein Ordnungsproblem, sondern ein **Ablageproblem: es gab keine Regel,
wo ein neuer Satz hingehoert.** Wer etwas Neues hatte, haengte es unten an oder
legte ein neues Dokument an.

**Das war der zweite Anlauf.** `build.py` haelt fest, dass die Ablage schon
einmal umgebaut wurde, von `canon/ craft/ log/ plot/` plus einer *story-bible*
auf `doc/01` bis `doc/08`. Danach sind zehn weitere Dokumente danebengewachsen,
**weil keine Regel sagte, wohin sie gehoeren.** Genau das soll diesmal nicht
wieder passieren, und dafuer sorgt Schritt 6, nicht der Umbau selbst.

**Und es hat Geld gekostet.** Der Sechs-Zuege-Plan fuer den Schluss von Band 2
stand in einem Dokument namens *"Naechste Schritte"*. Ein Plan unter diesem
Namen wird ueberflogen. Unter *Kanon* wird er gelesen.

## Was der Umbau technisch vorfand, und es war besser als befuerchtet

- **Die Verweise sind sauber.** Alle Querverweise auf `doc/NN` stehen
  ausschliesslich in `doc/`, `CLAUDE.md` und `werkzeug/*.py`. **In den Kapiteln
  steht kein einziger**, in den Hooks auch nicht, und es gibt keine
  zeilengebrochenen. Das sind **318 Ersetzungen**, vollstaendig skriptbar.
- **`build.py` hat einen Verweispruefer** (`warn_dead_refs`, Zeile 190). Der
  Umbau ist damit **nachweisbar vollstaendig**, nicht nur hoffentlich.
- **Nur drei Werkzeuge kennen einen Dateinamen wirklich:** `anwesenheit.py` →
  `doc/12`, `zusagen.py` → `doc/13`, `check.py` → `doc/05`. Alles andere sind
  Kommentare.

Daraus folgt eine Nummernvergabe, die Arbeit spart: **`10-naehe`, `12-stimmen`
und `13-zusagen` behalten ihre Nummer.** Das sind **77 der 318 Verweise, die
nie angefasst werden, und zwei der drei Werkzeugpfade.** Der Preis ist, dass
die Nummern innerhalb eines Blocks keine Lesereihenfolge sind. Die
Lesereihenfolge steht in `00-readme`, wo sie hingehoert.

## Der Zielbaum

**Die Zehnerstelle ist die Sorte. Jeder Block hat Platz, damit nichts wieder
umsortiert werden muss.**

| | Datei | Inhalt | kommt aus |
|---|---|---|---|
| **0x** | `00-readme.md` | eine Seite, Zahl der Dokumente **erzeugt** | 00 |
| **1x Kanon** | `10-naehe.md` | **unveraendert** | 10 |
| | `11-figuren.md` | Praemisse, die zwei Leads, der ganze Cast | 02 + 03 |
| | `12-stimmen.md` | **unveraendert**, Korrekturen eingearbeitet | 12 + Korrekturteile 14 |
| | `13-zusagen.md` | **unveraendert** | 13 |
| | `14-welt.md` | Haus, Haushalt, Geschaeft, Geld, die Macht-Regel | 04 |
| | `15-kalender.md` | Jahr, Kalender, Tage, Geburtstage, Alter, Fahrerwoche | 05, Zeitteil |
| | `16-motive.md` | wiederkehrende Bilder, festgelegte Zeilen, die Wut | 05, Textteil |
| | *17 bis 19 frei* | | |
| **2x Regeln** | `20-handwerk.md` | alle Schreibregeln, **eine Stelle** | 01 + Regelteile 14/16 |
| | `21-figurenbau.md` | wie man eine Figur baut, buchunabhaengig | 17 |
| | `22-pruefen.md` | Pruefverfahren und Arbeitsteilung | 11 + 09 |
| | *23 bis 29 frei* | | |
| **3x Plan** | `30-plan-band-1.md` | die Stoffbloecke, **abgeschlossen markiert** | 06 |
| | `31-plan-band-2.md` | Ziel, die sechs Zuege, Reihenfolge, offene Faeden | 07, Planteil |
| | `32-plan-band-3.md` | was uebergeht, Los elf | 07, Band-3-Teil |
| | *33 ff. frei fuer Band 4* | | |
| **4x** | `40-verworfen.md` | was schon abgelehnt wurde, damit es nicht wiederkommt | 08, Verwurfteil |
| **Archiv** | `protokoll/*.md` | alles Datierte, append-only, **nicht im Handbuch** | 14, 16, die Schwaenze |

**Fuenfzehn Dateien statt achtzehn**, plus dieses Verzeichnis. `doc/05` wird
geteilt, weil Kalender und Motive zwei Fragen sind und wer das eine
nachschlaegt sonst durch das andere blaettert.

**Der Uebergabestoff** (*Was Band 2 mitbekommt*, *Der Zustand am 1. Maerz*)
kommt in den Plan des **empfangenden** Bandes, nicht des abgebenden. Wer ihn
braucht, sucht ihn dort.

## Die drei Entscheidungen des Autors, 27.08.

1. **Der Kapitelindex wird eingedampft und erzeugt** (Variante a von dreien).
2. **Es wird umnummeriert**, nicht nur verschoben.
3. **`doc/08-decisions` wird aufgeloest.** Eine getroffene Entscheidung ist
   danach entweder Kanon oder Regel und gehoert dorthin. Uebrig bleibt das
   Verworfene, und das ist kurz und wirklich noetig.

Dazu die Auflage: **auch Band 1 bekommt einen Planslot**, damit die Ablage
nicht ein zweites Mal umsortiert werden muss.

## Die sieben Schritte

### Voraussetzung

**Der Umbau laeuft in einer Sitzung, allein im Repo.** Andere Chats schreiben
in `doc/07` und `doc/15`, waehrend daraus Abschnitte herausgetrennt werden. Ein
Merge-Konflikt in einer Datei, die gerade zerlegt wird, ist nicht aufloesbar.

### Schritt 1 · Sicherung  **[ERLEDIGT]**

`doc/` vollstaendig und wortgleich nach `protokoll/2026-08-27-ablage-vorher/`.
Achtzehn Dateien, byteweise geprueft, 251.071 Woerter. **Ab hier ist nichts
mehr verlierbar, nur noch verschiebbar.**

### Schritt 2 · Das Protokoll ausziehen, vor allem anderen

Zuerst raus, was reine Sitzungsgeschichte ist. Danach sind die verbleibenden
Dokumente klein genug, um sie ueberhaupt zu beurteilen.

| nach `protokoll/` | Umfang |
|---|---|
| `2026-08-stil.md` ← `14-stilprotokoll` ganz | 19.919 W |
| `2026-08-inhalt.md` ← die datierten Schwaenze von `07`, `05`, `15` | 25.262 W |
| `2026-08-regelaenderungen.md` ← `16` ganz | 3.019 W |

**Regel fuer den Schnitt:** eine Ueberschrift mit Datum darin und
Vergangenheitsform gehoert ins Archiv. **Ausnahme:** Regeln, die in einem
datierten Abschnitt *beschlossen* wurden, bleiben als Regel zurueck und wandern
nach `20-handwerk`. Das betrifft vor allem `doc/16` Abschnitte A und B.

**Pruefung:** vorher und nachher summieren sich auf 251.071.

### Schritt 3 · Die 42.576 Woerter, und das ist die einzige gefaehrliche Stelle

Der Kapitelindex ist kein Muell. Er enthaelt echten Kanon in Nacherzaehlung
eingebettet, zum Beispiel die Festlegung vom 23.08. zu *"I'm afraid of
Tuesdays"*. **Ihn abzuschneiden wuerde Entscheidungen vernichten.**

**3a. Erzeugen, was erzeugbar ist.** `build.py` bekommt `erzeugt/KAPITEL.md`,
eine Zeile je Kapitel aus dem Kapitelkopf und dem Manifest:

```
- **B2 45** *The line above it* (v1.1) · Tag 279 · Do 9. Juli · 3.041 W
```

Nummer, Titel, Fassung, Tag, Datum und Laenge stehen alle im Kapitelkopf.
**Damit ist die Versionsdrift fuer immer erledigt**, und `check.py`s
`chapter_state` wird ueberfluessig: sie kann heute ohnehin nur Versionsnummern
nachziehen und meldete am 22. August siebzehn veraltete Zeilen.

**3b. Sieben, nicht kuerzen.** Jeder Satz bekommt eine Frage: **koennte morgen
ein Kapitel falsch geschrieben werden, wenn dieser Satz fehlte?**

- **Ja** → Kanon, wandert nach `15-kalender` oder `16-motive`, **unter sein
  Thema, nicht unter seine Kapitelnummer.**
- **Nein** → Nacherzaehlung. Das Buch steht daneben.

Die Liste der Saetze, die als Kanon bleiben sollen, geht **vor dem Eingriff**
an den Autor. Geschaetzt achtzig bis hundertzwanzig.

**3c. Der Rest wird nicht geloescht.** Der ganze alte Block liegt wortgleich in
`2026-08-27-ablage-vorher/`.

### Schritt 4 · Zusammenlegen und umnummerieren

Erst jetzt, wenn die Dokumente auf ihre Sachhaelfte geschrumpft sind, werden
sie bewegt. Je Zieldatei ein Skript: Abschnitt am Ueberschriftenanker
schneiden, `assert` dass er gefunden wurde, anhaengen, **erst danach** aus der
Quelle entfernen. **Kein Loeschen vor einer bestaetigten Ankunft.** `git mv`
fuer die Dateien, die nur die Nummer wechseln, damit die Geschichte mitkommt.

### Schritt 5 · Der Verweis-Sweep

Zuordnungstabelle alt → neu, skriptiert ueber `doc/*.md`, `CLAUDE.md`,
`werkzeug/*.py`. **318 Ersetzungen**, dazu die drei Werkzeugpfade von Hand, von
denen zwei sich nicht aendern, und eine Handvoll Prosastellen, die keine Links
sind (etwa `doc/14:1064`, *"Aus dem doc/12-Durchgang"*).

**Pruefung:** `python3 build.py` meldet **null tote Verweise.**

### Schritt 6 · Die drei Saetze, die verhindern, dass es wiederkommt

Ganz oben in `CLAUDE.md`, vor allem anderen:

1. **Wohin ein neuer Satz gehoert**, entschieden an seiner Zeitform: Praesens
   ueber die Fiktion → Kanon. Imperativ → Regel. Futur → Plan des Bandes.
   Vergangenheit mit Datum → `protokoll/`.
2. **Wer gewinnt beim Widerspruch:** Kanon vor Regel vor Plan. **Protokoll
   gewinnt nie.**
3. **Kein neues Dokument ohne Block.** Wer etwas anzulegen hat, das in keinen
   Block passt, hat es falsch verstanden.

Dazu eine Pruefung in `check.py`, weil ein Satz allein nichts haelt: **eine
datierte Ueberschrift in einer Datei aus 1x, 2x, 3x oder 4x ist ein Befund.**
Meldet, blockiert nicht.

### Schritt 7 · `00-readme` und die Zahl

Die Zahl der Dokumente wird von `build.py` geschrieben, nicht getippt.

## Was danach anders aussieht

| | vorher | nachher |
|---|---|---|
| Dokumente | 18 | 15 plus Archiv |
| `doc/` Woerter | 251.071 | rund 150.000 |
| `HANDBUCH.md` | 322.283 W, **laenger als der Roman** | rund 155.000 |
| Kapitelindex | 42.576 W von Hand, endet bei B2 K45 | erzeugt, 116 Zeilen, nie veraltet |
| Vorrang bei Widerspruch | ungeregelt | drei Zeilen, von `check.py` gestuetzt |

## Was der Umbau ausdruecklich nicht tut

- **Kein Satz wird umformuliert.** Verschieben, nicht neu schreiben.
- **`doc/12-stimmen` wird inhaltlich nicht angefasst**, ausser dass die
  dreiundzwanzig Korrekturen aus `doc/14` dort eingearbeitet werden, wo sie
  hingehoeren. Bisher stand die Korrektur in einer anderen Datei als das
  Korrigierte.
- **Nichts am Buch.**
