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
Datumszeilen, Versionsnummern. `build.py` erzeugt `paste/`, `book.md`,
`HANDBUCH.md` und `MANIFEST.txt` neu und bricht ab, wenn Dateiname und Kopfzeile
auseinanderlaufen.

Beides laeuft ausserdem von selbst: als Hook vor jedem Commit und als GitHub
Action bei jedem Push. Der Hook baut und **blockiert bei einem Build-Fehler**,
die Kapitelpruefung warnt nur.

## Ordnung

| Oben | Was |
|---|---|
| `CLAUDE.md` | Diese Datei. Die einzige oben, die von Hand bearbeitet wird |
| `book.md` | Lesefassung der Geschichte. **Erzeugt** |
| `HANDBUCH.md` | Lesefassung aller Regeln und des Kanons. **Erzeugt** |
| `BEGEGNUNGEN.md` | Wer wann vorkommt, mit Tag und Fundstelle. **Erzeugt** |
| `MANIFEST.txt` | Baubericht. **Erzeugt** |

| Ordner | Was |
|---|---|
| `chapters/` | Die Kapitel. Kanon |
| `doc/` | Die acht Quelldokumente |
| `paste/` | Einfuegefassungen. **Erzeugt**, nie bearbeiten |

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
braucht: Zahlen quer ueber siebzehn Kapitel, Zeitangaben gegen den Kalender,
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
