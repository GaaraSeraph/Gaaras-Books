# Naechste Schritte und offene Faeden

Die kleinste Datei und die wichtigste. In jeder Sitzung zuerst und zuletzt lesen.

---

## Reihenfolge ab hier

Was als Naechstes drankommt und in welcher Ordnung. Erledigtes wird gestrichen,
nicht abgehakt.

**Erledigt:** Kangs Anruf. Das Abendessen mit Sang-hoon und der Hanseong-Bericht. Do-yun als Mann von innen, benannt und begründet. **Die Heimfahrt nach Sang-hoon**, geschrieben als Kapitel 17 (v12.1, Tag 46, derselbe Abend wie Kapitel 16). Sie endet nicht auf "I enjoy this": darauf folgt *He had meant to stop there.* und das Geständnis über das Wort *Mistress*, und danach gibt Annie im Korridor die elf Häuser zurück. Der Wortlaut in `doc/05-continuity.md` unter "Festgelegte Zeile" reicht nur bis "I enjoy this." und beschreibt den ersten Teil.

**Als Nächstes, in dieser Reihenfolge:**

1. **Tag 45 nachreichen.** Unterschrift und zweite Abteilung, siehe oben.
2. **Der Bericht kommt zurück.** Sang-hoon hat "You'll get it back on Thursday" gesagt. Das ist Tag 48, Donnerstag der 20. November. Ein datiertes Versprechen, das jemand einlösen muss.
3. **Das Gespräch mit den Kims** und der Satz über den Namen und die Kontrolle, aus Georgijs Mund und nicht aus ihrem. Ye-rin nur über Hana, einmal und nicht schnell.
4. **Woo an die Seite der Kims holen.** Das ist die teure Bitte, und die vier Minuten dafür liegen seit Tag 28 bereit.
5. **Der Apfelsatz.** Erst wenn Sang-hoon Hanseong tatsächlich gekauft hat, nicht vorher.
6. **Die Zollakte und der Container.** Als Zeile in einer Akte, nie als Szene.
7. **Choi Dae-ho**, den Georgijs Verfahren nicht finden kann.
8. **Los elf und der Name sind derselbe Gang.** Kein offener Faden, sondern eine laufende Vorenthaltung, und die zwei Hälften gehören zusammen. Annie hat den Jungen gekauft, und sie hat bei derselben Gelegenheit den Namen des Garanten geholt, weil Georgij ihr am ersten Abend gesagt hat, dass das Fenster drei Wochen offen steht, und sie verschwendet nichts. Das ist Kanon in `doc/04-world.md` unter "Die Pipeline".

    Was der Text davon zeigt: ein Katalog ohne den Jungen und das Wort "No" (Kapitel 6). Neunzehn Tage in ihrem Besitz und trotzdem kein Name (Kapitel 12). Ihre Begründung, dass es ändert, worum sie ihn bitten muss (Kapitel 11). Und Kapitel 15 sagt in einem Nebensatz, dass sie den Namen seit seiner ersten Woche im Haus hat.

    **Der Leser weiß also seit Kapitel 12, dass sie etwas hält**, und weiß seit Kapitel 6, dass ein Junge aus einem Katalog verschwunden ist. Was er nicht hat, ist die Verbindung: dass beides an einem Abend beschafft wurde und dass der Kauf keine Gnade war. Wenn das aufgeht, gehen beide Hälften zusammen auf, und die Erleichterung darüber, dass der Junge nicht verkauft wurde, muss im selben Satz kassiert werden.
9. **Die Pipeline.** Kanon in `doc/04-world.md`, im Text noch nicht ausgesprochen, und wenn sie ausgesprochen wird, darf sie keine Erleichterung sein.

Erst danach die Blöcke F bis J, und zwar mit Abstand. Der Bruch trägt nur, wenn zwischen Kapitel 16 und ihm noch Arbeit liegt, an der die beiden nebeneinander gut sind.

---

---

## Offene Faeden

Was unaufgeloest ist und irgendwann bezahlt werden muss. Wer einen Faden
schliesst, streicht ihn hier und vermerkt in welchem Kapitel.

- **Los elf.** Ein Junge, laut Akte sechzehn, tatsächlich höchstens vierzehn. Der Käufer wurde ruiniert und holt ihn nicht ab. Achtzig heute, sechzig nächsten Monat, und bei sechzig fragt das Haus nicht mehr, wer kauft, weil die Marge das Fragen nicht deckt.
- **Was Annie für sechzig bekäme** (Georgijs Argument im Wagen, unbeantwortet geblieben): Erstens einen Namen. Das Haus kann ein zurückgegebenes Los nicht neu listen, ohne die Rückgabe zu erklären, und es gibt nur eine wahre Erklärung. Wer den Mann in der zweiten Reihe garantiert hat, hat Geld und kein Gesicht und kauft nicht einen einzelnen Jungen für sich. Zweitens, und länger haltbar, das Haus selbst: Wer weiß, dass ihr Buch schmutzig ist, bekommt jeden Katalog, wird nicht überboten und erreicht sie um elf Uhr abends. Der Name ist im Frühjahr alt, das andere trägt Jahre. Und es gilt nur heute Nacht, weil sie in drei Wochen eine gemeinsame Version haben werden.
- **Was er dabei preisgegeben hat.** Auf ihre direkte Frage nennt er den wahren Grund ohne Umweg: "Because he's fourteen." Und er sagt dazu, dass sie ohnehin herausgefunden hätte, womit er sich kaufen lässt, also lieber heute und lieber billig. Sie hat den Hebel jetzt.
- **Der Abend in drei Wochen.** Annie hat ihn in der Auffahrt angekündigt: Dort will sie die andere Hälfte und sonst nichts. Das ist die Gala.

---

### Bekannte Baustellen, Stand nach Kapitel 17

- **Bandwurmsaetze: erledigt, alle siebzehn auf null.** Der Eintrag stand hier
  noch auf sechzehn in Kapitel 7, zwoelf in Kapitel 13 und je elf in 4, 6, 8 und
  9. Nachgezaehlt am 22.08. mit derselben Regel, die `check.py` anwendet
  (Trennung auf `(?<=[.!?"])\s+`, Schwelle vierzig): **null in jedem Kapitel.**
  Der Rest der Basislinie ist kein Satzlaengenbestand, sondern drei
  Zahl-Konstanten - eine in Kapitel 6, zwei in Kapitel 12.

  **Wobei ein groesseres Loch auffiel, und das war der eigentliche Fund.** Die
  Basislinie war nach dem **versionierten Dateinamen** geschluesselt, und
  `check.py` uebersprang unbekannte Schluessel stillschweigend. Da jede
  Bearbeitung den Dateinamen aendert, war jedes gerade bearbeitete Kapitel ein
  unbekannter Schluessel. Die Sperrklinke verglich also ausschliesslich Kapitel,
  die niemand angefasst hatte - genau die, die nicht schlechter geworden sein
  koennen. Ein frisch eingebauter Satz mit sechsundsechzig Woertern kam mit
  `--ratchet` und Rueckgabewert 0 durch.

  Behoben: die Basislinie steht auf **Kapitelnummern**, der Dateiname nur noch
  als Kommentar dahinter; alte Zeilen werden weiter gelesen. Ein unbekannter
  Schluessel bedeutet jetzt ein wirklich neues Kapitel und wird gemeldet statt
  verschluckt. Gegenprobe gefahren: dieselbe Kaputtmachung, die vorher mit 0
  durchkam, meldet jetzt *Kapitel 16: 0 geduldet, jetzt 1* und gibt 1 zurueck.

- **Das Laecheln in Kapitel 2 bis 6: zwei Stellen gesetzt, der Rest offen.**
  Es fehlte ueber fuenf Kapitel am Stueck, genau dort, wo er das Haus dreht, und
  Kapitel 7 erklaerte es danach als Handwerkslehre, als haette es das nie
  gegeben. Gesetzt sind jetzt Kapitel 3 (Ji-won auf der Treppe, klein gehalten)
  und Kapitel 5 (der Schneider, hauptsaechlich im Kinn). **Kapitel 2, 4 und 6
  haben weiterhin keins**, und das ist vertretbar: gestreut wuerde es billiger,
  nicht besser. Der volle Katalog steht in `doc/05-continuity.md`, die noch
  offenen Sorten sind dort als *offen* markiert.

  **Kapitel 16 hatte ebenfalls keins** und hat jetzt eines (v1.12): dieselbe
  Sorte wie Kapitel 5, das Respektvolle, hauptsaechlich im Kinn, fuer Kompetenz,
  die ihm nichts nuetzt. Es steht in der Stunde, in der Sang-hoon sein Handwerk
  erklaert, und es ist das einzige Laecheln des Kapitels. Das ist der teuerste
  Ort dafuer gewesen, weil sein Hauptwerkzeug sonst dreieinhalb Stunden lang
  nicht vorkam und Kapitel 17 eine Seite spaeter den ganzen Katalog aufzaehlt.

- **Das Halsband: keine Quote, sondern eine Bedingung.** Der Eintrag stand hier
  als Luecke ueber Kapitel 14 bis 17 und war zum groessten Teil ein Zaehlfehler.
  Die Suche lief auf `collar`, `throat`, `neck` und `jaw`, also auf vier
  Substantive fuer den **Gegenstand**, bekam null Treffer und wurde als
  Abwesenheit gelesen. Sie hat nie gefragt, ob die **Sache** vorkommt.

  **Sie kommt vor, und zwar dort am dichtesten, wo der Gegenstand fehlt.**
  Kapitel 14: *all that tells me is that he does not like what I am.* Kapitel
  15, die deutlichste Stelle im ganzen Buch: *"It's the night I was bought," he
  said*, dazu Hana ueber ihn als *the strongest thing you owned or the softest*
  und Annie mit *That is what I am buying.* Dieselbe Sorte in Kapitel 11
  (*eight hundred people had spent the evening deciding what I am*), 3 (*not one
  of the people who owned them*) und 8 (Chef Bang verbeugt sich vor *the table
  that had bought him*).

  **Die Regel, die daraus folgt:** Das Halsband erscheint nicht nach Takt,
  sondern wenn der Koerper tragen muss, was der Dialog gerade sagt. In Kapitel
  16 und 17 war genau das der Fall, und beide Kapitel sagten die Sache im
  Dialog laengst - Kapitel 16 sogar ausdruecklich (*I belong to one person. She
  paid a great deal for me*) - waehrend die zwei Stellen, an denen es koerperlich
  wurde, leer waren: die Frage, wo er schlaeft, und das Eingestaendnis, dass
  *Mistress* wahr geworden ist. Dort steht es jetzt, in v1.12 und v12.3.

  **Kapitel 14 und 15 bleiben, wie sie sind.** Was in beiden steht, ist besser
  als der Gegenstand, weil es aus einem Mund kommt.

  **Die Pruefung, die kuenftig laeuft**, ist deshalb nicht die Substantivsuche,
  sondern die Frage je Kapitel: sagt es irgendwer, in irgendeinem Register, was
  er ist? Und falls ja: muss der Koerper es an dieser Stelle mittragen? Nur wenn
  beide Antworten auseinanderfallen, ist etwas offen.

- **Der Haushalt ist seit Kapitel 13 fast verschwunden.** Kapitel 14 und 16
  enthalten je eine Haushaltsfigur. Die Textur, die das Buch in den Kapiteln 3
  bis 6 hatte, traegt die Verhandlungsszenen erst.

- **Hana muss den Apfel gehoert haben**, bevor die Szene mit Sang-hoon kommt.
  Steht seit Kapitel 15 im Text, also erledigt, aber es darf nicht wieder
  herausfallen.

- **Georgij lacht zweimal, nicht einmal.** Kapitel 7 an Mrs Sunwoo, nachdem sie
  die Decke haesslich genannt hat: *"He laughed. She was pleased. She went
  away."* Das ist Handwerk, gebaut wie die Laecheln daneben. Und Kapitel 13 ueber
  Woos Geschichte vom Schiffsagenten: *"which was not work."* Nur das zweite ist
  dieselbe Gattung wie das ungebaute Laecheln. Der Zusatz *which was not work*
  ergibt ueberhaupt nur Sinn, weil der Vergleichsfall existiert - und er stand
  bisher nirgends verbucht, was den einen echten Lacher billiger gemacht hat,
  als er ist.

  **Dieselben drei Woerter fallen ein zweites Mal**, in Kapitel 16 aus
  Sang-hoons Mund: *"That one was not work."* Beide Stellen sind jetzt als
  festgelegte Zeile in `doc/05-continuity.md` verbucht.

- **Der Zahltag von quid pro quo.** Ab Kapitel 17 faellt der Satz nicht mehr
  beilaeufig. Die naechste Verwendung ist die im Bruch. Eine Ausnahme ist bereits
  verbraucht: In Kapitel 17 benutzt Georgij ihn gewichtet, um ihr etwas zu geben.
  Das laedt den Bruch auf, statt ihn zu entwerten, aber ein zweites Mal traegt es
  nicht.

- **Kalte Faeden.** Die Glasfirma aus Yeongdeungpo, vier Fremde an Seilen an
  einer Wand ohne Tuer, jeden zweiten Mittwoch, steht seit Kapitel 5 oben auf
  Georgijs Liste fuer Jang und ist nie wieder erwaehnt worden. Eun-jus zwei
  Fragen nach seinem Vorher liegen seit Tag fuenf. Mr Yeo hat in sechsundvierzig
  Tagen kein Wort gesagt, was so bleiben soll, aber einmal wieder auftauchen
  muss, damit es Absicht bleibt. Choi Dae-ho ist seit Kapitel 7 ein Name ohne
  Szene. Die Familie Lee steht im Figurenverzeichnis und ist in siebzehn
  Kapiteln nicht vorgekommen.
