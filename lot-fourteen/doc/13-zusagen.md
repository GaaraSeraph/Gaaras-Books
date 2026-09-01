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

## Kanonstand nach der Vollpruefung vom 01.09.

Die acht verbliebenen `[BELEG?]`- und `[ZITAT?]`-Markierungen sind gegen die
jeweils hoechste Kapitelfassung geprueft und aufgeloest. **Keine Markierung
bleibt im aktiven Schuldbuch.**

Der Fehler lag nicht in einem einheitlichen Kapitelversatz. Mehrere Zeilen
hatten Einloesungen aus geloeschten Fassungen geerbt. Dadurch standen unter
anderem *"I have had him"* und *"The other fifty-eight are in the back of the
book"* als Belege da, obwohl beide Saetze im heutigen Kanon nicht vorkommen.

**Ab jetzt gilt:** Eine Zusage ist nur bezahlt, wenn die Einloesung in der
hoechsten Fassung eines Kanonkapitels steht. Alte Fassungen bleiben unten als
Gedaechtnis erhalten, werden von `zusagen.py` aber nicht mehr als aktueller
Stand gelesen.

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
Fristlose Zusagen kommen von Hand hier hinein, mit `faellig bei <Ereignis>`.

Das ist Absicht und folgt Regel 8 aus `doc/22-pruefen.md`: ein Detektor, der jeden
Satz mit *I will* meldet, ist so wertlos wie einer, der nichts meldet. **Diese
Fassung meldet lieber zu wenig und verlässt sich darauf, dass die Liste gepflegt
wird.**

---

## Offen

- [OFFEN] **B2 32** Annie an Georgij · gesagt Tag 244 · faellig Tag 248 · "What he actually owns behind the lawyers in Singapore." · **Nie eingeloest, und der Text weiss es.** B2 39, sechsundzwanzig Tage spaeter, Sang-hoon: *"I have not found the Singapore end yet."* Danach faellt das Wort im ganzen Buch nicht mehr. Siehe `doc/32-plan-band-3.md`
- [OFFEN] **B2 18** Georgij an Sang-hoon · gesagt Tag 209 · faellig Tag 453 · "I am going to have him before the end of the year." · Choi stirbt erst im April. B2 89 und B2 90 sprechen ueber Tat und Folge, aber nirgends ueber die verfehlte Jahresfrist. Deshalb offen und nicht verfallen
- [OFFEN] **B2 30** Mrs Jeon an Georgij · gesagt Tag 242 · faellig Tag 273 · "I have four months of money and a son who is going to offer next month, and I am going to take it." · Angebot und Annahme kommen nach B2 30 in keiner kanonischen Fassung mehr vor
- [OFFEN] **B2 19** Annie an Georgij · gesagt Tag 209 · faellig bei der Mitteilung an alle fuenf · "Go back and tell all five that they do not owe me anything." · B2 69 bezahlt Mr Kwon. Fuer die anderen vier gibt es im heutigen Kanon weder Gespraech noch Brief
- [OFFEN] **B2 67** Georgij an Moon Hae-sook · gesagt Tag 409 · faellig bei jedem einzelnen der achtundfuenfzig · "I will use your words and not mine." · B2 83 setzt Hwang an die Suche; B2 89 verbucht vier von achtundfuenfzig. Der Posten laeuft weiter
- [OFFEN] **B2 65** Georgij an Annie · gesagt Tag 397 · faellig bei dem Tag, an dem Baek die Urkunde herausgibt · Datum und Wortlaut der zweiten Korrektur, ohne Umschreibung · **Am Bandende offen, und der Text weiss es**
- [OFFEN] **B2 85** Mrs Seo an Georgij · gesagt Tag 531 · faellig Tag 897 · "In about a year I am going to tell you what it was." · **Sie setzt die Frist, damit sie nie faellig wird**: *you are going to have forgotten this conversation and I am not.* Tag 897 ist Samstag, der 18. Maerz 2028 - 2028 ist ein Schaltjahr, deshalb 366 und nicht 365 Tage. **Die Szene steht ganz in `doc/32-plan-band-3.md`, und er kommt auf den Tag**

## Bezahlt

- [BEZAHLT] **B2 32** Annie an Georgij · gesagt Tag 244 · faellig Tag 248 · "Who else has been at that man's table." · B2 33 liefert elf Namen; B2 34 erweitert die Antwort auf einunddreissig
- [BEZAHLT] **B2 32** Annie an Georgij · gesagt Tag 244 · faellig Tag 248 · "Whether anybody has ever once seen him lose." · B2 34: einmal, vor elf Jahren, und es hat ihn nicht beendet
- [BEZAHLT] **B2 54** Annie an Georgij · gesagt Tag 319 · faellig Tag 322 · "Put it in front of me on Friday. Not today." · B2 55, am Freitag um sieben
- [BEZAHLT] **B2 54** Annie an Georgij · gesagt Tag 319 · faellig Tag 326 · "in about a week you will have found a way to make it about you and I would like to have said this first" · B2 56: Mr Ahn zwingt ihn, seine eigene Rolle in der Sache anzusehen
- [BEZAHLT] **B2 58** Annie an Georgij · gesagt Tag 371 · faellig Tag 377 · Donnerstag neun Uhr bei Mr Hwang, und er geht allein · B2 59, zwei Minuten vor neun
- [BEZAHLT] **B2 58** Annie an Georgij · gesagt Tag 371 · faellig Tag 377 · Mr Hwang wird in derselben Stunde auch nach Moon Hae-sook gefragt · B2 59, bevor Georgij geht
- [BEZAHLT] **B2 27** Mr Hwang an Georgij · gesagt Tag 238 · faellig bei dem Tag, an dem die Seite existiert · Ein Blatt soll festhalten, dass Mrs Jeon das Buch hingehalten und Hwang es nicht genommen hat · B2 59: Georgij bestaetigt ihm, dass das Blatt existiert
- [BEZAHLT] **B2 59** Georgij an Mr Hwang · gesagt Tag 377 · faellig Tag 384 · "Come back with an answer about the series and do not take longer than a week about it." · B2 60, am Donnerstag; die Antwort ist ja
- [BEZAHLT] **B2 59** Mr Hwang an Georgij · gesagt Tag 377 · faellig bei dem Tag, an dem das Formular kommt · Er unterschreibt die Abtretung, sobald Weisung, Preis und vier Seiten da sind · B2 64: am Freitag am eigenen Schreibtisch gegengezeichnet
- [BEZAHLT] **B2 61** Georgij an Mrs Jeon · gesagt Tag 385 · faellig bei dem Tag, an dem er den Tag hat · "I will telephone you with the day, and it will be the day I have it and not the day after." · B2 63, vierzig Minuten nach der Bestaetigung
- [BEZAHLT] **B2 63** Georgij an Mrs Jeon · gesagt Tag 391 · faellig Tag 394 · Die vier Seiten am Sonntagabend, in einem Raum mit Licht, zwei Stunden, niemand in der Tuer · B2 64, um sieben abgegeben und um zehn nach zehn beantwortet
- [BEZAHLT] **B2 62** Mr Ahn an Georgij · gesagt Tag 388 · faellig bei dem Tag, an dem sie geholt wird · "whoever is in the car has about four minutes... and it had better not be a man" · B2 64: Mrs Jeon spricht als Erste und Georgij bleibt im Wagen
- [BEZAHLT] **B2 56** Georgij an Mr Ahn · gesagt Tag 326 · faellig bei der Raeumung des Hauses · "Somebody is going to stand underneath her before anybody takes the floor away." · B2 64: Mrs Jeon steht unter ihr, bevor jemand den Boden nimmt
- [BEZAHLT] **B2 64** Mrs Jeon an Ahn Jung-hee · gesagt Tag 395 · faellig Tag 397 · "One, tomorrow or the day after. I will read it to you first and I will read the third paragraph twice." · B2 65, am Mittwoch um zehn; der dritte Absatz zweimal
- [BEZAHLT] **B2 54** Georgij an Annie · gesagt Tag 319 · faellig bei der ersten Stunde nach der Uebergabe · "she is told that in the first hour by somebody who is not you and not me" · B2 65: Mrs Jeon sagt es; Annie ist eine Etage hoeher und Georgij ausser Hoerweite
- [BEZAHLT] **B2 60** Georgij an Baek Jun-ho · gesagt Tag 382 · faellig bei dem Tag nach Ahn Jung-hees Herauskommen · Er erfaehrt den Namen des Errichters erst danach · B2 65: Anruf am Folgetag, persoenliche Antwort am Mittwoch
- [BEZAHLT] **B1 32** Georgij an die sechs · gesagt Tag 80 · faellig Tag 80 · "I am going to say it again now to all six, in the same words, because I promised" · B1 32 selbst; der Satz ist die Einloesung
- [BEZAHLT] **B2 30** Mrs Jeon an Georgij · gesagt Tag 242 · faellig bei dem Tag, an dem die Seite existiert · "I will write one page and I will sign it and I will put the date on it, and it goes to you." · B2 59 bestaetigt Seite, Unterschrift und Datum
- [BEZAHLT] **B2 12** Georgij an Annie · gesagt Tag 182 · faellig Tag 216 · "When it is over the other five will be yours, completely, not as customers and not as an arrangement." · B2 79 bestaetigt den Registerkauf; B2 87 datiert ihn auf November
- [BEZAHLT] **B2 05** Annie an Georgij · gesagt Tag 159 · faellig Tag 190 · "You do not yet. You will in about a month." · B2 69, 151 Tage zu spaet, von ihr selbst und mit Begruendung fuer die Wartezeit
- [BEZAHLT] **B1 31** Annie an Georgij · gesagt Tag 74 · faellig Tag 164 · "I will ask you again in March, and you will not be able to say it is not the moment, because in March it will be." · B2 06, am 16. Maerz, auf den Tag drei Monate. **Stand bis zum 25.08. ueberhaupt nicht im Schuldbuch und war neun Erzaehlmonate unbezahlt** - gefunden bei der Suche nach fristlosen Zusagen, weil `--neu` sie nicht sieht
- [BEZAHLT] **B1 24** Georgij an Annie · gesagt Tag 55 · faellig Tag 149 · "on the second of March I will hand it back to you" · B2 01, am zweiten Maerz, auf den Tag
- [BEZAHLT] **B1 09** Hana an Georgij · gesagt Tag 22 · faellig Tag 52 · "In about a month she and I are going to need each other rather badly" · B1 20, neunzehn Tage spaeter, und Georgij zaehlt sie im Text nach
- [BEZAHLT] **B1 24** Annie an Georgij · gesagt Tag 55 · faellig Tag 58 · "Monday. Named, capped, and it dies on the first of March." · B1 25
- [BEZAHLT] **B2 12** Georgij an Annie · gesagt Tag 182 · faellig Tag 203 · "I want her. Not the letter, not the lane, not an apology, and not a settlement." · B2 18 und B2 19, Nam Byung-hee am 23. April
- [BEZAHLT] **B2 09** Georgij an Annie · gesagt Tag 168 · faellig Tag 217 · "Mrs Jeon at the settlement desk, who is out in seven weeks anyway and who I am going to be able to do something about" · B2 30: Sie gibt das Buch her und behaelt die Entscheidung
- [BEZAHLT] **B2 12** Georgij an Annie · gesagt Tag 182 · faellig bei dem Ende der Ulsan-Sache · "When it is finished I will tell you whether I enjoyed it, and it will be the true answer and not the one that is easier to say in this room." · B2 19: "Yes. Once. For about a second and a half, at a gate."

---

## Geprüft und keine Zusage

**Das ist der wichtigste Abschnitt der Datei.** Ohne ihn meldet `--neu` dieselben
geprueften Fundstellen immer wieder, und nach der zweiten Woche sieht niemand
mehr hin. Wer eine Fundstelle hier ablegt, schreibt dazu, warum sie keine Zusage
ist.

- [KEINE] **B2 02** Annie an Georgij · gesagt Tag 152 · faellig bei nichts · "You will find that they are all four of them worth having, and that two of them will be gone by June." · Vorhersage ueber Dritte, keine Zusage. Ob sie eingetroffen ist, bleibt als Kontinuitaetsfrage in `doc/31-plan-band-2.md`
- [KEINE] **B2 06** Annie an Georgij · gesagt Tag 164 · faellig bei nichts · "You are mine. It has no end on it and there is no Tuesday in it. Build on this one." · Kein Posten mit Faelligkeit, sondern ein Zustand. Sie kann ihn nicht erfuellen, nur brechen
- [KEINE] **B2 54** Annie an Georgij · gesagt Tag 319 · faellig bei nichts · "I will have to buy a consignment from a house that is going to be finished by Christmas" · Dieselbe Fundstelle steht mit der tatsaechlichen Verpflichtung unter BEZAHLT; der zweite Treffer entsteht nur durch Zeichensetzung
- [KEINE] **B2 58** Georgij an Annie · gesagt Tag 371 · faellig bei einer Absage von Mr Hwang · "If he refuses after that, we do not go back." · Der Ausloeser tritt nicht ein: Hwang sagt in B2 59 zu
- [KEINE] **B2 61** Georgij an Mrs Jeon · gesagt Tag 385 · faellig bei nichts · "I will have a day when the placing party has the form" · Auskunft ueber den Stand eines fremden Verfahrens, keine Zusage
- [KEINE] **B2 66** Mrs Seo an Annie · gesagt Tag 399 · faellig bei nichts · "The woman is coming on Wednesday. She has asked for the eleventh and not the tenth" · Bericht ueber Ahns und Moons verabredete Ankunft, keine eigene Zusage. B2 67 erzaehlt die Ankunft am Mittwoch
- [KEINE] **B1 03** Mrs Seo an Georgij · gesagt Tag 1 · faellig offen · "Your room is on the first floor, east end. Ji-won will take you up. Breakfast is from seven" · Hausordnung, keine Zusage
- [KEINE] **B1 21** Hana an Georgij · gesagt Tag 49 · faellig offen · "Not the second week, because everybody gives theirs in the second week and Ye-rin will already have said no" · Lagebeschreibung ueber Dritte
- [KEINE] **B1 25** Georgij an Annie · gesagt Tag 59 · faellig offen · "It expires on the first of March at midnight. Not the second. There is no grace period" · Beschreibung eines Instruments, keine Zusage. Die Zusage dazu steht bei B1 24
- [KEINE] **B2 08** Shin an Georgij · gesagt Tag 168 · faellig offen · "Not the twenty-sixth and not longer than the first. On the first I write" · Absicht eines Dritten in eigener Sache, nicht an Georgij gerichtet
- [KEINE] **B2 09** Annie an Georgij · gesagt Tag 168 · faellig offen · "You went into that building four times over seven weeks, and you gave up something on the third visit" · Beschreibung der Vergangenheit
- [KEINE] **B2 09** Annie an Georgij · gesagt Tag 168 · faellig offen · "Say it again on the first, after that woman in Ulsan has written her letters" · Bedingung, keine Zusage
- [KEINE] **B2 11** Georgij an Mr Hwang · gesagt Tag 180 · faellig offen · "If she uses it, I will not be able to protect you from most of what follows" · Warnung, und ausdruecklich das Gegenteil einer Zusage
- [KEINE] **B2 14** Georgij an Mr Kwon · gesagt Tag 193 · faellig offen · "Because there is nothing I could offer you that you will not do for your own reasons inside a week" · Begruendung, kein Versprechen
- [KEINE] **B2 82** Chairman Woo an Annie · gesagt Tag 500 · faellig offen · "You will decide in about three weeks that you were wrong this morning, and you will not come back, because you will have made it into a principle by then" · **Vorhersage ueber eine dritte Person, keine Zusage.** Woo sagt nicht zu, etwas zu tun, sondern sagt voraus, was Annie tun wird. Sie kommt tatsaechlich nicht zurueck; der Text bestaetigt es durch Abwesenheit und einmal ausdruecklich in B2 83: *"Chairman Woo telephoned once, in April, and asked one question and rang off."* Steht hier, damit `--neu` sie nicht jedes Mal wieder meldet

---

## Was der erste Lauf fand und was davon heute gilt

**Mrs Jeon, B2 Kapitel 30 (2. Juni):** *"I have four months of money and a son
who is going to offer next month, and I am going to take it."* Das Angebot und
seine Annahme stehen in keiner spaeteren Kanonfassung. **Der Posten ist weiter
offen und laengst ueberfaellig.**

**Annies Satz aus B2 Kapitel 54:** *"in about a week you will have found a way
to make it about you and I would like to have said this first."* Der alte Stand
uebersah B2 Kapitel 56. Dort zwingt Mr Ahn Georgij genau zu dieser Verschiebung.
**Der Posten ist bezahlt.**

---

## Zwei Beobachtungen nach der Vollpruefung

**Erstens: Georgij macht wenige ausdruecklich datierte Zusagen.** Gerade deshalb
ist die verfehlte Jahresfrist gegen Choi keine Kleinigkeit. Der heutige Text
erfuellt den groesseren Inhalt, bemerkt aber die gebrochene Frist nicht.

**Zweitens: Annie datiert Auftraege und Vorhersagen auffaellig oft.** Das bleibt
Teil ihrer Stimme. Es ist aber kein Beweis, dass jeder von ihr gesetzte Termin
im Text bezahlt wird: Singapur bleibt offen, und die Juni-Vorhersage aus B2 02
ist bis zum Bandende weder bestaetigt noch widerlegt.

---

# Aus dem Kapitelindex

*Bis zum 27.08. fuehrte das damalige `doc/05-continuity` eine Kapitelliste von Hand: **62.030 Woerter in zwei Bloecken**, von denen der zweite - Band 2 Kapitel 46 bis 90 - ohne eigene Ueberschrift unter einem Abschnitt ueber eine Handbewegung hing. Sie ist herausgenommen; das Geruest erzeugt `build.py` nach `erzeugt/KAPITEL.md`, die Nacherzaehlung steht im Buch, und was **bindend** war, steht hier.*

*Die vollstaendige Siebung mit allen 209 Eintraegen und der Regel, nach der gesiebt wurde, liegt in `protokoll/2026-08-27-kanonliste.md`. Der ganze alte Block liegt wortgleich in `protokoll/2026-08-27-ablage-vorher/`.*

102. **b2 K12, Annies zwei Bedingungen:** kein unwahres Wort, und *"When it is finished you will come to this room and tell me whether you enjoyed it."*
103. **alt K30, vollstaendig:** *"I will not give anything of yours to anybody without asking you first, and if the room is such that I cannot ask, I will not give it, and I will lose whatever is lost."*
104. **b2 K30:** Mrs Jeons Blatt ueber Hwang geht **an Georgij**, mit Auflage *"You will keep it and you will not use it."*
105. **b2 K19:** Nam wird in etwa vier Monaten eingestellt, **nicht von ihm**, und sie erfaehrt nie, woher es kommt.
106. **b2 K26 (geteilt):** *"Whatever it is, and whenever I have it, you will hear it from me and not from anybody else."*
107. **b1 K31 / b2 K6:** *"I will ask you again in March"* - **sie hat nie wieder gefragt**, und die Zusage ist am 16. Maerz eingeloest worden, auf den Tag drei Monate.

210. **Die Bedingung fuer den Abholtag:** *"whoever is in the car has about four minutes to be the first person in four years who says a true sentence to her, and it had better not be a man."*
211. **Baek will es am Tag nach ihrem Herauskommen hoeren, auch wenn es schiefgeht** - und gibt den Namen des Errichters deshalb erst dann her.
212. **Der Ventilator**, faellig Tag 347, und **Regel 2 bleibt gewahrt:** er gehoert Mr Ahn, steht in Mr Ahns Ecke, laeuft mit Mr Ahns Strom.

---

## Aus einer Fassung, die es nicht mehr gibt

**Gefunden und ausgelagert am 28.08.** Diese **27** Posten stehen auf
Erzaehltagen zwischen **318 und 367**, und das Buch erzaehlt diese Strecke
heute nicht mehr: **zwischen Tag 329 und Tag 361 liegt gar nichts**, und
`b2 ch57` (Tag 328) stoesst direkt an `b2 ch58` (Tag 362).

**Es ist eine Ursache und nicht siebenundzwanzig Fehler.** Beim Umbau von
Band 2 ist rund ein Monat herausgefallen - September bis November 2026 -,
und mit ihm die Szenen, in denen diese Zusagen gegeben und bezahlt wurden.
Daher stammen auch die meisten Zitate, die sich im Kanon nicht mehr
wiederfinden lassen, und die Belege, die auf Kapitel bis `B2 90` zeigen.

**Warum sie nicht geloescht werden.** Das Schuldbuch ist ein Gedaechtnis. Eine
Zusage, die einmal gegeben wurde, gehoert hinein, auch wenn die Szene sie
nicht mehr traegt. Sie stehen nur nicht mehr zwischen den Posten, die das
Buch heute halten muss.

**Was mit ihnen zu tun ist, und das ist Lesearbeit.** Jede einzelne ist
entweder (a) in einer heute erzaehlten Szene wieder aufgetaucht und muss
dorthin adressiert werden, (b) ersatzlos weg, oder (c) **eine Zusage, die im
Buch noch offen ist, ohne dass irgendwo steht, dass sie gegeben wurde** -
und die dritte Sorte ist die teure.

- [BEZAHLT] **B2 57 (alt)** Woo an Georgij · gesagt Tag 318 · faellig Tag 322 · "I will come to you." · B2 61, Sonntag im Haus
- [BEZAHLT] **B2 77 (alt)** Woo an Georgij · gesagt Tag 324 · faellig offen · "You have until she asks." · B2 74: **die Frist ist am Tag 350 abgelaufen.** Sechsundzwanzig Tage. Sie fragt am Ende des Kapitels, und zwar weil sie einen Mann bepreisen muss und nicht weil sie etwas gemerkt hat
- [BEZAHLT] **B2 71 (alt)** Georgij an Mrs Sunwoo · gesagt Tag 333 · faellig bei dem Ende des Feldzugs gegen Choi · "you will tell me the whole of it and not the comfortable part" · B2 89, am 19. November, fuenfzig Minuten. **Sie hat fuenfzig Minuten auf die Stelle gewartet, an der jemand klug war, und es gibt keine**
- [BEZAHLT] **B2 67 (alt)** Georgij an Sim · gesagt Tag 339 · faellig Tag 346 · "There is a difference. You will not be able to hear it and she will." · B2 72: sie sagt am 14. seinen Namen, zum ersten Mal in vier Jahren. **Sim und Mr Ahn lesen es als Abschied, und keiner von beiden war am siebten in dem Zimmer** (Notiz im Wagen, B2 74 v1.1)
- [BEZAHLT] **B2 67 (alt)** Sim an Georgij · gesagt Tag 339 · faellig Tag 346 · "I am going to make it because on the fourteenth of September a woman in a house in Gangwon-do will be waiting for a telephone to ring." · B2 72, am Tag, zehn nach fuenf, sechsundzwanzig Minuten
- [BEZAHLT] **B2 67 (alt)** Sim an sich selbst · gesagt Tag 339 · faellig bei dem Tag, an dem die Frau in Gangwon-do ihn nicht mehr braucht · "After the fourteenth I am finished." · B2 89: die Leitung ist seit dem 30. September tot, sie ist seit dem 2. November heraus, und er hat keinen Auftrag mehr angenommen
- [BEZAHLT] **B2 69 (alt)** Annie an Georgij · gesagt Tag 341 · faellig Tag 342 · "You are going tomorrow, and you are not going with anything." · B2 70, am naechsten Morgen
- [KEINE] **B2 69 (alt)** Annie an Mr Kwon · gesagt Tag 341 · faellig offen · "You do not owe anybody in this house one hour of anything" · Entlastung. Sie nimmt eine Schuld weg, statt eine einzugehen
- [BEZAHLT] **B2 70 (alt)** Mr Ahn an Georgij · gesagt Tag 342 · faellig Tag 347 · "It will be ready Tuesday." · B2 73, am Dienstag, mit Kabel aufgerollt und Tuch runter
- [BEZAHLT] **B2 61 (alt)** Georgij an Mrs Jeon · gesagt Tag 343 · faellig bei dem Tag, an dem er den Namen hat · "You will tell me her name before I am in the room with her. Not the reference. The name, and how it is written, and which part of it her mother used." · B2 83, alle drei Teile. **Den dritten hat Mr Ahn am Dienstagabend gegeben und vierzig Sekunden dafuer gebraucht**
- [BEZAHLT] **B2 71 (alt)** Georgij an Mrs Jeon · gesagt Tag 343 · faellig Tag 385 · "I will come in October." - "Say the date." - "The twenty-third." · B2 83, am Tag, mit dem ersten Zug, nach drei Stunden neunzehn Minuten, und wieder ohne etwas
- [BEZAHLT] **B2 71 (alt)** Mrs Jeon an Georgij · gesagt Tag 343 · faellig Tag 346 · "I will telephone Gwangyang on Monday." · B2 72, am Montag um zwanzig nach zehn und nicht am Abend
- [BEZAHLT] **B2 71 (alt)** Mrs Jeon an Georgij · gesagt Tag 343 · faellig Tag 363 · "The start date will be the first of October." · B2 78, am Donnerstag. **Niemand in dem Haus weiss etwas ueber den Tag ausser dem Datum**, und Georgij telefoniert absichtlich nicht
- [BEZAHLT] **B2 71 (alt)** Mrs Jeon an Georgij · gesagt Tag 343 · faellig bei der ersten Stunde nach der Uebergabe · Sie nimmt sie an · B2 87, und sie liest nichts zusammen und sagt an keiner Stelle, was es bedeutet
- [BEZAHLT] **B2 72 (alt)** Annie an Georgij · gesagt Tag 346 · faellig Tag 350 · "It will be decided on Friday and it will be decided in this room." · B2 74, am Freitag um neun, in vier Teilen und mit einer Zahl
- [BEZAHLT] **B2 72 (alt)** Sim an Georgij · gesagt Tag 346 · faellig Tag 360 · "I am telephoning that house again on the twenty-eighth." · B2 77, am Tag, zehn nach fuenf, und er kuendigt im selben Gespraech den naechsten fuer Donnerstag an
- [BEZAHLT] **B2 73 (alt)** Georgij an Mr Ahn · gesagt Tag 347 · faellig offen · Er soll Sim fragen, wie lange es sonst dauert, sie ans Telefon zu holen · B2 74, am naechsten Morgen in Jongno: Schnitt sechs Minuten, kuerzeste vier zehn, laengste elf am 27. August, und am 14. September einundvierzig Sekunden
- [OFFEN] **B2 73 (alt)** Mr Ahn an sich selbst · gesagt Tag 347 · faellig bei Ahn Jung-hees Rueckkehr · "It goes in that corner and it stays there... until she comes in here and switches it off herself." · -
- [BEZAHLT] **B2 74 (alt)** Georgij an Sim · gesagt Tag 348 · faellig bei dem Ende des Feldzugs gegen Choi · "You will be told, and you will not be told the comfortable part of it." · B2 89, am Freitag in Jongno, eine Stunde zehn, und der Tee stand bereit
- [BEZAHLT] **B2 74 (alt)** Annie an Georgij · gesagt Tag 350 · faellig Tag 353 · das Geld soll bis zum Zweiundzwanzigsten auf einem eigenen Konto liegen · B2 76, am Montag, in vierzig Sekunden auf dem Weg zum Wagen: ein Konto bei einer Bank, die sie sonst nicht benutzt, ihr Name darauf, sonst nichts darin. **Woher es kommt, sagt sie nicht, und er fragt nicht**
- [KEINE] **B2 74 (alt)** Georgij an Annie · gesagt Tag 350 · faellig offen · "you have told her you will be at her table on the twenty-third" · Keine neue Zusage, sondern die Wiedergabe von B2 71. `--neu` findet sie, weil der Wortlaut abweicht
- [KEINE] **B2 75 (alt)** Annie an die vier Spediteure · gesagt Tag 350 · faellig offen · "if anybody ever tells them otherwise they are to be shown the letter" · **Keine Zusage mit Faelligkeit, sondern eine Buergschaft ohne Ablauf.** Eingeloest in dem Moment, in dem der Brief existiert, und nie faellig
- [BEZAHLT] **B2 77 (alt)** Annie an Georgij · gesagt Tag 360 · faellig Tag 364 · "I will tell you on Friday who he is." · B2 78, am Freitag um neun, im Stehen: **Chairman Woo**, und es sind vier Fragen, die sie ihm nicht stellen wird
- [BEZAHLT] **B2 77 (alt)** Sim an Georgij · gesagt Tag 360 · faellig Tag 363 · "I will telephone that number on Thursday to find out whether it still exists." · B2 78, dreimal an einem Abend: einundvierzig Klingelzeichen, dann nichts, dann der Ton. **Die Nummer ist weg**
- [BEZAHLT] **B2 82 (alt)** Annie an Georgij · gesagt Tag 364 · faellig Tag 367 · "Monday, at ten... And you are going to be in the room." · **im selben Kapitel**, seit der Zusammenlegung: vier Minuten vor zehn, und sie nimmt nichts mit
- [BEZAHLT] **B2 82 (alt)** Annie an Georgij · gesagt Tag 367 · faellig Tag 369 · "He is going to write them tonight." · B2 80: am Mittwoch kommt nichts und am Donnerstag auch nicht, und Georgij rechnet aus, dass genau das die Bestaetigung ist
- [OFFEN] **B2 82 (alt)** Chairman Woo an Annie · gesagt Tag 367 · faellig bei seinem Tod · vier Antworten in seiner Handschrift, beim Anwalt, versiegelt, "and not one hour before" · **Die einzige Zusage im Buch mit einem Termin, den niemand nachschlagen kann.** B2 90 bestaetigt nur, dass der Umschlag existiert
