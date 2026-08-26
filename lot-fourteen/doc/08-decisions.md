# Entscheidungen und Verworfenes

## Das Projektverzeichnis haelt nur noch die zwei Lesefassungen, 25.08.

**Vom Autor gewuenscht.** In `lot-fourteen/` lagen neben `book-band-1.md` und
`book-band-2.md` noch vier Skripte, drei erzeugte Dokumente, eine README und
vier Dateien lokalen Muells. Jetzt:

| | |
|---|---|
| `werkzeug/` | `build.py`, `check.py`, `reader.py`, `zuschreibung.py`, `stimmen.py`, `belege.py`, `faktenspur.py` (die letzten drei kamen am 25.08. dazu) |
| `erzeugt/` | `HANDBUCH.md`, `BEGEGNUNGEN.md`, `MANIFEST.txt` |
| `doc/00-readme.md` | war `README.md` |
| geloescht | `live.txt`, `chapters_live.txt`, `chapters-2_live.txt`, `__pycache__/` (nie verfolgt) |

**`CLAUDE.md` bleibt liegen, und das ist keine Nachlaessigkeit.** Claude Code
laedt die Datei ueber ihren Ort. Wer sie verschiebt, nimmt allen drei Sitzungen
ihre Anweisungen weg.

**Die Aufrufe haben sich geaendert:**

    python3 werkzeug/check.py chapters/chNN_vX_Y_en.md
    python3 werkzeug/build.py

**Und der eigentliche Eingriff steckt nicht im Verschieben.** `check.py` und
`zuschreibung.py` haben ihr Projektverzeichnis aus **dem eigenen Dateipfad**
abgeleitet (`os.path.dirname(os.path.abspath(__file__))`). Ein blosses
Verschieben haette sie sofort und still kaputtgemacht: sie haetten
`werkzeug/doc/` und `werkzeug/chapters/` gesucht. Beide **suchen die Wurzel
jetzt**, statt sie anzunehmen - nach oben, bis ein Verzeichnis `chapters/` und
`doc/` enthaelt. Damit laufen sie von ueberall, auch aus der Repo-Wurzel.

**Geprueft:** `book-band-1.md` und `book-band-2.md` sind nach dem Umbau
**byte-identisch** (gleiche Pruefsumme wie vorher). Die Action ist nachgezogen,
sowohl die zwei Aufrufe als auch die Liste der zurueckzuschreibenden Dateien.

---

Damit nichts zweimal verhandelt wird und Gestrichenes nicht durch Zufall zurueckkommt.

---

## Das Ziel von Band 2 ist ausgewechselt, 25.08.

**Vom Autor entschieden, und es ist die groesste Entscheidung des Tages.** Sie
stand bis zum Dokumentendurchgang nur in `doc/07-next.md` - **und genau deshalb
hat das alte Ziel dort achthundert Zeilen weiter unten unveraendert als Kanon
weitergestanden.** Ein Ziel, das nirgends als Entscheidung gefuehrt wird, hat
nichts, was auf es zeigt, wenn es sich aendert. Deshalb steht es jetzt hier.

| | |
|---|---|
| **Alt, bis 25.08.** | *Dass die Zeile nicht gegen sie verwendbar ist* |
| **Neu, ab 25.08.** | **Choi Dae-ho hat am Ende nichts. Niemand geht an sein Telefon. Niemand isst mit ihm.** |

**Die Begruendung ist eine Handwerksregel und keine Geschmacksfrage.** `doc/01-craft.md`
Abschnitt 2i sagt seit Kapitel 11: ein Ziel ist ein Zustand, den man
**herstellt**; wer auf eine **Gefahr** hinarbeitet, bekommt einen bestimmten
Bogen, *jedes Mal, unvermeidlich*. Die Regel stand da, das Ziel wurde nie
geaendert, und die vorhergesagte Folge ist eingetreten: Kapitel 26 bis 45 sind
eine einzige Ermittlung, ab 35 stehen elf Kapitel lang drei Menschen im Buch,
und Georgij laechelt in 46 Kapiteln kein einziges Mal.

**Was daraus folgt und leicht uebersehen wird:** Choi war in der Tabelle
*Gegner, Gegenstand, Ziel* als **Gegner** gefuehrt, der Nam die Waffe gibt.
**Er ist jetzt das Ziel.** Fuer Nam und den Sanierer stimmt die Zeile weiter.

**Die Probe fuer jedes geplante Kapitel:** *bringt es Choi einen Anruf naeher an
niemanden?*

---

## Geburtstage werden nicht mehr geparkt, 25.08.

**Aus der Not entschieden, nicht aus Ueberzeugung.** Das Verfahren war: alle
erfundenen Geburtstage in die unerzaehlte Strecke Juli bis September legen,
damit jede Figur ueber beide Baende genau **eine** Altersangabe hat. Das hat
getragen, solange diese Strecke unerzaehlt war.

**Sie ist es nicht mehr.** Band 2 stand am Morgen des 25.08. bei Kapitel 65 und
dem 1. September, am Abend bei Kapitel 69 und dem 9. September, und **Tag 366
ist der 4. Oktober** - der Jahrestag der Auktion, auf den das Buch sichtbar
zulaeuft. Vier Alter standen an einem Tag gegen ihren eigenen Geburtstag: Yeom,
Woo, Mrs Sunwoo und Annie.

**Ab jetzt gilt die Spalte *Geburtstag* als Datum und nicht als Parkposition:**
ab diesem Tag ist die Figur ein Jahr aelter, und `doc/05-continuity.md` sagt es
in der Tabelle. Neue Figuren bekommen ihren Geburtstag weiterhin hinter der
Erzaehlfront, damit ihre Zahl bis dahin stillsteht.

**Der Fall, an dem es haengt, ist geprueft und harmlos:** Georgij wird an Tag
344, dem 12. September, **siebenundzwanzig**. Seine Sechsundzwanzig steht im
ganzen Buch nur zweimal, und beide Male ist es der Katalog vom 4. Oktober -
*"Lot fourteen. Male, twenty-six."* und der Widerhall in Kapitel 2. Datierte
Papiere, keine laufende Altersangabe. **Kein Satz muss umgeschrieben werden.**

---

## Annie erklaert sich in Kapitel 62, und das ist erlaubt, 25.08.

**Vom Autor entschieden.** `doc/12-stimmen.md` fuehrt als Annies staerkste Regel:
*sie erklaert nie die Sache, sie erklaert **ihn**.* In der neuen Passage in
Kapitel 62 erklaert sie sich selbst - und das ist **kein Fehler und keine
Abweichung, die repariert werden darf**.

**Der Grund:** sie ist aufgebracht. Georgij hat ihr gerade gesagt, dass ihr
Gestaendnis eine Kategorie verwechselt, und er hat es mit ihrem eigenen Satz vom
sechzehnten Maerz belegt. An dieser Stelle ist der Regelbruch die Figur und
nicht der Fehler.

**Wer einen Stildurchgang macht, laesst diese Passage stehen.** Sie wuerde sonst
genau als das auffallen, was sie ist: eine Abweichung von einem gemessenen
Muster. Sie ist gewollt.

---

## Entscheidungen

Damit nichts zweimal verhandelt wird. Jeder Eintrag sagt, was entschieden wurde
und warum, nicht nur was gilt.

### Was aus Kapitel 2 gestrichen wurde und nicht zurückkommt

- **Ein dritter Stromstoß.** Es sind zwei, hier und überall.
- **Ein eigener Fahrer.** Es gibt keinen. Georgijs "Three, including the woman who pays you" aus Kapitel 1 zählt Annie, den Wachmann und ihn selbst.
- **Die Protokollszene.** Annie kann ihm keinen Regelbruch vorwerfen, den es noch nicht gibt, und tut es auch nicht. Sie verweigert ihm stattdessen die Regel.
- **Der Wachmann als Menschenkenner.** Er analysiert Georgij nicht und bekommt von Annie kein Lob.
- **Der Brieföffner.** Ersetzt durch die Nagelschere aus dem Maniküre-Etui.

---

### Im Keller gilt kein Handyverbot

**Entschieden: es gibt keins, und es darf keins geben.**

Aufgekommen an einem Plakatentwurf, der neben dem Podium ein Schild mit
`NO PHONES` trug. Sieht plausibel aus fuer ein Haus, das auf Unsichtbarkeit
gebaut ist. Es kostet aber drei Stellen, und die dritte ist teuer:

- `ch01:70` - Georgijs Beweis, dass der Mann in der zweiten Reihe fremdes Geld
  bietet: *"both times he stopped to look at his phone before he raised his
  hand. He isn't checking a message. He's checking a figure, and he didn't set
  it."* Ohne Telefon gibt es die drei Sekunden nicht, in denen er ihn ruiniert.
- `ch01:80` - der Moment, in dem der Saal kippt: *"Two of the middlemen at the
  front already had their phones in their hands."*
- `ch02:86` - und hier wird es tragend. Georgij baut in der Auffahrt sein
  ganzes Angebot darauf: *"He read a figure off his phone before every raise.
  Somebody set that figure and somebody stood behind him in the room tonight.
  That somebody has money and no face."*

Das ist die Herkunft des **Namens des Garanten**, also des Fadens, der ueber
Kapitel 6, 11, 12 und 15 laeuft und den Annie bis heute nicht herausgibt. Ein
Handyverbot nimmt nicht eine huebsche Beobachtung weg, sondern den Ursprung des
zentralen offenen Fadens.

**Was stattdessen geht:** Das Haus verbietet Namen, nicht Geraete. `ch01:12`
sagt es schon: *"A notary signed it. A bank recorded it. Nobody had to say
anything out loud."* Ein Schild mit `NO NAMES` ist Kanon, `NO PHONES` nicht.

---

### Im Keller sitzen neunzehn, und sonst niemand

**Entschieden: die dreihundert Zuschauer sind gestrichen.**

`ch01:74` maß den Saal ein zweites Mal: *"there were three hundred people
watching, and a man who shocks the merchandise without instruction in front of
nineteen buyers has a difficult conversation ahead of him."* Zwei Zahlen für
denselben Raum, im selben Satz.

Die neunzehn sind tragend, die dreihundert waren es nie:

- `ch01:40` setzt die Sitzordnung, Platz für Platz: *"Nineteen buyers. Seven at
  the front with notebooks and no drinks... Nine in the middle, drinking... Three
  at the back."*
- `ch01:78`, vier Zeilen unter der gestrichenen Stelle, handelt der Text danach:
  *"Nineteen people turned to look at him at once."*
- `ch06:84` ist Georgijs eigene Rechnung: *"after it had opened its mouth in
  front of nineteen people."*
- `ch06:94` ist der Grund, warum es keine Ermessensfrage ist. Er sagt über die
  drei Kellergäste auf der Gala: *"the three of them are the only people in that
  building who know what I am."* Drei von neunzehn ist eine Belastung, die man
  tragen kann. Drei von dreihundert ist keine Aussage.

Der Faden über Kapitel 6 - die drei Namen auf den einundneunzig, Annies
*"it's been handled"* - setzt voraus, dass der Keller abzählbar war. Gestrichen
wurde deshalb nur die Zwischenklausel, ohne Ersatz: die Sitzordnung vier
Absätze früher setzt den Maßstab besser, als eine Zahl es könnte.

**Nicht angetastet:** *"in a room where everything else was full"* (`ch01:42`).
Ein kleiner voller Raum ist genau der Punkt, und er macht die zwei leeren Plätze
neben Annie erst sichtbar. Die achthundert der Gala sind ein anderer Saal und
bleiben.

---

### "Thank you" ist ein Mittel und keine Wiederholung

**Entschieden: bleibt, wie es ist. Nicht ausdünnen.**

Der Satz steht siebzehnmal im Prosatext, achtzehnmal, wenn man die Überschrift
von Kapitel 11 mitzählt. Sechzehn der siebzehn sind Georgijs, genau eines ist
Annies, und das ist die Zeile, die dem Kapitel den Titel gibt.

Das ist keine Formel, die sich abnutzt, sondern eine Figureneigenschaft. Es ist
das Einzige, was er zu geben hat: an Ji-won für eine Lampe, an den Schneider, an
Jang, an Hong für den dritten Namen, an Kang. Wer nichts besitzt, dankt oft.

**Und der Ausfall trägt.** In Kapitel 14 bis 17 steht kein einziges. Das letzte
im Buch ist Kapitel 13 an Chairman Woo. `doc/05-continuity.md` begründet die
Wortlosigkeit für die festgelegte Zeile in Kapitel 17 ausdrücklich, aber sie
reicht über vier Kapitel und nicht über eine Szene. Zweimal wird das Danken im
Text zusätzlich abgewiesen: "Don't thank me yet" (Hana) und "Don't thank me. I
have not given you a name." (Woo).

Wer die Zahl in einem Durchgang für einen Tic hält, streicht das Mittel und den
Ausfall in derselben Bewegung.

---

---

### Was in Fassung 1.9 repariert wurde

Alles gegen die damals sechzehn Kapitel und den damaligen Dokumentbestand geprueft. Historischer Eintrag, vor dem Umbau auf `doc/01` bis `doc/08`.

**Widersprüche zum Kanon, geändert:**

1. Block A endete angeblich auf "There are no exits, Georgij." Der Satz wird im Text beantwortet und ist nicht das Ende.
2. Block A: Bae macht drei Dinge richtig, nicht eines.
3. Block A und I: die tote Zone hinter den östlichen Rosen existiert nicht. Kamera vierundzwanzig sieht genau dorthin, Georgij weiß es seit Tag zwei, Jang seit Tag vier, Tae-min steht zweimal die Woche davor.
4. Block B: Jang ist Interimschef und kein Ersatz für den Wachmann. Er kam ohnehin, weil Noh geht.
5. Block B: "knackt ihren Rechner" ist falsch. Die Maschine hing nie an einem Netz, er hat ihr beim Tippen zugesehen.
6. Block B: "der erste Moment, in dem sie ihn wirklich ansieht" widerspricht Kapitel 1 bis 3. Gestrichen.
7. Block B: Los elf wird zweimal gefragt, nicht einmal, Kapitel 1 und Kapitel 4. In Kapitel 6 fragt er nicht mehr, sondern stellt fest, und darauf gibt es eine Antwort, nämlich "No". Das ausdrückliche Nicht-Fragen steht als eigener Satz im Text.
8. Gala: Kapitel 6 ist der Tag der Gala selbst, nicht der Tag davor.
9. Gala und Block C und E und F: **es gibt keine Visitenkarte.** An allen vier Stellen entfernt.
10. Block C: Sang-hoon sitzt an Tisch zwei, nicht an der Bar. Das Wort "ewig" fällt nicht.
11. Block C: die Allianz entsteht nicht auf der Gala. Annie und Hana wechseln dort kein Wort, nach Absprache.
12. Block C: Min-ho nennt Georgij nicht einen Lügner und spricht ihn gar nicht an. Die Ausbildungsfrage kommt von Hong.
13. Gala: keine stillen Tische. Neun Lose, Paddel, Holzhammer, Los neun ist Chef Bang.
14. Block E: Hanseong darf nicht an Kang gehen. Der Köder gehört Sang-hoon allein und liegt seit Tag 46 bei ihm.
15. Block E: schwarze Karte, Shilla, Donnerstag neun Uhr sind unbelegt und als Vorschlag markiert.
16. Block F: der Namensbruch ist der zweite. Der erste war in Kapitel 9 zu Hana und wurde in Kapitel 11 selbst gemeldet.
17. Block G: die zwei bis drei beiläufigen Nennungen von "quid pro quo" sind geliefert, es sind vier, Kapitel 3 bis 6. Beiläufig fällt der Satz ab jetzt nicht mehr. Kapitel 17 benutzt ihn einmal gewichtet, als Auftakt zu Georgijs eigenem Geständnis im Wagen; das ist die verbrauchte Ausnahme, danach kommt er erst im Bruch wieder.
18. Block I: der Sake vom eigenen Geld widerspricht `doc/02-leads.md` ("Er besitzt nichts"). Drei Auswege benannt, einer empfohlen.
19. ~~Block H: Georgij raucht nirgends und besitzt nichts. Die Zigarette braucht vorher eine halbe Zeile Herkunft.~~ **Gegenstandslos, Block H ist am 22.08. gestrichen.** Damit faellt die Zigarette samt ihrer Herkunftsschuld weg.

**Ergänzt:**

20. Blockübersicht mit Kapitelzuordnung und Statusmarkierungen.
21. Abschnitt "Was der Plan nicht hatte" für Kapitel 12 bis 16.
22. Die Lücke an Tag 45: Unterschrift und zweite Abteilung sind verabredet, aber nicht geschrieben.
23. Sang-hoons Rückgabetermin für die neunzehn Seiten, Tag 48, Donnerstag 20. November.
24. Der offene Faden aus Kapitel 10, dass Georgij angeboten hat, ein Abendessen selbst zu bezahlen. Hängt an derselben Frage wie der Sake.
25. Reihenfolge ab hier neu sortiert, Erledigtes herausgenommen.
26. Figurenabschnitt entdoppelt, `doc/02-leads.md` und `doc/03-cast.md` sind massgeblich.

**Außerhalb dieser Datei aufgefallen, nicht geändert:**

Drei Sachen, die Kapitel betreffen und die ich deshalb nicht angefasst habe. Sag Bescheid, was Du damit willst.

- **Kapitel 12, Kangs Anruf: "Chairman Woo has told several people that you asked him the same thing."** Kapitel 11 und Kapitel 16 führen als die zwei Verwendungen des Griffs beide Hong und Kang, nicht Woo. Es ist rettbar, und zwar ohne Änderung: Georgij zählt zwei, weil er Hong und Kang meint, und Woo hat unabhängig davon erzählt, dass der Neue sich von ihm die ganze Geschichte von vor der Hafenbehörde erklären lassen wollte, was aus Woos Sicht dieselbe Bitte ist. Dazu passt auch "some minutes earlier", denn Woo war in Kapitel 10 tatsächlich Minuten vor Kang dran, während Hong dreieinhalb Stunden früher lag. Wenn das so gemeint war, steht es nirgends, und beim nächsten Durchgang stolpert ein Leser darüber. Entweder Hong einsetzen und "some minutes earlier" ändern, oder eine halbe Zeile, die Woos Version erwähnt.
- **Zehn oder elf Minuten.** In Kapitel 9 sagt die Erzählstimme, Hana sei elf Minuten freundlich zu ihm gewesen, in Kapitel 11 sagt Georgij zehn. Einer von beiden rundet, und wenn das Absicht ist, ist es unsichtbar. Elf ist außerdem die Zahl, die in diesem Buch ohnehin schon am meisten arbeitet.

---

## Offene Ausstattungsfragen und Verworfenes

Was noch nicht entschieden ist, und was aus dem Rohverlauf ausdruecklich nicht
uebernommen wird. Beides gehoert festgehalten, damit es nicht durch Zufall
zurueckkommt.

### Was aus dem Rohverlauf nicht übernommen wird

- **Die unbekannte Nummer**, die Georgij per SMS die Gästeliste und Kangs Abendessen zuspielt. Es gibt sie bei uns nicht. Er findet beides selbst.
- **Seoyoung** als zweiter Name für Hanseong.
- **Zehn Jahre im Käfig.** Bei uns sind es siebzehn, seit er neun war.
- **Die 10 und die 60 Millionen.** Bei uns 220 Millionen, durchgehend. Für Los elf gilt achtzig heute, sechzig im nächsten Katalog.

---

### Offene Ausstattungsfrage: der Laptop

Georgij kann Systeme knacken (`doc/02-leads.md`), an Annies Desktop aber nicht: Die Maschine hing nie an einem Netz, er hat ihr die sieben Buchstaben abgesehen. Dafür braucht er Hardware, und woher er sie bekommt, ist selbst eine Szene.

**Vorschlag:** Annie gibt ihm in der ersten Woche unaufgefordert ein Gerät. Neu, sauber, offensichtlich verwaltet, mit allem, was ein Firmengerät eben mitbringt. Sie sagt nichts dazu und er fragt nichts. Er bedankt sich und benutzt es ausschließlich für die Arbeit, die sie ihm gegeben hat.

Das ist die Ladung für die Desktop-Szene in Block B. Sie hat ihm ein Werkzeug an der Leine gegeben, er ist um die Leine herumgegangen und sagt es ihr von sich aus, weil er nicht lügt. Sie fragt weder wie noch was er gesehen hat.

Wenn er stattdessen darum bitten müsste, wäre es auch ein Test, denn sie prüft ihn daran, worum er bittet. Beides funktioniert. Ich halte das Geschenk für stärker, weil es sie zur Handelnden macht und den späteren Bruch teurer.

---

### Das Halsband in der festgelegten Zeile von Kapitel 17

**Entschieden am 22.08., ausdrücklich, weil es eine festgelegte Zeile berührt.**

Das Halsband fehlte über Kapitel 14 bis 17 vollständig, also im ganzen Schluss.
Kapitel 16 ist in Fassung 1.11 geschlossen worden, an der vierten Wand. Für
Kapitel 17 ist die Stelle die Beichte über das Wort *Mistress*, denn dort sagt
er, dass es wahr geworden ist, und der Gegenstand, der es von Anfang an
zutreffend gemacht hat, sitzt an seinem Hals und stand nirgends.

**Gesetzt zwischen zwei Repliken, nicht in eine hinein:**

> "The first time I called you Mistress it was a courtesy with an edge on it. It was not true."
>
> He looked straight ahead at the back of the panel.
>
> **Beneath the linen at his throat there was a band of steel, and it had been there since the second house. It had made the word accurate from the first day, and it had never once needed him to mean it.**
>
> "It has been true for some time. I did not notice that either."

**Kein festgelegter Wortlaut ist geändert.** Der Block unter *Festgelegte Zeile:
die Heimfahrt* zitiert für die zweite Hälfte nur die Repliken; die Erzählung
dazwischen gehört nicht dazu. Trotzdem steht die Entscheidung hier, weil die
Passage als Ganzes geschützt ist und die Rhythmusänderung eine Entscheidung ist
und kein Handgriff.

**Warum es die Beichte nicht entwertet.** Die Unterscheidung, die der Absatz
trägt, ist die des Kapitels: das Wort war immer **zutreffend** und ist jetzt
**gemeint**. Das Halsband liefert die erste Hälfte und rührt die zweite nicht
an. *It had never once needed him to mean it* ist die kälteste verfügbare
Fassung davon und die einzige, die nicht nach Selbstmitleid klingt.

**Verworfen:** eine erste Fassung, die auf Annie zeigte (*Nobody in this house
had offered*). Sie machte aus einer Feststellung einen Vorwurf, richtete den
Absatz auf die falsche Person und gab Georgij eine Regung, die er nicht hat.

**Verworfen:** die Platzierung bei *one hand flat on the seat between them*
weiter oben. Dort wäre es Körperinventar neben anderem Körperinventar gewesen.
An der Beichte ist es das Scharnier.

**Offen bleiben Kapitel 14 und 15.**

---

### Februar ist die Frist, Januar ist das Fenster

**Entschieden am 22.08.** Der Absatz las sich als Plan zu warten und war als
Frist gemeint. Der Autor selbst hat ihn falsch herum gelesen, und das entscheidet
die Frage.

**Die Rechnung, die dahintersteht.** Das Essen mit Sang-hoon ist Tag 46, also
der 18. November. Er kauft die Routen in vier bis sechs Wochen, das ist Mitte
bis Ende Dezember, und danach ist er ein Quartal lang knapp. Ye-rin bricht an
einem Dienstagmorgen im Februar. **Dazwischen liegt Januar**, und das ist der
einzige Monat, in dem beides gleichzeitig wahr ist: er gebunden, sie noch
haltend.

Der Text nannte den Anfang und das Ende und liess die Mitte weg - also genau
das, worum es in der ganzen Rechnung geht. *"That is what I would work to"*
konnte beides heissen.

**Gesetzt in Fassung 12.4:**

> "Then it is February," said Annie. "Not March and not the spring."
>
> "February is when we lose her. It is not when we move." Georgij looked at the back of Mr Pyo's head. "He signs for the routes in December. For the quarter after that he is short of money and can do nothing about it, and she holds through January. Those two things are true at the same time for about four weeks."
>
> "January," said Annie.
>
> "That is what I would work to."

**Nebenwirkung, die beabsichtigt ist.** *"Georgij looked at the back of Mr Pyo's
head"* steht jetzt in einer Reihe mit zwei spaeteren Stellen: die Abtrennung
faehrt hinter demselben Kopf hoch, und danach sieht er *straight ahead at the
back of the panel*. Dieselbe Blickachse dreimal, einmal mit einem Menschen
darin und zweimal ohne.

**Der zweite Februar.** Kapitel 16 sagt *Pyeongtaek was February* und meint den
vergangenen. Kapitel 17 meint den kommenden. Getrennt werden sie jetzt durch
Dezember und Januar, die als Anker daneben stehen.

---

### Der Container hat einen Urheber, und der Text nennt ihn jetzt

**Entschieden am 22.08.** Kanon war es immer - `doc/03-cast.md` und
`doc/04-world.md`: **Sang-hoon** hat den ausgebauten Container in eine
Kim-Sendung geschoben und den Zoll darauf stossen lassen. Der Ausbau ist der
Beweis, nicht die Ladung, und der Container war leer.

**Im Text stand es nirgends.** Kapitel 11 gibt nur das Wort *container*.
Kapitel 17 setzte den Taeter voraus und lieferte ihn erst am Ende eines langen
Absatzes nach, als *the Republic of Korea is doing it for him*. Der Autor hat
beim Lesen gefragt, wer den Container dorthin gestellt hat, und ob es die Kims
selbst waren. Damit ist erwiesen, dass die Stelle es nicht getragen hat.

**Geaendert:** aus *"The container was not put into a Kim shipment to slow them
down"* wird *"Sang-hoon put the container into that shipment, and he did not do
it to slow them down."*

**Es bleibt eine Vermutung und keine Feststellung**, weil Annie zwei Zeilen
vorher *Say the guess* sagt. Die Grundlage liegt im selben Kapitel und im
vorigen: zwei gekaufte Konkurrenten im Februar und Maerz, dasselbe Muster bei
den Kims, und Sang-hoons eigener Satz an diesem Abend, dass Angst nie von dem
gekauft werden muss, der sie liefert.

**Unveraendert bleibt:** die Zollakte kommt nie als Szene vor, nur als Zeile.
Das steht so in `doc/07-next.md` und gilt weiter.

---

### Kapitel 17 heisst jetzt "I have never put it down"

**Entschieden am 22.08. vom Autor**, nachdem der alte Titel beim Lesen nicht
getragen hat.

**Warum *Who holds the paper* weg ist.** Er war Grundbuchsprache und sollte laut
`doc/01-craft.md` "auch fuer ihn" gelten - wer das Papier ueber Georgij haelt.
Diese zweite Bedeutung wird im Kapitel **nie aktiviert.** Im Text meint der Satz
ausschliesslich die drei Belastungen auf Hanas Land, also den Nebenstrang, und
er kommt aus Georgijs eigenem Mund ueber eine dritte Person. Das Ereignis des
Kapitels findet zwischen den beiden statt.

**Warum der neue traegt.** Die sechzehn anderen Titel sind ueberwiegend zitierte
Repliken aus fremdem Mund, und meist solche, die ihn bepreisen: *Merchandise
doesn't talk*, *What did she pay for you*, *You are better when you don't know*.
Annies Zeile gehoert in diese Reihe. Sie beantwortet sein Gestaendnis nicht,
sondern ueberbietet es:

> "In this one you put it down and did not notice you had put it down."
>
> Annie put two fingers on the back of the chair and left them there.
>
> "I have never put it down. Not one night." Her hand stayed where it was. "And this is my house."

**Er deckt beide Haelften.** Im Wagen legt Georgij die Waffe hin, ohne es zu
beschliessen. Im Korridor sagt sie, dass sie ihre nie hingelegt hat, in ihrem
eigenen Haus. Und seit derselben Fassung steht die Geste auf beiden Seiten
(siehe die festgelegte Zeile ueber die zwei Haende in `doc/05-continuity.md`).

**Er erfuellt die Titelregel.** Vor dem Kapitel klingt er nach Sturheit oder
nach einer Trotzhaltung. Danach ist er der einsamste Satz im Buch. Genau das
verlangt `doc/01-craft.md`: erst im Rueckblick aufgehen und vorher nicht
verraten, worum es geht.

**Verworfen:** *They were yours* (staerkster Satz, aber allein stehend
raetselhaft - der Leser weiss vor dem Kapitel nicht, was "they" ist),
*The cameras do not go to bed* (der klangvollste, benennt aber einen Zustand
des Hauses statt des Vorgangs zwischen den beiden), und den alten Titel zu
behalten und das Wortspiel einzuloesen (haette Georgij dazu gebracht, ueber
seinen eigenen Status nachzudenken, statt ihn festzustellen - das Buch tut das
nirgends).

---

### check.py teilt jetzt erst in Absaetze, dann in Saetze

**Geaendert am 22.08.**, beim Schreiben von Kapitel 18 aufgefallen.

**Der Fehlalarm.** Der Satzteiler trennte nur nach `.`, `!`, `?` und `"`. Eine
ganz kursive Zeile endet aber auf einem Stern, und der Text wurde am Stueck
geteilt. Also klebte jede solche Zeile am folgenden Absatz. In Kapitel 18 wurde
so ein Satz mit dreiundvierzig Woertern gemeldet, den es nicht gibt:

> *Later.*
>
> And on page nine, beside the two rumours from two mouths that had no reason to know each other:

**Betroffen war nicht nur diese Stelle.** Dieselbe Konstruktion steht in jeder
Datumszeile, in den vier Notizbuchzeilen in Kapitel 16 und ueberall dort, wo ein
kurzer kursiver Satz allein steht. Bisher ist es nie aufgefallen, weil zufaellig
nie ein langer Absatz dahinter stand.

**Die Aenderung:** erst an Leerzeilen in Absaetze zerlegen, dann innerhalb jedes
Absatzes in Saetze. Ein Satz laeuft nie ueber eine Leerzeile, auch nicht bei der
Fortsetzungskonvention in der Rede - dort endet der erste Absatz zwar ohne
schliessendes Anfuehrungszeichen, aber die Saetze darin enden normal.

**Gegenprobe in beide Richtungen gefahren**, nach der Regel aus `CLAUDE.md`:

- Alle achtzehn Kapitel: kein Satzlaengenfehler mehr. Uebrig bleiben nur die
  drei geduldeten Zahl-Konstanten in Kapitel 6 und 12.
- Ein absichtlich eingebauter Satz mit fuenfzig Woertern, **direkt hinter einer
  kursiven Zeile**, wird weiterhin gemeldet, und zwar mit fuenfzig und nicht mit
  einer aufgeblaehten Zahl.

**Und eine Panne, die hier steht, damit sie sich nicht wiederholt.** Der erste
Versuch wurde ueber ein Shell-Heredoc eingespielt, und das hat den Backslash vor
dem `n` verschluckt. Aus `r"
\s*
"` wurde ein echter Zeilenumbruch mitten im
Regex, und `check.py` liess sich fuer ein paar Minuten nicht mehr uebersetzen.
Aufgefallen, weil der Kontrolllauf danach **gar nichts** ausgab statt einer
Meldung - ein leeres Ergebnis ist kein gruenes Ergebnis. Wer Backslashes in
diese Datei bringt, baut sie mit `chr(92)` zusammen oder schreibt die Datei
direkt, statt sie durch eine Shell zu schicken.

---

### Wer wem was schuldet: die Rueckgabe ist keine Gefaelligkeit

**Entschieden am 22.08. vom Autor**, gegen die erste Fassung von Kapitel 18.

**Die erste Fassung hatte es falsch herum.** Dort las Georgij die vier
Bleistiftnotizen als Geschenk: *Sang-hoon had not owed him this... von einem
Mann, der nichts umsonst tut.* Das ignoriert das Konto. Georgij hat ihm in
Kapitel 16 vier Waende gegeben, dazu die Bestaetigung ueber die Kims, deren
Preis er im Raum laut genannt hat, und neunzehn Seiten, auf die ein Mann in
seiner Lage handeln kann. Dagegen stehen drei Woerter und eine Zahl.

**Sang-hoon steht weiter tief in der Schuld**, auch nach der Durchsicht. Die
Rueckgabe ist eine **Abschlagszahlung**, und die Uhrzeit gehoert dazu: Der Wagen
ist um halb acht in Yeouido losgefahren, damit die Seiten am Vormittag da sind.

> A man who owes a great deal and pays a little of it quickly is not a man
> clearing his debts. He is a man who intends to go on borrowing and would like
> the account to stay open.

**Was daraus folgt, ist besser als das Geschenk.** Es sagt, dass es einen
zweiten Abend geben wird, und das ist mehr wert als die Korrekturen. Und es
haelt Georgij kalt an einer Stelle, an der die erste Fassung ihn geruehrt hat.

---

### Das Scheingebot auf Hanseong

**Entschieden am 22.08. vom Autor**, und einmal korrigiert, weil die erste
Mechanik nicht funktionierte.

**Der Zweck.** Zur Wahrung des Scheins versucht Annie selbst, Hanseong zu
kaufen, damit der Verdacht bestaetigt wird, dass es ein lohnendes Ziel ist. Ein
Mann, der gebissen hat, prueft weiter, und das Einzige, was einen Mann am
Pruefen hindert, ist zuzusehen, wie jemand anders nach demselben Teller greift.

**Verworfen: das Gebot unter dem Vorbehalt eines Vorstandsbeschlusses.** Die
erste Fassung liess Annie so bieten und schloss daraus, Sang-hoon lerne daraus,
"ueber einen Beschluss hinwegzugehen, den es nicht geben wird". **Das geht
nicht.** Ohne wirksamen Beschluss ist eine Veraeusserung nichtig, und Sang-hoon
ist die vorsichtigste Figur des Buches. Ein Beschluss kann ihm nicht egal sein.

Ausserdem widersprach es Kapitel 17, wo der Weg laengst steht: *Half that board
wants out badly enough to sign anything, and will sign cheaply, and that is the
half he will sit down with.*

**Wie es wirklich laeuft.** Er braucht ueberhaupt keinen Beschluss, um
hineinzukommen. Er kauft die **Anteile der Haelfte, die raus will**, und Anteile
verkaufen die, denen sie gehoeren. Seite vierzehn ist nicht sein Hindernis,
sondern die **Falle danach**: Er haelt dann die Haelfte einer Firma, deren
Vorstand weiterhin nicht tagen kann, kann sich die Routen nicht uebertragen
lassen, kann nicht verkaufen, was er nicht will, und kann nichts davon aufloesen,
weil die Blockade, in die er hineingekauft hat, die Blockade ist. Genau das sagt
Kapitel 17 bereits.

**Die richtige Mechanik: Annie bietet fuer das Ganze.** Ein Gebot auf eine ganze
Firma wird von denen angenommen, denen sie gehoert, und die sitzen seit Maerz
nicht mehr zusammen in einem Raum. Ihre Anwaelte bauen es sorgfaeltig, ordentlich
und voellig korrekt, und es braucht beide Haelften auf einem Blatt Papier. Sie
bekommen es nicht einmal in derselben Woche zu sehen.

**Was Sang-hoon daraus lernt, ist nicht Kuehnheit, sondern dass die Vordertuer
zu ist.** Ein ernsthafter Kaeufer ist mit Geld hingegangen und wieder abgezogen,
aus einem Grund, ueber den er selbst schon zweimal gelesen hat. Wer das sieht,
sucht keinen dritten Weg mehr. **Er hoert auf zu suchen und hoert auf, Leute zu
fragen**, und Leute fragen ist die einzige Art, wie jemand herausfindet, was
Georgij tut.

**Das Restrisiko** steht im Text und liegt Annie vor, bevor sie zustimmt: Wenn
die beiden Haelften sich doch einigen, kauft sie eine Reederei ohne
arbeitsfaehigen Vorstand. Gegenmittel ist eine **Obergrenze** im Gebot, niedrig
genug zum Abgelehntwerden und hoch genug zum Geglaubtwerden. (In der ersten
Fassung stand dort "floor", also eine Untergrenze, und das war das Gegenteil des
Gemeinten.) Georgij baut sie **mit** ihren Leuten und nicht fuer sie.

---

### Woos Preis ist Ladung, nicht Geld und nicht ein Name

**Entschieden am 22.08. vom Autor**, gegen die erste Fassung, in der Woo fuer
den Namen des Terminal-Interessenten und einen Rueckkauf der Hongkong-Anteile
zusagte. **Das war zu billig fuer das, worum er gebeten wird.**

**Was nur Annie hat:** Ladung. Ein Terminal ist nicht wert, was der Beton
gekostet hat, sondern was woechentlich und fahrplanmaessig darueber geht. Ihre
Spezialchemie laeuft seit elf Jahren nach Fahrplan ueber irgendeinen Hafen.

**Der Handel:** zehn Jahre, Mindestmengen, mit einer Zahl darin, die etwas
bedeutet. Es kostet sie echtes Geld, wenn Georgij den Durchsatz falsch
geschaetzt hat, und genau das macht es zu einem Preis und nicht zu einer Geste.

**Es loest den Dienstag von selbst.** Ein Terminal mit zehn Jahren kontrahierter
Menge zerlegen drei Erben nicht, sie betreiben es, weil es laufend mehr
abwirft als zerschlagen. Sang-hoon bekommt hoechstens ein Drittel an einem
Geschaeft unter einem Vertrag, den er nicht aendern kann und nicht geschrieben
hat. Niemand muss ihn auskaufen, weil dort nichts mehr zu wollen ist.

**Der Name kommt obendrauf und ungefragt**, damit Woo wieder in der Schuld
steht. Genauer: Georgij hat den Namen nicht und wird nicht so tun, als haette
er ihn. Was er mitnimmt, ist die Kontonummer der Firma in Jung-gu und die drei
Daten von der Innenseite des Aktendeckels aus Kapitel 13. Das ist die Form der
Tuer, durch die der Name geht.

**Annie gibt den Auftrag dazu selbst**, und ihre Begruendung ist keine
Grosszuegigkeit: *a man who is enjoying himself gives away the wrong things by
accident, and I would rather you gave away the right one on purpose.*

---

### Block H, der Garten, ist gestrichen

**Entschieden am 22.08. vom Autor.** Begruendung: Der Block stammt unveraendert
aus der Vorlage, ist improvisierter als der Rest, und die Versoehnung, die er
dort tragen sollte, gehoert einer Annie, die es in diesem Buch nicht gibt.

**Was der Schluss dadurch gewinnt.** Er steht jetzt auf drei Schlaegen statt auf
vier: **Bruch, Mauer, Bruecke.** Dazwischen liegt keine Verhandlungsszene mehr,
in der zwei Leute in einem Garten aushandeln, was gerade passiert ist. Er bricht,
er geht sichtbar, sie setzt sich auf den Beton. Die Versoehnung findet
ausschliesslich dort statt.

**Was mit dem Block wegfaellt, damit es nicht unbemerkt verschwindet:**

- *"Mein Vater haette dich dafuer auspeitschen lassen." / "Tu Dir keinen Zwang an."*
- Die Zigarette, die sie ihm wegnimmt. Damit faellt auch die Herkunftsschuld weg,
  die Punkt 19 oben verzeichnet hat - Georgij raucht in siebzehn Kapiteln nicht
  und besitzt nichts.
- Die Clubkarte, fuer die er keine Verwendung hat.
- Ihr Angebot, das Halsband in den Safe zu legen, und seine Ablehnung.
- Sein Gegenvorschlag: er erledigt die Sache und die Route, danach laesst sie ihn
  frei.
- Ihre Erkenntnis, dass er nicht bitten kann, ohne im selben Atemzug seine eigene
  Zerstoerung anzubieten.

**Und die Zeile, die als "ihre beste im ganzen Material" verzeichnet war:**

> "Ich habe dich gekauft, weil du das Einzige in dieser Stadt bist, das nicht kaputtgeht, wenn ich darauf druecke."

**Sie ist kein Verlust, sondern eine Doppelung.** Block J hat denselben Gedanken
als Eingestaendnis statt als Kompliment: *"Ich wollte sehen, ob du zerbrechen
wuerdest."* Die J-Fassung ist die bessere, weil sie beschreibt, was sie getan
hat, und nicht, was er ist. Zwei Saetze fuer dieselbe Sache haetten einander
entwertet.

**Was ausdruecklich NICHT nachgeholt wird**, solange niemand es verlangt: Georgij
bittet nirgends darum, freigelassen zu werden. Der Gegenvorschlag aus Block H war
die einzige Stelle, an der er es getan haette. Ein Mann, der um seine Freiheit
bittet, hat einen Preis fuer sich genannt, und das ist genau das, was diese Figur
nicht tut.

---

### Die Frage nach der Veraeusserung steht NICHT im Bericht

**Entschieden am 22.08. vom Autor.** Sang-hoon soll aus Georgijs neunzehn Seiten
nur erfahren, welche Vorstandshaelfte verkaufen will. Die Frage, ob ein Vorstand,
der nicht mehr tagt, eine Veraeusserung genehmigen kann, bringt er selbst mit.

**Warum das besser ist.** Ein Dokument, das einem Fremden den genauen Mechanismus
seines eigenen Ruins mitliefert, riecht. Sang-hoon ist die vorsichtigste Figur
des Buches, und er wuerde es riechen. So gibt Georgij ihm nichts in die Hand.

**Und es dreht die Information um.** Wenn die Frage nicht auf dem Papier steht,
dann hat Sang-hoon sie mitten in einem Gespraech ueber eine Decke aus eigenem
Antrieb gestellt - und damit verraten, dass er nicht mehr prueft, sondern
rechnet. Georgijs Satz dazu in Kapitel 18: *"A man who is still deciding does not
ask what will be in his way afterwards."*

**Drei Stellen mussten nachgezogen werden**, und die dritte hat erst die
Gegenprobe ueber alle aktuellen Fassungen gefunden:

- **Kapitel 17** (v12.6): aus *"which is page fourteen"* wird *"and that is not in
  the document anywhere. He brought it with him."*
- **Kapitel 18** (v2.2): oben liegt jetzt **Seite sechzehn**, die Seite ueber den
  im Maerz gespaltenen Vorstand und darueber, welche Haelfte aufgehoert hat zu
  kommen. Die vierte Bleistiftnotiz steht dort und lautet **"Which."** - ein Mann,
  der seinen Vertragspartner auswaehlt. *"Later."* faellt weg.
- **Kapitel 16** (v1.14): die Notizbuchzeile im Wagen sagte *"Disposal by a board
  that has stopped meeting, page fourteen."* Jetzt: *"...which is nowhere in the
  pages."*

**Die Falle bleibt unveraendert und wird sogar sauberer.** Sie war nie, dass er
den Hinweis uebersieht. Sie ist, dass er ihn kennt und fuer Papierkram haelt.
Woos Satz aus Kapitel 13 traegt sie weiter: einmal entschieden, dass jemand die
Muehe wert ist, ist der Rest Papierkram.

---

### Die Falle ist eine Auseinandersetzung und ein Kalender, kein Stillstand

**Korrigiert am 22.08.**, auf den Einwand des Autors: Wenn Sang-hoon weiss, dass
der Vorstand zerstritten ist, warum kauft er dann ueberhaupt?

**Weil er es kann, und weil er recht hat.** Er kauft die Haelfte, die raus will,
billig und schnell, und nimmt danach die andere Haelfte einzeln auseinander. Genau
das hat er in Pyeongtaek getan, im Februar gekauft und im Maerz die Direktoren
einzeln nach Busan bestellt, und darin ist er besser als sonst jemand. **Es
funktioniert.** Hanseong ist ein gutes Ziel und seine Einschaetzung stimmt.

**Es kostet ihn nur ein Quartal**, und dieses Quartal ist das ganze Spiel.

**Kapitel 14 hatte es von Anfang an richtig**, und die spaeteren Kapitel sind
davon abgedriftet:

> "He cannot move quickly and buy four routes in the same quarter, and he will buy the routes, because he cannot help it."
>
> "And on the day he needs to be liquid enough to take a logistics company off a family under customs investigation, **he will be a man with four routes and a fight**."

Eine **Auseinandersetzung**, kein Stillstand. Meine Fassungen in Kapitel 17
(*"a company that cannot authorise anything afterwards"*) und Kapitel 18 (*"he
cannot have the routes assigned to him, he cannot sell what he does not want, he
cannot resolve any of it"*) haben daraus eine Sackgasse gemacht, und eine
Sackgasse haette er gesehen. Er ist die vorsichtigste Figur des Buches.

**Warum er das Quartal trotzdem ausgibt.** Er glaubt, er hat es. Er sagt es in
Kapitel 16 selbst: *"With a family? Two years. Eighteen months if somebody
frightens them for me."* Was er nicht weiss, ist, dass Woos Name neben dem der
Kims plus Annies Geld der Angst in vierzehn Tagen den Anlass nimmt.

**Damit ist niemand dumm**, und das Gift ist genau das aus Kapitel 14: *ein
Dokument, in dem jedes Wort wahr ist, an dem er sich ruiniert.* Nicht weil das
Ziel schlecht waere, sondern weil ein gutes Geschaeft zum falschen Zeitpunkt
Ruin ist.

**Geaendert:**

- **Kapitel 17** (v12.7): *"Then he is bound. He will have paid for four routes
  and bought a fight with the half that would not sit in a room. He will win it.
  He took Pyeongtaek apart one director at a time... It will take him a quarter,
  and he thinks he has a quarter, because he told me on Tuesday that a family
  takes two years."*
- **Kapitel 18** (v2.3): Der ganze Austausch ueber die Falle neu. Kernzeilen:
  *"So it works." / "It works. That is the part I need you to hold on to... I am
  not selling him a bad company. Hanseong is worth having and he is right about
  it." / "Then where is the difficulty." / "In the calendar. Nowhere else."* Und
  Annies Schlusssatz dazu: *"He is spending a quarter he believes he has."*

**Merke fuer alles Weitere:** Sang-hoon irrt sich nirgends in dem, was er sehen
kann. Wo eine Szene ihn dumm aussehen laesst, ist die Szene falsch.

---

### Ye-rin wird im Dezember angesprochen, nicht im Januar

**Korrigiert am 22.08.**, auf den Einwand des Autors: Warten um des Wartens
willen ergibt keinen Sinn, wenn alles vorbereitet ist.

**Warum Januar ueberhaupt dastand.** Ich hatte vier Vorbedingungen fuer den einen
Versuch notiert, darunter *"Woos Name steht oeffentlich neben ihrem und die
Kuendigungen haben aufgehoert."* Diese Bedingung ist am selben Tag gestrichen
worden - die Reporter kommen jetzt **nach** ihrer Zusage, und sie haelt den
Ausloeser. Ich habe die Liste danach nicht neu gerechnet und den Termin
verteidigt, weil er aufgeschrieben war.

**Neu gerechnet bleibt eine einzige echte Vorbedingung: Sang-hoon muss gebunden
sein.** Das ist er in der ersten Dezemberwoche.

**Drei Gruende, nicht zu warten:**

- Warten kostet die Familie drei Kuendigungen pro Woche und bringt den Neffen mit
  vier Prozent naeher an seinen Anruf. Der eine Schuss faellt dann auf eine Frau,
  die schon dabei ist, die Kontrolle zu verlieren.
- Kapitel 18 sagt es selbst: *"It is three weeks, and they are the three weeks
  over the New Year, when nobody in this country signs anything."* Der Januar ist
  der schlechteste Teil des Fensters, nicht der beste.
- **Und der eigentliche Gewinn: Woo ist an diesem Abend im Haus.** Sie muss
  Georgij nicht glauben. Sie kann in den Nebenraum gehen und einen Mann mit
  einundfuenfzig Jahren fragen, ob es echt ist. Das ist der bestmoegliche Beweis,
  und es gibt ihn genau einmal, weil Woo aus seinen eigenen Gruenden ohnehin da
  ist.

**Die Feier bei Hana**, Mitte Dezember, loest damit alles auf einmal:

- Woos Bedingung woertlich - *"a room with that family in it and somebody who can
  actually sign"*. Der Bruder hat den Titel, und in einem Nebenzimmer machen die
  beiden ihr gewoehnliches Papier. **Deshalb ein Haus und kein Hotel:** Der Anlass
  traegt das Nebenzimmer.
- **Woo findet Ye-rin selbst.** Er hat gesagt *"not the ones who talk"*, und auf
  einer Feier ist die, die nicht redet, genau die, die er sucht. Hinterher sagt er
  Georgij, dass er sie gefunden hat.
- Hanas Einfuehrung, die `doc/04-world.md` als *"eine Einfuehrung, keine
  Erlaubnis"* fuehrt.
- Und das eine Gespraech, an diesem Abend, allein, in einem Zimmer.

**Die Kette steht damit so:**

| Wann | Was |
|---|---|
| Ende November | Annies Scheingebot scheitert sichtbar |
| kurz darauf | Sang-hoon auf dem Anwesen. **Der Bruch.** Er geht am selben Tag |
| danach | die Bruecke |
| Anfang Dezember | Sang-hoon kauft und ist gebunden |
| **Mitte Dezember** | **Die Feier bei Hana. Ye-rin, allein, an diesem Abend** |
| danach | die sechs unterschreiben, dann gruenes Licht fuer Reporter |

**Er geht also wenige Tage nach dem Bruch in das wichtigste Gespraech des
Buches** - als ein Mann, dem gerade vor einem Zeugen vorgefuehrt wurde, dass seine
Stellung ausschliesslich vom Wohlwollen einer anderen abhaengt. Und bittet eine
Frau, ihre unbeschriebene Macht aufschreiben zu lassen.

---

### Annie geht auf Woos Satz mit keinem Wort ein

**Entschieden am 22.08.** In Kapitel 20 berichtet Georgij, was Woo ueber das
Vetorecht gesagt hat. Annie erwidert **nichts**. Keine Bestaetigung, kein
Widerspruch, kein *"Was dachtest Du denn, was ich kaufe?"*

Das macht sie groesser und laesst ihn ratlos: Weiss sie es? Ist es ihr gleich?
Hat er gerade einen Fehler gemacht? Er bekommt keine Antwort und wird auch keine
bekommen.

**Sie stellt stattdessen genau eine Frage, und die ist nicht ueber die Sache,
sondern ueber ihn:** *"Und was hast Du gesagt?"*

Er hat *"Yes"* gesagt. Er hat einem Fremden gegenueber bestaetigt, dass die
Kritik an ihrem Plan zutrifft. **Das ist das erste, was er je getan hat, das
nicht fuer sie war.** Sie bestraft es nicht. Sie legt es ab.

**Und das ist der Zuender.** Wochen spaeter fragt Sang-hoon in ihrem Haus, was
Georgij kostet, und sie weiss seit diesem Freitag, dass er ueber sie schon einmal
mit jemand anderem einer Meinung war.

**Seine Eroeffnung steht fest** und stammt vom Autor:

> "Mistress, I am sorry. I could not do what you said. I came back with a favour."

Er zahlt den Preis zuerst und liefert den Inhalt danach, unaufgefordert, fuer
eine Anweisung, die er nicht einhalten konnte. Und *I came back with a favour*
ist woertlich wahr: Er traegt ihn herein.

---

## Der Schluss von Band 1, entschieden am 23.08.

**Der Geschaeftsstrang ist mit Kapitel 33 gewonnen und laeuft nur noch ab.** Das
wurde beim Planen von Kapitel 34 gegen jeden offenen Faden einzeln geprueft, mit
einer Frage: kann das noch schiefgehen? Vollmacht, Mietvorvertrag, Sang-hoon, Woos
sieben Jahre - nein. Zollakte, Choi Dae-ho, Los elf, die Pipeline - Faeden ohne
Zaehne. Uebrig blieb genau eine Sache, die scheitern kann, und sie ist die
Titelzeile: was Georgij will.

**Verworfen: ein Jahreswechsel-Kapitel als Coda.** Es waere das Kapitel gewesen, in
dem sich alles von allein fuegt, also eines ohne Frage. Die leeren Wochen bleiben
drin, aber als erster Abschnitt von Kapitel 34 und als Druck, nicht als Ruhe.

**Der Eintrag wird gestrichen und das Halsband bleibt.** Die Alternative war, dass
Georgij die Loeschung ganz ablehnt. Sie ist schwaecher: dann aendert sich nichts,
und der Titel bleibt unbezahlt. Kapitel 24 hat den Ausgang ausserdem selbst gelegt.
Annie sagt dort *"until that is dealt with, taking it off you would be the most
dangerous thing anybody has ever done to you"*, und Georgijs Gegenrede auf der
Bruecke ist **rein taktisch** - Marktwert, Aufwand, ein Mann ohne Zeichen ist Ware.
Wird der Eintrag erledigt, faellt seine ganze Begruendung mit, und was uebrig
bleibt, ist der Grund, den er sich auf der Bruecke ausgesucht hatte nicht zu geben.
**Annie tut es in genau dieser Reihenfolge und sagt, dass sie es tut.**

**Der zurueckgehaltene Grund ist dieselbe Rechnung wie auf der Bruecke, nur zeigt
sie auf sie.** Wer ihr gehoert, muss verkauft werden: Preis, Raum, Zeugen, Wochen,
und um den neunten Morgen herum will man vielleicht nicht mehr. Wer frei ist, wird
an einem Dienstag im Flur zwischen zwei anderen Dingen weggeschickt. Er hat keine
Angst vor dem Markt, er hat Angst davor, wie billig sie es sich ueberlegen kann.
Das ist eine Anklage, die er nicht als eine meint, und Annie hoert sie als eine.

**Die Anrede bleibt, und das ist die zweite Weigerung.** Ueber das Halsband kann
man taktisch streiten, ueber das Wort nicht. Es kostet nichts, es fallen zu lassen,
und niemand kann es erzwingen, seit es kein Papier mehr gibt. Damit schliesst sich
der Bogen aus Kapitel 23, wo er es ihr entzogen hat.

**Was fuer Band 2 aufgehoben wird:** Los elf und der Name des Garanten, Choi
Dae-ho, die Pipeline, und Ye-rin, die von selbst zurueckkommt, sobald das Vetorecht
beisst. Nichts davon wird in 34 angefasst.

---

## Kapitel 34 im Einzelnen, entschieden am 23.08.

**Die leeren Wochen sind ein Befehl und keine Leere.** Erste Fassung liess
Georgij zehn Wochen lang untaetig sein, weil nichts anlag. Das ist unglaubwuerdig:
Ein Mann, dessen Arbeit das Arrangieren ist, sucht sich andere Ziele. **Annie
untersagt es ihm am 2. Januar, in einem Satz, und nennt keinen Grund.**

**Warum sie keinen nennt.** Sie haelt Gruende zurueck, das ist ihre Methode seit
Kapitel 4 - *"I'd rather find out what you bring me when nobody has told you what
to want."* Ein genannter Grund haette ihn rechnen lassen, und dann haette er im
Maerz eine Antwort gehabt. Sie sagt es ihm erst am 1. Maerz, und dann vollstaendig.

**Der Grund selbst ist geschaeftlich**, wie bei ihr immer: Jeder gewonnene Raum
legt etwas auf Sang-hoons Zahl, und sie wollte nicht viermal in dem Gebaeude sein,
waehrend er teurer wird. Verschwiegen hat sie es, weil er die Differenz bepreist
und einen Weg gefunden haette, nuetzlich zu sein, den sie von dort nicht sieht.

**Sein Irrtum ist der dritte und der laengste.** Er haelt es fuer Strukturschutz.
Das ist kompetent und falsch, und im November hat er sich in derselben Frau
zweimal in vier Tagen geirrt. Dieser dauert zehn Wochen.

**Die Vollmacht wird genau einmal benutzt, und belanglos.** Verworfen wurde,
sie gar nicht zu benutzen (dann fragt der Leser, wozu sie da war) und sie etwas
anrichten zu lassen, das in Band 2 zurueckkommt. Eine Fristverlaengerung, vier
Minuten, weil er der Einzige im Haus mit Zeichnungsbefugnis war, ist die bessere
Pointe: Ein Recht, das man sich als Bezahlung fuer einen Bruch geben laesst, wird
fuer Verwaltung verbraucht.

**Und die Vorhersage dazu ist eingeloest.** Auf der Bruecke sagt er vier Raeume
bis Februar voraus und zwei Unterschriften darin. Es wurden vier Raeume und keine
Zeile. Er hat die Welt richtig gerechnet und sich selbst falsch, und er rechnet es
Mr Chae vor, weil das kaelter ist, als es ihr zu sagen.

**Er argumentiert nicht mehr im Praesens gegen einen Zustand, den es nicht mehr
gibt.** Eine Fassung liess ihn sagen *"you have to sell me"*, vier Minuten nachdem
sie das abgeschafft hatte. Jetzt steht die erste Haelfte im Konditional und mit
ihrem Datum, und Annie benennt, was er beschreibt: *"You are describing being
free."* Er gibt es zu. **Seine Weigerung ist zugegeben unvernuenftig, nicht
unlogisch**, und das ist der Unterschied, an dem die Szene haengt.

**Das Halsband ist ab jetzt ein Zeichen ohne Deckung, und er sagt es.** Damit
waechst ihm ein taktischer Grund zurueck, und Annie bietet ihn ihm an. **Er nimmt
ihn nicht** - *"It would hold." He did not take it. "It is not why."* Er versteckt
sich nicht hinter einem verfuegbaren wahren Grund, und das ist dieselbe Bewegung
wie in Kapitel 33, eine Stufe teurer.

**Papiere und Konto: unveraendert.** Das Register ist das private Buch eines
Auktionshauses. Eine gestrichene Zeile darin erzeugt keine Staatsangehoerigkeit
und kein Konto. Papiere gibt es seit Oktober, weil ihre Compliance sie brauchte.
**Regel 2 gilt am 1. Maerz unveraendert.**



---

## Kontinuitaetsdurchgang Band 2, entschieden am 24.08.

Drei Durchgaenge ueber alle 42 Kapitel von Band 2: Zahlen und Zeitachse,
Wissens- und Zusagenkette, Punkt oder Fragezeichen. Was dabei entschieden wurde:

**Woo ist achtundsiebzig, und er ist mit siebenundzwanzig eingestiegen.** Band 2,
Kapitel 13 liess ihn zweimal *"I am seventy-five"* sagen. Band 1 sagt viermal
achtundsiebzig, einmal aus seinem eigenen Mund (*"I am not starting at
seventy-eight"*), und vielfach *"fifty-one years"* im Gewerbe. Der aeltere und
haeufigere Text gewinnt. **Die Gegenprobe war der eigentliche Fund:** wer nur das
Alter hochsetzt, erzeugt aus *"since I was twenty-four"* vierundfuenfzig Jahre
und zerschiesst die einundfuenfzig, die quer durch Band 1 stehen. Also ist der
Einstieg mitgegangen: siebenundzwanzig.

**Dienstzeiten sind auf die haeufigere Zahl gezogen.** Byun sechsundzwanzig Jahre
(viermal gegen einmal zweiundzwanzig), Jang dreissig Jahre (dreimal gegen zweimal
zweiundzwanzig - die zweiundzwanzig gehoeren Mr Noh und sind vermutlich von dort
herueber), Mrs Seo neun Jahre (Band 1 und Annies eigener Mund gegen zweimal elf
in Kapitel 24).

**Die vierte Gebuehr wurde am Abend bezahlt und nicht vier Jahre spaeter.** Byun
und Yeom sagen es beide so, und Kapitel 22 zaehlt sie unter *"two others going
back four years"*. Kapitel 29 und 33 hatten daraus *"last year"* und *"four years
late"* gemacht, und Kapitel 29 stuetzte darauf die ganze Ueberzeugung von
Mrs Jeon. Die Argumentation laeuft jetzt ueber das, was ohnehin die staerkere
Fassung war und in Kapitel 27 schon steht: **eine Abwesenheit im Buch ist eine
Frage, eine Zahlung ist ein Dienstag.**

**Kapitel 34 weiss das Grundstueck noch nicht.** Es kam aus Annies Auftrag und
wird erst in Kapitel 36 geliefert. Kapitel 34 nennt jetzt, was er am 4. Juni
wirklich hat: zwei Adressen und einen Arzt, der ueber eine Losnummer bezahlt
wurde.

**Annie hebt ihr eigenes Verbot ausdruecklich auf.** Das Verbot aus Kapitel 34
(*"Not the florist and not the addresses"*) wurde in Kapitel 36 gebrochen, ohne
dass jemand es bemerkte - bei einem Mann, der jede solche Entscheidung
mitspricht, und einen Tag nach einer Szene, die ihn beim Einhalten zeigt. Statt
den Bruch zu erzaehlen, hebt sie ihn am Montagabend auf, und zwar nur zur
Haelfte: die Blumenfrau bleibt geschuetzt.

**Annies Auskunft ueber das Essen geht nicht an einen Koch.** In Kapitel 39 gab
Georgij Mr Baek die ganze Regel, um zu erklaeren, warum die Frage zaehlt. Das ist
nach dem 29. Mai, faellt also unter seine eigene Zusage. Er sagt jetzt, dass er
es nicht erklaeren wird; die Folgerung steht im Erzaehltext.

**Vier Bitten bekommen ihr Fragezeichen.** *Will you give me his name?* (18),
*Will you give me the two names?* (10), *Who told you?* (25), *Have you ever
watched him eat?* (26). Die Probe ist in allen vier Faellen im Text beantwortet:
der andere sagt nein. Die Marke gehoert dem, der den Zug abgibt, auch wenn die
Zeile kalt ist. Der Gegenbeleg stand im selben Buch - *"Did you meet him?"* in
Kapitel 1 ist dieselbe Bitte an dieselbe Frau mit demselben Ausgang und hatte das
Zeichen. Dazu **"What do you want?"** aus Byuns Mund in Kapitel 22, der an dieser
Stelle nichts mehr fordert.

**Das Komma-Mittel wird wieder eingehegt.** *"Is there anything I should do,"
said Mr Ok.*, *"When," said Georgij.* und *"What did the fund tell you," said
Georgij.* sind keine Abfertigungen, sondern genau der Fall, fuer den die Regel
das Zeichen vorsieht. Sie haben es bekommen. Der Rest der Form bleibt bei denen,
die den Zug haben. **Stand danach: rund zehn Vorkommen in Band 2. Das ist die
Obergrenze, nicht der Anfang einer Gewohnheit.**


---

## Byun geht Ende Februar, entschieden am 24.08.

Der Widerspruch: Band 1, Kapitel 34 sagt, Annies Kauf lief vom 4. Januar bis zum
19. Februar, und Kapitel 22 laesst Byun ihre vier Besuche aus erster Hand
erinnern - *"she was the only one of them who frightened me"*. Gleichzeitig stand
dreimal im Text, er habe das Haus im November verlassen.

**Gewaehlt wurde das Datum, nicht die Szene.** Die Erinnerung ist zu gut, um sie
jemand anderem zu geben, und Band 1 ist Kanon. Also ist der November gefallen.

**Was der Tausch einbringt.** Aus einer Reparatur wird eine Schaerfung: Byun hat
die letzte Loeschung verkauft, **nachdem** Hwang die Praxis abgestellt hatte, im
selben Haus, in dem Hwang seit Oktober sass. Hwangs *"This house has not sold a
deletion since the eleventh of December"* war der Satz, an dem der Widerspruch
haftete - er steht so in keiner Fassung mehr; jetzt sagt er stattdessen, dass sie danach noch einmal verkauft wurde,
und er sagt es unaufgefordert. Der Mann, dessen Wert seine Genauigkeit ist,
liefert die eigene Luecke mit, und Georgij muss sie ihm nicht abringen.

**Nicht geaendert:** Yeoms Bericht in Kapitel 25, Byun sei im Februar des
Vorjahres zu ihm gekommen und habe von *einer* Gebuehr gesprochen. Das ist ein
frueheres Gestaendnis ueber einen aelteren Vorgang und bleibt richtig.

---

## Eine Lesefassung je Band, entschieden am 24.08.

`book.md` hatte sechsundsiebzig Kapitel und beide Baende in einer Datei. Geteilt
in `book-band-1.md` und `book-band-2.md`, erzeugt von `build.py` wie vorher.
Mitgezogen: `CLAUDE.md`, `README.md`, `chapters-2/README.md` und die Liste der
erzeugten Dateien in `.github/workflows/build.yml` - **letzteres ist die Stelle,
die es sonst still zerlegt haette**, weil der Workflow nur zurueckschreibt, was
namentlich in dieser Liste steht.


---

## Zwei Trenner, entschieden am 24.08.

Die Quelldateien hatten einen Trenner fuer zwei verschiedene Dinge. In Band 2
steht `---` alle fuenfeinhalb Zeilen; das ist ein **Takt** zwischen zwei
Bloecken. Zweimal im Kapitel ist derselbe Strich aber eine **Szenengrenze**.
Markdown kennt den Unterschied nicht und hat aus beidem eine Trennlinie
gemacht: 2450 Stueck in der Lesefassung von Band 2.

**Ab jetzt:**

- `---` ist der Takt. In `book-band-N.md` faellt er weg, die Absatzleerzeile
  traegt ihn. In `read/` bleibt er das zentrierte Ornament, in `paste/` wird er
  wie bisher zu `* * *`.
- `* * *` ist die Szenengrenze. In `book-band-N.md` und in `read/` ist er ein
  Strich, in `paste/` ein langer Gedankenstrich.

**Gesetzt sind sie nach den Szenenbeschreibungen in diesem Dokument**, nicht
nach Gefuehl: `doc/05-continuity.md` sagt je Kapitel, aus wie vielen Szenen es
besteht und welche das sind. Band 2 hat danach **zweiunddreissig** Grenzen in
vierundvierzig Kapiteln. Ein Automatismus wurde versucht und verworfen - er
traf vier von vierundvierzig Kapiteln richtig.

**Offen:** Band 1 hat noch keine Szenengrenzen. Dieselbe Arbeit, vierunddreissig
Kapitel, dieselbe Quelle.

**Und die Probe, die dazugehoert:** Die Zahl der `* * *` in einem Kapitel muss
der Szenenzahl aus diesem Dokument minus eins entsprechen. Das laesst sich
maschinell pruefen und tut es noch nicht.


---

## Georgij hoert im Endspurt auf, Fehler zu machen, entschieden am 25.08.

**Anlass war eine Frage des Autors:** ob Georgij weiterhin inkompetent ist oder
kompetenter wird. Nachgesehen, Kapitel fuer Kapitel:

**Bis Kapitel 73 wird er fuenfmal hintereinander korrigiert.** Annie diagnostiziert
ihn in 69. Mr Ahn liest in 70 den Satz richtig, an dem er vierzehn Tage
gescheitert ist. Mrs Jeon sagt ihm in 71, was er getan hat. In 72 schreibt er drei
Erwartungen auf und hat zwei falsch. In 73 dreht Mr Ahn seine und Sims Lesart um.

**Kapitel 73 ist die letzte Stelle, an der jemand eine Deutung von ihm
umstoesst.** Ab 74 kommen die Korrekturen von ihm selbst: die zweite Frau in 74,
Mr Pyeon in 76 (*"He is right and we are wrong"*), die harte Fassung fuer Mr Ahn
und die haltende Lesart gegen Sim in 77, der vorgelegte Briefweg und die drei
Zahlen in 78, die einzige Tuer und der eigene Interessenkonflikt in 80.

**Entscheidung des Autors:** das bleibt so, und es darf so bleiben. *"Wir sind im
Endspurt, es ist ok wenn er langsam aufhoert Fehler zu machen."*

**Woraus zwei Regeln fuer den Rest des Bandes folgen:**

1. **Niemand baut ihm rueckwirkend neue Fehler ein**, um die Kurve zu
   verflachen. Wer ab 74 eine Stelle findet, an der er zu gut aussieht, laesst
   sie stehen.
2. **Die Kurve laeuft aber nicht auf Unfehlbarkeit zu, sondern durch die
   Kompetenz hindurch.** Das steht schon in Kapitel 80: die Methode bei Sim hat
   funktioniert, weil er nichts von der Form des Satzes hatte, und bei Mr Hwang
   hat er alles davon. **Die Gefahr im Endspurt ist nicht mehr, dass er etwas
   falsch liest, sondern dass er es richtig liest und benutzt.** Das ist
   dieselbe Regel, die er in 80 selbst ausspricht: jemand wird gemacht, indem
   man ihm im falschen Moment einen guten Grund gibt.

**Und die eine Fehlerklasse, die bleiben muss:** er darf sich weiterhin ueber
sich selbst irren. Ueber Sachverhalte nicht mehr, ueber die eigene Lage schon.
In 74 haelt er sich vier Tage lang faelschlich fuer die Ursache von November,
und Annie widerlegt ihn mit einem Datum. **Diese Sorte darf bis zum letzten
Kapitel vorkommen**, weil sie nichts mit Koennen zu tun hat.

## Weg C: Kapitel 62 gibt die Form und nicht den Namen (26.08.)

**Entschieden vom Autor**, nachdem beim Kuerzen ein Widerspruch aufgefallen war:
Kapitel 62 liess Georgij am selben Abend erzaehlen, was 74, 75 und 78 als
sechsundzwanzig Tage Schweigen behandeln. Gewaehlt wurde Weg C von dreien -
nicht streichen, sondern **die Auskunft um eine Frage verschieben**.

**Drei Regeln daraus:**

1. **Annie weiss ab dem 23. August die Form und nicht den Namen.** Sie kann ihn
   sich denken, und sie fragt nicht. Wer spaeter eine Szene zwischen dem
   23. August und dem 18. September schreibt, schreibt eine Frau, die es
   ausrechnen koennte und es laesst.
2. **Woos Besuch ist Sonntag, der 23. August, und die Frist ist
   sechsundzwanzig Tage.** Der Fliesstext sagte viermal den 24. und neunmal
   fuenfundzwanzig; die Kopfzeile und `doc/13` hatten recht.
3. **Der Name, die Dreiteilung und das Mittagessen gehoeren in 61 und 75 und
   nirgendwo sonst.**

## Das Heft wird benutzt und nicht nur gefuehrt (26.08.)

**Vom Autor:** *"Wir suchen hier nach einem Mann, der nichts hinterlaesst, und
diese Spuren zusammenzufassen ist legitim. Es fasst es fuer den Leser zusammen.
Diese Notizen sollten aber irgendwann verwendet werden fuer die Detektivarbeit."*

**Damit ist die Bilanz nicht der Fehler, die Einseitigkeit ist es.** Gemessen
am 26.08.: 167 Ablagen, 13 Entnahmen. Dreiunddreissig Kapitel legen etwas ab,
das nie wieder geholt wird.

**Die Regel fuer alles Weitere:** jede neue Ablage braucht eine spaetere
Entnahme. Wer eine schreibt, notiert wo. `werkzeug/heft.py` misst das
Verhaeltnis, und es ist ab jetzt eine Zahl, die man nennen kann.

## Choi ueberlebt das Ende nicht, und Georgij hat ihn trotzdem nicht gehabt (26.08.)

**Vom Autor:** *"sorgen wir noch dafuer, dass alle wissen, dass Choi das Ende
NICHT ueberleben kann. Er hat zu viele maechtige Leute manipuliert. Er soll
nicht erfahren, wer davon weiss im Gespraech. Aber einige Anrufe werden schon
dafuer sorgen, dass sie in meiner Schuld stehen und ihn sehr ungerne
ungestraft am Leben lassen wuerden."* Und dazu: *"er hat Sang-Hoon
manipuliert. Alleine der sorgt schon fuer ein bye bye bye."*

**Ausgefuehrt in B2 90 als neun Anrufe von Annie.** Drei Dinge daran sind
Regeln und keine Szene:

1. **Annie telefoniert, nicht Georgij.** Regel 2: er besitzt nichts, hat kein
   Telefon und keinen Namen. Sie hat den Stand, und nur sie kann jemanden in
   ihre Schuld setzen.
2. **Das gebrochene Versprechen bleibt gebrochen.** Der VERFALLEN-Eintrag zu
   *"I am going to have him before the end of the year"* steht unveraendert.
   Wer spaeter versucht, Georgij den Sturz zuzuschreiben, hebt den ganzen
   Schluss auf.
3. **Choi erfaehrt nie, wer davon weiss.** Seine einzige Szene liegt am
   6. November, die Anrufe fangen am neunten an. *"He will not know that there
   is a where."* Das ist ausdrueckliche Vorgabe des Autors und keine
   Kunstfertigkeit.

**Und das Verfahren ist nicht neu.** Es steht seit Kapitel 36 im Buch und ist
seither nie benutzt worden: *"I go to them one at a time and I tell them what
was done to them. I do not accuse him of anything, because he has never once
claimed anything."* **Damit ist es zugleich die groesste Heft-Entnahme des
Buches** - ein Plan, der im Mai abgelegt und im November geholt wird.

