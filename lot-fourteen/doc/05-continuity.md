# Kontinuitaet

Kalender, Kapitelstand, wiederkehrende Bilder, woertlich festgelegte Zeilen. Die Datei fuers Pruefen.

---

## Kalender und Kapitelstand

Tag 1 ist Samstag, der 4. Oktober. Jede Datumszeile laesst sich daraus
nachrechnen, und `check.py` tut das automatisch.

### Kalender

**Tag 1 ist Samstag, der 4. Oktober.** Ohne Jahresangabe, und das Jahr wird nirgends genannt. Erzwungen wird das durch Kapitel 12, wo Kang sagt "On Saturday you asked me for guidance": Tag 22 muss ein Samstag sein, und 21 ist durch sieben teilbar, also ist Tag 1 ebenfalls Samstag.

**Jedes Kapitel trägt eine Datumszeile.** Kapitel mit mehreren Abschnitten bekommen sie als Zwischenüberschrift (`## Day Thirty-One · Monday 3 November`), Kapitel an einem Tag als Kursivzeile direkt unter dem Titel (`*Day 22 · Saturday 25 October*`). Spannt ein Kapitel über zwei Tage, steht die Spanne dort (`*Days 27 to 28 · Thursday 30 to Friday 31 October*`). Die Nacht nach der Auktion und die Nacht nach der Gala zählen jeweils zum Vortag, weil sie erzählerisch dazugehören.

**Kapitellängen.** Der Median liegt bei etwa 2800 Wörtern, die Spanne zwischen 2000 und 4300. Wird ein Kapitel deutlich länger, ist es zwei. Kapitel 14 stand bei 6475 und wurde an der Tagesgrenze geteilt.

**Kapitelüberschriften mit Datum.** Wo ein Kapitel datierte Abschnitte hat, steht der Wochentag und das Datum dabei: `## Day Thirty-One · Monday 3 November`. Das ist Leserführung und gilt ab jetzt für jedes datierte Kapitel.

**Ein Kapitel hat nicht zwingend einen Tag, und die erste Datumszeile ist nicht der Tag des Kapitels.** Sieben Kapitel haben mehrere Abschnitte: **5** (vier Tage), **12**, **14**, **27** und **28** (je drei), **26** und **34** (je zwei). Kapitel 14 laeuft ueber die Tage **31, 33 und 34**.

**Am 23.08. hat das eine richtige Angabe in `doc/02-leads.md` kaputtkorrigiert.** Dort stand, Annie bekomme bis **Tag 34** kein Laecheln. Beim Pruefen wurde die erste Datumszeile von Kapitel 14 gelesen, *Day Thirty-One*, daraus geschlossen, das Kapitel sei Tag 31, und die richtige Zahl in eine falsche geaendert. *And then he smiled* steht im Abschnitt **Day Thirty-Four**. Zurueckgenommen.

**Die Regel daraus:** Wer ein Ereignis datieren will, sucht die Datumszeile **ueber der Stelle**, nicht die oben im Kapitel. `awk '/^## Day/{d=$0} /suchwort/{print d}'` macht das in einer Zeile.

- Tag 1, Sa 4. Oktober: die Auktion
- Tag 4, Di 7. Oktober: Jang kommt
- Tag 6, Do 9. Oktober: die Inventur des Haushalts
- Tag 9, So 12. Oktober: der Schneider, die Fernbedienung verschwindet
- Tag 19, Mi 22. Oktober: die Datei auf ihrem Rechner
- Tag 22, Sa 25. Oktober: die Gala
- Tag 23, So 26. Oktober: der Morgen danach, Jangs Bericht
- Tag 25, Di 28. Oktober: Kangs Anruf
- Tag 26, Mi 29. Oktober: Annies Bitte
- Tag 27, Do 30. Oktober: sein Ja in der Küche
- Tag 28, Fr 31. Oktober: das Essen mit Woo
- Tag 31, Mo 3. November: die Gesichter über die Fotografen
- Tag 33, Mi 5. November: Hanseong gefunden, Schreiben beginnt
- Tag 34, Do 6. November: die acht Seiten bei Annie
- Tag 39, Di 11. November: Hanas Name im Grundbuch
- Tag 41, Do 13. November: das Essen zu dritt
- Tag 45, Mo 17. November: Annie unterschreibt den Mietvorvertrag, Georgij zieht die zweite Abteilung
- Tag 46, Di 18. November: das Essen mit Sang-hoon, die Heimfahrt, die festgelegte Zeile
- Tag 48, Do 20. November: Sang-hoon gibt die neunzehn Seiten zurück und das Mandat (Kapitel 18), am Nachmittag Yeongjong (Kapitel 19)
- Tag 49, Fr 21. November: der Bericht ueber Yeongjong, das Hanseong-Gebot geht Montag raus (Kapitel 20), am Nachmittag Hanas Haus (Kapitel 21)
- Tag 52, Mo 24. November: das Gebot geht raus
- Tag 55, Do 27. November: Sang-hoon kommt ins Haus, die Preisfrage, der Bruch (Kapitel 22), in derselben Nacht die Mapo-Bruecke (Kapitel 23 und 24)
- Tag 59, Mo 1. Dezember: die Vollmacht wird gezeichnet, Mr Chaes erster Auftritt, der Anruf bei Woo (Kapitel 25)
- Tag 62, Do 4. Dezember: Sang-hoon kauft die vierzig Prozent von Hanseong (Schluss von Kapitel 25)
- Tag 63, Fr 5. Dezember: der Apfelsatz faellt (Kapitel 26)
- Tag 66, Mo 8. Dezember: Georgij bei den Kims, im eigenen Gebaeude (Kapitel 26)
- Tag 67 bis 70, Di 9. bis Fr 12. Dezember: der Mietvertrag Woo/Hana (Kapitel 27)
- Tag 70, Fr 12. Dezember, spaeter Nachmittag: die eine Einladung und der Brief (Kapitel 28)
- Tag 71, Sa 13. Dezember: die vier Zeilen, neun Fassungen, Hana uebergibt sie im Garten (Kapitel 28)
- Tag 72 bis 74, So 14. bis Di 16. Dezember: keine Antwort (Kapitel 28)
- Tag 74, Di 16. Dezember: Hanas Abend, sechs bis neun (Kapitel 29), ab neun die Terrasse (Kapitel 30)
- Tag 80, Mo 22. Dezember: die Unterschriften bei Sung-ho (Kapitel 32)
- Tag 87, Mo 29. Dezember: Sang-hoon kommt die Auffahrt herauf (Kapitel 33)
- Tag 91, Fr 2. Januar: **Annie legt ihn still.** Nichts bis Maerz, kein Grund
  genannt (Kapitel 34)
- Tag 112, Fr 23. Januar: die einzige Ausfuehrung unter der Vollmacht, eine
  Fristverlaengerung in Jung-gu, vier Minuten (Kapitel 34)
- Tag 139, Do 19. Februar: **der Registereintrag wird gestrichen** (Kapitel 34)
- Tag 145, Mi 25. Februar: die stillgelegten Wochen, zweiter Abschnitt von 34
- Tag 149, So 1. Maerz: **die Sperre vom 2. Januar laeuft an diesem Tag aus**,
  weil sie bis Maerz galt und Maerz an diesem Tag anfaengt. Niemand erwaehnt es,
  auch Georgij nicht. Die Vollmacht laeuft am Ende desselben Tages um Mitternacht
  ab; Mr Chae holt die Zweitschrift, der Eintrag ist gestrichen, das Halsband
  bleibt (Kapitel 34). **Ende Band 1**
- Tag 150, Mo 2. Maerz: **Anfang Band 2.** Erster Arbeitstag, weil der Sonntag
  ihr gehoert hat. Er bittet um eine neue Vollmacht und bekommt sie nicht. Der
  aufgeraeumte Katalog kommt ins Haus (Band 2, Kapitel 1)
- Tag 152, Mi 4. Maerz: Gimpo, Shins Hof. **Er bezahlt zum ersten Mal, statt zu
  nehmen**, und bekommt dafuer das Vetorecht von unten zu sehen (Band 2,
  Kapitel 2)
- Tag 153 bis 155, Do 5. bis Sa 7. Maerz: **die Aktensuche nach den anderen zwei
  Zeilen**, unbeauftragt. Drei von vier Abenden aufgeloest, **Mrs Sunwoo**
  gefunden, der vierte Abend hat kein Papier. Abends Ulsan und die erste
  offene Zurueckhaltung ihr gegenueber (Band 2, Kapitel 3)
- Tag 159, Mi 11. Maerz: **die Trauerfeier**, das Buch ohne Umschlag, Sang-hoon
  im Korridor. Er bekommt die Tuer ins Register und bezahlt mit der vollen
  Auskunft ueber Hanseong. Jang meldet den Wagen, **Annie hat es zuerst**
  (Band 2, Kapitel 4)
- Tag 159, Mi 11. Maerz, abends: **die Abrechnung im kleinen Zimmer.** Er hat
  sich selbst ausgegeben, und das gehoert ihm nicht. Die Vollmacht wird
  erteilt, mit Deckel, benannten Gegenparteien und Frist bis zum 31. Maerz
  (Band 2, Kapitel 5)
- Tag 161 bis 163, Do 12. bis So 15. Maerz: Vorbereitung auf den neuen Mann,
  ausschliesslich aus den Unterlagen der drei Haeuser, die er vorher
  ausgeraeumt hat (Band 2, Kapitel 6, rueckblickend)
- Tag 164, Mo 16. Maerz: **das Auktionshaus.** Mrs Jeon im Settlement, die
  Warnung vor der Bezahlung, *"I have to ask"*. Der aelteste der vier
  Eintraege ist nie ueber den Schreibtisch gelaufen. Abends der Preis, Annies
  Absage an den eigenen Namen und Sang-hoons statt dessen. Nachts die
  Gesellschaftskette und der Abbruch (Band 2, Kapitel 6)
- Tag 166, Mi 18. Maerz: **Nam Byung-hee schreibt am achtzehnten.** Vormittags
  gibt Mrs Jeon den Rest heraus, **Mr Hwang** bekommt einen Namen. Nachmittags
  der Brief: eine Stunde, die sechs im Raum, Frist **26. Maerz**, danach
  schreibt sie **am ersten April** wie immer (Band 2, Kapitel 7)
- Tag 168, Fr 20. Maerz: **Ulsan.** Mit dem Zug, ohne Wagen, unangekuendigt.
  Annie weigert sich ausdruecklich, ihn zu schicken. Er erklaert Nam das Veto
  und bekommt Aufschub bis zum **1. April**. Sie laesst sich seinen Namen
  aufschreiben (Band 2, Kapitel 8)
- Tag 168, Fr 20. Maerz, nachts: **der Bericht, und die Frage, die er seit dem
  2. Maerz nicht gestellt hat.** Annie hat fuer eine **Loeschung** bezahlt und
  einen **Strich mit Aufbewahrung** bekommen. Das Veto wird auf Nams Spur
  schlicht nicht mehr gezogen. **Georgij benennt zum ersten Mal ein Ziel:
  das Haus ist Ende April erledigt, und zwar durch seine eigenen Kunden**
  (Band 2, Kapitel 9)
- Tag 172, Di 24. Maerz: **Mrs Sunwoo.** Er sagt einen Satz und laesst sie in
  ihrer eigenen Post nachsehen. Sie fuehrt die Sache ab jetzt selbst, ueber den
  ganzen April, ohne dass Annies Name faellt. Und: der Betrug ist aelter als die
  Aktenfuehrung (Band 2, Kapitel 10)
- Tag 172 bis 179, Di 24. bis Di 31. Maerz: Ladung faehrt in Ulsan, Mrs Sunwoo
  isst zweimal zu Mittag, ein Haus, das seit 1988 dort kauft, sagt eine
  Besichtigung ab. **Die Vollmacht laeuft am 31. aus und wird nicht erneuert**
  (Band 2, Kapitel 11, rueckblickend)
- Tag 180, Mi 1. April: **Nams zweiter Brief und seine Antwort.** Sie hat nicht
  an ihre sechs geschrieben und fragt statt dessen, **was er ist.** Er schreibt
  es ihr mit der Hand: der 4. Oktober, die Nummer, drei Zeilen ueber ihrer
  (Band 2, Kapitel 11)

**Das Jahr bleibt ungenannt, aber `check.py` rechnet mit dem 4. Oktober 2025.**
Der Februar hat damit achtundzwanzig Tage, und daraus folgen Tag 145 fuer den
25. Februar und Tag 149 fuer den 1. Maerz. Wer das Jahr verschiebt, verschiebt
beide.

### Die Fahrerwoche

**Der Wechsel liegt am Samstag.** Das ist nirgends ausgesprochen und ergibt sich
zwingend aus zwei Stellen, die beide Kanon sind: Kapitel 11 an Tag 22, Samstag
25. Oktober, fährt **Mr Ku**; Kapitel 16 an Tag 46, Dienstag 18. November, fährt
**Mr Pyo**, und der Text sagt dort ausdrücklich *"The two drivers went week and
week about and this one was his."* Bei einem Wechsel am Montag oder Sonntag gehen
diese vierundzwanzig Tage nicht auf, bei einem Wechsel am Samstag genau.

Daraus, für alles Weitere:

| Woche | Wer |
|---|---|
| Sa 25.10 - Fr 31.10 | Ku |
| Sa 1.11 - Fr 7.11 | Pyo |
| Sa 8.11 - Fr 14.11 | Ku |
| **Sa 15.11 - Fr 21.11** | **Pyo** (Kapitel 16, 17, 20, 21) |
| Sa 22.11 - Fr 28.11 | Ku (Kapitel 22) |
| Sa 29.11 - Fr 5.12 | Pyo |
| Sa 6.12 - Fr 12.12 | Ku (Kapitel 27, Donnerstag der 11.) |
| **Sa 13.12 - Fr 19.12** | **Pyo** (Kapitel 28, 29, Hanas Abend am 16.) |

**Und einmal hat diese Tabelle selbst den Fehler gemacht.** Sie liess die Woche
vom 6. bis 12. Dezember aus und schrieb die folgende auf Ku. Kapitel 29 stand
darum am Dienstag, dem 16., auf *"Mr Ku had him at the gate at six, which was
his week"* - und Kapitel 28 hatte drei Tage vorher, am **Samstag dem 13.**,
also am Wechseltag selbst, schon Mr Pyo fahren lassen. Zwei Kapitel
nebeneinander, zwei verschiedene Fahrer in derselben Woche. Korrigiert am
23.08.: 29 faehrt Pyo, weil 28 und die Alternation aus beiden Ankern es sagen
und weil dort eine Zaehlung gegen zwei steht.

**Die Lehre daraus ist nicht die Rota.** Ein Hilfsmittel, das gegen den Text
gehalten wird, muss selbst geprueft werden, sonst schreibt es den Fehler in den
Text, statt ihn zu finden. Diese Tabelle hat genau das getan.

**Warum das hier steht.** In Kapitel 21 stand zuerst Mr Ku, an einem Freitag in
Pyos Woche. Das ist der Fehler aus `doc/01-craft.md`, Punkt 2: ein Fahrer, der
laut Rota diese Woche nicht fährt. Er fällt keinem Skript auf und keinem Leser,
der nicht zurückblättert.

**Feste Termine voraus, ab Kapitel 21 im Text genannt und damit Kanon:**

- Mo 24. November (Tag 52): Annies Gebot auf Hanseong geht raus
- erste Dezemberwoche: Sang-hoon unterschreibt bei der Haelfte, die aussteigen will
- **Di 16. Dezember: Hanas Abend.** Georgij um sechs, Woo um sieben, die Kims um acht, Ye-rin um neun, Kang um halb zehn. **Der Fotograf ist von sieben bis neun da und dann nicht mehr**, und daran hängt alles Weitere: das Bild von Woo neben der Familie entsteht gegen zehn nach acht und steht am Donnerstag in zwei Zeitungen.

  **Woo bleibt bis halb zehn, und das ist eine Bitte, die Georgij noch stellen muss.** Der Grund steht in `doc/07-next.md`: Ye-rin braucht einen Beweis und keine Hoffnung, sie steht auf keinem Bild und liest keine Zeitung über einen Fremden, also muss sie den Mann im Raum stehen sehen. Damit begegnen Woo und Kang sich für etwa vier Minuten in Hanas Halle. **Das bricht Woos Bedingung nicht**, denn die lautet wörtlich *"no photograph with a politician in it"* und nicht: keine Begegnung. Zu diesem Zeitpunkt ist kein Fotograf mehr im Haus.

  **Und der Punkt, an dem das Kapitel hängt:** Hana konnte diesen Fehler nicht selbst vermeiden, weil sie sich zwei Absätze vorher verboten hat zu wissen, wofür der Abend ist. Sie stellt Georgij die Rechnung dafür im selben Gespräch, ohne Vorwurf.
- Februar: Ye-rin bricht, wenn bis dahin nichts steht

**Prüfregel:** Jeder Tag mit Rest 1 bei Teilung durch sieben ist ein Samstag. Sang-hoon hat "after the fifteenth" gesagt, der Sechzehnte wäre ein Sonntag, deshalb der Achtzehnte.

### Geprueft und stehengelassen

**Was `check.py` dauerhaft meldet, ohne dass etwas zu tun ist.** Am 22. August
einmal vollstaendig durchgesehen. Wer eines davon wieder untersucht, verliert
eine halbe Stunde.

**Zwei Zahlen-Fehlalarme, in der Basislinie verbucht:**

- **Kapitel 6, Zeile 40**, *"two languages"*. Gehoert einem anderen Los im
  Auktionskatalog, nicht Georgij. Die Pruefung kann das Subjekt nicht sehen.
- **Kapitel 12, Zeilen 28 und 56**, *"two sheets"*. Jangs zwei Blatt aus dem
  Sicherheitsbuero, nicht der Hanseong-Bericht.

**Vier Fragezeichen-Hinweise, alle Aussagesyntax und alle richtig mit Punkt:**
Kapitel 1 *"When he bought the boy."*, Kapitel 9 *"Whatever I was given."*,
Kapitel 24 *"What you paid me in on the gravel."*, Kapitel 26 *"What she wants
is shares, security, and a veto over routes."* Der Regex trifft auf *What* und
*When* am Satzanfang, ohne den Satzbau zu pruefen.

**Zwei Ketten nackter Repliken, beide in Ordnung:** Kapitel 2 ab *"You waited,
though."* und Kapitel 24 ab *"Then you did not leave."* Schneller
Frage-Antwort-Wechsel mit kurzen Repliken; der Leser kann jede Zeile zuordnen.
Die Meldung ab sieben ist ein Anlass zum Hinsehen, kein Urteil.

**Zwei Ton-Etiketten aus frueheren Fassungen**, bewusst stehengelassen: Kapitel
1 *"kept his voice warm and unhurried, and let it carry"* - das *let it carry*
ist eine Handlung und traegt den Satz - und Kapitel 13 *"without any pressure
anywhere in it"*. Beide sind alt, abgenommen und stehen seit Monaten.

**Die Laengen:** Kapitel 5 mit 4340 und Kapitel 27 mit rund 4700 liegen ueber
der Spanne. Nach `doc/01-craft.md` Punkt 0 wird dafuer nicht gekuerzt.

### Stand der Kapitel

- **Kapitel 1** *Merchandise doesn't talk* (v6.5) - Auktion, Los elf, der Zuschlag, die Fahrt, quid pro quo. Endet auf "Unless somebody buys him first."
- **Kapitel 2** *Quid pro Quo* (v11.7) - Die Auffahrt, zwei Stromstöße, das Angebot zu Los elf, das Auge, die Einlösung des Vertragssatzes, ihr Auftrag, die Fernbedienung neben der Schlüsselschale.
- **Kapitel 34** *Then take it off* (v1.8) - **Drei Abschnitte, und der Schluss von Band 1.**

  **Tag 91, Fr 2. Januar. Der Befehl.** Sie sitzt eine Stunde vor dem Wagen im kleinen Zimmer und hat nach niemandem geschickt. *"There is nothing for you between now and March. ... You will not open anything new. You will not go and look at anybody."* **Er fragt nicht nach dem Grund, sondern nach der Kante** - *"Does that include what is already open?"* -, und die Kante ist enger als erhofft: *"It includes going and looking."* Sie stellt fest, dass er nicht gefragt hat, sagt nichts dazu und geht.

  **Den Grund arbeitet er sich zehn Minuten spaeter auf der Treppe zurecht:** Strukturschutz, waehrend das Geld in drei Tranchen laeuft. Kompetent und falsch. *"In November he had been wrong about this woman twice in four days, on facts he was holding at the time. This one took ten weeks."*

  **Tag 145, Mi 25. Februar. Die stillgelegten Wochen.** Er ist nicht beschaeftigungslos, er ist stillgelegt, und das ist etwas anderes. Woos erste Ladung faehrt seit dem 9. Januar, der Kim-Block hat zweimal abgestimmt, Annies Kapital ist im Januar geflossen. **Zweimal bringt er ihr trotzdem etwas**, getarnt als Notiz zu etwas Offenem: beim ersten Mal dreht sie das Blatt um und sagt nie ein Wort dazu, beim zweiten kommt er nicht bis zum Ende des ersten Satzes. *"No," she said again, and she was not unkind about it, and that was the part he could not get past.* Die **2.200.000.000 aus Kapitel 33 gehen nicht weg**, und das Schlimme daran ist, dass er eine Meinung dazu hat, ob sie stimmen.

  **Die Vollmacht wird genau einmal benutzt:** eine Fristverlaengerung in Jung-gu am 23. Januar, vier Minuten, **weil er an dem Nachmittag der Einzige im Haus mit Zeichnungsbefugnis ist.** Kein Erwerb, Verwaltung. *"The signature came out the same as it had come out in December. He had one now, and this was the thing it turned out to be for."*

  **Tag 149, So 1. Maerz. Mr Chae um zehn.** Die Vollmacht laeuft um Mitternacht ab. Die zwei Woerter vom 1. Dezember lauten **"No fee"**. Und Georgij rechnet ihm die eigene Fehlkalkulation vor: Auf der Bruecke hatte er **vier Raeume bis Februar** vorhergesagt und **zwei Unterschriften** darin. Es wurden vier Raeume - 8., 16., 22. und 29. Dezember - und **keine einzige Zeile.** *"Then you were right about the rooms."* Damit loest sich Chaes erster Satz vom 1. Dezember ein: *this instrument is smaller than you think it is.* Zum Umschlag sagt er nur *"That is not this instrument"* und *"I am at home today"*.

  **Dann fragt Annie, wie am 16. Dezember angekuendigt, und er antwortet mit einer Zahl**, weil das die einzige Einheit ist, die er fuer sich selbst hat. Sang-hoons Minute an der Tuer hat genau das gekauft.

  **Der Eintrag ist gestrichen**, am 19. Februar, nach sechs Wochen und vier Terminen in dem Gebaeude, **und beim dritten Mal war es nicht das Geld.** Ihr Grund ist geschaeftlich: die Zeile war der letzte Weg, auf dem ihn ihr jemand haette abkaufen koennen.

  **Und hier wird der Januar eingeloest.** Georgij fragt danach, und sie rechnet es vor: Jeder Raum, aus dem er als Sieger kommt, legt etwas auf Sang-hoons Zahl, und sie wollte nicht viermal in diesem Gebaeude sein, waehrend er teurer wird. Verschwiegen hat sie es, **weil er die Differenz bepreist und einen Weg gefunden haette, nuetzlich zu sein, den sie von dort nicht sieht.** Die zweite Haelfte bleibt einen Spalt offen und niemand geht hindurch: *"Is that all of it." - "It is all of it that has a figure in it."*

  **Damit ist ihre Bedingung aus Kapitel 24 erfuellt** - *"until that is dealt with"* -, und das Halsband kann ab. **Er weigert sich.**

  **Von den drei Saetzen der Bruecke ueberlebt einer, und das ist neu ab v1.8.** Zwei sind mit dem Eintrag weggefallen; *"a man who belongs to nobody is stock"* nicht, und er beschreibt jetzt ihn. **Das Halsband ist ein Zeichen ohne Deckung** - *"What is round my neck is a mark with nothing behind it. It goes on working for exactly as long as nobody looks in that book."* Annie bietet ihm das als Grund an, und **er nimmt ihn nicht**: *"Then keep it for that." - "It would hold." He did not take it. "It is not why."*

  **Der zurueckgehaltene Grund steht im Konditional, weil alles andere unwahr waere:** *"Until the nineteenth of February, if you had finished with me, you would have had to sell me."* Preis, Raum, Zeugen, Wochen, und um den neunten Morgen herum haette sie vielleicht nicht mehr gewollt. *"And now." - "Now there is nothing to sell."* Die einzige Kontraktion des Kapitels steht davor: **"I'm afraid of Tuesdays."**

  **Was der Satz heisst, und nur das, festgelegt am 23.08.:** Die Angst gilt **ausschliesslich davor, von ihr verstossen zu werden**, in einem Flur, zwischen zwei anderen Dingen. Sie ist **keine allgemeine Furcht vor Dienstagen** und darf nirgendwo sonst mitschwingen. Ein Dienstag im uebrigen Kalender ist ein Wochentag wie jeder andere - Kapitel 16 spielt an einem, das Essen mit Sang-hoon, und das traegt keine Ladung.

  **Annie benennt es, und er gibt es zu:** *"You are describing being free," said Annie. - "I am describing how cheap it has become to be finished with me. ... Those are the same thing. I know that they are."* Seine Weigerung ist damit nicht unlogisch, sondern zugegeben unvernuenftig.

  Dann die Umkehrung aus Kapitel 24 - *"It is not what holds me and it never was. It is what holds you."* - und **"I will not stop calling you Mistress"**, ohne dass noch ein Papier es verlangt. **Das faellt, bevor sie sich bewegt.** Erst danach geht sie ans Fenster, stellt sich mit dem Ruecken zum Raum und sagt *"Come here."*, und **er geht auf dem Boden an ihren Beinen herunter** - sie steht dabei, es gibt keinen Stuhl. *"He went down onto the floor beside her ... and sat back on his heels with his shoulder against her leg."*

  **Die vier Tuesdays liegen in einer Kette, und Annie legt das Wort hin.** Chae sagte in einer frueheren Fassung beilaeufig *"explain on Tuesday"* und hat es damit vor der Zahlung verbraucht; er sagt jetzt Montag, was ausserdem stimmt, weil die Vollmacht Sonntag um Mitternacht stirbt.

  **Der Registereintrag zum Schluss, und die drei Dokumente.** *There is no column on that page for what a man is called. There has never been one, because a name is the one thing in the transaction that nobody on either side of it needs.* Die anderen beiden - die im Oktober geordneten Papiere und die Vollmacht - tragen seinen Namen und handeln davon, **was er tun darf**. Das Registerblatt war das einzige, das davon handelte, **was er ist**.

- **Kapitel 33** *That is five* (v1.11) - Tag 87, Montag der 29., in der toten Woche zwischen den Jahren. Sang-hoon kommt **die Auffahrt herauf**, angemeldet, nicht ueber die Mauer, und bietet **2.200.000.000 Won**. Annies Hand geht nirgendwohin; die Jacke haengt in einem anderen Zimmer. Sie dreht den Kopf fuenfzehn Grad zu Georgij, und das ist alles, was sie tut. **Er bittet sie vorher um Erlaubnis, ihre Anweisung aus 17 zu brechen** ("Be pleased with it in this car and nowhere else"). Dann die **fuenfte und letzte Guidance**, und er sagt vorher, dass er diesmal nicht wirklich fragt: *"Please guide me. How does a man let go of a sweet, sweet, beautiful, poisoned apple that he has already bitten into?"* Elf Sekunden, dann lacht Sang-hoon. Auf die Kims: *"There is nothing to announce."* - *"That is not an answer."* - *"It is the whole answer."* Annies vier Woerter: **"He was never for sale."** Und an der Tuer legt Sang-hoon **eine Zahl in Georgijs Kopf**, sagt, sie sei zu niedrig, und dass er nicht zweimal zahlt. Im Maerz will Annie ihn fragen, was er will.
- **Kapitel 32** *In those words* (v1.2) - Tag 80, Montag der 22., in Sung-hos Haus von 1974. Neun Leute, Ye-rin zum ersten Mal seit zwanzig Jahren mit einem Fremden in einem Raum, auf dem Stuhl, von dem aus man beide Tueren sieht. Georgij steht und macht die unangenehme Haelfte zuerst. **Die schaebige Frage - "How much are they paying you?" - und die wahre Antwort: nichts, und er wird nicht bezahlt.** Dann sagt der Cousin mit dem Temperament, dass ihm zweimal Geld geboten wurde, und **der ganze Tisch dreht sich zu Ye-rin um, ohne dass einer es entscheidet.** Die siebzehn Fotos aus 15, live, in anderthalb Sekunden. Georgij sagt nichts dazu, weil Benennen es zum Trick machen wuerde. Unterschrift um zehn nach vier, Ye-rin zuletzt auf Seite elf. Do-yun am Tuerrahmen: sechs Tage statt vierzehn.
- **Kapitel 31** *A number and a date* (v1.6) - Der Rest des Abends, die Heimfahrt, und Annie wach im kleinen Zimmer mit nichts in den Haenden. Der Bericht gerafft. **Dann fragt sie ihn, was er will, und er sagt es nicht** - mit derselben Begruendung, die er eine Stunde vorher Ye-rin gegeben hat, und sie erkennt es. Sie setzt **Maerz** darauf. Am Morgen Woo am Telefon: es hat funktioniert, die Fotos waren nicht verschwendet, und seine eine Frage aus Kapitel 13 hat es getan. Der Raum: Montag, der 22., bei Sung-ho, kein Hotel.
- **Kapitel 30** *Who do they telephone* (v1.7) - Die Terrasse, zweiundzwanzig Minuten. **Das eine Gespraech, und es ist gelungen.**

  **Sie geht selbst hinaus**, ohne Mantel, und stellt sich an die Ecke, von der aus das Glas den ganzen Raum gibt - dorthin, wo sie die Tueren sieht. Er gibt es vierzig Sekunden und folgt.

  **Der Zutritt ist das Papier**, wie in `doc/07-next.md` vorgesehen: sechs Vorgaenge in zweiundzwanzig Jahren, in denen sie offensichtlich gehandelt hat und in keinem einzigen vorkommt. Er liest sie vor wie einen Busfahrplan und sagt dazu, dass er nichts davon beweisen kann. *"Your brother's people have never found any of it."* - *"Your brother's people were not looking for a woman."*

  **Die Frage ist Woos Frage, uebersetzt.** Bei Woo galt sie einem Gegenstand, bei ihr einer Funktion: **"When you do not answer the telephone any more, who do they call?"** Ihre Antwort kommt flach und sofort, weil sie seit dreizehn Jahren fertig dasteht: **"Nobody."**

  **Was sie bekommt:** Die sechs binden ihre 41 Prozent zu einem Block, gerichtet von einer im Dokument benannten Person. Das erste Papier seit zwanzig Jahren mit ihrem Namen darin.

  **Der Preis, im selben Atemzug genannt, bevor sie ihn selbst findet:** Unsichtbar muss Sang-hoon sechs Leute kaufen. Aufgeschrieben muss er **eine brechen**. *"You become the place to press. I would rather you heard that from me on a terrace than worked it out in March."* - *"You are very bad at selling things."* - *"I am extremely good at selling things. This is the other one."*

  **Und den Grund, warum sie es trotzdem nimmt, findet sie selbst**, weil Georgij ihn ihr ausdruecklich nicht in den Mund legt: *"I know what it costs you. I do not know what it buys you, and I have thought about it for four days, and I am not going to invent something and put it in your mouth."* Ihre Antwort: **Unsichtbare Macht stirbt mit der Person, aufgeschriebene ist am Morgen noch da.**

  **Was sie dafuer haben will, ist eine Grenze fuer das Veto:** *"The veto covers boxes. Which box, which sailing, which port, which week. It does not cover people."* Abgelehnt, und zwar sofort, obwohl er ihr zustimmt - *"the first thing she had said all evening that he wanted to agree with."* Der Grund ist ein Satz und keine Ausrede: **Wer entscheidet, welche Kiste auf welches Schiff geht, entscheidet, wer sie laedt.** Ein Veto, das an der Ladung endet und den Hof nicht erreicht, ist eine Zeile in einem Dokument.

  Und er sagt geradeheraus, was daraus folgt, statt ein Wort dafuer zu suchen: *"So they become staff."* - *"In the way that counts, yes. I am not going to find you a kinder word for it at half past nine on a terrace, and if I did you would only have to unlearn it in March."* **Das ist der Faden, an dem sie spaeter von selbst zurueckkommt.**

  **Ihre zwei Zahlungsmittel dafuer, beide abgelehnt, beide mit Begruendung:**

  - **Zeit** bis Maerz gegen ihr persoenliches Wort. Abgelehnt, *weil* er dem Wort glaubt: Es bindet sie und nicht die sechs, und macht sie drei Monate lang haftbar fuer einen Cousin mit Temperament.
  - **Do-yun**, den sie liefern kann - *"where he works, what he carries out of that building, and whose telephone he answers on a Sunday"*, und *"there is nobody else alive who can say that sentence about him."* Das ist die einzige Stelle, an der sie ihre Macht vorzeigt, und er lehnt sie ab, weil sie nichts kostet: Am Tag der Unterschrift hat sein Arbeitgeber verloren und er steht binnen vierzehn Tagen bei Sung-ho vor der Tuer. *"If I said yes to it, I would be taking a price off you for something I get free. You would find that out in March, and then nothing I ever said to you again would be worth hearing."*

  **Das ist die Stelle, an der Luegen alles glatt geschlossen haette**, und sie sagt es: *"You could have said yes."* - *"Because you are going to be in rooms with me for the next fifteen years, and I would like all of them to be like this one."*

  **Die Veto-Grenze wird vertagt, nicht abgelehnt.** Es gibt einen Preis, der sie kaufen wuerde, und Georgij nennt ihn nicht: *"There is a thing that would buy the line about people, and I am not going to tell you what it is."* Begruendung: *"It is a very large price and it buys a limit I do not think you will need for two years. If you ever do need it, you will think of it yourself in about four seconds, and then it is yours to offer. It is not mine to have put in your head in December."*

  **Das Geschenk danach, damit es nichts bezahlt:** wer den Container hingestellt hat, ausdruecklich als Vermutung. Der Grund ist nicht taktisch - *"you have spent six weeks looking at nine people at dinner and wondering. That is a bad way to live and it is worse than useless, and you can stop."*

  **Ihre Anweisungen zum Schluss** sind die Zusage: Dokument an den Bruder ins Buero, zweite Kopie in einem blanken Umschlag ueber Hana an einem Donnerstag, und die sechs hoeren Georgijs Satz **vor** dem guten Teil. Dann: *"Twenty-two minutes. I told my driver twenty."*
- **Kapitel 29** *The ones who came at seven* (v1.3) - Der Abend, sechs bis neun.

  **Annie kommt nicht, und das ist entschieden und begruendet:** *"If I am in that house it is my evening. Then it is a chaebol standing in a room with a family under investigation, and everybody spends the week deciding what it was for."* Georgij ist da und jeder weiss, wessen er ist, und das ist der Unterschied zwischen einer Besprechung und einer Party.

  **Das Bild entsteht um elf nach acht und dauert vier Sekunden**, und niemand stellt es. Woo zeigt mit dem Stock auf eine schlechte Aufnahme von 1974, Sung-ho steht an seiner Schulter, zwei Neffen sind mitgekommen, weil ihr Onkel mitgekommen ist. Danach die Leere, die Georgij aus Yeongjong kennt: *"It is not disappointment. It is the sudden absence of the load."*

  **Und die Kang-Frage loest sich auf, waehrend er sie stellt.** Er geht zu Hana, um sie zu bitten, die beiden Maenner in der Halle auseinanderzuhalten, und hoert sich mitten im Satz zu: **Es ist vier Wochen alt.** Kang war in zwei Rollen gefaehrlich, und beide sind weg. Als Kanal zu Sang-hoon wird er nicht gebraucht, weil das Foto Donnerstag ohnehin in zwei Zeitungen steht - *"he is a day early with something I am paying a man to print."* Und als Drohung gegen Hana ist er entwertet, seit ihr Wert nicht mehr allein an der Widmung haengt.

  **Wichtig fuer die Genauigkeit:** Am 16. ist **nichts unterschrieben**. Woo feilscht noch, wie in Kapitel 27 angekuendigt. Was schon weg ist, ist nicht die Unsicherheit, sondern der Zustand, in dem eine einzige Akte in einem einzigen Gebaeude ihr ganzer Wert war.

  Hana: *"So he is just a man who comes at Christmas. That is nine years and I had stopped noticing that I count him. Do you know how long I have been careful in my own hall?"*

  **Und Hanas letzte Regel vor neun:** *"If she comes up that drive, do not go out to the car. She will not want to be met. She will want to walk in and find the room already happening."*

  **Ye-rin kommt um zwei vor neun.** Der Wagen haelt vor der Tuer, sie oeffnet die Tuer selbst, gibt ihren Mantel ab, sieht den Raum an - Bruder, Cousin, zwei Neffen, der alte Mann im Sessel mit dem Stock ueber den Knien - und dreht dann den Kopf um etwa fuenfzehn Grad zu der Ecke, in der ein Mann steht, den sie nie getroffen hat und der genau dort steht, wo vier Zeilen auf einer Karte es angekuendigt haben.
- **Kapitel 28** *A woman in a room can be asked* (v1.3) - Zweite Haelfte des Freitags, ohne Zeitsprung.

  **Ye-rin weiss seit Montag alles**, weil Sung-hos neunzehn Minuten am Telefon in Kapitel 26 ein Anruf bei ihr waren. Sie kennt Datum, Haus und Woos Ankunft um sieben, hat es geprueft, die Familie geschickt und sich selbst herausgehalten. Hanas Lesart: *"That is not a no. If it were a no she would have kept them home."*

  **Hana hat sie NICHT gefragt.** Drei Dienstage verstrichen, alle drei bewusst - am 25. hatte sie eine Party, am 2. eine Party und eine Gaesteliste, am 9. eine Party, eine Gaesteliste und einen Mann aus dem Ministerium, und sie sass zehn Minuten mit dem Telefon in der Hand. Der Grund ist ihre eigene Regel aus Kapitel 15: *"Not quickly and not twice. Once."* Was am 9. fehlte, waren *"nine people in a building in Mapo who had not said yes to anybody"*, und sie wusste seit dem 21. November, dass sie darauf wartet, und nicht, ob es je kommt.

  **Und dann der Grund, warum diese Frau ueberhaupt nirgends hingeht** - im ganzen Buch zum ersten Mal ausgesprochen und die Voraussetzung fuer alles Weitere: *"A woman in a room can be asked. Her brother has the title and can be asked, and he says he will look into it, and everyone knows what that means. She has no title, so nothing protects her from a direct question."* Zu Hause nimmt sie den Anruf oder nicht und antwortet am Donnerstag. **"That is not shyness. That is the whole engine. Twenty years of never once deciding anything while somebody was watching her face."**

  **Daraus folgt, was die Einladung sein muss:** keine Auskunft, sondern eine Zusicherung. *"It is a promise about what will not happen to her, and it has to come from the person who would otherwise be the one asking."*

  **Und deshalb schlaegt Hana den Brief vor, nicht Georgij.** Sie kann die zwei Namen tragen und nicht sagen, wofuer sie stehen, weil sie sich verboten hat es zu wissen - und sie kann die Zusicherung nicht geben, weil sie fuer ihn spraeche. Georgij sagt das Papier-Risiko selbst an, dasselbe, das er im November auf ihre Kosten formuliert hat, und schreibt trotzdem: **Jeder hat den schlimmsten Teil zuerst bekommen ausser ihr.** Hana deckt ihn unaufgefordert mit ihrer Karte, ihrer Hand und ihrem Haus auf dem Umschlag.

  **Die Lampe ueber der Stufe ist repariert.** Und in der Halle der persoenliche Teil, den er in Kapitel 21 nicht sagen konnte.

  **Der Samstag.** Er schreibt zwischen sechs und halb neun und kommt auf **vier Zeilen**, in neun Fassungen. Sechs davon sind die Arbeit eines Mannes, der etwas verkauft, und man sieht es jedes Mal in der zweiten Zeile; sie gehen ins Kaminfeuer. Der Grund fuer die Schwierigkeit ist handwerklich: *"He had written nineteen pages about a shipping group in three days in November and had enjoyed most of it, because nineteen pages is a place to hide and four lines is not."*

  **Was der Brief sagt und was nicht.** Er sagt nicht, wofuer der Abend ist, und er laedt nicht ein - das ist Hanas Teil. Er sagt, **was ihr nicht passieren wird**: keine Frage an sie, nichts zu unterschreiben, nichts zu lesen, und zwanzig Minuten stehen und gehen ist unauffaellig. Dann, in sechs Woertern und ohne Weichzeichnung, wer ihn geschrieben hat und was er ist. **Der Wortlaut steht weiterhin nicht im Text.**

  **Die Uebergabe, und das einzige Zeichen, das es gibt.** Hana findet sie im Garten und sie **zieht die Handschuhe aus, um die Karte zu halten**, was sie nicht muesste. Sie oeffnet sie nicht vor ihr. Dann fragt sie nach Hanas Mutter, die seit sechs Jahren tot ist und zu deren Beerdigung Ye-rin gekommen war. Hanas Lesart: *"That was her telling me she had understood every single thing about why I was standing in her garden, and that she was not going to make me say any of it out loud. It is the kindest thing that woman does and it is also the closest she comes to a warning."* Und dazu: *"We know she took her gloves off. I have been doing this for twenty-four years and that is all I have got. Do not build on it."*

  **Dann drei Tage nichts.** Kein Wort, keine Nachricht, nichts ueber Sung-ho. Am Sonntagabend meldet Hana, dass nichts ist; am Montag meldet sie gar nichts mehr, was selbst ein Bericht ist.

  **Und der Schluss ist der Zustand, den Georgij nicht kennt:** Alles Gebaute steht, und es aendert nichts. *"On Tuesday at nine o'clock a woman of fifty-four either walks up a drive or does not, and there is nothing I can do between now and then that moves it by a single per cent."* - *"I have never had a piece of work end like that."*

  Annies Antwort holt Kapitel 1 zurueck: *"You have. You had one in October. You stood in a cellar with a number pinned on you for four hours and could not do anything about that either."* - *"That is not the same."* - *"It is exactly the same, and it came out well."*

- **Kapitel 27** *Not out of your account* (v3.2) - Drei Tage. Georgij bittet Annie um sechs Stunden ihrer Zeit **fuer jemand anderen**, zum ersten Mal, und begruendet es kaufmaennisch: Hanas ganzer Wert haengt an einer Widmung, und damit ist sie das weiche Stueck in Annies eigener Anordnung. Annies Bedingung: *"Do not do it as a gift. Because she will not be able to accept it, and then you will have spent six hours making her poorer and more careful, and I will have lost the only person in this city who tells me things."*

  **Die Flaechen kollidieren nicht, und der Text rechnet es vor.** Annies Mietvorvertrag aus Kapitel 15 lautet woertlich *"Twenty years, rent fixed, the buildings named"* und tritt in Kraft, sobald ihr Kapital in die Logistiksparte fliesst; er verfaellt, wenn das bis Ende Maerz nicht geschehen ist. **Er nennt Gebaeude, nicht die Flaeche.** Ihre vier sind die ueberdachten auf der Nordgrenze, weil ihre Vorprodukte Dach, Temperatur und eine Zollverschlusslinie brauchen; das sind etwa fuenftausend der sechzehntausend Quadratmeter.

  **Woo will Hartflaeche**, offenes, entwaessertes Gelaende mit Tor auf der Ostseite. Container brauchen kein Dach und gehoeren in keine Zollhalle. Die beiden beruehren sich an keiner Stelle, und Georgij hat das **am Sonntag mit Lageplan und Annies Mietvertrag nebeneinander geprueft, in dieser Reihenfolge**, bevor er sie ueberhaupt gefragt hat: *"I am not going to sell the same ground twice, and I am certainly not going to sell yours."*

  **Und es geht nicht glatt auf, was richtig ist:** Woo mietet in Yeonan zwoelftausend, die offene Flaeche ist rund tausend Meter kleiner. Georgij sagt es ihm, bevor er die Zeichnung sieht. Woo nimmt es trotzdem - *"Forty minutes a load in January is four hundred hours a winter, and I have been paying it since 2019 because nobody would sell me the east side."* Das Tor ist mehr wert als der Hektar.

  **Warum die beiden nicht laengst selbst zusammengekommen sind**, und Hana sagt es selbst, weil es sonst im Raum stehen bliebe. Sie besitzt die Ostseite seit 2014 und hat sie **keinen Tag vermietet** - *"You do not let out the thing you are going to bring to the table. You sit on it and you pay the interest and you wait for the right room."* Die Flaeche war ihr Einsatz, und im November hat sie den Raum bekommen.

  **Und dann hat sie den Mietvorvertrag als Rettung gelesen und nicht nachgerechnet.** Seit dem 17. November liest sie ihn als das, was sie rettet, und hat ihn nie neben einen Lageplan gelegt: *"Because it does not say sixteen thousand anywhere in it. It says four buildings. Which I wrote. In my own conditions, at your table, in front of you both."* Vier Wochen leere Hartflaeche, uebersehen, weil sie auf die Seite geschaut hat, auf der ihre Rettung stand.

  **Dazu kommt, dass keiner von beiden je inseriert haette:** Woo nimmt keine Makler, sie nimmt keine Vermittlung. *"It is not clever of you, and I would like you to know that I know that as well. It is only that you were the one man alive who had both pages on the same desk."*

  **Der Zug selbst kostet niemanden etwas.** Woo faehrt ab Januar sieben Jahre Ankerladung durch Incheon und mietet Flaeche auf der falschen Strassenseite. Hana hat sechzehntausend Quadratmeter, die bis April leer stehen. Kein Makler, keine Provision, kein Anteil fuer Annie und keiner fuer Georgij - *"Because I do not have an account for one to go into."*

  **Und die Wirkung ist strukturell:** Aus *Grundstueck mit Widmung* wird *Grundstueck mit Ertrag*. Damit ist die dritte Grundschuld gegen den Uplift kein Abgrund im Fruehjahr mehr, sondern eine Zeile in einem Tilgungsplan - und Hana ist ueber das Ministerium nicht mehr kippbar. Das schliesst ihren offenen Faden aus `doc/03-cast.md`.

  **Sie nimmt es an, weil er es richtig benennt:** *"It is not a gift, it is arbitrage, and there is nothing in it for me at all, and I would like both of those to be true at the same time, because they are."* Und weil sein Grund nicht die Dachrinne ist, sondern der 21. November - sie hat die Frage nach dem Abend zurueckgenommen und damit das Einzige aufgegeben, was sie nie hergibt.

  **Die Lampe ueber der Stufe ist repariert**, achtzigtausend Won und ein Mann auf einer Leiter, nach zwei Jahren. Sie sagt es ihm von sich aus, damit er es nicht zaehlt.

- **Kapitel 26** *The name and the control* (v1.4) - Zwei Tage. Freitag faellt der Apfelsatz, den er seit September traegt: *"He has eaten the apple. All of it, in twelve days."* Montag steht er zum ersten Mal vor der Familie Kim, in ihrem eigenen Gebaeude, an ihrem Tisch.

  **Er legt Woos Vertrag zuerst hin, bedingungslos**, bevor er irgendetwas verlangt - sieben Jahre Ladung, ausgefertigt am 20. November, vierzehn Tage nachdem der Zoll ins Gebaeude ging. Dann verkauft er ihnen den schlimmsten Teil zuerst, weil sie ihn ohnehin finden wuerden: **"You keep the name. And she gets the control."** Der Satz aus `doc/04-world.md`, aus seinem Mund und nicht aus ihrem, ohne ein einziges weichmachendes Wort.

  **Kim Do-yun sitzt mit am Tisch**, und Georgij hat die ganze Stunde darum herum gebaut. Der Faden aus Kapitel 14 wird eingeloest: Dort hat er sich in ihm geirrt, ihn als schwach gelesen, und den Namen auf ein leeres Blatt geschrieben. Do-yuns Frage nach dem Container kommt vierzig Sekunden zu frueh, und beide merken es. *"You are going to be a problem." - "I am going to be at that house on the sixteenth from six o'clock, and so, I hope, are you."*

  **Und dann geht Sung-ho telefonieren**, neunzehn Minuten, und Georgij sitzt mit dem Mantel auf den Knien in einem Raum, in dem die Entscheidung nicht faellt. Sie faellt bei einer Frau, die nicht im Gebaeude ist, die er nie getroffen hat, die 1,4 Prozent haelt und die man **einmal** fragen kann. Ihm geht dabei auf, dass Hana ihm das im November im Klartext gesagt hat und dass er es als Schwierigkeit gehoert hat statt als Tatsache.

  **Ergebnis:** Die Kims kommen am 16., vollzaehlig. Ueber Anteile, Sicherheiten und Routen ist nichts entschieden, und Sung-ho sagt ausdruecklich, dass niemand im Raum die Befugnis dazu hat. Der Schluss ist ein durchgestrichener Satz im Notizbuch: *She said yes* - weggestrichen, weil er es nicht weiss und bis zum Sechzehnten nicht wissen wird.
- **Kapitel 25** *The name on the paper* (v1.3) - Montag, die Vollmacht. **Mr Chaes erster Auftritt.** Er erklaert das Instrument, Georgij findet die Widerrufsklausel im ersten Durchgang und will sie ausdruecklich behalten: Wenn Annie in vier Sekunden beenden kann, muss sie beim Geben nicht vorsichtig sein. Dann die Unterschriftszeile - **er hat in seinem Leben noch nie etwas unterschrieben** - und der aufgedruckte Nachname, den er noch nie gesehen hat. Chaes Satz ueber die zwei Dokumente. Der Anruf bei Woo um die halbe Stunde, ohne Begruendung. Und am Donnerstag kauft Sang-hoon.

  **Er kennt Annies Haus inzwischen ganz**, und der Text sagt, wie: nicht mehr als drei Ausgaenge und zweiundzwanzig Objektive, sondern so, wie man ein Haus kennt, in dem man wohnt - welche der vierzehn Erdgeschosstueren bei Nasse klemmen, dass der zweite Stock vier Zimmer hat und zwei davon zu sind. Er hat nichts davon gesucht; es ist ueber neunundfuenfzig Tage angekommen.

  **Und es gibt genau einen Gegenstand, den er nie gefunden hat.** Dreizehn Tage im Oktober war die Fernbedienung nirgends, wo er vorbeikam, und einmal nach der Gala hat er vom falschen Ende eines Flurs eine Schublade zugehen hoeren. Er ist nicht suchen gegangen, und das war eine Entscheidung, die er oben an der Treppe in anderthalb Sekunden getroffen hat. **In zwoelf Haeusern ist das der einzige Gegenstand, der sich vor ihm verborgen hat**, und er gehoerte der einzigen Person, die ihn je gekauft hat.

  **Der Nachname, und warum er nicht im Text steht.** Georgijs Papiere wurden in der zweiten Oktoberwoche *regularisiert*; jemand hat an einem Schreibtisch gesessen und einem Mann einen Nachnamen gegeben, damit ein Dokument haelt, und ist danach essen gegangen. **Der Text nennt ihn nicht, weil Georgij ihn nicht ablegt** - und das ist der Reim zu Kapitel 24: Vier Naechte vorher sind zwei Silben sofort an den Platz gegangen, an dem er ein Gesicht an einer Tuer und eine Zahl am Rand aufbewahrt, und dort geblieben. Dieser hier faengt sich an nichts. *"He let it go, and it was his own."*

  **Seine Unterschrift entsteht in zwei Sekunden** und wird die bleiben, die er sein Leben lang benutzt: der gedruckte Name in einer Hand ohne Schnoerkel, *"the signature of a competent man of no particular background, which is precisely what it was."*

  **Und Chae zieht eine Grenze, die spaeter zaehlt:** Es gibt eine vierte Gegenpartei, die nicht auf dem Papier steht. Wenn Annie Georgij je bittet, ihr gegenueber zu zeichnen, ist das nicht dieses Instrument, und er soll vorher anrufen. *"Would you take that call?" - "I would take that call, on a Sunday."*
- **Kapitel 24** *Have you eaten* (v1.4) - Zweite Haelfte derselben Nacht auf der Bruecke. Die Ecke bei den Garagen, der Beweis, dass er nicht fuer Geld bleibt, die drei Kippenstummel und ihr erstes echtes Lachen. Der Praezedenzfall vom Kies, die Unterschriftsvollmacht - und Georgijs eigener Einwand dagegen. Ihr Name. Die Fernbedienung in den Han. Das Halsband bleibt und bekommt seinen Grund. Im Wagen die Frage vom Gelaender.

  **Der Fehler mit der Vollmacht ist seiner, und das ist entscheidend.** Er hat den Preis verlangt, die Form gewaehlt und sie *payment* genannt; sie hat innerhalb einer Minute geliefert. Ihre Zeile *"Do not thank me for that. It is what it costs"* ist richtig - sie erkennt an, dass sie schuldet. **Eine Fassung, in der er ihr das vorwirft, ist unlogisch**, und genau die stand hier zuerst.

  Jetzt korrigiert er sich selbst, unaufgefordert und gegen den eigenen Vorteil: *"I asked you for that as payment. I chose the form, I named the price, and you agreed to it inside a minute. None of that is on you."* Das ist die Regel aus `doc/01-craft.md`: Ein Patzer bleibt ein Patzer, auch wenn er gut ausgeht, und er sagt das auch.

  **Die Vollmacht ist keine Bezahlung, und er sagt es selbst.** Er hat sie verlangt, weil er ohne sie nicht arbeiten kann - und rechnet dann nach: *"It is a better tool for your house and nothing else. You have just paid me by making me more useful to you, and I nearly took it."* Das ist der Kern der Figur: Er rechnet praezise, auch gegen den eigenen Vorteil.

  **Dann fragt sie, was er will, und er kann es nicht beantworten.** Nicht aus Bescheidenheit und nicht als Technik. Er zerlegt die Frage wie jede andere, und es gibt keine Teile. *"There is nothing there. I have looked."* Ein Junge in dem Gewerbe, der etwas will, hat jemandem gezeigt, wo man drueckt; mit neunzehn war aus der Disziplin eine Tatsache geworden.

  **Deshalb gibt sie ihm etwas, das er nicht verlangen konnte: ihren Namen.** **Zwei** Silben auf Koreanisch, in einer Stimme, die er nicht kennt. Er steht auf keinem Papier, ihre Mutter und ihr Bruder haben ihn benutzt und beide sind tot, und seit sie dreiundzwanzig ist nennt sie in diesem Land jeder Annie, einschliesslich ihres Mannes. *"You cannot spend it, you cannot sign with it, and it will not get you through a single door in Seoul. It is the only thing I have got that is not for something."* Und der Grund: *"because you gave me one on the fourth of October in the back of a car and I did not give you anything back."*

  **Zwei Silben, nicht vier. Hier stand bis zum 23.08. "vier Silben", in dieser Datei und in `doc/07-next.md`.** Der Text sagt *"something in Korean, two syllables"*. Das ist keine Kleinigkeit, sondern legt fest, **was fuer ein Name es ist**: zwei Silben sind im Koreanischen ein **Vorname** (Ji-yeon, Su-jin, Eun-hee), kein vollstaendiger. Sie hat ihm also ihren Vornamen gegeben und keinen Familiennamen, und das passt zu *"My mother used it and my brother used it and both of them are dead."*

**Wer spricht ihn, und wie oft.** **Sie**, zweimal, in dieser Szene - er bittet *"Say that again"*, und sie tut es. **Georgij nie.** Was er einmal benutzt, ist *Annie*, und zwar in **Kapitel 23** auf der Bruecke: *"So. Annie." He let the name sit there, on a bridge, at half past ten at night, for the first time.* Das ist der Regelbruch mit der englischen Anrede und hat mit dem koreanischen Namen nichts zu tun. **Wer beides verwechselt, verbraucht den koreanischen Namen, ohne ihn geschrieben zu haben.**

**Der Name lautet Hye-jin, und er steht im Text.** Kapitel 24, **genau einmal**, kursiv, **nicht in seinem Mund, sondern in seinem Kopf**: *He had a place to put a thing like that, which was the same place he put a face at a door and a number in a margin.* **Hye-jin** *went in there and stayed, and he did not take it out again for a very long time.*

**Bis zum 23.08. stand in dieser Datei und in `doc/07-next.md`, der Name sei noch nicht entschieden.** Das ist die gefaehrlichste Sorte Dokumentfehler: nicht veraltet, sondern eine Einladung, beim naechsten Mal einen zweiten Namen zu erfinden.

**Warum diese zwei Silben, und das ist eine Sperrliste fuer alles Weitere.** Gewaehlt gegen die im Buch belegten Silben: **Ji-** ist doppelt vergeben (Ji-won, Ji-hoon), ebenso **Eun-** (Eun-ju), **Min-** (Min-ho), **Seo** (Mrs Seo) und **Tae-** (Tae-min). Alles auf **-won** verbietet sich neben den Won-Betraegen, und Jae-won gibt es ausserdem schon. Und er klingt bewusst **nicht** nach *Annie*, weil Annie eine Erfindung ist und keine Uebersetzung.

**Kollision, gefunden und behoben am 23.08.:** In Kapitel 15 und 18 hiess eine der vier Konkurrenzgruppen **Hyeonjin**, was neben **Hye-jin** stand, und eine zweite **Yun**, was neben **Kim Do-yun** und dem Kuechenjungen **Yun** aus Kapitel 34 stand. **Geaendert wurden die Firmen und nicht die Menschen**, weil beide Personennamen begruendet sind und die Firmen je zweimal vorkommen. Sie heissen jetzt **Kyeongil** und **Nam**; die zwei Stellen sind Kapitel 15 (v2.7) und Kapitel 18 (v1.1). **Der Name Yun gehoert ab jetzt genau einem Menschen im Buch**, dem Jungen, und Do-yun steht immer mit beiden Silben da.

**Der Familienname ist weiterhin nicht vergeben, und das ist Absicht.** Sie hat im ganzen Buch keinen, an keiner Stelle - *"It is on nothing."* **Annie ist damit die einzige Figur ohne vollstaendigen koreanischen Namen.**

**Offen bleibt nur noch, wann er faellt**, also wann Georgij ihn ausspricht.

- **Kapitel 23** *Nobody weighs a door handle* (v3.5) - Erste Haelfte der Nacht nach dem Bruch. Eine Stunde bergab durch eine Stadt, die nach Hause geht; die Haende gehen an und wieder aus; viermal bis *Sang-hoon saw it* und nicht weiter. Kein Geld, kein Ort, kein anderes Ergebnis als zurueck vor Mitternacht. Die Mapo-Bruecke, deren Bedeutung er erst an der Schrift im Gelaender begreift. Jang im Laufschritt, der Sake aus seiner Tasche, das Einschenken mit beiden Haenden, die Ecke bei den Garagen. Dann Annie auf dem Beton, die Bruchfrage, **der Entzug der Anrede**, und ihre Antwort, die seine Lesart umwirft.

  **Der Hoehepunkt ist der Entzug der Anrede.** Auf ihr *"A man who does not break is a man nobody can hold"* kontert er mit dem, was tatsaechlich der Fall ist: **Sie hat ihn fuenfundfuenfzig Tage lang tadellos gehalten**, jeden Raum, jeden Namen, jede wache Stunde, fuer eine Unterschrift im Oktober und nichts weiter. *"So why did you go and try to waste it?"*

  Dann: **"I don't feel like calling you Mistress right now."** Und die Definition hinterher, die Kompliment und Anklage zugleich ist - *ruthless and beautiful and intelligent as hell*, jeden Tag seit dem 4. Oktober, *"and I have not had one hour of regret about who owns me. That is not a compliment. It is the reason I am still in the country."*

  **Und dann zaehlt er.** *"Tonight she was two of them."* - *Annie did not ask which.* **Ruecksichtslos war sie**, und ruecksichtslos ist bei Georgij ein Kompliment; er bewundert Haerte. Was fehlte, ist das dritte: Es war **dumm**. Sie hat ihr teuerstes Werkzeug vor einem Zeugen beschaedigt und dabei ihre eigene Regel aus Kapitel 12 gebrochen. Sie fragt nicht nach, weil sie es weiss, und ihre spaetere Antwort bestaetigt es: *"I did not weigh it."* **Eine Fassung mit "none of them" ist falsch** - sie war zwei davon, und das ist schaerfer.

  **Und in der Liste steht ein Wort, das nicht hineingehoert.** *Beautiful* hat in einer Aufzaehlung ueber Kompetenz nichts zu suchen, und er hoert es erst, als es weg ist - *"the way he had heard the other one go on a floor at the Grand Hotel"*, also derselbe Mechanismus wie das verbotene Wort gegenueber Hana in Kapitel 11. Annie wird kurz still und kommt zurueck, und er kann die Stille nicht deuten.

  **Eingeloest wird es in Kapitel 24, nach dem Wurf**, wenn nichts mehr zu verhandeln ist: *"You said beautiful." - "I did." - "In the middle of a list about whether I am any good at my work." - "Yes." - "Why?"* Seine Antwort ist der einfachste Satz des Kapitels und jedes Wort davon stimmt: **"Because it is true, and because tonight I was not selecting."** Das trifft seine ganze Methode - er waehlt aus, immer, das ist sein Verfahren; heute Abend nicht.

  Ihre Antwort: *"Do not do it again."* - *"No, Mistress."* - und dann, nach einer Pause: **"That was not an order. I do not know what it was."**

  Und dann der Name: **"So. Annie. Why in God's name did you do it?"**

  **Das ist die Waffe dieses Kapitels**, nicht der quid pro quo - den hat er in Kapitel 22 verbraucht. Und es kehrt die Regel aus Kapitel 11 um: Dort rutscht ihm das verbotene Wort gegenueber Hana heraus, hier entzieht er es ihr mit Absicht.

  **Der Bogen ist ausgezaehlt.** Nach dem Entzug faellt "Mistress" nicht mehr - nicht bei der Vollmacht, nicht bei der Bitte, nicht beim Lachen. Es kommt erst **nach dem Wurf** in Kapitel 24 zurueck, beim Halsband, und der Text markiert es: *"He heard himself do it, and so did she, and neither of them made anything of it."* Wer dazwischen ein "Mistress" einfuegt, macht den Entzug wertlos.

  **Und ihre Antwort wirft seine Lesart um.** Er glaubt, sie habe ihn nicht abgewogen - *"A man weighs the things he thinks are close to him. Nobody weighs a door handle."* Falsch, und zwar vollstaendig: *"He asked what you would cost, and for about one second I did not know the answer. Not the number. I did not know whether there was one."* Sie kennt den Preis von allem, seit sie neunzehn ist, und fand bei ihm keinen. Ihre eigene Bruchstellen-Erklaerung raeumt sie im selben Zug ab: *"That is what I told myself in the four hours afterwards, and it is a better sentence, and I have been saying it to you for twenty minutes."*

  **Damit hat Georgij sich zweimal in vier Tagen in derselben Frau geirrt**, auf Tatsachen, die er in der Hand hielt - Kapitel 20 ueber dem Schreibtisch, und hier. *"I have had it backwards twice since Friday."* - *"I know. I was there for the other one."*

- **Kapitel 22** *Not shown* (v1.1) - Sang-hoon kommt auf das Anwesen und fragt vor Annie, was Georgij kosten würde. Sie greift in die Jackentasche und bricht damit ihre eigene Regel aus Kapitel 12. Der quid pro quo fällt zum ersten Mal als Waffe. Er geht in den Garten, raucht eine von Jangs Zigaretten und über die Mauer.

  **Wo die Fernbedienung ist, und warum das zaehlt.** Sie liegt **nicht** auf der Steinablage. Der Weg ist in vier Stellen festgelegt und laeuft so:

  | Wann | Wo |
  |---|---|
  | Tag 1, ein Uhr nachts (Kap. 2) | Annie legt sie neben die Schluesselschale |
  | Tag 2 (Kap. 4) | liegt noch dort, *"where she had put it at one o'clock that morning"* |
  | **Tag 9 (Kap. 5, der Schneider)** | **weg.** Er sieht es und hebt den Blick nicht zur Kamera im Tuersturz |
  | Tag 19 (Kap. 5, Arbeitszimmer) | sie spricht ihn darauf an. *"I know," he said. "Day nine."* - *"I went back and watched you not do it nine times."* |
  | **Tag 22 (Kap. 6, Fuss der Treppe)** | sie oeffnet vor ihm die Clutch, nimmt den Lippenstift heraus und legt die Fernbedienung an dessen Stelle. Wortlos |

  Kapitel 6 bestaetigt die Frist in der ersten Zeile: *"the place the remote had lain for the first eight days he was in the house."* Der Gala-Absatz schliesst mit *"he was going to know it every minute until they came home."*

  **Seither traegt sie sie am Koerper, und er weiss es jede Minute.** Genau das macht Kapitel 22 hart: Er hat sie an dem Abend die Jacke anziehen sehen. Er wusste, wo das Ding ist, und hat es nicht gedacht. **Eine Fassung, in der er ueberrascht ist, weil das Geraet irgendwo lag, ist falsch.**
- **Kapitel 21** *The ones who come at nine* (v1.7) - Hanas Haus. Der Abend im Dezember wird gebaut: drei Wellen, die Laufordnung, der Fotograf bis neun. Kang steht auf ihrer Gaesteliste, seit neun Jahren, und Georgij kann nichts dagegen sagen, ohne zu erklaeren warum - sie sieht das Zoegern trotzdem. Sie fragt, wofuer der Abend ist, und nimmt die Frage selbst zurueck, und der Grund ist Kang. Die Rechnung dafuer stellt sie ihm noch im selben Gespraech, als das Loch in der Laufordnung auffaellt. **Der Rundgang durch das ganze Haus**, vierzig Minuten, auf seine Bitte und mit ihrer Erlaubnis - zweimal, einmal fuer das, was da ist, und einmal fuer das, was von wo nicht zu sehen ist, genau wie in Kapitel 3, nur bei Tageslicht und mit der Eigentuemerin daneben. Zwei Treppen, der Dienstflur hinter dem Esszimmer, die kaputte Lampe ueber der Stufe, das Arbeitszimmer ihres verstorbenen Vaters. **Und die vier Minuten in der Halle, die er abgeht** - drei Meter zwischen der Stelle, an der ein Ankommender wartet, und der, an der ein Gehender wartet, mit einem Steintisch dazwischen, der etwas Hohes bekommt. *"Your mother's housekeeper was arranging a party. I am arranging four minutes."* Die Terrasse als Ort fuer Ye-rin. Der Flirt in der Halle, der nicht abgewiesen, sondern ueberholt wird.

  **Kein Hanseong in diesem Kapitel, und das ist Absicht.** Eine Fassung hatte Georgij hier darum bitten lassen, das Scheingebot ueber Kang streuen zu lassen. Das ist ueberfluessig: Sang-hoon steht drei Tage nach dem Gebot selbst in Annies Salon (Kapitel 22) und redet darueber. Er weiss es aus erster Hand, lange bevor eine Dezember-Einladung herausgeht. **Damit ist Kang kein Werkzeug, sondern eine Belastung** - ein Mann, der an Sang-hoons Leute durchsticht, steht in dem Raum, in dem Woo oeffentlich neben die Kims tritt.
**Wem der Routen-Satz gehoert, festgeschrieben am 23.08.** Er wandert durch sechs Kapitel und die Herkunft war in einem davon falsch.

- **Kapitel 15, Tag 41:** **Georgij** sagt die Mechanik zuerst, an Annies Tisch mit Hana dabei, und ausfuehrlicher als Woo sie je sagen wird - vier Gruppen auf denselben zwei Lanes, Kyeongil, die Nam-Operation, *"you would be the group whose cargo was already loaded, and somebody else would do the explaining"*. Er sagt es **als Grund, es zu tun**.
- **Kapitel 19, Tag 48:** **Woo** sagt fast denselben Satz und haengt an, was Georgij nicht danebengelegt hatte: *"so that the woman who owns you ends up with her hand on the throat of everybody else in this trade."*
- **Kapitel 20** stand bis zum 23.08. auf *"He told me what that is"* und schrieb damit Woo die Mechanik zu, die Georgij eine Woche vorher **vor Annie** vorgetragen hatte. Sie war im Raum, sie haette es gewusst. Jetzt: *"He told me what it makes you"*, und Georgij sagt von sich aus dazu, wo er den Satz zuerst benutzt hat und wofuer. **Damit traegt Annies Schweigen danach etwas**, statt nur dazustehen.
- **26, 30 und 32** sind Weitergaben an neue Zuhoerer und bleiben. **31 wurde gekuerzt**: dort trug Georgij Annie eine Formel vor, die sie seit November hat. Kapitel 32 bleibt ausdruecklich woertlich, weil Sung-ho danach fragt und weil das Versprechen aus Kapitel 14 *in those words* lautet.

- **Kapitel 20** *I came back with a favour* (v1.4) - Der Bericht ueber Yeongjong, die vierzehn Meter, das gefaltete Blatt und der vierte Termin, den keiner nennt, Woos Satz ueber das Vetorecht und Annies Schweigen dazu, ihre eine Frage, und die Suche nach einem Haus.
- **Kapitel 19** *What happens on the Tuesday* (v1.9) - Yeongjong. Die vierzehn Meter, Woo nennt seinen eigenen Preis und bekommt ihn unterschrieben, der leere Tarif, "Can you fill it?", die drei Daten und ein Mittwoch im September, und was er sich selbst dabei ausrechnet.
- **Kapitel 18** *On account* (v2.6) - Die neunzehn Seiten kommen zurueck, vier Bleistiftnotizen, die Abschlagszahlung, die Uhr auf vierzehn Tage, und im Arbeitszimmer zwei Bitten: das Scheingebot auf Hanseong und zehn Jahre Ladung fuer Woos Terminal.
- **Kapitel 17** *I have never put it down* (v12.10) - Der Bericht auf der Schnellstraße, die Angst als billigste Ware, die Falle im Vorstand, Hanas Belastungen, die Abtrennung, die festgelegte Zeile, ihre Antwort an der Flurkreuzung.
- **Kapitel 16** *Where the walls are* (v1.16) - Das Essen mit Sang-hoon, die vier Wände, der Biss über dem Gespräch über die Decke, das best-made thing.
- **Kapitel 15** *Four thousand two hundred* (v2.7) - Das Essen zu dritt, Ye-rin, das Vetorecht, der Mietvorvertrag, die viertausendzweihundert.
- **Kapitel 14** *In the same size type* (v7.6) - Die Gesichter, der Irrtum über Do-yun, Hanseong, der Plan in drei Teilen, das erste Lächeln.
- **Kapitel 13** *The man with the open hand* (v2.5) - Das Ja ohne Bedingung, der Mietwagen und das vierte Datum, das Essen mit Woo.
- **Kapitel 12** *You are better when you don't know* (v1.7) - Jangs Bericht und der vierte Wagen, Kangs Anruf, Annies Bitte.
- **Kapitel 11** *Thank you for telling me* (v2.8) - Die Heimfahrt, vollständige Offenlegung, der gemeldete Regelbruch, die Namensfrage.
- **Kapitel 10** *What did she pay for you* (v2.5) - Woos Einladung und die abgewiesene Frage, Kang und der zweite Griff, der Blickwechsel, Sang-hoon am Tisch.
- **Kapitel 9** *The friendly ones* (v3.3) - Hana, die Terrasse mit Min-ho, Kang an den Türen, die dreifache Frage, der Handkuss, der Ausrutscher.
- **Kapitel 8** *Something to do with my hands* (v3.5) - Das Glas, die Frau von der Stiftung, die zwei Direktoren und der Name aus Busan, Woos Prüfung, die Frau in Dunkelrot, die Versteigerung.
- **Kapitel 7** *Where were you educated* (v6.5) - Die Fahrt, die Ankunft, die ersten fünfzehn Minuten, die Legende, der Schnitt.
- **Kapitel 6** *Withdrawn or sold* (v1.6) - Der Katalog ohne den Jungen, die drei aus dem Keller, der Kragen, Jang vor dem Abend, Mrs Seo, die Fernbedienung in die Clutch.
- **Kapitel 5** *Seven Letters* (v5.10) - Vier datierte Szenen, darunter die Inventur des Haushalts an Tag sechs: Jang an Tag vier, der Schneider an Tag neun samt verschwundener Fernbedienung, die Datei auf ihrem Rechner an Tag neunzehn.
- **Kapitel 4** *Count again* (v1.9) - Der erste Morgen, die Küche, Laptop und Telefon, die verweigerte Gästeliste, die zwei fehlenden Kameras, Los elf.
- **Kapitel 3** *Dead angles* (v2.7) - Mrs Seo, Ji-won, Bae, die Inspektion, die Kamerawinkel, "There are no exits" und seine vier.

#### Band 2

**Die Zeilen tragen hier einen Bandpraefix**, weil die Nummern von vorne
anfangen. `check.py` liest beide Formen; ohne Praefix ist Band 1 gemeint.

- **Band 2, Kapitel 1** *Nothing to sign with* (v1.4) - **Tag 150, Mo 2. Maerz, der Tag nach dem Schluss von Band 1. Ein Tag, drei Szenen.**

  **Der Einfall, und die zwei Fristen laufen einen Tag auseinander.** Annies Sperre (*"nothing for you between now and March"*) endet, als Maerz anfaengt, also am **Sonntag**, dem 1. Maerz - und dessen Ende hat er auf dem Boden am Fenster verbracht, an ihren Beinen, ohne einmal daran zu denken. Die Vollmacht stirbt am Ende desselben Sonntags um Mitternacht. **Erst der Montag ist der Tag, an dem er wieder anfaengt**, und er zieht in zwei Richtungen: *"So on the Monday he was permitted to work and had nothing to work with."*

  **Hier stand bis zum 23.08. "um dieselbe Mitternacht", und das war falsch.** Zwei Fristen mit verschiedenen Enden waren zu einer zusammengezogen, und dabei ging der beste Teil verloren: dass sein erster freier Arbeitstag ihr gehoert hat und er es nicht bemerkt hat.

  **Der Morgen.** Haushaltstextur, die seit Kapitel 13 fehlt. **Yun**, der Kuechenjunge seit der ersten Januarwoche, ist acht Wochen da und traegt die Teller inzwischen in den Haenden statt auf den Unterarmen. Er gruesst Georgij jeden Morgen, was ihm niemand gesagt hat und was zwei der vier Maedchen bis heute nicht tun. Georgij steht zum dritten Montag hintereinander frueh genug auf, um jemand anderem bei der Arbeit zuzusehen.

  **Die Bitte, und die Szene haengt an einem Satz aus Kapitel 24.** Er haelt sein Versprechen woertlich - *"a date on it, after which it is dead and I ask you again."* Annie fragt **"What for."**, und am 2. Maerz liegt nichts an. Er nennt die einzige Ausfuehrung vom 23. Januar. **Annies Gegenzug ist vernichtend und richtig: dann gebe ich eine an Mrs Seo** - neun Jahre im Haus, fuehrt Personal, Konten und Fremdfirmen, ist abends ohnehin im Gebaeude, und eine solche Vollmacht laeuft nie ab.

  **Dann gibt sie ihm seinen eigenen Satz zurueck.** Aus Kapitel 19, im Schuppen in Yeongjong an Woo: *"I have nothing to sign with, and that is not modesty. It is the arrangement."* Ihre Antwort darauf ist **"There is no arrangement."** Der Satz war laut `doc/07-next.md` ab Dezember verboten, weil er unwahr geworden war; **seit dem 1. Maerz um Mitternacht stimmt er wieder, und das Verbot ist mit dem Instrument abgelaufen.** Was nicht zurueckkommt, ist die zweite Haelfte.

  **Und damit steht da, worum er wirklich bittet.** Die Papiere vom Oktober tragen seinen Namen und nicht ihren. Das Registerblatt trug ihren und nicht seinen, weil es dafuer keine Spalte gibt. *"The instrument that died at midnight had both. It is the only thing that ever has."* **Sie gibt sie ihm nicht**, und ihre Begruendung ist geschaeftlich: Mr Chae schreibt auf, wofuer ein Instrument da ist, und das hier geht in keine Aktentasche. *"Then ask me again when there is a room in it."*

  **Beim Hinausgehen bleibt sie an der Tuer stehen**, was sie am 2. Januar nicht getan hat, und gibt ihm die zehn Wochen zurueck: *"Nobody has told you what to want."* Das ist ihr Prinzip aus Kapitel 4, zum ersten Mal als Freigabe.

  **Der Katalog. Derselbe Gegenstand wie in Kapitel 6, und aufgeraeumt.** In Kapitel 6 gilt: *"They renumber every month, so the numbers meant nothing."* Jetzt steht in sechs Punkt unter der ersten Seite: *"References are permanent and are not reissued. Withdrawn and completed entries retain their reference."* Er liest ihn zum ersten Mal **in der Hand** statt auf dem Kopf.

  **Die Seite hinten ist der Anschlag.** Eine Liste ueber vier Jahre: Referenz, Saison, ein Wort. *Completed*, *Withdrawn* - und bei vieren drei Woerter statt einem: **"Retained, not disclosed."** Darunter **elf und vierzehn, vier Zeilen auseinander, mit denselben drei Woertern.** Vier in vier Jahren, zwei davon sind ihre.

  **Die Umkehrung, auf der Band 2 steht:** *"The line was struck on the nineteenth of February. The striking of it is now the most durable thing about it."* Annies Gnade ist die Spur.

  **Der erste Auftritt des Sanierers ist eine Unterschrift unter einer Vorschrift ueber Aktenfuehrung** - vier Saetze, alle ueber Methode, und in keinem ein Wort darueber, worauf die Referenzen verweisen. Georgijs Kinn tut, was es bei Arbeit tut, die besser ist als noetig, und niemand ist im Raum.

  **Und die vierte Vorenthaltung faengt auf Seite eins an.** Auf *"Did you meet him?"* sagt Annie **"Ask me something else."** Sie war viermal in dem Gebaeude.

  **Der Schluss** holt den Titel zurueck: Er hatte Woo im November gesagt, er habe nichts zu zeichnen, und das sei keine Bescheidenheit, sondern die Abmachung. *"It was the first evening on which only the first half of that was true."*

- **Band 2, Kapitel 2** *The order of loading* (v1.0) - **Tag 152, Mi 4. Maerz. Zwei Szenen: Shins Hof in Gimpo, dann das Haus am Abend.**

  **Die Regel dahinter ist `doc/01-craft.md` 2h.** Er laeuft nicht mit stumpfem Werkzeug hinein und scheitert. Er steht drei Sekunden in dem Hof und **legt alle vier Eroeffnungen ab**, bevor er den Mund aufmacht. Drei sind fuer Raeume, in denen der andere noch entscheidet, was Georgij ist; Shin entscheidet gar nichts, er hat vier Lastwagen und seit fuenf Wochen keine Ladung. Die vierte ist die Frage nach dem, vor dem man sich hueten soll, und die gehoert einem Neuling.

  **Der Grund ist nicht Beruehmtheit, sondern Arithmetik:** *"You cannot take anything from a man who has nothing. You can only pay him."* Ein Spediteur mit neun Lastwagen liest keine Wirtschaftspresse und weiss nicht, wer Georgij ist. Er hat nur nichts mehr, woraus man etwas herausschmeicheln koennte.

  **Womit er bezahlt, ist das, was Annie weggewischt hat.** Die vier Zeilen ueber Gimpo, die sie im Januar umgedreht und nie erwaehnt hat. Shin hat **Daehan** Ende Januar verloren und haelt sich seit fuenf Wochen selbst dafuer verantwortlich; in Wahrheit hat der Versicherer des Kunden im August eine Zeile ueber Traegerkonzentration umgeschrieben, und ab dem 1. Januar darf oberhalb einer Tonnage nur noch **ein** benannter Spediteur fahren. Shin liegt darunter. *"Nobody at your size in this country kept that contract this year, and the man who took it off you is not better at this than you are."* Dazu die Seite aus der Meldung des Kunden - Kanon aus `doc/04-world.md`: Georgij liest die Meldungen der Kunden, nicht die Vertraege.

  **Was es ihn kostet, sagt er Annie selbst:** Es ist oeffentlich, es kostet sie nichts, und es gibt vielleicht vier Leute im Land, die es nachgelesen haetten. *"That is the part that cost something. He will repeat it, and he will repeat where he had it."*

  **Der teuerste Satz des Kapitels ist einer, den er nicht sagt.** Shin hat im Februar zwei Maenner entlassen und ihnen die zwei Ladungen vom Oktober als Grund genannt. Georgij sagt ihm nicht, dass er jetzt hingehen und etwas anderes sagen kann - *"saying it out loud would have been the second thing given and the first thing taken."*

  **Und dann kommt, wofuer das Kapitel da ist: das Vetorecht von unten.** Shin steht seit zwoelf Jahren zweimal die Woche am Tor in Incheon. *"What's different since January is that the waiting has a shape to it. Same name goes on first. Every sailing."* Dazu **der Mann aus Ulsan** - Chemie, eine Lane, sonst nichts -, dessen Kisten seit Mitte Januar zweimal stehengeblieben sind und der jetzt Dienstagnacht in der Fahrerkabine am Tor schlaeft, damit er morgens als Erster durchkommt. *"Being first through that gate has got nothing whatever to do with what goes on the ship. He knows that. He does it anyway."*

  **Damit ist der Satz aus `doc/04-world.md` eingeloest**, der seit November darauf gewartet hat: *"Er wird das irgendwann zu Ende denken."* Georgij erkennt im Hof seine eigene Handschrift im Wetter. Er hat den Mechanismus im November an Annies Tisch vorgetragen, **als Grund, es zu tun**, und war zufrieden damit, wie sauber der Satz war. *"A man sleeps in a cab now, on the strength of it."*

  **Choi kommt nicht vor, und das ist die Entscheidung des Kapitels.** Eine erste Fassung liess Shin von einem frueheren Besucher erzaehlen, der selbst gefahren war, nichts angefasst und keinen Namen hinterlassen hatte - also genau die Form, die Georgijs Verfahren nicht sieht. **Das haette Annies Vorenthaltung am dritten Tag entwertet**, denn wer die Form kennt, verhaelt sich korrekt darum herum, und korrektes Verhalten ist laut Kapitel 12 die Unterschrift. Choi bleibt draussen, bis sie es entscheidet oder bis es Georgij etwas kostet.

  **Am Abend behandelt Annie die drei Dinge verschieden, und das ist die zweite Szene.** Die zwei Auftragspunkte nimmt sie in unter einer Minute. Zu der Bezahlung sagt sie **nichts** - nicht ja, nicht nein - und geht mit *"What else."* weiter. Ulsan nimmt sie im Sitzen und mit sechs Fragen, von denen er zwei nicht beantworten kann; die zweite davon ist **"whether anybody had gone to him yet"**.

  **Ihr Auftrag am Schluss:** den Mann aus Ulsan namentlich, **nicht** ueber Shin, sondern aus den Meldungen und dann von jemandem, der selbst an dem Tor gestanden hat. Dazu ihre Prognose ohne Eile: *"They are all four of them worth having, and two of them will be gone by June."*

  **Der Schluss zaehlt die zweite Nichtantwort.** *"That was the second time in two days that a question he had put down in front of her had been stepped over rather than answered, and the first time had been about a name."* Und die Bilanz: Gestern hat er um ein Papier gebeten, das sagt, was er darf, und keines bekommen; heute hat er ohne Papier etwas von ihr verschenkt, hatte recht, und sie hat es stehenlassen. **Er geht die Osttreppe hinauf und zaehlt die Stufen nicht** - in Kapitel 34 hat er sie gezaehlt und zweiundzwanzig bekommen, was er seit Oktober wusste.

- **Band 2, Kapitel 3** *We haven't met* (v1.0) - **Tag 155, Sa 7. Maerz. Drei Tage Aktenarbeit, rueckblickend erzaehlt, dann der Abend.**

  **Niemand hat ihn darum gebeten, und das ist der erste Satz.** Ulsan war am Donnerstag um vier fertig. Was er mit den restlichen drei Tagen macht, entscheidet er selbst - und er beruft sich dabei auf ihren eigenen Satz vom Montag: *"Nobody has told you what to want."* **Sie hat es als Freigabe gemeint. Er nimmt es als eine, und er weiss, dass sie das nicht gemeint hat.** Dazu die Uebertretung in Fingernagelgroesse: Er nimmt den Katalog vom Schreibtisch im kleinen Zimmer mit nach oben, **das erste Ding, das er je aus diesem Raum genommen hat, ohne dass es ihm gereicht wurde.**

  **Das Verfahren ist das aus Kapitel 7, zum zweiten Mal.** Er geht nicht ans Haus, er geht an **das Aussenherum eines Abends**: Fahrdienst, Blumen, Stuhlverleih, Abrechnungslaeufer. Vierhundertdreissig Namen kamen im Oktober aus einem Fahrdienst, einem Floristen und einer Korkgeldrechnung, und Choi Dae-ho war nicht darunter.

  **Es funktioniert, und es funktioniert ueber Fahrtenzettel.** Eine Firma in Jung-gu hebt ihre Dockets sieben Jahre auf, wegen eines verlorenen Steuerstreits. Vier Fahrten auf dieselbe Strasse in drei Jahren sind ein Kunde. Dahinter eine Briefkastenfirma, zwei Zimmer und eine Sekretaerin, schlecht gebaut - *"whoever set it up had not been trying very hard, which by itself said something."*

  **Und dahinter steht Mrs Sunwoo.** Entschieden am 23.08. Sie ist **nicht neu erfunden**: Kapitel 1 sagt, dass an dem Abend, an dem Georgij verkauft wird, ein Laeufer der Abrechnung **zu der Dame an der Saeule** heruntergeht - sie hat in diesem Raum gekauft. Kapitel 7 laesst sie ihm die Hand geben mit *"We haven't met."* **Ihr eigener Eintrag ist aelter**, drei Jahre zurueck, und der Kauf vom 4. Oktober gehoert nicht dazu; sie ist Stammkundin.

  **Damit dreht sich eine Szene aus Kapitel 7 um.** Er hielt die vier Woerter fuer eine Hoeflichkeit. Sie waren eine Pruefung: **ob der Neue am Tisch weiss, was sie ist.** Er hat ihr mit dem Gesicht geantwortet, dass er es nicht weiss, und sie ist zufrieden weggegangen. *"He worked out on Saturday afternoon what she had actually been doing, and it took him under a minute once he stopped being flattered."*

  **Was er nicht hat, ist die Zeile selbst.** Eine Referenz, eine Saison und ein Federstrich. Wer dort stand, steht nirgends. **Und das Motiv aus Kapitel 6 kommt veraendert wieder:** dort war es *withdrawn or sold*, hier ist es *"There are two reasons a person pays for that, and one of them is the reason Annie had. From the outside of an evening they look exactly alike."*

  **Der vierte Abend hat kein Papier.** Kein Wagen bestellt, niemand verkoestigt, nur Stuhlverleih und Blumen fuer den Raum. Georgij geht ihn zweimal an, legt ihn hin und notiert sich als Grund **das Alter der Unterlagen, was vernuenftig ist.** Der Leser, der Kapitel 7 kennt, weiss, was ein leeres Ergebnis bedeutet. **Georgij nicht**, und er darf es hier nicht wissen - siehe `doc/07-next.md`.

  **Und der Fund ist die falsche Haelfte.** Abschreckung braucht jemanden, der so gross ist, dass die Seite unbenutzbar wird. *"A page with Annie on it and a woman of eighty-one on it is a page with two people on it who can both be hurt, and that is not a deadlock, that is a queue."*

  **Er geht Mrs Sunwoo nicht an**, und die Begruendung ist Hanas Regel von einer anderen Frau, die niemanden empfaengt: **Not quickly and not twice.** Eine Frau, die seit vierzig Jahren vorsichtig ist, wird einmal gewarnt, und danach ist sie vorsichtig in Bezug auf **eine bestimmte Sache** statt in Bezug auf alles, was schlimmer ist. Dazu: Er hat nichts, was sie will.

  **Abends Ulsan, und Annies vierte Frage ist die gefaehrliche.** Nam Byung-hee hat die Firma seit dem Tod ihres Bruders, dazu den Vorsitz des Verbands der unabhaengigen Verlader - sechs Firmen, und sie schreibt ihnen **am Ersten jedes Monats**, ob es etwas zu schreiben gibt oder nicht. Die letzten drei Briefe sagen nichts und sind trotzdem abgegangen. Annies Schluss: *"Then she is not somebody who is going to be told to be patient."* Die vierte Frage lautet, ob Nam je etwas ausserhalb dieses Gewerbes gehalten hat, die Antwort ist nein, und **Annie legt bei der Antwort die Hand flach auf die Lehne.**

  **Dann die Umkehrung, und sie ist der Kern des Kapitels.** Auf *"What have you been doing since Thursday afternoon."* laesst er **nichts weg** - er verweigert offen: *"Something of my own. I will tell you, and I am not going to tell you tonight."* Auf ihre Nachfrage bindet er sich dreifach: nicht heute, am Tag an dem es kostet bekommst Du alles, und **wenn Du jetzt fragst, sage ich es Dir jetzt.**

  **Der Unterschied zwischen den beiden steht damit fest und ist der Schluss des Kapitels: Georgij haelt mit Frist zurueck, Annie ohne.** *"In eight days she had stepped over two of his questions and had not put a date on either."* Und die letzte Bewegung ist ihre Hand im Nacken auf dem Weg vorbei, wie zweimal im Februar.

  **Das letzte Wort ist eines, das er selbst nicht bemerkt hat, bis es heraus war.** *"Belongs. On the seventh of March, by a man with no line, no owner and no date anywhere in the world. He did not correct it."*

- **Band 2, Kapitel 4** *I have nothing to put in it* (v1.3) - **Tag 159, Mi 11. Maerz. Eine Trauerfeier, ein Korridor, und die Heimfahrt.**

  **Er sucht nicht den Mann, er sucht den Kalender.** *"A man with thirty-one years in a trade that size is on a schedule whether he likes it or not, and most of it is private and about four days of it a year are not."* Startbahnen, Uebergaben, fremde Terminaleroeffnungen - **und Trauerfeiern, weil die angekuendigt werden und jeder kommen darf.** Er findet eine am Sonntagabend in zwanzig Minuten. Der Tote ist ein Mann aus Mokpo, sechsundsiebzig, den er nie getroffen hat.

  **Warum kein Brief und kein Mittelsmann:** *"Then you would have had a day to decide what I wanted."* Do-yun wird ausdruecklich nicht benutzt.

  **Und er entschuldigt sich nirgends dafuer, einen fremden Toten zu benutzen.** Die erste Fassung hatte an zwei Stellen genau das - *"did not intend to say any of them to anybody"* im Erzaehler und *"because I have no business having them"* im Dialog. Beides ist `doc/01-craft.md` 2b: **ein Verdienst aus einer Unterlassung, die nichts kostet**, und im Dialog zusaetzlich eine Haltung, die angekuendigt statt vollzogen wird. Es steht jetzt kalt da: *"at the end of it he knew four true things about a man he was going to use"* und *"I read four things about him on Sunday night and came here on the strength of them."*

  **Der Eintrittspreis wird bezahlt, bevor Sang-hoon ueberhaupt auftaucht, und er ist Regel 2.** An der Tuer liegt ein Buch, in das jeder Besucher seinen Namen schreibt, daneben der Kasten fuer den Umschlag, und der Betrag kommt spaeter in die zweite Spalte. **Georgij hat nichts.** Er schreibt trotzdem seinen Namen und sagt es dem Mann am Tisch: **"I have nothing to put in it."** Auf dessen *"That is all right"* antwortet er *"It is not"* und laesst die Zeile durchstreichen, damit niemand es fuer ein Versehen haelt.

  **Das ist die nackteste Stelle des Buches gegenueber einem Fremden**, und sie steht in einer Warteschlange. Dazu die Rechnung, die der Text nur legt und nicht ausspricht: Sein Name steht seit Oktober auf Papieren darueber, was er **tun darf**, und seit dem 19. Februar auf nichts darueber, was er **ist**. *"This was a book with a name in it and nothing else next to it."*

  **Sang-hoon kommt von selbst herueber**, was der ganze Grund war, warum es ein Raum sein musste und kein Telefon. Er faengt an, wo er aufgehoert hat: *"Two billion two hundred million. ... I have moved up. Say a number."*

  **Und da faellt die Zeile, die seit Dezember bereitliegt:** *"He was never for sale. Five words. They were hers and not mine, and I was in the room when she said them."* **Er war es**, Kapitel 33: Sang-hoon steht am Fenster, Annies Antwort nimmt fuenf Woerter, Georgij steht daneben. *(In der ersten Fassung stand hier "and I was not in the room". Das war schlicht unwahr, und zwar aus seinem Mund - der teuerste Regelbruch, den dieses Buch kennt.)*

  **Und dann bedankt er sich, aber nicht fuer die Zahl.** Sang-hoon hat am 29. Dezember nicht nur geboten, er hat einen Grund dazu genannt, und der Grund war etwas, das er Georgij hatte tun sehen. *"It is the only compliment anybody has ever paid me that arrived with a number on it. I have thought about that more than is useful. And I would sooner have had it from you than from anybody in this country."* **Ein Mann, der nichts besitzt, misst Achtung in der einzigen Einheit, die je auf ihn angewandt wurde.** Sang-hoons Antwort davor ist seine Selbstauskunft: *"I do not pay what a thing is worth. I pay what it costs to stop having to think about it."*

  **Sang-hoon weiss, dass die Zeile gestrichen ist, und sagt es nicht.** Es geht ihm eine Viertelsekunde uebers Gesicht und bleibt seins. **Georgij schliesst darauf, er weiss es nicht** - der Erzaehler weiss hier ausdruecklich nicht mehr als er.

  **Die Bitte ist eine Schlussfolgerung, keine Frage:** *"You will have had somebody look in a book for you, in a building near the river. A man who puts a figure on a thing and does not move off it from December to March has been at the paper on it. I do not want what was on the page. I want to know how you got the look."*

  **Was er bekommt: die Tuer, und dass sie zugeht.** *"It is there. It is not going to be there in a month."* Der Weg ist **Settlement** - *"the only desk in the building that touches every line and gets paid the least for it"* - und der neue Mann ist bereits durch den Raum und durch die Leute gegangen. **Damit laeuft eine zweite Uhr neben Nams.** Den Namen sagt Sang-hoon nicht im Korridor, sondern unten am Wagen, und er passt in eine Zeile.

  **Der Preis ist die vollstaendige Auskunft ueber Hanseong**, und die Frage ist praeziser, als sie in der ersten Fassung war. **"Warum ich" ist kein Raetsel** - Sang-hoon wollte die Kim-Logistik, Annie brauchte sie, und das weiss er seit Dezember. Georgij sagt es ihm auch so: *"If you had been after a chemical works I would have gone and found you a chemical works."*

  **Was er nicht hat, ist warum ER unterschrieben hat.** *"I saw the wall. I asked you about it out loud, at your table, and then I signed."* Das ist die Frage, ueber der er seit zweieinhalb Monaten sitzt, und nur der Mann, der die Falle gebaut hat, kann sie beantworten.

  **Die Antwort in drei Schritten.** Erstens: Er haette Hanseong von jedem gekauft - Routen, billig, blutend, halber Vorstand unterschriftsbereit. *"That is your trade, and it is the only reason the thing could be used at all."* Zweitens: Als **Angebot** haette er den zerstrittenen Vorstand gesehen und waere gegangen. Drittens, und das ist der Mechanismus: *"You told me that when you take hold of a thing you do not put it down. ... It is also the only part of you that can be aimed. Everything else is judgement, and judgement will not go where a stranger points it."*

  **Also lag es nicht als Gelegenheit auf dem Tisch, sondern als Bitte um Korrektur** - neunzehn wahre Seiten und die Frage, ob das Ganze Unsinn sei.

  **Und hier haengt die Szene an Kapitel 18, nicht an einer Erfindung.** Auf Sang-hoons *"It was you being wrong"* antwortet Georgij mit der Fundstelle: **Seite neun.** Zwei Geruechte ueber fehlendes Geld bei einer Tochter, von einem Schiffsagenten und von einer Pruefenden, die einander nicht kennen - **ein Mund, zweimal gezaehlt.** Sang-hoons Bleistift dazu: **"Same."** Und Georgij gibt zu: *"I received it at both ends and counted it twice, and I was pleased with myself for four days."*

  **Damit haelt Regel 1, und zwar an der schwierigsten Stelle des ganzen Manoevers.** Er hat nicht vorgetaeuscht, falsch zu liegen. *"It was a real mistake and I did not know it was there. I did not need to know. I needed the nineteen pages to be true and the asking to be genuine, and both of those were."*

  **Und der Kaufgrund am Ende:** Sang-hoon fand vier Fehler, alle in Bleistift, und las neunzehn Seiten zweimal, um sie zu finden - *"drei Woerter und eine Zahl"*, Kapitel 18. *"You had it won by page eleven, and there was nothing to show for it except three words and a figure in a margin. A man like you does not leave a thing won and unpaid."* Und: *"You were not valuing an asset when you signed. You had finished the argument two weeks earlier and you were putting the last word on it, and the last word cost several hundred billion won."*

  **Und Georgij gibt den unangenehmen Teil mit:** *"I stayed for the other two hours and fifty because it was the best thing anybody has ever told me about this trade, and I was enjoying it. I want that said, because it is the part I am least comfortable with."*

  **Sang-hoons Antwort darauf ist die beste Zeile, die er im Buch bekommt:** *"I would do the three and a half hours again. With you, next week, if you asked. That is not a man who has learned something. That is a man who found out what he is."*

  **Am Wagen noch ein Angebot, und es ist konkret und nicht stimmungsvoll.** Kein Brief, kein Mittelsmann, kein Gefallen, den man erbitten muesste: *"Four or five of these a year, until I am the one in the room. You will not have to write to anybody. You will not have to ask a man for a favour or stand in an office and be looked at. You come and stand in a corridor, and I will come over."* **Das ist genau das, was Georgij heute getan hat**, und es ist an einen Mann gerichtet, der nichts besitzt und niemanden um etwas bitten kann. Sein Grund: *"I have wanted to buy you twice and been told no twice, and both times I went home and thought about the work and not about the price."* Einmal gesagt, dann nicht mehr erwaehnt - *"A man should say a thing like that once and then not go on about it."*

  **Der Schluss ist die Falle, die er sich selbst gestellt hat.** Jang steht auf dem Kies, was er nicht tut, und weiss seit halb zehn, wo der Wagen war - eine solche Halle veroeffentlicht Raumnummer und drei Tage. **Annie hat es zuerst.** Und Georgij hat am Samstag gesagt: *am Tag, an dem es zu kosten anfaengt, bekommst Du alles an dem Tag.* Er wollte es sagen, sie wusste es vorher, und **die Reihenfolge kann er nicht beweisen.** *"The trouble with a man who has never said anything untrue is that he has also never had to be believed."* Letzte Zeile des Kapitels: **"Take the coat off," said Annie.**

- **Band 2, Kapitel 5** *The east side* (v1.5) - **Tag 159, Mi 11. Maerz, abends. Eine Szene, das kleine Zimmer, unmittelbar an das Ende von Kapitel 4 anschliessend.**

  **Der Einstieg ist die Falle aus Kapitel 4, und er raeumt sie selbst ab.** Er sagt zuerst, was er nicht beweisen kann: Jang stand auf dem Kies, sie hatte es vor ihm. *"There is no way for me to show you which of us was going to say it first. ... I would only be asking you to take my word for the one thing my word is no good for."* Annies Antwort setzt das Thema: **"The order is not what is wrong with today."**

  **Was Annie NICHT vorgeworfen wird, und das war die erste Fassung.** Sie hat die Zeile im Februar selbst streichen lassen und weiss genau, worueber sie nachverfolgbar ist. Ihn darueber zu belehren waere Unsinn. **Die Frage ist, warum sie seit Februar nichts getan hat**, und die Antwort ist die Architektur des Bandes: *"There is no move available to me that does not confirm the line matters, and there is no man available to me who is not visibly out of this house."*

  **Der Vorwurf ist Kapitel 27, umgedreht.** Georgij verteidigt sich mit ihrer eigenen Methode und benennt sie beim Namen: In Kapitel 27 wurde nicht die Drohung von Hana genommen - das kann niemand - sondern **das, was sie bedrohbar machte.** *"The ground stopped being a dedication and started being a rent, and the third charge on it stopped being a cliff in the spring and became a line in a schedule."* Annies Wort dafuer, und der Titel: **"The east side."** Angewendet auf das Register: vier Zeilen, alle vier langweilig, *"not worth the postage"*.

  **Und warum er nicht fragen durfte, nicht konnte:** *"The one thing in this that has any value at all is that nobody sent me. ... You are the one person alive who cannot touch that book."*

  **Der Fehler in seinem eigenen Argument, den sie ihn aussprechen laesst:** *"I am the line."* Eine Seite mit vier stumpfen Zeilen ist nichts wert; eine Seite, an der ein Mann aus ihrem Haus haengt, der seit Maerz danach fragt, ist sehr viel wert - **und zwar wegen des Fragens.**

  **Und dann die zweite Haelfte, die ihm gehoert und nicht ihr, und die in drei Fassungen falsch dastand.** Sie ergibt sich aus `doc/04-world.md`: seit dem 19. Februar ist der Eintrag **gestrichen**. Wer ihn ansieht, liest Besitz und fasst ihn nicht an; **wer nachschlaegt, findet nichts** - und dann steht *"a man who belongs to nobody is stock"*. Das Halsband ist ein **Zeichen ohne Deckung**. *"I have been doing all of this wearing a mark that is empty. Every man in that corridor read it and left me alone. Not one of them has looked."* - **"And this afternoon."** - *"This afternoon I made thirteen of them curious about the one book that would tell them there is nothing behind it."*

  **Die drei gescheiterten Fassungen, weil der Fehler jedes Mal eine Ebene tiefer sass.** Erstens *"an instrument that only exists if I am not yours"*: logisch richtig, aber drei Verneinungen dicht hintereinander, und *instrument* ist im Buch die Vollmacht. Zweitens *"Somebody owns me"*: schickt den Leser aufs Papier. Drittens *"nobody can place"*: naeher dran, aber immer noch die falsche Gefahr. **Die Gefahr ist nicht, dass jemand herausfindet, dass er ihr gehoert. Die Gefahr ist, dass jemand herausfindet, dass er es nicht tut.**

  **Daraus folgt auch, welche Option er weglegt, und die erste Fassung hatte die verkehrte.** *Freilassen* ist sinnlos - er ist auf dem Papier bereits frei. Die Option ist die umgekehrte: **sich wieder eintragen zu lassen.** *"A mark with something behind it works on everybody. A mark with nothing behind it works until one man checks."* - **"And."** - *"And it costs your name on a live page to do it."* Er legt also seinen eigenen Schutz hin, um sie nicht auf eine lebende Seite zu setzen, und sagt an keiner Stelle, dass er das tut. Sie geht darauf mit keinem Wort ein.

  **Was Annie tatsaechlich boese macht, und es ist ein Eigentumsdelikt.** Zwei Ausgaben an einem Nachmittag, beide von derselben Sache - seiner Unsichtbarkeit - und beide von ihm allein bepreist. Erstens Sang-hoon, der jetzt weiss, dass dieses Haus sich fuer ein Buch am Fluss interessiert. Zweitens **das Kondolenzbuch**: sein Name, mit Datum, an der Tuer eines Raumes mit dem halben Gewerbe darin, und dann die Bitte um den Strich, die ihn fuer jeden in Hoerweite merkbar macht. **Regel 2 dreht sich zum ersten Mal gegen ihn.** Er besitzt nichts - bisher war das seine Freiheit, hier ist es die Anklage.

  **Seine Begruendung fuer den Strich ist richtig und sie sagt es:** Ein Umschlag waere eine Zahl neben seinem Namen gewesen, in Tinte, mit Datum, aus fremdem Geld. *"A line through it is nothing at all."* - **"That part is correct. It is the only part of today that is."** Und ganz am Schluss, einmal und nicht wiederholt: *"That was the correct thing to do and it was quick, and nobody taught you it. I will not say that twice, and you are not to build anything on it."*

  **Yeouido, und der Preis der Antwort.** Ihre Leute koennen es besser, und er sagt das auch. Sein Gegenargument ist das einzige, das ihn etwas kostet: *"Every one of them arrives from somewhere. ... Nobody comes over to them in a corridor."* Annie zieht die Folge, er bestaetigt sie ohne Ausweichen. **"So the asset is that other men want you."** - *"Yes, Mistress."* - **"That is a filthy thing to have to put in a report."**

  **Die Vollmacht kommt, aber als Deckel und nicht als Belohnung**, und Annie benutzt dafuer sein eigenes Verfahren: **Deckel, benannte Gegenparteien, Frist.** Der Deckel ist, dass er den Preis vorher nennt und nicht das Ergebnis zuerst. Gegenparteien sind Sang-hoon und der Schreibtisch im Settlement, sonst niemand. Frist ist der **31. Maerz**, weil dann die Tuer zufaellt. Mr Chae hat das Papier **seit Montagnachmittag** - sie hat es am Tag der Absage aufsetzen lassen und gewartet, bis es einen Raum dafuer gab. *"I am not giving you this because you have earned it this afternoon. Some of this afternoon was very expensive."* - *"I know what it cost."* - *"You do not yet. You will in about a month."* **Dieser letzte Satz ist eine Schuld mit Frist und steht als solche in `doc/07-next.md` unter "Faelliges mit Datum": faellig Anfang April, im selben Fenster wie Nams Brief vom Ersten. Annie weiss hier etwas, das er nicht weiss, und sie darf nicht geraten haben.**

  **Die vierte Zeile, und Annie fragt nicht nach.** *"Annie asks second questions."* Sie stellt keine, und er legt die Antwort dorthin, wo er sie hinlegt. Das haelt Chois Vorenthaltung offen, ohne die Bauform von Kapitel 3 zu wiederholen.

  **Der Schluss ist koerperlich und ohne Preis.** Er geht um den Schreibtisch und auf den Teppich, *"which has stopped needing a word between them"*, und ihre Hand bleibt diesmal liegen. Und die Zeile, die auf der Treppe faellt: **Sie hat ihn nicht gefragt, ob er es ihr gesagt haette, wenn Jang in der Kueche gewesen waere.** Sie hat entschieden, es nicht herauszufinden.

- **Band 2, Kapitel 6** *I have to ask* (v1.0) - **Tag 164, Mo 16. Maerz. Vier Szenen: die Vorbereitung rueckblickend, das Auktionshaus, das Haus am Abend, und die Nacht.**

  **Er benutzt die Tuer aus Kapitel 4, und der Ort ist geladen.** Das Haus ist das Gebaeude am Fluss, in dem er im Oktober **im Keller** stand, vier Stunden, mit einer Nummer an sich. Er kommt zum ersten Mal vorne herein. Und es ist der eine Ort der Stadt, an dem ein Schreiber mit einem Terminal in unter einer Minute nachsehen kann, was hinter dem Halsband steht - **naemlich nichts.** *"He went in anyway. There was no version of the month in which he did not."*

  **Die Vorbereitung ist Aktenarbeit ohne eine einzige Frage an einen Menschen.** Ein Mann, der ein Haus ausraeumt, hat andere Haeuser ausgeraeumt, und die haben Unterlagen. Drei in sechs Jahren, eines davon abgewickelt und deshalb vollstaendig. Daraus **die Reihenfolge**: nicht der Schreibtisch mit dem Geld zuerst, sondern der mit dem Papier ueber das Geld. Und das Vorzeichen vier bis sechs Wochen davor: die schriftliche Bitte, in eigenen Worten die eigene Ablage zu erklaeren. **Georgij kennt die Form, weil er im Dezember eine gebaut hat**, und er schreibt genau das am Freitag in einer Zeile auf und beschoenigt es nicht.

  **Mrs Jeon**, Anfang fuenfzig, seit **dreiundzwanzig Jahren** hinter dem Glas, und ihr ganzer Wert war, dass nie jemand hingesehen hat. Erster Auftritt, und der Name kollidiert mit nichts im Kanon.

  **Er zahlt, bevor er fragt, und sagt das auch.** Die Warnung geht vollstaendig und bedingungslos ueber den Tresen: *"You can send me down the stairs and you will still have it. That was the whole reason for the order I said it in."* Sie bedankt sich nicht, und das ist keine Undankbarkeit - sie ist morgens mit einer Stellung hereingekommen und geht abends mit zwei Monaten heraus.

  **Der Preis ist das Spiegelbild seiner eigenen Lage.** Sie will einen Namen: einen Menschen ausserhalb des Gewerbes, der einen Anruf annimmt und einen Satz sagt, dessen Satz traegt. Dreiundzwanzig Jahre, die auf kein Blatt Papier passen. **Sein Problem ist, dass kein Name an ihm haftet; ihres, dass keiner an ihr haften will.**

  **Und hier beisst Annies Deckel aus Kapitel 5 zum ersten Mal.** Er weiss sofort, wen er fragen kann, und dass ein Ja das Ganze in einer Minute schliessen wuerde. Er sagt statt dessen **"I have to ask"** und faehrt nach Hause. *"I am not going to stand here and promise you a thing I do not own."*

  **Genau das bringt die Auskunft ein, und zwar geschenkt.** *"Nobody has ever said the other thing. Not once, at this desk, in twenty-three years."* Danach: **der aelteste der vier Eintraege ist nie ueber diesen Schreibtisch gelaufen.** Keine Rechnung, keine Quittung, keine Zeile. *"Somebody stood in that room and took a person home and this house did not send anybody a bill."* Sie hat es zweimal geprueft, weil es sie damals gestoert hat und seither stoert.

  **Der Abend: der Preis zuerst, das Ergebnis danach**, wie verlangt. Annie sagt zum eigenen Namen **nein**, und der Grund ist derselbe wie beim Register: er waere die Erklaerung dafuer, warum dieses Haus sich fuer jenes interessiert, *"standing at a bus stop in Incheon with her handbag"*. Sie gibt **Park Sang-hoon**, und zwar mit Begruendung: *"He is the only name in this that explains itself. ... If it were my name, the only question anybody could ask is why."*

  **Was es kostet, sagt Georgij, weil sie es nicht sagen wird:** das dritte, was Sang-hoon erfaehrt, und dass er der Mann sein darf, der es geloest hat. Und **es benutzt den Korridor**, den Sang-hoon einmal angeboten und danach nicht mehr erwaehnt hat. Annies Antwort: *"It is exactly what a man means when he says that. That is why it costs."* Dazu ihre Auflage: *"You will tell him what she is going to be able to say about him afterwards, before you ask him. He will say it does not matter. Tell him anyway."*

  **Der Schluss ist die zweite Begegnung mit Choi, und sie darf nicht gemerkt werden.** Eine Abrechnung, die nie stattgefunden hat, heisst, dass das Haus angewiesen wurde, keine zu schicken, und so eine Anweisung kommt von einem Eigentuemer. Der Eigentuemer ist ein Fonds, vier Gesellschaften tief, die vierte an einer Adresse in Jung-gu mit neun weiteren. **Georgij erkennt die Bauform, bevor er durch die zweite Schicht ist** - zweimal im Herbst gesehen, beide Male von unten, beide Male ohne Namen am Ende. Also **bricht er ab**: keine Unterlagen bestellt, kein Registerauszug, keine einzige Anfrage mit Datum, und um zwanzig nach eins liegt alles so, wie er es vorgefunden hat. Letzte Zeile: **"He had no way of knowing that it was the second time."**

- **Band 2, Kapitel 7** *Not the first* (v1.2) - **Tag 166, Mi 18. Maerz. Zwei Szenen an einem Tag, und die zweite macht die erste wertlos.**

  **Vormittags zahlt Mrs Jeon.** Sang-hoon hat am Montag um zehn nach acht bei ihr angerufen, vier Minuten, ohne eine einzige Frage - er hatte entschieden, bevor er den Hoerer abnahm.

  **Was sie liefert, ist der Mann, der das Los hat gehen lassen, und nicht der, der es mitgenommen hat.** Das Bild vom "nahen und fernen Ende" stand bis zum 23.08. da und wurde nicht verstanden - **ein Bild, das man erklaeren muss, ist ein kaputtes Bild**, und an dieser Stelle gibt es zwei einfache Substantive, die genau dasselbe sagen. Ein Los verlaesst das Haus ohne Rechnung nur gegen eine **Freigabe**: eine Seite, die sagt, was hinausgeht und wer es genehmigt hat, und die den Empfaenger nicht nennt, weil der Empfaenger das ist, wofuer die Rechnung da waere. **Dreimal in dreiundzwanzig Jahren, und dreimal dieselbe Unterschrift.**

  **Der Sanierer bekommt seinen Namen: Mr Hwang.** Und Georgij hat ihn schon gehabt - in sechs Punkt am Fuss der Seite in Kapitel 1. *"He had read the four sentences twice, because they were the best thing in that book. He had not read the name at all."*

  **Mrs Jeons Urteil ueber den Mann, der sie hinauswirft, und sie faelscht es nicht:** *"He is the most honest person I have ever worked for."* Er hat den Katalog aufgeraeumt, weil Aufraeumen richtig ist. Die Rueckseite ist auch seine: *"He made it findable because findable is correct."* **Und damit steht der schlimmste Satz des Monats im Korridor:** ein Mann kommt in ein Haus zurueck, macht fuenf Monate lang seine Arbeit besser als je jemand in dem Gebaeude, und baut dabei das, was jetzt auf Annie zeigt. *"There is no fault anywhere in that sentence."*

  **Und der Ansatzpunkt fuer Weg 2 faellt geschenkt mit ab:** *"He keeps everything. ... He is proud of that too."*

  **Nachmittags der Brief, und das Signal steht im Datum.** Sie schreibt seit zwanzig Jahren am Ersten. Sie schreibt am **achtzehnten**, und Georgij liest das Datum, bevor er ein einziges anderes Wort liest. *"I am writing to you on the eighteenth because I no longer have a first to wait for."*

  **Der Brief ist keine Erpressung, und das ist das Schlimmere.** Sie nennt, was sie hat, was sie nicht tun wird (*"Neither of those puts one container on my lane"*), und was sie will: **eine Stunde, die sechs im Raum, und dass ihnen jemand antwortet. Nicht ihr. Ihnen.** Frist der **26. Maerz**. Und danach: *"If nobody comes, I will write again on the first, as I always do."* Unterschrieben als **Chair** eines Verbands, den nie jemand haben wollte - ihr einziger Titel.

  **Georgijs Befund ueber den Brief ist der Kern der Bandregel:** *"There is not one untrue sentence in it. ... A man who lies leaves you something to catch him at. She has left nothing at all, and she has done it deliberately, and she has done it because she is certain she is right. She is also right."*

  **Dann die Frage, auf die er zum ersten Mal in zwei Baenden nichts hat.** **"Who gave it to her."** - *"I do not know."* Was er ableiten kann: sie hat die **Bedeutung** und nicht nur die Seite, jemand hat sich mit ihr hingesetzt; sie hat ausserhalb dieses Gewerbes nie etwas gehalten; und es kam **in der vierten Woche ihres schlimmsten Quartals**, nicht im Januar und nicht im Juni. *"Somebody chose her, and chose extremely well."*

  **Annie antwortet nicht, und Georgij sagt den Grund, weil sie ihn sagen laesst:** eine Stunde in einem Raum **ist** die Bestaetigung. Auf der Seite steht nirgends, dass das Veto ihres ist. **"So it is the same box as the book."** - *"It is exactly the same box. ... It is the shape of what is being done to you."*

  **Ihr letzter Satz zeigt auf Kapitel 8:** *"Then somebody who is not out of this house is going to have to go to Ulsan"*, gesagt zum Fenster hin, und er antwortet nicht, weil es keine Frage war.

  **Der Schluss ist ueber ihn und nicht ueber den Gegner.** Er schlaegt sein eigenes Notizbuch beim 5. Maerz auf und liest seine eigene Handschrift ueber die Verbandssatzung: ***"Mostly nothing. One clause about who may speak for the members in a dealing with a carrier."*** Er hat die einzige Rechtsstellung, die diese Frau besitzt, vor zwei Wochen in der Hand gehabt und *mostly nothing* danebengeschrieben. **Er reisst es nicht heraus und korrigiert es nicht.** Er schreibt das Datum darunter.

- **Band 2, Kapitel 8** *Nobody sent me* (v1.2) - **Tag 168, Fr 20. Maerz. Drei Szenen: der Donnerstagabend, die Fahrt, der Hof in Ulsan.**

  **Die Tuer steht im Brief selbst, und er findet sie erst beim vierten Lesen.** *"I want somebody to answer them."* **Nicht Du. Irgendwer.** Eine Frau, die zwanzig Jahre lang jeden Monat an dieselben sechs Leute schreibt, setzt kein Wort aus Versehen.

  **Annie schickt ihn ausdruecklich nicht, und das ist die Bedingung fuer alles Weitere.** *"I am not going to tell you to go." ... "I want that to be true when somebody asks you. Not a form of words. True."* **Sie enthaelt ihm die Anweisung vor und macht sie damit zum Werkzeug.** In Ulsan ist *"Nobody sent me"* dann keine Ausrede, sondern eine pruefbare Tatsache, und es ist das Einzige, was ihn in den Raum bringt.

  **Der Preis vorher, wie verlangt:** Geht er, ist er das Haus, *"because I have not got anything else to be"*. Und er kann nichts unterschreiben - die Vollmacht deckt einen Schreibtisch am Fluss, Sang-hoon und einen Monat. **"I am not going to stretch it."**

  **Wie er ueberhaupt nach Ulsan kommt, und das ist Regel 2 auf einer halben Seite.** Er fragt Mrs Seo, wie ein Mensch nach Ulsan faehrt, weil er noch nie im Leben eine Fahrkarte gekauft hat, und er sagt es in einem Satz, ohne sein Gesicht dabei einzurichten. Am Morgen liegt ein Umschlag da: Hinfahrt, Rueckfahrt, Bahnsteig, letzte Verbindung. **Kein Geld darin.** Sie hat darueber nachgedacht und sich dagegen entschieden, und er ist dankbar auf eine Art, die er nicht untersucht.

  **Der Augenblick, den das Kapitel eigentlich sucht:** Er sagt seinen Namen und der Name bedeutet ihr nichts. *"He watched it mean nothing, and for about a second he was a man standing in a yard."*

  **Was er ihr gibt, ist die Erklaerung, die ihr seit Januar niemand gegeben hat.** Kein Tarif, keine Behoerde, keine Abneigung im Hafen: ein privates Vetorecht in einem Gesellschaftervertrag. *"There is no office. There is nobody to write to. None of that is accidental. It is what the thing is for."* Und dann der Teil, den er praezise treffen muss: **es zielt nicht auf sie.** *"You are the floor of a room somebody else is standing in."* - **"That is worse."** - *"Yes."*

  **Die Zeile aus Kapitel 19 kann er nicht mehr zu Ende sagen.** Auf die Frage, was er verkaufen will: *"Nothing. I have nothing to sign with."* Und dann der Erzaehler: **die zweite Haelfte wurde ihm am 2. Maerz im kleinen Zimmer abgenommen, von der einzigen Person, die dazu berechtigt war**, und er hat nichts gefunden, was er dorthin setzen koennte.

  **Was er anbietet, ist ausschliesslich, dass er argumentieren wird.** Erstens die Auskunft, die sie schon hat, egal wie es ausgeht. Zweitens: er faehrt zurueck und vertritt, dass sie niemandem im Weg steht, und *"people do not usually refuse to do things that cost them nothing"*. Bei Irrtum: acht Tage verloren, und sie schreibt am Ersten wie geplant.

  **Und die Probe ist Ladung, nicht Post:** *"You will know because cargo moves. Not because anybody writes to you. Nobody is going to write to you, and if somebody did you should not believe it. Watch the lane."*

  **Warum sie zusagt, und es ist der traurigste Satz, den sie hat.** Zwanzig Jahre am Ersten, **vier Antworten insgesamt, alle vier von demselben Mann, und der ist tot.** Dazu: *"you have not once said the word unfortunately."* Ihr Aufschub geht bis zum **1. April**, nicht bis zum 26. Maerz - *"It is exactly what I was always going to do. I have simply told you."*

  **Die Rechnung auf der Rueckfahrt wird beidseitig aufgemacht, und die erste Fassung hat das nicht getan.** Dort stand nur *"most of it came out well"*, ohne dass je gesagt wurde, was. **Ein Kapitel, in dem nur die Kostenseite ausbuchstabiert ist, sieht aus wie ein Verlust.**

  **Was er tatsaechlich mitnimmt, ist eine Formaenderung.** Sie hat um **eine Stunde mit sechs Maennern darin** geschrieben, und genau das ist das Einzige, was nicht gegeben werden kann, weil es das Eingestaendnis selbst ist. Sie laesst ihn mit **Ladung** gehen. *"Cargo admits nothing. Cargo is a lane going back to what it was, and not one person has to say a word out loud in order for it to happen."* **Aus einer unerfuellbaren Forderung ist eine erfuellbare geworden**, und das ist mehr wert als die drei Dinge, die es gekostet hat.

  **Und ein zweites, das er nicht geholt hat und durch Fragen nie bekommen haette:** sein Name bedeutet ihr nichts. *"Whoever sat down with that woman had given her the page and had not given her the man on it. That is not an oversight. That is a decision, and a decision of that kind tells you what somebody is keeping something back for."*

  **Der Schluss ist die Rechnung, die nicht aufgeht.** Sie laesst ihn seinen Namen auf die Ecke eines Lieferblocks schreiben, ohne Titel, ohne Haus, ohne Telefonnummer, reisst die Ecke ab und steckt sie in die Manteltasche. **Sie hat seit dem 14. Maerz eine Kopie der Rueckseite mit Los vierzehn darauf. Sie weiss nicht, dass das dasselbe ist.** Und: *"the sort of person who found her in the first place does not do that once and then leave the rest to chance. And on the day she is told, she will remember that she asked for it."*

- **Band 2, Kapitel 9** *What you paid for* (v2.1) - **Tag 168, Fr 20. Maerz, nachts. Eine Szene, das kleine Zimmer, unmittelbar an Kapitel 8 anschliessend.**

  **Fassung 1 wurde am 23.08. verworfen, und der Grund gilt fuer 9 bis 11 zusammen.** Elf Kapitel lang endete keines damit, dass Georgij etwas gewonnen hatte. Jedes lief nach demselben Muster: zahlen, die Haelfte bekommen, dafuer geprueft werden. **Das ist kein Bogen, das ist eine Ratsche.** Und es widerspricht der Praemisse - er hat in Band 1 Park Sang-hoon geschlagen. Die Regel aus 2h heisst, dass **das Repertoire** stumpf wird, nicht der Mann.

  **Drei Fehler, die dabei benannt wurden:** die Gegner hatten ab Kapitel 7 die gesamte Initiative; er bezahlte dreimal hintereinander mit **Auskunft ueber sich selbst**; und er arbeitete auf eine **Gefahr** statt auf ein **Ziel**, was genau diesen Bogen erzeugt.

  **Was jetzt darin steht.** Der Bericht und Annies Pruefung der Offenlegung bleiben, aber kurz: sie stoppt ihn bei *"shareholders"*, und ihr Urteil bleibt doppelt - **"It was the right trade. It is still a leak."** Die Ladungsentscheidung ist eine **Unterlassung** und das ist ihr Witz: *"An hour in a room is an answer. Cargo is weather."* - **"Because it is not a thing that gets done."** - *"Because it is a thing that stops getting done."*

  **Dann die Frage, die er seit dem 2. Maerz nicht gestellt hat**, weil es keine Fassung davon gab, in der er nicht nach sich selbst fragte: **"On the nineteenth of February, what did you buy."** Annie: eine **Loeschung**, viermal in sieben Wochen, beim dritten Mal nicht Geld, und sie hat sich das Wort in einem vollstaendigen Satz sagen lassen und ein zweites Mal wiederholen lassen.

  **Und er findet es im Raum.** Die Seite hinten ist eine Liste **aufbewahrter** Eintraege. *"A deletion is the other thing. A deleted entry is nowhere."* **Zwei der vier sind ihre.** - *"They took your money twice and they struck a line through a page twice and kept the record twice. You were not sold silence. You were sold a piece of stationery."* Und: **"A house that does it once has a dishonest man in it. A house that does it four times in four years has a price list."**

  **Der Satz, der keine Analyse ist:** *"What they took the money for was me. ... They sat on the other side of a table and let you do it, and they had no intention of doing it, and they will do it again to somebody in June."*

  **Der Umschlag des Bandes, und er sagt ihn selbst.** *"I have been working to a danger and not to a target. ... I have spent three weeks answering. Tonight I stop."* Das Ziel: **das Haus ist Ende April erledigt, erledigt durch seine eigenen Kunden, und nichts davon kommt an diese Tuer zurueck.**

  **Die Methode ist keine Drohung.** Das Haus verkauft ausschliesslich Verschwiegenheit und ist sonst nichts wert. Der Beweis steht auf der Rueckseite eines Katalogs, **den das Haus seinen Kunden selbst geschickt hat.** Also: Mrs Sunwoo die Wahrheit sagen und sie in ihre eigene Post sehen lassen. *"She is the second-largest customer that house has ever defrauded, she is eighty-one, and she has forty years of knowing exactly who else buys there."*

  **Die drei, die es trifft und die nichts getan haben**, zaehlt er selbst auf: Mrs Jeon (fuer die er etwas tun kann), **Mr Hwang** (fuer den nicht), und wer auf der vierten Zeile steht. **Warnen geht nicht**, weil Hwang nichts zurueckhaelt: *"There is no version where he gets to know and does not write it down. All of the doors are the same door."*

  **Annie verlaengert die Vollmacht nicht, und zwar aus Respekt und nicht als Strafe:** *"A power of attorney with three names and a month on it is a document that describes a man doing errands. You are going to walk up that woman's drive holding nothing, which is what you are for."*

  **Und sie prueft, ob er es ernst gemeint hat.** *"Say it again on the first."* - **Er sagt es am ersten wieder, und es ist immer noch Ende April.**

- **Band 2, Kapitel 10** *The third line down* (v2.0) - **Tag 172, Di 24. Maerz. Eine Szene, ein Haus auf einem Huegel im Norden.**

  **Die Vorbereitung besteht aus Streichungen.** Nicht drohen, nicht handeln, nicht ueberzeugen - *"a woman who has been careful for forty years has a lifetime of watching men be convincing, and it is the fastest way there is to be shown the door."* **Was bleibt, ist ein Satz und ein Blatt Papier, das schon in ihrem Haus liegt.**

  **Wie er hineinkommt:** ihr eigener Satz, zurueckgegeben. **"Tell her we haven't met."** - *"I have been saying it for a very long time and nobody has ever handed it back."*

  **Der Satz selbst, und er hat auf dem Sonntag das Wort *sorry* daraus entfernt**, weil es fuer ihn gewesen waere und nicht fuer sie: *"They took the money and they did not delete it. It is on the back page of the catalogue they posted you in March. It is the third line down."* **Dann hoert er auf zu reden.** Sie laesst den Katalog holen, weiss genau, wo er liegt, findet die Zeile mit einem Finger und liest sie zweimal.

  **Sie fragt die gefaehrliche Frage und er beantwortet sie.** *"Which line is you."* - **"The fourth of October. Fourteen."** Das ist der Preis des Kapitels und er ist bewusst gezahlt.

  **Und er bittet sie um nichts**, weil es nichts gibt, was sie nicht binnen vierzehn Tagen fuer sich selbst taete. Sie durchschaut es und sagt es laut: *"So you did come here to ask me for something. You have simply arranged it so that I have to think of it myself."* - **"Yes. And I would rather you said that out loud than thought it on Thursday."**

  **Was sie zusagt, ist mehr als er geholt hat:** den ganzen April, langsam, an Leute, die zaehlen, **und Annies Name faellt in keinem Satz.** Ihr Grund ist kalt und richtig: *"a woman of eighty-one who has been personally cheated is the most credible witness in this city, and the moment there are two of us it becomes a dispute."*

  **Und die Auskunft, die alles vergroessert:** es gab welche **vor** dieser Seite. Sie kennt zwei, beide tot, einer hat es ihr 2011 auf einer Beerdigung erzaehlt und fand es komisch. **Was Hwang gefunden hat, war nur, was jemand aufgeschrieben hatte.**

  **Woraus die naechste Frage folgt, und sie gefaellt ihm nicht:** ein Haus, das so etwas tut, seit bevor es Akten fuehrte, tut es **fuer jemanden**. Und die eine Zeile, die nie berechnet wurde, ist das einzige Stueck, das er nicht stumpf machen kann.

  **Zum Abschied, ohne Anlass:** *"I shall not mention you to anybody. That is not a favour and you are not to put any weight on it. I have never in my life told anybody anything the whole way through, and I am not going to start at this age with something as interesting as you."*

  **Annies einzige Frage am Abend gilt nicht Mrs Sunwoo:** *"Say the fourth line to me again."* - *"No car. No dinner. No settlement. The house carried it."* - **"Yes. That is the one I want."**

- **Band 2, Kapitel 11** *In my own hand* (v1.1) - **Tag 180, Mi 1. April. Eine Szene, dazu drei Absaetze ueber die verstrichene Woche.**

  **Die Vollmacht ist am 31. ausgelaufen und wurde nicht erneuert, und niemand erwaehnt es.** *"He noticed it at about four in the afternoon on the Tuesday, the way a man notices that a tooth has stopped aching."*

  **Mrs Sunwoo wirkt bereits.** Zweimal zu Mittag gegessen, und am Freitag sagt ein Haus, das seit 1988 dort kauft, eine Besichtigung ab, ohne einen Grund zu nennen. **Eine Absage. Und der vierte Tag.**

  **Nams zweiter Brief, und sie hat nicht an ihre sechs geschrieben.** Sie fragt statt dessen, und der Rahmen ist ihr wichtiger als die Frage: *"I would like you to notice that I am asking rather than finding out, because I could find out and I have decided not to."* Dann: **"So. What are you."** - *"You told me you work in the house I wrote to. So does a gardener."* Sie weiss vom Kondolenzbuch. Und: *"I am fifty-eight and I would rather be told an unpleasant thing on the first of April than a pleasant one in June."*

  **Er antwortet vollstaendig, und es ist eine Entscheidung und keine Notlage.** Preis zuerst, wie vereinbart: sie kann es fuer den Rest ihres Lebens beweisen, verkaufen, weiterreichen, **und es gibt keine Fassung, in der er es zurueckbekommt.**

  **Was er sagt, dass es kauft, und er trennt sauber zwischen dem Sicheren und dem Erhofften.** Erstens: sie hoert auf zu suchen, und wer nicht geantwortet wird, **geht zum Fremden zurueck** - *"that is the one thing in all of this I would pay almost anything to prevent."* Zweitens, und er nennt es selbst eine Hoffnung: wer mit etwas betraut wird, das jemanden vernichten kann, benutzt es meistens nicht, **weil das Benutzen ihn in einen anderen Menschen verwandelt als den, dem vertraut wurde.** Dazu: *"I have watched it work on you."*

  **Annie ordnet nichts an, und diesmal aus einem anderen Grund als in Ulsan.** *"This one is yours because the thing you are proposing to give away is yours. It is the only thing in the world that is. I have never had a claim on it and I am not going to invent one now in order to be helpful."* Und ohne Beschoenigung: *"If she uses it, I will not be able to protect you from most of what follows."*

  **Er hat es sich vorgestellt und sagt, wie weit:** Chairman Woo wuerde erfahren, woneben er bei dem Essen stand. Hana Seo-yeon wuerde erfahren, was am 16. Dezember an ihrem Tisch sass. *"The rest of it I have not, and I am not going to sit here and pretend I have."*

  **Annies Befund ueber die letzten elf Tage:** *"You have got better at this in eleven days, and I would like to know what did it, because I would like more of it."* - *"I stopped working to a danger."* - **"Yes. Do not lose that again."**

  **Der Brief, in seiner Handschrift, beim vierten Versuch.** Kein Titel, kein Gehalt, kein Konto, nichts, was ihm gehoert. **"I belong to her."** Der 4. Oktober, das vierzehnte Los, drei Zeilen ueber ihrer im selben Buch. *"You can do what you like with this. I would sooner you had it from me than from whoever gave you the page."* **Darunter steht nichts** - es gibt in keiner Sprache eine Formel, die an diese Stelle passt.

  **Und das Haeusliche, das dieses Kapitel traegt.** Er muss Mrs Seo fragen, wie man einen Brief verschickt, zum zweiten Mal in vierzehn Tagen eine gewoehnliche Sache. Sie bringt abends den Einschreibbeleg - **das einzige Papier der Welt mit seinem Namen darauf, das er behalten darf.** Und Jang fragt sie seit dem 26. Maerz jeden Tag, ob etwas fuer ihn gekommen ist. Heute konnte sie ja sagen. *"He said good. That is all he said, and he went out to the cars."*

  **Der Schluss ueberspringt die Antwort und sagt statt dessen, was in der Zwischenzeit geschieht:** *"Nam Byung-hee did not answer it that week, or the next, and by the time she did the house on the river had stopped taking new consignments."*

---

## Die Wut, die niemand sieht ausser Annie

**Festgelegt am 23.08. vom Autor.** Georgij ist seit dem **18. Maerz** in kalter
Wut, seit dem Augenblick, in dem Nam Byung-hees Brief auf dem Tisch lag. Nicht
weil sie unrecht hatte - sie hat recht, und er sagt es. Sondern weil sie **Annie
persoenlich** angeschrieben hat, auf Briefpapier, damit es beweisbar ist, nach
vier Tagen Ueberlegung.

**Und die Waffe, die sie aufgehoben und gerichtet hat, ist er.**

**Der Zorn aendert nicht, was er in Kapitel 8 bis 11 tut. Er aendert, was es
bedeutet:**

- **Ulsan** ist keine Anstaendigkeit. Wer ertrinkt, tut an jedem Morgen
  irgendetwas Unvorhersehbares. Wer nicht mehr ertrinkt, bleibt stehen, wo man
  ihn hingestellt hat.
- **Die Ladung** stellt sie in Reichweite.
- **Der Brief vom 1. April** ist wahr **und** der letzte Pflock. Beides
  gleichzeitig, und er entscheidet nicht, welches davon zuerst kommt.

**Regel 1 bleibt unangetastet.** Kein Satz in irgendeinem davon ist unwahr. Das
ist dasselbe Verfahren wie bei Hanseong: neunzehn wahre Seiten, ein echter
Fehler, ein ruinierter Mann. `doc/02-leads.md`: *"fuehrt durch Auswahl in die
Irre."*

**Die vier Pflanzungen, und sie sind Absicht und duerfen nicht wegredigiert
werden.** Beim ersten Lesen unsichtbar, beim zweiten unuebersehbar:

1. **Band 2, Kapitel 7.** Er legt den Brief zurueck, *"square to the edge, which
   took him a moment longer than it needed to."*
2. **Band 2, Kapitel 7**, direkt nach *"She is also right."* - **Annie sieht ihn
   an. "What," said Georgij. "Nothing," said Annie.** Sie hat es am achtzehnten
   gesehen und sechzehn Tage lang nichts gesagt.
3. **Band 2, Kapitel 8**, auf der Rueckfahrt: der dritte Posten, den er auf
   keine Seite der Rechnung schreibt, *"because he had not decided which side it
   belonged on."*
4. **Band 2, Kapitel 11**, um elf Uhr nachts: der Brief hat zwei Wirkungen, und
   er legt keine davon vor die andere.

**Dazu die Auslassung, die Annie laut bemerkt.** In Kapitel 9 zaehlt er drei
Leute auf, die es treffen wird und die nichts getan haben. **Nam ist nicht
dabei.** *"You have not put the woman in Ulsan on that list."* - *"No."*

**Und die Einloesung liegt in Kapitel 12**, wo es zum ersten Mal seit dem
2. Maerz nichts zu berichten gibt und Annie ihn deshalb ansehen kann.

---

## Wiederkehrende Bilder

Motive leben von Variation, nicht von Wiederholung. Zu jedem steht hier, wo es
herkommt, wie oft es schon gefallen ist und was beim naechsten Mal anders sein
muss.

## Wiederkehrende Bilder

- **Die Fernbedienung, die abgelegt wird.** Annie nimmt sie in der ersten Nacht aus der Handtasche und legt sie **innen** neben die Schlüsselschale auf den Steinvorsprung an der Haustür, auf Hüfthöhe, ohne Kommentar. Nicht draußen: sie behält sie, sie benutzt sie nur nie. In siebzehn Jahren hat Georgij so ein Ding nie außerhalb einer Hand gesehen. Später verschwindet sie vom Vorsprung und liegt in ihrem Schreibtisch. Das Bild kehrt auf der Mapo-Brücke wieder.
- **Elf Zentimeter.** Der Abstand von seiner linken Hand zur offenen Handtasche während der Fahrt. Zwölf vor der letzten Kurve. Er zählt immer.
- **Die Handtasche.** Bleibt auf der Fahrt offen zwischen ihnen liegen. Inhalt, den er sehen kann: Telefon, Kartenetui, flache Lederrolle mit Druckknopf, Maniküre oder Nähzeug, beides brauchbar. Annie lässt sie beim Aussteigen auf dem Sitz, weil jemand dafür bezahlt wird, sie zu tragen. Georgij nimmt sie mit, benutzt die Schere, wischt sie ab, legt sie zurück und reicht ihm die Tasche mit "Your bag, Mistress".
- **Marmor.** Sein Gesicht unter Strom.
- **Los elf.** Der Junge kommt nächsten Monat zurück in den Katalog, zu niedrigerer Taxe.

### Die Lächeln

Georgij besitzt viele, und fast alle sind Handwerk.

**Geordnet nach Aufgabe, nicht nach Wärmegrad.** Ein Typ ist ein Werkzeug für
einen Zweck, kein Gefühl. Wärmegrade lassen sich beliebig vermehren und ergeben
eine Liste; Aufgaben nicht. Wer eine neue Art erfindet, sieht vorher hier nach.

Jeder Eintrag hat eine Fundstelle oder ist als **offen** markiert.

#### I. Die Fassade - getragen, nicht gezielt

- **Die entschiedene Miene.** Zwei Tage vorher gebaut, an der Tür aufgesetzt,
  sechs Stunden gehalten. Eine junge Miene, am äußersten Rand dessen, was er
  durchhält, und sie sagt: er kann die Decke nicht fassen, die Frau an seinem
  Arm ist das Größte, was ihm je passiert ist, und er will niemandem Mühe
  machen. Sie zielt auf niemanden. Sie ist der Boden, auf dem alles andere
  steht. (Kapitel 7, *the face he had decided on two days ago*, und später
  *slightly too pleased to be standing where he was standing*)
- **Das breite.** Geht ganz nach oben und kommt eine Viertelsekunde zu spät, und
  genau die Verzögerung macht, dass man es glaubt. Gebaut in einem Haus in
  Daejeon, als er einundzwanzig war. Hat bei Fremden nie versagt. Es ist das
  Werkzeug, das die Miene trägt: *Most of the work was done by the smile.*
  (Kapitel 7)

#### II. Die Werkzeuge - ein Gesicht, ein Ergebnis

- **Das kalibrierte.** Exakt so warm wie das mitgebrachte und kein Grad wärmer.
  Sagt: ich überbiete Dich nicht. (Kapitel 7, Mrs Sunwoo)
- **Das Ausgehenlassen.** Geht eine Sekunde aus, wenn jemand etwas Echtes
  hinlegt, und der andere merkt sofort, dass er gerade etwas auf den Tisch
  gelegt hat. Seltener und wertvoller als jedes Lächeln. (Kapitel 7,
  Chairman Woo)
- **Das absichtlich Weggelassene.** Vor jemandem, der noch entscheidet, was man
  ist: ein fremdes Lächeln quer durch den Raum wäre eine weitere Entscheidung,
  und sie trifft seit vierzig Minuten Entscheidungen. (Kapitel 7 und 8, die
  junge Frau an der Bar)
- **Das zu frühe.** *Offen, und mit Vorgeschichte.* Kommt an, bevor der andere
  den Satz zu Ende hat, und sagt ohne ein Wort: ich wusste es schon. Der
  Gegenzug zur Viertelsekunde des breiten - dieselbe Uhr, andere Richtung. Für
  Sang-hoon und Do-yun.

  **Kapitel 16 wurde dafür geprüft und verworfen.** Die Stelle wäre gewesen, wo
  Sang-hoon sagt *"In the same size type"* und damit seine eigene Prüfung
  verrät, während Georgij den Satz genau dafür gesetzt hatte. Gesetzt wurde
  stattdessen das Respektvolle, weil es dem Kapitel mehr gibt: ein Werkzeug an
  dieser Stelle hätte gezeigt, dass er vorne liegt, das unbewachte zeigt, dass
  ihm etwas entgeht. Wer es doch noch will, braucht dafür Do-yun, nicht
  Sang-hoon - der hat sein Gesicht in diesem Kapitel schon.
- **Das ans Publikum.** *Offen, und nach der grössten Lücke die zweitgrösste.*
  Zielt an dem vorbei, mit dem er spricht, auf den, der zusieht. Der Empfänger
  ist nicht das Ziel.

  **Der Grundsatz steht im Text und das Instrument nicht.** Kapitel 11:
  *Because eight hundred people had spent the evening deciding what I am. I gave
  them an answer that is not one and let them keep it.* Genau das beschreibt ein
  Lächeln, das an einem Gesicht vorbei in einen Saal geht - und der Saal steht
  in Kapitel 8 und 9 bereit, mit achthundert Leuten darin. Die Stelle ist dort
  und nirgends später.
- **Das am Telefon.** *Gesetzt, Kapitel 12 v1.6.* Niemand sieht es, er baut es
  trotzdem, weil die Stimme das Gesicht mitträgt. Reine Mechanik, an nichts
  verschwendet.

  > "Then it's a test," said Georgij **pleasantly**, "and you and I can both live with that. Go on."
  >
  > **He had put the smile on before he said it. Nobody could see it, at either end, and he built it anyway. A voice carries a smile, and a pleasant thing said with a flat mouth arrives flat.**

  **Die Reihenfolge ist der Punkt.** Das *pleasantly* stand schon da und
  beschrieb eine Stimme. Der Leser hört es erst und erfährt danach, dass es
  hergestellt war - dieselbe Bewegung wie *Most of the work was done by the
  smile* in Kapitel 7, nur ohne Zuschauer.

  **Es heißt *smile* und nicht *face*, und zwar nach einer Korrektur.** Die
  erste Fassung (v1.6) schrieb *the face*, mit der Begründung, am Telefon sehe
  niemand ein Lächeln. Das ist die Sache genau verkehrt herum: Der Begriff
  Telefonlächeln existiert, weil es ein **Lächeln** ist, das wirkt, ohne
  gesehen zu werden. *the face* nimmt dem Satz seinen Gegenstand. Ausserdem
  klingt *put the smile on* an *He put it on at the door and left it there*
  (Kapitel 7 und 8) an, und dort gehört es hin.
- Verwandt und im selben Haus gebaut: **unnahbar sein**, was über den Winkel
  läuft. Falsch herum stehen, etwas halten, die Augen auf etwas legen, das kein
  Mensch ist. (Kapitel 8)

#### III. Die Klingen - sie sollen als Drohung ankommen

- **Das freundlichere, je schlimmer es wird.** *Zurückgestellt, nicht offen.*
  `doc/02-leads.md` führt den Grundsatz seit Anfang: je zuvorkommender er wird,
  desto näher ist jemand am Schaden. Kapitel 1 zeigt die Mechanik ohne das
  Gesicht - *He said it gently.*, während er einen Mann vernichtet. Es ist das
  einzige Lächeln, bei dem der Leser die Akte glaubt.

  **Es stand hier als grösste Lücke und ist keine.** Der Bogen des Buches ist,
  dass der Leser die Akte über siebzehn Kapitel hinweg immer weniger glaubt,
  weil er einen Mann bei der Arbeit zusieht und nicht bei der Vernichtung. Wenn
  das Instrument unterwegs auftaucht, wird der Verdacht am Leben gehalten und
  der Bruch verliert. Es gehört in die Blöcke F bis J und dort an die erste
  Stelle, an der jemand wirklich beschädigt wird.

  **Damit ist es eine Entscheidung und kein Versäumnis**, und wer es vorher
  einbaut, nimmt dem Buch seinen teuersten Moment. Bis dahin bleibt Kapitel 1
  die einzige Fundstelle, und sie bleibt ohne Gesicht.
- **Das kalte.** *Offen, und die nächste Gelegenheit steht schon fest.* Kein
  Weglassen und keine Spiegelung: ein vollständiges Lächeln, aus dem die Wärme
  herausgenommen ist, und der andere soll das merken. Sagt: ich habe Dich
  gelesen und tue nicht so, als hätte ich nicht.

  **Die Stelle ist das Gespräch mit den Kims**, das in `doc/07-next.md` als
  Nächstes steht, und darin Do-yun. Georgij hat sich in Kapitel 14 einmal in ihm
  geirrt und es an Fotografien gemerkt. Beim zweiten Mal weiss er es, und dieses
  Lächeln ist die einzige Art, es zu sagen, ohne es zu sagen.
- **Das halbe.** *Offen und sparsam, und ohne Anker.* Ein Mundwinkel, gilt
  niemandem, er amüsiert sich. Das einzige, vor dem kompetente Leute Angst
  haben, weil es heißt, dass er Spaß hat.

  **Der Anker, der hier stand, war falsch zugeordnet.** Genannt war Kapitel 17,
  *He knew he was doing it and he did not take it off.* Diese Zeile gehört
  nachweislich **dem eigenen**: vier Absätze später steht *Two of them in
  seventeen years had been his own. One had gone to Mr Hong at the gala… This
  was the other one.* Dieselbe Bewegung steht in Kapitel 14 (*he did not put it
  away*) und ist dort ausdrücklich *not one he had built*.

  Damit hatte das halbe seine Glaubwürdigkeit aus der einen Sorte geliehen, die
  das Dokument zwei Absätze weiter unten ausdrücklich schützt: *Wer die zwei
  vermischt, verbraucht die zwei in siebzehn Jahren.* Der Anker ist gestrichen.
  Das halbe hat keine Fundstelle und braucht eine eigene.

#### IV. Die unbewachten - es wird nichts geholt

- **Das Respektvolle**, hauptsächlich im Kinn. Für Kompetenz, die ihm nichts
  nützt. (Kapitel 5, der Schneider, der ihm eine Zeile vorher gesagt hat, wie er
  das Kinn zu halten hat: *Georgij smiled at him, and most of it was in the
  chin.*)

  **Zweite Fundstelle: Kapitel 16**, und es ist das einzige Lächeln in dem
  Kapitel. Sang-hoon hat gerade beschrieben, wie er in vier Räumen mit vier
  Leuten desselben Vorstands saß und jedem die Wahrheit gesagt hat, jedem eine
  andere, und keine davon war gelogen. Das ist Georgijs eigenes Verfahren,
  benannt von dem Mann, der es erfunden hat, an einem Abend, an dem Georgij vier
  Wände aufstellt, die alle wahr sind. Es wird nichts damit geholt, und der Text
  sagt das ausdrücklich: *Nothing was being fetched with it.*

  **Der Rückverweis ist nicht wörtlich**, und das ist Absicht: nicht wieder *in
  the chin*, sondern *most of it went where it had gone once before, for an old
  man who had come to the house with a tape measure and thirty words*. Wer die
  Stelle wiedererkennt, bekommt sie; wer nicht, verliert nichts.

  **Annie bepreist es in Kapitel 17**, ohne zu wissen, dass sie es tut: *Be
  pleased with it in this car and nowhere else. You got it because a man was
  showing off to somebody he had decided was nobody. If you look pleased in a
  room, he stops showing off.* Damit ist das eine unbewachte Gesicht des Abends
  rückwirkend auch das einzige, was ihn etwas gekostet haben könnte. Georgij
  merkt davon nichts, und das bleibt so.
- **Das kleine.** Klein gehalten, weil ein großes um ein Uhr nachts von einem
  Mann mit Halsband eine zweite Sache wäre, vor der jemand Angst hat.
  (Kapitel 3, Ji-won auf der Treppe)
- **Das ehrlich freundliche.** Für Mrs Seo, Ji-won, Bae, Jang. Nicht gebaut,
  sondern **entschieden** - und es holt nichts. Der Text sagt an mehreren
  Stellen *and he meant it* und hängt kein Gesicht daran; genau dort gehört es
  hin. Am deutlichsten bei Mrs Ryu in Kapitel 7: *he meant it, and she could
  hear that he meant it*, und ihr Gesicht ändert sich kaum, und sie gibt ihm
  trotzdem sechs Minuten.

  **Zweimal gesetzt, beide Male an einer Stelle, an der der andere zuerst etwas
  gegeben hat:**

  - *Kapitel 4, Mrs Seo in der Küche.* Sie sagt ihm, dass sie sein Schweigen
    bemerkt hat und ihn deshalb länger höflich behandeln wird als geplant.
    Darauf: *He was not after anything with it, and she would have known if he
    had been.* Die zweite Hälfte ist zugleich das Kompliment an sie.
  - *Kapitel 6, Jang vor der Gala.* Jang meldet von sich aus, dass er die Route
    des Nachtpostens geändert und es nicht gesagt hat. Darauf: *which he did not
    have to do and got nothing for.*

  **Dritte Fundstelle: Kapitel 18, an Chairman Woo.** *Then he smiled at him,
  and meant it.* Es ist die erste Stelle, an der es jemandem gilt, von dem er
  etwas will - und es holt trotzdem nichts, weil er ihm im selben Termin bringt,
  was der andere seit einem Jahr sucht. Beide gewinnen, und deshalb ist nichts
  zu holen. Es folgt ausserdem der Regel der ersten zwei: der andere hat zuerst
  etwas gegeben, und zwar etwas, das ihn teuer zu stehen kommt.

  **Korrigiert am 22.08.: die Behauptung, es werde häufiger, war falsch.** Hier
  stand: *In Kapitel 3 bis 6 selten und knapp, im Schluss selbstverständlich.*
  Nachgezählt über alle Kapitel steht *and he meant it* in dieser Bedeutung in
  Kapitel 3 (zweimal), 6, 7 und 9 - **und danach in acht Kapiteln nicht mehr.**
  Es wurde nicht häufiger, es riss ab, und zwar genau dort, wo der Haushalt aus
  dem Buch verschwindet. Kapitel 18 ist die erste Wiederaufnahme.

  **Was daraus folgt:** Es ist das einzige Lächeln, das nichts holt, und es fiel
  in dem Abschnitt weg, in dem er gut in der Arbeit wird. Das darf eine Tragödie
  sein, aber dann muss der Text sie tragen. Bis dahin gilt: wo eine Szene einen
  Menschen enthält, den er mag, gehört es hin. Das ist dieselbe Bewegung wie *I have not looked once
  since I came here*, nur im Gesicht statt in der Erzählung. Er hat aufgehört,
  die Stelle zu suchen, an der es weh tut, und gleichzeitig angefangen, Leute
  anzulächeln, von denen er nichts will, und keines von beidem hat er
  beschlossen.

  **Abgrenzung, die halten muss:** *Das eigene* ist unfreiwillig und überrascht
  ihn. *Das ehrlich freundliche* entscheidet er. Wer die zwei vermischt,
  verbraucht die zwei in siebzehn Jahren.
- **Das eigene.** Zwei in siebzehn Jahren, beide vergeben. Siehe unten.
- **Das ungebaute.** Ab Tag 34, an Annie. Siehe unten.

#### V. Was er bekommt

- **Das wiedererkannte.** Chef Bang steht in Kapitel 8 während der Gebote in
  Weiß neben dem Pult, die Hände gefaltet, und lächelt, weil man ihm gesagt
  hat, wo er stehen soll. Georgij rechnet daneben **drei einhalb**.

  Gesetzt ist eine halbe Zeile bei der ersten Sicht: *Georgij knew the smile.
  It is the one you put on at the door and leave there.* Das ist wörtlich der
  Satz aus Kapitel 7 über sein eigenes breites Lächeln (*He put it on at the
  door and left it there*), und damit steht sein Werkzeug auf dem Gesicht
  eines Mannes, der gerade verkauft wird.

  **Der Text kommentiert nichts weiter, und das bleibt so.** Was es kostet,
  tragen die Rechnung und Annies Nichthinsehen während der ganzen
  Versteigerung. Wer hier erklärt, nimmt beiden das Gewicht.

---

**Alle in I bis III sind für eine Situation kuratiert, auf ein Gesicht gerichtet und auf ein Ergebnis gezielt.** In fünfzehn Minuten benutzt er vier verschiedene an neun Leuten und keines davon an Annie, und das fällt ihm erst später auf.

**Wo die Regel nicht hinreicht.** Er sagt nie etwas Unwahres, und ein Gesicht ist
keine Aussage. Die Gruppen II und III sind damit die einzige Stelle, an der sein
Grundsatz nicht greift, und Gruppe IV die einzige, an der er ihn nicht braucht.
Ausführlich in `doc/02-leads.md` unter **Er lügt nie**.

**Der Bogen.** Das Buch bewegt ihn von I und II nach IV. Der Katalog erzählt
damit dieselbe Geschichte wie die festgelegte Zeile in Kapitel 17.

**Zwei in siebzehn Jahren waren seine eigenen, und am 29. Dezember kam ein drittes.** Der Zaehler in Kapitel 17 - *"Two of them in seventeen years had been his own"* - stimmt fuer den Stand von Kapitel 17 und nur dafuer.

**Das erste** geht in Kapitel 7 an Mr Hong, anderthalb Sekunden lang, weil der Mann ihm den dritten Namen gegeben hat und Georgij weiß, was das gekostet hat. Der Text sagt dazu: *it was the only one that was his*.

**Das zweite** ist das ungebaute, und es kommt zweimal. **Kapitel 14, Tag 34, über ihrem Schreibtisch**, als er sagt, dass er einem Mann ein Dokument geben wird, in dem jedes Wort wahr ist, damit der sich daran ruiniert. Es kommt langsam, von hinter der Höflichkeit her, ohne Grausamkeit und ohne Entschuldigung, und es ist das Gesicht eines Mannes, der Arbeit gefunden hat, die zu ihm passt. Es ist das erste Mal in vierunddreißig Tagen, dass er ihr etwas dieser Art zeigt, und er nimmt es nicht weg, weil Wegnehmen eine zweite Lüge wäre.

**Kapitel 17, Tag 46, im Wagen**, als Sang-hoon angebissen hat. Dasselbe Lächeln, zwölf Tage später, und der Unterschied ist die Geschwindigkeit: über dem Schreibtisch hat es sich Zeit gelassen, hier nicht mehr.

**Regel:** Das ungebaute nie beschreiben, als wäre es neu. Es hat eine Geschichte und die fängt in Kapitel 14 an. Wenn es wiederkommt, verändert sich etwas daran, nicht die Beschreibung.

**Das dritte**, Kapitel 33, Tag 87, in den elf Sekunden, in denen Sang-hoon den Apfel begreift. Es steht in **keiner** der Gruppen oben, weil die Gruppen kuratierte Sorten fuehren und dieses keine ist: *He had no name for this one.* Zwei Dinge unterscheiden es von den ersten beiden. Es faellt **vor dem Mann, um den es geht**, und vor Annie, die genau das untersagt hat. Und er merkt es erst, als es schon da ist - *He noticed it the way you notice that it has started raining.* Die ersten beiden standen in Raeumen mit einer einzigen Person darin, und die wusste ohnehin alles.

### Der Griff und wie er zurückkommt

Die Bitte um Orientierung ist Georgijs bester Griff und läuft in drei Stufen auf ihre eigene Aufdeckung zu.

**Einmal benutzt bei Hong**, Kapitel 7. Hana warnt ihn noch am selben Abend: Hong hat die Geschichte elfmal erzählt, bis Freitag wissen vier Leute in dieser Stadt, dass der Neue sich führen lässt, und ihr Satz dazu lautet: **"It's a good tool. You've used it once. Be careful how many times it fits."**

**Kang** spricht ihn später darauf an. Georgij lacht es mit Unerfahrenheit weg.

**Sang-hoon**, beim Abendessen, zum ersten Mal bei ihm: der Hanseong-Bericht mit der Bitte, ihm zu sagen, ob die Analyse Unsinn sei. Sang-hoon korrigiert, indem er handelt, und beißt.

**Sang-hoon, danach:** "Du bittest oft um Rat." Und weil Georgij ihn zu diesem Zeitpunkt genau **einmal** gefragt hat, ist das keine Beobachtung, sondern der Beweis, dass Sang-hoon ihn hat nachprüfen lassen. Der Satz kommt nach einer einzigen Verwendung als Ergebnis einer Erkundigung zurück.

**Das Bild läuft in drei Stufen durch das Buch, und jede Stufe ist kürzer als die vorige.**

**Erstens, Kapitel 15, Tag 41, am Tisch mit Hana und Annie.** Hier wird es geprägt, in voller Länge, während er erklärt, wozu das Dokument dient:

> "It is an apple. Sweet, full of juice, and there is not a mark on the skin of it anywhere, because I have taken a great deal of trouble over the outside."
>
> "The poison is that all of it is true. If I had shaded one line he would have found it in an afternoon, and I would never have got near him again."
>
> "A poisoned apple," said Hana.
>
> "Yes. And he is going to enjoy every mouthful of it."

Hana spricht die zwei Wörter aus, damit sie im Raum stehen und nicht nur in seinem Kopf. Damit hat sie es gehört, und das ist Voraussetzung für die spätere Szene.

**Zweitens, Kapitel 17, Tag 46, im Wagen.** Nur noch ein Fragment, weil das Bild steht:

> "He has taken a bite out of the apple, and he is carrying the rest of it around in his coat until Thursday."

**Drittens, die Szene mit Sang-hoon.** Die volle Fassung, ins Gesicht des Mannes, vor Zeugen.

**Die dritte Stufe ist deshalb keine Enthüllung, sondern eine Schließung, und das ist Absicht.** Der Leser kennt das Bild, Annie kennt es, Hana soll es bis dahin auch kennen. Wenn er es Sang-hoon ins Gesicht sagt, erfährt als Letzter der Mann davon, dem es gilt, und alle anderen im Raum sehen eine Bestätigung. Ein Bild, das nur einmal fällt, hat diese Wirkung nicht.

**Regel:** Jede weitere Verwendung muss kürzer sein als die davor, bis auf die letzte. Ein Motiv lebt von Variation, nicht von Wiederholung.

**In derselben Szene schließt sich die zweite Schleife.** Der Griff, jemanden um Rat zu bitten, ist Georgij mehrfach vorgehalten worden: von Hana auf der Terrasse, von Kang am Telefon, von Sang-hoon selbst bei Minute zwölf. Wenn er ihn dort ein letztes Mal benutzt, benutzt er ihn an dem Mann, der ihn als Erster benannt hat, und danach nie wieder.

Georgijs Antwort kostet ihn nichts mehr, weil der andere schon drinsteckt, und ist die reinste Form seiner Regel im ganzen Buch:

> "Ja. Dann bitte ich Sie um Rat. Zeigen Sie mir, wie ein Mann von einem vergifteten Apfel ablässt. Ich habe mir große Mühe gegeben mit diesem hier. Ich weiß, wie gut er ausgesehen haben muss."

Sang-hoon kann daraufhin nur zweierlei: es für Frechheit halten und weiterbeißen, oder es für den Bluff eines Anfängers halten und weiterbeißen.

### Der Hammer

**Kapitel 8, Los neun.** Die Benefizversteigerung endet mit Chef Bang Seung-min, ausgebildet in Lyon und Tokio, der an einem Abend nach Wahl des Käufers mit eigenen Leuten in dessen Haus geht und für acht kocht. Er steht während der Gebote neben dem Pult in Weiß, die Hände gefaltet, und lächelt, weil man ihm gesagt hat, wo er stehen soll. Zuschlag bei zweiundsechzig Millionen. Er verbeugt sich zweimal, einmal in den Saal und einmal zum Tisch, der ihn gekauft hat.

Der Text kommentiert nichts. Er gibt nur die Rechnung, die Georgij macht, bevor er sich dagegen entscheiden kann, wie in jedem Raum, in den man ihn je gestellt hat: **drei einhalb**.

Der Hammer ist hölzern, etwa so lang wie ein Löffel, und macht in einem Saal dieser Größe fast kein Geräusch. Jemand an Tisch neun sieht nicht einmal auf.

---

## Festgelegte Zeilen

Wortlaut steht fest. Wer eine dieser Stellen anfasst, aendert nicht die Formulierung,
sondern nur mit ausdruecklicher Entscheidung, und traegt sie unten in
`doc/08-decisions.md` ein.

### Festgelegte Zeile: die Heimfahrt nach dem Essen mit Sang-hoon

Im Wagen, unter vier Augen, unmittelbar nachdem er zum ersten Mal einen Menschen absichtlich vergiftet hat, mit einem wahren Bericht und ohne eine einzige Lüge.

> "Mistress. About the quid pro quo."
>
> "Go on."
>
> "Eleven houses. Seventeen years." Nichts in der Stimme, an keiner Stelle. "In every one of them, the first thing I did when I came through the door was find the place where it would hurt. Not the locks and not the exits, those are reflexes. The place. I found it every time, and I used it whenever I needed it, and in some of those houses I needed it a great deal."
>
> Eine Pause.
>
> "I have not looked once since I came here."
>
> Und dann, bevor sie etwas sagen kann:
>
> "I did not decide to stop. It stopped being the first thing I did in a room and I did not notice it stopping. I have been in your house six weeks and I found out about it tonight, in this car, on the way home from doing it to somebody else."
>
> "And now?"
>
> "I enjoy this."

**Es sind elf Häuser, nicht vier.** Die vier sind nur die, bei denen jemand einen Grund vermerkt hat. Davor war er ein Kind, und Kinder werden ohne Papierkram weitergereicht. Er hat in allen elf gesucht und gefunden. Keine Zählung im Text, weil Zählen das Gewicht wegnimmt.

**Warum es ein Kompliment ist.** Nicht weil er sagt, dass es ihm gefällt. Weil er in siebzehn Jahren in jedem Raum dasselbe getan hat und hier damit aufgehört hat, **ohne es zu beschließen und ohne es zu merken**. Unfreiwillig, und deshalb nicht zurücknehmbar.

**Warum dort und nirgends sonst.** Er bemerkt es ausgerechnet an dem Abend, an dem er es bei einem anderen getan hat. Damit steht das Kompliment neben der Tat und wird kalt statt warm.

**Aufgehoben in Fassung 10.5.** Der Satz "I enjoy this" ist nicht mehr das Ende. Es folgt eine zweite Hälfte, und sie steigert, statt abzufallen.

> "The first time I called you Mistress it was a courtesy with an edge on it. It was not true."
>
> "It has been true for some time. I did not notice that either."
>
> "I stopped looking and I started meaning it. Neither of them was my doing."
>
> "They were yours."

**Warum das größer ist als die elf Häuser.** Dort hat er aufgehört, etwas zu tun. Hier gibt er zu, dass etwas mit ihm geschehen ist, und dass er nicht der Handelnde war. Er sagt kein einziges Mal danke, und das ist Absicht: **"Thank you" steht achtundzwanzigmal im Text**, fast immer in seinem Mund, an Ji-won für eine Lampe, an den Schneider, an Hana. Es ist sein Kleingeld. Die einzige Art, in der er ihr danken kann, ist die Zuschreibung.

**Hier stand bis zum 23.08. "achtzehnmal", nachgezählt am Stand von Kapitel 17.** Es sind inzwischen achtundzwanzig, und das Argument wird davon nur stärker. **Beim Nachzählen fiel ausserdem auf, wem die Ausnahme gehört:** Annie sagt es genau einmal im ganzen Buch, in Kapitel 11, nachdem Georgij ihr ungefragt einen Regelbruch gemeldet hat, den niemand bemerkt hatte. *"Thank you for telling me."* **Das ist der Titel des Kapitels.** Sie gibt ihm also einmal genau das zurück, was bei ihm Kleingeld ist, und es ist bei ihr das Teuerste, was sie an dem Abend hergibt.

**Das Wort war eine Waffe, keine Beleidigung.** In Kapitel 1 und 2 ist die makellose Höflichkeit die Klinge, und "Mistress" ist ihr schärfstes Stück. Ausgesprochen als Beleidigung steht es nirgends, und er sagt nichts, was der Leser nicht nachprüfen kann.

**Folge für den Bruch.** Wenn der Spott in Block G zurückkommt, kommt er in ein Wort zurück, von dem der Leser weiß, dass es inzwischen wahr war. Das macht den Bruch teurer, nicht billiger.

**Korrigiert in Fassung 10.3:** Die Zeile stand ursprünglich auf "four weeks". Das Essen mit Sang-hoon liegt an Tag 46, also sechseinhalb Wochen nach dem Kauf. Der Wortlaut ist auf "six weeks" gesetzt und gilt so.

**Unter vier Augen, und wie das zustande kommt.** Mr Pyo fährt, und die Abtrennung ist bis dahin unten, weil in diesen Wagen immer nur Arbeit gesprochen wurde. Annie fährt sie hoch, unaufgefordert, in dem Moment, in dem er aufhört zu berichten und nicht wieder anfängt. Georgij greift nicht nach dem Schalter, und der Grund ist nicht Unachtsamkeit: Er hatte in siebzehn Jahren nie etwas, das hinter eine Abtrennung gehört. Alles, was er je in einem Wagen gesagt hat, war Arbeit, auch der Satz in Kapitel 11 über seine Herkunft, denn das war ein Bericht über einen Fehler. Sie hört den Unterschied vor ihm.

### Festgelegte Zeile: das best-made thing

**Kapitel 16, an der Tür, Tag 46.** Sang-hoon gibt ihm die Hand, was er bei der Ankunft nicht getan hat, und sagt, dass er ihn vorher hat prüfen lassen. Dann:

> "And you are either exactly what you look like," said Park Sang-hoon, "or you are the best-made thing anybody has ever put in front of me."

**Warum das später zahlt.** Sang-hoon meint "thing" als Händlerwort. Er kauft Firmen und behandelt die Leute darin als Posten, und in seinem Mund ist der Satz das höchste Lob, das er zu vergeben hat. Er weiß nicht, dass er wörtlich recht hat, und er wird sich an den Satz erinnern, wenn er es erfährt. Georgij kann ihn dann zitieren, ohne ein Wort zu erfinden, und das ist die einzige Art von Waffe, die er sich erlaubt.

**Das Wort hat eine Vorgeschichte.** Der erste Wachmann sagt in Kapitel 1 und 2 durchgehend "it" und nennt ihn seit dem Ladehof einen Hund, und er meint es wörtlich, und es ist die Hälfte des Grundes, warum er das Auge verliert. Sang-hoon sagt dasselbe über ihn und verliert nichts. **Der Unterschied ist nicht die Beleidigung, sondern die Kompetenz des Sprechers**, und damit ist der Satz zugleich die sauberste Illustration von Georgijs eigener Regel im ganzen Buch.

**Ab hier ist es persönlich**, und der Text sagt das nirgends.

**Regeln für den Umgang damit:**

- **Keine Reaktion im Text.** In Kapitel 16 steht nichts hinter dem Satz. Georgij geht, schreibt vier Zeilen ins Notizbuch, und keine davon ist diese. Das bleibt so.
- **Nicht wiederaufgreifen, bis es sich einlöst.** Kein Nachdenken darüber, kein Echo im Erzähltext, keine zweite Erwähnung durch Dritte. Ein Satz dieser Art verliert alles, wenn die Figur ihn zwischendurch anfasst.
- **Wörtlich aufbewahren.** Wenn er zurückkommt, kommt er mit genau diesen Worten zurück, und der Sprecher ist dann Georgij.

---

### Festgelegte Zeile: was nicht Arbeit war

Drei Woerter, zweimal, drei Kapitel auseinander. **Beide Stellen sind Wortlaut.**

**Kapitel 13, ueber Georgij.** Erzaehlung, nicht Rede:

> At some point Woo told a story about a shipping agent in Busan in 1994 that was very funny, and Georgij laughed properly at it, **which was not work**.

**Kapitel 16, aus Sang-hoons Mund.** Nach der vierten Wand, der Frage, wo Georgij schlaeft:

> Then he laughed, and it was the second time Georgij had heard it, and it was not longer than the first.
>
> **"That one was not work,"** he said. "I wanted to know."

**Warum das haelt.** Beide Male markieren dieselben drei Woerter den einen
Augenblick eines durchgearbeiteten Abends, in dem jemand aufgehoert hat zu
arbeiten. Die Asymmetrie ist der Punkt: Georgijs Version ist Erzaehlung, weil er
den Satz ueber sich selbst nicht sagen wuerde und ihn auch gar nicht bemerkt.
Sang-hoon sagt ihn laut, weil ein Mann in seiner Lage sich leisten kann, seine
eigene Dienstpause zu benennen. Der eine bekommt es zugeschrieben, der andere
spricht es aus.

**Und seit Fassung 1.11 traegt es doppelt.** Sang-hoons einziger unbezahlter
Moment des Abends ist ausgerechnet die Frage nach dem Halsband, das er nicht
sehen kann.

**Regeln fuer den Umgang damit:**

- **Beide Saetze sind Wortlaut.** Wer eine der beiden Stellen umformuliert,
  toetet den Reim, ohne ihn zu sehen: es sind drei gewoehnliche Woerter, und
  keine Suche findet sie von selbst. Deshalb stehen sie hier.
- **Kein drittes Mal.** Zweimal ist ein Reim, dreimal ist ein Tic.
- **Kein Kommentar, in keine Richtung.** Georgij bemerkt es nicht, der
  Erzaehler zeigt nicht darauf, und keine Figur greift es auf.
- **Die eine erlaubte Zukunft:** dass Georgij ihn selbst laut sagt. Das waere
  ein Zustandswechsel und keine Formulierungsfrage, gehoert also vorher nach
  `doc/08-decisions.md`.

---

### Festgelegte Zeile: die zwei Haende, die sich nicht bewegen

**Kapitel 17, zweimal, zweiundsechzig Zeilen auseinander. Wortlaut auf beiden Seiten.**

> *Im Wagen, allein im Absatz, waehrend er die Beichte zu Ende bringt:*
>
> "It has been true for some time. I did not notice that either."
>
> **His hand stayed where it was.**
>
> "I stopped looking and I started meaning it. Neither of them was my doing."

> *Am Stuhl im Korridor, eingeschoben in ihren eigenen Satz:*
>
> "I have never put it down. Not one night." **Her hand stayed where it was.** "And this is my house."

**Warum es traegt.** Dieselben vier Woerter, zwei Menschen, zwei Gestaendnisse.
Er sagt, dass er die Waffe abgelegt hat, ohne es zu beschliessen; sie sagt, dass
sie ihre nie abgelegt hat. Die Haende tun in beiden Faellen dasselbe, und der
Unterschied liegt darin, worauf sie liegen: seine auf dem Sitz **zwischen
ihnen**, ihre auf der Lehne des Stuhls, dem einen Quadratmeter, den sie fuer
sich behaelt. Damit steht das Argument des Kapitels in einer Geste, und keine
Figur benennt es.

**Die Platzierung ist Teil des Reims.** Seine steht allein in einem Absatz, ihre
steckt in ihrem eigenen Satz. Er braucht den Raum, sie nicht.

**Regeln fuer den Umgang damit:**

- **Beide Saetze sind Wortlaut.** Es sind vier gewoehnliche Woerter, keine Suche
  findet den Reim von selbst, und wer eine der beiden Stellen umformuliert,
  toetet ihn, ohne ihn zu sehen.
- **Kein drittes Mal**, in keinem Kapitel.
- **Kein Kommentar.** Weder Georgij noch der Erzaehler zeigt darauf.
- **Entstanden am 22.08. im zweiten Durchgang**, nicht geplant: der Beat fuer
  ihn wurde gebraucht, weil dort zwei Redebloecke derselben Figur ohne etwas
  Koerperliches aufeinander folgten. Dass Annies Zeile schon so dastand, ist
  aufgefallen, nachdem er geschrieben war.
