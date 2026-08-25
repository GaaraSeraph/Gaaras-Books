# Wie geprüft wird

Dieses Dokument sagt nicht, **was** im Buch steht — das steht in `doc/05`. Es
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

## Aus einem Fund einen Streifzug machen — vier Schritte

1. **Die Klasse benennen.** Der Kartenfehler in Kapitel 38 ist kein Kartenfehler.
   Er ist ein Fall von: *dieselbe seltene Sache steht zweimal in einem Kapitel,
   mit zwei verschiedenen Personen daran.*
2. **Die Klasse bekommt eine Signatur**, die eine Maschine sehen kann.
3. **Der Detektor wird am bekannten Exemplar geeicht.** Findet er den Fehler
   nicht, den er finden können muss, ist er wertlos.
4. **Erst dann der Lauf** — und ein leeres Ergebnis ist dann ein Ergebnis.

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
Kapitel 1 zweimal zwei Stunden sagt. Band 2 sagt an zwei Stellen vier — und die
beiden Zahlen messen Verschiedenes: Kapitel 1 zählt die Zeit **im Saal**, Band 2
die Zeit **im Gebäude**. Die Korrektur war der Fehler. Zurückgenommen.

**2. Die eigenen Korrekturen werden nachgeprüft wie fremde.**
Sieben Blöcke hielten. Der achte nicht. Wer seine eigene Arbeit nicht durch
denselben Durchgang schickt, hat den Durchgang nicht gemacht.

**3. Der Blickwinkel wird vorher benannt.**
Ohne Grenze findet ein Durchgang alles ein bisschen und nichts ganz. Die bisher
gelaufenen: Rückbezüge, Wissensstand, eingelöste Zusagen, Interpunktion, Zahlen
und Daten, Sinn der Aussagen — und zuletzt **Zuschreibung**.

**4. Ein Fund ohne Gegenbeleg ist eine Meinung.**
Kapitel und Wortlaut der Gegenstelle gehören dazu, sonst wird er nicht gemeldet.

**5. Was sich nicht beweisen läßt, bleibt stehen — mit dem Grund.**
Am 25.08. zwei Vorschläge zurückgehalten: einer betraf einen Absatz, der **in
sich stimmig** ist, der andere war eine Ergänzung und keine Korrektur.

**6. Gegenprüfen heißt widerlegen.**
Wer prüft, bekommt den Auftrag, den Fund umzuwerfen, und sagt im Zweifel *nein*.
Am 25.08. hat das **neun von neunundzwanzig** Rohfunden entfernt, also knapp ein
Drittel. Die häufigsten Widerlegungen: zwei Angaben messen Verschiedenes; eine
Figur spricht im Dialog zulässig ungenau; die Gegenstelle steht in einer
überholten Fassung.

**7. Kein Zwischenstand ohne Gegenprüfung.**
Eine Zahl, die sich um ein Drittel bewegt, ist als Zwischenstand irreführend.

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
| `werkzeug/build.py` | erzeugt die Lesefassungen; nie von Hand auflösen | — |

**Die zwei stehenden `check.py`-Fehler sind geprüft und bleiben.** Sie melden
eine Zahl-Konstante mit einem anderen Subjekt; die Begründung steht in `doc/05`.

---

## Die Probe vor jedem Bericht

1. Steht der Gegenbeleg da, mit Kapitel und Wortlaut?
2. Ist die Zahl gezählt oder geschätzt?
3. Habe ich versucht, meinen eigenen Fund umzuwerfen?
4. Wenn nichts gefunden wurde: **war der Detektor geeicht?**
