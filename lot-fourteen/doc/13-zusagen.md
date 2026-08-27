# Das Schuldbuch

Jede Zusage, die im Text gemacht wird, mit Fälligkeit und Stand. Wird von Hand
geführt und mit `werkzeug/zusagen.py` gegen den Erzählkalender gerechnet.

---

## Warum es das gibt

**Am 25.08. sind zwei Zusagen als überfällig gefunden worden, beide von Hand,
beide Monate zu spät.**

Die fünf Firmen aus Kapitel 12 (3. April): *„When it is over the other five will
be yours, completely, not as customers and not as an arrangement."* Der Verband
kam in vierundvierzig Kapiteln nicht mehr vor.

**Und beim Bezahlen ist der zweite Fehler aufgefallen, der schlimmer war als der
erste.** Ich hatte die Zusage zuerst in Kapitel 69 eingelöst, im September. Der
Autor: *„Kapitel 69 ist ein bisschen spät, meinst Du nicht? Das sollte als
immediate win dastehen, nachdem ich fertig bin mit der Dame mit vier Trucks."*

Er hat recht, und die Zusage sagt es selbst: *„in about three weeks they are going
to be extremely grateful to somebody. That somebody can be you and it will cost
you nothing you have not already spent."* **Das ist Dankbarkeit, sofort, umsonst**
- und keine Eigentumsübertragung. Sie gehört an den 30. April, in denselben
Bericht wie Nam Byung-hees Ende. **Jetzt steht sie in Kapitel 20**, siebenundzwanzig
Tage nach der Zusage und drei vor der Frist.

**Was in Kapitel 69 übrigbleibt, ist die kleinere und wahrere Schuld:** Annies
Anschlussauftrag vom selben Abend, den Georgij mit *„It will keep"* verschoben hat.
Fünf Männer, denen niemand gesagt hat, dass sie nichts schulden. Kwon fährt im
September vier Stunden, um zu fragen, was der Preis ist.

Annies *„You will in about a month"* aus Kapitel 5 (11. März), fällig Anfang
April, offen bis September. Sechs Monate.

**Beide standen im Text und in keiner Liste.** Das ist derselbe Fehlertyp wie die
falschen Rückverweise, die zu `doc/10-naehe.md` geführt haben, und wie die
behaupteten Stimmen, die zu `doc/12-stimmen.md` geführt haben: **was nicht
gemessen wird, driftet.**

---

## Wie man es führt

Eine Zeile je Zusage, und das Format ist maschinenlesbar. Wer es ändert, ändert
den Ausdruck in `zusagen.py` mit.

```
- [OFFEN] **B2 12** Georgij an Annie · gesagt Tag 182 · faellig Tag 210 · "Zitat" · -
```

- **Status**: `OFFEN`, `BEZAHLT` oder `VERFALLEN`. Verfallen heißt: die Figur hat
  die Zusage gebrochen und **der Text weiß das**. Eine gebrochene Zusage, die der
  Text nicht bemerkt, ist offen und nicht verfallen.
- **Fälligkeit**: entweder `Tag N` in Erzähltagen oder `bei <Ereignis>`.
  **`offen` gibt es seit dem 25.08. nicht mehr**, und das ist die Antwort auf
  einen Einwand des Autors: eine Zusage ohne genannte Frist hat trotzdem einen
  Auslöser - *wenn sie herauskommt*, *wenn es vorbei ist*, *wenn er den Namen
  hat*. Wer den nicht hinschreibt, kann später nicht prüfen, ob er eingetreten
  ist, und die Zusage ist dann kein offener Faden, sondern ein unsichtbarer.
  `zusagen.py` listet beide Sorten getrennt und **meldet jede Zeile, die weder
  einen Tag noch ein Ereignis trägt**, mit Rückgabewert 1.
- **Eingelöst**: das Kapitel, das sie bezahlt, oder `-`.

**Nach jedem geschriebenen Kapitel:**

```bash
python3 werkzeug/zusagen.py --neu
```

Das listet Zusagen mit Frist, die im Buch fehlen. Jede wird eingetragen oder es
wird hier begründet, warum sie keine ist.

**Und `zusagen.py` ohne Argument gibt den Stand.** Überfällig, offen, bezahlt.
Es endet mit Rückgabewert 1, solange etwas überfällig ist.

---

## Was das Werkzeug nicht kann

**Es entscheidet nicht, ob etwas eine Zusage ist.** Das ist Urteil und bleibt es.

**Und `--neu` findet nur Zusagen mit einer Frist im selben Satz.** *„I am going to
have him before the end of the year"* wird gefunden. *„I will not tell him"* nicht.
Fristlose Zusagen kommen von Hand hier hinein, mit `faellig offen`.

Das ist Absicht und folgt Regel 8 aus `doc/22-pruefen.md`: ein Detektor, der jeden
Satz mit *I will* meldet, ist so wertlos wie einer, der nichts meldet. **Diese
Fassung meldet lieber zu wenig und verlässt sich darauf, dass die Liste gepflegt
wird.**

---

## Offen

- [KEINE] **B2 58** Annie an Georgij · gesagt Tag 319 · faellig bei nichts · "I will have to buy a consignment from a house that is going to be finished by Christmas" · Dieselbe Zusage steht weiter unten als BEZAHLT. `--neu` meldet sie noch einmal, weil sie im Kapitel mit einem Komma endet und der Wortlaut im Buch ohne eines steht
- [KEINE] **B2 83** Georgij an Mrs Jeon · gesagt Tag 385 · faellig bei nichts · "I will have a day when the placing party has the form" · Keine Zusage, sondern eine Auskunft ueber den Stand eines fremden Verfahrens. Der Termin selbst steht als eigener Posten im Buch


- [BEZAHLT] **B2 19** Georgij an Sang-hoon · gesagt Tag 209 · faellig Tag 453 · "I am going to have him before the end of the year." · **B2 88 und B2 90, und der Weg dahin ist die ganze Frage.** Am 6. November im Wagen dreht er die Bedeutung von *nehmen*: Choi besitzt nichts, also ist ihm nichts **abzunehmen** - aber er hat neun Leute angehaeuft, die nicht wissen, was er ihnen angetan hat, und die sind ihm **wegzunehmen**. *"I am going to have him."* Bezahlt zwischen dem 9. und dem 19. November mit neun Telefonaten aus dem Gang hinter der Kueche. **Am 20. November, auf ihre Frage: *"I have had him."***
- [BEZAHLT] **B2 88** Choi Dae-ho an Annie · gesagt Tag 399 · faellig Tag 404 · "You will send somebody on the eleventh and they will bring her." · B2 89, am Mittwoch, und es hat den ganzen Tag gedauert
- [BEZAHLT] **B2 65** Georgij an Mrs Sunwoo · gesagt Tag 333 · faellig bei dem Ende des Feldzugs gegen Choi · "you will tell me the whole of it and not the comfortable part" · B2 89, am 19. November, fuenfzig Minuten. **Sie hat fuenfzig Minuten auf die Stelle gewartet, an der jemand klug war, und es gibt keine**
- [BEZAHLT] **B2 74** Georgij an Sim · gesagt Tag 348 · faellig bei dem Ende des Feldzugs gegen Choi · "You will be told, and you will not be told the comfortable part of it." · B2 89, am Freitag in Jongno, eine Stunde zehn, und der Tee stand bereit
- [BEZAHLT] **B2 67** Sim an sich selbst · gesagt Tag 339 · faellig bei dem Tag, an dem die Frau in Gangwon-do ihn nicht mehr braucht · "After the fourteenth I am finished." · B2 89: die Leitung ist seit dem 30. September tot, sie ist seit dem 2. November heraus, und er hat keinen Auftrag mehr angenommen
- [OFFEN] **B2 89** Georgij an Moon Hae-sook · gesagt Tag 409 · faellig bei jedem einzelnen der achtundfuenfzig · Was aus den Eingeladenen geworden ist. **Am Bandende offen, und der Text weiss es** - B2 90, in seiner eigenen Rechnung am Schluss: *"The other fifty-eight are in the back of the book and I am going to be at this for years."*
- [BEZAHLT] **B2 67** Georgij an Sim · gesagt Tag 339 · faellig Tag 346 · "There is a difference. You will not be able to hear it and she will." · B2 72: sie sagt am 14. seinen Namen, zum ersten Mal in vier Jahren. **Sim und Mr Ahn lesen es als Abschied, und keiner von beiden war am siebten in dem Zimmer** (Notiz im Wagen, B2 74 v1.1)
- [BEZAHLT] **B2 67** Sim an Georgij · gesagt Tag 339 · faellig Tag 346 · "I am going to make it because on the fourteenth of September a woman in a house in Gangwon-do will be waiting for a telephone to ring." · B2 72, am Tag, zehn nach fuenf, sechsundzwanzig Minuten
- [BEZAHLT] **B2 70** Mr Ahn an Georgij · gesagt Tag 342 · faellig Tag 347 · "It will be ready Tuesday." · B2 73, am Dienstag, mit Kabel aufgerollt und Tuch runter
- [BEZAHLT] **B2 58** Annie an Georgij · gesagt Tag 319 · faellig Tag 322 · "Put it in front of me on Friday. Not today." · B2 60: *"He put all of it in front of Annie at seven on the Friday evening"* - am Tag. **Stand bis zum 25.08. falsch als offen und mit falschem Kapitel und Tag im Buch.**
- [BEZAHLT] **B2 69** Annie an Georgij · gesagt Tag 341 · faellig Tag 342 · "You are going tomorrow, and you are not going with anything." · B2 70, am naechsten Morgen
- [BEZAHLT] **B2 61** Woo an Georgij · gesagt Tag 324 · faellig offen · "You have until she asks." · B2 74: **die Frist ist am Tag 350 abgelaufen.** Sechsundzwanzig Tage. Sie fragt am Ende des Kapitels, und zwar weil sie einen Mann bepreisen muss und nicht weil sie etwas gemerkt hat
- [BEZAHLT] **B2 32** Mrs Jeon an Georgij · gesagt Tag 242 · faellig Tag 273 · "I have four months of money and a son who is going to offer next month, and I am going to take it." · B2 71, siebzig Tage spaet: der Sohn hat am 3. Juli angeboten, sie hat die Haelfte genommen (die Miete, nicht das Zimmer) und sagt selbst, dass sie nicht weiss, ob das ehrlich ist
- [BEZAHLT] **B2 58** Annie an Georgij · gesagt Tag 319 · faellig Tag 326 · "in about a week you will have found a way to make it about you and I would like to have said this first" · B2 70, sechzehn Tage spaet, und nicht sie sagt es ihm, sondern Mr Ahn
- [BEZAHLT] **B2 71** Mrs Jeon an Georgij · gesagt Tag 343 · faellig Tag 346 · "I will telephone Gwangyang on Monday." · B2 72, am Montag um zwanzig nach zehn und nicht am Abend
- [BEZAHLT] **B2 74** Annie an Georgij · gesagt Tag 350 · faellig Tag 353 · das Geld soll bis zum Zweiundzwanzigsten auf einem eigenen Konto liegen · B2 76, am Montag, in vierzig Sekunden auf dem Weg zum Wagen: ein Konto bei einer Bank, die sie sonst nicht benutzt, ihr Name darauf, sonst nichts darin. **Woher es kommt, sagt sie nicht, und er fragt nicht**
- [BEZAHLT] **B2 77** Annie an Georgij · gesagt Tag 360 · faellig Tag 364 · "I will tell you on Friday who he is." · B2 78, am Freitag um neun, im Stehen: **Chairman Woo**, und es sind vier Fragen, die sie ihm nicht stellen wird
- [OFFEN] **B2 78** Chairman Woo an Annie · gesagt Tag 367 · faellig bei seinem Tod · vier Antworten in seiner Handschrift, beim Anwalt, versiegelt, "and not one hour before" · **Die einzige Zusage im Buch mit einem Termin, den niemand nachschlagen kann.** B2 90 bestaetigt nur, dass der Umschlag existiert
- [BEZAHLT] **B2 78** Annie an Georgij · gesagt Tag 367 · faellig Tag 369 · "He is going to write them tonight." · B2 80: am Mittwoch kommt nichts und am Donnerstag auch nicht, und Georgij rechnet aus, dass genau das die Bestaetigung ist
- [KEINE] **B2 80** Georgij an Annie · gesagt Tag 371 · faellig bei einer Absage von Mr Hwang · "If he refuses after that, we do not go back." · **Der Ausloeser ist nie eingetreten:** Hwang hat in B2 81 in etwa vierzig Sekunden zugesagt. Die Selbstbindung steht damit ungeprueft im Buch, und das ist ihr Zustand und kein Versaeumnis
- [BEZAHLT] **B2 80** Annie an Georgij · gesagt Tag 371 · faellig Tag 377 · Donnerstag neun Uhr bei Mr Hwang, und **er geht allein** · B2 81, zwei Minuten vor neun
- [BEZAHLT] **B2 80** Annie an Georgij · gesagt Tag 371 · faellig Tag 377 · Mr Hwang wird **in derselben Stunde** auch nach Moon Hae-sook gefragt · B2 81, im Stehen, bevor er geht. **Die Antwort ist: nichts.** Kein Los, keine Nummer, kein Eintrag im ganzen Haus
- [BEZAHLT] **B2 32** Mr Hwang an Georgij · gesagt Tag 238 · faellig bei dem Tag, an dem die Seite existiert · Er moechte, dass irgendwo auf der Welt ein Blatt existiert, das sagt, dass sie das Buch hingehalten hat und er es nicht genommen hat · B2 81: **Georgij sagt ihm, dass es existiert, und weigert sich, ihm eine Zeile daraus vorzulesen**, weil Mrs Jeon es an die Bedingung geknuepft hat, es nicht zu benutzen
- [BEZAHLT] **B2 81** Georgij an Mr Hwang · gesagt Tag 377 · faellig Tag 384 · "Come back with an answer about the series and do not take longer than a week about it." · B2 82, am Donnerstag um zwanzig nach acht, sieben Tage nach der Frage. **Die Antwort ist ja, in einem Wort und ungeschmueckt**
- [BEZAHLT] **B2 81** Mr Hwang an Georgij · gesagt Tag 377 · faellig bei dem Tag, an dem das Formular kommt · Er unterschreibt die Abtretung, sobald Weisung, Preis und vier Seiten da sind · B2 86: gegengezeichnet am Freitag, dem 30. Oktober, an seinem eigenen Schreibtisch, mit niemandem im Gebaeude
- [BEZAHLT] **B2 78** Annie an Georgij · gesagt Tag 364 · faellig Tag 367 · "Monday, at ten... And you are going to be in the room." · **im selben Kapitel**, seit der Zusammenlegung: vier Minuten vor zehn, und sie nimmt nichts mit
- [BEZAHLT] **B2 77** Sim an Georgij · gesagt Tag 360 · faellig Tag 363 · "I will telephone that number on Thursday to find out whether it still exists." · B2 78, dreimal an einem Abend: einundvierzig Klingelzeichen, dann nichts, dann der Ton. **Die Nummer ist weg**
- [KEINE] **B2 75** Annie an die vier Spediteure · gesagt Tag 350 · faellig offen · "if anybody ever tells them otherwise they are to be shown the letter" · **Keine Zusage mit Faelligkeit, sondern eine Buergschaft ohne Ablauf.** Eingeloest in dem Moment, in dem der Brief existiert, und nie faellig
- [OFFEN] **B2 73** Mr Ahn an sich selbst · gesagt Tag 347 · faellig bei Ahn Jung-hees Rueckkehr · "It goes in that corner and it stays there... until she comes in here and switches it off herself." · -
- [BEZAHLT] **B2 73** Georgij an Mr Ahn · gesagt Tag 347 · faellig offen · Er soll Sim fragen, wie lange es sonst dauert, sie ans Telefon zu holen · B2 74, am naechsten Morgen in Jongno: Schnitt sechs Minuten, kuerzeste vier zehn, laengste elf am 27. August, und am 14. September einundvierzig Sekunden
- [BEZAHLT] **B2 72** Sim an Georgij · gesagt Tag 346 · faellig Tag 360 · "I am telephoning that house again on the twenty-eighth." · B2 77, am Tag, zehn nach fuenf, und er kuendigt im selben Gespraech den naechsten fuer Donnerstag an
- [BEZAHLT] **B2 72** Annie an Georgij · gesagt Tag 346 · faellig Tag 350 · "It will be decided on Friday and it will be decided in this room." · B2 74, am Freitag um neun, in vier Teilen und mit einer Zahl
- [BEZAHLT] **B2 71** Mrs Jeon an Georgij · gesagt Tag 343 · faellig Tag 363 · "The start date will be the first of October." · B2 78, am Donnerstag. **Niemand in dem Haus weiss etwas ueber den Tag ausser dem Datum**, und Georgij telefoniert absichtlich nicht
- [BEZAHLT] **B2 71** Georgij an Mrs Jeon · gesagt Tag 343 · faellig Tag 385 · "I will come in October." - "Say the date." - "The twenty-third." · B2 83, am Tag, mit dem ersten Zug, vierhundert Kilometer, und wieder ohne etwas
- [BEZAHLT] **B2 71** Georgij an Mrs Jeon · gesagt Tag 343 · faellig bei dem Tag, an dem er den Namen hat · "You will tell me her name before I am in the room with her. Not the reference. The name, and how it is written, and which part of it her mother used." · B2 83, alle drei Teile. **Den dritten hat Mr Ahn am Dienstagabend gegeben und vierzig Sekunden dafuer gebraucht**
- [BEZAHLT] **B2 83** Georgij an Mrs Jeon · gesagt Tag 385 · faellig bei dem Tag, an dem er den Tag hat · "I will telephone you with the day, and it will be the day I have it and not the day after." · B2 85, vierzig Minuten nach der Bestaetigung. **Sie sagt, sie habe diesen Satz seit 1998 etwa vierhundertmal gehoert und zweimal gehalten bekommen**
- [BEZAHLT] **B2 85** Georgij an Mrs Jeon · gesagt Tag 391 · faellig Tag 394 · Die vier Seiten am Sonntagabend, in einem Raum mit Licht, zwei Stunden, niemand in der Tuer · B2 86, um sieben abgegeben, und um zehn nach neun ruft sie an: zwei Woerter im dritten Absatz, die man im Lesen falsch nehmen kann
- [BEZAHLT] **B2 84** Mr Ahn an Georgij · gesagt Tag 388 · faellig bei dem Tag, an dem sie geholt wird · "whoever is in the car has about four minutes... and it had better not be a man" · B2 86: Mrs Jeon spricht als Erste und Georgij steigt nicht aus
- [BEZAHLT] **B2 63** Georgij an Mr Ahn · gesagt Tag 326 · faellig bei der Raeumung des Hauses · "Somebody is going to stand underneath her before anybody takes the floor away." · B2 86, am 2. November, elf Uhr, und die Raeumung hatte am Donnerstag angefangen
- [BEZAHLT] **B2 86** Mrs Jeon an Ahn Jung-hee · gesagt Tag 395 · faellig Tag 397 · "One, tomorrow or the day after. I will read it to you first and I will read the third paragraph twice." · B2 87, am Mittwoch um zehn, fuenfzig Minuten, und der dritte Absatz zweimal
- [BEZAHLT] **B2 58** Georgij an Annie · gesagt Tag 319 · faellig bei der ersten Stunde nach der Uebergabe · "she is told that in the first hour by somebody who is not you and not me" · B2 87: zwei Menschen im Raum, Annie eine Etage hoeher mit offener Tuer, Georgij am Ende des Gangs ausser Hoerweite
- [BEZAHLT] **B2 71** Mrs Jeon an Georgij · gesagt Tag 343 · faellig bei der ersten Stunde nach der Uebergabe · Sie nimmt sie an · B2 87, und sie liest nichts zusammen und sagt an keiner Stelle, was es bedeutet
- [BEZAHLT] **B2 82** Georgij an Baek Jun-ho · gesagt Tag 382 · faellig bei dem Tag nach Ahn Jung-hees Herauskommen · Er erfaehrt den Namen des Errichters erst danach · B2 87: am Tag danach angerufen, und Baek kommt am Mittwoch um zwei persoenlich
- [OFFEN] **B2 87** Georgij an Annie · gesagt Tag 397 · faellig bei dem Tag, an dem Baek die Urkunde herausgibt · Datum und Wortlaut der zweiten Korrektur, ohne Umschreibung · **Am Bandende offen, und der Text weiss es**
- [BEZAHLT] **B1 32** Georgij an die sechs · gesagt Tag 80 · faellig Tag 80 · "I am going to say it again now to all six, in the same words, because I promised" · B1 32 selbst: der Satz **ist** die Einloesung, er sagt es im selben Atemzug an alle sechs. **Stand bis zum 25.08. als aeltester offener Posten im Buch und war nie einer.**

## Bezahlt

- [KEINE] **B2 74** Georgij an Annie · gesagt Tag 350 · faellig offen · "you have told her you will be at her table on the twenty-third" · Keine neue Zusage, sondern die Wiedergabe von B2 71. `--neu` findet sie, weil der Wortlaut abweicht
- [BEZAHLT] **B2 32** Mrs Jeon an Georgij · gesagt Tag 242 · faellig offen · "I will write one page and I will sign it and I will put the date on it, and it goes to you." · B2 71: geschrieben am 14. Juni, neunundachtzig Tage in der Schublade, weil sie nicht postet, was ueber einen Tisch gehoert
- [BEZAHLT] **B2 12** Georgij an Annie · gesagt Tag 182 · faellig Tag 216 · "When it is over the other five will be yours, completely, not as customers and not as an arrangement." · B2 20, am 30. April, siebenundzwanzig Tage nach der Zusage und drei vor der Frist
- [BEZAHLT] **B2 20** Annie an Georgij · gesagt Tag 209 · faellig offen · "Go back and tell all five that they do not owe me anything." · **Einer in B2 69 (Kwon, und nur weil er selbst vorfuhr), die anderen vier in B2 75, einhunderteinundvierzig Tage spaet und nicht von ihm.** **Und in B2 76 kommt einer der vier zurueck:** Mr Pyeon schickt ihn am Tag des Empfangs ungeoeffnet-wieder-gefaltet zurueck, weil ein unterschriebenes Blatt aus diesem Haus in seinem Hof keine Quittung ist, sondern eine Beziehung. **Die Zusage bleibt bezahlt - die Form war der Fehler und nicht die Bezahlung.** Sie schreibt vier Briefe von Hand, unterschrieben und datiert, ohne Briefkopf; Mrs Seo verschickt sie aus vier verschiedenen Orten und erfaehrt nicht, was drinsteht
- [BEZAHLT] **B2 05** Annie an Georgij · gesagt Tag 159 · faellig Tag 190 · "You do not yet. You will in about a month." · B2 69, 151 Tage zu spaet, von ihr selbst und mit Begruendung fuer die Wartezeit
- [BEZAHLT] **B1 31** Annie an Georgij · gesagt Tag 74 · faellig Tag 164 · "I will ask you again in March, and you will not be able to say it is not the moment, because in March it will be." · B2 06, am 16. Maerz, auf den Tag drei Monate. **Stand bis zum 25.08. ueberhaupt nicht im Schuldbuch und war neun Erzaehlmonate unbezahlt** - gefunden bei der Suche nach fristlosen Zusagen, weil `--neu` sie nicht sieht
- [KEINE] **B2 06** Annie an Georgij · gesagt Tag 164 · faellig bei nichts · "You are mine... It has no end on it. Build on this one." · **Kein Posten mit Faelligkeit, sondern ein Zustand.** Sie kann ihn nicht erfuellen, nur brechen; ein Bruch waere VERFALLEN und keine Ueberfaelligkeit. Steht hier, damit er nicht als vergessener Faden wiederkommt
- [BEZAHLT] **B1 24** Georgij an Annie · gesagt Tag 55 · faellig Tag 149 · "on the second of March I will hand it back to you" · B2 01, am zweiten Maerz, auf den Tag
- [BEZAHLT] **B1 09** Hana an Georgij · gesagt Tag 22 · faellig Tag 52 · "In about a month she and I are going to need each other rather badly" · B1 20, neunzehn Tage spaeter, und Georgij zaehlt sie im Text nach
- [BEZAHLT] **B1 24** Annie an Georgij · gesagt Tag 55 · faellig Tag 58 · "Monday. Named, capped, and it dies on the first of March." · B1 25
- [BEZAHLT] **B2 12** Georgij an Annie · gesagt Tag 182 · faellig Tag 203 · "I want her. Not the letter, not the lane, not an apology, and not a settlement." · B2 19 und 20, Nam Byung-hee am 23. April
- [BEZAHLT] **B2 09** Georgij an Annie · gesagt Tag 168 · faellig Tag 217 · "Mrs Jeon at the settlement desk, who is out in seven weeks anyway and who I am going to be able to do something about" · B2 32, sie gibt das Buch her und behaelt die Entscheidung
- [BEZAHLT] **B2 57** Woo an Georgij · gesagt Tag 318 · faellig Tag 322 · "I will come to you." · B2 61, Sonntag im Haus

---

## Geprüft und keine Zusage

**Das ist der wichtigste Abschnitt der Datei.** Ohne ihn meldet `--neu` dieselben
dreizehn Fundstellen bis in alle Ewigkeit, und nach der zweiten Woche sieht
niemand mehr hin. Wer eine Fundstelle hier ablegt, schreibt dazu, warum sie keine
Zusage ist.

- [KEINE] **B1 03** Mrs Seo an Georgij · gesagt Tag 1 · faellig offen · "Your room is on the first floor, east end. Ji-won will take you up. Breakfast is from seven" · Hausordnung, keine Zusage
- [KEINE] **B1 21** Hana an Georgij · gesagt Tag 49 · faellig offen · "Not the second week, because everybody gives theirs in the second week and Ye-rin will already have said no" · Lagebeschreibung ueber Dritte
- [KEINE] **B1 25** Georgij an Annie · gesagt Tag 59 · faellig offen · "It expires on the first of March at midnight. Not the second. There is no grace period" · Beschreibung eines Instruments, keine Zusage. Die Zusage dazu steht bei B1 24
- [KEINE] **B2 08** Shin an Georgij · gesagt Tag 168 · faellig offen · "Not the twenty-sixth and not longer than the first. On the first I write" · Absicht eines Dritten in eigener Sache, nicht an Georgij gerichtet
- [KEINE] **B2 09** Annie an Georgij · gesagt Tag 168 · faellig offen · "You went into that building four times over seven weeks, and you gave up something on the third visit" · Beschreibung der Vergangenheit
- [KEINE] **B2 09** Annie an Georgij · gesagt Tag 168 · faellig offen · "Say it again on the first, after that woman in Ulsan has written her letters" · Bedingung, keine Zusage
- [KEINE] **B2 11** Georgij an Mr Hwang · gesagt Tag 180 · faellig offen · "If she uses it, I will not be able to protect you from most of what follows" · Warnung, und ausdruecklich das Gegenteil einer Zusage
- [KEINE] **B2 14** Georgij an Mr Kwon · gesagt Tag 193 · faellig offen · "Because there is nothing I could offer you that you will not do for your own reasons inside a week" · Begruendung, kein Versprechen
- [KEINE] **B2 69** Annie an Mr Kwon · gesagt Tag 341 · faellig offen · "You do not owe anybody in this house one hour of anything" · Entlastung. Sie nimmt eine Schuld weg, statt eine einzugehen

---

## Was das Werkzeug beim ersten Lauf gefunden hat, das niemand hatte

**Zwei, und beide sind offen.** Sie stehen oben in der Liste und hier steht,
warum sie zaehlen.

**Mrs Jeon, Kapitel 32 (2. Juni):** *"I have four months of money and a son who is
going to offer next month, and I am going to take it."* Vier Monate Geld ab Juni,
das Angebot des Sohnes im Juli. **Faellig etwa Tag 273 und seit siebzig Tagen
offen.** Sie ist die Figur, die Georgij ausdruecklich als sein Spiegelbild im
Kleinen gefuehrt wird (`doc/11-figuren.md`), und der Text hat sie nach dem 2. Juni
fallen lassen.

**Annie, Kapitel 59 (18. August):** *"in about a week you will have found a way to
make it about you and I would like to have said this first."* **Faellig Tag 326.**
Sie sagt eine Sache voraus, die er tun wird, und sie hat sich bisher nicht
gezeigt - was entweder heisst, dass sie unrecht hatte, oder dass es niemand
aufgegriffen hat. Bei dieser Figur ist das erste unwahrscheinlich.

---

## Zwei Beobachtungen aus der ersten Fuellung

**Erstens: Georgij macht kaum Zusagen mit Frist.** Das ist Figur und kein Mangel -
er sagt, was er tut, während er es tut. Die drei, die er gemacht hat, sind alle
gegenüber Annie, und **zwei davon hat er nicht gehalten.**

**Zweitens: Annie macht Zusagen und hält sie ausnahmslos**, und sie datiert sie
beim Sagen. Das ist dieselbe Maschine wie in `doc/12-stimmen.md`: ihr Beweismittel
ist ein Datum. **Sie ist die einzige Figur im Buch, deren Zusagen sich mit einer
Uhr prüfen lassen**, und das gehört zu ihr wie das Halsband zu ihm.

---

# Aus dem Kapitelindex, gesiebt am 27.08.

*Bis zum 27.08. fuehrte das damalige `doc/05-continuity` eine Kapitelliste von Hand: **62.030 Woerter in zwei Bloecken**, von denen der zweite - Band 2 Kapitel 46 bis 90 - ohne eigene Ueberschrift unter einem Abschnitt ueber eine Handbewegung hing. Sie ist herausgenommen; das Geruest erzeugt `build.py` nach `erzeugt/KAPITEL.md`, die Nacherzaehlung steht im Buch, und was **bindend** war, steht hier.*

*Die vollstaendige Siebung mit allen 209 Eintraegen und der Regel, nach der gesiebt wurde, liegt in `protokoll/2026-08-27-kanonliste.md`. Der ganze alte Block liegt wortgleich in `protokoll/2026-08-27-ablage-vorher/`.*

102. **b2 K12, Annies zwei Bedingungen:** kein unwahres Wort, und *"When it is finished you will come to this room and tell me whether you enjoyed it."*
103. **b2 K30, vollstaendig:** *"I will not give anything of yours to anybody without asking you first, and if the room is such that I cannot ask, I will not give it, and I will lose whatever is lost."*
104. **b2 K32:** Mrs Jeons Blatt ueber Hwang geht **an Georgij**, mit Auflage *"You will keep it and you will not use it."*
105. **b2 K20:** Nam wird in etwa vier Monaten eingestellt, **nicht von ihm**, und sie erfaehrt nie, woher es kommt.
106. **b2 K29:** *"Whatever it is, and whenever I have it, you will hear it from me and not from anybody else."*
107. **b1 K31 / b2 K6:** *"I will ask you again in March"* - **sie hat nie wieder gefragt**, und die Zusage ist am 16. Maerz eingeloest worden, auf den Tag drei Monate.

210. **Die Bedingung fuer den Abholtag:** *"whoever is in the car has about four minutes to be the first person in four years who says a true sentence to her, and it had better not be a man."*
211. **Baek will es am Tag nach ihrem Herauskommen hoeren, auch wenn es schiefgeht** - und gibt den Namen des Errichters deshalb erst dann her.
212. **Der Ventilator**, faellig Tag 347, und **Regel 2 bleibt gewahrt:** er gehoert Mr Ahn, steht in Mr Ahns Ecke, laeuft mit Mr Ahns Strom.
