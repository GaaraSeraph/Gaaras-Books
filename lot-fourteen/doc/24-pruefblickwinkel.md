# Pruefblickwinkel

*Regel. Geordnete, endliche Warteschlange fuer Gesamtpruefungen. Imperativ,
nicht datiert.*

Dieses Dokument beantwortet zwei Fragen vor jedem neuen Gesamtdurchgang:

1. Welcher Blickwinkel kommt als Naechstes?
2. Was genau muss unter diesem Blickwinkel geprueft werden?

Erfinde keine neue Pruefmethode, solange in der Tabelle ein offener
Blickwinkel steht. Nimm den ersten Eintrag mit Status **NAECHSTER**, danach den
ersten mit Status **OFFEN**. Aendere den Status erst, wenn ein datiertes,
append-only Protokoll unter `doc/protokoll/` den Umfang, die Gegenproben, die
Befunde und die Umsetzung oder bewusste Nichtumsetzung festhaelt.

---

## Verbindlicher Ablauf

1. Hole vor jeder Aenderung `origin` und pruefe, dass `HEAD` und `origin/main`
   weder vor- noch nachlaufen. GitHub ist bei der Synchronisation fuehrend.
2. Lies den ganzen festgelegten Umfang, nicht nur Suchtreffer oder
   Zusammenfassungen. Kanon sind jeweils die hoechsten Fassungen in den
   Kapitelordnern.
3. Formuliere vor dem Lesen die Fehlerklasse und die Gegenprobe. Ein Fund muss
   sich widerlegen lassen koennen.
4. Belege jeden sicheren Fund mit Kapitel, Wortlaut und Gegenstelle. Trenne
   **SICHER**, **UNSICHER** und **ABSICHTLICH**.
5. Praesentiere Manuskriptaenderungen vor dem Umschreiben, sofern der Autor im
   laufenden Chat nicht ausdruecklich die umgekehrte Reihenfolge freigibt.
   Begleitdokumente duerfen ohne Rueckfrage berichtigt werden.
6. Fuehre nach jeder Umsetzung `check.py`, `zusagen.py --neu` und `build.py`
   aus. Pruefe danach die eigene Aenderung mit demselben Blickwinkel erneut.
7. Lege pro Blickwinkel genau ein neues Protokoll an. Aendere kein altes
   Protokoll.
8. Melde auch einen leeren Durchgang. Nenne dann den geprueften Umfang und die
   staerksten Stellen, an denen ein Fehler vermutet und widerlegt wurde.

---

## Status und Reihenfolge

| Nr. | Blickwinkel | Status | Nachweis |
|---:|---|---|---|
| 1 | Chronologie, Zahlen und harte Kontinuitaet | ERLEDIGT | `protokoll/2026-09-01-kontinuitaet-band-2.md` |
| 2 | Wissensfluss und Vertraulichkeit | ERLEDIGT MIT AUTORENSPERRE | `protokoll/2026-09-01-wissensfluss-band-2.md` |
| 3 | Psychologische Folgekosten | ERLEDIGT | `protokoll/2026-09-02-psychologische-folgekosten-band-2.md` |
| 4 | Entscheidungsfreiheit und kausale Eigenstaendigkeit | ERLEDIGT | `protokoll/2026-09-02-entscheidungsfreiheit-band-2.md` |
| 5 | Raum, Wege, Koerper und Logistik | ERLEDIGT | `protokoll/2026-09-02-raum-logistik-band-2.md` |
| 6 | Gegenstaende, Dokumente und Besitzketten | ERLEDIGT | `protokoll/2026-09-02-gegenstaende-besitzketten-baende-1-bis-3.md` |
| 7 | Institutionen, Recht, Wirtschaft und Verfahren | ERLEDIGT | `protokoll/2026-09-02-institutionen-recht-wirtschaft-verfahren-baende-1-bis-3.md` |
| 8 | Rollen, Vollmachten, Eigentum und Abhaengigkeiten | ERLEDIGT | `protokoll/2026-09-02-rollen-vollmachten-eigentum-abhaengigkeiten-baende-1-bis-3.md` |
| 9 | Figurenstimmen und Machtlage im Dialog | ERLEDIGT MIT AUTORENSPERRE | `protokoll/2026-09-02-figurenstimmen-machtlage-dialog-baende-1-bis-3.md` |
| 10 | Perspektivnaehe und Erzaehlergewissheit | NAECHSTER | - |
| 11 | Szenenfunktion, Kausalbruecken und Redundanz | OFFEN | - |
| 12 | Zusagen, Motive und spaete Auszahlungen | OFFEN | - |
| 13 | Leserwissen und Fairness der Enthuellungen | OFFEN | - |
| 14 | Moralische Rahmung und unbeabsichtigte Entlastung | OFFEN | - |
| 15 | Fehlende Folgen und Handlungen ausserhalb der Szene | OFFEN | - |
| 16 | Banduebergang, Spannungsdruck und neue Bewegungsrichtung | OFFEN | - |

**Autorensperre zu Nr. 2:** Oeffne den im Wissensflussprotokoll beschriebenen
Moon-Befund nicht erneut. Aendere Moons fruehe Namens- oder Wissenslinie nur,
wenn der Autor diese Entscheidung ausdruecklich wieder aufnimmt. Die drei
anderen Befunde dieses Protokolls sind umgesetzt.

**Autorensperre zu Nr. 9:** Band 2, Kapitel 67 behaelt Moons *"Say the rest of
it"*. Die Stelle wurde im Stimmendurchgang ausdruecklich ausgenommen. Oeffne
sie nicht als Restfund des Sprechbefehl-Werkzeugs, solange der Autor diese
Entscheidung nicht ausdruecklich wieder aufnimmt.

---

## 1. Chronologie, Zahlen und harte Kontinuitaet

Pruefe Datum, Wochentag, Alter, Geburtstag, Uhrzeit, Dauer, Entfernung,
Besuchszaehlung, Geld, Mengen, Berufs- und Besitzdauer sowie jede Form von
*first*, *never*, *only* und *since*. Rechne Zeitspannen aus und stelle jede
Zahl neben alle spaeteren Wiederholungen. Trenne Angaben, die verschiedene
Strecken oder Zeitraeume messen, bevor du einen Widerspruch meldest.

Ein Fehler liegt vor, wenn zwei kanonische Angaben denselben Gegenstand messen
und nicht gleichzeitig wahr sein koennen.

## 2. Wissensfluss und Vertraulichkeit

Fuehre fuer Namen, Akten, Briefe, vertrauliche Inhalte, Todesfaelle und
verborgene Verbindungen eine Kette aus **Quelle -> Empfaenger -> Zeitpunkt ->
spaetere Verwendung**. Pruefe die Wissensgrenze der nahen Perspektive und
unterscheide Wissen, Vermutung und Erzaehlerbehauptung.

Ein Fehler liegt vor, wenn eine Figur oder der nahe Erzaehler etwas sicher
weiss, bevor eine sichtbare oder kanonisch belegte Quelle existiert.

## 3. Psychologische Folgekosten

Verfolge nach jeder irreversiblen Handlung Verhalten, Schlaf, Koerper,
Arbeitsweise, Beziehungen, Schuld, Abwehr und neue Grenzen. Pruefe Opfer,
Helfer, Mitwisser und Nebenfiguren mit. Verwechsle Beruhigung nicht mit
Freispruch und Einsicht nicht mit Heilung.

Ein Fehler liegt vor, wenn eine Handlung spaeter folgenlos behandelt wird oder
eine spaetere Reaktion die zuvor gezeigte Verletzung ohne Ereignis aufhebt.

## 4. Entscheidungsfreiheit und kausale Eigenstaendigkeit

Lege fuer jede folgenreiche Entscheidung fuenf Spalten an:

1. Wer entscheidet?
2. Was weiss die Person in diesem Moment?
3. Welche reale Gegenoption besitzt sie?
4. Welcher eigene Grund traegt ihre Entscheidung?
5. Welche Folge muss sie selbst tragen?

Melde nicht jede Unfreiheit als Fehler. Markiere einen Vorgang als
**ABSICHTLICH UNFREI**, wenn Manipulation, Abhaengigkeit oder fehlende
Ausweichmoeglichkeit Gegenstand der Szene sind und der Text den Preis kennt.

Ein Fehler liegt vor, wenn der Plot ein Ergebnis braucht, die Figur aber weder
einen eigenen Grund noch eine tragende Wahl hat, oder wenn der Text spaeter
eine erzwungene bzw. uninformierte Handlung als freie Entscheidung abrechnet.

## 5. Raum, Wege, Koerper und Logistik

Zeichne fuer jede Szene Ort, Ein- und Ausgang, Stockwerk, Sichtlinie,
Sitzordnung, Fahrzeug, Fahrer, Abfahrts- und Ankunftszeit. Pruefe, wer wen sehen
oder hoeren kann, wo Haende und Gegenstaende liegen und ob ein Koerper die
beschriebene Bewegung aus der vorherigen Position ausfuehren kann. Rechne
Fahrten gegen die im Buch gesetzten Reisezeiten, nicht gegen eine geschaetzte
Landkarte.

Ein Fehler liegt vor, wenn eine Person, ein Blick, ein Geraeusch oder ein
Gegenstand eine nicht gezeigte Raumgrenze ueberspringt.

## 6. Gegenstaende, Dokumente und Besitzketten

Fuehre fuer jedes wiederkehrende Objekt und jedes Papier eine Kette aus
**Erzeugung -> Besitz -> Einsicht -> Kopie -> Transport -> Verwahrung ->
Vernichtung**. Pruefe besonders Notizbuecher, Akten, Formulare, Briefe,
Kataloge, Registerseiten, Zertifikate, Schluessel, Fahrzeuge und medizinische
Lieferungen.

Ein Fehler liegt vor, wenn jemand ein Objekt haelt, liest, kopiert oder
vernichtet, ohne dass es in seine Reichweite gelangt ist, oder wenn Original
und Kopie spaeter vertauscht werden.

## 7. Institutionen, Recht, Wirtschaft und Verfahren

Pruefe jeden Mechanismus innerhalb des gesetzten Romansystems: Trust,
Treuhandpflicht, Register, Auktion, Wind-up, Arbeitsvertrag, Kauf, Miete,
Versicherung, Behoerde und Berufsaufsicht. Frage, wer unterschreiben darf,
welches Papier die Handlung ausloest, welcher Anreiz jede Partei bewegt und
welcher Preis oder Nachteil bestehen bleibt.

Melde reale Rechtsfragen nur dann als Tatsachenfehler, wenn sie belegt sind.
Trenne sonst **interne Unstimmigkeit** von **Recherchebedarf**.

## 8. Rollen, Vollmachten, Eigentum und Abhaengigkeiten

Pruefe fuer jede Handlung, in welcher Rolle die Figur handelt: Eigentuemer,
Kaeufer, Angestellter, Vertreter, Treuhaender, Gast, Hausherr oder Privatperson.
Pruefe ausdrueckliche und stillschweigende Vollmachten, Georgijs Besitzlosigkeit,
Annies Entscheidungshoheit sowie jede spaetere Aenderung eines
Abhaengigkeitsverhaeltnisses.

Ein Fehler liegt vor, wenn eine Figur verfuegt, verspricht, kauft, beauftragt
oder Zugang gewaehrt, obwohl ihre aktuelle Rolle das nicht traegt.

## 9. Figurenstimmen und Machtlage im Dialog

Pruefe jede zentrale und jede Nebenfigur gegen `doc/12-stimmen.md`. Vergleiche
Wortwahl, Satzlaenge, Zahlengebrauch, Anrede, Ausweichbewegung und das, was die
Figur unabhaengig vom Plot will. Pruefe Punkt und Fragezeichen pro Replik nach
der aktuellen Machtlage, nicht nach Rang oder Kaelte.

Ein Fehler liegt vor, wenn mehrere Figuren dieselbe Georgij- oder
Annie-Bewegung ausfuehren, eine Nebenfigur nur Informationen liefert oder die
Interpunktion eine Antwort erzwingt, die in der Szene verweigert werden kann.

## 10. Perspektivnaehe und Erzaehlergewissheit

Markiere pro Absatz, ob er Wahrnehmung, Schluss, Erinnerung,
Erzaehlerueberblick oder spaetere Vorausblende ist. Pruefe, ob Gewissheit und
Zeitform zu dieser Ebene passen. Achte besonders auf Saetze ueber ungesehene
Privatraeume, fremde Gedanken und zukuenftige Folgen.

Ein Fehler liegt vor, wenn ein naher Absatz ohne Signal allwissend wird oder
eine Vermutung grammatisch als Tatsache erscheint.

## 11. Szenenfunktion, Kausalbruecken und Redundanz

Schreibe fuer jede Szene in einem Satz: **Ausloeser -> Entscheidung -> neue
Lage**. Markiere Szenen, in denen kein Glied wechselt. Vergleiche wiederholte
Verhandlungen, Berichte, Anfahrten, Notizbucheintraege und spaete Abrechnungen.
Nutze `doppelt.py`, `heft.py` und `kuerzen.py` als Hinweise, nie als Urteil.

Ein Fehler liegt vor, wenn eine notwendige Kausalbruecke fehlt oder eine Szene
nur eine bereits vollstaendig ausgefuehrte Bewegung wiederholt.

## 12. Zusagen, Motive und spaete Auszahlungen

Pruefe jede Zusage mit `zusagen.py` und `doc/13-zusagen.md`. Fuehre fuer Motive
aus `doc/16-motive.md` die Kette **Setzung -> Variation -> Auszahlung**.
Pruefe auch negative Zusagen wie *nicht wiederkommen*, *nicht fragen* und
*nicht erzaehlen*.

Ein Fehler liegt vor, wenn eine faellige Zusage unbemerkt bleibt, eine
Auszahlung ohne Setzung erscheint oder ein Motiv nur wiederholt wird, ohne
seine Bedeutung zu veraendern.

## 13. Leserwissen und Fairness der Enthuellungen

Trenne diesen Durchgang vom reinen Figurenwissen. Frage, welche Spur der Leser
vor einer Enthuellung besitzt, welche falschen Deutungen fair moeglich sind und
ob die Aufloesung aus gezeigten Teilen entsteht. Pruefe, ob ein spaeter
entscheidendes Detail erst im Moment seiner Verwendung eingefuehrt wird.

Ein Fehler liegt vor, wenn eine Enthuellung nur durch neue Information
funktioniert, die vorher weder sichtbar noch als Luecke markiert war.

## 14. Moralische Rahmung und unbeabsichtigte Entlastung

Pruefe, wem der Erzaehler Praezision, Guete, Notwendigkeit oder Unvermeidbarkeit
zuschreibt. Suche nach Unterlassungen, die als Verdienst erscheinen, nach
Leid, das nur die Hauptfigur vertieft, und nach Konsequenzen, die Verantwortung
zu schnell in Tragik verwandeln.

Ein Fehler liegt vor, wenn die Prosa eine Handlung freispricht, obwohl Szene
und Kanon ihren Preis setzen, oder ein Opfer nur zur moralischen Entwicklung
des Handelnden dient.

## 15. Fehlende Folgen und Handlungen ausserhalb der Szene

Liste jede off-page Handlung und jede grosse Veraenderung zwischen zwei
Kapiteln. Pruefe, ob mindestens eine sichtbare Spur existiert: Verhalten,
Papier, Geld, Geruecht, Beziehung, Arbeitsablauf oder Raum. Frage auch, welche
naheliegende Reaktion ausbleibt und ob der Text dafuer einen Grund setzt.

Ein Fehler liegt vor, wenn ein Ergebnis ohne tragende Zwischenursache eintritt
oder eine gesellschaftliche, berufliche oder persoenliche Folge verschwindet,
obwohl der Text sie zuvor unvermeidbar gemacht hat.

## 16. Banduebergang, Spannungsdruck und neue Bewegungsrichtung

Lies das letzte Fuenftel von Band 2 zusammen mit den ersten Kapiteln von Band 3.
Pruefe, was abgeschlossen, offen, absichtlich nachwirkend und neu ausgeloest
ist. Stelle sicher, dass Band 3 weder Band 2 wiederholt noch dessen moralische
Rechnung loescht. Pruefe, ob der neue Gegner eine andere Art von Problem
erzeugt und ob Georgijs bisherige Methode deshalb wirklich an eine Grenze
kommt.

Ein Fehler liegt vor, wenn der neue Band nur eine groessere Fassung des alten
Konflikts beginnt, eine offene Folge vergisst oder eine bereits bezahlte
Enthuellung erneut als neu verkauft.

---

## Abschluss eines Durchgangs

Schreibe ins neue Protokoll:

- Git- und Manuskriptstand;
- Kapitel- und Wortumfang;
- Fehlerdefinition und Gegenprobe;
- sichere, unsichere und absichtliche Befunde;
- konkret geaenderte Stellen oder den Grund fuer keine Aenderung;
- naechsten offenen Blickwinkel aus dieser Tabelle.

Setze danach genau einen offenen Eintrag auf **NAECHSTER**. Lass nie zwei
Eintraege zugleich auf **NAECHSTER** stehen.
