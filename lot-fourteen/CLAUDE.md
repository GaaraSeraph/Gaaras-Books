# Lot Fourteen

Literarischer Roman, laufende Arbeit. Suedkorea, Gegenwart, Chaebol-Milieu.
Manuskript auf Englisch, Absprachen auf Deutsch.

**Kanon sind die Kapiteldateien `chNN_vX_Y_en.md`.** Alles andere beschreibt sie
oder plant voraus. Wo ein Planungsdokument dem Text widerspricht, hat der Text
recht und das Dokument wird geaendert.

---

## Die Ablage, und diese drei Saetze gelten vor allem anderen

Am 27.08. ist `doc/` umgebaut worden, weil achtzehn Dokumente auf **251.071
Woerter** angewachsen waren - fast so viel wie der Roman - und rund
**dreiunddreissig Prozent davon Sitzungsprotokoll und Nacherzaehlung** waren.
Die Ursache war nicht Unordnung, sondern **eine fehlende Ablageregel**: wer
etwas Neues hatte, haengte es unten an oder legte ein neues Dokument an.

**1. Wohin ein neuer Satz gehoert, entscheidet seine Zeitform.**

| Zeitform | Sorte | Ort |
|---|---|---|
| Praesens ueber die Fiktion | **Kanon** | `1x` |
| Imperativ, bindend beim Schreiben | **Regel** | `2x` |
| Futur, was noch geschehen soll | **Plan** | `3x`, je Band |
| Vergangenheit **mit Datum** | **Protokoll** | `doc/protokoll/` |

**2. Bei einem Widerspruch gilt: Kanon vor Regel vor Plan. Das Protokoll
gewinnt nie.** Ein Bericht sagt, was jemand an einem Tag gemessen oder
beschlossen hat, und ist nie eine Anweisung. Bis zum 27.08. gab es diese Regel
nicht, und als `doc/16` und `CLAUDE.md` sich bei den Fragezeichen
widersprachen, musste das ueber **zweihundert Zeilen** ausgefochten werden.

**3. Kein neues Dokument ohne Sorte.** Wer etwas anzulegen hat, das in keinen
der vier Bloecke passt, hat es falsch verstanden. Die Zehnerstelle ist die
Sorte, und in jedem Block sind Nummern frei.

**`check.py` meldet Verstoesse gegen Satz 1**: eine datierte Ueberschrift in
einer Datei aus `1x` bis `4x` heisst, dass ein Bericht in ein Sachdokument
geschrieben wurde. Es meldet und blockiert nicht.

---

## Zuerst

**`doc/20-handwerk.md` lesen, mindestens den ersten Abschnitt.** Das ist die Liste, die in jedem
Durchgang laeuft: Bandwurmsaetze, ob die Saetze ueberhaupt Sinn ergeben, ob jede
Aussage einen Rueckbezug hat, die Laecheln, die Satzzeichen, die Quoten.

Danach:

1. Das betroffene Kapitel und die zwei davor lesen. Nicht die Zusammenfassung.
2. Bei einer Figurenszene: `doc/11-figuren.md`.
3. Bei einer Verhandlungsszene: `doc/14-welt.md` ganz.
4. Beim Pruefen von Daten und Motiven: `doc/16-motive.md`.
5. **Bei jeder Szene mit einer Nebenfigur: `doc/12-stimmen.md`.** Dort steht,
   was diese Figur will, das mit dem Fall nichts zu tun hat, und wie sie von A
   nach B kommt. Ohne das schreibt man Georgij mit einem anderen Namen davor.
   **Bei einer neuen Nebenfigur zuerst `doc/21-figurenbau.md`** - dort steht,
   woraus eine Figur gebaut wird, und der erste Punkt ist der, der am meisten
   fehlt: ein Zug, der ihr nicht schmeichelt.
6. Bei jeder Szene, in der die beiden einander anfassen: `doc/10-naehe.md`.
   Jede Ruecksicht auf eine fruehere Beruehrung wird dort gegriffen und nicht
   aus dem Gedaechtnis geschrieben.

## Bevor Du etwas abgibst

```
python3 werkzeug/check.py chapters/chNN_vX_Y_en.md
python3 werkzeug/zusagen.py --neu
python3 werkzeug/build.py
```

**`werkzeug/zusagen.py` fuehrt das Schuldbuch in `doc/13-zusagen.md`:** jede
Zusage aus dem Text, mit Faelligkeit in Erzaehltagen und Stand. Ohne Argument
gibt es den Stand und endet mit Rueckgabewert 1, solange etwas ueberfaellig ist.
Mit `--neu` listet es Zusagen mit Frist, die im Buch fehlen; jede wird eingetragen
oder als `KEINE` mit Begruendung abgelegt.

**Warum es das gibt:** am 25.08. sind zwei Zusagen ueberfaellig gefunden worden,
von Hand, Monate zu spaet - die fuenf Firmen aus Kapitel 12 (vier Monate) und
Annies *"You will in about a month"* aus Kapitel 5 (sechs). **Beim ersten Lauf
fand das Skript sofort zwei weitere, die niemand hatte.**

**Wie geprueft wird, steht in `doc/22-pruefen.md`.** Vier Schritte, um aus einem
einzelnen Fund einen Streifzug zu machen, sieben Regeln mit je einem Fehler
dahinter, und der Katalog der Fehlerklassen, die es bisher gibt. Wer einen neuen
Durchgang plant, faengt dort an und nicht bei Null.

`werkzeug/stimmen.py` misst, wie verschieden die Figuren tatsaechlich reden -
Zeilen, Satzlaenge, was jede Figur zaehlt, welche Haustics in ihren Repliken
stehen und wer wen wie anredet. `python3 werkzeug/stimmen.py Jang` gibt alle
sicher zugeordneten Zeilen einer Figur aus. **Zwei Fallen stehen im
Kopfkommentar**, und beide haben mich erwischt: ein Begleitsatz kann innerhalb
einer fremden Replik stehen, weil eine Figur eine andere zitiert - so sind
Georgijs Saetze zweimal in fremde Blaetter geraten. Und in Zweipersonenszenen
laeuft der Dialog ohne Begleitsaetze, eine niedrige Zahl heisst dort also wenig
Begleitsatz und nicht wenig Text.

`zuschreibung.py` sucht **Zuschreibungsfehler**: eine Tat oder ein Satz, der
der falschen Person zugeschrieben ist. Es **eicht sich zuerst selbst** an einem
bekannten Fund und meldet gar nichts, wenn die Eichung durchfaellt. Der
Kopfkommentar erklaert, wie man aus einem einzelnen Fund einen Streifzug macht.

`kuerzen.py` beantwortet die eine Frage, die beim Kuerzen mechanisch
beantwortbar ist: **traegt dieses Kapitel etwas, das nirgends sonst steht?**
Vier Kriterien aus `doc/23-kuerzen.md` - es bezahlt eine Zusage, es steht im
Naehe-Register, es traegt einen Stimmbefund, es enthaelt einen Erstauftritt.
**Ein Kapitel ohne alle vier ist ein Kandidat und keine Streichung**; die
Entscheidung ist Urteil und steht in `doc/23-kuerzen.md`. `--kandidaten` zeigt
nur die Liste, `--form` die Formzahlen je Kapitel.

`doppelt.py` beantwortet die zwei Fragen, die `check.py` nicht stellt, weil sie
ueber Kapitelgrenzen gehen: **was wird mehrfach behauptet, und welcher
Gespraechszug laeuft immer gleich?** `--nester` zeigt Behauptungen, die in drei
oder mehr Kapiteln stehen, `--oeffner` womit Repliken anfangen, `--ketten`
Gespraechsfolgen, die sich wiederholen. **Es entscheidet nicht, ob eine
Wiederholung schaedlich ist** - das Steinbord in Band 1 steht in fuenf Kapiteln
und soll es. Der Befund vom 26.08. steht in `doc/23-kuerzen.md`.

`heft.py` misst das Verhaeltnis, das den Choi-Strang zaeh gemacht hat: **wie oft
wird ins Notizbuch gelegt, und wie oft wird etwas herausgeholt?** Am 26.08.
stand es 167 zu 13. Der Leser sieht sonst ein Konto wachsen, von dem nie
abgehoben wird, und deshalb fuehlt sich die Arbeit nutzlos an, obwohl sie es
nicht ist. **Regel daraus: jede neue Ablage braucht eine spaetere Entnahme, und
wer eine schreibt, notiert wo.**

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
`doc/15-kalender.md`. Dort bekommen Band-2-Zeilen einen Praefix:

```
- **Kapitel 15** *Four thousand two hundred* (v2.7) - ...      <- Band 1
- **Band 2, Kapitel 1** *Titel* (v1.0) - ...                   <- Band 2
```

**Was NICHT getrennt laeuft, und das ist Absicht:** die Dokumente in `doc/`,
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
| `erzeugt/HANDBUCH.md` | Lesefassung aller Regeln und des Kanons. **Erzeugt** |
| `erzeugt/BEGEGNUNGEN.md` | Wer wann vorkommt, mit Tag und Fundstelle. **Erzeugt** |
| `erzeugt/KAPITEL.md` | Eine Zeile je Kapitel: Titel, Fassung, Tag, Datum, Laenge. **Erzeugt** |
| `erzeugt/MANIFEST.txt` | Baubericht. **Erzeugt** |

| Ordner | Was |
|---|---|
| `chapters/` | Die Kapitel von **Band 1**. Kanon |
| `chapters-2/` | Die Kapitel von **Band 2**, wieder ab `ch01`. Kanon |
| `doc/` | Die Quelldokumente, nach Sorte nummeriert. Gelten fuer beide Baende. **Wie viele es sind, steht in `doc/00-readme.md` und wird erzeugt** |
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
Dokument gegen Text. Ein Leser kann 50.000 Woerter plus zehn Dokumente nicht mit
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
3. **Ueber sich selbst nennt er ausserhalb dieses Hauses keine Zahlen.** Eine
   Zahl ist ein Datum, und ein Datum kann man neben ein anderes legen. Ueber
   andere ist er praezise. **Ihr gegenueber gibt er die Zahlen her**, und
   zwar seit Band 1: *"I had ten and I did not need them"* (`b1 ch20:36`),
   *"May I have ten minutes, Mistress"* (`b1 ch16:324`), *"I have been this
   for about three weeks"* (`b2 ch14:208`). **Berichtigt am 29.08.: die Regel
   stand hier ohne die Ausnahme, und der Text hatte sie von Anfang an.**
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
| **Kanon** | *Was im Buch wahr ist. Praesens, nie datiert* |
| `doc/10-naehe.md` | Jede koerperliche Szene zwischen den beiden, mit der Zeile, die im Buch steht |
| `doc/11-figuren.md` | Praemisse, Georgij, Annie, und der ganze uebrige Cast |
| `doc/12-stimmen.md` | Wer wie spricht. Maschine, Anliegen und Verbote je Figur |
| `doc/13-zusagen.md` | Das Schuldbuch. Jede Zusage aus dem Text, mit Faelligkeit und Stand |
| `doc/14-welt.md` | Das Anwesen, der Haushalt, das Geschaeft, das Register |
| `doc/15-kalender.md` | Das Jahr, die Erzaehltage, Geburtstage und Alter |
| `doc/16-motive.md` | Wiederkehrende Bilder und die festgelegten Zeilen |
| **Regeln** | *Was beim Schreiben bindet. Imperativ, nie datiert* |
| `doc/20-handwerk.md` | Alle Regeln. Beginnt mit der Liste, die **immer** laeuft |
| `doc/21-figurenbau.md` | **Wie man eine Figur baut.** Uebertragbar, gilt fuer jedes Buch |
| `doc/22-pruefen.md` | Wie geprueft wird und wer welchen Teil prueft |
| `doc/23-kuerzen.md` | Was jedes Kapitel traegt und was davon kuerzbar ist. **Beim Schreiben zu fuehren, nicht danach** |
| **Plan** | *Was noch geschehen soll. Futur, je Band* |
| `doc/30-plan-band-1.md` | Die Stoffbloecke von Band 1. **Geschrieben, also erledigt** |
| `doc/31-plan-band-2.md` | Ziel, Feldzug, offene Faeden. **Hier duerfen Zeilen stehen, die im Buch nicht stehen** |
| `doc/32-plan-band-3.md` | **Band 3.** Der Chaebol-Angriff, Woos Tod, Los elf |
| `doc/33-plan-band-4.md` | **Band 4.** Sanierung, Werkseintritt, Verlobungsring |
| `doc/34-plan-band-5.md` | **Band 5.** Hochzeit, Unterwelt, das erste Blut |
| `doc/35-plan-band-6.md` | **Band 6.** Kinder, und er fuehrt es. Der duennste, und das ist richtig |
| **Verworfenes** | |
| `doc/40-verworfen.md` | **Nur Verworfenes.** Was versucht und abgelehnt wurde, und was aus dem Text gestrichen ist |
| `doc/41-entscheidungen.md` | Entscheidungen mit Begruendung. **Am 29.08. von 40 getrennt** |
| **Archiv** | |
| `doc/protokoll/` | Alles Datierte. Append-only, **gewinnt nie**, nicht im Handbuch |
| `erzeugt/HANDBUCH.md` | **Erzeugt.** Alle Dokumente am Stueck, mit Inhaltsverzeichnis |

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
