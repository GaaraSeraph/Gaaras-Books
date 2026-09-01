# Kalender

*Kanon. Was wann geschieht. Praesens ueber die Fiktion, keine datierten
Berichte - die stehen in `protokoll/`.*

**Welches Kapitel an welchem Tag spielt, steht nicht hier, sondern in
`erzeugt/KAPITEL.md`**, eine Zeile je Kapitel, aus den Kapitelkoepfen erzeugt.
Bis zum 27.08. wurde diese Liste hier von Hand gefuehrt: 42.576 Woerter in
zwei Bloecken, von denen der zweite unter einer Ueberschrift ueber eine
Handbewegung hing. **Was daran Kanon war, steht jetzt unter seinem Thema; was
Nacherzaehlung war, steht im Buch.**

Kalender, Kapitelstand, wiederkehrende Bilder, woertlich festgelegte Zeilen. Die Datei fuers Pruefen.

---

## Kapitelnummern in Band 2: mehrere Verschiebungen, alte Verweise bleiben markiert

**Band 2 hat neunzig Kapitel** (aktueller Stand ueber `chapters-2/`; die
Zahlen fuenfundachtzig und neunundachtzig waren Zwischenstaende).

**Es hat drei Nummerierungsgenerationen gegeben** - vor dem 27.08., die
Umnummerierung vom 27.08. (`archiv/UMNUMMERIERUNG.md`), und die Teilung vom
28.08. **Ein pauschales Verschieben wuerde die falschen Stellen
mittreffen.**

### Die Regel, aufgestellt und geprueft am 29.08.: das Format sagt, welche Generation gilt

| Schreibweise | Bedeutung | Zahl in `doc/` |
|---|---|---|
| **`b2 chNN:LL`** | **aktuelle Nummerierung, mit Zeilennummer.** Gueltig | **521** |
| **`KNN`, `b2 KNN`, `Kapitel N`** | **alte Nummerierung.** Vor dem Benutzen im Text nachschlagen | **476** |

**Und die erste Zeile ist nachgewiesen, nicht behauptet:**
`python werkzeug/belege.py --kapitel` meldet am 29.08. **null Zitate unter
der falschen Kapitelnummer.** Alle Verweise im `chNN:LL`-Format sind gegen
den Text geprueft.

**Damit ist der Drift sichtbar statt unsichtbar.** Wer eine Nummer im
alten Format sieht, weiss ohne Nachdenken, dass er sie nachschlagen muss.
**Wer eine im neuen Format sieht, darf sie benutzen.**

**Die 476 alten Stellen sind einzeln aufgefuehrt in
`archiv/VERWEISE-OFFEN.md`** und werden umgehaengt, wenn jemand sie
anfasst - nicht auf Vorrat.

**Fuer neue Eintraege gilt ab sofort: nur noch `b2 chNN:LL`.** Wer im alten
Format schreibt, erzeugt eine neue Altlast.

**Was immer stimmt, ist `erzeugt/KAPITEL.md` und `erzeugt/REGISTER.md`.** Beide
werden aus den Kapitelkoepfen erzeugt und koennen nicht driften.

---

## Kalender und Kapitelstand

Tag 1 ist Samstag, der 4. Oktober. Jede Datumszeile laesst sich daraus
nachrechnen, und `check.py` tut das automatisch.

### Das Jahr

**Ermittelt am 26.08. Das Jahr stand bis dahin in keinem Dokument, obwohl es
seit Band 1 im Werkzeug festgeschrieben ist.**

**`DAY1 = 2025-10-04` in `werkzeug/check.py`.** Daraus:

| | Tag | Datum |
|---|---|---|
| **Band 1, Kapitel 1** - die Auktion | 1 | Sa **4. Oktober 2025** |
| Band 1, Ende | 149 | So 1. Maerz 2026 |
| **Band 2, Kapitel 1** | 150 | Mo 2. Maerz 2026 |
| **frueheres Kapitel 90** | 415 | So 22. November 2026 |
| **Band 2, Kapitel 89** | 590 | So **16. Mai 2027** |
| **Band 2, Kapitel 90** - Bandende | 590 | So **16. Mai 2027** |
| **Band 3, Kapitel 1** | 592 | Di **18. Mai 2027** |
| **Band 3, Kapitel 2** - der neunundvierzigste Tag | 600 | Mi **26. Mai 2027** |

**Band 1 spielt also im Herbst und Winter 2025/26. Band 2 laeuft vom 2. Maerz
2026 bis zum 16. Mai 2027 und damit ueber die Jahresgrenze**; die Kapitel 76 bis
90 spielen im Jahr 2027 - Kapitel 76 faengt an Tag 460, dem 6. Januar, an. Bis zum Umbau endete der Band im November 2026, und
alle Jahresspannen im Text waren auf 2026 gerechnet. Die Wochentage sind ueber alle 126 Kapitel geprueft und stimmen:
Kapitel 62 sagt *"Sunday 23 August"*, der Kalender sagt Sonntag; Kapitel 90 sagt
*"Sunday 16 May"*, der Kalender sagt Sonntag.

**Offene Epilogklammer in Band 2, Kapitel 89:** Mr Ims Wirkungskette beginnt im
Januar 2027 und umfasst zwei Essen im Februar sowie eines im April. Die
Einleitung *"Between the nineteenth of March and the end of April"* schliesst
die ersten drei davon aus und muss **Between January and the end of April**
lauten; festgehalten in `doc/31-plan-band-2.md`.

**Annies Alter ist jetzt eindeutig.** `b2 ch78` sagt: im Fruehjahr 2002
vierzehn, seit fuenfundzwanzig Jahren am Tisch, mit dreissig verstanden und seit
neun Jahren gewusst. Mit dem gefuehrten Geburtstag 18. September ist sie im
Januar 2027 **39**. `b1 ch30` sagt nun *"since I was thirty-one"*; die
Familienfinanzen fuehrt sie laut `b1 ch15` seit 2009.

**ZWEI JAHRESANGABEN WIDERSPRACHEN DEM KALENDER, und die erste ist am 26.08. als
erledigt verbucht worden, ohne dass sie je im Text ankam:**

1. **"Twenty-three years ago" fuer 2002.** Am 26.08. wurden vierzehn Stellen in
   acht Kapiteln benannt und der Fall geschlossen. **Am 28.08. nachgemessen: kein
   einziges Kapitel trug die Aenderung.** Weder die Altfassungen im Archiv noch
   der Kanon; `archiv/band-2-vor-umbau/ch61_v1_4_en.md:222` und das heutige
   `chapters-2/ch71` sagten beide unveraendert *"twenty-three years ago"*.

   **Das ist die teuerste Sorte Eintrag: ein Bericht, der eine Korrektur
   beschreibt, die es nicht gibt.** Wer ihn liest, sucht nicht mehr. Die Regel
   dagegen steht in `doc/22-pruefen.md`: **die Wirkung pruefen, nicht den
   Schreibvorgang.**

   **Ausgefuehrt am 28.08., und diesmal nachgemessen: 23 Ersetzungen in zwoelf
   Kapiteln.** Weil der Band seit dem Umbau ueber die Jahresgrenze laeuft, ist
   die Zahl nicht mehr einheitlich:

   | Handlungsjahr | 2002 liegt zurueck | Kapitel |
   |---|---|---|
   | 2026 | **vierundzwanzig** | 17, 29, 63 (fuenfmal), 64, 67 (zweimal) |
   | 2027 | **fuenfundzwanzig** | 71 (zweimal), 72 (dreimal), 75, 76, 77 (zweimal), 79, 80 (dreimal) |

   **Der letzte Ausreisser ist korrigiert:** `b2 ch69 v3.5`, am 11. Dezember
   2026, sagt nun auch am Szenenanfang *"Twenty-four years ago there was a
   customs matter"*. Die spaeteren Nennungen derselben Szene stimmen damit
   ueberein.

   **Nicht angefasst, weil richtig:** Mrs Jeons dreiundzwanzig Jahre hinter dem
   Glas (sechzehn Stellen), Mr Chaes dreiundzwanzig Jahre Urkunden, der Neffe von
   dreiundzwanzig, die dreiundzwanzig uebrigen Namen in 30 und 78 - und
   **Chois dreiundzwanzig Jahre Kaeufe in dem
   Haus** (`ch80:274`), weil das eine eigene Spanne ab 2004 ist und nicht an 2002
   haengt. Dass in derselben Replik *"twenty-five"* und *"twenty-three"*
   nebeneinander stehen, ist kein Fehler, sondern die Aussage: er war der Mann,
   bevor er anfing zu kaufen.
2. **"I arranged that in 2014"** fuer den Trust, den Kapitel 87 auf *"eleven years
   ago"* datiert, steht jetzt auf **2015**. Eine Stelle: Kapitel 88. Geaendert
   wurde das Jahr und nicht die elf, weil die elf Jahre an fuenf Stellen haengen
   (42, 44, 45, 87, 88) und das Jahr nur an einer.

**Beide lasen sich, als haette jemand vom Startjahr 2025 aus gerechnet statt vom
laufenden Handlungsjahr.** Der Kalender hat entschieden, weil an ihm 124
gepruefte Datumszeilen haengen.

**NICHT ANGETASTET: Mrs Jeons dreiundzwanzig Jahre im Settlement.** Die Zahl
kommt ueber dreissigmal vor (Kapitel 6, 7, 27 bis 34, 71, 78, 83) und hat mit
2002 nichts zu tun. **Wer hier je wieder sucht, muss die beiden Bestaende
trennen, bevor er ersetzt.**

**AM 01.09. IM ROMANTEXT KORRIGIERT:** `b2 ch77 v3.2` und `b2 ch78 v3.2`
sagen jetzt *"nine years"*. Das entspricht 2002, vierzehn, dreissig und
fuenfundzwanzig Jahren am Tisch sowie dem gefuehrten Geburtstag.

### Kalender

**Tag 1 ist Samstag, der 4. Oktober.** Ohne Jahresangabe, und das Jahr wird nirgends genannt. Erzwungen wird das durch Kapitel 12, wo Kang sagt "On Saturday you asked me for guidance": Tag 22 muss ein Samstag sein, und 21 ist durch sieben teilbar, also ist Tag 1 ebenfalls Samstag.

**Jedes Kapitel trägt eine Datumszeile.** Kapitel mit mehreren Abschnitten bekommen sie als Zwischenüberschrift (`## Day Thirty-One · Monday 3 November`), Kapitel an einem Tag als Kursivzeile direkt unter dem Titel (`*Day 22 · Saturday 25 October*`). Spannt ein Kapitel über zwei Tage, steht die Spanne dort (`*Days 27 to 28 · Thursday 30 to Friday 31 October*`). Die Nacht nach der Auktion und die Nacht nach der Gala zählen jeweils zum Vortag, weil sie erzählerisch dazugehören.

**Kapitellängen.** Der Median liegt bei etwa 2800 Wörtern, die Spanne zwischen 2000 und 4300. Wird ein Kapitel deutlich länger, ist es zwei. Kapitel 14 stand bei 6475 und wurde an der Tagesgrenze geteilt.

**Kapitelüberschriften mit Datum.** Wo ein Kapitel datierte Abschnitte hat, steht der Wochentag und das Datum dabei: `## Day Thirty-One · Monday 3 November`. Das ist Leserführung und gilt ab jetzt für jedes datierte Kapitel.

**Ein Kapitel hat nicht zwingend einen Tag, und die erste Datumszeile ist nicht der Tag des Kapitels.** Sieben Kapitel haben mehrere Abschnitte: **5** (vier Tage), **12**, **14**, **27** und **28** (je drei), **26** und **34** (je zwei). Kapitel 14 laeuft ueber die Tage **31, 33 und 34**.

**Am 23.08. hat das eine richtige Angabe in `doc/11-figuren.md` kaputtkorrigiert.** Dort stand, Annie bekomme bis **Tag 34** kein Laecheln. Beim Pruefen wurde die erste Datumszeile von Kapitel 14 gelesen, *Day Thirty-One*, daraus geschlossen, das Kapitel sei Tag 31, und die richtige Zahl in eine falsche geaendert. *And then he smiled* steht im Abschnitt **Day Thirty-Four**. Zurueckgenommen.

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
  **Offener Postweg:** Derselbe in Ulsan geschriebene und eingeschrieben
  versandte Brief liegt bei Georgijs Rueckkehr um 14:10 Uhr schon in Seoul.
  Das geht per Einschreiben nicht am selben Tag. Die Daten bleiben besser
  unangetastet, weil der 18. Maerz die spaeteren Formeln *sixteen days* und
  *a year ago today* traegt. Der kleinste Eingriff ist ein Kurierbrief gegen
  Empfangsnachweis statt Einschreiben; das bewahrt auch die Belegbarkeit.
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
- Tag 182, Fr 3. April: **die Bitte.** Zum ersten Mal seit dem 2. Maerz gibt es
  nichts zu berichten, und Annie sieht ihn deshalb an. Sie versucht es ihm
  abzunehmen und laesst ihn dann von der Leine: **der Deckel vom 11. Maerz ist
  aufgehoben.** Ihr Gegenwert sind die fuenf uebrigen Firmen der Spur. Danach
  Jang im Pfoertnerhaus (Band 2, Kapitel 12)
- Tag 187, Mi 8. April: Jang liefert zwei Tage frueh. Sechs Firmen, wovor jede
  Angst hat, und wem sie folgen wuerden. **Vier von fuenf nennen denselben Mann,
  und es ist nicht Nam** (Band 2, Kapitel 13)
- Tag 188, Do 9. April: **Yeongjong.** Er bittet Chairman Woo zum ersten Mal um
  etwas - und baut es so, dass es Woo nichts kostet, **damit die Schuld stehen
  bleibt.** Woo macht daraus sieben Jahre. Und gibt ungefragt den Januar-Fund
  her (Band 2, Kapitel 13)
- Tag 193, Di 14. April: **Mr Kwon.** Ein wahrer Satz ueber sieben Jahre, dann
  **"Ask her."** Und Mr Ku sagt zum ersten Mal seit Oktober etwas
  (Band 2, Kapitel 14)
- Tag 195 bis 200, Do 16. bis Di 21. April: der Anwalt schreibt an fuenf, drei
  lesen die Satzung, zwei rufen Nam an, **sie sagt beide Male die Wahrheit.**
  Kwon beantragt schriftlich eine Mitgliederversammlung (Band 2, Kapitel 14)
- Tag 202, Do 23. April: **die Mitgliederversammlung.** Sie sagt zweimal die
  Wahrheit und verliert alles. **Vier dafuer, eine dagegen, Cho enthaelt sich.**
  Kwon wird Vorsitzender. Georgij ist in Seoul und sucht parallel den Versender:
  **drei der fuenf Namen vom Januar-Essen stehen auf der Versandliste**
  (Band 2, Kapitel 15)
- Tag 199, Mo 20. April: **das Haus am Fluss nimmt keine Einlieferungen mehr an**
  (frueheres Kapitel 16, rueckblickend)
- Tag 204, Sa 25. April: **Mr Ok.** Zwei der drei Namen fallen ohne Aufwand weg.
  Der dritte hat am 12. Maerz um sechzehn Uhr vierzig eine Seite kopieren lassen,
  **zweimal**, und in seinem Buero steht keine einzige Anweisung. **Nach Georgijs
  eigener Probe ist er eine Hand.** Und die zweite Kopie ist irgendwo
  (frueheres Kapitel 16)
- Tag 206, Mo 27. April: **Mr Ok an seiner eigenen Mauer.** Erschreckt und
  sonst nichts. Er liefert den Januar-Mann: sechzig, nicht gross, hat nichts
  gegessen, wurde ohne Namen vorgestellt, rief in der ersten Maerzwoche an -
  **und sagte zum Abschied "I am glad we finally met", obwohl sie sich nie
  begegnet waren** (Band 2, Kapitel 16)
- Tag 206, Mo 27. April, abends: **Annie kennt ihn und sagt es zum ersten Mal.**
  Den Namen gibt sie trotzdem nicht, und diesmal mit dem echten Grund: **der Name
  ist das Einzige, was Georgij lesbar machen wuerde.** Statt dessen ein
  Verhaltensmerkmal, das mehr wert ist (Band 2, Kapitel 17)
- Tag 208, Mi 29. April: die Liste der neun Mahlzeiten wird geschrieben und
  **durchgestrichen** - Annie hatte *met* gesagt und er hatte *eaten with*
  gehoert. **Das Haus am Fluss schliesst fuer das Publikum**
  (Band 2, Kapitel 18, rueckblickend)
- Tag 209, Do 30. April: **der dritte Zug nach Ulsan.** Die drei Unglueck, die
  Entschuldigung fuer den 20. Maerz, der Neffe, und die Zusage ueber den
  Versender. Ihre Frage: **"Was it you, or was it her."**
  (Band 2, Kapitel 18)
- Tag 209, Do 30. April, nachts: **die Abrechnung.** Er hat den Termin gehalten.
  Er sagt die Wahrheit auf Annies zweite Bedingung: **einmal, anderthalb
  Sekunden, an einem Tor.** Und er bittet um den Deckel zurueck. **Sie sagt
  nein** (Band 2, Kapitel 19)
- Tag 213, Mo 4. Mai: **das leere Haus am Fluss.** Georgij nimmt Hwangs Regel
  auseinander und bekommt den Namen des Vorgaengers, der die vier Gebuehren
  genommen hat (Band 2, Kapitel 20)
- Tag 215, Mi 6. Mai: **Mr Byun in Seongdong.** Er kann sich nicht erinnern,
  welche vier. Georgij bietet ihm nichts an und nimmt trotzdem, was er hergibt:
  **die vierte Gebuehr kam vom Eigentuemer persoenlich, aus der eigenen Tasche**
  (Band 2, Kapitel 21)
- Tag 222, Mi 13. Mai: **Mrs Sunwoo bekommt den Namen Byun.** Drei Wochen, kein
  lautes Wort, kein unwahres. Am Tag darauf Annie, foermlich, weil sie zwei der
  vier ist. **Und der Eigentuemer sitzt seit Januar auf der dritten Etage der
  Adresse in Jung-gu, vor der Georgij im Maerz umgekehrt ist**
  (Band 2, Kapitel 22)
- Tag 224, Fr 15. Mai, zwanzig nach neun: **die Entscheidung faellt, und sie ist
  ein Formular.** Registerauszug ueber zehn Gesellschaften in Jung-gu, mit Datum
  und seinem Namen darauf (Band 2, Kapitel 23)
- Tag 227, Mo 18. Mai: **die erste der fuenf Haelften wird unterschrieben**,
  Kwons Teilhaber (Band 2, Kapitel 23)
  **Offener Widerspruch:** Band 2, Kapitel 87 datiert spaeter den Kauf aller
  fuenf auf November. Kapitel 23 und die Marktprognose in Kapitel 19 tragen
  dagegen den Mai-Juni-Zeitraum.
- Tag 228, Di 19. Mai, zwanzig vor drei: **Mr Yeom ruft im Haus an und verlangt
  Georgij mit Namen.** Einladung zum Mittagessen am Donnerstag
  (Band 2, Kapitel 23)
- Tag 230, Do 21. Mai: **das Mittagessen.** Yeom isst. Am dritten Tisch vom
  Fenster sitzt eine Stunde und zehn Minuten lang ein Mann vor einer Schale,
  die er nicht anruehrt. **Und die vierte Gebuehr hat Yeom selbst bezahlt**
  (Band 2, Kapitel 24)
- Tag 236, Mi 27. Mai: **der Stapellauf.** Sang-hoon hat Choi in acht Jahren
  nie essen sehen. **Und er gibt Georgij den Namen, ungefragt** - Choi Dae-ho,
  neunundfuenfzig, dritter von Hongs drei Namen am 25. Oktober
  (Band 2, Kapitel 25)
- Tag 236, Mi 27. Mai, abends: **er sagt den Namen im kleinen Zimmer**, und sie
  gibt den echten Grund fuer das Zurueckhalten her. **Choi kauft Menschen, und
  die vierte Zeile ist einer davon. Sie weiss es seit dem 20. Maerz**
  (frueheres Kapitel 27)
- Tag 237, Do 28. Mai: **das Haus am Fluss, fast leer.** Mr Hwang gibt die
  Adresse her - und ungefragt den 9. Januar: **Mrs Jeon hat ihm ein
  Schulheft hingehalten, und er hat es nicht angefasst.** Ihr letzter Tag war
  der 12. Mai (Band 2, Kapitel 26). **Der 9. Januar liegt im selben Jahr 2026:**
  Die Rueckblicke in Kapitel 80 und 83 verschieben diesen Gang mit *four years
  ago* faelschlich nach Januar 2023. Dort muss **last year** stehen; offen in
  `doc/31-plan-band-2.md`.
- Tag 238, Fr 29. Mai: **die Wohnung vier Haltestellen draussen.** Er bezahlt
  ihren Preis vom 16. Maerz mit dem Einzigen, was er hat: **er sagt ihr, dass er
  auf der Seite steht.** Und bekommt Los sechs, die Fruehjahrsauktion vor vier
  Jahren, den Schalter offen bis Mitternacht ohne Verrechnung, und vier
  abgerechnete Posten gegen dieselbe Fundstelle: **Blumen, zweimal. Ein Fahrer.
  Und ein Arzt, im Juli** (Band 2, Kapitel 26)
- Tag 238, Fr 29. Mai, zwanzig nach sieben: **er sagt es ihr, bevor er den Ertrag
  auf den Tisch legt.** Annie straft nicht, sondern korrigiert: **Mrs Jeon
  bekommt die Settlement-Stelle der Gwangyang-Firma, deren Haelfte seit dem
  18. Mai Annie gehoert** - mit dem Eigentuemernamen auf der ersten Seite.
  **Und er schlaeft zum ersten Mal in einem Raum ein, in dem sie ist**
  (frueheres Kapitel 30)
- Tag 239, Sa 30. Mai: **das Blumengeschaeft in Hyoja-dong.** Er fragt vorher um
  den Tag und bekommt ihn. Die Doppelbuecher geben zwei Lieferungen drei Wochen
  auseinander, **zwei verschiedene Adressen**, kein Kaertchen beim zweiten Mal
  und die Bleistiftzeile des Fahrers: *"Left at the desk. They would not give a
  room."* **Und den Namen des Bestellers: Sim** - der sich am Telefon bei einer
  Fremden dafuer bedankt, sie wiedergesehen zu haben, genau wie bei Yeom vor vier
  Jahren (Band 2, Kapitel 27)
- Tag 242, Di 2. Juni: **das Heft geht zurueck, und der Brief aus Gwangyang liegt
  schon da**, seit Samstag, Erstzustellung, abgeschickt in der Freitagnacht.
  Mrs Jeon benennt es als das, was es ist (*"I have been handled"*), nimmt es
  trotzdem und laesst sich den Unterschied sagen. **Und Georgij stellt die Frage,
  die er am Freitag nicht gestellt hat:** die Arztrechnung war ein Hausbesuch
  ausserhalb der Stadt, die Anfahrt dreimal so teuer wie der Termin, **und im
  Feld fuer den Namen standen sechs Zeichen, naemlich die Losnummer.** Er nimmt
  die Adresse nicht (Band 2, Kapitel 28)
- Tag 243, Mi 3. Juni: **er legt alles auf den Schreibtisch, bevor gefrühstückt
  wird.** Byuns Zettel, Hwangs Zettel, das kopierte Heft, die zwei
  Blumenbelege, das Notizbuch. **Erstes Mal, dass Annie die ganze Fadenlaenge
  sieht.** Sie verbietet ihm nichts, verlangt aber Meldung vor jedem Schritt an
  beide Adressen und setzt Jang auf die zweite - **von aussen, bevor sein Name
  irgendwo faellt.** *"You do not go near either address without telling me
  first. Not asking. Telling."* (Band 2, Kapitel 29)
- Tag 244, Do 4. Juni: **er liest das Notizbuch von vorn und findet den Satz
  zweimal.** Mrs Gwaks *"good to see us again"* und Sang-hoons Profil aus
  Kapitel 26 - *"He tells people he is glad they have finally met. The first
  time. When they have never met."* **Dass es Choi Dae-ho ist, wissen beide
  schon seit dem 27. Mai (Kapitel 27) - neu ist, dass zwei Fremde, die nie
  voneinander gehoert haben, unabhaengig denselben Satz bezeugen.** Annies
  eigenes Wissen seit ihrem vierzehnten Jahr war nie mehr als ihr Wort; das
  hier ist das erste Stueck, das nicht an ihr allein haengt. Sie stoppt trotzdem
  jede Bewegung fuer vier Tage - **niemand geht an eine der beiden Adressen,
  Sang-hoon erfaehrt nicht, dass eine Blumenverkaeuferin und eine Adresse jetzt
  in der Sache stehen** (frueheres Kapitel 34)
- Tag 244, Do 4. Juni: **Sang-hoon ruft an, zum ersten Mal in acht Monaten.**
  Georgij haelt die vier Tage, ohne zu luegen: *"Not entirely mine."* Jang
  bestaetigt separat, dass die zweite Adresse unberuehrt bleibt, und stellt
  ihm dieselbe Frage wie Sang-hoon, ohne es zu wissen - **wessen vier Tage
  sind das.** Annie zeigt am Abend elf von geplanten dreissig Namen (Band 2,
  Kapitel 35)
- Tag 248-249, Mo/Di 8./9. Juni: **Annies drei Ergebnisse und das Treffen mit
  Sang-hoon.** Einunddreissig Namen, elf davon mit unerklaerten Wendepunkten;
  ein Immobilienbesitz in Gangwon-do, vier Eigentuemer tief, der ein
  Pflegeheim ausserhalb Wonjus finanziert und keine Namen an der Tuer fuehrt;
  und ein einziges Mal, vor elf Jahren, an dem jemand ihn hat verlieren sehen -
  unbenannt. **Georgij bringt Sang-hoon nicht den Namen** (den hat Sang-hoon
  ihm selbst in Kapitel 26 gegeben) **sondern das erste Beweisstueck, das
  ausserhalb dieses Hauses steht** - und liefert damit trotzdem nur die Haelfte
  der eigentlichen Schuld (den Mann, nicht die vier Entscheidungen). **Sang-hoon
  liefert die andere Haelfte selbst zurueck: er hat seit Samstag unabhaengig
  dieselbe Grundstuecksakte verfolgt** (Band 2, Kapitel 30)
- Tag 255, Mo 15. Juni: **Mrs Jeons erster Arbeitstag bei Gwangyang laut
  Kapitel 35.** Das Blatt,
  das sie Hwang schuldig war, ist auf denselben Morgen datiert: *"He was correct
  about the desk. He was wrong about the book."* Kapitel 35 laesst den Brief mit
  Gwangyang-Poststempel jedoch schon an diesem Morgen um neun in Seoul ankommen;
  Kapitel 59 und 83 nennen sein Datum abweichend den 14. Juni. **Diese Kette ist
  offen.** Der kleinste widerspruchsfreie Ablauf ist: Schreiben am 15., Ankunft
  am Dienstag, dem 16., und beide spaeteren Rueckblicke ebenfalls auf den 15.
  **Auch die Leserzahl in beiden Rueckblicken ist offen:** Annie liest die Seite
  hier vollstaendig und zitiert sie. Georgij ist deshalb nicht neben Mrs Jeon
  der einzige Leser; korrekt sind Mrs Jeon, Georgij und Annie.
  Georgij haendigt das Blatt Hwang **nicht** aus - es sollte
  existieren, nicht gelesen werden. **Nebenbei: er nimmt sich zum ersten Mal
  seit dem Regentag Sang-hoons vier Entscheidungen wieder vor** - vier Initialen
  aus Sang-hoons eigenem Kalender, noch keine Namen (Band 2, Kapitel 31)

  **OFFEN seit dem Kontinuitaetsdurchgang vom 01.09.:** Dieser Arbeitsbeginn
  steht gegen `b2 ch61`, das Mrs Jeons gesamte Szene am 23. Oktober auf einen
  Beginn am 1. Oktober und genau dreiundzwanzig Tage im Betrieb baut. `b2 ch87`
  bestaetigt dagegen nochmals, sie fuehre die Settlement-Funktion seit Juni.
  Bis der Manuskriptentscheid gefallen ist, sind weder Juni noch Oktober als
  widerspruchsfrei bezahlt zu behandeln; die vollstaendige Gegenueberstellung
  steht in `doc/31-plan-band-2.md`.
- Tag 257, Mi 17. Juni: **Annie waehlt "Y", die juengste der vier Initialen,
  zuerst.** Sang-hoon nennt Yeom - und Georgij faengt den eigenen Fehler ab,
  bevor er ihn ausspricht: Yeom war laut Kapitel 25 selbst Empfaenger des
  Anrufer-Tics, kann also nicht gleichzeitig der Anrufer bei Sang-hoons
  Kartenabend gewesen sein. **Ein geteilter Anfangsbuchstabe ist kein Hinweis,
  nur der Schatten von einem.** Yeom bleibt vorlaeufig entlastet, die
  Restaurant-Buchpruefung steht noch aus (Band 2, Kapitel 32)
- Tag 259, Fr 19. Juni: **die Restaurant-Buchpruefung.** Vier Lokale bei Sinsa
  haben seit letztem Juli den Besitzer gewechselt; das gesuchte gehoert jetzt
  einer Frau, die nichts vom Vorbesitzer Mr Baek hat ausser einer kaputten
  Kaffeemaschine - **und die im April bereits einen zweiten Fragesteller
  hatte**, der beim ersten toten Punkt sofort abzog. Baek selbst, zwei Strassen
  weiter, bestaetigt: zwei Maenner, kein Dritter, **Yeom vollstaendig
  entlastet.** Der Begleiter, der die Karten vorschlug, hat gegessen - **also
  nicht Choi Dae-ho selbst**, sondern jemand in dessen Auftrag. Annie und
  Georgij ziehen am Abend eine unbewiesene, schwere Vermutung: **Choi hat
  Sang-hoon womoeglich absichtlich erfahren lassen** (Band 2, Kapitel 32)
- Tag 261, So 21. Juni: **Jangs Bericht nach sechzehn Beobachtungstagen.**
  Vier Autos morgens und abends (Rota, nicht Familie), Waeschelieferung
  dienstags, Lebensmittel freitags fuer sechs bis zehn Personen, ein Auto
  bleibt nur mittwochs ueber Nacht. **Ein alter Mann an der Bushaltestelle
  berichtet von einer Frau am Fenster im zweiten Stock, jeden Nachmittag
  zur selben Zeit, seit Jahren.** Licht in elf von sechzehn Naechten,
  immer aus bis zehn. Jangs Einordnung: *"Above the middle of it. Not
  anywhere near the top."* **Georgij wird das Grundstueck weiterhin nicht
  betreten - der naechste Schritt liegt bei Sang-hoons Grundbuchrecherche**
  (Band 2, Kapitel 33)
- Tag 262, Mo 22. Juni: **der Arzt-Faden, ganz vom Schreibtisch aus.**
  Elf registrierte Hausbesuch-Praxen landesweit vor vier Jahren, sechs
  sofort ausgeschlossen (Paediatrie, geschlossen, zu weit weg), eine
  Klinikgruppe wegen eigener Revision, zwei per Telefon als gewoehnliches
  Geschaeft bestaetigt. **Bleiben zwei - eine mit erloschener statt
  geschlossener Zulassung**, die andere von Kollegen gedeckt, die ihn nie
  aus der Naehe gesehen haben, aber als harmlos entlarvt, sobald Georgij
  ihre Klinik direkt anruft. **Dr. Oh Seung-min, vierundfuenfzig beim
  Hausbesuch vor vier Jahren, jetzt achtundfuenfzig.** Der Name geht an
  niemanden ausser Annie - nicht Sang-hoon, nicht Jang, nicht einmal ins
  Notizbuch ein zweites Mal (Band 2, Kapitel 34)
- Tag 270, Di 30. Juni: **Sang-hoons Grundbuchrecherche liegt vor.** Vier
  Eigentuemer sind vier Firmen tief plus ein Trust, verwaltet seit elf
  Jahren von Solicitor Baek Jun-ho (Yeouido, nicht der Koch). **Derselbe
  Trust steht hinter der erloschenen Arztzulassung** - einmal gebaut,
  zweimal benutzt. Zwei Daten, die nicht zusammenpassen wollen: **Trust
  gegruendet vor elf Jahren, Arztbesuch vor vier.** Georgij bringt eine
  dritte, duesterere Lesart ins Spiel: nicht zwei Gruende, sondern einer,
  der vier Jahre in seine Laufzeit versagt hat und einen Arzt brauchte.
  Sang-hoon setzt die Aufgabe: **klaeren, ob die Frau, die Jang beobachtet
  hat, dieselbe ist, fuer die der Trust vor elf Jahren gebaut wurde**
- Tag 273, Fr 3. Juli: **Sang-hoons vier Entscheidungen, zwei mehr datiert.**
  S (Maerz, vor vier Jahren) und H (Oktober, drei Jahre danach, sechs Wochen
  vor Hwangs Ankunft) haben jetzt Daten ohne Namen. K bleibt offen - Annie
  weist auf Orte ohne Rechnung: Golfplatz, Badehaus (Band 2, Kapitel 35)
- Tag 276, Mo 6. Juli: **Brandschutz-Meldung und Jangs Gasflaschen-Lieferwagen
  bestaetigen sich gegenseitig.** Medizinischer Sauerstoff wurde am
  Pflegeheim bei Wonju genau einmal gemeldet, im Juli vor vier Jahren, nie
  storniert. Jang beobachtet seit drei Wochen denselben Lieferwagen, nur an
  diesem Haus, ohne festen Rhythmus - vermutlich bestellt statt Routine.
  **Stuetzt Georgijs dritte Lesart** (eine Person, elf Jahre gehalten, vor
  vier Jahren verschlechtert), **beweist aber keinen Namen.** Annie bremst
  ausdruecklich. K weiterhin offen, jetzt mit ausgeschlossenem Ansatz
  (Golfclub-Mitgliederlisten nicht zugaenglich) (frueheres Kapitel 44)
  (Band 2, Kapitel 35)


**Das Jahr bleibt ungenannt, aber `check.py` rechnet mit dem 4. Oktober 2025.**
Der Februar hat damit achtundzwanzig Tage, und daraus folgen Tag 145 fuer den
25. Februar und Tag 149 fuer den 1. Maerz. Wer das Jahr verschiebt, verschiebt
beide.

### Die Fahrerwoche

**Die Tabelle endet mit Band 1, nachgetragen am 24.08.** Ab Maerz gibt es keinen
Wochenwechsel mehr: Mr Pyo faehrt Annie, Mr Ku faehrt Georgij. Gesagt wird es
einmal, in Band 2, Kapitel 2. Vorher liess Kapitel 4 (Tag 159), Kapitel 10
(Tag 172) und Kapitel 31 (Tag 239) Mr Ku in einer Pyo-Woche fahren, Kapitel 31
sogar am Wechseltag selbst - derselbe Fehler, den diese Tabelle weiter unten
fuer Band 1 schon einmal verbucht hat. Der Text will an diesen drei Stellen
Mr Ku (seine Schweigsamkeit ist ein laufendes Motiv), also ist der Dienstplan
gewichen und nicht die Figur. **Wer die Tabelle auf Band 2 anwendet, prueft
gegen eine Regel, die es dort nicht mehr gibt.**

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
Pyos Woche. Das ist der Fehler aus `doc/20-handwerk.md`, Punkt 2: ein Fahrer, der
laut Rota diese Woche nicht fährt. Er fällt keinem Skript auf und keinem Leser,
der nicht zurückblättert.

**Feste Termine voraus, ab Kapitel 21 im Text genannt und damit Kanon:**

- Mo 24. November (Tag 52): Annies Gebot auf Hanseong geht raus
- erste Dezemberwoche: Sang-hoon unterschreibt bei der Haelfte, die aussteigen will
- **Di 16. Dezember: Hanas Abend.** Georgij um sechs, Woo um sieben, die Kims um acht, Ye-rin um neun, Kang um halb zehn. **Der Fotograf ist von sieben bis neun da und dann nicht mehr**, und daran hängt alles Weitere: das Bild von Woo neben der Familie entsteht gegen zehn nach acht und steht am Donnerstag in zwei Zeitungen.

  **Woo bleibt bis halb zehn, und das ist eine Bitte, die Georgij noch stellen muss.** Der Grund steht in `doc/31-plan-band-2.md`: Ye-rin braucht einen Beweis und keine Hoffnung, sie steht auf keinem Bild und liest keine Zeitung über einen Fremden, also muss sie den Mann im Raum stehen sehen. Damit begegnen Woo und Kang sich für etwa vier Minuten in Hanas Halle. **Das bricht Woos Bedingung nicht**, denn die lautet wörtlich *"no photograph with a politician in it"* und nicht: keine Begegnung. Zu diesem Zeitpunkt ist kein Fotograf mehr im Haus.

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
der Spanne. Nach `doc/20-handwerk.md` Punkt 0 wird dafuer nicht gekuerzt.

## Der Juli ist betreten

**Ueberholt am 25.08. und stehengelassen als Zeitmarke.** Dieser Abschnitt
notierte am Vormittag, dass Band 2 mit den Kapiteln 46 und 47 zum ersten Mal in
die geparkte Strecke hineinschreibt, und nannte drei Geburtstage, die inzwischen
alle verschoben sind. **Wer hier nach Daten sucht, sucht falsch** - sie stehen im
Abschnitt darunter.

Was von ihm bleibt, ist die Beobachtung, wie schnell das ging: zwischen dem
Satz *"die Grenze kommt bald"* und dem ersten Alter, das gegen seinen eigenen
Geburtstag stand, lagen keine zwei Tage Schreiben.

## Geburtstage und Alter

**Wozu.** Ein Alter ohne Datum driftet. Chairman Woo war in Band 1 viermal
achtundsiebzig und in Band 2 zweimal fuenfundsiebzig, und niemand hat es gemerkt,
weil es keine Stelle gab, an der man nachsieht. Diese Tabelle ist diese Stelle.

**Wie die Geburtstage lagen, und warum das nicht mehr traegt.** Der Einfall war:
alle Geburtstage in den Juli, August oder September legen, weil das die einzige
Strecke war, die nicht erzaehlt wird. Damit hatte jede Figur ueber beide Baende
**genau eine** Altersangabe.

**Der Einfall ist am 25.08. eingeholt worden.** Band 2 steht bei Kapitel 69 und
dem **9. September** (Tag 341). Die Strecke, in der die Geburtstage geparkt waren, ist
erzaehlte Zeit geworden - und drei Altersangaben standen prompt gegen ihren
eigenen Geburtstag:

| Figur | Alter im Text | Kapitel, Datum | Geburtstag stand auf | waere also |
|---|---|---|---|---|
| Mr Yeom | dreiundsechzig | 53 und 55, 4. und 12. August | 15. Juli | vierundsechzig |
| Chairman Woo | achtundsiebzig, dreimal | 61, 23. August | 19. August | neunundsiebzig |
| Mrs Sunwoo | einundachtzig | 65, 1. September | 4. Juli | zweiundachtzig |
| Annie | siebenunddreissig, ausgerechnet | 61, 23. August: *"Two thousand and two is twenty-three years ago and she was fourteen."* | 3. August | achtunddreissig |

**Aufgeloest ueber die Geburtstage und nicht ueber den Text**, weil diese drei
Daten erfunden waren und nie in einem Satz standen - sie liegen jetzt hinter dem
1. September. Der Text bleibt unangetastet und behaelt recht.

**Und einer ist kein Buchhaltungsposten mehr:** Park Sang-hoons Geburtstag steht
**im Buch** und nicht in dieser Tabelle. In `b2 ch47`, am Tag 298: *"It was
Monday. It was my birthday. I did not want to spend the whole of it being sixty
in a restaurant."* Der Montag davor ist Tag 297, **Montag der 27. Juli 2026**,
und seither ist er sechzig.

**Genau deshalb ist er am 28.08. um fuenf Monate gealtert.** In `b2 ch75`, am
Tag 453, dem **30. Dezember**, stand noch *"I am going to go and be fifty-nine
at somebody"*. Das war fuenf Monate nach seinem sechzigsten. Die Zeile heisst
jetzt **sixty**, und ch71 steht auf v3.5.

**Wie das entstanden ist, und warum es niemand gesehen hat.** Ein Alter ist
richtig, wenn es geschrieben wird, und bleibt stehen, waehrend die Szene sich
im Kalender bewegt. Diese hier ist beim Zusammenlegen und Umnummerieren von
Band 2 an das Jahresende gerutscht, und die Zahl ist mitgereist. Der einzige
Ort, an dem das auffaellt, ist eine Liste, die jede Altersangabe neben den Tag
stellt, an dem sie faellt - und die gab es bis zum 28.08. nicht.

**Chois Alter in der Gegenwart stimmt.** `b2 ch25` nennt ihn am 27. Mai 2026
neunundfuenfzig, und fuenf Stellen am 18. Maerz 2027 nennen ihn *a man of
sixty*. Sein Geburtstag, der 18. November, liegt dazwischen.

**Sein historisches Alter ist ebenfalls korrigiert.** Mit diesem Geburtstag war
er am 11. April 2002 fuenfunddreissig. `b2 ch69`, `ch77`, `ch78`, `ch82`,
`ch84`, `ch86` und `b3 ch02` nennen ihn jetzt dort fuenfunddreissig.
`b3 ch02` setzt entsprechend fuenfundzwanzig Jahre seit dem Dienstende an.

**Das Fenster gibt es nicht mehr, und der Band ist fertig.** Band 2 endet auf
**Tag 590, Sonntag dem 16. Mai 2027**. Zwischen Tag 1 und Tag 590 liegen
**neunzehn Monate und zwoelf Tage** - **jedes Kalenderdatum kommt darin
mindestens einmal vor.** Es gibt also keine Parkposition mehr, nirgends, fuer
niemanden.

*Die Zahlen in diesem Absatz standen bis zum 28.08. auf Tag 415 und dem
22. November, aus der Zeit, als Band 2 dort endete. Der Schluss stimmte
trotzdem, weil eine laengere Strecke die kuerzere enthaelt - aber ein Satz,
der sich selbst nicht mehr nachrechnen laesst, wird beim naechsten Mal
geglaubt statt geprueft.*

**Am 26.08. sind vier Alter nachgezogen worden, alle nach demselben Verfahren
wie im August:** der Geburtstag ist erfunden und steht in keinem Satz
(nachgeprueft, alle vier Daten kommen im Text nicht vor), also weicht der
Geburtstag und nicht der Text.

| Figur | Alter im Text | zuletzt genannt | Geburtstag stand auf | jetzt |
|---|---|---|---|---|
| Baek Jun-ho | dreiundsechzig | b2 K89, 16. Mai 2027 | 26. September | **10. November** |
| Mrs Jeon Mi-ja | einundfuenfzig | b2 K64, 1. November | 24. Juli | **15. November** |
| Mrs Sunwoo | einundachtzig | b2 K89, 16. Mai 2027 | 29. September | **17. November** |
| Choi Dae-ho | sechzig | b2 K87, 18. Maerz 2027 | 8. September | **18. November** |

**Und einer hat dem Autor gehoert, und er hat ihn am 26.08. entschieden:
Georgijs Geburtstag ist der 28. Juni.** Der Autor hat zugleich entschieden,
dass der Auktionskatalog gilt. Damit ist er an Tag 1 sechsundzwanzig und wird
am 28. Juni des zweiten Erzaehljahres siebenundzwanzig. Die heutigen
Schlusskapitel nennen sein Alter nicht mehr; das oeffnet die Entscheidung
nicht wieder.

**Der fruehere Schlussstand mit neun November-Anrufen ist ebenfalls kein Kanon
mehr.** Im heutigen Schluss stirbt Choi am 8. April; B2 89 erzaehlt die Folgen
und B2 90 laesst Georgij Mord und Kollateralschaden gegenueber Annie
aussprechen. Der groessere Inhalt seiner Drohung ist Wirklichkeit geworden,
die zugesagte Jahresfrist aber nicht. Weil der Text den Fristbruch nicht
benennt, steht der Posten in `doc/13-zusagen.md` auf **OFFEN**.

| Figur | Alter | Geburtstag | Beleg |
|---|---|---|---|
| **Georgij** | 26 bei der Auktion, **27 ab dem 28. Juni des zweiten Jahres** | **28. Juni**, vom Autor am 26.08. gesetzt, und der Katalog gilt | Band 1, Kapitel 1, aus dem Mund des Auktionators: *"Lot fourteen. Male, twenty-six."* Dazu *"nine years old"* und *"seventeen years"* |
| **Annie** | **39 im Januar 2027** | **18. September** (war 3. August) | `b2 ch78`: vierzehn plus fuenfundzwanzig; mit dreissig verstanden und seit neun Jahren gewusst |
| **Park Sang-hoon** | 59 bis 26.07., **ab 27.07. 60** | 27. Juli, **im Text** | Band 2, Kapitel 43: *"It was my birthday... being sixty"*, Montag, der 27. Juli. Kapitel 48 am 20. Juli: *"I am fifty-nine"* |
| **Choi Dae-ho** | 35 im April 2002; 59 bis 17.11.2026, danach **60** | **18. November** (war 8. September) | `b2 ch25`, danach fuenfmal *a man of sixty*; historische Nennungen auf 35 korrigiert |
| **Chairman Woo Jae-sung** | 78 | **27. September** (war 19. August) | Band 1, Kapitel 18 und 19, viermal, davon einmal aus seinem Mund. Im Gewerbe **seit siebenundzwanzig**, also einundfuenfzig Jahre |
| **Mrs Sunwoo** | 81 | **17. November** (war 29. September, davor 4. Juli) | Kapitel 10 und 23. Kauft seit einundvierzig Jahren in dem Haus |
| **Nam Byung-hee** | 58 | 21. September | Kapitel 8, 11 (ihr eigener Brief), 19, 20, 21, 22 |
| **Mr Byun** | 68 | 30. August | Kapitel 22. Register sechsundzwanzig Jahre |
| **Mr Yeom** | 63 | **24. September** (war 15. Juli) | Kapitel 23 und 25 |
| **Mr Ok** | 56 | 2. August | Kapitel 16 |
| **Mrs Jeon Mi-ja** | 51 | **15. November** (war 24. Juli) | Kapitel 30; in Kapitel 6 aus Georgijs Blick *"somewhere near fifty"*. Dreiundzwanzig Jahre am Schalter |
| **Mr Hwang** | 54 bis 10. September 2026, danach **55** | 11. September | Kapitel 21 schaetzt *"He is about fifty"*; Kapitel 83 legt es aus seinem eigenen Mund fest: *"I am fifty-five and I have been the man who keeps everything since I was thirty"* |
| **Mr Hong** | 61 | 6. August | Band 1, Kapitel 7. Neunzehn Jahre am selben Tisch |
| **Cho** | 40 | 17. Juli | Kapitel 13 und 15 |
| **Kwons Partner** | 63 | 29. Juli | Kapitel 14 |
| **Dr Oh Seung-min** | 58 | 13. August | Kapitel 41; vor vier Jahren vierundfuenfzig |
| **Baek Jun-ho** | 63 | **10. November** (war 26. September) | Kapitel 42. Alter erneut in Kapitel 82: *"He is sixty-three and he has eleven trusts"* |
| **Nam Byung-hees Neffe** | 23 | 9. August | Kapitel 19 |
| **Hana Seo-yeon** | 51 | 22. Juli | Band 1, Kapitel 21, aus ihrem eigenen Mund: *"I have a house with nobody in it on Fridays, and I am fifty-one"* |
| **Kim Sung-ho** | 61 | 30. Juli | Band 1, Kapitel 26. Aelterer Bruder von Ye-rin, haelt den Titel |
| **Kim Do-yun** | 38 | 6. September | Band 1, Kapitel 9 und 11 (*"late thirties"*), Kapitel 26 |
| **Kim Ye-rin** | 54 | 5. August | Band 1, Kapitel 26, 28 und 30 |
| **Kang** | 43 | 25. August | Band 1, Kapitel 11 |
| **Mr Chae** | 58 | 3. September | Band 1, Kapitel 25, aus seinem eigenen Mund |
| **Mr Kwon** | 54 | **30. September** | **frueheres Kapitel 69, aus seinem eigenen Mund:** *"I am fifty-four and I have been doing this since I was twenty-two, and work does not arrive."* Neun Lastwagen auf einer Spur aus Ulsan, eine der fuenf Firmen |
| **Sim** | 63 | **1. Oktober** | **frueheres Kapitel 68, aus seinem eigenen Mund:** *"I am sixty-three. I have got one instrument and I have just found out what it was for."* Dazu im selben Kapitel *"a man of sixty-odd"*. Dreissig Jahre im Dienst |
| **Mrs Ha** | **in ihren Sechzigern** | **offen** | Kapitel 72 und 89: *"Mrs Ha is in her sixties"* bzw. *"A woman in her sixties"*. Dreissig Jahre |
| **Ahn Jung-hee** | **35 im November 2026** | **offen** | Kapitel 53, 57, 59, 61 und 64. Bei ihrem Weggang vor vier Jahren einunddreissig |
| **Mr Ahn** | **39 im Oktober 2026** | **offen** | Kapitel 62: *"a man of thirty-nine who mends small motors"*. Vier Jahre aelter als Ahn Jung-hee |
| **Moon Hae-sook** | **52 am 19. Januar 2027** | **offen** | Kapitel 80: *"She is fifty-two."* |
| **Mr Im (Mullae)** | **57 am 30. Dezember 2026** | **offen** | Kapitel 75, aus seinem eigenen Mund: *"a man of fifty-seven"*. Nicht Mr Im aus Annies Wartungsrota |
| **Mrs Gwak** | etwa 70 | **offen** | Kapitel 31: *"about seventy"*. Schaetzung des Erzaehlers. Kein Geburtstag, solange die Zahl weich ist |
| **Jang** | **58** | **offen** | Kapitel 72, am 21. Dezember aus seinem eigenen Mund im Wagen: *"I have got a street and a coffee and I am fifty-eight"*. Dreissig Jahre im Gewerbe (12, 13, 40) |
| **Mrs Seo** | **offen** | **offen** | Neun Jahre im Haus, kein Alter im Text |

**Zuschreibung korrigiert am 1. September:** Der Satz mit der Strasse, dem Kaffee
und den achtundfuenfzig Jahren gehoert Jang. Mrs Ha erscheint erst im Absatz
danach und wird dort bereits als *in her sixties* eingefuehrt. Der fruehere
2.-Oktober-Geburtstag fuer Mrs Ha hatte deshalb keine Textgrundlage.

**Die Regel dazu.** Wer eine Altersangabe schreibt, holt sie hier. Wer eine
aendert, aendert sie hier zuerst. Wer eine Figur neu einfuehrt und ihr eine Zahl
gibt, traegt sie mit einem Geburtstag hinter der Erzaehlfront ein - Stand 25.08.: **nach dem 7. September**,
**bevor** die Zahl in einen Satz kommt - und prueft, ob das Fenster ueberhaupt
noch existiert. Und wer ein Alter aus einer anderen Zahl ableitet -
*"since I was twenty-four"*, *"eight years at that table"* - rechnet beide
Richtungen nach, weil genau dort der Fehler bei Woo entstanden ist: das Alter
wurde geaendert und die abgeleitete Zahl blieb stehen.

---

## ~~OFFEN:~~ ERLEDIGT: Kapitel 20 zaehlte fuenf Mitteilungen, von denen vier noch
nicht stattgefunden haben konnten (25.08.)

**Gefunden beim Nachpruefen der Kapitel 20 (v1.8) und 69 (v1.1), beide am
25.08. neu.** Die Zusage vom 3. April ist damit eingeloest, und das haelt - der
Doppelbeleg steht unten. Ein Absatz in Kapitel 20 zaehlt aber gegen sich selbst.

**Kapitel 20 spielt am Donnerstag, dem 30. April.** In demselben Bericht steht:

| | |
|---|---|
| **Vergangenheit** | *"Every one of the five was told who asked Chairman Woo, individually, by me, **on the day he signed**... I drove to four yards and a kitchen and I said the same sentence in the same words **five times**."* |
| **Zukunft, elf Zeilen vorher** | *"Mr Kwon signed on the twenty-seventh. **The other four sign Chairman Woo's paper in the first week of May.**"* |

**Am 30. April hat also genau einer von fuenfen unterschrieben.** Vier
Unterschriften liegen eine Woche in der Zukunft, und mit ihnen vier der fuenf
Mitteilungen - die er im Perfekt und mit Zahl berichtet.

**Die entlastende Lesart traegt nicht.** Man koennte *"the day he signed"* auf
**Woo** beziehen und alle fuenf Besuche auf einen Tag legen. Dagegen steht
zweierlei: der Text datiert Woos eigene Unterschrift **nirgends**, und Kapitel
69 verankert es an der Firma - Mr Kwon: *"On the **twenty-seventh** of April
you drove into my yard and told me who had asked Chairman Woo"*, und der 27.
ist laut Kapitel 20 **Kwons** Unterschriftstag. Jede Mitteilung faellt also auf
den Unterschriftstag der jeweiligen Firma.

**Vom Autor entschieden am 25.08.: Weg 2, die Unterschriften wandern.** Kapitel
20 steht jetzt auf v1.9: *"All five have signed Chairman Woo's paper, seven
years, the same document as the anchor cargo. **Mr Kwon was the last of them, on
the twenty-seventh.**"* Damit ist das Perfekt gedeckt, und Kwons
Unterschriftstag bleibt der 27. - den braucht Kapitel 69.

**Eine Folgestelle musste mit**, und nur eine: Kapitel 69 sagte *"The five firms
have been Woo's customers since the first week of May"* und sagt jetzt *"since
the end of April"* (v1.2).

**Und es passt besser als vorher.** Kapitel 14 hatte Kwon ohnehin als letzten:
*"The fifth was Mr Kwon. He answered the third question in nine words."* Er war
schon dort der Fuenfte, jetzt ist er es auch beim Unterschreiben.

**Nicht angefasst und geprueft unberuehrt:** *"The five halves come onto the
market between the middle of May and the middle of June"* (das sind die
Teilhaber-Haelften, ein anderer Vorgang), Mr Hwangs erste Maiwoche in Kapitel 56
(die Abrechnungsbuecher), und Georgijs *"I have known that since about the first
week of May"* in 69 - er hat es ein paar Tage nach den Unterschriften begriffen,
und das stimmt weiter.

**Neuer Stand vom 01.09.:** Der damalige Abgleich war fuer Kapitel 19, 20, 23
und 69 richtig. Die spaeter hinzugekommene Schlussfassung von Kapitel 87 sagt
jedoch *"you bought five of them in November"*. Das widerspricht der ersten
Unterschrift am 18. Mai und dem ausdruecklich angesagten Mai-Juni-Fenster. Der
Kalender behaelt die belegte Mai-Zeile; der Manuskriptfund steht offen in
`doc/31-plan-band-2.md`.

**Weiterer Gegencheck vom 01.09.:** Auch der damalige Vermerk *nur Kwon ist
unterrichtet* ist im heutigen Kanon ueberholt. Die Kwon-Szene und die vier
Briefe existieren nur in geloeschten Fassungen; aktuell ist keiner der fuenf
unterrichtet. Die folgenden zwei Wege dokumentieren die damalige Entscheidung
und sind kein heutiger Kanonstand.

**Die beiden Wege, die zur Wahl standen:**

1. **Die Zahl an den Kalender anpassen** - nur Kwon ist unterrichtet, die
   uebrigen vier bekommen denselben Satz in der ersten Maiwoche. **Das ist die
   kleinere Aenderung und sie macht Kapitel 69 schaerfer:** Annies Anweisung
   *"Go back and tell all five that they do not owe me anything"* betrifft dann
   vier Leute, die er ohnehin noch sehen muss - und er faehrt trotzdem nicht.
2. **Die vier Unterschriften vorziehen**, dann stimmt das Perfekt. Kostet
   allerdings den Satz ueber die erste Maiwoche und die Kette dahinter.

**Was davon unberuehrt bleibt und geprueft ist:** die Zusage selbst. Kapitel 12
(v1.8) traegt **beide** Haelften, die 20 und 69 einzeln zitieren - *"the other
five will be yours, completely, not as customers and not as an arrangement"* und
*"in about three weeks they are going to be extremely grateful to somebody. That
somebody can be you."* Kein Widerspruch zwischen den beiden Kapiteln.
**Siebenundzwanzig Tage** vom 3. auf den 30. April gehen auf.

## Korrigiert am 24.08., Kanon ab jetzt

**Die zwei stehenden check.py-Fehler sind geprueft und bleiben.** Beide melden
eine Zahl-Konstante mit einem anderen Subjekt, und das Skript kann das nicht
sehen:

- **Band 1, Kapitel 6, Zeile 40:** *"Male, twenty-two, two languages."* Das ist
  ein anderes Los im Katalog. Georgij hat vier Sprachen; hier steht ein anderer
  Mann auf der Buehne.
- **Band 1, Kapitel 12, Zeilen 28 und 56:** *"Jang came up from the security
  office at nine with two sheets of paper."* Das sind Jangs zwei Blaetter und
  nicht der Bericht, der acht, neun oder neunzehn Seiten hat.

Sie sind in der Basislinie verbucht und erzeugen keine neue Verschuldung. **Wer
sie im Lauf sieht, hat nichts gefunden.**

Drei Durchgaenge ueber Band 2: Zahlen und Zeitachse, Wissens- und Zusagenkette,
Punkt oder Fragezeichen. Die Begruendungen stehen in
`doc/41-entscheidungen.md`, was
offen blieb in `doc/31-plan-band-2.md`. Die Zahlen und Tatsachen, die ab jetzt gelten:

- **Chairman Woo: achtundsiebzig, im Gewerbe seit siebenundzwanzig.** Band 2,
  Kapitel 13 sagte zweimal fuenfundsiebzig und *"since I was twenty-four"*.
- **Mr Byun: sechsundzwanzig Jahre** am Register. Kapitel 22 sagte an der Tuer
  zweiundzwanzig, viermal vorher sechsundzwanzig.
- **Jang: dreissig Jahre** im Gewerbe. Kapitel 40 sagte zweimal zweiundzwanzig -
  das ist Mr Nohs Zahl aus `doc/11-figuren.md` und vermutlich von dort gerutscht.
- **Mrs Seo: neun Jahre** im Haus. Kapitel 24 sagte zweimal elf.
- **Mrs Jeon geht am 12. Mai.** Am 16. Maerz kuendigt sie selbst acht Wochen an,
  und sie behaelt recht. Kapitel 9 machte vier Tage spaeter sechs daraus. Ihr
  Rueckblick in Kapitel 61 verschiebt dieselbe Mitteilung faelschlich in den
  Januar; die Manuskriptkorrektur ist in `doc/31-plan-band-2.md` offen.
- **Hongs Bildungsfrage faellt bei zwoelf Minuten**, nicht bei vierzehn
  (Band 1, Kapitel 7).
- **Die vierte Gebuehr wurde am Abend des Loses bezahlt**, aus Yeoms eigener
  Tasche, in einem fertig gemachten Umschlag - nicht vier Jahre spaeter.
  Kapitel 29 und 33 hatten daraus *"last year"* und *"four years late"* gemacht.
- **Mr Kwon zeichnet am 27. April**, die anderen vier in der ersten Maiwoche.
- **Kapitel 34 kennt das Grundstueck in Gangwon-do noch nicht.** Es ist Annies
  Fund und kommt erst in Kapitel 36.
- **Sang-hoons Auftrag faellt am 27. Mai im Schuppen**, nicht im April.
- **Mr Byun verlaesst das Haus Ende Februar**, nicht im November, und hat Annies
  Kauf vom 4. Januar bis 19. Februar selbst abgewickelt - zehn Wochen nachdem
  Hwang die Praxis abgestellt zu haben glaubte. Hwang findet im Dezember drei
  Gebuehren, die vierte erst, als der Katalog beim Drucker liegt.
- **Sim weiss am 27. August, wofuer er telefoniert.** Georgij erklaert ihm an
  diesem Tag beide Frauen und den Dachsatz; Sim fuehrt den Anruf noch am selben
  Abend aus. Kapitel 59 verschiebt diese Erkenntnis faelschlich auf den 7.
  September; die Manuskriptkorrektur ist in `doc/31-plan-band-2.md` offen.
- **Die Warnung an den Wachmann steht jetzt im Wagen, wo sie hingehoert.**
  Kapitel 2 beruft sich nach dem Stich auf *"I did mention the collar
  wouldn't protect you."* - gesagt hatte er es nirgends. Statt den
  Rueckbezug zu aendern, ist der Satz nachgetragen: in Kapitel 1 bringt der
  Wachmann das Halsband selbst ins Spiel (*"it's got a collar on"*), und
  Georgij beantwortet beide Haelften seiner Rede - *"Three. Including the
  woman who pays you." ... "And the collar is on my throat. It has never
  once protected anybody else's."* Damit ist die Drohung angesagt, bevor
  sie eingeloest wird, und Annies *"You waited, though"* auf der Auffahrt
  bekommt einen zweiten Boden.
- **Die Gebotsleiter in Kapitel 1 hatte eine Luecke von vierzig Millionen.**
  Die Mitte stirbt bei hundertzehn, die Front stieg zwischen hundertfuenfzig
  und hundertsechzig aus - und danach steigt der Preis noch bis zweihundert,
  ohne dass jemand dagegenhaelt. Die Front steigt jetzt bis hundertneunzig aus.
- **Kapitel 17 sagte am Dienstag "on Tuesday".** Sang-hoon hat es ihm am
  Abend desselben Tages gesagt, beim Essen; zwei Tage spaeter, in Kapitel 18,
  ist dasselbe "on Tuesday" richtig. Steht jetzt auf *tonight*.
- **Die Lesefassung ist geteilt:** `book-band-1.md` und `book-band-2.md`.
- **Georgij hat in Band 2 keine eigene Kontraktion.** Der einzige Treffer ist ein
  Zitat: *"Tell her we haven't met."* (Kapitel 10). Siehe `doc/20-handwerk.md`,
  Abschnitt 2c.

---

**Der Protokollteil ist am 27.08. ausgezogen** und steht in
`doc/protokoll/2026-08-inhalt.md`: der Fund vom 26.08. zum Satz mit dem Wort zu
viel, die Erzaehlerkommentar-Durchgaenge, die Zuschreibungsdurchgaenge ueber
beide Baende und die sieben Band-1-Inhaltsdurchgaenge vom 25.08., zusammen
5.658 Woerter.

**Was hier absichtlich stehengeblieben ist:** *Korrigiert am 24.08., Kanon ab
jetzt.* Die Ueberschrift traegt ein Datum, der Abschnitt aber die verbindlichen
Zahlen des Buches - Woo achtundsiebzig, Byun sechsundzwanzig Jahre, Jang
dreissig, Mrs Seo neun. **Das ist Kanon in einem datierten Gewand** und gehoert
nicht ins Archiv.

---

# Aus dem Kapitelindex

*Bis zum 27.08. fuehrte das damalige `doc/05-continuity` eine Kapitelliste von Hand: **62.030 Woerter in zwei Bloecken**, von denen der zweite - Band 2 Kapitel 46 bis 90 - ohne eigene Ueberschrift unter einem Abschnitt ueber eine Handbewegung hing. Sie ist herausgenommen; das Geruest erzeugt `build.py` nach `erzeugt/KAPITEL.md`, die Nacherzaehlung steht im Buch, und was **bindend** war, steht hier.*

*Die vollstaendige Siebung mit allen 209 Eintraegen und der Regel, nach der gesiebt wurde, liegt in `protokoll/2026-08-27-kanonliste.md`. Der ganze alte Block liegt wortgleich in `protokoll/2026-08-27-ablage-vorher/`.*

56. **Zwei Fristen laufen einen Tag auseinander:** Annies Sperre endet mit dem Anfang des Maerz, also **Sonntag, 1. Maerz**; die Vollmacht stirbt am Ende desselben Sonntags **um Mitternacht**. Erst der **Montag** ist sein erster freier Arbeitstag. (Bis 23.08. stand hier faelschlich *"um dieselbe Mitternacht"*.)
57. **Die erste Vollmacht wird genau einmal benutzt:** Fristverlaengerung in Jung-gu am **23. Januar**, vier Minuten, weil er an dem Nachmittag der Einzige im Haus mit Zeichnungsbefugnis ist. Kein Erwerb, Verwaltung.
58. **Die zweite Vollmacht** (b2 K5): Gegenparteien **nur** Sang-hoon und der Schreibtisch im Settlement, Frist **31. Maerz**. Mr Chae hat sie **seit Montagnachmittag** - aufgesetzt am Tag der Absage.
59. **Am 16. Dezember ist nichts unterschrieben**, Woo feilscht noch.
60. **Die Fernbedienung, vier festgelegte Stellen:** Tag 1 neben die Schluesselschale, Tag 2 noch dort, **Tag 9 weg**, Tag 19 spricht sie ihn darauf an, **Tag 22 legt sie sie vor ihm in die Clutch.** Seither traegt sie sie am Koerper, **und er weiss es jede Minute.** *(Bindend: eine Fassung, in der er in b1 K22 ueberrascht ist, ist falsch.)*
61. **Nam schreibt am achtzehnten statt am Ersten**, und das Datum ist das Signal: *"I am writing to you on the eighteenth because I no longer have a first to wait for."* Ihr Aufschub geht bis zum **1. April**, nicht bis zum 26. Maerz.
62. **Die Zeile in Ulsan liegt seit dem 14. Maerz dort** - zwoelf Tage nach dem Paket vom 2. Maerz. *"Das ist nicht die Zeit zum Bemerken, das ist die Zeit zum Benutzen."*
63. **Der Sauerstoff:** die Adresse steht **genau einmal** in der Brandschutz-Meldeliste, **im Juli vor vier Jahren**, nie storniert.
64. **Die Lieferabstaende ueber vier Jahre: dreissig, vierundzwanzig, sechzehn, neun** - mit **einer Luecke von einundfuenfzig Tagen im zweiten Herbst**, mitten in einer Strecke von Vierundzwanzigern.
65. **Die Blumen:** **6. April** zwoelf weisse Stiele, Pyeongchang-dong mit Wohnungsnummer und Stock, Kaertchen ***"From an old friend."*** **27. April** dieselbe Bestellung, **andere Adresse ausserhalb der Stadt, kein Kaertchen** - und der Laden fragt immer. Dazwischen, auf derselben Zeile, **der Wagen vom 26.**
66. **Los sechs:** Fruehjahrsauktion vor vier Jahren, im Buch vom Januar davor bis zum September danach, vier abgerechnete Posten gegen dieselbe Fundstelle: **Blumen zweimal, ein Fahrer, ein Arzt im Juli.**
67. **K ist datiert: 24., 25. oder 26. Februar, vier Jahre zurueck.** S steht auf dem 20. Maerz. **Zweiundzwanzig bis vierundzwanzig Tage**, nicht drei Jahre. **H: Oktober, drei Jahre nach S, sechs Wochen bevor Hwang ins Haus kam.**
68. **Georgij hat vor elf Jahren einen Verlierer gehabt:** ein Zimmer, eine Hochzeit, die nicht stattfand, vier Jahre Ausland danach, zwei unabhaengige Zeugen mit dem Wort *"unrecognisable"*. **Kein Name.**
69. **Neun Mahlzeiten seit Oktober, ueber vierhundert Begegnungen.** Annie sagte **met**, er hoerte **eaten with**.

---

---

## Die Vernichtungskette, und warum kein Glied allein verschoben werden darf

**Sieben Termine, die einander tragen.** Jedes Glied steht inzwischen im Text.
Wer eines davon bewegt, ohne die anderen zu kennen, bricht drei Szenen. Genau
das ist am 27.08. schon einmal passiert, siehe `protokoll/`.

| Tag | Datum | Was daran haengt |
|---|---|---|
| 377 | Do 15. Okt 2026 | `b2 ch59`. Hwang erklaert die Nummernfolge. **Er kennt kein Datum**, ein Fonds entscheidet. Georgij bittet um den ersten Anruf statt den sechshundertvierzigsten Umschlag |
| 384 | Do 22. Okt 2026 | `b2 ch60`. Der Fonds hat entschieden, Hwang ruft um **zwanzig nach sieben** an. Annie haelt ihre Rede ueber neun Jahre zu Ende, **weil er sie nicht unterbricht**, und wird danach richtiggestellt. Sie unterschreibt |
| 395 | Mo 2. Nov 2026 | Der Kauf. Ihr Name geht mit dem Eintrag in die Folge |
| 510 | Do 25. Feb 2027 | `b2 ch83`. Klasse eins, neunzehn Kisten, ueber eine Brueckenwaage in Siheung. Zweitguenstigste von vier Offerten, weil die guenstigste kein Zertifikat anbot |
| 514 | Mo 1. Mrz 2027 | Das Zertifikat liegt in Georgijs Innentasche. Es bleibt dort |
| 517 | Do 4. Mrz 2027 | Klasse vier zuletzt, *"because there are people in them who are alive"* |
| 522 | Mo 8. Mrz 2027 | `b2 ch84`. Die siebenundzwanzig Einladungen gehen hinaus. **Nach dem Vernichtungstermin, und das ist kein Zufall** |
| 531 | Do 18. Mrz 2027 | Das Essen, `b2 ch86` mit Choi, `b2 ch87` die Bilanz. **Auf den Tag ein Jahr nach dem Brief** (`ch12`: *"The eighteenth of March." / "Sixteen days."*) |

**Ihr Name steht damit drei Monate und dreiundzwanzig Tage.** Vom zweiten
November bis zum fuenfundzwanzigsten Februar, einhundertfuenfzehn Tage.

### Der Mechanismus, in drei Saetzen

**Klasse ist Termin.** Hwang sortiert die Papiere des Hauses in vier Klassen,
und jede Klasse hat einen Tag. Klasse vier geht zuletzt, am vierten Maerz, weil
Menschen darin vorkommen, die leben.

**Index ist Klasse.** Indexieren heisst, festzuhalten, in welche Klasse etwas
gehoert. Und weil die Klasse den Termin traegt, entscheidet der Index, **wann**
etwas vernichtet wird. Was in keiner Klasse steht, bekommt keinen Termin und
liegt fuer immer.

**Deshalb ist Nachlaessigkeit in einem Archiv kein Verlust, sondern
Ueberleben.** Eine Aufbewahrungsfrist laeuft vom Datum auf dem Einlieferungs-
schein, und niemand oeffnet eine Kiste, um nachzusehen, ob das Papier darin aus
dem Jahr ist. Oeffnen ist eine Woche Arbeitszeit, das Formular ist umsonst.

### Wer was weiss, und wann

**Die Anzeige nennt ein Datum und keine Methode.** Sie sagt, dass das Haus nach
dem fuenfundzwanzigsten Februar nichts mehr haelt. Sechshundertvierzig Kaeufer
haben das im Oktober gelesen, und Hwang sagt im Februar voraus, dass jeder von
ihnen denselben Schluss zieht: **Archiv.** Er hat niemandem etwas anderes
gesagt, auch dem Fonds nicht.

**Choi ist einer der sechshundertvierzig.** Er hat den Umschlag im Oktober
bekommen wie alle anderen und musste niemanden fragen. Was er trotzdem nicht
wissen konnte, ist, ob es vollzogen wurde, und das herauszufinden haette
bedeutet, **ein Interesse geltend zu machen, schriftlich, mit seinem Namen
oben** (Klausel elf), in genau die Folge hinein, um die es geht. Der Mann, dem
alles zugestellt wurde, konnte die eine Frage nicht stellen.

**Darum bietet er am achtzehnten Maerz an, den Eintrag ordentlich indexieren zu
lassen.** Er plant an einem Gegenstand herum, den es seit drei Wochen nicht
mehr gibt, und Georgij hat das Zertifikat waehrenddessen in der Tasche und
nimmt es nicht heraus. **Das ist der Abstand zwischen den beiden Maennern:**
der eine denkt in Verbergen, der andere in Nichtexistenz.

### Und der Satz, der die Bilanz traegt

**Wissen ist kein Griff.** Ein Griff ist ein Haus, das gefragt, und ein Buch,
das aufgeschlagen werden kann. Fuenf Menschen wissen, was Annie getan hat, und
keiner von ihnen kann es beweisen; siebzehn weitere sassen am vierten Oktober
in demselben Saal; sechshundertvierzig haben einen Katalog in einer Schublade.
**Keiner von ihnen kann ein Blatt danebenlegen.**

Das Zertifikat ist der Gegenstand, der das belegt, und `ch79` sagt warum: *"It
does not give a lot, a buyer, a price or a name, because a certificate of
destruction is a document about paper and not about what was on it."*

## Der Zoll im Gebaeude der Kims, und die Zahl, die stehengeblieben war

**Der Zoll geht am Tag 16 hinein, dem 19. Oktober 2025.** Das Datum steht in
keinem Satz. Es ergibt sich aus vier Stellen, die es unabhaengig voneinander
einkreisen, und sie stimmen alle:

| Fundstelle | Tag | verstrichen | Text |
|---|---|---|---|
| `ch09:134` Hana auf der Terrasse | 22 | 6 | *for six days* |
| `ch11:116` Georgij berichtet | 22 | 6 | *six days* |
| `ch14:120` die dritte Sache | 34 | 18 | *eighteen days* |
| `ch17:68` gegen Sang-hoon | 46 | 30 | *a month* |
| `ch26:132` im Sitzungssaal, ab Tag 48 | 66 | 32 | *thirty-two days after* |

**Die sechste Stelle war falsch, und sie ist am 28.08. korrigiert worden.**
In `ch13:226` fragt Georgij Chairman Woo am Tag 27 nach einer Familie, die
*customs in a building for six days* hat. Sechs war Hanas Zahl vom Tag 22.
Fuenf Tage spaeter sind es elf, und der Satz steht jetzt so da. Kapitel 13
ist damit auf v2.11.

**Warum das kein Schoenheitsfehler ist.** Georgij sagt nie etwas Unwahres.
Der Satz ist als Hypothese gebaut - *if a family in your line of business
had* - aber die Zahl darin ist eine Tatsachenbehauptung ueber die Kims, und
Woo erkennt sie sofort als solche und sagt es ihm ins Gesicht. Eine falsche
Zahl an dieser Stelle bricht die erste Regel des Buches, nicht die
Genauigkeit.

**Und so entstehen diese Fehler.** Die Zahl war richtig, als sie geschrieben
wurde, und ist es geblieben, waehrend die Szene sich verschob. Wer eine
Replik von einem Tag auf einen anderen zieht, nimmt jede Zahl mit, die auf
den alten Tag gerechnet war.

**Die runden Angaben bleiben, wie sie sind.** `ch26:60` sagt *six weeks* fuer
siebenundvierzig Tage, `ch17:68` sagt *a month* fuer genau dreissig. Das ist
gesprochene Sprache, die auf die volle abgelaufene Einheit abrundet, und sie
ist in beiden Faellen richtig herum. Nur die gezaehlten Tage muessen stimmen.

## ~~OFFEN:~~ ERLEDIGT am 28.08.: Die fuenf Wochen in Kapitel 66

`ch66:282` steht als Georgijs eigene Nachschrift da:

> *The fourth of November is five weeks before the tenth of December.*

Zwischen den beiden liegen **sechsunddreissig Tage**, also fuenf Wochen und
ein Tag. Beide Daten sind gebunden und koennen nicht weichen: der vierte
November ist ein Mittwoch und wird zwei Zeilen vorher als *the Wednesday*
ausgewiesen, der zehnte Dezember ist der Donnerstag, an dem er Sim das erste
Mal anruft.

**Warum es ueberhaupt auffaellt.** Der Absatz handelt davon, dass die
Reihenfolge falsch notiert war und *the order is the whole of it*, und er
zaehlt daneben genau: *two days after*, *let it go eleven and nine*. In einem
Absatz, der so rechnet, ist eine gerundete Woche der einzige ungenaue Wert.

**Zur Entscheidung**, weil es eine Frage des Registers und nicht der Richtig-
keit ist:

* *five weeks and a day before* - genau, und das Nachzaehlen passt zu ihm.
* *thirty-six days before* - genau, und es nimmt Mr Oks eigene Zaehlweise
  aus demselben Kapitel auf, der auf dem Bus zweihundertdreiunddreissig Tage
  ausgerechnet hat.
* stehenlassen - vertretbar, weil *fuenf Wochen vorher* im Englischen die
  abgelaufene Einheit meint und der Rest wegfaellt.

**Gewaehlt wurde die Tageszaehlung.** Die Zeile heisst jetzt *"The fourth of
November is thirty-six days before the tenth of December."* Zeile 286
behaelt *five weeks*: das ist die zusammenfassende Erzaehlung danach und
keine Gleichsetzung. Kapitel 66 steht auf v3.3.

**Und eine Spanne bleibt gemeldet, ohne ein Fehler zu sein.** `spanne.py`
zeigt `b2 ch79:98`: Los sechs geht am 12. Februar ins Buch, die Auktion ist
am 28. Maerz, und der Satz sagt *open for seven weeks* - das sind
vierundvierzig Tage gegen neunundvierzig. Es geht auf, weil die sieben
Wochen nicht bis zur Auktion laufen, sondern bis zum Ausscheiden aus dem
Buch: das Los **hat nicht zugeschlagen** und stand danach weiter drin.
`b2 ch52:266` sagt dasselbe unabhaengig - *stayed in it for seven weeks*.
Wer diese Meldung wegmachen will, muesste einen der beiden Saetze
faelschen.

## Elf Jahre: gemessen am 28.08., und bewusst stehengelassen

Die Hochzeit ist *in der zweiten Aprilwoche vor elf Jahren*, der Trust wird
*in der zweiten Maerzwoche vor elf Jahren* errichtet. **Die Formel steht
rund zwanzigmal im Buch**, und ein Kapitel traegt sie im Titel: `b2 ch60`,
*Eleven years of paying for it*.

**Das Problem, und es ist echt.** Der Satz faellt aus Kapiteln, die im Juni
2026 spielen, und aus Kapiteln, die im Maerz 2027 spielen. Neun Monate
Abstand, dieselbe Formel:

| gesprochen in | Abstand zu Maerz 2016 | was man sagen wuerde |
|---|---|---|
| `ch30`, `ch32`, Juni 2026 | 10 Jahre 3 Monate | zehn |
| `ch51`, `ch53`, August 2026 | 10 Jahre 5 Monate | zehn |
| `ch61`, November 2026 | 10 Jahre 8 Monate | elf |
| `ch82`, `ch84`, Maerz 2027 | 11 Jahre | elf |

**Die harte Jahreszahl 2016 widerspricht an den Stellen zum urspruenglichen
Trust nicht.** Sie bezeichnet das Instrument, die ersten vier
Sauerstoffzahlungen und Baeks Entscheidung, danach nicht mehr zu fragen.

**Die Wohnung gehoert nicht in dieses Jahr.** In `b2 ch47` ist sie seit vier
Jahren Teil des Schedules, und in `b2 ch49` sagt Sim, sie sei sieben Jahre
nach Moon Hae-sooks Unterbringung hinzugefuegt worden. Baeks erster Blick auf
die Wohnung liegt deshalb 2022. `b2 ch81` trennt nun die zwei Versaeumnisse:
2016 liest er den Trust nicht gruendlich; 2022 fragt er wegen der neuen
Wohnung einmal nach und akzeptiert die bequeme Antwort. Der Termin am
2. Maerz ist entsprechend vier und nicht neun Jahre spaet.

**Entschieden: bleibt.** *Eleven years* ist im Buch keine Rechnung, sondern
der **Name** der ganzen Sache - so wie *lot fourteen* keine Losnummer mehr
ist. Sechs Kapitel aus dem Sommer 2026 auf *ten* umzustellen wuerde eine
Formel zerlegen, die als Formel arbeitet, und den Titel von `ch56` mitnehmen.

**Was dadurch NICHT verdeckt sein soll:** die Zahlen oben stehen jetzt da.
Wer den Anker spaeter verschiebt, sieht sofort, welche sechs Kapitel
mitmuessen.

## Was die vier Skripte entscheiden koennen, und was nicht

`werkzeug/register.py` sagt, welches Kapitel einen Tag erzaehlt. Alles
andere haengt daran.

`werkzeug/datumsprobe.py` zaehlt die Datumsangaben und sortiert sie nach
Pruefbarkeit. **Seine Hauptmeldung ist nicht ausloesbar**, solange die
Kapitel in Tagesreihenfolge stehen, und das steht seit dem 28.08. auch in
seiner Gegenprobe: geprueft wird jetzt die Reihenfolgepruefung selbst, die
Aufloesung nach Naehe und die Erkennung ausdruecklicher Jahresabstaende.

`werkzeug/wochentag.py` bindet Wochentage an Daten. **Vier Stellen im ganzen
Buch tun das**, alle vier stimmen. Die vierte ist B3 Kapitel 1: Mittwoch, der
26. Mai, und sie loest im dynamisch berechneten Handlungsfenster auf 2027 auf.
Eine kleine Zahl ist hier kein Mangel: es ist die einzige Zeitangabe, die ohne
Urteil entscheidbar ist.

`werkzeug/spanne.py` rechnet Spannen nach, **aber nur, wenn beide Enden im
selben Satz stehen**. Das sind zwei. Die weite Fassung meldete
dreiunddreissig, davon siebenundzwanzig Unsinn, und eine Liste mit dieser
Trefferquote wird nach zwei Durchgaengen nicht mehr gelesen. Die
eintausendvierhundert Spannen mit nur einem Ende bleiben Lesearbeit, und das
Skript sagt das auch.

`werkzeug/alter.py` stellt jede Altersangabe neben den Tag, an dem sie
faellt, und meldet die eine Sorte Widerspruch, die ohne Urteil auskommt:
**ein Alter geht nie zurueck.** Es ordnet acht Angaben zu und laesst
hundertvier liegen, weil *"a man of sixty"* niemandem gehoert. Das
Verhaeltnis ist Absicht - die erste Fassung ordnete alles zu, was einen
Namen in derselben Zeile hatte, und meldete neun Faelle, von denen neun
falsch waren.

**Es ist an der echten Zeile geprueft und nicht an einem Ersatzfall.** Wird
`ch71:302` sein alter Wortlaut untergeschoben, meldet es *Park Sang-hoon
geht zurueck, Tag 298: 60, Tag 453: 59*. Mit dem heutigen Wortlaut meldet es
nichts.

**Drei Dinge, die an einem Tag stillschweigend nichts geprueft haben**, und
die deshalb hier stehen:

1. Die Aufloesung sprang ueber den Vortag hinweg, weil sie nur *erzaehlte*
   Tage kannte. `ch18` spielt am 30. April und nennt den 29.; das landete ein
   Jahr spaeter.
2. Ein Satz, der zurueck- und vorausblickt, folgte dem Vorwaertsteil.
   `ch32` sagt *On the eighth of December I said this ... I am going to say
   it again now*, und der achte Dezember rutschte ins Jahr darauf.
3. Der Probelauf von `datumsprobe.py` stand auf Modulebene. Beim Import
   durch die beiden anderen Skripte beendete er deren Gegenprobe - lautlos,
   mit Rueckgabewert null. **Beide meldeten daraufhin nichts und sahen aus,
   als waeren sie durchgelaufen.**

Der dritte ist der teuerste, weil er die beiden anderen Pruefungen
unbemerkt abgeschaltet haette. Nach jeder Aenderung an einem dieser Skripte
gilt derselbe Satz wie fuer den Text: einmal absichtlich kaputtmachen und
nachsehen, ob es feuert.

## Historischer Umbau: Band 2 wurde zunaechst 89 Kapitel

**Am 28.08. ausgefuehrt.** Gegen einen Median von **2.512 Woertern** stand
ch29 bei **7.395** und ch26 bei **6.716**. ch35 ist am selben Tag bei 7.940
geteilt worden; diese zwei waren die letzten daneben.

**Spaeter wurde das damalige Schlusskapitel noch einmal geteilt; der aktuelle
Band hat neunzig Kapitel.**

**ch26 war der auffaelligere Fall:** sechstausendsiebenhundert Woerter ueber
zwei Tage mit **einem einzigen Szenentrenner**.

| alt | neu | Tag | Woerter | Titel |
|---|---|---|---|---|
| 26 | **26** | 237 | 2.396 | *The same sort of man* |
| 26 | **27** | 238 | 2.424 | *She has a list* |
| 26 | **28** | 238 | 1.912 | *A practice keeps records* |
| 29 | **31** | 243 | 1.506 | *The drawer that locks* |
| 29 | **32** | 244 | 3.995 | *Two witnesses* |
| 29 | **33** | 245 | 1.918 | *Whose four days* |

**Geschnitten wurde an den Tagesgrenzen**, plus bei ch26 an dem einen
vorhandenen Trenner, hinter dem ein Orts- und Stundenwechsel steht: *He got
back to the house at twenty past seven and went straight in.* **Kein Wort ist
geaendert worden** - die Probe hat beide Staende Wort fuer Wort verglichen,
221.569 zu 221.569.

**Die Titel sind aus dem jeweiligen Teil genommen**, wie im ganzen Buch.
*The same sort of man* ist Hwangs Satz, *A practice keeps records* faellt
zweimal hintereinander, *Whose four days* ist die Frage, mit der das Kapitel
endet.

**Fassungsnummern nach der Konvention der ch35-Teilung:** Hauptnummer plus
eins, Nebennummer null, fuer alle Teile.

### Was die Teilung an Verweisen gekostet hat, gemessen

Alles ab dem alten ch27 rueckt um zwei, alles ab dem alten ch30 um vier.

* **36 Schuldbuchadressen** neu gegen ihr woertliches Zitat gestellt.
* **18 Verweise** der Form `b2 chNN` in `doc/`.
* **163 Verweise** der Form `b2 KNN`, plus **19**, die auf die geteilten
  Kapitel zeigen und jetzt `(geteilt)` tragen.

**Und eine Annahme ist dabei an der Stichprobe zerbrochen**, was hier steht,
weil sie beim naechsten Mal wiederkommt. Ich hatte angenommen, die
`b2 KNN`-Verweise stuenden noch auf der Zaehlung vom 27.08. und brauchten
**+6**. `doc/11-figuren.md` sagt aber *"Choi hat im ganzen Buch keine Replik
ausser in b2 K82"*, und Chois einzige Szene ist heute ch86 und nicht ch88.
Sie standen also laengst auf der 85er-Zaehlung. **Ein Lauf mit +6 haette
hundertdreiundsechzig richtige Verweise zerlegt**, und keine Pruefung im Haus
haette es gemeldet.
