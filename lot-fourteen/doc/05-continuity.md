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
  (Band 2, Kapitel 16, rueckblickend)
- Tag 204, Sa 25. April: **Mr Ok.** Zwei der drei Namen fallen ohne Aufwand weg.
  Der dritte hat am 12. Maerz um sechzehn Uhr vierzig eine Seite kopieren lassen,
  **zweimal**, und in seinem Buero steht keine einzige Anweisung. **Nach Georgijs
  eigener Probe ist er eine Hand.** Und die zweite Kopie ist irgendwo
  (Band 2, Kapitel 16)
- Tag 206, Mo 27. April: **Mr Ok an seiner eigenen Mauer.** Erschreckt und
  sonst nichts. Er liefert den Januar-Mann: sechzig, nicht gross, hat nichts
  gegessen, wurde ohne Namen vorgestellt, rief in der ersten Maerzwoche an -
  **und sagte zum Abschied "I am glad we finally met", obwohl sie sich nie
  begegnet waren** (Band 2, Kapitel 17)
- Tag 206, Mo 27. April, abends: **Annie kennt ihn und sagt es zum ersten Mal.**
  Den Namen gibt sie trotzdem nicht, und diesmal mit dem echten Grund: **der Name
  ist das Einzige, was Georgij lesbar machen wuerde.** Statt dessen ein
  Verhaltensmerkmal, das mehr wert ist (Band 2, Kapitel 18)
- Tag 208, Mi 29. April: die Liste der neun Mahlzeiten wird geschrieben und
  **durchgestrichen** - Annie hatte *met* gesagt und er hatte *eaten with*
  gehoert. **Das Haus am Fluss schliesst fuer das Publikum**
  (Band 2, Kapitel 19, rueckblickend)
- Tag 209, Do 30. April: **der dritte Zug nach Ulsan.** Die drei Unglueck, die
  Entschuldigung fuer den 20. Maerz, der Neffe, und die Zusage ueber den
  Versender. Ihre Frage: **"Was it you, or was it her."**
  (Band 2, Kapitel 19)
- Tag 209, Do 30. April, nachts: **die Abrechnung.** Er hat den Termin gehalten.
  Er sagt die Wahrheit auf Annies zweite Bedingung: **einmal, anderthalb
  Sekunden, an einem Tor.** Und er bittet um den Deckel zurueck. **Sie sagt
  nein** (Band 2, Kapitel 20)
- Tag 213, Mo 4. Mai: **das leere Haus am Fluss.** Georgij nimmt Hwangs Regel
  auseinander und bekommt den Namen des Vorgaengers, der die vier Gebuehren
  genommen hat (Band 2, Kapitel 21)
- Tag 215, Mi 6. Mai: **Mr Byun in Seongdong.** Er kann sich nicht erinnern,
  welche vier. Georgij bietet ihm nichts an und nimmt trotzdem, was er hergibt:
  **die vierte Gebuehr kam vom Eigentuemer persoenlich, aus der eigenen Tasche**
  (Band 2, Kapitel 22)
- Tag 222, Mi 13. Mai: **Mrs Sunwoo bekommt den Namen Byun.** Drei Wochen, kein
  lautes Wort, kein unwahres. Am Tag darauf Annie, foermlich, weil sie zwei der
  vier ist. **Und der Eigentuemer sitzt seit Januar auf der dritten Etage der
  Adresse in Jung-gu, vor der Georgij im Maerz umgekehrt ist**
  (Band 2, Kapitel 23)
- Tag 224, Fr 15. Mai, zwanzig nach neun: **die Entscheidung faellt, und sie ist
  ein Formular.** Registerauszug ueber zehn Gesellschaften in Jung-gu, mit Datum
  und seinem Namen darauf (Band 2, Kapitel 24)
- Tag 227, Mo 18. Mai: **die erste der fuenf Haelften wird unterschrieben**,
  Kwons Teilhaber (Band 2, Kapitel 24)
- Tag 228, Di 19. Mai, zwanzig vor drei: **Mr Yeom ruft im Haus an und verlangt
  Georgij mit Namen.** Einladung zum Mittagessen am Donnerstag
  (Band 2, Kapitel 24)
- Tag 230, Do 21. Mai: **das Mittagessen.** Yeom isst. Am dritten Tisch vom
  Fenster sitzt eine Stunde und zehn Minuten lang ein Mann vor einer Schale,
  die er nicht anruehrt. **Und die vierte Gebuehr hat Yeom selbst bezahlt**
  (Band 2, Kapitel 25)
- Tag 236, Mi 27. Mai: **der Stapellauf.** Sang-hoon hat Choi in acht Jahren
  nie essen sehen. **Und er gibt Georgij den Namen, ungefragt** - Choi Dae-ho,
  neunundfuenfzig, dritter von Hongs drei Namen am 25. Oktober
  (Band 2, Kapitel 26)
- Tag 236, Mi 27. Mai, abends: **er sagt den Namen im kleinen Zimmer**, und sie
  gibt den echten Grund fuer das Zurueckhalten her. **Choi kauft Menschen, und
  die vierte Zeile ist einer davon. Sie weiss es seit dem 20. Maerz**
  (Band 2, Kapitel 27)
- Tag 237, Do 28. Mai: **das Haus am Fluss, fast leer.** Mr Hwang gibt die
  Adresse her - und ungefragt den 9. Januar: **Mrs Jeon hat ihm ein
  Schulheft hingehalten, und er hat es nicht angefasst.** Ihr letzter Tag war
  der 12. Mai (Band 2, Kapitel 28)
- Tag 238, Fr 29. Mai: **die Wohnung vier Haltestellen draussen.** Er bezahlt
  ihren Preis vom 16. Maerz mit dem Einzigen, was er hat: **er sagt ihr, dass er
  auf der Seite steht.** Und bekommt Los sechs, die Fruehjahrsauktion vor vier
  Jahren, den Schalter offen bis Mitternacht ohne Verrechnung, und vier
  abgerechnete Posten gegen dieselbe Fundstelle: **Blumen, zweimal. Ein Fahrer.
  Und ein Arzt, im Juli** (Band 2, Kapitel 29)
- Tag 238, Fr 29. Mai, zwanzig nach sieben: **er sagt es ihr, bevor er den Ertrag
  auf den Tisch legt.** Annie straft nicht, sondern korrigiert: **Mrs Jeon
  bekommt die Settlement-Stelle der Gwangyang-Firma, deren Haelfte seit dem
  18. Mai Annie gehoert** - mit dem Eigentuemernamen auf der ersten Seite.
  **Und er schlaeft zum ersten Mal in einem Raum ein, in dem sie ist**
  (Band 2, Kapitel 30)
- Tag 239, Sa 30. Mai: **das Blumengeschaeft in Hyoja-dong.** Er fragt vorher um
  den Tag und bekommt ihn. Die Doppelbuecher geben zwei Lieferungen drei Wochen
  auseinander, **zwei verschiedene Adressen**, kein Kaertchen beim zweiten Mal
  und die Bleistiftzeile des Fahrers: *"Left at the desk. They would not give a
  room."* **Und den Namen des Bestellers: Sim** - der sich am Telefon bei einer
  Fremden dafuer bedankt, sie wiedergesehen zu haben, genau wie bei Yeom vor vier
  Jahren (Band 2, Kapitel 31)
- Tag 242, Di 2. Juni: **das Heft geht zurueck, und der Brief aus Gwangyang liegt
  schon da**, seit Samstag, Erstzustellung, abgeschickt in der Freitagnacht.
  Mrs Jeon benennt es als das, was es ist (*"I have been handled"*), nimmt es
  trotzdem und laesst sich den Unterschied sagen. **Und Georgij stellt die Frage,
  die er am Freitag nicht gestellt hat:** die Arztrechnung war ein Hausbesuch
  ausserhalb der Stadt, die Anfahrt dreimal so teuer wie der Termin, **und im
  Feld fuer den Namen standen sechs Zeichen, naemlich die Losnummer.** Er nimmt
  die Adresse nicht (Band 2, Kapitel 32)
- Tag 243, Mi 3. Juni: **er legt alles auf den Schreibtisch, bevor gefrühstückt
  wird.** Byuns Zettel, Hwangs Zettel, das kopierte Heft, die zwei
  Blumenbelege, das Notizbuch. **Erstes Mal, dass Annie die ganze Fadenlaenge
  sieht.** Sie verbietet ihm nichts, verlangt aber Meldung vor jedem Schritt an
  beide Adressen und setzt Jang auf die zweite - **von aussen, bevor sein Name
  irgendwo faellt.** *"You do not go near either address without telling me
  first. Not asking. Telling."* (Band 2, Kapitel 33)
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
  in der Sache stehen** (Band 2, Kapitel 34)
- Tag 245, Fr 5. Juni: **Sang-hoon ruft an, zum ersten Mal in acht Monaten.**
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
  dieselbe Grundstuecksakte verfolgt** (Band 2, Kapitel 36)
- Tag 255, Mo 15. Juni: **Mrs Jeons erster Arbeitstag bei Gwangyang, und ein
  Brief kommt mit Gwangyang-Poststempel an: das Blatt, das sie Hwang schuldig
  war, datiert auf denselben Morgen.** *"He was correct about the desk. He was
  wrong about the book."* Georgij haendigt es Hwang **nicht** aus - es sollte
  existieren, nicht gelesen werden. **Nebenbei: er nimmt sich zum ersten Mal
  seit dem Regentag Sang-hoons vier Entscheidungen wieder vor** - vier Initialen
  aus Sang-hoons eigenem Kalender, noch keine Namen (Band 2, Kapitel 37)
- Tag 257, Mi 17. Juni: **Annie waehlt "Y", die juengste der vier Initialen,
  zuerst.** Sang-hoon nennt Yeom - und Georgij faengt den eigenen Fehler ab,
  bevor er ihn ausspricht: Yeom war laut Kapitel 25 selbst Empfaenger des
  Anrufer-Tics, kann also nicht gleichzeitig der Anrufer bei Sang-hoons
  Kartenabend gewesen sein. **Ein geteilter Anfangsbuchstabe ist kein Hinweis,
  nur der Schatten von einem.** Yeom bleibt vorlaeufig entlastet, die
  Restaurant-Buchpruefung steht noch aus (Band 2, Kapitel 38)
- Tag 259, Fr 19. Juni: **die Restaurant-Buchpruefung.** Vier Lokale bei Sinsa
  haben seit letztem Juli den Besitzer gewechselt; das gesuchte gehoert jetzt
  einer Frau, die nichts vom Vorbesitzer Mr Baek hat ausser einer kaputten
  Kaffeemaschine - **und die im April bereits einen zweiten Fragesteller
  hatte**, der beim ersten toten Punkt sofort abzog. Baek selbst, zwei Strassen
  weiter, bestaetigt: zwei Maenner, kein Dritter, **Yeom vollstaendig
  entlastet.** Der Begleiter, der die Karten vorschlug, hat gegessen - **also
  nicht Choi Dae-ho selbst**, sondern jemand in dessen Auftrag. Annie und
  Georgij ziehen am Abend eine unbewiesene, schwere Vermutung: **Choi hat
  Sang-hoon womoeglich absichtlich erfahren lassen** (Band 2, Kapitel 39)
- Tag 261, So 21. Juni: **Jangs Bericht nach sechzehn Beobachtungstagen.**
  Vier Autos morgens und abends (Rota, nicht Familie), Waeschelieferung
  dienstags, Lebensmittel freitags fuer sechs bis zehn Personen, ein Auto
  bleibt nur mittwochs ueber Nacht. **Ein alter Mann an der Bushaltestelle
  berichtet von einer Frau am Fenster im zweiten Stock, jeden Nachmittag
  zur selben Zeit, seit Jahren.** Licht in elf von sechzehn Naechten,
  immer aus bis zehn. Jangs Einordnung: *"Above the middle of it. Not
  anywhere near the top."* **Georgij wird das Grundstueck weiterhin nicht
  betreten - der naechste Schritt liegt bei Sang-hoons Grundbuchrecherche**
  (Band 2, Kapitel 40)
- Tag 263, Di 23. Juni: **der Arzt-Faden, ganz vom Schreibtisch aus.**
  Elf registrierte Hausbesuch-Praxen landesweit vor vier Jahren, sechs
  sofort ausgeschlossen (Paediatrie, geschlossen, zu weit weg), eine
  Klinikgruppe wegen eigener Revision, zwei per Telefon als gewoehnliches
  Geschaeft bestaetigt. **Bleiben zwei - eine mit erloschener statt
  geschlossener Zulassung**, die andere von Kollegen gedeckt, die ihn nie
  aus der Naehe gesehen haben, aber als harmlos entlarvt, sobald Georgij
  ihre Klinik direkt anruft. **Dr. Oh Seung-min, vierundfuenfzig beim
  Hausbesuch vor vier Jahren, jetzt achtundfuenfzig.** Der Name geht an
  niemanden ausser Annie - nicht Sang-hoon, nicht Jang, nicht einmal ins
  Notizbuch ein zweites Mal (Band 2, Kapitel 41)
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
  weist auf Orte ohne Rechnung: Golfplatz, Badehaus (Band 2, Kapitel 43)
- Tag 276, Mo 6. Juli: **Brandschutz-Meldung und Jangs Gasflaschen-Lieferwagen
  bestaetigen sich gegenseitig.** Medizinischer Sauerstoff wurde am
  Pflegeheim bei Wonju genau einmal gemeldet, im Juli vor vier Jahren, nie
  storniert. Jang beobachtet seit drei Wochen denselben Lieferwagen, nur an
  diesem Haus, ohne festen Rhythmus - vermutlich bestellt statt Routine.
  **Stuetzt Georgijs dritte Lesart** (eine Person, elf Jahre gehalten, vor
  vier Jahren verschlechtert), **beweist aber keinen Namen.** Annie bremst
  ausdruecklich. K weiterhin offen, jetzt mit ausgeschlossenem Ansatz
  (Golfclub-Mitgliederlisten nicht zugaenglich) (Band 2, Kapitel 44)
  (Band 2, Kapitel 42)


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

- **Band 2, Kapitel 8** *Nobody sent me* (v1.4) - **Tag 168, Fr 20. Maerz. Drei Szenen: der Donnerstagabend, die Fahrt, der Hof in Ulsan.**

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

  **Und was er ohne eine einzige Frage mitnimmt, weil er auf Schreibtische sieht:**
  Auf der Kante liegt **eine fotokopierte Einzelseite in einer Klarsichthuelle**,
  nicht der gebundene Katalog, den jeder Kaeufer im Maerz bekam. **Also hat
  jemand mit dem Band eine Seite herausgesucht** - der Bote steht auf der
  Kundenliste des Hauses. Dazu die eine harmlose Frage: *"How long have you had
  that."* - **"Since the fourteenth."**

  **Und das Datum traegt mehr als die Huelle.** Zwoelf Tage zwischen dem Paket
  am 2. Maerz und der Seite in Ulsan am 14. **Das ist nicht die Zeit zum
  Bemerken, das ist die Zeit zum Benutzen.** Dazu der schwerste Schluss: die
  Rueckseite traegt keinen einzigen Namen, eine Seite mit Los vierzehn ist also
  wertlos fuer jeden, der nicht schon weiss, wessen sie ist. **Er wusste es vor
  dem Paket. Das Paket war der Weg, es weiterzugeben, ohne der zu sein, der es
  weiss.** Und die Zeile bleibt unaufgeloest stehen: drei Namen auf dieser Liste
  hat er an einem Tisch sitzen sehen.

  **Und die Annahme, die ihn das kostet:** Er hat seit Mittwoch geglaubt, jemand
  habe sich mit ihr hingesetzt. Eine Seite in einer Huelle braucht kein
  Gespraech. **"A man who arranges a meeting can be found afterwards. A man who
  posts something cannot."**

  **Wer sie ihm gegeben hat, fragt er ausdruecklich nicht**, und das ist in der
  ersten Fassung schlicht vergessen worden. Der Grund ist derselbe wie spaeter
  in Kapitel 11: sie wuerde antworten und dabei begreifen, dass Seite, Woche und
  Person ausgesucht waren. **"A woman who has been used goes and finds out for
  herself. There is exactly one person she could go to."**

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

- **Band 2, Kapitel 11** *What she cannot prove* (v2.0) - **Tag 180, Mi 1. April. Vier Szenen: die verstrichene Woche, der Brief, das kleine Zimmer, und der Hof in Ulsan am selben Nachmittag.**

  **Fassung 1 hiess *In my own hand* und liess ihn die Antwort schreiben. Am 23.08. vom Autor verworfen, aus zwei Gruenden, und beide stimmen.**

  **Erstens: schriftlich ist ein Charakterbruch.** Er setzt seinen Namen nirgends hin - Kapitel 5 dreht sich vollstaendig darum, was ihn ein Name in einem Kondolenzbuch kostet. Zwei Wochen spaeter ein unterschriebenes Gestaendnis in die Post zu geben, ist nicht kalt, sondern unklug. Jetzt: *"I have spent one chapter of this year finding out what it costs to put my name in a book at a door. I am not going to sit upstairs and put it in an envelope."*

  **Zweitens: Hana weiss es laengst**, und Woo und Sang-hoon auch. Das steht seit Kapitel 8 v1.4 in seiner eigenen Rechnung - **drei Namen, mit denen er an einem Tisch gesessen hat.** Die alte Fassung liess ihn ausmalen, dass sie es erfahren wuerden, und widersprach damit direkt.

  **Was daraus geworden ist, ist besser.** Der Unterschied heisst nicht Geheimhaltung, sondern **Beweisbarkeit**: *"A woman of fifty-eight with no standing outside her own lane, saying that thing about this house, is a woman saying a thing. The same sentence in my writing is a document, and a document does not need her to be believed. It only needs to be found once."*

  **Und was er sich stattdessen ausmalt, benutzt die drei:** *"Every day since then, each of them has chosen not to say it. That is what it is at the moment. It is three people choosing."* Wenn Nam es ausspricht, wird aus drei Entscheidungen eine Sache, die jeder wiederholen darf, **und die drei muessen sie vor anderen noch einmal treffen.**

  **Annie ordnet nichts an, und der Grund ist ein anderer als in Ulsan im Maerz:** *"This one is yours because the thing you are proposing to give away is yours. It is the only thing in the world that is."* Ohne Beschoenigung: *"If she uses it, I will not be able to protect you from most of what follows."*

  **Mrs Seo hat den Umschlag vor neun hingelegt, ungefragt.** Zwei Fahrkarten, die zwoelf vierzig und die letzte zurueck. *"I am not clever, I am organised."* - **"You are both."** Und: nimm einen waermeren Mantel, Du wirst in einem Hof am Wasser stehen.

  **Der Hof, und sie ist nicht ueberrascht.** *"You could have written."* - **"No."** - *"No. I suppose not."* Er sagt es im Stehen, in sechs Saetzen, in der Reihenfolge, die er im Zug festgelegt hat. Sie setzt sich waehrend des vierten und er haelt nicht an.

  **Ihr erster Satz danach ist der beste, den sie bekommt:** *"That is why you would not let the man at the funeral write a figure next to your name. ... I had you down for a man with a criminal conviction."*

  **Warum er es tut, sagt er ihr auch:** *"Because you asked plainly, and you are the first person outside that house who ever has. And because you have had nothing but silence out of everybody since January, and it seemed to me that one person should tell you the whole of something."*

  **Und was sie ihm am Tor gibt, ist alles, was sie hat.** Sie wird es nicht wiederholen - **nicht aus Zuneigung**, und sie sagt dazu, dass er darauf nichts bauen soll: *"Since January something has been done to me by people who never had to say one word out loud. I have found out this month that I do not want to be that. And it turns out to be a thing you decide on a particular afternoon, and not once and for all."*

  **Er antwortet darauf nicht**, weil ihm nichts zur Verfuegung steht, das wahr und sagbar zugleich waere. *"He has been in that position perhaps four times in his life, and it has never once been on the receiving end."*

  **Der Schluss bleibt wie in Fassung 1 und wiegt jetzt mehr.** Um eins nachts, mit dem Fahrscheinabschnitt vor sich: wem die Wahrheit ueber jemanden gesagt wurde, hoert auf zu suchen - **und genau das tut man mit jemandem, den man stillstehen haben will.** Beides ist der Fall. Er legt keines vor das andere.

  **Und die letzte Zeile ist neu und zeigt weiter:** *"By the time she did, the house on the river had stopped taking new consignments, and it was not to Georgij."*

- **Band 2, Kapitel 12** *Sixteen days* (v1.3) - **Tag 182, Fr 3. April. Zwei Szenen: das kleine Zimmer, dann die Garagen.**

  **Der Ausloeser ist eine Leere.** Mrs Sunwoo braucht ihn nicht, die Ladung faehrt, die Vollmacht ist seit Dienstag weg. **Zum ersten Mal seit dem 2. Maerz steht er in dem Raum ohne Bericht** - und Annie kann ihn dadurch zum ersten Mal ansehen.

  **Sie loest den Tell aus Kapitel 7 ein, und zwar praezise und ohne Vorwurf:** *"You have been squaring things off since the eighteenth of March. Paper. Cups. The blotter, twice, in front of me. ... You do not fidget. You have never fidgeted in your life. You put things straight."* - **"Sixteen days," said Annie.**

  **Dann versucht sie, es ihm abzunehmen**, und das Argument ist gut: achtundfuenfzig, vier Lastwagen, ertrunken, und er hat ihr das Wasser genommen. *"That is normally the end of it."*

  **Seine Antwort hat zwei Haelften und er gibt sie in dieser Reihenfolge.** Erstens: **sie hatte recht**, jedes Wort, und wenn jemand Annie so behandelt haette, wuerde er ihn ohne zweiten Grund auseinandernehmen. Zweitens: **vier Tage.** Sie hat es selbst hineingeschrieben, damit niemand es fuer Zorn haelt. Fremdes Briefpapier, Annie mit Namen, unterschrieben als *Chair*, per Einschreiben, **damit es sich hinterher beweisen laesst.**

  **Und die Haelfte, die es persoenlich macht:** *"The thing she picked up and pointed at you was me."* Dazu die Zeile, die den ganzen Band traegt: **"I am the weapon in every sentence. I have never minded that. I mind it when the hand is not yours."**

  **Annie prueft ihn und findet keine Unschaerfe**, und das ist der Grund, aus dem sie ihn gehen laesst - nicht Mitleid und nicht Zustimmung. *"You are not angry. ... Anger makes people quick and rough and I cannot use anybody in that condition."* Und nach der Aufzaehlung der sechzehn Tage: **"You have not made one mistake. That is not what a man in a temper does. That is what a man does who has decided something and is waiting."**

  **Die Bitte, im Kanon-Register: die Hoeflichkeit steigt, sie sinkt nicht.** Er steht dafuer auf. **"May I have this one, Mistress?"** Mit Zeichen, weil sie nein sagen koennte. Und der Umfang wird ausgesprochen: *"I want everything she has, and I want it done by people who are entitled to take it from her, and I want her to be somebody nobody in that trade will read a letter from ever again."*

  **Der Preis ist der Deckel selbst.** *"I cannot tell you what a thing costs before I pay for it. ... If I stop to come home and name a figure, I will lose the week."* Er bittet darum, die Regel vom 11. Maerz auszusetzen - **die einzige Bitte in zwei Baenden, bei der sie haette nein sagen koennen.**

  **Was Annie dafuer bekommt, und er bringt es von selbst mit:** die **fuenf uebrigen Firmen**, vollstaendig, nicht als Kunden und nicht als Absprache. Sein Grund ist ungeschoent: eine Privatrache, die nichts einbringt, waere ihr Monat fuer seine Gefuehle. *"It is also true that I want it. Both of those are the case, and the second one is not the smaller of the two."*

  **Ihre zwei Bedingungen, und keine davon schuetzt Nam.**

  1. **Kein unwahres Wort**, nicht um es zu beschleunigen, nicht um es haerter zu machen, nicht am Ende. Und ihre Begruendung ist nicht Moral: *"That rule is the only thing you have ever had that is yours, and I am not going to watch you spend it on a haulier in Ulsan."* Seine Antwort ist die kaelteste des Kapitels: **"I will not need to."** - *"No. I know."*
  2. **"When it is finished you will come to this room and tell me whether you enjoyed it."** Und die Wahrheit darueber. *"I am aware of what I am asking for, and I am asking for it anyway."*

  **Und der Satz an der Tuer, der Sang-hoon als Gegenbild benutzt:** *"I want her finished. I do not want her hurt for four months so that somebody can watch. Park Sang-hoon takes eighteen months over a man because he enjoys the second year. You are not going to become that."* Zeitrahmen: **drei Wochen, vier wenn der Zweite vorsichtig ist.**

  **Und im selben Gespraech wird das andere Ende ausgesprochen, vollstaendig und ungefragt:** *"I am not going to have you told about him in three weeks as a thing that has already happened."*

  **Es sind zwei Leute, und sie bekommen sehr verschiedene Dinge. Der Unterschied ist ab jetzt Kanon.**

  **Der Versender hat entschieden.** Er hat die Seite aus einem gebundenen Band genommen, er hat die vierte Woche des schlimmsten Quartals dieser Frau genommen, und aus allen Menschen des Landes hat er **sie** genommen. **Er verliert alles, was sie verliert, und zwar danach**, damit er es vierzehn Tage lang auf sich zukommen sieht.

  **Der Bote hat getragen. Er wird erschreckt, und das ist alles.** Und Georgij sagt dazu, dass es keine Milde ist: Firma, Name, jeder Won bleiben. *"On an ordinary morning, when nothing at all is happening, he finds out that I know who he is and what he carried and which week he carried it in. After that he looks behind him at night for some years and nothing else ever happens to him."*

  **Und die Zusage aus demselben Gespraech, die die fuenf betrifft: alle fuenf, nicht vier und nicht die zwei leichten.** Ausbuchstabiert in Kapitel 14, wo jeder einzelne Weg hineingeschrieben ist.

  **Und der Grund, aus dem der Bote stehen bleibt, ist nicht Anstand:** *"He is how I get the first one. There is no road to that man that does not go through somebody who has touched the paper."*

  **Auf die Frage, ob es wirklich zwei sind, sagt er nein**, sofort, und es ist das Einzige an dem Nachmittag, das er von selbst zurueckholt. *"I am certain there is one who decided. I have never in my life seen a man of that sort carry his own paper to a post office."*

  **Und die Probe, an der er sie unterscheidet, ist der Kalender.** *"A man who is carrying a thing gets rid of it on the day he is told to get rid of it. ... Somebody sat down with a calendar. Nobody sits down with a calendar on somebody else's behalf."*

  **Jang im Pfoertnerhaus, und er ist, was `doc/03-cast.md` sagt: Interimschef der Sicherheit**, dreissig Jahre bei Haeusern dieser Art und nie bei einer Firma, die etwas herstellt. **In Fassung 1.1 stand er faelschlich an den Garagen und redete ueber Fahrer** - das ist Ku und Pyo, nicht er.

  **Georgij bestellt zwei Sorten**: jemanden, der herausfindet, wovor sechs kleine Firmen tatsaechlich Angst haben und wem jede von ihnen in einen Raum folgen wuerde; und jemanden, der vor einem Hof in Ulsan sitzt und aufschreibt, wer kommt. *"I do not think anybody is going to come. I would like to be wrong in a way I can read afterwards."*

  **Und Jang bietet die dritte Sorte von selbst an**, weil sie sonst im Kopf statt im Raum waere: drei Maenner, zwei davon aus seinem eigenen Fach. *"They are people who go and stand in front of somebody, and that is a different trade, and it works about half the time and the other half it makes everything worse for a year."* Georgij: **"Not yet."** - *"He did not say no. Jang heard him not say it."*

  **Und die einzige Frage, die ein Sicherheitsmann stellt:** *"Is any part of this going to arrive at that gate."* Antwort: die eigenen sechs nehmen es ihr ab, sie werden im Recht sein und es fuer ihre eigene Idee halten, **und eine Frau, die alles an die Leute verloren hat, an die sie zwanzig Jahre lang am Ersten geschrieben hat, faehrt nicht vier Stunden an ein Tor. Sie geht nach Hause.** - **"That is worse," he said.** - *"Yes."*

- **Band 2, Kapitel 13** *What it costs him* (v1.0) - **Tag 188, Do 9. April. Zwei Szenen: Jangs Lieferung am Mittwoch, dann Yeongjong.**

  **Jangs vier Blatt sind der Beweis, dass die Maschine laeuft**, und sie sind konkret: ein Sohn an einer Universitaet in Australien und sieben Monate Restlaufzeit auf einem Kredit gegen den Hof; ein Teilhaber, der seit dem Tod seiner Frau heraus will und nur bleibt, weil es niemanden zum Verkaufen gibt; zwei Brueder, die seit 2019 nicht miteinander reden und beide mit der Frau des Juengeren; einer, der seit Februar still Arbeit von der Spur nimmt; ein Mann von vierzig, der die Firma im Herbst uebernommen hat und seither in keiner Sitzung ein Wort gesagt hat.

  **Und der eigentliche Fund ist die Trennung zweier Fragen**, die Jang selbst benennt: *"You asked for what they are afraid of, which is the hard half, and then you asked who they would follow, which is the half people get wrong."* **Vier von fuenf wuerden demselben Mann folgen, und es ist der mit neun Lastwagen und ohne Schulden, und es ist nicht Nam Byung-hee.**

  **Dazu zwei Dinge, um die niemand gebeten hat.** Keine der sechs ist Annie oder irgendjemandem aus dem Haus je begegnet, zweimal geprueft. Und vor dem Hof in Ulsan sitzt seit Montag jemand, der einen Grund hat, auf der Strasse zu sein, und von jemandem in Busan bezahlt wird, der glaubt, es gehe um etwas anderes.

  **Yeongjong ist die erste Bitte auf eigene Rechnung in zwei Baenden**, und sie kostet ihn genau das, wofuer sie gebaut ist. **Georgij baut sie so, dass sie Woo nichts kostet** - fuenf Firmen, Bodenpreis, und ein Makler in Busan mit zwoelf Prozent, der Woo seit 2021 aergert. **Nicht aus Anstand, sondern damit die Schuld stehen bleibt.** Eine Bitte, die den anderen nichts kostet, tilgt nichts.

  **Woo sieht es binnen einer Minute und benennt es**, und die Stelle ist die haerteste, die er im Buch bekommt: *"You are not going to let me pay you back."* - **"No," said Georgij.** - *"Some men would call that a very cold way to treat somebody who likes them."* - *"Yes."* - *"Are you going to tell me it is not."* - **"No."**

  **Und die Begruendung ist die einzige weiche Stelle des Kapitels und sie ist wahr:** *"You are the only man in this country who has ever talked to me for three hours without wanting anything at the end of it. I am not going to spend that on a lane."*

  **Er sagt Woo, wofuer es ist, ungeordnet und ohne Federung, und er benutzt das Wort *finished*** - *"He did not use any of the softer ones and there are four or five available."* Die vierzig kommen unter, **der Neffe namentlich**, und *"I will know it has happened because I will ask."* Auf *"And her."*: **"Her nothing."**

  **Woo ist nicht erschuettert und sagt auch, warum nicht:** *"I am seventy-five. I have finished four men in my life and I remember the names of all four and two of them deserved it."*

  **Und statt eines Gefallens macht er ein Geschaeft: sieben Jahre, dasselbe Papier wie die Ankerladung.** *"You came here to ask me for something you thought I owed you. What you are getting instead is a customer, and I would like that on the record, because I know exactly what you are doing and I am going to let you do it."* Danach: **"Then you still have the three hours."** - *"I still have the three hours."*

  **Der Januar-Fund, ungefragt am Wagen, wie im Oktober.** Bei einem Hafenbehoerden-Essen in der ersten Januarwoche hat ein Mann Woo gefragt, ob er die Ulsan-Zubringerspur je benutzt habe und was er von der Frau halte, die den Verband fuehrt - *"the way you ask about a house you are thinking of buying."* Woo hat gesagt, sie sei **ehrlich** und die Spur zu klein, **und der Mann war an dem Wort *ehrlich* sehr interessiert.** Keinen Namen, weil der Mann nichts wollte. Aber die fuenf anderen am Tisch.

  **Und daraus der Schluss auf der Bruecke, der den Band vergroessert:** im Januar war auf der Spur noch nichts. Niemand war verletzt, niemand hatte sich beschwert. **Also suchte er nicht jemanden, dem etwas angetan worden war, sondern die Person, der es gleich angetan werden wuerde** - und dafuer musste er in der ersten Januarwoche wissen, was im Dezember in einem Zimmer in Seoul unterschrieben worden war, **und zwar binnen vierzehn Tagen nach der Unterschrift.**

  Letzte Zeile: **"That is a very short list as well."**

- **Band 2, Kapitel 14** *Ask her* (v1.2) - **Tag 193, Di 14. April, dazu die Woche danach in Raffung.**

  **Das Verfahren ist Mrs Sunwoo, auf einen Mann mit neun Lastwagen angewendet:** ein wahrer Satz, dann aufhoeren. Sieben Jahre Ankerpapier, **fuenf Firmen und nicht sechs**, einer nach dem anderen, und der Erste setzt den Satz fuer die uebrigen vier. Aus dem Satz gestrichen hat er auf dem Sonntag das Wort *opportunity*.

  **Auf die Frage nach dem Warum sagt er, was er tut, und nicht, was geschehen wird:** *"Because I am not going to bring him the sixth one. ... I am telling you what I am going to do and not what is going to happen to her, because I do not know the second thing and I would be guessing."*

  **Und dann der ganze Zug des Kapitels, in zwei Woertern: "Ask her."** Er sagt kein Wort gegen sie und weist ausdruecklich darauf hin. **Ihre Ehrlichkeit ist die Waffe, und er muss sie nicht einmal beruehren:** *"She will tell you the truth, because she does not lie, and you have known that about her for twenty years and it is the only reason this is going to work."*

  **Kwon stellt am Wagen die Frage, die die Sache aufraeumt:** *"You said ask her. You did not say what to ask her about."* - *"No."* - **"Because if you had, it would be your question."** - *"Yes."*

  **Der Anruf bei Woo ist die Probe und Georgij sitzt dabei.** Woo bestaetigt die Jahre zweimal und ueber Georgij gar nichts: *"I am not going to tell you any more than that."* Und danach, nach etwas Unhoerbarem: **"I would not believe me either."**

  **Was Georgij dabei ueber sich sagt, ist die vollstaendige Wahrheit und hilft nicht:** kein Titel, keine Firma, kein Gehalt, kein Konto. *"There is no piece of paper anywhere in this country with my name on it and a position underneath it."* - **"That is not an answer."** - *"It is the whole of the answer. There is nothing about me to check."*

  **Die Frage, die niemand sonst gestellt hat, und sie steht am Ende:** *"I said you were an unpleasant man and you said today. Was that true."* - **"No. I have been this for about three weeks and I do not know yet whether it goes away."**

  **Und Mr Ku sagt zum ersten Mal seit Oktober etwas**, und es ist kein Vorwurf und keine Frage: der Bruder seiner Frau fuhr zwoelf Jahre fuer eine Firma mit einem Hof wie diesem, *"then it was a different firm and the yard was the same and he was not there any more."* - **"Is that a question."** - *"No."*

  **Und das Neue an dieser Woche:** er berichtet nichts. Der Deckel ist seit elf Tagen ab. *"This is the first week since October in which he has done a week's work and said nothing at all about it to anybody. It turns out to be quieter than he had expected, and not in the way he had expected."*

  **Die Maschine laeuft am Ende ohne ihn.** Woos Anwalt schreibt an alle fuenf am selben Tag dieselben drei Fragen, und die dritte ist die, die jeder Anwalt stellt und ueber die niemand nachdenkt: **wer ist berechtigt, fuer Sie zu zeichnen, und hat das in den letzten sechs Monaten jemand getan.** Drei lesen die Satzung, zwei rufen Nam an, **sie sagt beide Male die Wahrheit** - Georgij weiss nicht, was sie gesagt hat, und hat nicht versucht, es herauszufinden.

  **Der Beobachter meldet nichts, was der Befund ist**, und dazu eine Zeile, um die niemand gebeten hat: am Samstagabend brannte das Licht ueber der Waage bis halb elf, und irgendwann kam sie heraus und sah eine Weile vier Lastwagen an.

- **Band 2, Kapitel 15** *One word, and it was true* (v1.0) - **Tag 202, Do 23. April. Zwei Straenge an einem Nachmittag: die Suche in Seoul, dann der Anruf um zwanzig nach vier.**

  **Er ist nicht im Raum und es gibt keine Fassung, in der er es sein koennte.** Er hat es am Mittwochabend trotzdem vier Minuten lang geprueft.

  **Der Vormittag ist das zweite Werkzeug bei der Arbeit.** Das Haus laesst in Mapo versenden, ein Buero dieser Art fuehrt eine Adressliste und behaelt sie, weil der Kunde naechste Saison wiederkommt. **Sechshundertvierzig Namen**, davon hundertneun Mantelgesellschaften. *"It took him a little over two hours and he did not enjoy it as much as he had expected to, which he noted and did not examine."*

  **Und dann der Fund, der nicht in der Liste steht, sondern in ihrer Kreuzung:** sechshundert Namen sind kein Verdaechtigenkreis, sondern ein Telefonbuch. **Das richtige Ende ist, wer einen Katalog bekam UND im Januar bei dem Hafenbehoerden-Essen war.** Woos fuenf Namen liegen seit dem 9. April im Notizbuch. **Drei der fuenf stehen auf der Versandliste.** *"Three is not an answer. Three is a shape."*

  **Die Versammlung kommt vollstaendig als Bericht von Mr Kwon**, und der Punkt des Kapitels ist eine einzige Silbe. Auf die Frage, ob sie auf Verbandsbriefpapier geschrieben habe: **"She said yes." - "Straight away. Not a second."** Auf die Frage, ob es Verbandsangelegenheiten betraf: **"She said no."**

  **Sie hatte einen offenen Ausweg und hat ihn angesehen und nicht genommen.** *"She could have said it was association business and none of us would have been able to prove otherwise for a month, and by then it would have been over."* - **"She does not lie."** - *"It cost her everything in about a second and a half and she did not even look surprised."*

  **Das Ergebnis: vier dafuer, eine dagegen, eine Enthaltung.** Kwon wird Vorsitzender, in vier Minuten, gegen seinen Willen und weil sonst niemand da ist. **Niemand beantragt den Ausschluss ihrer Firma**, und Kwon haette dagegen gestimmt. Sie behaelt vier Lastwagen und eine Spur ohne Arbeit, waehrend die anderen fuenf sieben Jahre bekommen, *"and everybody in that room understood exactly what that means, and not one of us said it out loud."*

  **Cho, vierzig, seit Oktober ohne ein Wort in einer Sitzung, sagt heute eines** - dass sie zwanzig Jahre lang an sechs Leute geschrieben hat und niemand je zurueckgeschrieben hat, **und dass er nicht finde, dass jemand alles verlieren solle fuer das Erste, worum er je fuer sich selbst gebeten hat.** Und dann enthaelt er sich.

  **Georgijs Urteil darueber steht nur in der Erzaehlstimme und ist das Kaelteste im Kapitel:** wer ein wahres Wort sagt und danach nicht handelt, hat sich besser gefuehlt und nichts geaendert. *"It is the commonest thing in the world. He has used it in nine rooms since October and has never once had to work for it."*

  **Kwon nimmt die sieben Jahre und nicht den Dank**, und er sagt es als Bedingung: *"I will take the seven years and I will not take the thanks, and I would like that to be the arrangement between us from now on."* Vorher, haerter als alles andere in dem Gespraech: *"Do not stand at the other end of a telephone and be clever at me about it."* Und Georgijs **"I am sorry"**, ungeplant, *"before he had decided whether it was for Mr Kwon or for himself, which is the reason he almost never says it."*

  **Und der Satz, der das Mitleid des ganzen Buches traegt:** Sie ist geblieben und hat die Stuehle gestapelt. *"It is what she has done after every meeting for twenty years and I do not think it occurred to her to do anything else."* Dann hat sie jedem gute Nacht gesagt, mit Namen, Kwon zuletzt, **und war dabei nicht spitz, weil sie dazu nicht in der Lage ist.**

  **Georgijs Reaktion darauf ist die Haltung des gesamten Bandes:** *"He did not predict that, and he cannot make it be anything other than what it is, and it does not alter one single thing about the rest of the month."*

  **Und das, was er nicht aufschreibt.** Ins Notizbuch kommen fuenf Woerter. Was Cho gesagt hat, kommt nicht hinein: *"A thing that goes in the notebook stops having to be carried. That is the entire point of the notebook and he has known it since October, and he left it out anyway."*

  **Annie hat es ohne ihn mitverfolgt und sagt es auch:** *"I have had the Yeouido people watching the filings since Tuesday and I did not tell you, because you would have wanted to know why and the answer is that I wanted to see it happen."* Dann: *"Sit down and do not report to me. You do not have to and I have not asked."*

- **Band 2, Kapitel 16** *A hand* (v1.0) - **Tag 204, Sa 25. April. Ein Tag am Schreibtisch, dann das kleine Zimmer.**

  **Mrs Sunwoos April traegt: seit dem 20. April nimmt das Haus keine Einlieferungen mehr an.** Ohne Ankuendigung - *"It tells the fourth person who telephones that the spring sale is under review, and by the eighth person it has stopped being a rumour."* Zwoelf Mittagessen seit dem 24. Maerz, und Georgij weiss die Zahl, weil ihr Kalender offen liegt, **und hat beim Nachsehen zweimal etwas empfunden, das er nicht benennt.**

  **Und er widersteht der ersten falschen Spur des Bandes:** zwei ihrer Tischgaeste stehen auf der Versandliste, einer davon auch auf der Januar-Liste. Er tut nichts damit. *"A coincidence in a city of that size is not a fact, and a man who forgets that ends up with the wrong person."*

  **Zwei der drei Namen fallen ohne Aufwand weg**, und die Gruende sind Charakter und nicht Papier: der eine kauft seit sechs Jahren offen kleine Betriebe auf und haette sie an ein Telefon gebracht; der andere sitzt selbst im Ausschuss, **und wer bei einer Sache ist, weil sie ihm gehoert, stellt dort keine Frage, an die sich niemand erinnern soll.**

  **Der dritte ist Mr Ok**, sechsundfuenfzig, Seeversicherungsmakler in zweiter Generation, elf Angestellte, kauft seit 2003 Keramik in dem Haus. **Er hat mit Kuestenverkehr nicht das Geringste zu tun** und war bei dem Essen, weil sein Vater immer hinging. *"That is not evidence of anything. A man is allowed to ask a question at a lunch."*

  **Und dann macht Georgij zum ersten Mal in Band 2 das, was `doc/02-leads.md` seit jeher unter *Digitale Sicherheit* fuehrt**, und der Text beschreibt es ausdruecklich nicht: *"He is not going to write down how, and it does not matter."* Ein Buero mit elf Leuten seit 1978 in denselben zwei Etagen, ein Geraet im Flur seit 2019, **und ein Protokoll, in das nie jemand gesehen hat.** Fuenfzig Minuten, davon das meiste Lesen.

  **Der Fund: 12. Maerz, sechzehn Uhr vierzig, eine Seite auf dem Glas, ZWEIMAL kopiert.** *"Two copies is a fact and one copy is an errand."* Das Konto gehoert einer Frau, die dort seit 2004 die Ablage macht. **Sie hat keine Sekunde darueber nachgedacht, weil man eine Seite kopiert, wenn man gebeten wird, eine Seite zu kopieren.**

  **Und was das Protokoll nicht kann, gehoert zum Fund:** es sagt nicht, was danach mit den Kopien geschah. *"Somebody put one of them in an envelope. That is in no log anywhere and it never will be, and it is the reason a page arrives in Ulsan and a man in Jung-gu has no idea that he has done anything at all."*

  **Der eigentliche Befund ist eine Abwesenheit.** Keine Nachricht, keine Notiz, kein Brief, kein Kalendereintrag, nichts am elften und nichts am zehnten. **Und damit greift Georgijs eigene Probe vom 3. April**, die Annie ihn zweimal hatte sagen lassen: *"Nobody sits down with a calendar on somebody else's behalf."* **In diesem Buero gibt es keinen Kalender. Also ist Mr Ok eine Hand.**

  **Und das kostet ihn die Rache, die er seit dem 18. Maerz mit sich traegt.** *"He had wanted a man to take apart. ... What he has is a broker of fifty-six who buys ceramics and does what he is asked by somebody at a lunch."* Er schreibt trotzdem **Frightened only** auf und aendert es nicht: *"That is his own rule and he made it in front of her before he knew who it was going to protect, which is the only condition under which a rule is worth anything at all."*

  **Die zweite Kopie ist der Schluss und sie ist das Erste seit acht Wochen, das ihm wirklich Angst macht.** Sie ist irgendwo, seit sechs Wochen, und musste noch nicht benutzt werden. **Und sie sagt etwas ueber den Versender, das Nams Lage nachtraeglich verschlimmert:** *"a man who makes two copies of a thing is a man who does not expect the first one to be enough. ... he had already decided in March that she might not do it, and that it would not particularly matter if she did not."*

  **Annie sieht sein Gesicht, bevor er etwas sagt:** *"Say the bad one first."* Und danach: *"Tell me about the second copy from the beginning, and do not leave out the part where you are frightened, because I would rather have it from you than watch you carry it around the house for a fortnight."*

  **Und das Vorziehen der Abrechnung**, die eigentlich fuer das Ende verabredet war: *"If I take him apart because I have been carrying something since March, then I am doing it for me, and I told you on the third of April that I would tell you the truth about that afterwards. This is the afterwards arriving early."*

- **Band 2, Kapitel 17** *Four minutes of somebody's time* (v1.0) - **Tag 206, Mo 27. April. Eine Szene, an einer niedrigen Mauer vor einem Buerohaus in Jung-gu.**

  **Das Erschrecken besteht ausschliesslich aus Auskunft.** Kein Wort ist eine Drohung. Georgij sagt ihm das Datum, die Uhrzeit, das Geraet, die zwei Kopien, den Namen der Frau aus der Ablage, und was am 23. April in einem Raum ueber einer Bank in Ulsan geschehen ist. **Mehr braucht es nicht.**

  **Und der Satz, der ihn wirklich anhaelt, ist der ueber Mrs Uhm:** *"She is not going to be troubled by anybody, ever, and I want that said before the rest of it."* Georgij hat gewusst, dass dieser Satz ihn stoppen wuerde, hat ihn deshalb dorthin gesetzt **und hat ihn ausserdem so gemeint.**

  **Die Absolution ist kaelter als jede Drohung.** Nichts geschieht seiner Firma, seiner Familie, seinen Kunden, seiner Bank. *"That is not a negotiating position and there is nothing you can do that would change it."* Der Grund: **"Because you did not choose anything."** Und dann der Satz, der haerter landet als alles davor: *"I am telling you that you are a hand."*

  **Was Ok liefert, ist der bisher einzige Augenzeuge des Versenders.** Januar-Essen, ein Mann kommt an sein Ende des Tisches, **wird ohne hoerbaren Namen vorgestellt**, fragt nach der Ulsan-Kueste und dann nach ihr namentlich, **und interessiert sich auffallend fuer das Wort *ehrlich*** - was Woo unabhaengig davon genauso berichtet hat.

  **Erste Maerzwoche: ein Anruf.** Eine Seite hinten im Katalog, ein Freund in Ulsan, die Adresse dazu. **Und ausdruecklich zwei Kopien: eine zum Schicken und eine fuer die Akte.** Die Akte-Kopie liegt seit sechs Wochen ungeoeffnet auf der zweiten Etage - *"Then that is not the one I am afraid of."* **Damit ist die zweite Kopie aufgeloest und die Angst aus Kapitel 16 abgeraeumt**, ohne dass Georgij etwas dafuer tun musste.

  **Die Beschreibung: sechzig oder etwas weniger, nicht gross, pleasant, quiet, *the sort of man who has been in rooms*. Und er hat bei diesem Essen nichts gegessen, kein einziges Ding.**

  **Und die Signatur, auf die das ganze Kapitel zulaeuft:** *"At the end of the lunch he stood up and shook my hand and said that he was glad we had finally met."* Sie waren einander nie begegnet. **"He did not confuse you with anybody."**

  **Das ist die Umkehrung von Mrs Sunwoos *We haven't met*.** Sie sagt es, um zu pruefen, ob der andere weiss, was sie ist. Er sagt es, damit der andere glaubt, er haette es wissen muessen.

  **Und die letzten dreissig Sekunden sind der Preis des Kapitels.** Georgij sagt Ok, er solle beim naechsten Anruf ja sagen, es genau so tun, wie es verlangt wird, und niemanden warnen. Auf dem Weg zur Bruecke merkt er, was das ist: **im Maerz hat jemand diesen Mann um vier Minuten fremder Zeit gebeten, und heute Abend hat ein Mann an seiner Mauer gestanden und ihn zum selben gemacht.** *"There is a word for that and he did not go looking for it."*

  **Und Ok will am Schluss den Namen**, den Georgij ihm vorher als nutzlos angekuendigt hatte. Er bekommt ihn, und er bedeutet ihm nichts, **wie im Maerz an einem Tor in Ulsan - nur dass es diesmal nicht mehr das tut, was es damals getan hat.**

  **Der Schluss zeigt auf Kapitel 18:** eine Beschreibung ist keine Beschreibung, vierhundert Maenner in dieser Stadt sind sechzig und leise und nicht gross. **Aber ein Satz gehoert jemandem**, und es gibt genau eine Person, die in genug Raeumen war, um einen Satz zu hoeren und ein Gesicht darauf zu legen. *"She has been declining to give him that face since December, and she has had a reason every single time, and every one of those reasons was better in December than it is tonight."*

- **Band 2, Kapitel 18** *The face on it* (v1.1) - **Tag 206, Mo 27. April, abends. Eine Szene, das kleine Zimmer, am selben Tag wie Kapitel 17.**

  **Er liest ihr alle neun Zeilen vor und sagt vorher, warum:** *"Eight of them are worth nothing. I am going to read you all nine anyway, because if I read you the one you will hear it differently."*

  **Und der Beweis ist eine Abwesenheit, genau wie in Kapitel 16.** Er kennt die sechs oder sieben kleinen Dinge, die an ihr geschehen, wenn sie ueberrascht ist, wenn sie sich langweilt, wenn sie es schon von jemand anderem hatte. **Keines davon geschieht.** *"She went entirely still in the way that a person does not go still by accident."*

  **"You know him." - "Yes."** Zum ersten Mal beantwortet sie diese Frage mit einem Wort. **Und den Namen gibt sie trotzdem nicht.**

  **Georgij argumentiert und kuendigt an, dass er verlieren wird**, und seine Argumente sind gut: die Gruende vom Dezember und vom Maerz waren beide, die Arbeit zu schuetzen, **und es gibt keine Arbeit mehr zu schuetzen.** *"He has spent me. ... Whatever I was on the second of March, I am not it now."* Dazu die zweite Haelfte, die er selbst als kein Argument bezeichnet: er koennte einer Frau in Ulsan alles geben ausser einem Wort, **und das eine Wort ist das einzige, das sie wollen wuerde.**

  **Annies Urteil darueber ist eines der haertesten Dinge, die sie ihm sagt:** *"That is the worst argument you have ever made in this room, and it is the first one that has ever been difficult to listen to, and I want you to understand that those are two different sentences."*

  **Und dann antwortet sie zum ersten Mal vollstaendig, statt sich hinter Dezember zu stellen.** Choi handelt nie: keine wiederholbare Anweisung, keine Bitte, die man ablehnen koennte, seit fuenfundzwanzig Jahren. *"That is not a man with a method. That is a man who has found a way to live."*

  **Der echte Grund fuer das Zurueckhalten, und er ist neu und er ist besser als der alte:** der Name sagt nichts ueber Ort oder Besitz - **er veraendert Georgij.** *"The day you have his name, everything you do about him is a decision. ... And he reads guest lists for a living."* Also: **"The name is the thing that makes you legible."** Sieben Wochen unsichtbar, und zwar vollstaendig zufaellig.

  **Und ihr Schlusssatz dazu laesst nichts uebrig:** *"I am not going to spend it on a Thursday afternoon in a yard in Ulsan so that a woman who tried to blackmail me can feel answered."* Danach: *"It is better than yours and we both know it, and I am sorry, and being sorry does not move it."* **Er reagiert nicht auf das Wort**, weil sie es sonst bereuen wuerde, und weil sie es etwa zweimal im Jahr sagt.

  **Was er statt dessen bekommt, ist mehr wert als ein Name, und es ist ein Verhaltensmerkmal: er isst nicht vor Leuten, an denen er arbeitet.** Nicht aus Disziplin, sondern weil er beides nicht gleichzeitig kann, **und er hat nie bemerkt, dass man es sieht.**

  **Und die Folge daraus ist der eigentliche Fund:** jeder Mann in dieser Stadt, der ihn je hat essen sehen, ist ein Mann, an dem er **nicht** gearbeitet hat. Annie faellt fuenf davon ein. **Georgij hat zwei davon getroffen.** Sie sagt nicht welche - *"You will get there in about four days and it will be yours when you do."*

  **Sie benennt selbst, was sie tut:** *"I have been sitting on the whole of it since December and I have just given you the smallest piece I could get away with, and both of us are aware of it."* Und er spricht es aus: sie haelt es weiter, und am Tag, an dem sie aufhoert, wird es daran liegen, dass es unsicher geworden ist, **und nicht daran, dass er gefragt hat.**

  **Ihre Frage danach ist die erste in zwei Baenden, ueber die er nachdenken muss, bevor er antwortet.** *"Does that make you angry."* - **"No. It makes me tired, and I have not been tired since the second of March, and I would rather be angry. Anger is quicker."**

  **Und die Hand auf der Halsseite ueber dem Halsband**, dreimal seit Oktober und noch nie in diesem Raum. Dazu ihr letzter Zug, der ehrlich ist und trotzdem ein Zug: *"You are going to manage it because you have not got the name and cannot give it to her."* - *"That is not why you kept it."* - **"No. But it is going to be true on Thursday anyway."**

  **Und auf der Treppe faengt er sofort an**, und macht es richtig: die Liste wird nicht heute Abend geschrieben, sondern am Mittwoch, auf Papier, mit Daten, in der Reihenfolge der Mahlzeiten, *"because that is how a list stops being a feeling."* **Neun Mahlzeiten seit Oktober**, und eine davon ist der 18. November, und er weiss schon, was dort stehen wird, **und schreibt es trotzdem der Reihe nach hin.**

- **Band 2, Kapitel 19** *The third time* (v1.0) - **Tag 209, Do 30. April. Der Hof in Ulsan zum dritten Mal, dazu der Mittwoch davor.**

  **Die Liste der neun Mahlzeiten wird geschrieben und sofort durchgestrichen.** Annie hatte **met** gesagt, er hatte **eaten with** gehoert, *"and he had heard it because a list of nine meals is a thing a man can do in an hour at his own desk."* Getroffen hat er seit Oktober ueber vierhundert. **Der Mittwoch produziert nichts ausser einer genauen Vorstellung davon, wie viel es ist.**

  **Und den einen Mann, den er fragen koennte und nicht fragt:** *"a man who telephones Park Sang-hoon to ask which people have watched a particular person eat has just told Park Sang-hoon a great deal, and Park Sang-hoon does not put things down."*

  **Das Haus am Fluss schliesst am 29. April.** Kein Aushang, nur eine Telefonnummer und eine Frau, die seit dem zwanzigsten denselben Satz sagt. Mrs Sunwoo hat noch drei Mittagessen im Kalender fuer Mai.

  **Der dritte Zug, und die Struktur ist gesetzt: dreimal derselbe Hof, dreimal ein anderer Mann.** Beim ersten Mal kam er und fragte. Beim zweiten sagte er, was er ist. Beim dritten sagt er, was er getan hat. Ihre Begruessung: *"Third time. ... You have not brought anything."* - **"No."**

  **Die drei Unglueck, und das dritte ist keines:** die Container waren nie auf sie gerichtet; sie wurde ausgewaehlt, **und zwar weil jemand gesagt hat, sie sei ehrlich**; und dann *"you were unlucky in the way you thought."* Dazu ausdruecklich: *"That part was yours. ... I am not going to pretend it is bad luck as well."*

  **Wofuer er sich entschuldigt, ist nicht die Vernichtung, sondern der 20. Maerz**, und die Kapitel-10-Regel fuer dieses Wort haelt: es ist fuer sie und nicht fuer ihn. *"On the eighteenth of March, in the hour your letter came out of the envelope, I decided what I was going to do to you. I did not admit that to myself until the twentieth."* Und der Posten aus Kapitel 8, den er auf keine Seite geschrieben hat: **"I wrote it in the middle of the page as a thing I had not decided about. I had decided about it."**

  **Ihre Antwort darauf ist die praezise:** *"You could have got out of that. Nobody in the world would have known. I would not have known. You have just handed me the one piece of it that you did not have to hand anybody."* Seine Begruendung ist Regel 1 auf sich selbst angewandt: **"leaving that out is the only untrue thing available in this room."**

  **Die zwei Dinge, die kein Trost sind.** Der Neffe ist seit dem 20. April bei Mr Kwon, auf der Neun-Wagen-Rota, zum ersten Mal auf richtigem Lohn - *"That was arranged and it was arranged by me, and I checked on Monday that it had actually happened."* Dazu: *"He is twenty-three, and he is not the one who wrote the letter."*

  Und: **der Mann, der sie ausgewaehlt hat, bekommt dasselbe.** Ohne Namen, mit Frist - *"before the end of the year"* - und mit der einen Praezision, die Georgij ueberall macht: *"he will lose it slowly enough to watch it coming. You did not. That is the only respect in which you have been treated better than he is going to be."*

  **Ihre eine Frage ist die schlimmste, die sie stellen konnte, und sie stellt sie in demselben Ton, in dem sie alles liest:** *"Was it you, or was it her."* Antwort ohne jede Federung: **"It was me. ... She permitted it. She did not order it, she did not suggest it, and there is no version of this in which I was doing what I was told."** - *"So it was personal."* - **"It was entirely personal."**

  **Und dann kommt sie selbst an:** *"Lot fourteen," she said.* Danach der Satz, der Nams ganze Lage traegt: **"I have thought about that page every day since the fourteenth of March, and it never once occurred to me that there was a person on it."** - *"No. That is what a page is for."*

  **Und was Choi damit getan hat, in einem Satz:** *"He gave you a page with a man on it and did not tell you the man was on it, and then he went home and had his dinner."*

  **Sie bereut nichts und sagt es**, und er glaubt ihr genau deshalb: *"I am not sorry that I wrote it. I have tried for a week to be and I am not. ... I would write it again tomorrow if I did not know what I know now."* - **"I would not have believed you if you had."**

  **Am Tor der Teil, der kein Mitleid ist, und er ist keine Drohung, sondern eine Beschreibung:** sie darf alles erzaehlen, jedem, ihr Leben lang. *"By the end of May there will not be one firm on this coast that is not better off than it was in December, and every one of them will know exactly who it is better off because of. A man whose yard has just been made worth something does not repeat a thing like that. He does not decide not to. It simply does not occur to him."*

  **Und der eine Satz mit Zaehnen, nicht mehr als einer:** *"Then I will come here a fourth time, and there will be nothing in my hands then either."*

  **Ihr letzter Satz ist der beste, den irgendeine Figur in Band 2 bekommt, und er bleibt unbeantwortet:** *"That is the only thing you have said today that you enjoyed."* Dazu: *"He thought about that on the platform for twenty minutes and on the train for four hours, and he has not got an answer to it that he is willing to write down."*

  **Damit steht Annies zweite Bedingung vom 3. April offen und geladen** - er soll zurueckkommen und sagen, ob es ihm gefallen hat, und die Wahrheit darueber sagen. **Eine Fremde hat die Frage vier Stunden frueher gestellt.**

- **Band 2, Kapitel 20** *Cheaper than deciding* (v1.0) - **Tag 209, Do 30. April, zwanzig nach elf. Eine Szene, das kleine Zimmer, und die Tuer ist zu.**

  **Er haelt den Termin, den er am 3. April genannt und am 1. April auf ihr Verlangen wiederholt hat.** Der Bericht ueber den Monat dauert vier Minuten. **Annie sagt zu keinem Teil davon irgendetwas**, weil sie niemanden beglueckwuenscht und es ihr nie eingefallen ist, dass jemand das wollen koennte.

  **Dann die zweite Bedingung, und sie stellt sie so, dass er nicht daran vorbeikommt:** *"I am not going to ask it gently and I am not going to give you a way of answering it that lets you past."* - **"Did you enjoy it."**

  **Die Antwort ist die genaueste, die er geben kann, und sie ist schlimmer als ja oder nein.** *"Yes. Once. For about a second and a half, at a gate, at four o'clock this afternoon."* Naemlich der eine Satz mit Zaehnen. Und der ganze Rest des Monats: **"No. Not one minute of it."**

  **Und woher er es weiss, ist das Bitterste daran: Nam hat es ihm gesagt.** Vier Stunden vor Annie, in demselben Ton, in dem sie alles liest. - **"Then she is better at this than I am."** - *"She is not. She had the advantage of not caring what the answer was."*

  **Die Bitte, auf die das Kapitel zulaeuft: er will den Deckel zurueck.** Preis vorher, jedes Mal, ab morgen frueh.

  **Und Annie sagt nein, und ihr Grund ist der Kern des ganzen Bandes.** *"You are not asking me for a ceiling. You are asking me to be the thing that stops you, and a man who has somebody to stop him has to decide once, on a Thursday in April, and never again."* Dazu die Diagnose, die er selbst anwendet: **"You put a rule in front of a man so that he does not have to make the decision again in June. It works every single time, and it works because a rule is cheaper than deciding."**

  **Sie weigert sich, sein Gewissen zu sein, und begruendet es nicht mit Unlust, sondern mit Eignung:** *"Because I would be extremely good at it and you would never have to do it again. In four years you would be somebody who does whatever is in front of him and comes home and has it audited."* Und: *"You have had two months of it now and I am not going to take it off you because the second month was unpleasant."*

  **Sein Satz, der kein Argument ist, ist die Bilanz der Figur nach diesem Monat:** *"I have been afraid of four things and I could name all four. As of this afternoon there are five, and the fifth one is that I am going to be all right about it."* - **"That is the correct one to be afraid of, and I would have been disappointed in you if it had taken you until June."**

  **Danach fragt Annie zum ersten Mal seit dem 20. Maerz nach Nam Byung-hee**, und daraus wird die Zusage, die spaeter eingeloest werden muss: **jemand stellt sie ein, in etwa vier Monaten, nicht er, und sie erfaehrt nie, woher es kommt.**

  **Die Gruende, in der Reihenfolge, in der sie tatsaechlich stehen.** Erstens: *"Somebody who has been armed once can be armed again. A woman with nothing is a woman who says yes to the next man who arrives with a page."* Zweitens ihre Ehrlichkeit, drittens ihre Kompetenz - **und die Kompetenz setzt er selbst an die letzte Stelle, wenn er ehrlich ueber die Reihenfolge ist.**

  **Der vierte Grund, den Annie ihm abfragt und den er lieber nicht haette:** *"He will hear that his instrument was taken apart in six weeks and then picked up off the floor by the same hand, and there is nothing at all he can do with that except sit with it."*

  **Und warum erst in vier Monaten:** *"Because in May it is a payment. ... I would have bought my way out of this afternoon for the price of a job. She said something to me at a gate today that I have not got an answer to. I am not going to answer it with a favour."*

  **Der Schluss gehoert dem Haushalt, der seit Kapitel 13 fast verschwunden war.** Vier Menschen haben gemerkt, dass er seit dem 18. Maerz nicht richtig schlaeft, **und einer davon hat etwas gesagt** - Mr Ku auf der Autobahn am 14. April - und hat sich danach vierzehn Tage lang Sorgen gemacht, ob er gedurft hat. *"Tell him it was the most useful thing anybody said to me all month."* - **"Tell him yourself. He is on the early rota."**

  Und die Hand im Haar, wie in Kapitel 5 und Kapitel 9, **nur dass er diesmal gewusst hat, dass die Schultern oben waren.**

- **Band 2, Kapitel 21** *Tidily* (v1.2) - **Tag 213, Mo 4. Mai. Eine Szene, ein Raum mit drei Kisten darin, in einem Gebaeude, das aufgeloest wird.**

  **Am 23.08. gegen meine eigene erste Anlage korrigiert.** Ich hatte Hwangs Haltung als unangreifbar gebaut. **Sie ist es nicht**, und der Autor hat gesagt warum: vier bezahlte, arrangierte und abgesegnete Auftraege wurden nicht ausgefuehrt, er hat es gewusst, und er hat weder erfuellt noch erstattet noch es den vieren gesagt.

  **Georgij nimmt die Regel in einer Minute auseinander, und der Kern ist eine Unterscheidung:** die Regel, fuer die Hwang geholt wurde, ist eine **ueber die Zukunft** - dieses Haus verkauft keine Loeschungen mehr. *"It has nothing whatever to say about four people who paid for something last year and did not get it."*

  **Die drei sauberen Wege werden aufgezaehlt und alle drei waren offen:** erfuellen, erstatten mit Begleitschreiben, oder es jedem der vier sagen. *"You took none of them. You kept the money and you kept the record. That is the position the men before you were in. The only difference between you and them on the thirty-first of December is that your filing is better."*

  **Hwangs einziger Einwand ist ein Gefuehl und Georgij benennt es:** *"That is not fair."* - **"No. It is accurate. Those are different words and I chose the one I meant."**

  **Und die zwei Saetze, die die Szene tragen:** *"You did not decline to delete four entries. You declined to give four people back a thing they had already bought, and you called that a principle."* Und: **"You have not been running a clean house for five months. You have been running the same house tidily."**

  **Die Anomalie der vierten Zeile, und Hwang gibt sie von sich aus her.** Sie
  betrifft **nicht** die Gebuehr - die hat der Mann bezahlt, im selben Buch, in
  derselben Handschrift wie die drei anderen. **Sie betrifft die Abrechnung des
  Loses**, und dort fehlt alles: keine Rechnung, keine Verrechnung, keine Zeile
  an Mrs Jeons Schreibtisch. **Damit bestaetigt Hwang Kapitel 3, 16 und 17
  unabhaengig.**

  **Und die beiden Tatsachen passen nicht zusammen, und das ist der Fund.** Wer
  nicht in Rechnung gestellt wird, ist jemand, dem das Haus etwas schuldet, vor
  dem es Angst hat, oder dem es gehoert - **und so einer muss keine Gebuehr
  zahlen. Er sagt einfach, es soll heraus.** *"And he paid anyway. On the same
  terms as everybody else, in cash, through the same man."*

  **Hwangs einzige Erklaerung in fuenf Monaten, und sie gefaellt ihm nicht:**
  *"That he did not want anybody in this building to know that he could have
  had it for nothing."*

  **Die Wiedererkennung braucht zwei Sekunden**, weil dieser Mann die vier Eintraege genauer gelesen hat als irgendwer sonst: **"Lot fourteen."** - *"The fourth of October. Struck on the nineteenth of February. And retained. And I retained it."*

  **Und auf die direkte Frage die direkte Antwort:** *"Is the house shut because of you."* - **"Yes. Not by me."** Eine Kundin, ein wahrer Satz, ein Katalog, den sie schon hatte. *"And you knew what she would do."* - **"I knew exactly what she would do. That is why I said the sentence."**

  **Was Georgij ihm sagt und was kein Trost ist:** er ist fertig. Nicht das Haus, er. Fuenf Monate im Lebenslauf und ein Gebaeude, das unter ihm gestorben ist, **und niemand wird das je wohlwollend lesen und niemand wird nachfragen.**

  **Und der Satz, an dem Georgij seit dem 23. April festhaengt:** *"Nobody in the whole of this took a single won. Not you. Not me. Not her. Everybody involved did what they thought was correct and a woman of fifty-eight is going to be selling two trucks on Thursday."*

  **Der Vorgaenger.** Hwang schreibt Name, Position, die Daten der vier und die heutige Anschrift auf die Rueckseite seiner Liste, reisst den Streifen ab **und haelt ihn hin, statt ihn hinzulegen.** Und er benennt selbst, was er gerade getan hat: *"I have just done in twenty seconds the thing I refused to do for four people in five months. I did it because a man came in here and made me feel it."*

  **Der Mann ist im November gegangen, vor Hwang, und nicht wegen alledem** - er wollte nicht fuer einen Fonds arbeiten. **Damit ist ein neues Ziel im Buch und es hat einen Namen und eine Adresse.**

  **Zum Schluss die letzte wahre Sache, die Georgij noch hat:** *"You are going to be given work by somebody eventually and it is going to be beneath you, and you are going to take it, and you will do it properly because you cannot do anything the other way."* - *"Is that supposed to be a kindness."* - **"No. It is the last true thing I have got and I have run out of the other kind."**

  **Und die Klammer:** er traegt sich beim Hereingehen selbst in das Besucherbuch ein, weil niemand da ist, und beim Hinausgehen die Uhrzeit in die zweite Spalte. **Das Buch ist am Freitag in einer Kiste.**

- **Band 2, Kapitel 22** *I did not offer you anything* (v1.0) - **Tag 215, Mi 6. Mai. Eine Szene, achter Stock in Seongdong, mit Blick auf den Fluss.**

  **Mr Byun**, achtundsechzig, hat das Register des Hauses **sechsundzwanzig Jahre** gefuehrt und ist im November gegangen, weil er nicht fuer Leute arbeiten wollte, die ihn fragen, was er den ganzen Tag macht. **Erster Auftritt und einziger.**

  **Er ist der Erste in diesem Band, der genau das ist, wonach er aussieht.** Keine Hand, kein Kategorienfehler, keine Tragik. Er hat das Geld genommen, er wusste es, und es hat ihn nie beschaeftigt. **Er freut sich ueber Besuch und erzaehlt in den ersten zwei Minuten von den vierzig Prozent Aufschlag fuer die Aussicht.**

  **Und der Augenblick, den Georgij nicht wieder hinlegt:** auf den Vorwurf hin ist er weder erschrocken noch wuetend. **Er versucht sich zu erinnern, welche vier.**

  **Seine Verteidigung ist die gewoehnliche und er bringt sie ohne jede Abwehr:** das Haus hat das verkauft, bevor er in dem Stuhl sass, der Mann vor ihm hat es getan und der davor auch, *"and it is the only thing that house had to sell that nobody could get anywhere else."* Dazu: **"Nobody was hurt."**

  **Was Georgij ihm entgegenhaelt, ist Nam**, in vier Saetzen. Byuns Antwort: *"That is very unfortunate. I do not know her."* - **"No. She does not know you either."**

  **Und dann keine Drohung, sondern eine Ankuendigung:** die vier Kaeufer werden informiert. Mit Namen, mit Betrag, mit Datum, und dass der Eintrag noch da ist. *"What any of them does after that is theirs and not mine."*

  **Die Rueckerstattung wird angeboten und aendert nichts.** *"They are still going to be told."* Und dann faellt er zusammen, sehr schnell, aus einem einzigen Grund: **Mrs Sunwoo kennt jeden.**

  **Der Kern der Szene ist, dass Georgij nichts anbietet und es vorher sagt.** *"I am not trading with you and I want that said before you say another word, because if you say it thinking that you are buying something you are going to be angry with yourself tomorrow."* **Byun sagt es trotzdem.**

  **Und was er sagt, ist der bisher schwerste Fund des Bandes.** Drei sind zu ihm gekommen. **Beim vierten wurde er vom Eigentuemer persoenlich instruiert**, im Stehen, unter einer Minute: kein Rechnungsbeleg fuer das Los, eintragen und im Fruehjahr wieder herausnehmen, **und nichts darueber schreiben, wer es hatte.**

  **Und der Teil, den Byun in sechsundzwanzig Jahren nicht verstanden hat:** *"He said the fee had been paid and I was to put it through the book as though it had come to me."* Das Geld kam aus der eigenen Tasche des Eigentuemers, in einem fertig gemachten Umschlag. **"That is the only time in twenty-six years that anybody has ever given me money so that the money would be in the right place."**

  **Er hat eine Zeile aufgeschrieben und vier Jahre nicht angesehen**, weil erschrockene Maenner dieser Art genau das tun, und Georgij sagt ihm auf den Kopf zu, dass es sie gibt. **Ein Datum und vier Woerter darueber, woher die Anweisung kam.**

  **Und dann der Satz, um den das Kapitel gebaut ist:** *"You have got what you came for."* - **"I did not come for that. I did not know it existed until twenty minutes ago and I did not ask you for it. You offered it to me because you thought you were buying something. I told you before you opened your mouth that you were not, and you did it anyway."**

  **Byuns Urteil und Georgijs Antwort darauf setzen die drei Raeume nebeneinander:** *"Then you are a very cruel young man."* - **"No. I have been in three rooms in the last three weeks and in two of them that would have been true. In this one it is not, and you have not got the first idea why."**

  **Und die Einloesung von Kapitel 20 steht am Schluss und ist der Grund, warum das Kapitel gebraucht wurde:** er hat nichts davon vorher entschieden. Er ging mit vier Daten und einer Adresse hin. **Den Rest entschied er im Stehen, in den vier Sekunden, in denen ein Achtundsechzigjaehriger sich erinnern musste, welche vier.** Und: *"Nobody put a ceiling on it, nobody is going to audit it, and there is no room he has to walk into afterwards and say what it cost."*

- **Band 2, Kapitel 23** *Three of the four* (v1.0) - **Tag 222, Mi 13. Mai, und der Donnerstag darauf. Drei Szenen: das Haus auf dem Huegel, das kleine Zimmer, und eine Entscheidung, die nicht faellt.**

  **Das Kapitel beginnt mit einem Versprechen, das er nicht halten kann, und er laesst es sich nicht als Formsache durchgehen.** Er hat Byun gesagt, die vier Kaeufer wuerden informiert. **Er erreicht drei. Der vierte ist der Mann, den er sucht.** *"He said a thing in a room that will be three quarters true, and Mr Byun will go to his grave not knowing which quarter, and the only person who is ever going to notice is Georgij."*

  **Mrs Sunwoo steht diesmal nicht auf und sagt auch warum:** *"I stood up in March because I did not know what you were and it seemed safer."* Und: *"do not do the thing where you say one sentence and stop, because I am eighty-one and it was charming once."*

  **Er gibt ihr Byun vollstaendig, einschliesslich der Adresse und der Schwiegertochter im selben Haus, und benennt selbst, dass das mehr war als noetig.** Auf *"You are inviting me to do something"*: **"What you do is yours. I have not got a view and I would not give you one if I had."**

  **Was sie tun wird, sagt sie genau:** drei Wochen, **kein lautes Wort und kein unwahres**, und danach wird er zu nichts mehr eingeladen, solange er lebt. Georgij will nicht wissen, wie: *"I want you to be able to say afterwards that you did not tell me."*

  **Und sie durchschaut den Maerz und haelt es ihm nicht vor**, was ihn haerter trifft als ein Vorwurf: *"You came here because you needed the house shut, and telling me the truth was the only way to get it, and both of those are the case at once."* - **"No. You should."** - *"I am eighty-one. There are so few of them that I would run out of afternoons."*

  **Annie wird foermlich informiert, obwohl sie alles weiss, und der Grund ist der bessere von zwei:** sie ist **zwei der vier**, und wer Mrs Sunwoo foermlich unterrichtet und Annie beilaeufig, macht aus ihr eine andere Sorte Kaeuferin. **Sie ist keine andere Sorte.** Der zweite Grund ist schlechter und ehrlicher: von dem Satz in Seongdong ist das der einzige Teil, ueber den er Gewalt hat.

  **Dann der Fund vom siebten Mai, den er seit sechs Tagen mit sich traegt.** Das Haus gehoerte von 2011 bis zum Winter **Mr Yeom**, dreiundsechzig, geerbt, wenig angesehen, hat Geld gebracht. Im Winter hat er es an den Fonds verkauft - **und eine Stellung bei ihnen genommen.** Annie sagt das voraus, bevor er es sagt: *"A fund does not want the building. It wants the man who knows what is in it."*

  **Und die Stellung ist auf der dritten Etage der Adresse in Jung-gu**, zehn Gesellschaften ohne Personal. **Also genau dort, wo Georgij in der Nacht des 16. Maerz um zwanzig nach eins umgekehrt ist**, ohne eine einzige Anfrage mit Datum zu hinterlassen.

  **Die Entscheidung ist die schwerste des Bandes und sie faellt in diesem Kapitel nicht.** Er benennt sie vollstaendig: *"Backing away was invisible. Going at it will not be. There is no version where I do this and stay the man he cannot see."* Und: *"the question is not whether it is dangerous. It is whether I am prepared to stop being the only thing about me that has been useful since March."*

  **Annie gibt keine Erlaubnis und keine Anweisung - aber zum ersten Mal seit dem 3. April eine Meinung**, und sie sagt dazu, warum sie sie diesmal nicht fuer sich behaelt: *"you asked me a fortnight ago to put the ceiling back on and I said no, and I am not going to spend the first difficult one pretending I have not got an opinion."*

  **Und die Meinung ist die Sorte Satz, um die das Buch gebaut ist:** *"Invisibility is a thing you spend. It is not a thing you keep, and a man who keeps it for ever has spent his whole life not being seen and has nothing at the end of it except that."* Dazu die Bilanz: sieben Wochen Unsichtbarkeit haben ihm Nam, Ok, Byun und ein geschlossenes Haus gekauft. **Nicht ihn.**

  **Und das zweite Stueck vom Regal, und Annie zaehlt selbst mit:** der Mann, den er sucht, **besitzt an dieser Adresse ebenfalls nichts.** Keine Anteile, an keiner der zehn, nie. *"He is the reason ten companies with no staff are on the third floor of a building in Jung-gu, and there is no document anywhere in this country that says so, and there never will be, and that is what you are proposing to walk towards."*

- **Band 2, Kapitel 24** *Ten minutes on a Friday* (v1.0) - **Tag 224 bis 228, Fr 15. bis Di 19. Mai.**

  **Die schwerste Entscheidung des Bandes faellt, und sie ist Papierkram.** Ein Registerauszug, zehn Minuten, ein Formular und eine Gebuehr, *"done about four thousand times a day by clerks who are thinking about lunch"*. Und: **"He put his own name on it, because there is nobody else's he could have used."**

  **Und genau darin liegt die Einloesung von Kapitel 20.** Niemand im Raum, kein Deckel, keine Abnahme, kein Zimmer, in das er hinterher gehen muss. *"That is what Annie meant on the thirtieth of April and he had not understood the size of it until he was doing it."*

  **Er wartet danach darauf, etwas zu empfinden, und es kommt nichts.** *"It is a form and a fee."*

  **Annies Reaktion ist der zweite Teil derselben Lektion und schlimmer als der erste.** Zwei Fragen, dann **"Good"**, dann arbeitet sie weiter. *"That is the whole of what was said in that house about the largest decision he has made in his life."*

  **Das Wochenende sind die zwei laengsten Tage seit Oktober**, und das Haus reagiert von selbst: Jang sieht ihn ohne Grund in der Diele stehen, sagt nichts, **und eine halbe Stunde spaeter stehen zwei Mann am Tor statt einem, und seither jeden Tag.**

  **Am Montag wird die erste der fuenf Haelften unterschrieben.** Kwons Teilhaber, dreiundsechzig, ein Termin, kein Feilschen, danach sitzt er eine Weile im eigenen Wagen, bevor er ihn startet. **Kwon ruft an und Georgij nimmt nicht ab**, weil es nichts zu sagen gaebe, das nicht entweder unwahr oder unfreundlich waere. Die Kaeuferin ist eine Gesellschaft in Busan mit einer Angestellten, die noch nie etwas gekauft hat.

  **Vier Arbeitstage. Dann klingelt das Telefon.** Mrs Seo kommt selbst herauf, was sie nicht tut: *"I have been answering that telephone for eleven years and nobody has ever asked for you."*

  **Mr Yeom ist der erste Gegner in zwei Baenden, der keine Angst hat**, und der Grund ist, dass er inzwischen fuer sie arbeitet. Er ist vollkommen entspannt und ausdruecklich nicht geistreich, *"which was the unpleasant part."*

  **Georgij nimmt ihm den einzigen Zug ab, den er hat:** *"You are not going to ask me how I know it was you."* - *"No."* - **"Because you have just told me. You said it in the second half of your first sentence and you did not notice, or you did notice and you wanted me to have it. Either way it is the same information."**

  **Und dann dreht Georgij die Frage um**, und das ist der einzige Punkt, an dem Yeom eine halbe Sekunde zu lange braucht: ein Mann, der ein Haus im Dezember verkauft hat und seit fuenf Monaten draussen ist, zaehlt drei Dinge in der richtigen Reihenfolge auf. *"So I would like to know what you want, and I have got a stronger reason for asking than you have."*

  **Die Einladung ist die Falle und Georgij sieht sie sofort.** Am 27. April hat Annie ihm ein Verhaltensmerkmal gegeben statt eines Namens: **er isst nicht vor Leuten, an denen er arbeitet.** Und jetzt hat ihn jemand zum Mittagessen eingeladen. *"A table at half past twelve is a table at which somebody is going to have to decide whether to eat."*

  **Und der Preis des Kapitels steht auf der Treppe:** Yeom weiss, dass er Anfang Mai in dem Gebaeude war, in dem niemand am Empfang stand. Entweder Hwang hat es gesagt - oder jemand hat das Besucherbuch aus der Kiste geholt und **zwei Zeilen in Georgijs eigener Handschrift gelesen, Uhrzeit hinein und Uhrzeit hinaus.** *"He wrote both of them himself, at a desk nobody was standing at. It seemed to him at the time that a man who signs a book when somebody is watching should sign it when nobody is."*

  **Annies Schluss stellt den Donnerstag scharf:** *"I want you to hear me say that I think you were right, because I am not going to be able to say it again after Thursday."* Und der Grund: entweder er hat den Boden gefunden, **oder jemand hat sich ihm gegenuebergesetzt und nicht gegessen** - *"and after that neither of us is going to have the luxury of an opinion about anything."*

- **Band 2, Kapitel 25** *Four people who could see us* (v1.0) - **Tag 230, Do 21. Mai, halb eins. Eine Szene, vierter Tisch von der Tuer links.**

  **Die Probe faellt sofort und schliesst genau einen Mann aus. Yeom isst.** Ohne Umstaende, mit sichtbarem Vergnuegen, und er redet dabei und legt die Staebchen zwischen den Saetzen nicht hin. *"It rules out one man. That is all it rules out and it is worth having and it is not worth anything else."*

  **Und Yeom bemerkt, dass Georgij nicht isst, und sagt es**, was noch keiner getan hat: *"You are moving it about. I have watched a great many people not eat at this table and you are doing it better than most."*

  **Was Yeom vom Fonds bekommen hat, gibt er vollstaendig her:** *"They told me to find out and to be pleasant about it. Those were the two things and there was not a third."* **Den Namen des Anrufers gibt er nicht**, und sein Grund ist der erste seit Maerz, den Georgij nicht bestreitet: siebenmal im Leben fuer jemanden gearbeitet und nie einen davon herausgegeben, *"and if I started at sixty-three I would not know who I was in the afternoon."*

  **Und dann faellt der Fund, den Georgij nicht geholt hat.** Byun ist im Februar des Vorjahres aus Angst von selbst zu Yeom gegangen und hat ihm von **einer** Gebuehr erzaehlt. Yeom hat es durchgehen lassen, **weil der Mann von selbst gekommen war** - *"A man who tells you a thing you would never have found out has not got anything else in his pocket."* Und als er hoert, dass es vier waren: **"That was my view for a very long time and I have just watched it stop being one."**

  **Die vierte Gebuehr hat Yeom selbst bezahlt.** Aus der eigenen Tasche, in einem Umschlag, damit im Buch eine gewoehnliche Zahlung steht - fuer einen Anrufer, der sagte, er frage **im Auftrag von jemandem, der dankbar waere.**

  **Und er hat nicht gefragt, wer, und das ist keine Feigheit, sondern Arithmetik**, und es ist die kaelteste Rechnung des Bandes: *"If I ask who, then he tells me, and then I have done a favour for a person and I am owed by a person. If I do not ask, then I am owed by whoever it is, and whoever it is knows that I did not ask, and that is worth about ten times as much and it costs nothing."* **Ausgezahlt hat es im Dezember**, in einem Preis ueber Wert und einer Stellung.

  **Und der Anrufer von vor vier Jahren hat zum Schluss gesagt, er freue sich, dass sie sich endlich getroffen haetten.** Sie waren sich nie begegnet. Yeom erinnert sich daran, weil er es seiner Frau erzaehlt hat. **Das ist die dritte voneinander unabhaengige Quelle fuer denselben Satz** - nach Mr Ok in Kapitel 17 und Chairman Woo in Kapitel 13.

  **Und mitten in dem Satz, in dem Yeom sagt, dass er die vierte Gebuehr bezahlt hat, legt am dritten Tisch vom Fenster ein Mann von etwa sechzig, nicht gross, einen Loeffel neben eine Schale, die er nicht angeruehrt hat.** Er sitzt dort eine Stunde und zehn Minuten. Die Schale wird kalt.

  **Georgij sieht ihn in der Randsicht und dreht den Kopf nicht um einen Grad.** Beim Hinausgehen sieht er nicht hin, wird nicht langsamer, **und tut auch nicht das, was ein Mann mit den Schultern tut, wenn er beschlossen hat, nicht hinzusehen.** *"He has been practising that since October and it has never once mattered until today."*

  **Die drei Moeglichkeiten stehen am Schluss nebeneinander und keine wird aufgeloest:** ein Niemand ohne Appetit; jemand, der nicht wusste, dass Georgij dort sein wuerde, **und den Georgij damit gesehen hat, ohne dass er es weiss**; oder jemand, der die Uhrzeit der Reservierung kannte und gekommen ist, **um sich das anzusehen, was seit Maerz um sein Arrangement herumlaeuft.**

  **Und der Schlusssatz ist die neue Lage des Bandes:** *"Both of those are facts. Only one of them is a fact about Georgij, and he does not know which."*

  **Dazu Georgijs einziger Rat an Yeom, und er ist ernst gemeint:** *"Do not say the rest of that out loud in this room. ... you have just told me you do not know who you did it for, and that is the only thing keeping you comfortable, and it is a great deal safer than knowing."*

- **Band 2, Kapitel 26** *The third name on a list of three* (v1.0) - **Tag 236, Mi 27. Mai. Eine Szene, zweiter Raum einer Werfthalle bei einem Stapellauf.**

  **Der Grund, es im Maerz nicht zu tun, ist am 15. Mai um zwanzig nach neun in ein Registeramt gegangen.** Deshalb geht er jetzt hin. Das Korridorangebot aus Kapitel 4 wird zum ersten Mal so benutzt, wie es gemeint war, **und Sang-hoon kommt durch vierzig Leute selbst herueber**: *"There is never a corridor. It is a figure of speech and you knew what I meant in March."*

  **Georgij gibt acht der neun Zeilen und haelt die neunte zurueck.** Sang-hoon erkennt ihn nach zwei Sekunden und verlangt die neunte trotzdem: *"you are holding one and I would like to hear it."*

  **Die Frage klingt absurd und ist die einzige, die zaehlt:** *"Have you ever watched him eat."* Und Sang-hoon gibt sie nicht sofort her - **zum ersten Mal ueberhaupt** - bis er weiss, was sie wert ist. Georgij legt ihm Annies Geschenk vom 27. April umsonst hin: **"That is the most expensive sentence anybody has said to me this year, and you have just put it in front of me for nothing."**

  **Die Antwort ist der Kern des Kapitels.** Acht Jahre, ueber zwanzig Gelegenheiten, Abendessen bei ihm zu Hause, zwei Mittagessen, etwas auf einem Boot 2019. **"And I have never once seen him put anything in his mouth."** Und: *"I have known that man for eight years and I could not tell you one thing that he likes."*

  **Was Georgij ihm daraufhin sagen muss, ist die zweite unertraegliche Nachricht in sechs Wochen**, und er gibt sie flach: *"He has been working on you for eight years."* Sang-hoons Antwort: **"I have been sitting at that man's table since I was fifty-one. I have made four decisions at those dinners that I have never been able to account for afterwards, and I put every one of them down to being tired."**

  **Und dann die Umkehrung von Kapitel 4, und Georgij bringt sie von sich aus:** wenn ein Mann sechs Jahre vor ihm dasselbe getan hat, **dann hat Georgij ihn im November nicht gerichtet, sondern den Griff dort gefunden, wo ihn jemand anders liegen gelassen hat.**

  **Sang-hoon gibt den Namen ungefragt her**, und benennt selbst, dass er ungefragt war: *"You did not ask and you were not going to ask, and I have watched you not ask for four minutes."* **Choi Dae-ho. Neunundfuenfzig. Frueher Staatsanwalt, vorzeitig heraus, niemand sagt warum. Direktor einer Private-Equity-Firma in Hongkong ueber eine Anwaltskette in Singapur, und er hat nie in seinem Leben investiert. Er gibt Abendessen.**

  **Und damit faellt der Name zum ersten Mal in Band 2 - und der Leser hat ihn seit Kapitel 3 in Band 1.** Am 25. Oktober, vierzehn Minuten nach dem Betreten des Saales, hat Mr Hong ihm drei Namen genannt, an denen man vorbeigeht. **Woo. Sunwoo. Choi Dae-ho. Dritter.** *"It has been in my notebook for seven months in the third position, which is where a man puts the one he actually means."*

  **Sang-hoons Trost ist keiner und er ist das Nuetzlichste, was er sagt:** *"You did not miss it. It was put in a list of three so that you would keep it and not use it. Hong is a decent man and he has never in his life understood why he gives people three names instead of one."*

  **Und die neue Groesse der Sache steht in seinem naechsten Satz:** *"As of about six minutes ago I do not know how far out that goes, and neither do you, and I am not going to pretend it is a comfortable position for either of us."*

  **Sang-hoons Bitte ist die erste, die er je gestellt hat, und sie ist praezise.** Nicht der Mann - **die vier Entscheidungen.** *"Because the man is yours, and I have watched you for seven months and I am not going to be in the way of that. And because I have had a great deal taken off me this year by people who were entitled to, and I would like the four things back that I gave away for nothing."*

  **Georgij bleibt danach zwanzig Minuten stehen, weil Sofortgehen die Unterschrift waere**, und schreibt im Wagen eine Zeile, und nicht den Namen: ***Hong. 25 Oct. Third of three. Ask who put him at that table.***

  **Und der Schluss stellt den Abend scharf:** er muss in das kleine Zimmer gehen und einen Namen aussprechen, **den sie seit Dezember haelt** - und sie muss dabeistehen und hoeren, wie er ihn sagt, **bekommen von einem Mann, der ihn kaufen wollte, bei einem Stapellauf, umsonst.** *"Neither of them chose the afternoon."*

- **Band 2, Kapitel 27** *What he collects* (v1.2) - **Tag 236, Mi 27. Mai, zehn nach acht. Eine Szene, das kleine Zimmer, und die Aufloesung des laengsten Fadens des Buches.**

  **Er hat vier Stunden Rueckfahrt und verbringt drei davon damit, sich Fassungen zu bauen, und nimmt auf der Bruecke alle wieder auseinander.** *"A man who arranges the sentence has decided in advance what the other person is going to feel about it."* Also zwei Woerter, nichts an beiden Enden, **und dann steht er da und laesst sie es in der Form haben, in der es kommt.**

  **Was auf ihrem Gesicht geschieht, ist eine Reihenfolge und sonst nichts:** zwei Sekunden nichts, dann schreibt sie das Wort zu Ende, in dem sie war, dann legt sie den Stift hin.

  **Ihr Urteil ueber Sang-hoon steht in einem Satz und sie schiebt es weg:** *"Then he is a better man than I have ever been prepared to say, and I am going to have to sit with that, and not tonight."*

  **Und dann faengt sie sich bei einer Gewohnheitsluege und raeumt sie sofort ab**, was sie noch nie getan hat: *"I have known him since I was twenty-four," she said, and then stopped. "That is not true and I have said it for so long that it comes out by itself. I was fourteen."* **Sie hat mit vierzehn gemerkt, dass er nicht isst, und es mit dreissig verstanden.**

  **Die drei Gruende fuers Zurueckhalten waren alle wahr und keiner war der Grund.** Dezember, Maerz, der 27. April. **"And none of them is why."**

  **Der echte Grund ist der Satz, um den dieses Buch gebaut ist: "He collects."** Er kauft Menschen, in jenem Haus und in zwei anderen, seit sehr langer Zeit, **und sie weiss nicht wie viele und hat es nie wissen wollen.**

  **Und damit steht die Erklaerung fuer die Anomalie aus Kapitel 21 und 25:** *"An absence in a ledger is a question. A payment in a ledger is a Tuesday."*

  **Was unter Georgijs Regungslosigkeit passiert, sagt nur die Erzaehlstimme, und Annie sieht es trotzdem.** Vier Dinge haben ihn je dazu gebracht, Hand an jemanden zu legen, und das groesste davon ist, **was Erwachsene mit Kindern vorhaben.** *"Annie watched him not move and did not mistake it for one second."*

  **Sie weiss es seit dem 20. Maerz - seit er in Kapitel 9 die drei aufgezaehlt hat, die getroffen werden, ohne etwas getan zu haben, und der dritte war** *"whoever is on the fourth line, who nobody has ever billed."* **Sie hat es gerechnet, waehrend er noch sprach, und dann nach der Frau in Ulsan gefragt.** Damit ist Annies Ausweichfrage aus Kapitel 9 rueckwirkend etwas anderes, als sie beim ersten Lesen war. **Achtundsechzig Tage.**

  **Und der Grund unter dem Grund ist die haerteste Stelle im Band:** irgendwo gibt es einen Menschen ohne Zeile, ohne Eigentuemer und ohne Datum, **weil man ihn im Fruehjahr aus dem Buch genommen hat und nie jemandem in Rechnung gestellt hat.** **Und der Satz ist ihrer, nicht seiner** - sie hat ihn ihm am 2. Januar (Band 1, Kapitel 34) und am 11. Maerz (Kapitel 5) gegeben, beide Male als das, was ihn am Leben haelt: *"And it is my sentence ... both times I was telling you the thing that keeps you alive. I did not want you to find out that it is also a description of somebody who is not."*

  **Sie entschuldigt sich nicht und sagt auch warum nicht:** *"I am not going to tell you that I am sorry about it, because I am not, and you would know inside a syllable. I am telling you what I did. You may do whatever you like with it."*

  **Und Georgijs zwei Saetze sind die genaueste Sache, die er ihr je gesagt hat:** *"The first is that you were wrong and it does not matter now."* Und: **"this is the first time you have ever done anything for a reason that was not exactly what you said it was. And you did it about this. Out of everything in this year, you did it about this."** - *"Yes."*

  **Und auf die Frage, was er tun wird, kommt nicht der Gegner, sondern der Mensch.** *"Find the person."* - *"That is not what I asked."* - **"It is what I am going to do. The rest of it is going to happen to him and it is going to be complete ... But that is not what I am going to do first and it is not what any of this is for."**

  **Der erste Faden faellt ihm mitten in der Stunde ein und er sagt nichts davon.** Was im Fruehjahr aus einem Buch genommen wurde, stand vorher darin: vier oder fuenf Monate lang, mit Fundstelle und Saison, und **es war gewoehnlich, solange es dort stand.** Byun hat es geschrieben und wieder herausgenommen. Hwang hat es nie gesehen. **Und eine Frau hinter einer Glasscheibe hat dreiundzwanzig Jahre lang jede Zeile gelesen, die dieses Haus geschrieben hat** - und ist Mitte Mai zum letzten Mal aus dem Gebaeude gegangen.

  **Und der Weg zu ihr geht ueber den Mann, den er am 4. Mai auseinandergenommen hat:** *"He does not know where she lives and he has never asked, and there is exactly one person in this country who would have written it down. Mr Hwang keeps everything."*

  **Und die Stunde auf dem Boden ist die Romanze dieses Kapitels und besteht aus Schweigen.** *"Then come and sit on the floor for an hour before you start."* Kein Wort die ganze Stunde, die Hand im Haar, der Kopf zurueck an die Seite des Schreibtischs.

- **Band 2, Kapitel 28** *He keeps everything* (v1.2) - **Tag 237, Do 28. Mai. Eine Szene, dritter Stock im Haus am Fluss, zwei Kisten und ein Tisch.**

  **Der Titel ist Mrs Jeons Satz ueber Hwang aus Kapitel 7**, und er kommt zurueck, um sie zu finden: *"He keeps everything. Every note, every release, every letter that has ever come into this house about anything. He is proud of that too."*

  **Die Tuer will seinen Namen nicht mehr.** Dreimal in acht Wochen hat er sich in ein Buch an einer Tuer geschrieben, und jedes dieser drei Male ist mit Zinsen zurueckgekommen. **Jetzt ist kein Buch mehr da.** Die Glasscheibe steht ausgerahmt an der Wand, der Schlitz fuer Umschlaege ist ein Loch in einer Sperrholzplatte, **der eine Stuhl auf der Besucherseite ist weg.**

  **Georgij hat nichts zu bieten und sagt das als Erstes.** *"I have come to ask you for something, and I have nothing to give you for it, and I am not going to dress it up. There is no arrangement here and there is nothing at the end of it for you."* Hwangs Antwort: **"That is at least consistent."**

  **Und in diesem Raum hat zum ersten Mal Hwang die Macht.** Deshalb bekommt Georgij hier Fragezeichen, wo er sonst Punkte hat: *"Why did you do it?"*, *"How many?"*, *"Do you have it?"* **Die Machtlage entscheidet, nicht der Rang** - und sie hat sich gedreht.

  **Er kennt sie sofort und braucht nichts nachzuschlagen.** *"Jeon Mi-ja. Twenty-three years at that desk. Her last day was the twelfth of May and she came up here at half past four to give me the keys to the drawer, and she would not put them on the table. She put them in my hand."* Und: **"I have not had to look that up once since the twelfth of May, and I have tried."**

  **Der Fehler zum dritten Mal, und diesmal benennt er ihn selbst.** Zwoelf Stellen in der zweiten Aprilwoche, alle zwoelf richtig, **alle zwoelf an einem Nachmittag aus einer Tabelle.** *"I did not go down to that floor. I have been in this building since the autumn and I have been down to that floor twice."*

  **Und Georgij nimmt ihm das Urteil nicht ab:** *"No. You have just told me. Leave it where it is."*

  **Das Zentrum des Kapitels ist der 9. Januar, und Hwang gibt es her, bevor er die Adresse gibt, damit es keine Bezahlung ist.** Mrs Jeon sass in diesem Raum mit einem **selbst gekauften Schulheft** und hielt es ihm hin. Darin: alles, was in dreiundzwanzig Jahren ueber ihren Schreibtisch ging **und nicht abgerechnet wurde.** *"Not fraud. She was careful about that word and I have thought about how careful she was."*

  **Was er ihr geantwortet hat, ist juristisch tadellos und deshalb die schlimmste Stelle:** Wind-up, Zustimmung des Verwalters, eine unfertige Untersuchung sei schlimmer als keine. **"Every word of that is true, and I have taken it apart every night for three weeks and it is still true, and it is still the worst thing I have ever said to anybody."**

  **Und er hat es nicht angefasst.** *"I did not open it. She had it in her hands and she was holding it out and I did not put my hand on it."* Sie steckte es zurueck in die Tasche, sagte danke, **ging nach unten und machte noch vier Monate.**

  **Das Zeugnis, das nichts wert ist.** Zwei Seiten, jeder Satz wahr, das beste, das er je geschrieben hat - **und keine Firma im Land liest ueber den Briefkopf hinaus.** Er wusste das beim Schreiben. *"It was the same thing," said Georgij.*

  **Und dann die Schuld, die Georgij sich selbst stellt, unaufgefordert.** Er hat die Zusage vom 20. Maerz eingeloest: **ein Mann in dieser Stadt schuldete ihm eine Vermittlung, und Ende April hat eine Firma sie angerufen.** Auf die Nachfrage, was daraus wurde: **"And I do not know."**

  *"I made the call and I put a line through it. I have not asked her and I have not asked him, and in ten weeks it has not once been the most urgent thing in front of me."*

  **Hwangs Angebot einer Gemeinsamkeit nimmt er nicht an und weist es auch nicht von sich, sondern rechnet es nach** - und der Text sagt vorher, dass die fertige Antwort auf dem Weg zerfiel: *"Georgij had an answer ready and heard what was wrong with it before he got to it."* Dann: **"You did twelve in an afternoon and did not go down to the floor. I did one in a morning and did not go down either. That is a difference in size and it is not a difference in kind."**

  **Hwangs einzige Bitte ist keine Bitte um sich selbst, und sie ist die Klammer zu Mrs Jeons letztem Satz in Kapitel 7** (*"I would like that written down somewhere as well"*): *"I would like there to be a piece of paper somewhere in the world that says she did."*

  **Georgij stimmt nicht zu und lehnt nicht ab, und Hwang fragt kein zweites Mal.** Im Wagen schreibt er es dann doch, unter das Datum, **ohne es jemandem versprochen zu haben:** *Jeon Mi-ja. 9 Jan. Held it out. He did not take it.* / *She has a list.*

  **Am Schluss faengt Georgij an, die Prognose aus Kapitel 21 zu wiederholen - und Hwang laesst ihn nicht.** *"You said that to me in May. You said eventually, and you said it would be beneath me, and I asked you whether it was supposed to be a kindness. I have had three weeks with it and I am used to it."* Und dann: **"Do not say it twice. The second one is not for me."**

  **Das ist das erste Mal, dass jemand Georgij liest, so wie er alle liest**, und es stimmt: die zweite Fassung war fuer ihn selbst. Er nimmt es an und sagt es auch. *"No. It is not."*

  **Und danach steht die letzte Auskunft, und sie ist eine geschlossene Tuer:** die Settlement-Buecher sind **am 20. Mai in einem Wagen aus dem Haus gegangen, gegen ein von Hwang unterschriebenes Verzeichnis**, in ein Lager eines Fonds, der sie nie aufmachen wird. *"I could have had the settlement books copied in the first week of May and not one person would have asked me a question about it. It did not occur to me, because in the first week of May I still thought the worst thing in this house was a practice I had stopped."* - **"I should have asked you for them in May." - "Yes. You should."**

  **Damit ist die Lage vor Kapitel 29 eindeutig:** ausser dem Lager gibt es genau **eine** Aufzeichnung darueber, was an diesem Schalter nie durchgelaufen ist, und sie liegt in einer Wohnung vier Haltestellen draussen, in einem Schulheft, das eine Frau selbst bezahlt hat.

  **Korrigiert am 24.08. (v1.2).** Bis dahin sagte Georgij die Prognose zum zweiten Mal, und Hwang stellte woertlich dieselbe Frage wie in Kapitel 21 (*"Is that supposed to be a kindness."*). **Das war dieselbe Szene zweimal**, und `check.py` hatte den Satz in beiden Kapiteln gemeldet - der Fund lag da und wurde fuer ein Motiv gehalten.

  **Und der Schluss stellt das naechste Kapitel scharf:** am 16. Maerz hat sie ihren Preis genannt, und der Preis war ein Name. **"He is going to arrive at her door without one."**

- **Band 2, Kapitel 29** *The rest of what I know* (v1.3) - **Tag 238, Fr 29. Mai. Eine Szene, zweiter Stock, ein Zimmer und eine Kueche, vier Haltestellen draussen.**

  **Der Titel ist ihr eigener Satz vom 16. Maerz**, an dem der Preis haengt: *"Come back when you have your name, and I will tell you the rest of what I know, which is not very much and is worth having."*

  **Er kommt mit dem Bus, und das ist eine Entscheidung.** Mr Ku bietet den Wagen zweimal an. **Ein Wagen dieser Art vor der Tuer einer Frau, die seit siebzehn Tagen ohne Arbeit ist, ist ein Satz ueber sie, zugestellt an alle im Treppenhaus** - und sie muesste darin wohnen bleiben, wenn er weg ist.

  **Ihr erster Satz an der Tuer erledigt die Verhandlung, bevor sie anfaengt:** *"You do not have your name. I can see that from here."* Und: **"Then you have come to ask me for something on credit, and I told you in March what I do about that."**

  **Ihr Urteil ueber Hwang ist kaelter als jedes von Georgij und faellt in zwei Saetzen:** *"He could have opened it in January. He has had from January until May to be sorry about it, and being sorry about it is not the same as opening it, and I am not going to be the one who tells him it is."*

  **Was er ihr zuerst gibt, ist keine Information, sondern eine Bestaetigung** - das Einzige, was ihr in dreiundzwanzig Jahren niemand gegeben hat: *"You were right."* Nicht wahrscheinlich, nicht es-ist-was-dran. **"The fourth reference on that back page is a person, and there was no bill because there was never going to be one."**

  **Und dann kommt ihre Nacht, und sie ist die genaueste Stelle im Kapitel.** Neun Minuten nach elf sagte man ihr, sie solle den Schalter offen halten, es komme noch eine Verrechnung. **Sie sass bis Mitternacht. Es kam niemand.** Am Morgen hiess es, es sei ueber das Buero gelaufen. *"I have been in settlement for twenty-three years and that is the only night I have ever been told to wait for something that did not exist."*

  **Und dann legt sie den Anruf auf den Tisch, und er ist der Grund, warum sie ueberhaupt etwas von ihm will.** Am 10. April erfuhr sie, dass sie geht, **und niemand ausserhalb des Gebaeudes wusste das.** Am 28. April rief eine Firma aus Yeouido an. **Es fehlte kein Name** - die Anruferin nannte ihren eigenen, ihre Durchwahl und das Haus, und sie sass danach zwei ausgesucht hoeflichen Leuten gegenueber. **Was fehlte, war der Weg:** am Ende fragte sie, wie ihr Name auf diesen Tisch gekommen ist, *"and then said that it had come through a contact."*

  **Und die Bilanz, die Georgij ihr vorrechnet, beantwortet den Einwand, den das geschlossene Haus aufwirft.** Die Schliessung hat die Seite nicht wertlos gemacht, sondern **unbestaetigbar**: *"That page has four references on it and a phrase, and it has no column for who paid, and the house that wrote it is finished and cannot be asked anything. That is the whole of why she is safe."* Und weiter: *"a page that nobody living will stand behind is a photocopy of an allegation."*

  **Hwang faellt als Zeuge aus, und Georgij sagt auch warum:** *"Mr Hwang can say the page is his. He cannot say who was in the room, and what he does know he knows because I told him in May."*

  **Mrs Jeon zieht die Folge selbst, in ihrem eigenen Vokabular:** *"So I am the bill."* - **"You are the bill."** Sie ist genau das, was die Freigabe nie gesagt hat (Kapitel 7: *"it does not say who is receiving it, because the receiving is what the bill is for and there is no bill"*), **und sie ist die Einzige in der ganzen Sache, die nie von irgendwem bezahlt worden ist.**

  **Also nahm sie es nicht, und ihr Grund ist ihr Beruf und nicht ihr Stolz:** *"A line that arrives in the book and nobody will say where it came from is the one thing I know how to be afraid of. I have been sitting on one of those since January, and I was not going to go and work inside a second one for a salary."* Und dann: **"It was you." - "Yes."**

  **Korrigiert am 24.08. (v1.2).** Bis dahin stand hier, sie unterschreibe nichts, *"that has a blank where the counterparty goes"*. **Das war fachlich falsch und dramaturgisch duenn:** die Firma hatte einen Briefkopf, die Anruferin hatte sich vorgestellt, der Vertragspartner war vollstaendig da. Eine Frau mit dreiundzwanzig Jahren Settlement benutzt dieses Wort nicht falsch. **Die Leerstelle war nie ein Name, sondern eine Herkunft** - und damit ist ihre Absage dieselbe Form wie die vierte Zeile und nicht mehr eine Besessenheit mit Namen.

  **Das ist die erste wahre Auskunft, die sie seit Januar bekommt, und deshalb verlangt sie sofort die ganze:** *"Then you may have the rest of the question. You are somebody's. I could see that in March and I can see it now. Whose."*

  **Und hier steht die Entscheidung, die das Buch bisher vermieden hat.** Er sieht drei Auswege und beschreibt sie: *"the second one was good enough that she would not have found it for a week."* **Er nimmt keinen davon, und der Grund ist der moralische Kern des Kapitels: "All three of them worked by making her somebody who is handled. She has been that in a building for twenty-three years, and she was going to know."**

  **Er bezahlt mit dem Einzigen, was er besitzt, und es ist genau das, was Annie gefaehrdet:** *"I am on that page. Lot eleven and lot fourteen, four lines apart. I was in the room for both of them, and I was one of them, and the one I was is the second one."*

  **Und die Machtlage dreht sich mitten in der Szene, und die Satzzeichen folgen ihr.** Ihre beiden Fragen davor sind flach. Die eine, bei der sie von seiner Antwort abhaengt, geht hoch: **"Do you understand what you have just put on this table?"** - und der Text sagt es ausdruecklich: *"She had asked him two questions since he came in and both of them had been flat. That one went up at the end."*

  **Er rechnet ihr auf Verlangen vor, was er hergegeben hat**, und beschoenigt nichts: *"You could sell it. You could take it to a newspaper. You could hold it for eight years and take it out when you needed something."* - **"And you did it anyway." - "I did it anyway."**

  **Ihre Begruendung, es anzunehmen, ist ein Satz:** *"Twenty-three years, and nobody in that building ever told me anything that could hurt them."*

  **Das Heft ist kein Kassenbuch.** Karierte Blaetter, gruener Deckel, **etwa vierzig Zeilen in dreiundzwanzig Jahren**, jede mit Datum, Uhrzeit und ungefaehr sechs Woertern.

  **Und was daraufsteht, ist der Ertrag des Kapitels: Los sechs.** Fruehjahrsauktion, vor vier Jahren. **Im Buch vom Januar davor bis zum September danach**, und in dieser Zeit sind vier Posten gegen dieselbe Fundstelle ueber ihren Schalter gelaufen und alle vier haben abgerechnet: **Blumen, zweimal. Ein Fahrer. Und ein Arzt, im Juli.**

  **"I passed the invoice myself. It was a proper invoice from a proper practice, and I did not think about it for four years, and I have thought about it every day since the ninth of January."**

  **Sein Versprechen ist genau so weit, wie Regel 1 es zulaesst, und keinen Zoll weiter:** kein gutes Ende, weil er es nicht weiss. **Aber: "Whatever it is, and whenever I have it, you will hear it from me and not from anybody else."** Ihre Antwort: *"That is the correct answer, and it is the first correct answer I have had from anybody since January, and I notice that it is also the only one that costs you something to keep."*

  **Sie verleiht das Heft und verschenkt es nicht.** *"Copy it and bring it back. I have had it for twenty-three years and I would like it in this flat."* - **"I will bring it back on Tuesday."**

  **Ihr letzter Satz an der Tuer ist die Antwort auf Hwangs Bitte aus Kapitel 28, und sie weiss nichts von der Bitte:** *"You may tell him from me that I kept mine too, and that I bought the book myself, and that it did not take a great deal of courage until the day it did."*

  **Und der Anruf bekommt im Bus seine Antwort, zehn Wochen zu spaet:** *"The call was made. It was refused in the first minute it was possible to refuse it, and she was right to refuse it, and nobody would have had to explain any of that to him if he had asked once in April."*

  **Und der Schluss ist die erste Sache in zwei Baenden, die er ohne Erlaubnis getan hat.** Er rechnet es auf der Rueckfahrt zweimal durch und bekommt zweimal dasselbe Ergebnis, **naemlich dass sie es nicht tun wird, und dass er damit recht hat, und dass Rechthaben nicht der Punkt ist.** *"Nobody gave him leave to do it. He is going to have to go into the small room tonight and say so."*

- **Band 2, Kapitel 30** *A person with nothing* (v1.0) - **Tag 238, Fr 29. Mai, zwanzig nach sieben. Eine Szene, das kleine Zimmer, bis halb zwoelf.**

  **Der erste Absatz benennt die Reihenfolge, die er NICHT nimmt, und dass er sie kann:** erst das Mitgebrachte, dann der Preis, wenn der Raum schon zufrieden ist. *"He has used that order on other people this year and it works."* **Er sagt es andersherum, und das ist der ganze Anfang.**

  **Annies Reaktion ist keine Reaktion, sondern eine Verwaltungsfrage:** *"Her name."* So nimmt sie einen Schlag auf.

  **Und die einzige Regung, die sie nicht kontrolliert, ist eine Kleinigkeit:** *"Annie put the folder down on the desk and squared it with two fingers, which is not a thing she does."*

  **Sie stellt die Lage selbst auf, ohne Vorwurf:** *"So there is a woman in this city who can put a buyer and a lot number in the same sentence and be believed. She was behind the glass when both of them went through, and there is nothing whatever standing between her and a telephone."* - *"And you decided that." - "I decided that."*

  **Der Ertrag kommt erst danach, und bei einem der vier Posten dreht sie sich um.** *"She turned round at the doctor."*

  **Und ihr Satz darueber ist der Grund, warum das Kapitel gut ausgeht:** *"That is the first piece of paper in this entire business that was made by somebody who was not in the trade. Everything else has been made by people who know how to make it disappear. A receptionist in a practice does not know that and has never needed to."*

  **Der Satz, den er in der Hand hatte und nicht benutzt hat, und sie hat den ganzen Abend darauf gewartet.** Sie benennt ihn selbst und beziffert ihn: *"It is a good sentence. It is worth about four minutes and it would have cost you the rest of the year."*

  **Und sein Grund, ihn nicht zu benutzen, ist die praeziseste Unterscheidung im Band:** *"You held something back from me. I handed something of yours to a stranger. Those are two different verbs and only one of them can be taken away from the person it belongs to."* - **"That is the answer, and I want you to know that I checked."**

  **Sie gibt ihm sein Urteil ausdruecklich recht und nimmt ihm den Trost daran sofort wieder weg:** *"She is not going to use it." - "No." - "And it does not matter at all."*

  **Und der Titel steht in seiner Antwort:** *"A person with nothing has exactly one asset, and it is the thing she knows, and she does not have to be a bad woman for that to become the only door in the room."*

  **Annies Entscheidung ist keine Strafe, sondern das Instrument, das Georgij im April haette nehmen muessen.** Die Settlement-Stelle der Gwangyang-Firma, deren Haelfte ihr seit dem 18. Mai gehoert. **Und die Bedingung ist genau die, an der der Anruf im April gescheitert ist:** der Eigentuemername auf der ersten Seite, schriftlich, und der wahre Grund dazu.

  **Die Asymmetrie sagt sie selbst:** *"That is in the commercial register and anybody in this country may go and read it. That is the whole of the difference between what I am about to give her and what you gave her at half past ten this morning."*

  **Und dann der Satz, an dem das Kapitel haengt.** *"You have just described what you did to me." - "Yes."* Und danach, ohne jedes Gewicht: **"You were the most dangerous thing in that building and you had nothing, and I have never once pretended to myself that those were two separate facts."**

  **Was daraus folgt, sagt er, und sie korrigiert es:** *"Then I have not been punished." - "No. You have been corrected, which is worse, and you are going to feel it in about four days when you notice that I did the thing you should have done in April and that it took me eleven minutes."*

  **Die Zusage am Schluss ist vollstaendig, weil sie die Vollstaendigkeit verlangt** (*"I do not want a piece of it turning up in September with a good reason attached"*): **"I will not give anything of yours to anybody without asking you first, and if the room is such that I cannot ask, I will not give it, and I will lose whatever is lost."**

  ---

  **Und die Romanze dieses Kapitels ist die Erschoepfung, und sie ist die erste, die ihn einholt.** Er laeuft seit dem 18. Maerz ohne einen Tag Pause. **Die Hand im Nacken ueber dem Kragen ist neu** (Kapitel 27 war die Hand im Haar), und dauert etwa sechs Sekunden.

  **Der Satz, den er nicht zu Ende sagt, ist die Vorbereitung auf den Schlusssatz des Bandes.** *"I was going to say that I do not mind being corrected by you, and then I heard the end of the sentence coming and I did not want to put it in the room while you are working."* - **"Then do not. Not tonight, and not because I would not want it."**

  **Und dann das Erste, was er in zwei Baenden in ihrer Gegenwart nicht kontrolliert: er schlaeft ein.** Kopf an der Seite des Schreibtischs, eine Hand offen auf dem Knie. **Annie bewegt das Bein eine Stunde und zwanzig Minuten lang nicht** und blaettert mit zwei Fingern.

  **Und um halb zwoelf sagt sie ein Wort laut, zu niemandem: "Yes."** Woraufhin, bleibt offen und soll offen bleiben.

- **Band 2, Kapitel 31** *Nobody hides flowers* (v1.0) - **Tag 239, Sa 30. Mai. Zwei Szenen, der Schreibtisch vor sieben und ein Blumengeschaeft in Hyoja-dong.**

  **Das Kapitel beginnt mit dem Anschluss an Kapitel 30:** er wacht um eins auf dem Boden des kleinen Zimmers auf, **mit einem Mantel ueber sich, der ihm nicht gehoert.** Um zehn vor sieben liegt der Mantel wieder ueber der Armlehne. Es wird kein Wort darueber gesagt.

  **Er schreibt das Heft mit der Hand ab, nicht am Geraet**, weil er seit fuenf Monaten einem Kopierprotokoll rueckwaerts durch ein Gebaeude folgt (Kapitel 16).

  **Und dabei findet er, dass Mrs Jeon ihm mehr gegeben hat, als sie gesagt hat.** Laut ausgesprochen waren es vier Posten. Auf der Zeile steht: *6 Apr. 27 Apr. Hyoja-dong Flowers, house acct, both. 26 Apr, car, no letterhead kept. 3 Jul, practice, no letterhead kept.* **Drei Briefkoepfe, einer ausgeschrieben** - weil das Haus dreissig Jahre lang jede Woche dort Blumen gekauft hat und sie diesen Namen im Schlaf schreiben konnte.

  **Er fragt vorher um den Tag, und das ist die Zusage vom Vorabend in Betrieb**, ohne dass einer von beiden sie benennt. *"I would like the day." - "For what." - "The flowers."*

  **Der Titel steht in seiner Begruendung:** *"A van had to go somewhere, and a man had to be told where, and somebody wrote the address down in the ordinary way."* - *"And nobody has thought about it since."* - **"Nobody has thought about it once. Nobody hides flowers."**

  **Annie liefert das Risiko, und es ist neu im Buch:** *"Every door you have gone through this year belonged to somebody who already knew what he was standing in. Byun knew. Hwang knew. Yeom knew before you sat down. That shop does not."* Und: *"it is going to start being worth something, and you will be the reason, and it is the only copy."*

  **Seine Antwort ist die Lehre aus Kapitel 30 in Handlungsform:** Original in die Hand nehmen und zurueckgeben, Kopie bezahlen, **und der Frau nicht sagen, was sie da hat** - *"The day she knows, she is a person who can be visited."*

  ---

  **Die Ladenszene ist die erste seit Kapitel 21, in der Georgij nichts drueckt, nichts tauscht und niemanden auseinandernimmt.** Er sagt einen wahren Satz und bekommt alles: *"There is a person the flowers went to, and I am trying to find out what became of them, and that is the whole of the truth about why I am standing here. I am not going to tell you the rest of it, because the rest of it is not mine to hand round a shop."*

  **Mrs Gwak, etwa siebzig, Doppelbuecher mit Durchschlag im Schrank.** Ihr eigener Verlust steht daneben und wird nicht weggeredet: dreissig Jahre Dauerauftraege, und vom Ende erfuhr der Sohn **von einem Fensterputzer.** Georgijs Antwort dazu ist der haerteste kleine Satz des Kapitels: *"That is a kinder answer than the true one." - "It is the true one. The kinder one would have been that somebody meant to ring."*

  **Was auf den beiden Durchschlaegen steht:**

  - **6. Apr.** Zwoelf Stiele, weiss, ohne Papier. Adresse in Pyeongchang-dong mit Wohnungsnummer und Stock. Kaertchen, vom Mann der Inhaberin in Bleistift mitkopiert: ***"Card: From an old friend."***
  - **27. Apr.** Dieselbe Bestellung. **Andere Adresse, ausserhalb der Stadt. Kein Kaertchen** - und der Laden fragt immer, also wurde er gefragt und hat nein gesagt.
  - **Die Bleistiftzeile des Fahrers Han auf dem zweiten Zettel:** ***"Left at the desk. They would not give a room."***
  - **Im Eckfeld beide Male derselbe Besteller: Sim.** Telefonisch, mit Nummer.

  **Und die Arithmetik, die daraus eine Person macht:** dazwischen liegt auf ihrer Zeile der Wagen vom 26. **Jemand wurde am 26. aus der Stadt gebracht, am 27. gingen die Blumen an die neue Adresse, und der Absender musste nicht gefragt werden, wohin.**

  **Die Bestaetigung kommt nicht aus einem Dokument, sondern aus einem Gedaechtnis.** Mrs Gwak hat den Anruf vier Jahre lang mit sich herumgetragen: *"It has been good to see you again."* **Zu einer Frau, mit der er nie zuvor gesprochen hatte** - genau das, was Mr Yeom in Kapitel 25 von demselben Anruferverhalten erinnert (*"He said he was glad we had met"*). **Zwei Menschen, die einander nie begegnet sind, und ein Tic.**

  **Und der Schluss ist eine Unterlassung, die etwas kostet:** er hat zwei Adressen in der Tasche und faehrt zu keiner. *"It is the plan he would have run in April."*

  **Der letzte Absatz benennt, warum ausgerechnet dieses Blatt existiert:** *"Everything else that anybody wrote down in this was written by somebody who knew it might one day be read. The only page in it with a person on it was written by a shop that had no idea it was writing anything at all."*

  **Neu im Personal:** Mrs Gwak (Laden), Min-a (Aushilfe), Mr Han (Fahrer, achtzehn Jahre, schreibt auf alles). **Und Sim**, der Besteller, der bis hierhin nur eine Handschrift im Eckfeld und ein Satz am Telefon ist.

- **Band 2, Kapitel 32** *Where the name goes* (v1.0) - **Tag 242, Di 2. Juni. Eine Szene, dieselbe Kueche vier Haltestellen draussen, bis halb zwoelf.**

  **Drei datierte Faeden laufen an einem Tisch zusammen:** das Heft kommt zurueck wie am Freitag versprochen, der Brief aus Gwangyang liegt seit Samstag da, und Annies Ansage *"in about four days"* wird faellig.

  **Er gibt das Heft zurueck, bevor er sich setzt**, und sagt den Zustand dazu: *"Nothing has been taken out of it and nothing has been added to it, and there is one copy and it is in a locked drawer in a house on the river."*

  **Mrs Jeon hat den Brief so hingelegt, dass er ihn ansehen muss.** Und sie laesst Georgij den Namen auf der ersten Seite laut sagen. **Der Text druckt ihn nicht** - Annie hat im ganzen Buch keinen Nachnamen, und das bleibt so: *"He has heard that name said out loud in a great many rooms this year ... It has never once sounded the way it sounded in that kitchen."*

  **Die harte Frage kommt sofort:** *"When did you know."* - Freitagabend, halb neun, entschieden um Viertel vor. *"And you were out here on Friday morning and you did not come back on Saturday."*

  **Seine Begruendung ist die einzige, die ihm zusteht:** *"She decided it, and it is her firm and her name on the page, and it is her money. If I had come out here on Saturday to tell you first, I would have taken a thing that belongs to her and used it to be liked by you."* Und die zweite Haelfte, die sie ihm abfordert: **"You would have read that letter on Saturday morning as a thing I did. You would have been right to."**

  ---

  **Und dann der Satz, der Annies Instrument aus Kapitel 30 auf die Probe stellt:** *"I have been handled."* - **"Yes."**

  **Sie belegt es aus dreiundzwanzig Jahren:** *"Every increase, every rota, every time a man decided something about my week and then came and told me in a way that was designed to make me feel that I had been consulted. I know the shape of it in the dark."*

  **Georgij verteidigt nicht, er beziffert:** der Eigentuemer steht im Register, der Grund steht auf der Seite und ist der wahre, die Nummer unten wird abgehoben. **Und dann gibt er den Rest zu:** *"And that is not the same as being asked." - "No. It is not the same as being asked."*

  **Ihre Bilanz der letzten sechs Wochen ist die haerteste Stelle des Kapitels:** *"In April I was rung by two civil people who would not tell me how they got my name. In May I was made redundant by a man who has never once looked me in the face. On Saturday I was handed the best thing that has happened to me in four years by a woman I have never met, and every single one of those three was decided in a room I was not in."*

  **Sie nimmt es, und sie laesst das nicht als Zustimmung durchgehen:** *"I am fifty-one ... And I would like it understood by somebody that taking it is not the same as being asked either."*

  **Und Annies Prognose trifft wortgenau ein**, was Mrs Jeon zu hoeren bekommt: *"She said you would work out inside a week that you had been made safe on purpose ... and that you would open the post on the first of the month anyway."* - **"That is a horrible thing to be right about."**

  ---

  **Der Ertrag ist die Frage, die er am Freitag nicht gestellt hat.** Nicht was die Rechnung war, sondern **wie sie aussah.**

  - **Kein Termin, sondern ein Hausbesuch.** Und die Anfahrt kostete etwa das Dreifache des Termins: *"it is the only medical invoice I have ever passed where the getting there cost more than the seeing."* Also ausserhalb der Stadt.
  - **Und im Feld fuer den Namen standen sechs Zeichen.** *"The same six that were on my clearing slip, which is the lot."*

  **Der Titel steht in ihrer Selbstanklage, und sie ist der Grund fuer den 9. Januar:** *"Somebody in a practice was given a lot number and told that it was the patient, and wrote it in the box where the name goes ... And I passed it. I looked at that box and I read six characters and I put it through and I went to lunch."* - **"That is what I went upstairs about. Not the four years. The lunch."**

  ---

  **Und die Gegenprobe zu Kapitel 29 steht im selben Zimmer:** er nimmt die Adresse **nicht**. Er laesst das Notizbuch in der Tasche, und sie ist die, die es benennt. *"You are not asking me where."*

  **Sein Grund ist ohne Schmuck:** *"you are going to be inside a firm that belongs to her by the middle of the month, and the less of this that is in you, the better that is for you ... I do not need the rest of it from you and I am not going to take it because it is available."*

  **Und als sie den Widerspruch aufmacht** (*"On Friday you gave me a thing that could take her apart, and today you will not let me give you an address"*), erklaert er ihn nicht weg: **"On Friday I had nothing else to pay you with. Today I have. That is the only thing that changed and I am not going to dress it up as a principle."**

  ---

  **Hwangs Bitte aus Kapitel 28 wird nicht erledigt, sondern weitergereicht**, und das ist die Lehre des Kapitels in Handlungsform: *"I want to give you the question instead of deciding it, because he asked me to arrange a thing about you without asking you."*

  **Ihre Entscheidung ist besser als jede, die er getroffen haette:** *"Then it will exist and I will write it, and he does not get to have it."* Eine Seite, unterschrieben, mit Datum - **und sie geht an Georgij**, *"because a thing like that is worth nothing in the hand of the man it is about."* Mit Auflage: *"You will keep it and you will not use it, and if you ever do use it you will find that I am extremely difficult."*

  **Der Satz an der Tuer ist der Beweis, dass sie die Terms wirklich gelesen hat**, und es ist zugleich das Erste, was sie fuer Annie mitgibt: *"Tell her that I read all four pages of the terms and that the third one is generous in a way that somebody thought about. And tell her that I noticed it was posted on Friday night."*

  **Und daran haengt der Schluss.** Freitagnacht heisst: **Annie hat den Brief geschrieben, unterschrieben und aus dem Haus gehabt, waehrend er auf dem Boden neben ihrem Schreibtisch schlief.** *"Eleven minutes, she had said, and about four days. It is the fourth day."* - **"He has not been punished. He has been shown."**

  **Bewusster Widerhall:** *"You are a very strange young man"* steht gegen Mr Byuns *"Then you are a very cruel young man"* aus Kapitel 22. Zwei Urteile ueber denselben Mann aus zwei Zimmern, und das Buch faellt keines davon selbst.

- **Band 2, Kapitel 33** *A door with no name on it* (v1.0) - **Tag 243, Mi 3. Juni. Eine Szene, der Schreibtisch am Morgen.**

  **Georgij bricht sein eigenes Muster:** zum ersten Mal seit Januar (in Wahrheit seit dem 20. Maerz, als er die vierte Zeile zum ersten Mal ausspricht) legt er eine laufende Ermittlung offen, bevor sie ihn etwas kostet, statt danach. *"Since the flower shop, the only money that has gone into this is what you already handed me yourself, and I have not used your name once. I only noticed this morning that both of those were decisions, and I had not told you I was making them."* **Korrigiert am 24.08.:** die erste Fassung liess ihn behaupten, er habe "not spent a won" - falsch, Annie hatte ihm das Bargeld fuer den Blumenladen selbst gegeben (Kapitel 31).

  **Annie liest die Beweislage und liefert die Einordnung, die Georgij fehlt** - sie kennt die Sorte Adresse aus ihrem eigenen Geschaeft: *"A ward. A facility that takes people nobody wants found. Or a house that has been told to say no by somebody who pays its bills and does not live there."* Und die dritte ist die gefaehrliche, weil sie **nicht die Person darin schuetzt**, sondern denjenigen, der fuer das Schweigen zahlt.

  **Der Grund, warum er nicht hingefahren ist, ist zum ersten Mal nicht Vorsicht, sondern eine echte Neubewertung:** *"I do not know who is paying for the desk that says no, and every other man in this has been somebody I could stand in a room with and outlast ... I have been walking into empty buildings and cold flats all year and calling it work."*

  **Und der Satz, der die Szene traegt:** *"I brought it to you because if it goes wrong, it does not go wrong to me alone. It goes wrong to whoever I work for, in whatever room I am standing in when it happens."* **Annie: "That is the first time you have said that sentence in this house."**

  **Ihre Antwort ist keine Erlaubnis, sondern eine Bedingung, formuliert genau nach der Lehre aus Kapitel 30:** *"You do not go near either address without telling me first. Not asking. Telling."* Und sie setzt Jang auf die zweite Adresse, **von aussen, bevor sein Name irgendwo faellt.**

  **Drei offene Faeden werden im selben Gespraech genannt und bewusst nicht geschlossen:** Hwangs Bitte um Anerkennung fuer Mrs Jeon (das Blatt liegt ungelesen bei Georgij), und Sang-hoons vier unerklaerte Entscheidungen, die seit April liegen geblieben sind, weil die vierte-Zeile-Sache die Zeit gefressen hat. *"Then say that to him before he says it to you." - "I intend to."*

  **Neu im Personal, nur benannt:** ein Angestellter namens **Jang**, Sicherheitschef, wird zum ersten Mal in Band 2 mit einer eigenen Aufgabe betraut, ausserhalb von Georgijs Blick.

- **Band 2, Kapitel 34** *The best company in the room* (v1.0) - **Tag 244, Do 4. Juni. Nacht bis halb sieben morgens, der Schreibtisch.**

  **Korrigiert am 24.08.** Die erste Fassung liess Georgij den Namen Choi Dae-ho in dieser Nacht zum ersten Mal herleiten und Annie davon ueberrascht sein - **das widersprach Kapitel 27 direkt**, wo Sang-hoon ihm den Namen bereits am 27. Mai gegeben hat und Annie ihn seit ihrem vierzehnten Jahr kennt. Die Fassung unten ist die korrigierte.

  Er liest das Notizbuch von vorn und legt zwei Eintraege nebeneinander: Herrn Yeoms *"glad we had met"* (Kapitel 25/31) gegen Sang-hoons Auskunft aus Kapitel 26, *"He tells people he is glad they have finally met. The first time. When they have never met."* **Nicht die Identitaet ist die Entdeckung dieser Nacht - die kennt er seit Mai -, sondern dass zwei Fremde, die nie voneinander gehoert haben, unabhaengig denselben Satz bezeugen.** *"Now it does not need her to have been right alone."*

  **Die Probe, bevor er es fuer belastbar haelt:** *"A habit shared by two different men is a coincidence. A habit that specific, said in that exact shape, twice, four years apart ... is not a coincidence twice."*

  **Er bringt es zu Annie und benennt genau, was neu ist:** *"It is him. I have known that since the twenty-seventh of May, the same as you. What I have this morning that I did not have then is two people who have never heard of each other saying the same six words in the same shape."* Annie: **"That is not nothing."** Sie hat es seit ihrem vierzehnten Jahr getragen, ohne es je einem anderen Menschen zur Nachpruefung geben zu koennen - jetzt kann sie.

  **Annies Reaktion ist keine Bestaetigung des Namens, sondern eine Risikoabschaetzung, und sie zieht die Konsequenz sofort:** *"Then the florist is not safe either."* Georgij hatte das noch nicht bedacht - jeder, der ihm in den letzten anderthalb Wochen geholfen hat, ist jetzt ein Name, den ein gefaehrlicher Mann erreichen koennte, falls je bekannt wird, wer gefragt hat.

  **Ihr Befehl ist eine Vier-Tage-Pause fuer alle**, Jang eingeschlossen. **Sang-hoon erfaehrt nicht, dass eine Blumenverkaeuferin und eine Adresse jetzt in der Sache stehen** - den Mann hat er, den Rest noch nicht. Annies Begruendung: *"If you hand him a florist and an address he cannot yet protect ... he will act on it. That is not something either of you can take back."*

  **Und der Moment, an dem Georgij zum ersten Mal in elf Wochen (seit dem 20. Maerz, nicht mit Datum benannt, aber die Rechnung stimmt) stillhalten muss, statt selbst zu entscheiden, wann er einen Raum betritt** - er nennt es nicht Kraenkung, aber er muss sich zwingen, es nicht als eine zu hoeren.

  **Mrs Seo, zweimal in diesem Buch: Kaffee ohne Nachfrage, wenn jemand nicht ins Bett gegangen ist.** *"It is easier to run a house for people who do not tell me things than for people who tell me half of them."* Keine neue Figur, aber die erste eigene Zeile seit langem.

  **Der Schluss zaehlt die Leute auf, die ohne es zu wissen jetzt zur Bestaetigung einer Kindheitserinnerung geworden sind:** die Aushilfe, der Mann, der die Kaertchen kopiert hat, der Fahrer, der auf jeden Zettel geschrieben hat. **Und die letzte Zeile im Notizbuch ist fuer die Blumenverkaeuferin gedacht und nicht fuer Annie**, was ihm erst auffaellt, als er sie schon geschrieben hat: *"Four days. Not hers to lose either."*

- **Band 2, Kapitel 35** *Everything I am allowed to say* (v1.0) - **Tag 245, Fr 5. Juni. Ein Telefonat, ein Korridor, der Garagengang am Abend.**

  **Sang-hoon bricht sein eigenes Muster** (*"Sang-hoon does not telephone"*) und fragt direkt nach dem Kapitel-26-Auftrag. Die Szene ist eine Probe auf Regel 1 unter Zeitdruck: Georgij darf schweigen, weglassen, nicht aber luegen.

  **Die Frage, die ihn zwingt, ist die kleinste:** *"Whose four days."* Er antwortet **nicht** mit einer falschen Zuordnung, sondern haelt inne und gibt die einzige wahre Teilantwort, die in der Zeit verfuegbar ist: *"Not entirely mine."*

  **Sang-hoon nennt das den Preis und respektiert ihn trotzdem:** *"That is a very expensive way to talk to a man who has just given you a name for nothing."* Und akzeptiert die Frist: **"Tuesday. Not before."**

  **Der zweite Teil der Szene spiegelt den ersten, ohne dass die Figuren es wissen.** Jang, abgezogen von der zweiten Adresse, stellt Georgij fast wortgleich dieselbe Frage: *"Whether the person you got it from is the sort who wastes four days, or the sort who spends them."* **Georgij antwortet mit einem Urteil, das er sich selbst erst beim Aussprechen bestaetigt:** *"She spends them. I have watched her do it since October."*

  **Annie schliesst die Szene, indem sie die Frage zurueckgibt, statt sie zu beantworten:** *"Ask me something you do not already know the answer to, and I will tell you whether I am wasting anything."* Und zeigt den ersten Ertrag: **elf Namen am Abend des ersten Tages, dreissig bis Sonntag geplant**, keiner der Befragten weiss, dass gefragt wird.

  **Kein Fortschritt im Choi-Dae-ho-Faden selbst** - das Kapitel haelt die Vier-Tage-Frist bewusst offen und zeigt stattdessen, was das Halten kostet: eine Luege, die nicht gesagt wird, ein Sicherheitschef, der ohne Erklaerung vertraut, und ein Mann, der zum ersten Mal seit acht Monaten nicht selbst entscheidet, wann eine Tuer sich oeffnet.

- **Band 2, Kapitel 36** *Not the man, the four* (v1.0) - **Tag 249, Di 9. Juni. Zwei Szenen: die Bibliothek am Montagabend, ein Privatraum ueber einem Restaurant am Dienstag im Regen.**

  **Annies drei Ergebnisse, wortgenau gehalten:**
  1. **Einunddreissig Namen bis Sonntag, elf davon mit unerklaerten Wendepunkten.** Georgij bekommt keinen davon - Annie haelt acht lebende Betroffene bewusst zurueck: *"I am not going to hand you eight more people to feel responsible for on top of the ones you already have."*
  2. **Ein Immobilienbesitz in Gangwon-do, vier Eigentuemer tief**, der ein namenloses Pflegeheim ausserhalb Wonjus finanziert. Noch nicht bestaetigt als die zweite Blumenadresse, aber vom Typ her passend.
  3. **Einmal, vor elf Jahren, hat ihn jemand verlieren sehen.** Ein Zimmer, eine Hochzeit, die nicht stattfand, vier Jahre Auslandsaufenthalt danach, zwei unabhaengige Zeugen, die das Wort *"unrecognisable"* benutzen. **Kein Name. Zwei Gespraechspartner brachen ab, als sie ein zweites Mal gefragt wurden.**

  **Korrigiert am 24.08.** Die erste Fassung liess Georgij "I believe it is Choi Dae-ho" zu Sang-hoon sagen, als sei der Name neu - **das widersprach Kapitel 26 direkt, wo Sang-hoon ihm genau diesen Namen selbst gegeben hat.** Die Fassung unten laesst Georgij stattdessen das liefern, was tatsaechlich neu ist: Beweismaterial, das ausserhalb dieses Hauses steht.

  **Das Dienstagstreffen ist die erste offene Kommunikation seit Kapitel 26, und Georgij liefert bewusst nur die Haelfte des Geschuldeten:** *"I have something on him now that is not only your word and mine, and it did not exist a week ago ... I do not have the four decisions ... it is not what you told me to bring you."* **Er nennt das nicht Erfolg, sondern die ehrliche Haelfte:** *"I would rather hand you an honest half than a whole thing I have padded to look finished."*

  **Die Wendung, die das Kapitel traegt: Sang-hoon wusste es schon.** Er hat seit Samstag unabhaengig dieselbe Grundstuecksakte in Gangwon-do verfolgt, aus einem eigenen Verdacht, und wartete ab, ob Georgij es selbst sagen wuerde: *"I did not say it first because I wanted to hear whether you would."* **Zum ersten Mal seit Beginn dieses Fadens ziehen die beiden Ermittlungen aus verschiedenen Richtungen an derselben Tuer.**

  **Und Sang-hoon liefert am Schluss einen neuen, ungeoeffneten Faden:** in acht Jahren Tischgesellschaft hat Choi Dae-ho kein einziges Mal eine Frau erwaehnt - *"the one subject he has never once brought up."* Georgijs Notizbucheintrag haelt es fest, ohne zu deuten: *"Eight years. Never once a woman. Find out why not."*

  **Ausdruecklich nicht geloest in diesem Kapitel:** wer die vier Entscheidungen betrifft, wer im Pflegeheim ist, wer Choi Dae-ho vor elf Jahren verloren hat gesehen. **Drei offene Fragen bleiben offen, mit Absicht.**

- **Band 2, Kapitel 37** *A piece of paper somewhere in the world* (v1.0) - **Tag 255, Mo 15. Juni. Der Schreibtisch, der Post, das kleine Zimmer.**

  **Mrs Jeons erster Tag bei Gwangyang, und sie beginnt ihn, indem sie eine fremde Schuld begleicht statt der eigenen Arbeit.** Der Brief, den sie Hwang in Kapitel 32 versprochen hat, kommt mit Gwangyang-Poststempel am selben Morgen: *"He was correct about the desk. He was wrong about the book. I am writing this so that somewhere it says which was which."*

  **Georgij gibt das Blatt nicht an Hwang weiter, und die Begruendung ist die Lehre des ganzen Fadens:** *"He asked for this because he wanted to be forgiven for something, and if I hand it to him, I am the one deciding that he has earned it, and that is not mine to decide."* Annie prueft die Antwort wie eine Zahl, die sie zum dritten Mal nachrechnet, nicht aus Zweifel, sondern aus Gewohnheit - und sie haelt.

  **Annie liefert im Gegenzug, ungefragt, wie ihr erster Tag lief:** binnen anderthalb Stunden findet Mrs Jeon vier Dinge in einem Aktenschrank, die der Neffe drei Jahre lang nicht bemerkt hat. **"She was always going to be very good at this. The only thing that was ever in question was whether anybody would let her be."**

  **Und dann schickt Annie ihn weg von genau diesem Thema** - *"Go and do something today that is not this"* - und er nutzt den freien Vormittag fuer die andere liegen gebliebene Schuld: **Sang-hoons vier Entscheidungen**, seit dem Regentag in Kapitel 36 nicht mehr angefasst. Vier Initialen aus Sang-hoons eigenem Kalender - S, H, K, Y - mit Uhrzeiten und Stimmungen statt Namen, und die Einsicht, dass ein Buchstabe kein Hinweis ist, sondern nur der Schatten von einem.

  **Kein Name faellt in diesem Kapitel.** Annie liest am Abend die vier Zeilen und waehlt eine andere zuerst als Georgij - **welche, bleibt offen fuer das naechste Kapitel, das den Faden aufnimmt.**

- **Band 2, Kapitel 38** *The one with two parts* (v1.0) - **Tag 257, Mi 17. Juni. Ein Telefonat, dann der Garten am Nachmittag.**

  **Annie waehlt "Y" zuerst, mit Begruendung:** *"Eleven months is close enough that people still remember what they wore. Four years is a story by now."* Georgij haette mit der aeltesten Initiale angefangen, weil sie naeher an Los sechs liegt - **sie laesst die Meinungsverschiedenheit stehen, ohne sie zu kommentieren.**

  **Sang-hoon nennt einen Namen, bevor Georgij fragen muss: Yeom.** Derselbe Mann, der in Kapitel 25 den anonymen Anruf bekam - *"glad we had met"*, an einen Fremden gerichtet. **Und Georgij faengt den Fehler in Echtzeit ab, bevor er ihn Sang-hoon als fertige Antwort gibt:** Yeom steht am Ende dieses Satzes, nicht am Anfang. Wer angerufen wurde, kann nicht im selben Atemzug der Anrufer bei Sang-hoons Kartenabend sein, ohne dass das Buch das ausdruecklich behauptet - und das behauptet es nicht.

  **Die Regel, die er sich selbst vorspricht, ist die aus Kapitel 37, jetzt gegen die eigene Zuneigung gewendet:** *"A shared initial is not a lead. It is the shadow of one."* Sang-hoon haelt dagegen - vielleicht hat der Anruf vor vier Jahren aus einem Opfer einen Mitwisser gemacht -, und Georgij laesst die Moeglichkeit stehen, ohne sie zu entscheiden.

  **Im Garten gibt Annie dem Nachmittag seine schaerfste Wendung:** nicht die Logik ist das Risiko, sondern dass er Yeom mag. *"Liking a man does not clear him. It only makes it more expensive if he is not clear."* **Erstmals seit Bandbeginn benennt der Text, dass Georgij jemanden in diesem Geschaeft gemocht hat und nicht nur respektiert** - eine Unterscheidung, die er selbst zieht und die ihn ueberrascht.

  **Ergebnis des Kapitels: eine Methode, kein Name.** Yeom ist vorlaeufig entlastet, nicht bewiesen unschuldig - die Restaurant-Buchpruefung folgt. Sang-hoon bekommt die korrigierte statt der ordentlichen Antwort, **und Georgij nennt es selbst: "the same answer, corrected."**

- **Band 2, Kapitel 39** *A room that is somebody else's now* (v1.0) - **Tag 259, Fr 19. Juni. Zwei Kuechen, ein Gespraech in der Bibliothek am Abend.**

  **Die Restaurant-Buchpruefung aus Kapitel 38, und sie foerdert mehr zutage als sie sollte.** Vier Lokale bei Sinsa haben seit letztem Juli den Besitzer gewechselt. Das gesuchte gehoert jetzt einer Frau, die vom Vorbesitzer Mr Baek nichts hat ausser einer kaputten Kaffeemaschine - **und die im April bereits einmal danach gefragt wurde**, von einem Mann, der abzog, sobald die Spur in einem Buero statt in einer Kueche endete.

  **Ein Aufraeumer, der sein eigenes Werk ein zweites Mal prueft, ist kein aengstlicher Mann.** *"He checks once, and he checks early, and he does not come back unless he has a reason to think somebody else might be looking."*

  **Baek selbst bestaetigt das Wesentliche: zwei Maenner, kein Dritter - Yeom vollstaendig entlastet**, diesmal nicht vorlaeufig wie am Mittwoch. Und eine neue, praezise Probe: *"Did he eat."* **Der Kartenvorschlaeger hat gegessen, langsam, mit Kompliment an die Kueche - also nicht Choi Dae-ho selbst**, dessen Tick seit Kapitel 26 das genaue Gegenteil ist. Es gibt mindestens eine weitere Person in diesem Geflecht, die noch keinen Namen hat.

  **Der Abend in der Bibliothek zieht die schwerste Vermutung des Fadens bisher, und Annie haelt sie ausdruecklich fuer unbewiesen:** ein Mann, der im April eine Kueche zweimal pruefen laesst, ueberlaesst eine so grosse Sache nicht dem Zufall - **entweder er hat Sang-hoon nicht kommen sehen, was zu nichts sonst passt, oder er hat es kommen sehen und geschehen lassen**, weil ein langsames Lecken durch einen Mann, ueber den er acht Jahre Hebel haelt, ihn weniger kostet als ein Fremder, der ihn kalt erwischt. *"He let Sang-hoon find out on purpose."* **Keine Bestaetigung, nur die erste Aussprache eines Verdachts, den beide schon getragen haben.**

- **Band 2, Kapitel 40** *What the road knows* (v1.0) - **Tag 261, So 21. Juni. Das Zimmer neben der Bibliothek, der ganze Vormittag.**

  **Jangs Bericht nach sechzehn Beobachtungstagen, und Annie gibt ihm dafuer den ganzen Vormittag - ungewoehnlich fuer einen Bericht, den man im Stehen abliefern koennte.** Er hat das Grundstueck nicht betreten: *"I have not been onto the property. I have not spoken to anybody who works there ... I do not go past a line I have not been given."*

  **Was er hat, ist ein Fahrplan statt eines Namens:** vier Autos morgens und abends (Rota, nicht Familie), ein Auto nur mittwochs ueber Nacht, Waeschelieferung dienstags, Lebensmittel freitags fuer sechs bis zehn Personen. **Und einen alten Mann an der Bushaltestelle**, der seit Jahren, ohne es zu wissen, eine Frau am Fenster im zweiten Stock beobachtet - jeden Nachmittag zur selben Zeit, nie draussen, nie Besuch. Licht in elf von sechzehn Naechten, immer aus bis zehn.

  **Jangs dritte Vermutung ist die, die er "nicht seine, in diesem Raum zu sagen" nennt und trotzdem sagt:** eine Frau, die zu einer festen Stunde ans Fenster tritt, ist nicht ans Bett gefesselt, sondern ans Gebaeude - **und der Unterschied bedeutet, dass jemand entschieden hat, was fuer ein Leben ihr noch erlaubt sein soll, statt es zu beenden.** Mit zweiundzwanzig Jahren im Fach und einer eigenen Skala dahinter: *"Above the middle of it. Not anywhere near the top."*

  **Annie zieht die Grenze, bevor Georgij sie ueberschreiten kann, und sagt es laut, damit er sie von ihr und nicht erst von sich selbst hoert:** der naechste Schritt ist keine Strasse mehr, sondern ein Grundbucheintrag - **Sang-hoons Weg, nicht ihrer.** Und sie erinnert sich ausdruecklich an den Preis der letzten Vier-Tage-Frist, um keinen neuen Termin zu erfinden, den sie nicht halten kann.

  **Der Schluss gehoert Jang, nicht Georgij:** *"The light was on when I left this morning. She was awake before six."* Kein Kommentar, keine Deutung - nur die eine Tatsache, die ohne Vermutung auskommt.

- **Band 2, Kapitel 41** *The travelling cost more than the seeing* (v1.0) - **Tag 263, Di 23. Juni. Das kleine Zimmer, ein ganzer Tag am Schreibtisch.**

  **Der Arzt-Faden aus Kapitel 30/32, endlich aufgenommen - und ganz ohne eine einzige Tuer.** Georgij nutzt das erzwungene Stillhalten fuer genau die Ermittlung, die keine Adresse braucht: Hausbesuch-Praxen sind oeffentlich lizenziert, und eine Rechnung, deren Anfahrt dreimal so teuer war wie der Termin selbst, ist keine Stadtrechnung.

  **Die Filterkette, sauber nachvollziehbar:** elf Praxen landesweit vor vier Jahren registriert. Sechs sofort raus (Paediatrie, geschlossen, zu weit weg). Eine Klinikgruppe raus, weil eine Rechnung dieser Groesse eine interne Revision nicht vier Jahre lang ueberlebt. Zwei per Telefon bestaetigt als gewoehnliches, ehrliches Geschaeft - **und Georgij fragt wahrheitsgemaess, ohne zu sagen warum, nie mit einer erfundenen Begruendung** (eine fruehe Fassung hatte ihn hier luegen lassen, was Regel 1 gebrochen haette - korrigiert).

  **Bleiben zwei. Einer wird ueber die Aerztekammer geprueft und faellt heraus**, weil seine beiden Buergen ihn all die Jahre aus naechster Naehe kannten - ein Mann, der wirklich zwanzig Jahre lang gewoehnliche Hausbesuche gemacht hat. **Der andere hat eine erloschene statt geschlossene Zulassung** - ein Unterschied, den Georgij selbst benennt: *"A practice that was allowed to disappear rather than told to."*

  **Dr. Oh Seung-min.** Vierundfuenfzig beim Hausbesuch vor vier Jahren, jetzt achtundfuenfzig, falls die Zulassung ihm je gehoert hat. Die registrierte Adresse in Jung-gu ist seit anderthalb Jahren eine Zahnarztpraxis - **Georgij faehrt nicht hin, weil das Nichthinfahren die eine Regel war, die er diese Woche nicht brechen wollte.**

  **Annie nimmt den Namen entgegen und sperrt ihn sofort weg** - nicht Sang-hoon, nicht Jang, nicht einmal ein zweiter Notizbucheintrag. *"Everything on paper is eventually read by somebody it was not written for."* Der naechste Schritt haengt jetzt allein daran, ob Sang-hoons Grundbuchrecherche dieselben vier Eigentuemer hinter der erloschenen Zulassung findet wie hinter dem Pflegeheim bei Wonju.

- **Band 2, Kapitel 42** *Four owners deep* (v1.0) - **Tag 270, Di 30. Juni. Ein Restaurant, ein Tisch statt eines Privatraums.**

  **Sang-hoon liefert das Ergebnis, das der ganze Faden seit Kapitel 33 gebraucht hat.** Vier Eigentuemer sind vier Firmen, drei davon reine Huellen ohne eigenes Geschaeft. **Die vierte ist ein Trust** - und ein Trust muss niemanden nennen, der davon profitiert, nur wer ihn verwaltet: Solicitor **Baek Jun-ho**, Yeouido, seit elf Jahren, ausdruecklich nicht der Koch aus Kapitel 39 (Sang-hoon hat es selbst geprueft, bevor er den Namen brachte - dieselbe Vorsicht, die Georgij sich seit Kapitel 37 selbst auferlegt hat).

  **Der Trust wurde vor elf Jahren gegruendet.** Georgij braucht keine Erklaerung, was ihm das bedeutet - Annie hat mit vierzehn genau das bemerkt, das sie erst mit dreissig verstand (Kapitel 27). **Und derselbe Trust steht hinter der erloschenen Arztzulassung aus Kapitel 41** - einmal gebaut, zweimal benutzt, weil der Erbauer sich sicher genug war, dass niemand je nachpruefen wuerde.

  **Zwei Daten, die sich nicht zusammenlegen lassen, und Georgij haelt sich bewusst zurueck, keins davon vorschnell zu waehlen:** elf Jahre fuer das Gebaeude, vier fuer den Arzt. Dann bringt er selbst eine dritte, duesterere Lesart ins Spiel - **nicht zwei Gruende, sondern einer, der nach elf Jahren zum ersten Mal versagt hat und einen Arzt brauchte, weil die Alternative schlimmer gewesen waere.** *"That would make the doctor not the start of it, but the first time it went wrong."*

  **Sang-hoon gibt die Aufgabe zurueck, praeziser als Georgij sie sich selbst gestellt hatte:** nicht ob die Frau noch lebt, sondern **ob die Frau, die Jang beobachtet hat, ueberhaupt dieselbe ist, fuer die der Trust vor elf Jahren gebaut wurde.** Zwei verschiedene Fragen, und Georgij gibt zu, dass er sie bislang wie eine behandelt hat.

---

- **Band 2, Kapitel 43** *Six weeks before* (v1.0) - **Tag 273, Fr 3. Juli. Zwei Szenen: das kleine Zimmer am Vormittag, dann dasselbe Restaurant wie Kapitel 42.**

  **Georgij loest die eigene, aeltere Schuld ein: Sang-hoons vier Entscheidungen, zugesagt in Kapitel 26.** Y ist seit Kapitel 39 erledigt (Yeom). Aus dem Restaurant-Reservierungsbuch und Byuns Zettel bekommt er jetzt zwei Daten mehr, ohne Namen: **S. 8pm, Maerz, vor vier Jahren** - derselbe Fruehling wie die Auktion mit Los sechs. **H. 7:30, Oktober, drei Jahre nach S** - also gut neun Monate vor der aktuellen Kapitelzeit, **sechs Wochen bevor Hwang ins Haus kam.** K bleibt vollstaendig offen: nichts im Reservierungsbuch in vier Jahren, keine dritte Initiale.

  **Sang-hoon bestaetigt S sofort** - er kannte das Datum bereits. **H trifft ihn anders:** die Sechs-Wochen-Distanz zu Hwangs Ankunft war ihm nie aufgefallen. Er gibt die Sache hinter der Oktober-Entscheidung zu - eine Schiffsladung ueber seinen eigenen Namen bewegt, ohne Rechnung, ohne Nachfrage - und erkennt, dass es **die letzte kleine Entscheidung war, bevor Choi einen Fremden brauchte, um das Haus sauber zu halten.** Namen bekommt weder S noch H in diesem Kapitel, nur Daten und die Art der Entscheidung bei H.

  **Annie liefert die Richtung fuer K:** kein Tisch, keine Rechnung - ein Golfplatz, ein privates Badehaus, irgendein Ort, an dem ein Treffen wie Freizeit aussieht und deshalb keine Quittung braucht. Dazu eine neue Einzelheit ueber ihren Vater: **er hat zweimal im Monat auf einem Golfplatz Geschaefte gemacht und es Sport genannt**, niemand hat je aufgeschrieben, was dort entschieden wurde.

  *Korrekturhinweis 24.08.: Die erste Fassung hatte H versehentlich als "zwei Jahre nach S" und an einer Stelle als "vor drei Jahren" datiert - beides widersprach der Tatsache, dass Hwang laut Kapitel 21 erst seit Mai bekannt und (fuenf Monate zurueckgerechnet) im Dezember desselben jetzt laufenden Zeitraums ins Haus kam. Korrigiert auf "drei Jahre nach S" (ergibt Oktober, knapp ein Jahr vor der aktuellen Kapitelzeit), passend zu den sechs Wochen vor Hwangs Ankunft.*

---

- **Band 2, Kapitel 44** *A van that comes every ten days* (v1.0) - **Tag 276, Mo 6. Juli. Zwei Szenen: das kleine Zimmer am Tag, dann der Abend mit Annie.**

  **Georgij nimmt sich Sang-hoons Aufgabe aus Kapitel 42 vor - nicht ob die Frau lebt, sondern ob sie dieselbe ist.** Statt an ein Tor zu gehen, sucht er nach dem, was ein Haus mit einer medizinischen Notwendigkeit anmelden muss: **eine Brandschutz-Meldung fuer medizinischen Sauerstoff.** Die Adresse aus Sang-hoons Grundbuchrecherche taucht in der Meldeliste **genau einmal auf, im Juli vor vier Jahren** - weder frueher noch spaeter storniert.

  **Jang bestaetigt es von aussen, ohne dass Georgij ihm sagt, was er sucht:** ein grauer Lieferwagen einer Gasfirma, seit drei Wochen beobachtet, ausschliesslich an dieser Adresse, **ohne festen Rhythmus** - Jangs eigene Deutung: bestellt, wenn ein Tank zur Neige geht, nicht auf Route. **Zwei Dokumente, die einander nie kannten, stimmen ueberein.**

  **Annie bremst die Schlussfolgerung, bevor Georgij sie zu weit treibt:** die Ausruestung beweise, dass etwas geschah, nicht fuer wen. *"You have built a true thing out of two facts before, and you have also built a wrong one, and the difference between them was never how confident you felt while you were doing it."* Sie stimmt aber der zweiten Lesart zu, die Jangs Detail liefert - **jemand beobachtet den Tank taeglich genug, um den Anruf rechtzeitig zu machen, und das ist keine Einrichtung, die einen Dienstplan fuehrt, sondern eine Person, die sich kuemmert.**

  **K bleibt vollstaendig offen, jetzt mit einem ausgeschlossenen Ansatz:** Golfclub-Mitgliederlisten sind fuer Nicht-Mitglieder nicht zugaenglich, und Georgij lehnt es ab, fuer eine Namensliste beizutreten. **Faellig: ein anderes Dokument fuer K, und wer bei der Frau in Wonju taeglich nach dem Tank sieht - ueber die Gasfirma, nicht ueber das Tor.**

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
