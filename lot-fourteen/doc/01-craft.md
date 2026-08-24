# Handwerk

Alle Regeln und Pruefungen. Die stehende Liste laeuft in jedem Durchgang, der Rest wird nachgeschlagen.

---

## Was jeder Durchgang prueft

**Diese Liste laeuft immer.** Nicht nur beim ersten Entwurf, nicht nur bei einem
neuen Kapitel, sondern nach jeder Aenderung an jedem Text. Beim Reparieren
entstehen neue Fehler, weil sich beim Erklaeren die immer gleichen Konstruktionen
anbieten.

**Zweimal lesen, bis zweimal nichts gefunden wird.** Der zweite Durchgang findet
regelmaessig noch etwas.

---

### 0. Die Wortzahl ist keine Schere

**Erst fertig schreiben, dann teilen. Nie kuerzen, um unter 4300 zu kommen.**

Die Spanne in `doc/05-continuity.md` sagt, wann ein Kapitel **zwei** Kapitel ist.
Sie sagt nicht, dass Text weg soll. Wer sie als Obergrenze fuer die Schere liest,
streicht am Ende genau das, was ein Kapitel gewichtig macht, und behaelt das
Mittelmass, weil Mittelmass sich leichter streichen laesst.

**Am 22. August passiert und rueckgaengig gemacht.** Kapitel 23 stand bei 4914
Woertern. Statt zu teilen wurde an vier Stellen gekuerzt, und alle vier waren
Substanz: das Halsband an der vierten Wand mitten in der Stadt, der Haken in
Sang-hoons Kompliment, die zweite Fernbedienung in einer Schublade in Yeouido,
und die Haelfte von Annies Erklaerung. Danach war das Kapitel kuerzer und
schlechter, und geteilt werden musste es trotzdem.

**Die Reihenfolge, die gilt:**

1. Schreiben, bis die Szene fertig ist. Die Zahl waehrenddessen nicht ansehen.
2. Erst dann `check.py` und die Spanne.
3. Ueber 4300: an einer Naht teilen, an der beide Haelften ein eigenes Gewicht
   haben. Kapitel 23 wurde an Annies Antwort getrennt, 2555 und 2510.
4. Gestrichen wird nur, was nach den Punkten 1 bis 6 dieser Liste ohnehin weg
   muesste. Die Wortzahl ist dafuer nie der Grund.

### 1. Bandwurmsaetze

Kein Satz ueber vierzig Woerter. `python3 check.py` findet sie alle.

Nicht kuerzen, indem etwas gestrichen wird, sondern teilen. Ein Satz mit drei
"und" ist meistens drei Saetze.

### 2. Ergibt der Satz Sinn

**Der wichtigste Punkt und der einzige, den kein Programm findet.** Jeden Satz
einzeln fragen: Was tut er?

Woran es typischerweise scheitert:

- **Eine Unterscheidung, die sich selbst aufhebt.** *"Er hat den Namen nicht
  gesagt, aber ich werde nicht so tun, als waere es nicht der Name."* Dann war
  die Unterscheidung fuer nichts da ausser dafuer, dass der Sprecher praezise
  aussieht.
- **Ein Pronomen, das auf nichts zeigt.** "Both of them", "every one of them",
  "it", wenn vorher kein Substantiv steht, an dem es sich festhalten kann.
- **Ein Wortwechsel, in dem sich nichts bewegt.** Behauptung, Einwand,
  Absicherung, Quittung. Faellt eine Replik weg und die Szene verliert nichts,
  war sie Fuellung.
- **Ein Bild ohne Herkunft.** Ein Gegenstand, den die Figur laut Kanon nicht
  besitzen kann. Eine Handtasche, die in dieser Szene nicht eingefuehrt ist. Ein
  Fahrer, der laut Rota diese Woche nicht faehrt.
- **Ein Satz, der nur Haltung ist.** "Ich moechte vorsichtig sein mit dem Wort."
  Dann sei vorsichtig, statt es anzukuendigen.
- **Ein Verdienst aus einer Unterlassung, die nichts kostet.** Siehe unten, eigener
  Abschnitt. Das ist die haeufigste Art, wie sich Lob in die Erzaehlstimme schleicht.

**Probe:** Den Satz laut lesen und fragen, was der Leser danach weiss, was er
vorher nicht wusste. Wenn die Antwort nichts ist, streichen.

### 2b. Wer haette es getan

**"Er tat X nicht" ist nur dann eine Aussage, wenn im Text jemand X erwartet
hat.** Sonst ist es kein Satz ueber die Figur, sondern ein Kompliment, das der
Erzaehler ihr macht, und es kostet die Figur nichts.

Der Fund, aus Kapitel 21, Fassung 1.0:

> Mr Ku drove him, because Mr Pyo was with Annie and because Georgij did not
> have a car and was not going to start pretending he did.

Niemand hat je vermutet, er wuerde so tun, als haette er einen Wagen. Es gibt
keine Szene, in der er es tut, und keine Figur, die es ihm zutraut. Der Satz
erfindet also eine Versuchung, damit die Figur ihr widerstehen kann.

**Die Probe, ein Satz:** Wer im Text haette X getan? Steht dafuer keine Person
und keine Stelle, wird gestrichen. Nicht umformuliert, gestrichen.

**Woran man es im Satzbau erkennt.** Es haengt fast immer als zweites *because*
oder zweites *and* hinten an einem Satz, der schon fertig war. Die erste
Begruendung traegt, die zweite ist Zierat. Ein Satz mit zwei *because* ist
verdaechtig, und die Wendungen *was not going to*, *did not bother to*, *never
once considered*, *was not about to* sind es fast immer.

**Die Ausnahme, und sie ist eng.** Wenn eine Figur X tatsaechlich erwogen oder
frueher getan hat, ist das Unterlassen eine Handlung und gehoert hin. Kapitel 20:
*"I gave him the account number ... After he signed, and not before, so that it
did not pay for anything."* Da liegt beides im Text - er haette es vorher geben
koennen, und der Unterschied kostet ihn etwas.

**Und die Regel dahinter, die weiter reicht:** Was eine Figur ausmacht, sagt am
besten eine andere Figur, und zwar als Beobachtung. Dieselbe Sache steht dreissig
Absaetze spaeter aus Hanas Mund und tut dort Arbeit: *"You came up my drive in a
car you did not choose, driven by a man you did not hire, wearing a coat somebody
else paid for."* Der Erzaehler hatte sie vorweggenommen und dabei verdorben.

**Zweite Schicht, im selben Kapitel und im selben Durchgang gefunden.** Auch wenn
die Versuchung echt ist, wird sie nicht angekuendigt. Ebenfalls Kapitel 21,
Fassung 1.0, auf Hanas Frage, was sie bekommt:

> "Nothing that is not already yours. The lease was signed on Monday and I am
> not going to stand in your house and offer you a thing you have already been
> paid."

Hana honoriert im naechsten Satz, dass er nichts angeboten hat. Die Erwartung
steht also da, und trotzdem ist der Satz falsch, weil er die Unterlassung
**ausspricht** statt sie zu vollziehen. Steht auf *"Nothing. The lease was signed
on Monday."*, und ihre Antwort traegt genauso.

**Und das Warnzeichen, das beide Faelle verbindet:** die Formel war aus dem
eigenen Buch abgeschrieben. In Kapitel 15 steht *"I am not going to stand in your
dining room and tell you..."*, dort zu Recht, weil Annie eine Zeile vorher
widersprochen hat. In Kapitel 21 wurde daraus *"stand in your house"*. **Wenn
sich eine Wendung beim Schreiben von selbst anbietet, kommt sie meistens aus dem
Nachbarkapitel und nicht aus der Szene.**

**Gegenprobe, die dazugehoert.** Nicht nach der Stelle suchen, die man kennt,
sondern nach der Wendung. Der erste Durchgang suchte `was not going to start`
und fand einen Treffer. Die Suche nach `not going to` fand sechsundzwanzig, davon
zweiundzwanzig zu Recht - jedes Mal, wenn vorher wirklich jemand gefragt hatte.
**Der eigene Erwartungsfilter schneidet den Befund weg.**

### 2c. Die zwei Kontraktionen

**Ab Kapitel 17 spricht Georgij ohne Kontraktionen.** Davor war es ein Gefaelle,
und die Kurve ist die genaueste im ganzen Buch: **seine Sprache wird formeller, je
weniger Boden er unter sich hat.** Das ist nicht geplant worden, es ist beim
Schreiben passiert.

**Hier stand bis zum 23.08. "im ganzen Buch keine einzige Kontraktion" und "17, 18,
19, 20, 21 und 22 haben null". Beides war falsch, und der Fehler war die
Formulierung.** Die Regel gilt fuer **Georgij**, nicht fuer den Text: Woo sagt in
Kapitel 19 *"Don't."* und Hana in Kapitel 21 zweimal dasselbe, und keines davon ist
ein Fehler. Andere Figuren sprechen, wie sie sprechen; nur an ihm haengt die Kurve.

**Und eine war doch seine.** In Kapitel 21 meldete er sich am Telefon mit *"It's
Georgij."* Das ist kein Kontrollverlust, das ist eine Begruessung, und genau deshalb
war es die gefaehrlichste: Sie stand zwei Kapitel vor den zweien in 23 und haette
ihnen die Ausschliesslichkeit genommen, an der ihre ganze Wirkung haengt. Geaendert
auf *"This is Georgij."* (Fassung 1.7), was ausserdem seinem Register entspricht.

**Damit gilt, nachgezaehlt am 23.08. ueber alle vierunddreissig Kapitel:** Georgij
hat nach Kapitel 16 genau **drei** Kontraktionen, und alle drei stehen an einer
Stelle, an der er die Fassung verliert. Zwei in Kapitel 23, eine in Kapitel 34.

Daraus folgt ein Mittel, das genau einmal funktioniert.

**In Kapitel 23 stehen zwei Kontraktionen, und sie sind die einzigen seit
Kapitel 16:**

> *"Haven't you been holding me just fine?"*
>
> *"I don't feel like calling you Mistress right now."*

Beide fallen an der Stelle, an der er die Fassung verliert, und der Text sagt
es nicht, weil die Grammatik es sagt. Der Leser hoert es, ohne es benennen zu
koennen.

**Die Regel:** Kontraktionen sind ab Kapitel 17 keine Stilfrage mehr, sondern
ein Ereignis. Wer eine einbaut, baut einen Kontrollverlust ein. Wer die zwei in
Kapitel 23 glaettet - und das ist beim ersten Schreiben passiert, aus
*haven't* wurde *have you not*, aus *right now* wurde *at the moment* - nimmt
der Szene ihren Beweis und laesst einen Mann hoeflich bleiben, waehrend die
Regie sagt, dass er es nicht ist.

**Dasselbe gilt fuers Vokabular.** *Intelligent as hell* ist unbeholfener als
*clever as hell* und deshalb richtig. Ein Mann, der schmeichelt, waehlt das
zweite. Ein Mann, der es ernst meint und nicht mehr waehlt, sagt das erste.

**Nachtrag vom 24.08., Band 2.** Georgij hat in den zweiundvierzig Kapiteln von
Band 2 **keine einzige eigene Kontraktion**. Es gibt genau einen Treffer, und er
ist ein Zitat: *"Tell her we haven't met."* (Band 2, Kapitel 10, am Gartentor).
Das ist Mrs Sunwoos Satz aus dem Ballsaal, woertlich zurueckgegeben - die ganze
Szene haengt daran, dass er ihn unveraendert hergibt, und sie sagt es zwei
Repliken spaeter selbst: *"I have been saying it for a very long time and nobody
has ever handed it back."* **Er zaehlt nicht als vierte.** Wer die drei aus Band 1
nachzaehlt, findet ihn, und muss ihn nicht ein zweites Mal pruefen.

### 2d. Die Stiftshuette

**Ein Vorgang wird einmal ausgefuehrt und danach nur noch beruehrt.**

Exodus beschreibt die Stiftshuette zweimal in voller Laenge, einmal als
Anweisung und einmal als Ausfuehrung, und das ist genau die Falle. In diesem
Buch verhandelt Georgij dieselbe Sache regelmaessig mit drei Leuten
nacheinander, weil das seine Arbeit ist. **Der Leser braucht sie einmal.**

Kapitel 27, Fassung 1.5: Der Woo/Hana-Mietvertrag wurde dreimal vollstaendig
vorgetragen - an Annie, an Woo, an Hana. Dieselben vier Zahlen, dasselbe Tor,
dasselbe *since 2019*, dreimal. Beim Zaehlen: *open ground* viermal, *Yeonan*
dreimal, *sixteen thousand* dreimal.

**Die Regel fuer den zweiten und dritten Vortrag:**

1. Der Erzaehler sagt, **dass** es vorgetragen wurde, und wie lange es gedauert
   hat. *"He laid it out in the same order he had used at that desk on Tuesday
   and in the shed on Thursday, and it took under two minutes."*
2. Im Dialog steht nur, **was fuer diesen Zuhoerer neu ist.** Woo hoert den
   Fehlbetrag, Hana hoert die Konditionen. Was beide schon wissen, faellt weg.
3. **Der Zuhoerer darf vorgreifen.** Wer klug ist, kommt vor dem Sprecher ans
   Ende - *"She got to the end of it before he did."* Das erledigt die
   Wiederholung und charakterisiert im selben Zug.

**Probe:** Ein Substantiv, das in einem Kapitel dreimal in derselben Funktion
steht, ist fast immer die zweite Stiftshuette. Suchen laesst sich das mechanisch,
und es lohnt sich bei jedem Kapitel, in dem dieselbe Sache zwei Raeume weit
getragen wird.

### 2e. Wer spricht gerade

**Zwischen zwei Bloecken derselben Figur steht immer etwas Koerperliches.** Die
Regel steht unten bei den Dialogregeln; hier steht, wie man ihre Verletzung
findet, denn drei von vier Faellen sind mechanisch entscheidbar und `check.py`
meldet sie seit dem 22. August.

**Fall 1, fortgesetzte Rede.** Ein Absatz mit **ungerader** Zahl
Anfuehrungszeichen laesst das Zitat offen; der naechste Absatz gehoert derselben
Figur. Das ist formal erlaubt, und ohne Beat dazwischen liest es sich trotzdem
wie ein Sprecherwechsel - der Leser kommt vier Zeilen weiter, merkt, dass es
nicht aufgeht, und zaehlt zurueck.

**Fall 2, lange Ketten nackter Repliken.** Absaetze, die nur aus Rede bestehen,
ohne Sprechertag und ohne Beat. Der Leser liest sie abwechselnd, und das traegt
vier oder fuenf weit. Ab sieben meldet die Pruefung. Steht in so einer Kette
**doch** zweimal dieselbe Figur, ist alles Folgende falsch zugeordnet.

**Fall 3, der doppelte Beat.** Derselbe Satz steht zweimal im Kapitel, meist
wenige Zeilen auseinander, und beide Male tut er dasselbe. `check.py` meldet
jeden Satz ab sechs Woertern, der zweimal vorkommt.

Am 23. August fand der erste Lauf dieser Pruefung vier Stellen auf einmal:
*"He let that sit for exactly as long as it needed"* in 26, *"He looked at the
fire and not at her"* in 27, *"He looked at the floor for a second and then back
up"* in 28, und in 30 zweimal *"She said it without any drama at all"* in
**einem einzigen Absatz**. Dazu in 29 eine ganze Replik doppelt, die ein Leser
gefunden hat, bevor die Pruefung existierte.

**Nicht jede Wiederholung ist ein Fehler.** In Kapitel 16 sagt Georgij viermal
*"I am not going to answer that"* und zweimal *"I would like it back on
Thursday"*, und das ist die Figur: Er wiederholt sich flach, weil er sich nicht
verhandeln laesst. Darum Hinweis und nicht Fehler. Die Frage beim Lesen lautet:
**Tut der Satz beim zweiten Mal etwas anderes?** Bei einer Figur, die sich
weigert, ja. Bei einem Beat nie.

**Fall 4 ist nicht findbar.** Zwei getrennte Bloecke derselben Figur, beide
sauber geschlossen, ohne Tag und ohne Beat, liest ein Programm als
Sprecherwechsel und kann es nicht anders. Dafuer gibt es nur das Lesen.

**Der Befund vom 22. August, ueber alle siebenundzwanzig Kapitel:** dreizehn
Stellen, davon **sieben allein in Kapitel 27** und alle aus einer einzigen
Woche. Kapitel 17 hat drei, Kapitel 21 und 24 je eine, Kapitel 2 eine Kette.

**Und der Grund, warum es sich haeuft:** Es passiert beim *Teilen* von
Bandwurmsaetzen. Ein Redeblock wird an einem Punkt aufgetrennt, die zweite
Haelfte bekommt ein oeffnendes Anfuehrungszeichen, und der Beat, der vorher in
der Mitte stand, bleibt in der ersten Haelfte zurueck. **Nach jedem Satz-Split
in direkter Rede gehoert die Pruefung noch einmal gelaufen.**

### 2h. Werkzeuge stumpfen ab, und er legt sie selbst ab

**Ein Mittel, das zweimal benutzt wird, wirkt beim zweiten Mal weniger, und
Georgij weiss das vor dem Leser.**

**Deshalb gibt es in diesem Buch keine Szene, in der ein eingefuehrtes Werkzeug
Georgijs in seiner Hand versagt.** Wenn es stumpf ist, hat er es vorher abgelegt,
und die Szene handelt vom Ersatz. Wer ihn mit einem stumpfen Werkzeug
hineinlaufen und daran scheitern laesst, schreibt einen anderen Mann.

**Der Beleg steht im Text und ist unmissverstaendlich.** Sang-hoon sagt es ihm in
Kapitel 16 ins Gesicht - *"You could have stopped using it."* In Kapitel 33
benutzt er die Guidance ein letztes Mal, **sagt vorher dazu, dass es das letzte
Mal ist**, und stellt die Frage trotzdem. Ein Mann, der sein Hauptwerkzeug vor
Publikum selbst zu Grabe traegt, benutzt neun Wochen spaeter nicht den Rest
desselben Repertoires und wundert sich.

**Was daraus fuer Band 2 folgt, und es ist der Motor des Bandes:**

| Tot, und von ihm selbst | Warum |
|---|---|
| *"Please guide me"* | Kapitel 33, oeffentlich beendet |
| *"Who should I be careful of?"* | Die Frage des Neulings. Niemand sagt einem gefaehrlichen Mann, wen er fuerchtet |
| Der eifrige junge Mann | Seit Dezember stehen zwei Zeitungen dagegen |
| Vagheit ueber sich selbst als Schutz | In Kapitel 16 hat er die Zahl selbst hergegeben, in 33 kam die Rechnung |

**Und der Ersatz ist keine neue Masche, sondern ein anderer Handel.** In Band 1
hat er genommen, ohne zu geben: Charme, Fragen, Guidance, alles Instrumente zur
Entnahme. Wenn niemand mehr freiwillig gibt, muss er **bezahlen**, und er besitzt
nur eines - was er weiss.

**Damit dreht sich die Gefahr um.** In Band 1 war sie, gekauft zu werden. In
Band 2 ist sie, **gelesen zu werden**: jede Zahlung ist eine Handschrift, sie
haeufen sich, und Choi liest Handschriften. Wer ihn in Band 2 etwas herausholen
laesst, ohne dass er dafuer etwas hingelegt hat, hat die Szene nicht zu Ende
gedacht.

**Die Probe, ein Satz:** Was hat ihn dieser Raum gekostet? Steht darauf keine
Antwort, war es eine Band-1-Szene.

### 2f. Gekauft, nicht angestellt

**Es heisst *paid for*, nie *paying for*.** Annie hat Georgij einmal gekauft, im
Oktober, fuer 220 Millionen Won. Sie zahlt ihm keinen Lohn, und das ist keine
Nebensaechlichkeit, sondern die Achse des Buches: In Kapitel 24 sagt er es ihr
auf einer Bruecke ins Gesicht, *"I am not paid. There is no arrangement anywhere
in the world under which I receive one won of yours"*, und es ist der einzige
Beweis, den er dafuer hat, dass er nicht wegen des Geldes bleibt.

Eine Verlaufsform behauptet ein laufendes Verhaeltnis und macht aus einem
gekauften Mann einen Angestellten. Damit faellt der Beweis weg.

**Gezaehlt am 22. August:** ueber vierzig Stellen im Buch benutzen *paid for*.
Drei benutzen die Verlaufsform, und zwei davon zu Recht - Woo ueber einen
Vorgang (*"you were not paying for the signature"*) und Hana ueber laufende
Instandhaltung (*"a woman who was paying for exactly the parts that people see
from the road"*). Die dritte stand in Kapitel 27 und war falsch.

**Dieselbe Wachsamkeit gilt fuer alles, was nach Anstellung klingt:** Gehalt,
Kuendigung, Urlaub, Vertrag im arbeitsrechtlichen Sinn. Was zwischen den beiden
gilt, ist eine Schuldübernahme und ein Halsband, und die Sprache darf das nicht
weichzeichnen.

### 2g. Was ein Beat ist, und was keiner ist

**Ein Beat ist eine kleine koerperliche Handlung zwischen zwei Redebloecken.**
Er ist kein Schmuck. Er ist die Sprecherkennzeichnung, und er ersetzt das
*sagte er*, das dieses Buch fast nie benutzt.

> "I have not asked her."
>
> **Georgij put his coat over the back of the chair, which he had not intended
> to do.**
>
> "You said a Tuesday."

Ohne die mittlere Zeile liest man beide Repliken als Wechsel. Mit ihr ist klar,
wer spricht, und man erfaehrt nebenbei etwas ueber den, der spricht.

**Erlaubt:** Handlungen, Blicke, Haende, Gegenstaende, ein Gesicht, das sich
nicht bewegt, ein Raum, der weitergeht. *"She turned her glass a quarter turn
and left it there."* *"Annie did not move."* *"The fire did something and
settled."*

**Nicht erlaubt:** Kommentare ueber die Art des Sprechens. *"He kept his voice
level"*, *"she let it be the size it was"*, *"without any pressure anywhere"*.
Das etikettiert den Ton, statt etwas zu tun, und `check.py` meldet die
bekannten Formeln.

**Das Musterbeispiel** steht in Kapitel 17, Annies Rede an der Flurkreuzung:
vier Bloecke, vier Beats, kein einziger Sprechertag noetig. Nichts bewegt sich
im Gesicht, dann der Blick vom Stuhl weg, dann zwei Finger auf der Lehne, dann
*Her hand stayed where it was*.

**Wo Beats fehlen, siehe Punkt 2e** - es passiert fast immer beim Teilen von
Bandwurmsaetzen in direkter Rede.

### 2i. Der Bogen darf keine Ratsche sein

**Am 23.08. vom Autor gemeldet, nachdem elf Kapitel von Band 2 standen:**
*"Wieso bin ich in diesem Band so schwach, schlecht, inkompetent? Mir haben
vorher alle aus der Hand gefressen. Jetzt bin ich nur noch passiv und reagiere
und loesche Braende, die teilweise von mir verursacht wurden. Eine Handlung
laesst mich aermer zurueck als die naechste."*

**Nachgezaehlt und bestaetigt.** Von Band 2, Kapitel 1 bis 11 endete **kein
einziges** damit, dass Georgij etwas gewonnen hatte. Jedes lief nach demselben
Muster: bezahlen, die Haelfte bekommen, dafuer geprueft werden, und der Rest ist
schlechter als vorher. Das ist kein Bogen. Das ist eine Ratsche in eine Richtung,
und sie ist nach drei Kapiteln vorhersehbar und nach sechs unlesbar.

**Die drei Fehler, die dahin fuehren, und alle drei sind leicht zu machen:**

1. **Regel 2h falsch angewendet.** Dort steht, dass das **Repertoire** stumpf
   wird. Nicht der Mann. Wer daraus "seine Methoden wirken nicht mehr" macht,
   hat "er kann nichts mehr" geschrieben. Er hat in Band 1 Park Sang-hoon
   geschlagen.
2. **Die Initiative liegt beim Gegner.** Ab Kapitel 7 fing kein Kapitel mehr mit
   einer Entscheidung von ihm an. Nam feuert, Hwang ermittelt, Choi handelt
   unsichtbar, und er antwortet. **Wer nur antwortet, ist nur so gut wie die
   letzte fremde Handlung.**
3. **Dreimal derselbe Zug.** Hanseong an Sang-hoon, die Klausel an Nam, die drei
   Freigaben an Hwang: **er bezahlt jedesmal mit Auskunft ueber sich selbst.**
   Das ist nicht nur schwach, das ist handwerklich langweilig.

**Die Diagnose darunter ist eine einzige und sie steht seither im Text:** er hat
auf eine **Gefahr** hingearbeitet und nicht auf ein **Ziel.** *Die Seite stumpf
machen* ist etwas, das man tut, damit etwas nicht passiert. Ein Ziel ist ein
Zustand, den man herstellt. Defensive Ziele erzeugen exakt diesen Bogen, jedes
Mal, unvermeidlich.

**Die Probe, die ab jetzt in jedem Kapitel laeuft:** Was ist am Ende dieses
Kapitels da, das vorher nicht da war, und **gehoert es ihm?** Nicht: was hat es
gekostet. Das steht ohnehin immer da. Es darf Kapitel geben, die nur kosten -
aber nicht zwei nacheinander, und nie drei.

**Und die zweite Probe, fuer die Rechnung selbst:** Wenn ein Kapitel abrechnet,
wird **beidseitig** abgerechnet. In Band 2, Kapitel 8 stand die Kostenseite
vollstaendig da und der Ertrag als *"most of it came out well"*, ohne dass je
gesagt wurde, was. **Ein Kapitel, in dem nur ausbuchstabiert ist, was etwas
gekostet hat, liest sich als Verlust, auch wenn es keiner war.**

**Repariert am 23.08.** Band 2, Kapitel 9 bis 11 wurden vollstaendig neu
geschrieben. Der Umschlag liegt jetzt in Kapitel 9 und er spricht ihn selbst
aus: *"I have been working to a danger and not to a target. ... I have spent
three weeks answering. Tonight I stop."*

### 3. Rueckbezug

**Jede Aussage muss sich an etwas festmachen, das vorher im Text steht.**

- Wer "wie er gesagt hatte" schreibt, sucht die Stelle. Existiert sie nicht, ist
  der Verweis der Fehler und nicht der fehlende Text.
- Eine Figur darf nur wissen, was sie im Text erfahren hat. Wenn sie mehr weiss,
  gehoert die Stelle nachgetragen oder das Wissen gestrichen.
- Zahlen und Zeitangaben werden gegen `doc/05-continuity.md` nachgerechnet. Dort
  lagen alle bisherigen Fehler dieser Art.
- Ein Motiv, das zum zweiten Mal auftaucht, wird nicht beschrieben, als waere es
  neu. Beim zweiten Mal aendert sich etwas daran, nicht die Beschreibung.

### 4. Die Laecheln

`doc/05-continuity.md` fuehrt jede Sorte mit Fundstelle.

- **Wird ueberhaupt gelaechelt?** Der Charme ist Georgijs Hauptwerkzeug. In
  Kapitel 2 bis 6 kommt kein einziges Laecheln vor, und das ist ein bekanntes
  Loch, kein Vorbild.
- **Ist es eine Sorte, die es schon gibt?** Keine neue erfinden, ohne
  nachzusehen.
- **Wem gilt es?** Jedes gebaute Laecheln ist auf ein Gesicht gerichtet und auf
  ein Ergebnis gezielt. Eines ohne Empfaenger ist eine Ausnahme und hat eine
  Geschichte, die in Kapitel 14 anfaengt.
- Dasselbe gilt fuers Lachen. Kang, Sang-hoon, Woo und Hana haben je ein
  wiedererkennbares. **Georgij lacht zweimal**, und der Unterschied ist der
  Punkt: Kapitel 7 an Mrs Sunwoo ueber die Decke, gebaut wie die Laecheln
  daneben, und Kapitel 13 ueber Woos Schiffsagenten, *which was not work*. Der
  Zusatz ergibt nur Sinn, weil es den Vergleichsfall gibt.

### 5. Satzzeichen

- **Fragezeichen** nach der mechanischen Regel in `doc/01-craft.md`:
  Aussagesyntax behaelt den Punkt, Fragesyntax und verkuerzte Fragen bekommen das
  Zeichen. `check.py` meldet Verdachtsfaelle, entscheidet aber nicht.
- **Keine Gedankenstriche**, nur Bindestriche.
- **Anfuehrungszeichen** bei jeder direkten Rede. Erinnerte Rede wird zu
  indirekter umgebaut, statt ohne Zeichen dazustehen.
- **Klare Absatztrennung zwischen Sprechern.** Keine Replik teilt sich einen
  Absatz mit der Handlung eines anderen.
- **Fortgesetzte Rede** ueber mehrere Absaetze: oeffnendes Zeichen an jedem
  Absatz, schliessendes nur am letzten.

### 6. Die Quoten

- "Mistress" hoechstens vier bis fuenf pro Kapitel
- "nicht X, sondern Y" hoechstens einmal
- "would rather X than Y" hoechstens einmal
- Selbstkommentar zur eigenen Redlichkeit hoechstens einmal, und nur als Antwort
- Dieselbe Zahl nicht zu oft. Elf und neun sind bereits stark belastet

### 7. Zum Schluss

```
python3 check.py chNN_vX_Y_en.md
python3 build.py . .
```

Dann `doc/01-craft.md` fuer alles, was ein Programm nicht entscheiden kann.
Dann noch einmal lesen.

---

### Die Formel, die pro Kapitel legal ist

**Gefunden am 24.08. beim Schreiben von Kapitel 28, und zwar von Hand.**
*"did not soften"* stand in dreiundzwanzig von zweiundsechzig Kapiteln,
*"did not look away"* in einundzwanzig. Keine Pruefung hat je angeschlagen.

**Warum nicht, und das ist der eigentliche Befund:** `check.py` zaehlt Tics
**pro Kapitel.** Eine Formel, die genau einmal im Kapitel steht, reisst keine
Quote. Und `--echoes` vergleicht ganze Saetze und Sieben-Gramme, aber
*"He did not soften it"* steckt jedes Mal in einem anderen Satz.

**Die Luecke war genau die Mitte: zu selten fuer die Kapitelquote, zu variabel
fuer den Satzvergleich.** Und genau da sitzt die Sorte Wiederholung, die ein
LESER am staerksten merkt, weil er das Buch am Stueck liest und nicht
kapitelweise.

**Seit dem 24.08. zaehlt `formel_report()` sie ueber beide Baende.** Der nackte
Lauf meldet, was ueber einem Viertel der Kapitel steht; `--echoes` zeigt die
ganze Tabelle. **Bewusst eine feste Liste und kein Automatismus:** was eine
Formel ist und was ein Motiv, entscheidet sich nicht mechanisch.
*"no line, no owner and no date"* steht auch in mehreren Kapiteln und soll das.

**Was daraus folgt, wenn ein Beat gebraucht wird:** die Verneinung ist der
bequemste Beat der Welt und deshalb der erste, der sich selbst kopiert. Wer
zum dritten Mal *did not* schreibt, soll stattdessen sagen, **was die Figur
getan hat.** *"She put all of it down in front of him."* statt *"She did not
soften any of it."*

## Werkzeuge

**Kein Heredoc fuer Python mit Backslashes.** Die Shell frisst den Backslash,
bevor Python ihn sieht: Aus `r"\n\s*\n"` wird in der Datei ein echter
Zeilenumbruch und damit ein SyntaxError, und im schlimmeren Fall ein Regex, der
klaglos etwas anderes trifft. Das ist am 22. August zweimal passiert, einmal in
`check.py` und einmal bei einer Absatzteilung.

**Die Regel:** Alles mit Regex, `\n`, `\t` oder sonstigen Escapes geht ueber das
Datei-Werkzeug oder ueber eine eigene `.py`-Datei. Heredoc bleibt fuer reine
Textersetzung ohne einen einzigen Backslash.

**Und die Gegenprobe dazu**, weil ein SyntaxError laut ist, ein falscher Regex
aber nicht: Nach jedem Eingriff in `check.py` einmal absichtlich etwas
kaputtmachen und nachsehen, ob es feuert. Ein stiller Lauf beweist nichts.

## Prosaregeln

Die Tics in diesem Abschnitt entstehen beim **Ueberarbeiten** neu, nicht nur im
ersten Entwurf. Die Suchliste laeuft nach jeder Runde. `check.py` prueft alles,
was mechanisch pruefbar ist.

### Ton
Kalt, transaktional, Machtdynamik unter Höflichkeit. Dialog trägt die Handlung. Kurze Sätze. Figuren antworten unvollständig, brechen ab, schweigen an der falschen Stelle. Keine Aphorismenketten. Keine "Das ist nicht X, das ist Y"-Konstruktionen, höchstens **eine** pro Kapitel und nur, wenn sie es trägt.

**Zweiter Tic, genauso häufig: "I would rather X than Y".** In Kapitel 14 stand er achtmal, in Kapitel 15 sechsmal. Höchstens **einmal pro Kapitel**, und dann nur, wenn wirklich eine Abwägung gemeint ist. Sonst gerade sagen: "I am going to say it now", "Asking you at the table is cheaper", "You are both getting it tonight".

**Die Suchliste läuft nach jeder Überarbeitung, nicht nur nach dem ersten Entwurf.** Beim Nachbessern entstehen die Konstruktionen neu, weil sie sich beim Erklären von selbst anbieten. In Kapitel 14 waren nach der dritten Runde wieder sechs drin, alle neu.

**Das ist die häufigste Fehlerquelle.** In Kapitel 14 standen neun davon. Vor Abgabe suchen nach: "is not a", "it isn't", "not because", "never ... they", "you would not ... you would", und alles bis auf höchstens eine in gerade Aussage umschreiben. Innere Gedanken bleiben unfertig.

**Fragezeichen, mechanisch entscheidbar.** Steht der Satz in **Aussagesyntax**, darf der Punkt bleiben, auch wenn er eine Antwort erwartet. Das sind Sonden und Annies Grundregister: "You're negotiating." "You don't agree." "And you think they'd tell me." "You advise her."

Steht er in **Fragesyntax** oder ist er eine **verkürzte Frage**, kommt ein Fragezeichen hin, egal wie kalt er ist.

Drei Sorten fallen darunter:
1. **Fragewort allein:** "Then why?" "So why?" "Where?" "Then what?" "How much?"
2. **Umgestelltes Hilfsverb, aber nur wo um etwas gebeten wird:** "May I propose something?" "May I ask why not?" "Then may I have the guest list?" **Hier stand bis zum 23.08. das umgestellte Hilfsverb allein als Kriterium, und das war falsch und widersprach dem Kanon:** *"Was I useful."*, *"Was it worth it."* und *"How long did it take."* sind alle umgestellt und haben alle einen Punkt. Entscheidend ist nicht der Satzbau, sondern ob der andere nein sagen darf. Die volle Fassung der Regel steht in `CLAUDE.md` unter "Punkt oder Fragezeichen".
3. **Bloße Aufforderung zum Weiterreden**, auch wenn sie nur aus einem Wort oder einer Nominalphrase besteht: "And?" "And him?" "And the third?" "And Incheon?" "And the Kims?" Das ist Annies Grundregister und bleibt kalt, es bekommt nur das Zeichen.

Der Unterschied zu Gruppe drei ist einzig, ob ein vollständiger Aussagesatz dasteht. "And you said no." ist eine Sonde und behält den Punkt. "And him?" ist eine Aufforderung und bekommt das Zeichen.

Die einzige Ausnahme sind Abfertigungen, die mit Komma und Redebegleitsatz stehen und dadurch als Nicht-Frage markiert sind: "Will I," Annie said. "Would you," Annie said. Das Mittel ist selten und verliert seine Wirkung, wenn es überall steht.

Imperative sind ohnehin keine Fragen: "Go on." "Say why." "Say how differently."

**Fehler bleiben Fehler.** Georgij darf sich im Nachhinein nicht als heimlicher Planer herausstellen. Wenn ein Patzer gut ausgeht, ist er trotzdem ein Patzer, und er sagt das auch. Seine zwei Sätze dazu in Kapitel 11, beide wörtlich im Text: *"I thought that was a good decision for about three hours."* Und über den Anruf, den er sich selbst eingebrockt hat: *"He didn't have to find the gap. I walked across a room and showed it to him. There is nobody else to put that on."* Das ist die stärkste Schicht des Kapitels und der Maßstab für alles Weitere. Ein unschlagbarer Georgij wäre ein langweiliger.

**Prüfregel:** Jeder Rückverweis muss eine nachweisbare Stelle im Text haben. "Raised it", "used it", "the line", "on its own" sind nur zulässig, wenn im Text steht, worauf sie sich beziehen.

---

---

## Dialogregeln

## Dialogregeln

**Zwischen zwei Blöcken derselben Figur steht immer etwas Körperliches.** Redet eine Figur über mehrere Absätze, muss zwischen ihnen eine Handlung stehen, ein Blick, eine Hand, ein Gesicht, das sich nicht bewegt. Sonst liest sich der zweite Absatz, als hätte inzwischen die andere Figur gesprochen, und der Leser muss zurückspringen und die Sprecher neu abzählen. Der Beat ist keine Verzierung, er ist die Sprecherkennzeichnung.

Beispiel aus Kapitel 17, Annies Rede an der Kreuzung: *Nothing moved in her face anywhere*, dann *She looked away from the chair*, dann zwei Finger auf der Stuhllehne, dann *Her hand stayed where it was*. Vier Blöcke, vier Beats, kein einziger Sprechertag nötig.

**Der Beat soll etwas tun, nicht den Ton etikettieren.** Erlaubt sind Handlungen und Körper. Nicht erlaubt sind Kommentare über die Art des Sprechens, also kein "He kept his voice where it had been", kein "She let it be the size it was". Die Ausnahmen sind rar und müssen sich lohnen.

**Kurze Sätze am Schluss einer Rede.** Wo eine Figur Nachdruck braucht, wird nicht verlängert, sondern gekürzt. "I have never put it down. Not one night." Dann der Beat. Dann "And this is my house."

**Keine Selbstkommentare über die eigene Redlichkeit.** Georgij neigt dazu, seine Genauigkeit anzukündigen, statt genau zu sein: "I am not going to pretend", "I would like to be careful with the word", "I am saying so before I say it". Höchstens einer pro Kapitel, und nur, wenn er auf eine Frage antwortet und Inhalt trägt. Der Rest ist Eitelkeit und liest sich als solche.

**Der Bericht ist kein Duell.** Wenn er ihr etwas meldet, sagt er, was war, und sie nimmt es oder stellt eine Frage. Kein Behaupten, Einwenden, Absichern, Quittieren. "He has bitten." "Yes." Der Beweis stand einen Absatz vorher und wird nicht wiederholt.
- Klare Absatztrennung zwischen den Sprechern. Keine Replik teilt sich einen Absatz mit der Handlung des anderen

---

## Titel, Dateien, Format

### Kapiteltitel

Der Titel kommt aus der Sprache des Gewerbes oder aus einem Satz, der im Kapitel fällt, flach gesagt. Keine Inhaltsangaben, keine Stimmungswörter. Am besten geht er erst im Rückblick auf und verrät vorher nicht, worum es geht.

**Reihenfolge:** erst schreiben, dann den Titel aus dem fertigen Text ziehen. Nie umgekehrt. Bei Kapitel 11 war der Titel zuerst da und der Satz wurde danach ins Kapitel gebaut, und man hat es gemerkt: Die Wendung stand weit vorn und wurde nie eingelöst. Ersetzt durch *Thank you for telling me*, das über der Überschrift wie Höflichkeit klingt und nach dem Kapitel wie eine Strafe.

Bisher: *Merchandise doesn't talk* (die Zeile des Auktionators, die das Kapitel widerlegt), *Quid pro Quo*, *Dead angles*, *Count again* (ihre Provokation an der Tür), *Seven Letters* (sie tippt sie mit einem Finger), *Withdrawn or sold* (Katalogsprache für die Frage, die er nicht stellen darf), *Where were you educated*, *Something to do with my hands* (ihr Satz über das Glas, und seine Antwort darauf), *The friendly ones* (Annies dritte Kategorie), *What did she pay for you*, *Thank you for telling me*, *You are better when you don't know*, *The man with the open hand* (Woos Satz über die sechs Wochen), *In the same size type*, *Four thousand two hundred*, *Where the walls are* (Georgijs eigener Satz an Sang-hoon), *I have never put it down* (Annies Satz am Stuhl, der sein Geständnis überbietet).

Kandidaten für später: *Lot nine*, *In the order it arrived*, *That's why I didn't*, *A quarter of a beat behind*, *What I didn't give her*, *By the terms*, *Chin level*, *Pointed outward*, *No third file*, *Three and a half*.

### Regeln fürs Schreiben
- Keine Gedankenstriche, nur Bindestriche
- Dateien in zwei Formaten: `.md` fürs Archiv, `.txt` zum Einfügen ohne Markdown
- Szenentrenner in der Paste-Fassung als `* * *`
- "Mistress" sparsam einsetzen, höchstens vier bis fünf pro Kapitel. Der Effekt nutzt sich ab

---

## Pruefliste vor der Abgabe

`check.py` erledigt alles Mechanische. Diese Liste ist fuer das, was ein Programm
nicht entscheiden kann. Sie ist aus tatsaechlichen Fehlern entstanden, nicht aus
guten Vorsaetzen.

---

### Zuerst, weil es am meisten kostet

**Zweimal lesen, bis zweimal nichts gefunden wird.** Der zweite Durchgang findet
regelmaessig noch etwas, und der dritte manchmal auch. Was der erste Durchgang
findet, ist selten das Schlimmste.

**Beim Reparieren entstehen neue Fehler.** Fast jede Runde hat neue Tics
eingebaut, weil sie sich beim Erklaeren von selbst anbieten. Nach jeder
Korrektur laeuft `check.py` erneut, nicht nur nach dem ersten Entwurf.

---

### Zeitangaben

**Datumszeilen prueft `check.py`. Die Angaben im Fliesstext nicht.** Dort lagen
alle bisherigen Fehler. Jedes "seit X Tagen", "vor drei Wochen", "in fuenf
Wochen" gegen den Kalender in `doc/05-continuity.md` nachrechnen.

Gefunden wurden auf diese Weise: Noh geht "in fuenf Wochen", waehrend zwei
Absaetze vorher steht, dass er Ende des Monats geht. Ein Kapitel an Tag 27
zaehlt "achtundzwanzig Tage". Annie hat den Namen "achtundzwanzig Tage", obwohl
ein anderes Kapitel neunzehn Tage an einem frueheren Tag sagt.

**Das Buch zaehlt inklusiv.** An Tag 22 ist er zweiundzwanzig Tage im Haus.

### Rueckverweise

**Jeder Rueckverweis braucht eine nachweisbare Stelle.** Wer "wie er gesagt
hatte" schreibt, sucht die Stelle. Wenn sie nicht existiert, ist der Verweis der
Fehler und nicht der fehlende Text.

Dasselbe gilt fuer scheinbar harmlose Details: eine Clutch, die es in dieser
Szene nicht gibt, ein Fahrer, der laut Rota diese Woche nicht faehrt, ein
Gegenstand, den er laut Kanon nicht besitzen kann.

### Wiederholung ueber Kapitelgrenzen

**Ein Motiv, das zum zweiten Mal auftaucht, darf nicht beschrieben werden, als
waere es neu.** Der schwerste Fund dieser Art: Das ungebaute Laecheln wurde in
zwei Kapiteln jeweils als erstes seiner Art eingefuehrt.

Beim zweiten Auftreten aendert sich etwas daran, nicht die Beschreibung. Beim
Apfel ist es die Laenge, beim Laecheln die Geschwindigkeit.

**Formeln zaehlen ueber das ganze Buch.** "There was no version of the evening
in which", "let that sit exactly as long as it needed", "turned his hand over".
Zweimal pro Kapitel ist die Grenze, und ueber vier Kapitel hinweg faellt es auf.

**Und genau das war eingetreten, gemessen am 23.08. mit `--echoes`, nachdem der
Text fertig war.** Die Regel stand seit Monaten da und niemand hatte gezaehlt:

| Formel | vorher | jetzt |
|---|---|---|
| *turned his/her hand over* | **15 Kapitel**, 20 Stellen | 6 Kapitel |
| *He kept his hands where they were* | 7 | 2 |
| *did not look away* (zwei Fassungen) | 6 Kapitel, 8 Stellen | 2 |
| *The room went on being a room* | 5 | 2 |

**Zwei Funde dabei waren schwerer als die Zahlen.**

**Erstens: die Handbewegung wird zweimal als neu eingefuehrt.** Kapitel 1 sagt
*"an old and elegant little gesture"*, Kapitel 11 sagt *"an old gesture and a small
one"*. Das ist derselbe Fehler wie beim ungebauten Laecheln, eine Ueberschrift
weiter oben beschrieben, und er stand hier vier Monate unbemerkt daneben. Kapitel
11 sagt jetzt *"smaller than he had done it in a car on the first night"*, also
aendert sich etwas daran statt es zu wiederholen.

**Zweitens: die Geste gehoert Georgij, und zwei andere Figuren hatten sie.** Hana
in Kapitel 21 und Annie in Kapitel 34. Ein Tell, das drei Leute haben, ist keins.
Beide gestrichen.

**Wie ersetzt wurde, und warum meistens gar nicht.** Der haeufigste Fall war ein
Beat mitten in einer Rede, direkt nach einer kurzen Frage des anderen. Dort war der
Sprecher ohnehin eindeutig, der Beat also reine Fuellung, und die beiden
Redehaelften wurden zu einer zusammengezogen. Ein eigener Beat kam nur dorthin, wo
die Rede lang genug fuer eine Zaesur war, und dann aus der Szene: das Kinn nach dem
Stift, den Annie hingelegt hat, ein Mann, der sich nicht gesetzt hat.

**Was ausdruecklich stehen bleibt: *He kept his chin level*, sechs Kapitel.** Das
ist keine Formel, das ist eine Anweisung. Der Schneider gibt sie ihm in Kapitel 5
im Wortlaut: *"You'll want to keep your chin level. Not up. Level. Men lift the
chin when there's something at the throat and then everybody looks at the throat."*
Sechs Wiederholungen sind die Anweisung, die wirkt. **Wer das beim naechsten
Zaehldurchgang mit abraeumt, streicht den einzigen Beleg dafuer, dass Georgij eine
Lehre angenommen hat, die ihn nichts gekostet hat.**

### Der Bericht ist kein Duell

Wenn Georgij meldet, sagt er, was war, und sie nimmt es oder stellt eine Frage.
Kein Behaupten, Einwenden, Absichern, Quittieren. Wenn eine Antwort nur die
vorige Aussage bestaetigt, streichen.

Probe: Faellt eine Replik weg und die Szene verliert nichts, war sie Fuellung.

### Georgij kommentiert nicht seine eigene Redlichkeit

Er kuendigt seine Genauigkeit an, statt genau zu sein. `check.py` findet die
haeufigsten Formeln, aber nicht alle. Erlaubt ist einer pro Kapitel, und nur
als Antwort auf eine Frage.

**Die haeufigste Form davon ist die Verneinungsansage**, und sie ist am 22.08.
zweimal aus Kapitel 19 gestrichen worden:

> But she does not fill this quay ~~and I am not going to sit here and let you think she does~~.
>
> "It is the same account." ~~"I am not going to say more than that, because~~ more than that would be a guess."

**Beide Male sagt der Satz die Sache und kuendigt danach an, dass er sie sagt.**
Der zweite Teil ist immer streichbar, und ohne ihn wird der Satz haerter.

**Wo die Form bleibt.** Sie ist kein Verbot, sie ist eine Quote. In Kapitel 16
ist sie das Geraet des Kapitels: *"I will not say anything to you that is
untrue"*, *"I will not change the subject"*, und viermal identisch *"I am not
going to answer that"*. Dort haelt sie den ganzen Abend zusammen.

**Die Probe:** Steht die Verneinung fuer eine Regel, die er gerade aufstellt?
Dann bleibt sie. Beschreibt sie nur, was er ohnehin gerade tut? Dann weg.

**Die zweite Form derselben Sache**, am 22.08. ein drittes Mal in Kapitel 19
gefunden: Er sagt etwas und haengt an, welche unehrliche Alternative er dabei
nicht waehlt.

> "…she would have signed it in the morning, ~~and I would have told you so instead of standing here implying otherwise~~."

**Die Ausnahme, und sie ist wichtig:** Wenn ein **Grund** danebensteht, ist es
kein Selbstlob, sondern ein Argument. Kapitel 4: *"I'm telling you that instead
of letting you find it, because you'd find it before lunch and then we would be
having a different conversation."* Das ist Rechnen und darf bleiben. Ohne den
Grund bleibt nur die Haltung uebrig.

**Ueber alle neunzehn Kapitel gescannt** (`instead of standing/pretending/
letting`, `rather than pretend`, `let you think`, `implying otherwise`): sechs
Treffer, davon zwei bei Annie, einer Erzaehlung, einer die Regel aus Kapitel 16,
einer das Argument aus Kapitel 4 - und genau einer die reine Form, in Kapitel 19.
Es ist kein systemischer Tic, sondern eine Stelle, die dreimal repariert werden
musste, weil ich sie beim Lesen jedes Mal ueberging.

**Zaehlung ueber alle neunzehn Kapitel**, damit die Groessenordnung bekannt ist:
achtundzwanzig Vorkommen, davon elf allein in Kapitel 16 (Geraet) und vier in
Kapitel 19, von denen zwei Georgij gehoerten und gestrichen wurden. Wenn eine
Figur ausser Georgij sie benutzt, zaehlt sie nicht mit.

### Wer weiss es, und woher

**Jede Figur darf nur sagen, was sie im Text erfahren hat oder aus dem ableiten
kann, was sie hat.** Das steht schon oben unter Rueckbezug, aber es bricht am
haeufigsten in Verhandlungsszenen, weil dort die Planungsdokumente danebenliegen
und ihre Formulierungen mitwandern.

**Der Fall vom 22.08.** Chairman Woo sagte in Kapitel 19: *"You wrote nineteen
pages to ruin a man, so that a second man does not get a company, so that the
woman who owns you ends up with her hand on the throat of everybody else in her
own trade."*

Der Satz stammt fast woertlich aus `doc/04-world.md`, wo er als Notiz ueber
Georgijs Lage steht. **Woo erfaehrt im ganzen Kapitel nichts von den neunzehn
Seiten, nichts von Hanseong und nichts davon, dass jemand ruiniert wird.**
Georgij wuerde ihm das auch nicht erzaehlen; es ist nicht seins.

**Was Woo tatsaechlich hat**, und es reicht vollstaendig: dass Georgij ihn bittet,
neben die Kims zu treten, und die Antwort auf seine eigene Frage, was Annie von
den Kims nimmt - *"Shares, security and a veto over routes."* Was ein
Routen-Vetorecht ist, weiss er nach einundfuenfzig Jahren selbst. Also lautet der
Satz jetzt: *"You came out here to save a family, so that the woman who owns you
ends up with her hand on the throat of everybody else in this trade."*

**Und er wird dadurch besser**, weil Woo es sich selbst aus einer einzigen
Antwort zusammensetzt, statt es erzaehlt bekommen zu haben.

**Die Probe vor jeder Verhandlungsszene:** Fuer jeden Satz, den eine Nebenfigur
ueber die Lage sagt, die Stelle benennen, an der sie es erfahren hat. Findet man
sie nicht, ist entweder der Satz falsch oder die Stelle fehlt - und in einem
Planungsdokument gelesen zu haben zaehlt nicht.

### Fehler bleiben Fehler

Er darf sich nicht nachtraeglich als heimlicher Planer herausstellen. Geht ein
Patzer gut aus, ist er trotzdem ein Patzer, und er sagt das auch. Ein
unschlagbarer Georgij waere ein langweiliger.

### Ihre Repliken

Annie darf nicht zum Taktgeber werden, der nur Stichworte gibt. Wenn ihre
Repliken ueberwiegend vier Woerter oder weniger haben und sie am Schluss
ploetzlich zwei Absaetze bekommt, stimmt die Verteilung nicht.

Sie erklaert nichts. Sie gibt nichts her, was sie nicht hergeben wuerde.

**Fragezeichen: drei Klassen, nicht eine.** *Korrigiert am 22.08.*, nachdem ich
zweimal eine berechtigte Ruege mit einer falschen Zaehlung abgewehrt habe.

Annie, Sang-hoon und Woo sprechen oft in flachen Aufforderungen statt in Fragen,
und das ist Figurenzeichnung: Leute mit Macht fragen nicht, sie fordern auf. Nur
gilt das fuer **zwei** Satzarten und nicht fuer drei.

| Art | Beispiel | Satzzeichen |
|---|---|---|
| Aufforderung | *"Say the rest." "Go on." "Tell me now."* | Punkt |
| Behauptung als Aufforderung | *"And you want." "And it's all true." "So she never has to sign."* | Punkt. **Das ist das Geraet** |
| **Echte Frage** | *"Why." "What does it cost me." "Which is sixteen."* | **Fragezeichen** |

**Die Probe:** Fragt die Zeile nach etwas, das der Sprecher nicht weiss? Dann ist
es eine Frage, egal wie hart die Figur ist. *"And you want"* ist eine Behauptung,
weil Sang-hoon weiss, dass Georgij etwas will, und ihm nur den Rahmen hinlegt.
*"Which is"* ist eine Frage, weil Annie die Antwort nicht hat.

**Wie der Fehler entstanden ist**, damit er sich nicht wiederholt: `check.py`
meldet *"Fragezeichen pruefen"*, und ich habe die Meldung zweimal als
stilistisches Geraet abgetan, gestuetzt auf eine Zaehlung von siebenundsiebzig
flachen Aufforderungen im ganzen Buch. Die Zaehlung warf alle drei Klassen
zusammen. Getrennt nachgezaehlt standen **saemtliche echten Fragen mit Punkt in
den Kapiteln 16 bis 19**, also in dem, was an einem Tag geschrieben wurde. Die
siebzehn Kapitel davor machen es nirgends. Es war kein Geraet, es war ein
frischer Tic.

**Merke:** Eine Statistik, die drei Sorten in einen Topf wirft, verteidigt
zuverlaessig den Fehler, den sie enthaelt.

### Zahlen

Dieselbe Zahl nicht zu oft. Elf und neun sind im Buch bereits stark belastet.
Wenn eine Zahl tragend ist, etwa vier Waende und vier Schweigen, muessen die
beilaeufigen Vieren weichen.

**Und die teure Regel: eine Zahl aus einem Dokument wird nachgerechnet, nicht
nachgeschlagen.** Am 23. August haben an einem einzigen Tag **zwei**
Hilfsdokumente ihren eigenen Fehler in den Text geschrieben.

**Die Fahrerwoche.** Die Tabelle in `doc/05-continuity.md` liess die Woche vom
6. bis 12. Dezember aus und beschriftete die folgende darum falsch. Kapitel 29
stand danach auf *"Mr Ku had him at the gate at six, which was his week"*,
waehrend Kapitel 28 drei Tage vorher, am Wechseltag selbst, Mr Pyo fahren
liess. Zwei Kapitel nebeneinander, zwei Fahrer in derselben Woche.

**Die Kim-Anteile.** `doc/04-world.md` schrieb *"41,4 Prozent verteilt auf sechs
Leute"*. Kapitel 15 zaehlt sie einzeln auf und ist Kanon: elf, neun, sieben,
sechs, vier, vier. **Das sind 41.** Die 1,4 sind Ye-rins eigene und kommen
obendrauf. Aus dem Dokument wanderte die falsche Summe in Kapitel 30 und in
Kapitel 31, beide Male in einen betonten Satz.

**Was beide Faelle gemeinsam haben:** Das Dokument wurde *gelesen* und nicht
*geprueft*. In `doc/07-next.md` stand sogar ausdruecklich "Ihre Zahlen, gegen
`doc/04-world.md` geprueft" - ein Dokument gegen ein Dokument, und addiert hat
nie jemand. **Ein Hilfsmittel, das gegen den Text gehalten wird, muss selbst
gegen den Text geprueft werden**, sonst schreibt es den Fehler hinein, statt
ihn zu finden.

**Und was `check.py` daraus bekommen hat:** eine Liste `WRONG_PHRASES`, fuer
Wendungen, die einmal falsch dastanden und nie wiederkommen duerfen. Der erste
Versuch war ein Eintrag in `FACTS` - und der war **toter Code**, weil `QUANTITY`
bei *"forty-one per cent"* das Substantiv als `per` liest. Er lief still und sah
nach Schutz aus. Erst die vorgeschriebene Gegenprobe hat ihn auffliegen lassen.

### Zuletzt

**Der Titel wird nach dem Schreiben aus dem fertigen Text gezogen**, nie
vorher. Einmal war es umgekehrt und man hat es gemerkt.
