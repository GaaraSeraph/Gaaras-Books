# Wie geprüft wird

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
| **Falsche Person** | eine Tat, ein Gefühl oder ein Satz an der falschen Figur | B2 38 (die Karten), B2 42 (Annies Satz in Sang-hoons Mund), B2 40 (Jang von Georgij eingestellt) |
| **Falsches Datum an einer Person** | wer wann wovon wußte, wer wann wo war | B2 11 (Hana seit Dezember), B2 27/35 (der 2. statt 1. März), B2 47 (der 23. statt 22. Juni) |
| **Unmögliches Wissen** | die Erzählung ist nah an Georgij und darf nichts sagen, was er später erfährt | B2 8 (Mrs Sunwoos Schublade, vier Tage zu früh) |
| **Falsches „erstes Mal"** | *the first time*, *never*, *only* über eine Person | B2 38 (er habe noch nie jemanden gemocht), B1 17 (zwei eigene Lächeln statt sechs) |
| **Falscher Sprecher** | ein *he said*, dessen Träger nicht auszumachen ist | B2 42 (der Anwalt) |
| **Rückbezug auf den falschen Tag** | *„you told me on the…"* | B1 19 (die Einladung), B1 22 (Tisch statt Tür), B2 20 |
| **Ein Dokument, das das Buch aus dem Gedächtnis zitiert** | ein Register, das eine Zeile führt, die es im Text nicht gibt | `doc/10-naehe.md` (der zweite Satz über den Stuhl) |
| **Richtiges Zitat, falsches Kapitel** | die Zeile steht im Buch, aber unter einer anderen Nummer als im Register - typisch nach einer Umnummerierung | `doc/05` führte eine Zeile aus B2 42 unter B2 44, und schrieb sie Annie statt Sang-hoon zu |
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
anderen* - und sie hat genau ein Kapitel. Jede beliebige Wendung aus b2 K67 hätte
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
- **Redebegleitsatz:** das Zitat steht da, unterbrochen von *he said* (b2 K56).
- **Gestrichene Fassung:** das Dokument zitiert ausdrücklich, was **entfernt
  wurde** - nicht überholt, sondern weg. Fünf Meldungen, alle legitim.
- **Unmarkierter Vorschlag:** *"Eine Zeile wie ..."* fehlt in der Wortliste, und
  `doc/06-plot.md` ist von Haus aus ein Plandokument.

---

**Zwei Klassen, die die Tabelle oben noch nicht hatte:**

| Klasse | Woran man sie erkennt | Exemplar |
|---|---|---|
| **Ein Plan, der im Kanondokument als Bestand steht** | `doc/05` zitiert einen Satz mit einer Behauptung darüber (*"der einzige Satz in zwei Bänden"*), und der Satz steht in `doc/07` unter *was kommt* | `doc/05` Z938, das Bandende, korrigiert am 26.08. |
| **Dieselbe Wendung, zwei Bezüge, wenige Zeilen auseinander** | eine auffällige Formel läuft zweimal gleich an und meint zweimal etwas anderes - der Leser liest die zweite als Wiederaufnahme | b2 K34 Z42 gegen Z48: dieselben *"Two people"* sind einmal die Empfänger und einmal die Anrufer |

**Und eine Lücke im Werkzeugkasten, die keine Klasse ist:** alle zwölf Prüfungen
der Batterie messen **eine Figur gegen den Text**, keine misst **eine Figur gegen
eine andere**. Test 1 vergleicht nur gegen Georgij. Der Befund, der das ganze
Stimmenwerk ausgelöst hat, lautete aber *"außer mit Annie sind alle Dialoge
gleich"* - und das ist eine Aussage über zwei Figuren und nicht über eine. Was
fehlt, ist die Blindprobe: zwei Repliken ohne Namen, aus zwei kleinen Figuren,
und ob man sie zuordnen kann.
