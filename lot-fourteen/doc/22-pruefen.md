# Pruefen und Arbeitsteilung

*Regel. Wie geprueft wird und wer was prueft.*

Zusammengelegt am 27.08. aus `11-pruefen` (das Verfahren), `09-arbeitsteilung`
(wer welchen Teil prueft) und dem Regelkopf von `14-stilprotokoll` (was
gemeldet wird). **Das waren drei Dokumente ueber dieselbe Frage.** Die
Durchgaenge selbst stehen in `protokoll/2026-08-stil.md`.

Dieses Dokument sagt nicht, **was** im Buch steht - das steht in `doc/05`. Es
sagt, **wie man nachsieht**, und was das Nachsehen am 25.08. an sich selbst
gelernt hat.

Es ist aus Schaden geschrieben. Jede Regel unten hat einen Fehler hinter sich,
der ohne sie stehen geblieben wäre, und in zwei Fällen war der Fehler meiner.

---

## Der Kern

**Ein Fund ist nie nur ein Fund. Er ist ein Exemplar einer Klasse.**

Wer einen Fehler repariert und weitergeht, hat einen Fehler repariert. Wer fragt
*wovon ist das ein Fall*, bekommt ein Werkzeug, das den nächsten von derselben
Sorte findet, ohne dass jemand ihn liest.

---

## Aus einem Fund einen Streifzug machen - vier Schritte

1. **Die Klasse benennen.** Der Kartenfehler in Kapitel 38 ist kein Kartenfehler.
   Er ist ein Fall von: *dieselbe seltene Sache steht zweimal in einem Kapitel,
   mit zwei verschiedenen Personen daran.*
2. **Die Klasse bekommt eine Signatur**, die eine Maschine sehen kann.
3. **Der Detektor wird am bekannten Exemplar geeicht.** Findet er den Fehler
   nicht, den er finden können muss, ist er wertlos.
4. **Erst dann der Lauf** - und ein leeres Ergebnis ist dann ein Ergebnis.

**Schritt 3 ist der, den man ausläßt, und der einzige, der etwas beweist.**
Der Detektor in `zuschreibung.py` hat drei Anläufe gebraucht:

- **Fassung 1** nahm die Namen aus dem Satz. Sie fand einen gewollten Widerhall
  statt des Fehlers, weil die eine Hälfte in wörtlicher Rede steht und dort kein
  Name im Satz steht.
- **Fassung 2** nahm ein Fenster von Sätzen. Sie fand **gar nichts**, weil
  Georgij in jedem Fenster steht und der Schnitt nie leer wird. Der Erzähler
  selbst macht den Detektor blind.
- **Fassung 3** fand die Signatur: *dieselbe seltene Wortfolge einmal in der
  Ich-Form und einmal mit einem Namen daran.*

Nach Fassung 2 hätte der Bericht gelautet: *„über alle 87 Kapitel gelaufen,
nichts gefunden"*. Das wäre eine Lüge im Gewand eines Ergebnisses gewesen.
`zuschreibung.py` eicht sich deshalb beim Start selbst und **verweigert die
Meldung**, wenn die Eichung durchfällt.

---

## Sieben Regeln, jede mit einem Fehler dahinter

**1. Eine Zahl, die in beiden Bänden steht, wird in beiden geprüft, bevor eine
davon geändert wird.**
Ich habe in Band 1 Kapitel 28 *„four hours"* auf *„two hours"* gezogen, weil
Kapitel 1 zweimal zwei Stunden sagt. Band 2 sagt an zwei Stellen vier - und die
beiden Zahlen messen Verschiedenes: Kapitel 1 zählt die Zeit **im Saal**, Band 2
die Zeit **im Gebäude**. Die Korrektur war der Fehler. Zurückgenommen.

**2. Die eigenen Korrekturen werden nachgeprüft wie fremde.**
Sieben Blöcke hielten. Der achte nicht. Wer seine eigene Arbeit nicht durch
denselben Durchgang schickt, hat den Durchgang nicht gemacht.

**3. Der Blickwinkel wird vorher benannt.**
Ohne Grenze findet ein Durchgang alles ein bisschen und nichts ganz. Die bisher
gelaufenen: Rückbezüge, Wissensstand, eingelöste Zusagen, Interpunktion, Zahlen
und Daten, Sinn der Aussagen - und zuletzt **Zuschreibung**.

**4. Ein Fund ohne Gegenbeleg ist eine Meinung.**
Kapitel und Wortlaut der Gegenstelle gehören dazu, sonst wird er nicht gemeldet.

**5. Was sich nicht beweisen läßt, bleibt stehen - mit dem Grund.**
Am 25.08. zwei Vorschläge zurückgehalten: einer betraf einen Absatz, der **in
sich stimmig** ist, der andere war eine Ergänzung und keine Korrektur.

**6. Gegenprüfen heißt widerlegen.**
Wer prüft, bekommt den Auftrag, den Fund umzuwerfen, und sagt im Zweifel *nein*.
Am 25.08. hat das **neun von neunundzwanzig** Rohfunden entfernt, also knapp ein
Drittel. Die häufigsten Widerlegungen: zwei Angaben messen Verschiedenes; eine
Figur spricht im Dialog zulässig ungenau; die Gegenstelle steht in einer
überholten Fassung.

**8. Ein Detektor, der zu viel meldet, ist so wertlos wie einer, der nichts
meldet.**
`belege.py` hat am 25.08. in vier Fassungen gemeldet: **265, dann 236, dann 46**,
und die Kapitelprüfung **312, dann 61, dann 12**. Am Buch hat sich dabei nichts
geändert. Wer die erste Zahl gemeldet hätte, hätte den Autor durch
zweihundert Falschmeldungen geschickt, um drei echte zu finden. **Die Zahl sinkt,
bis jeder verbleibende Fund einzeln erklärbar ist** - erst dann wird berichtet.
Was jede Runde gekostet hat, steht als Kommentar im Programm, damit die nächste
Fassung nicht wieder dagegen läuft.

**9. Ein Dokument darf ein Zitat nur so gut kennen, wie es dasteht.**
Aus dem Gedächtnis geschriebene Zitate sind immer *besser* als das Original -
pointierter, symmetrischer, mit einer Zusatzklausel, die die These stützt. Genau
daran erkennt man sie. Drei Fälle in `doc/05` am 25.08., alle drei zugespitzt
gegenüber dem Buch, und einer davon trug den ganzen Absatz.

**7. Kein Zwischenstand ohne Gegenprüfung.**
Eine Zahl, die sich um ein Drittel bewegt, ist als Zwischenstand irreführend.

---

**10. Ein Detektor muss Behauptung und Vorschlag auseinanderhalten können -
und wenn er es nicht kann, muss man es ihm sagen.**
`belege.py` hat in `doc/12-stimmen.md` **zwanzig** Falschzitate gemeldet.
Achtzehn davon sind absichtlich erfundene Repliken - *so würde Jang reden*. Der
Hinweis kam aus der Stilsitzung, und er war richtig: eine Zahl, die zu neunzig
Prozent aus Absicht besteht, gewöhnt alle daran, sie zu ignorieren, **und dann
fängt sie auch das echte Falschzitat nicht mehr.** Das Programm liest jetzt
drei Töpfe: *ohne Beleg*, *alte Fassung*, *Vorschlag*. Nichts wird
unterdrückt - die zwei Nebentöpfe werden gezählt und stehen im Bericht.

**Und die Probe darauf hat gestimmt:** von den zwanzig blieb einer übrig, und
der war echt. Hanas Stimmblatt stand auf einem Satz, den es nicht gibt -
*"Half of what I say on a terrace I say on purpose."* Der Text sagt es
besser, in Kapitel 21, aus ihrem eigenen Mund: *"I am not being careless for
you. In twenty-five years I have not put one sentence into one room without
knowing what it would do when it got there."*

**Wer Vorschläge schreibt, markiert sie** - ein Wort genügt, in der Überschrift
oder im Absatz davor: *Beispiel*, *Vorschlag*, *Muster*, *Entwurf*, *Probe*,
*so würde*, *nicht im Text*. Keine neue Syntax; die Blätter schreiben ohnehin
*Ein Beispiel, ruhig*.

---

## Die Klassen, die es bisher gibt

Wer einen neuen Durchgang plant, fängt hier an statt bei Null.

| Klasse | Woran man sie erkennt | Exemplar |
|---|---|---|
| **Falsche Person** | eine Tat, ein Gefühl oder ein Satz an der falschen Figur | B2 38 (die Karten), B2 42 (Annies Satz in Sang-hoons Mund), B2 40 (Jang von Georgij eingestellt), `doc/15` (Jangs Alter Mrs Ha zugeschrieben) |
| **Falsches Datum an einer Person** | wer wann wovon wußte, wer wann wo war | B2 11 (Hana seit Dezember), B2 26/35 (der 2. statt 1. März), B2 47 (der 23. statt 22. Juni) |
| **Unmögliches Wissen** | die Erzählung ist nah an Georgij und darf nichts sagen, was er später erfährt | B2 8 (Mrs Sunwoos Schublade, vier Tage zu früh) |
| **Falsches „erstes Mal"** | *the first time*, *never*, *only* über eine Person | B2 38 (er habe noch nie jemanden gemocht), B1 17 (zwei eigene Lächeln statt sechs) |
| **Falscher Sprecher** | ein *he said*, dessen Träger nicht auszumachen ist | B2 42 (der Anwalt) |
| **Rückbezug auf den falschen Tag** | *„you told me on the…"* | B1 19 (die Einladung), B1 22 (Tisch statt Tür), B2 20 |
| **Ein Dokument, das das Buch aus dem Gedächtnis zitiert** | ein Register, das eine Zeile führt, die es im Text nicht gibt | `doc/10-naehe.md` (der zweite Satz über den Stuhl) |
| **Richtiges Zitat, falsches Kapitel** | die Zeile steht im Buch, aber unter einer anderen Nummer als im Register - typisch nach einer Umnummerierung | `doc/05` führte eine Zeile aus B2 42 unter B2 43, und schrieb sie Annie statt Sang-hoon zu |
| **Ein Alter, das seinen eigenen Geburtstag überholt** | eine Zahl im Text gegen die Geburtstagstabelle, sobald die geparkte Strecke erzählt wird | Yeom, Woo, Mrs Sunwoo und Annie am 25.08. |
| **Eine Spanne, die sich selbst aufhebt** | *since I was X*, wo X das heutige Alter der Figur ist | B2 62: Annie sagt *since I was thirty-seven* und ist siebenunddreißig |

---

## Reihenfolge: erst Stil, dann Inhalt

**Ein Durchgang, der jede Aussage an `doc/12-stimmen.md` anpasst, geht vor der
Inhaltsprüfung, nicht danach.** Drei Gründe:

1. **Eine Inhaltskorrektur ist ein umgeschriebener Satz.** Wird derselbe Satz
   danach in die Stimme gezogen, kann die Zahl darin wieder verschwinden. Wer
   zuletzt schreibt, hat recht - und das soll der Inhalt sein.
2. **Befunde gegen einen Wortlaut, den es nicht mehr gibt, sind wertlos.** Am
   25.08. lagen genau dafür Notizen im Register: die des alten Kapitels 46,
   geschrieben gegen eine Fassung, die es nach der Umnummerierung nicht mehr gab.
3. **Warten kostet nichts**, weil das Archiv jede Fassung behält. Der Zustand
   vor dem Durchgang muss nicht gesichert werden - er liegt schon da, und
   `faktenspur.py --seit <sha>` holt ihn.

**Zwei Dinge gehören aber davor.** Erstens: wer die Stimmen anlegt, muss die
**Festgelegten Zeilen** aus `doc/05` vor sich haben. Ein Stimmblatt glättet sie
sonst, und ein Zurücknehmen ist teurer als ein Nichtanfassen. Zweitens: die
Fakten stehen in wörtlicher Rede. *"I am fifty-nine"*, *"since I was
twenty-six"*, *"it was Y who suggested the cards"* - alles Stimme und alles
Kanon.

**Gemessen am 25.08.:** seit dem ersten Stimmen-Commit haben **acht Kapitel**
eine Zahl, ein Datum oder einen Namen bewegt. Das auffälligste Muster ist
kein Zahlenfehler, sondern eine **sinkende Namensdichte** - gestrichene
Sprecherangaben, etwa in Kapitel 60 das gelöschte *"Georgij said it without
any weight on it."* Das ist genau der Boden, auf dem die Klasse **falscher
Sprecher** wächst.

---

## Was ein Streifzug nicht kann

Er findet **Instanzen einer bekannten Klasse**. Er findet **nie eine neue
Klasse**. Die kommt aus einem Menschen, der liest und stolpert.

Beide Klassen, die am 25.08. das ganze Werkzeug ausgelöst haben, kamen vom Autor
und nicht aus einem Skript. Das ist keine Schwäche des Verfahrens, sondern seine
Arbeitsteilung: **lesen findet die Klasse, das Skript findet den Rest.**

---

## Die Werkzeuge

| | Was es prüft | Eicht sich selbst |
|---|---|---|
| `werkzeug/check.py` | Satzlänge, Datumszeilen, Versionsnummern, Zahl-Konstanten, Formeln | nein |
| `werkzeug/zuschreibung.py` | Zuschreibungsfehler nach Klasse 1 | **ja**, und meldet sonst nichts |
| `werkzeug/belege.py` | jedes englische Zitat der Dokumente gegen den Text, getrennt nach *ohne Beleg* / *alte Fassung* / *Vorschlag*; `--kapitel` zusätzlich die Kapitelnummer | **ja**, vier Proben, zwei davon frühere Falschmeldungen |
| `werkzeug/faktenspur.py` | was ein Stildurchgang an Zahlen, Daten und Namen bewegt hat; `--seit <sha>` gegen den Stand vor dem Durchgang | **ja**, drei Proben, darunter eine reine Stiländerung, die schweigen muss |
| `werkzeug/build.py` | erzeugt die Lesefassungen; nie von Hand auflösen | - |

**Die zwei stehenden `check.py`-Fehler sind geprüft und bleiben.** Sie melden
eine Zahl-Konstante mit einem anderen Subjekt; die Begründung steht in `doc/05`.

---

## Die Probe vor jedem Bericht

1. Steht der Gegenbeleg da, mit Kapitel und Wortlaut?
2. Ist die Zahl gezählt oder geschätzt?
3. Habe ich versucht, meinen eigenen Fund umzuwerfen?
4. Wenn nichts gefunden wurde: **war der Detektor geeicht?**

---

## Drei Lehren vom 26.08., aus der Gegenprüfung von `doc/16`

**11. Ein Test, der nichts findet, wird nicht gestrichen, bevor zwei Fragen
beantwortet sind: ist der Detektor geeicht, und misst er, was sein Name sagt?**
Die Testbatterie hat ihren Test 5 (*Verbotstest*) auf ein Nullergebnis gestrichen.
`stimmen.py --tics` hat keine Eichung und gibt eine Dichtetabelle der fünf
Haustics aus - es kennt weder den Begriff *Verstoß* noch die figurenspezifischen
Verbote aus `doc/12`. Der Test war nicht grün, er war nie gelaufen. **Die Probe
vor jedem Bericht hatte die halbe Frage schon** (*war der Detektor geeicht?*); die
andere Hälfte fehlte, und sie ist die billigere: **einmal laufen lassen und die
Ausgabe ansehen, bevor man ihr glaubt.** Die Tabelle wies Woo mit *Negativ-Def
0,8* aus - ungleich null für genau die Figur, der die geprüfte Regel die
Negativdefinition abspricht.

**12. Eine Zahl, die eine Figur mit einer Szene gegen Figuren mit achtzig stellt,
ist keine Messung.** Mrs Has Zug maß *drei Treffer bei ihr, null Prozent bei neun
anderen* - und sie hat genau ein Kapitel. Jede beliebige Wendung aus alt K67 hätte
dieselbe Zahl bekommen. **Und wo der Zug mit dem Gegenstand der Szene
zusammenfällt** - sie wird gefragt, wer was getan hat, und stellt richtig, wer die
Arbeit getan hat -, ist er nicht von der Szene zu trennen. Der ehrliche Stand ist
*Vorschlag* und wird beim zweiten Auftritt entschieden.

**13. Ein Detektor braucht so viele Töpfe, wie es Gründe gibt, warum ein Zitat
nicht im Text steht.** `belege.py` hat drei (*ohne Beleg*, *alte Fassung*,
*Vorschlag*). Von vierzehn Meldungen am 26.08. waren drei echt; die elf anderen
verteilten sich auf vier Gründe, die keinen Topf haben:

- **Auslassung:** das Zitat steht da, mit `...` zusammengezogen (b2 K6, drei
  Meldungen für ein Zitat).
- **Redebegleitsatz:** das Zitat steht da, unterbrochen von *he said* (b2 K53).
- **Gestrichene Fassung:** das Dokument zitiert ausdrücklich, was **entfernt
  wurde** - nicht überholt, sondern weg. Fünf Meldungen, alle legitim.
- **Unmarkierter Vorschlag:** *"Eine Zeile wie ..."* fehlt in der Wortliste, und
  `doc/30-plan-band-1.md` ist von Haus aus ein Plandokument.

---

**Zwei Klassen, die die Tabelle oben noch nicht hatte:**

| Klasse | Woran man sie erkennt | Exemplar |
|---|---|---|
| **Ein Plan, der im Kanondokument als Bestand steht** | `doc/05` zitiert einen Satz mit einer Behauptung darüber (*"der einzige Satz in zwei Bänden"*), und der Satz steht in `doc/07` unter *was kommt* | `doc/05` Z938, das Bandende, korrigiert am 26.08. |
| **Dieselbe Wendung, zwei Bezüge, wenige Zeilen auseinander** | eine auffällige Formel läuft zweimal gleich an und meint zweimal etwas anderes - der Leser liest die zweite als Wiederaufnahme | b2 K29 (geteilt) Z42 gegen Z48: dieselben *"Two people"* sind einmal die Empfänger und einmal die Anrufer |

**Und eine Lücke im Werkzeugkasten, die keine Klasse ist:** alle zwölf Prüfungen
der Batterie messen **eine Figur gegen den Text**, keine misst **eine Figur gegen
eine andere**. Test 1 vergleicht nur gegen Georgij. Der Befund, der das ganze
Stimmenwerk ausgelöst hat, lautete aber *"außer mit Annie sind alle Dialoge
gleich"* - und das ist eine Aussage über zwei Figuren und nicht über eine. Was
fehlt, ist die Blindprobe: zwei Repliken ohne Namen, aus zwei kleinen Figuren,
und ob man sie zuordnen kann.


---

Ab dem 24.08. laufen drei getrennte Sitzungen an diesem Buch. Dieses Dokument
sagt, wer was hat, was schon geprueft ist, und was offen liegt. **Wer eine
Sitzung aufmacht, liest es zuerst und danach `doc/15-kalender.md`.**

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
| Kontraktionen (`doc/20-handwerk.md`, Abschnitt 2c) | Rueckbezuege und Zeitdeixis in der Rede |
| Satzlaenge, Tics, Erzaehlerformeln, Echos | Kanonfakten: Alter, Dienstzeiten, Daten, das Geburtstagsregister |
| Sprecherkette und Beats (Regel 5) | Widersprueche zwischen Band 1 und Band 2 |
| Absatzbau: zwei Sprecher in einem Absatz, fehlende Trenner | Ob eine Zusage eingeloest wird und eine angekuendigte Faelligkeit kommt |
| Die zwei Trenner: `---` Takt, `* * *` Szene | |

**Dokumente.** `doc/20-handwerk.md` gehoert dem Stil-Chat. `doc/15-kalender.md`
und `doc/40-verworfen.md` und `doc/41-entscheidungen.md` gehoeren dem Inhalts-Chat. In `doc/31-plan-band-2.md`
schreibt der Schreibende vorn (was kommt) und der Pruefende hinten (was offen
blieb).

**`doc/13-zusagen.md` gehoert allen dreien und ist am 25.08. entstanden**, nachdem
der Pruefer zwei ueberfaellige Zusagen gefunden hatte, die beide im Text standen
und in keiner Liste: die fuenf Firmen aus Kapitel 12 (vier Monate erzaehlte Zeit)
und Annies *"You will in about a month"* aus Kapitel 5 (sechs Monate). Beide sind
heute bezahlt: Annies Satz in Kapitel 69, die fuenf Firmen nach einem ersten
Kauf in Kapitel 23 rueckblickend in Kapitel 79. **Das Kaufdatum ist noch offen
widerspruechlich**, weil Kapitel 87 alle fuenf auf November datiert.

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
  Zitat (Kapitel 10) und in `doc/20-handwerk.md` als Ausnahme verbucht.
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
   Kapitelliste von `doc/15-kalender.md` tragen die Band-2-Zeilen achtundvierzig
   Szenenangaben, die Band-1-Zeilen **zwei**, und eine davon ist Kapitel 5. Es
   ist also nicht dieselbe Arbeit wie in Band 2 und kein Abschreiben von einer
   Liste, sondern Lesearbeit ueber vierunddreissig Kapitel. Ein Automatismus
   wurde versucht und verworfen, er traf vier von vierundvierzig Kapiteln.

4. **94 Fragezeichen-Verdachtsfaelle** meldet `check.py` ueber beide Baende. Jeder
   ist eine Entscheidung und keiner ein Fehler - das Skript entscheidet die
   Machtlage nicht und darf es nicht.

5. ~~**Erzaehlerformeln.**~~ **Erledigt fuer Band 1 am 25.08. - und der Befund
   ist, dass Band 1 nie das Problem war.** Gezaehlt ueber beide Baende:

   | | Band 1 (34 Kap.) | Band 2 (70 Kap.) |
   |---|---|---|
   | *did not soften* | 5 | **12** |
   | *did not look away* | 6 | **10** |
   | *without any … in it at all* | **1** | **9** |

   **Und in Band 2 stehen sie geballt in den neuesten Kapiteln:** alt K67 bis alt K70
   tragen allein **dreizehn** der zweiundzwanzig. **Die Formel wird gerade neu
   angelegt, waehrend hier steht, dass sie abgebaut wird.** Das gehoert der
   Schreibsitzung und nicht mir.

   In Band 1 angefasst wurde genau eine Stelle, und die war doppelt: b1 K18 hatte
   *"He said it flatly and did not soften it."* - Ton **und** Formel in einem
   Beat, und vierzig Zeilen weiter noch ein *"He did not soften it."* Der
   doppelte ist raus, der einzelne steht.

   Der urspruengliche Eintrag lautete:

   *"did not soften"* und *"did not look away"* sind
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
    | Band 2, Kapitel 29 bis 56 | 100 | 90 | **1,1 Absaetze** |

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

11. ~~**Der Ton-etikettierende Beat.**~~ **Erledigt am 25.08.** Band 2 lief im
    August, Band 1 jetzt: **zweiunddreissig reine Ton-Etiketten entfernt** aus
    einundzwanzig Kapiteln.

    **Die Probe war dieselbe wie in Band 2:** ein Ton-Beat verdient seinen
    Platz, wenn er **etwas anderes tut als den Ton zu benennen** - einen Grund
    (*because it did not need one*), einen Vergleich (*in the same courteous
    register he had used for the cameras*), ein empfangenes Urteil (*which he
    liked*), eine Richtung (*to the water*), ein Tempo (*immediately*), oder
    eine Gegenueberstellung, die traegt (*He said it kindly* - nach dem Auge auf
    dem Kies).

    Gefallen sind die, die **nur** den Ton nennen - *plainly, flatly, levelly,
    without any weight* - und in Reichweite ohnehin etwas Koerperliches haben.

    **Band 1 war dabei deutlich besser als Band 2:** von 102 Stellen trugen 29
    von sich aus etwas, und von den uebrigen sind rund fuenfzehn ebenfalls
    stehengeblieben, weil sie Richtung, Tempo oder Wiederholung angeben und
    nicht Ton. **Kein einziger Beat wurde erfunden** - jede Stelle ist ein
    Zusammenlegen der zwei Redeteile.

    Stand danach: **Band 1 69 Ton-Beats, 2,0 je Kapitel, 0,68 je 1000 Woerter.
    Band 2 140, 2,0 je Kapitel, 0,81.** Die beiden Baende liegen damit erstmals
    gleichauf, und Band 1 ist die duennere Haelfte.

    Der urspruengliche Eintrag lautete:

    **Der Ton-etikettierende Beat, und das ist der grosse offene Posten.**
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
    reisst. Es ist dieselbe Luecke, die `doc/20-handwerk.md` fuer *did not soften*
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
  benutzt zu werden - alles in `doc/31-plan-band-2.md` unter dem Eintrag vom 24.08.

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
4. **`doc/15-kalender.md` ist der Uebergabepunkt.** Dort stehen unter
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
Schreibsitzung liest danach `doc/15-kalender.md`, Abschnitt *"Korrigiert am
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
mit einer Ergaenzung - **wer einen Band nimmt, schreibt es in `doc/31-plan-band-2.md`
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
vergeben, und in `doc/15-kalender.md` eintragen, was zusammengelegt wurde.

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
| `doc/20-handwerk.md` | Stil |
| `doc/15-kalender.md`, `doc/40-verworfen.md`, `doc/41-entscheidungen.md` | Inhalt |
| `doc/30-plan-band-1.md` | Schreiben |
| `doc/31-plan-band-2.md` | alle drei: Schreiben vorn, Pruefende hinten anhaengen |
| `doc/protokoll/2026-08-stil.md` | **Stil**, waehrend des Durchgangs. Die Inhaltspruefung liest nur |
| `doc/22-pruefen.md` | wer prueft, und zwar sofort nachdem er etwas gelernt hat |
| `doc/22-pruefen.md` | wer die Aufteilung aendert, und zwar bevor er sie aendert |

### Und der zweite Uebergabepunkt: das Stilprotokoll

Seit dem 25.08. gibt es `doc/protokoll/2026-08-stil.md`. **Ein Durchgang, der jede
Aussage an `doc/12-stimmen.md` anpasst, schreibt woertliche Rede um, und in
woertlicher Rede stehen die Fakten.** Ohne Protokoll muesste die
Inhaltspruefung danach hundert Kapitel neu lesen; mit Protokoll liest sie die
Zeilen, die sich bewegt haben.

Die Reihenfolge ist **erst Stil, dann Inhalt** - die Begruendung steht in
`doc/22-pruefen.md`. Kurz: wer zuletzt schreibt, hat recht, und das soll der
Inhalt sein; Befunde gegen einen Wortlaut, den es nicht mehr gibt, sind wertlos;
und Warten kostet nichts, weil das Archiv jede Fassung behaelt.

---

### Und der Uebergabepunkt

`doc/15-kalender.md` ist die Stelle, an der die drei einander erreichen. Dort
stehen die Kapitelliste, das Geburtstagsregister und die Liste der geaenderten
Kanonzahlen. **Wer etwas am Kanon aendert, traegt es dort ein, bevor er pusht.**
Wer schreibt, liest es, bevor er anfaengt. Alles andere ist Chatverlauf und damit
weg.

---

## Einstieg fuer den Stil-Chat, zum Kopieren

> Du uebernimmst Stil fuer *Lot Fourteen*. **Arbeite in einem eigenen Klon**,
> nicht in dem, in dem eine andere Sitzung laeuft - warum, steht unter Regel 5.
> Lies in dieser Reihenfolge: `lot-fourteen/CLAUDE.md`,
> `doc/22-pruefen.md`, `doc/20-handwerk.md` von vorn bis Abschnitt 2d.
> Inhaltliche Pruefung machst Du nicht - Zahlen, Daten, Wissensketten und
> Kanonfakten laufen in einer anderen Sitzung, und `doc/15-kalender.md` sagt
> Dir, was dort zuletzt geaendert wurde. Dein Ressort ist die linke Spalte oben:
> Satzzeichen, Satzlaenge, Tics, Erzaehlerformeln, Echos, Sprecherkette und
> Beats, Absatzbau, die zwei Trenner.
>
> Punkt 1 und 2 der offenen Liste sind erledigt. Die naechstgroessten Hebel sind
> die Erzaehlerformeln in Band 2 (Punkt 5), das Komma-Mittel zurueck auf zehn
> (Punkt 8) und die Szenengrenzen von Band 1 (Punkt 3). Bring Zahlen mit und
> keine Eindruecke - und wenn eine Zahl im Dokument nicht stimmt, zaehl nach und
> schreib sie um. Drei standen hier falsch.


---

**Wem es gehoert:** der Stilsitzung. Sie schreibt hier, die Inhaltspruefung
liest hier. Niemand sonst schreibt hinein - deshalb ist es eine eigene Datei und
nicht ein Abschnitt in `doc/05`, das schon zweimal kollidiert ist.

**Wozu.** Ein Durchgang, der jede Aussage an `doc/12-stimmen.md` anpasst,
schreibt woertliche Rede um. In woertlicher Rede stehen die Fakten: *"I am
fifty-nine"*, *"since I was twenty-six"*, *"it was Y who suggested the cards"*.
Ohne Protokoll muss die Inhaltspruefung danach hundert Kapitel neu lesen. Mit
Protokoll liest sie die Zeilen, die sich bewegt haben.

**Die Gegenprobe dazu** ist `werkzeug/faktenspur.py --seit <sha>`. Sie findet,
was an Zahlen, Daten und Namen anders ist. Sie findet **nicht**, was gleich
zaehlt und anders bedeutet. Genau dafuer ist dieses Blatt da.

---

## Ausgangsstand

**Vor dem Durchgang eintragen, in einer Zeile:**

    Durchgang <Name>, begonnen <Datum>, Ausgangsstand <sha>

Ohne den SHA ist `--seit` Raterei.

| Durchgang | Datum | Ausgangsstand | Kapitel | Stand |
|---|---|---|---|---|
| Erzaehlerkommentare, Band 2 | 25.08.2026 | `14a893e` | b2 K01-alt K68 | laeuft |

**Was dieser Durchgang tut, und warum er die vier Meldungen anders trifft als
erwartet.** Er schreibt **keine woertliche Rede um**. Er setzt Absaetze
*dazwischen*: der Erzaehler benennt wieder, was eine Szene zurueckhaelt.
Gemessen am 25.08.: Band 1 hat 25 solche Saetze (0,25 je 1000 Woerter), Band 2
hat 4 (0,02) - der Erzaehler ist nach Band 1 verstummt, und das Erklaeren ist
in die Muender der Figuren gewandert (Band 1 25:21, Band 2 4:46).

Daraus folgt fuer dieses Blatt:

- **Meldung 1** (Sprecherangaben) faellt fast weg - es wird nichts gestrichen.
- **Meldung 2 und 3 sind die schweren.** Jeder eingesetzte Satz ist eine **neue
  Tatsachenbehauptung des Erzaehlers**, und der Erzaehler wiegt schwerer als
  eine Figur. Steht darin eine Dauer (*four days*) oder ein Absolutum (*never*,
  *the largest*, *the whole of it*), steht sie unten - auch wenn ich sie aus
  dem Kapitel selbst genommen habe. **Woher ich sie habe, steht dabei.**
- **Meldung 4:** die festgelegten Zeilen in `doc/05` verbieten dem Erzaehler
  ausdruecklich, auf sie zu zeigen (*best-made thing*, *was nicht Arbeit war*,
  *die zwei Haende*). Alle drei liegen in Band 1. In Band 2 wird kein
  Kommentar in ihre Naehe gesetzt.

---

## Was gemeldet wird

Vier Sachen, und nur diese vier. Alles andere kostet die Inhaltspruefung nichts.

**1. Eine gestrichene oder eingesetzte Sprecherangabe.**
Kapitel, und die Zeile so, wie sie vorher dastand. Das ist die wichtigste der
vier: mit jeder gestrichenen Angabe haengt der Sprecher nur noch am Zusammenhang,
und *falscher Sprecher* ist eine belegte Fehlerklasse in diesem Buch.
Beispiel aus Kapitel 60: gestrichen wurde *"Georgij said it without any weight on
it."*

**2. Ein umformulierter Satz, in dem eine Zahl, ein Datum, ein Alter oder eine
Dauer steht.** Kapitel, vorher, nachher. Auch dann, wenn die Zahl selbst
gleich geblieben ist - *"four hours"* im Saal und *"four hours"* im Gebaeude sind
zwei verschiedene Angaben, und die Verwechslung hat schon einmal eine falsche
Korrektur ausgeloest.

**3. Eine angefasste absolute Behauptung.** *the first time*, *never*, *only*,
*since*, *not once*. Diese Saetze sind fast immer Kanon und fast nie nur Ton.

**4. Eine festgelegte Zeile, die das Stimmblatt aendern wollte.**
Die Liste steht in `doc/16-motive.md` unter **Festgelegte Zeilen**.
**Nicht aendern - hier eintragen.** Ein Zuruecknehmen ist teurer als ein
Nichtanfassen, und der Autor entscheidet das, nicht das Stimmblatt.

**Nicht gemeldet wird:** Satzzeichen, Satzlaenge, Absatzbau, Tics,
Erzaehlerformeln, Echos, Beats, die zwei Trenner. Reiner Ton, kein Inhalt.

---

## Erfundene Repliken markieren

`doc/12-stimmen.md` erfindet absichtlich Sprache, um eine Stimme zu zeigen.
`werkzeug/belege.py` hat die zuerst als Falschzitate gezaehlt - zwanzig Stueck,
achtzehn davon Absicht. **Ein Wort im Absatz davor oder in der Ueberschrift**
genuegt, damit das Werkzeug sie richtig einsortiert: *Beispiel*, *Vorschlag*,
*Muster*, *Entwurf*, *Probe*, *so wuerde*, *nicht im Text*. Keine neue Syntax.

**Warum das nicht Kosmetik ist:** von den zwanzig blieb nach der Trennung einer
uebrig, und der war echt - Hanas Blatt stand auf einem Satz, den es im Buch
nicht gibt. Eine Zahl, die zu neunzig Prozent aus Absicht besteht, wird
ignoriert, und dann faellt der eine nicht mehr auf.

---

## Unsicher

Wo eine Stimmkorrektur den Sinn verschoben haben koennte, auch ohne dass eine
Zahl gewandert ist. Eine Zeile genuegt: Kapitel, Stelle, woran es liegt. Lieber
eine zu viel.

---

## Zwei Regeln, die nicht verhandelbar sind

**Keine Zahl, kein Name, kein Datum und kein Alter wird geaendert, damit ein
Satz besser klingt.** Wenn die Stimme es verlangt, bleibt die Zahl stehen und
die Forderung kommt in dieses Blatt.

**Keine Sprecherangabe wird gestrichen, wenn der Sprecher im selben Wechsel
nicht anders erkennbar ist.** Im Zweifel stehen lassen und unter *Unsicher*
eintragen.

---

**Alle Durchgaenge sind am 27.08. ausgezogen** und stehen in
`doc/protokoll/2026-08-stil.md`, 19.199 Woerter. Was hier steht, sind die
**Regeln der Stilpruefung**, und sie wandern in Schritt 4 nach `22-pruefen`.

Damit ist der Name dieses Dokuments ueberholt: es ist kein Protokoll mehr.
