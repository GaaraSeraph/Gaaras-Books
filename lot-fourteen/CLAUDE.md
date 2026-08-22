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
| `canon/01-premise.md` | Praemisse und der Vertrag zwischen den beiden |
| `canon/02-georgij.md` | Die Figur, die Legende, der Charme, das Auge |
| `canon/03-annie.md` | Ihre Methode und ihre Regeln |
| `doc/01-craft.md` | Alle Regeln. Beginnt mit der Liste, die **immer** laeuft |
| `doc/02-leads.md` | Praemisse, Georgij, Annie |
| `doc/03-cast.md` | Haushalt, Verbuendete, Gegenseite, der Saal |
| `doc/04-world.md` | Das Anwesen und das Geschaeft |
| `doc/05-continuity.md` | Kalender, Kapitelstand, Motive, feste Zeilen |
| `doc/06-plot.md` | Stoffbloecke. Kein Kanon, keine Kapitel |
| `doc/07-next.md` | Naechste Schritte und offene Faeden |
| `doc/08-decisions.md` | Was entschieden wurde und warum |
| `HANDBUCH.md` | **Erzeugt.** Alle acht am Stueck, mit Inhaltsverzeichnis |
| `log/01-decisions.md` | Was entschieden wurde und warum |

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
