# Lot Fourteen

Literarischer Roman, laufende Arbeit. Suedkorea, Gegenwart, Chaebol-Milieu.
Manuskript auf Englisch, Absprachen auf Deutsch.

**Kanon sind die Kapiteldateien `chNN_vX_Y_en.md`.** Alles andere beschreibt sie
oder plant voraus. Wo ein Planungsdokument dem Text widerspricht, hat der Text
recht und das Dokument wird geaendert.

---

## Zuerst

**`doc/01-craft.md` lesen, mindestens den ersten Abschnitt.** Das ist die Liste, die in jedem
Durchgang laeuft: Bandwurmsaetze, ob die Saetze ueberhaupt Sinn ergeben, ob jede
Aussage einen Rueckbezug hat, die Laecheln, die Satzzeichen, die Quoten.

Danach:

1. Das betroffene Kapitel und die zwei davor lesen. Nicht die Zusammenfassung.
2. Bei einer Figurenszene: `doc/02-leads.md`.
3. Bei einer Verhandlungsszene: `doc/04-world.md` ganz.
4. Beim Pruefen von Daten und Motiven: `doc/05-continuity.md`.

## Bevor Du etwas abgibst

```
python3 check.py chapters/chNN_vX_Y_en.md
python3 build.py
```

`check.py` prueft alles Mechanische: Satzlaenge, Gedankenstriche, Tics,
Datumszeilen, Versionsnummern. `build.py` erzeugt `paste/`, `read/`, `book-band-1.md`, `book-band-2.md`,
`HANDBUCH.md` und `MANIFEST.txt` neu und bricht ab, wenn Dateiname und Kopfzeile
auseinanderlaufen.

`read/` ist die Fassung zum Anschauen: `reader.py` setzt jedes Kapitel als
HTML-Seite unter `read/band-N/`, dazu `read/book.html` mit allen Kapiteln beider
Baende und einem Inhaltsverzeichnis. Eine md-Datei bekommt man im Chat zum
Herunterladen, eine HTML-Seite kann man aufmachen und lesen. Kanon bleiben
`chapters/` und `chapters-2/`.

---

## Zwei Baende

**Band 1 steht in `chapters/` und ist fertig erzaehlt**, vierunddreissig Kapitel,
Tag 1 bis Tag 149. **Band 2 steht in `chapters-2/` und faengt wieder bei Kapitel 1
an**, am Tag 150.

**Die Bandnummer steht in keiner Kapiteldatei.** In der Datei steht weiterhin
`# Chapter 1: ...`; woraus beim Bauen `# Book Two · Chapter 1: ...` wird. Die
Nummer kommt aus dem Ordner. **Wer sie in die Kapitel schreibt, macht sie
driftfaehig** und muss ausserdem vierunddreissig Fassungen hochsetzen, damit oben
ein Wort mehr steht.

**Was daran je Band getrennt laeuft:** die Kapitelnummern, die Basislinie in
`.check-baseline` (Schluessel `b1/15`, `b2/1`) und die Kapitelliste in
`doc/05-continuity.md`. Dort bekommen Band-2-Zeilen einen Praefix:

```
- **Kapitel 15** *Four thousand two hundred* (v2.7) - ...      <- Band 1
- **Band 2, Kapitel 1** *Titel* (v1.0) - ...                   <- Band 2
```

**Was NICHT getrennt laeuft, und das ist Absicht:** die acht Dokumente in `doc/`,
der Kalender und das Begegnungsregister. Es ist eine Geschichte und eine
Figurenwelt. Der Kalender zaehlt ueber die Bandgrenze durch, und `check.py` prueft
die Datumszeilen von Band 2 gegen denselben Kalender wie die von Band 1.

Beides laeuft ausserdem von selbst: als Hook vor jedem Commit und als GitHub
Action bei jedem Push. Der Hook baut und **blockiert bei einem Build-Fehler**,
die Kapitelpruefung warnt nur.

## Ordnung

| Oben | Was |
|---|---|
| `CLAUDE.md` | Diese Datei. Die einzige oben, die von Hand bearbeitet wird |
| `book-band-1.md` | Lesefassung von Band 1 am Stueck. **Erzeugt** |
| `book-band-2.md` | Lesefassung von Band 2 am Stueck. **Erzeugt** |
| `HANDBUCH.md` | Lesefassung aller Regeln und des Kanons. **Erzeugt** |
| `BEGEGNUNGEN.md` | Wer wann vorkommt, mit Tag und Fundstelle. **Erzeugt** |
| `MANIFEST.txt` | Baubericht. **Erzeugt** |

| Ordner | Was |
|---|---|
| `chapters/` | Die Kapitel von **Band 1**. Kanon |
| `chapters-2/` | Die Kapitel von **Band 2**, wieder ab `ch01`. Kanon |
| `doc/` | Die acht Quelldokumente. Gelten fuer beide Baende |
| `paste/band-N/` | Einfuegefassungen je Band. **Erzeugt**, nie bearbeiten |
| `read/band-N/` | Lesefassungen als HTML, dazu `read/book.html` fuer alles. **Erzeugt**, nicht versioniert |

**Die Regel dahinter:** Was oben liegt, liest man. Was in einem Ordner liegt,
bearbeitet man. Von dem, was oben liegt, wird nur `CLAUDE.md` angefasst.

**Danach das Kapitel noch einmal lesen, und dann noch einmal.** Erst wenn zwei
Durchgaenge nacheinander nichts finden, ist es fertig. Das ist keine Floskel: In
der Praxis findet der zweite Durchgang regelmaessig noch etwas.

---

## Wie Konsistenz geprueft wird

Drei Ebenen, und nur die unterste ist mechanisch. Wer eine davon auslaesst,
prueft die falsche Sorte Fehler.

**1. Das Skript.** `check.py` entscheidet nur, was ohne Urteil entscheidbar ist:
Satzlaenge, Satzzeichen, Quoten, Datumszeilen, Versionsnummern, ein paar
Zahl-Konstanten. Das ist **Form, nicht Bedeutung.** Ob ein Satz wahr ist, kann
es nicht wissen.

**2. Lesen mit Vorlauf.** Das betroffene Kapitel **und die zwei davor**, nicht
die Zusammenfassung. Das ist die einzige Ebene, die Rueckbezuege und
Motivwiederholung faengt, weil man den Nachbartext im Kopf hat.

**3. Pruefauftraege an Agenten**, fuer alles, was das ganze Buch auf einmal
braucht: Zahlen quer ueber vierunddreissig Kapitel, Zeitangaben gegen den Kalender,
Dokument gegen Text. Ein Leser kann 50.000 Woerter plus acht Dokumente nicht mit
der noetigen Genauigkeit halten, vier Leser mit je einem Auftrag schon.

**Was in jeden Auftrag gehoert:** welche Dateien Kanon sind (namentlich, es
liegen alte Fassungen daneben), woertliche Zitate mit Zeilennummer statt
Beschreibungen, fertiger Ersatztext statt Problemschilderung, die Trennung
sicher/unsicher, und am Schluss der **Pruefumfang als Zahl**. "Nichts gefunden"
ohne Angabe, wie viel geprueft wurde, ist wertlos.

**Und die Regel, die alles traegt: Berichte werden nicht abgenommen.** Jede
folgenreiche Behauptung bekommt eine eigene Gegenprobe, bevor sie in eine Datei
wandert. Zwei Laeufe haben sich schon bei einer Zaehlung widersprochen, und der
mit der hoeheren Zahl hatte recht.

**Dasselbe gilt fuer die Pruefungen selbst.** Ein stiller Lauf beweist nichts.
Nach jeder Aenderung an `check.py` den Text absichtlich kaputtmachen und
nachsehen, ob es feuert. Eine Datumszeile wurde so monatelang stillschweigend
uebersprungen und danach als fehlend gemeldet.

**Wo die Fehler tatsaechlich sitzen:** nicht in den Datumszeilen, die geprueft
werden und deshalb stimmen, sondern in den Zeitangaben und Zahlen **im
Fliesstext**, die niemand nachrechnet. Was geprueft wird, ist richtig. Was nicht
geprueft wird, driftet.

---

## Punkt oder Fragezeichen

**Die Regel, die beim Schreiben am haeufigsten falsch angewendet wird**, weil sie
sich nicht aus der Grammatik ergibt, sondern aus der Machtlage im Raum.

**Der Punkt gehoert dem, der nicht bittet.** Eine Frage, die Auskunft *verlangt*,
behaelt ihn - auch bei umgestelltem Hilfsverb, auch mit Fragewort. Das ist Annies
Grundregister und Georgijs kalte Fassung, und es steht so quer durchs Buch:

> "What do you want." · "How much." · "Why." · "Why not."
> "Was it worth it." · "How long did it take." · "Why did you not."

**Das Zeichen gehoert dem, der den Zug abgibt.** Wer um Erlaubnis fragt, wer den
anderen weiterreden laesst, wer eine Antwort will, ueber die er nicht verfuegt:

> "May I ask why not?" · "May I propose something?" · "And?" · "And the third?"
> "Then why?" · "Does that include what is already open?" · "Was I useful?"

**Die Probe ist eine Frage:** Kann der andere nein sagen, ohne den Raum zu
verlassen? Dann Zeichen. Muss er liefern? Dann Punkt.

**Und die Machtlage kann sich mitten in einer Szene drehen.** Das Zeichen folgt
ihr, nicht dem Rang. Wer zuerst gegeben hat und dann selbst etwas will, fragt -
auch wenn ihm der Raum gehoert. In Band 2, Kapitel 4 sagt Park Sang-hoon erst
*"Ask."*, gibt die Tuer ins Register her und fragt danach **"What do you
have?"** Mit Zeichen, weil Georgij an dieser Stelle nein sagen koennte, ohne den
Korridor zu verlassen. Drei Repliken vorher haette derselbe Mann denselben Satz
mit einem Punkt bekommen.

**Die Probe bleibt also dieselbe, aber sie wird pro Replik gestellt und nicht
pro Figur.** Wer eine Figur einmal als "die mit dem Punkt" einsortiert, verliert
genau die Stellen, an denen etwas passiert.

**Der schnelle Weg zur Antwort ist, wer wen fragt.** Wer in dem Raum die Macht
hat, fordert und bekommt den Punkt: Annie, Sang-hoon, Ye-rin. Georgij fragt nach
oben und bekommt das Zeichen, **auch wenn die Zeile drei Woerter lang und eiskalt
ist**. *"Was I useful?"* stand bis zum 23.08. mit Punkt da und war die einzige
Ausnahme im ganzen Buch, in die eine Richtung wie in die andere.

**Kaelte ist kein Kriterium, und das ist die Falle.** Kurz und flach sieht aus wie
Annies Register, ist es aber nur, wenn der Sprecher nicht abhaengt von der Antwort.
Georgij ist bei jeder Frage, die er ihr stellt, davon abhaengig.

**Was ausdruecklich KEINE Rolle spielt:** ob ein Fragewort dasteht, und ob das
Hilfsverb umgestellt ist. *"Was I useful."* ist umgestellt und hat einen Punkt,
*"May I ask why not?"* ist umgestellt und hat ein Zeichen. Der Unterschied ist,
wer entscheidet.

**Ein Fragewort am Satzanfang macht noch keine Frage.** Ergaenzt jemand den Satz
eines anderen oder gibt eine Auskunft, ist es eine Aussage und bekommt den
Punkt: *"What she wants is shares, security, and a veto over routes."*, *"When he
bought the boy."*, *"Why I've done any of this."*

**Die einzige weitere Ausnahme** sind Abfertigungen mit Komma und
Redebegleitsatz, die dadurch als Nicht-Frage markiert sind: *"Will I," Annie
said.* Selten benutzen, sonst verliert das Mittel seine Wirkung.

**Nachgezaehlt am 23.08. ueber alle vierunddreissig Kapitel**, und dabei drei
Verstoesse gefunden und behoben: *"May I ask you for something."* in Kapitel 10,
*"May I put something next to it rather than against it."* in Kapitel 7 und
*"Does that include what is already open."* in Kapitel 34. Bei *"May I"* stand es
danach 15 zu 0.

**`check.py` entscheidet das nicht und darf es nicht.** Es meldet
Verdachtsfaelle als Hinweis, weil die Machtlage nicht mechanisch lesbar ist. Ein
Hinweis auf *"What do you want."* ist deshalb kein Fund, sondern die Pruefung,
die ihre Arbeit tut.

---

## Die fuenf Regeln, die am haeufigsten brechen

1. **Georgij sagt nie etwas Unwahres.** Er laesst weg, schmeichelt, schweigt,
   fuehrt durch Auswahl in die Irre. Er sagt nichts Falsches, nie.
2. **Er besitzt nichts.** Kein Geld, kein Konto, keine Beziehungen. Jede Szene,
   in der er etwas kauft, besitzt oder verschenkt, ist ein Fehler.
3. **Ueber sich selbst nennt er keine Zahlen.** Eine Zahl ist ein Datum, und ein
   Datum kann man neben ein anderes legen. Ueber andere ist er praezise.
4. **Kein Satz ueber vierzig Woerter.** `check.py` findet sie.
5. **Zwischen zwei Redebloecken derselben Figur steht immer etwas Koerperliches.**
   Der Beat ist die Sprecherkennzeichnung, keine Verzierung.
6. **Jeder Satz muss etwas tun.** Keine Unterscheidung, die sich selbst aufhebt,
   kein Pronomen ohne Bezug, kein Wortwechsel, in dem sich nichts bewegt.

## Vor jedem Kapitel wird der Inhalt besprochen

Nicht sofort schreiben. Erst den Inhalt vorschlagen, Entscheidungen klaeren,
dann schreiben. Das gilt auch dann, wenn der naechste Schritt offensichtlich
scheint.

---

## Wo was steht

| Datei | Inhalt |
|---|---|
| `doc/01-craft.md` | Alle Regeln. Beginnt mit der Liste, die **immer** laeuft |
| `doc/02-leads.md` | Praemisse, Georgij, Annie |
| `doc/03-cast.md` | Haushalt, Verbuendete, Gegenseite, der Saal |
| `doc/04-world.md` | Das Anwesen und das Geschaeft |
| `doc/05-continuity.md` | Kalender, Kapitelstand, Motive, feste Zeilen |
| `doc/06-plot.md` | Stoffbloecke. Kein Kanon, keine Kapitel |
| `doc/07-next.md` | Naechste Schritte und offene Faeden |
| `doc/08-decisions.md` | Was entschieden wurde und warum |
| `HANDBUCH.md` | **Erzeugt.** Alle acht am Stueck, mit Inhaltsverzeichnis |

## Dateinamen

**Die Versionsnummer im Dateinamen ist Absicht und bleibt.** Nicht aufraeumen,
nicht nach `chNN.md` normalisieren, auch nicht mit dem Hinweis, Git uebernehme
die Versionierung. Ohne die Nummer im Namen faellt die Pruefung weg, die
Dateiname und Kopfzeile gegeneinander stellt.

Beim Aendern eines Kapitels werden **beide** hochgesetzt: Dateiname und
Kopfzeile. Alte Fassungen duerfen in `chapters/` liegen bleiben, `build.py` nimmt
immer die hoechste. Die Einfuegefassung in `paste/` wird nicht von Hand gepflegt,
der Build erzeugt sie und loescht veraltete.

## Was ausserhalb bleibt

Explizite Inhalte werden nicht geschrieben. Die Fassung in diesem Repo ist die
saubere, literarische, und sie ist fuer eine Veroeffentlichungsplattform gedacht.
Was zwischen den beiden geschieht, endet an der Tuer.
