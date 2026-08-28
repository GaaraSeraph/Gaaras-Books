# Szenenpruefung ueber beide Baende, 27./28.08.

*Protokoll. Vergangenheit mit Datum. Gewinnt nie.*

Auftrag des Autors: **"Anzahl der Woerter, die zu viel sind, ist irrelevant. Ich
moechte alles streichen, was an Szenen ueberfluessig ist oder sich wiederholt."**

Damit ist die Bauentscheidung aus der Uebergabe vom 27.08. (Kapitel 26, 29, 32,
35 teilen oder nicht) hinfaellig. Sie war eine Antwort auf Wortzahlen. Die vier
bleiben, wie sie sind, und die Umnummerierung entfaellt.

---

## Pruefumfang

**Alle 117 Kapitel gelesen**, nicht referiert: 83 in `chapters-2/`, 34 in
`chapters/`. Neun Lesegruppen ueber je einen Block, dazu der Block 24 bis 35 von
Hand. Zusammen rund **270.000 Woerter**.

Die Rueckbezugsprobe lief mechanisch gegen alle 117 Kanon-Dateien, die
Kanonliste jeweils programmatisch als hoechste Fassung je Kapitelnummer
gebildet. Das war noetig: `chapters/` enthaelt bis zu siebzehn Fassungen
desselben Kapitels, und eine Suche ohne diesen Filter liefert fuenfzehnfache
Falschtreffer.

**Jede folgenreiche Behauptung unten ist gegengeprueft worden**, bevor sie hier
steht. Zwei Meldungen sind dabei gefallen und stehen unter *Widerlegt*.

---

## Das Ergebnis vorweg

**An ueberfluessigen Szenen gibt es fast nichts.** Von rund 300 echten Szenen
ueber beide Baende ist **eine einzige** ersatzlos streichbar. Der Band ist
dichter, als die Streichlisten vermuten lassen.

**Der Ertrag liegt woanders: elf harte Fehler, davon fuenf Reste desselben
Umbaus vom 27.08.** Die Wiederholung, die tatsaechlich dasteht, ist nie eine
ganze Szene, sondern **Beat-Doppelung innerhalb der Berichtsszenen** — und
zweimal eine Dreifachnennung innerhalb eines einzigen Kapitels.

---

## 1. Der Umbau hat fuenf Verweise stehengelassen

Beim Umbau am 27.08. wurde **alt `ch78`** (Tag 367, Montag 5. Oktober) zu
**neu `ch76`** und dabei auf Tag 500, Montag 15. Februar umdatiert. **Innerhalb**
des Kapitels ist sauber mitgezogen worden — alt `ch78:338` sagt *"a woman half
my age decided **in October**"*, neu `ch76:260` sagt *"**in February**"*.

Die Verweise ausserhalb hat niemand gesucht. Es sind fuenf:

| Stelle | Was sie behauptet | Was gilt |
|---|---|---|
| **`ch52:6-20`** | Blickt am **7. Oktober** auf Woos versiegelte vier Antworten zurueck | Woo kuendigt sie in `ch76:252` an, **15. Februar**, 131 Erzaehltage spaeter |
| **`ch50:102`** | *"Woo had done that for him on a Sunday"*, am **25. August** | Woos Sonntag ist `ch71`, **10. Januar** |
| **`ch78:66`** | *"You told him that yourself in December and you said it was the bill"* | Dieser Wortwechsel steht erst in `ch82:134-136`, **1. Mai** |
| **`ch82:172`** | *"the thing he said in October"* | Der Satz steht in `ch68:250`, **28. Dezember** |
| **`ch83:146`** | *"On the twenty-third of April … a woman in Yeouido"* | Der Schwur steht in `ch18:150`, **30. April**, gegenueber Nam Byung-hee **in Ulsan** |

**Gegenprobe zu `ch52`:** `four answers` ueber alle 117 Kanon-Dateien ergibt
`ch52:8`, `ch61:212` (anderer Zusammenhang), `ch76:62/206/228`, `ch80:52`. Es
gibt keine fruehere Woo-Szene. Im Archiv liegt die Vorgeschichte offen:
`archiv/band-2-vor-umbau/ch78_v1_6_en.md:166` traegt die Kopfzeile *Day Three
Hundred and Sixty-Seven · Monday 5 October*, und `ch80_v1_2_en.md:4` traegt
*Day Three Hundred and Sixty-Nine · Wednesday 7 October* — das ist das heutige
`ch52`. Alt 78 und alt 80 lagen zwei Tage auseinander, und der Bezug war richtig.

**`doc/15-kalender.md:622` fuehrt Tag 367 noch als Woo-Szene.**

**Warum `check.py` das nicht findet:** es prueft Datumszeilen gegen den
Kalender. Es kann nicht pruefen, ob ein Absatz auf ein kuenftiges Ereignis
zurueckblickt. Das ist genau die Klasse, die `CLAUDE.md` benennt — *was nicht
geprueft wird, driftet.*

---

## 2. Sechs weitere Fehler, unabhaengig vom Umbau

| Stelle | Befund |
|---|---|
| **`ch47:144-146`** | *"Nobody paid a fee for hers, because it was not a service. It was a term."* Widerspricht `ch20:48` (*"Four fees over four years"*), `ch20:54` (*"He paid the fee. It is in the ledger with the other three"*), `ch24:134` (Yeom: *"I paid that one"*) und `ch26:410`. **Die Gebuehr wurde bezahlt**, von Yeom, aus eigener Tasche; nicht in Rechnung gestellt wurde das **Los**. `ch47` verwechselt beides und dreht damit den Kernmechanismus des Buches um |
| **`ch57:178`** | *"It was not difficult and it is still twice." She rang off…* — Mrs Jeons Antwort und ihr Auflegen stehen **sechzehn Zeilen**, nachdem sie den Hoerer verlassen hat (`:162`, `:164` Trenner, `:166` *"He put the receiver down"*), mitten in der Jang-Szene. Gehoert unmittelbar hinter `:162` |
| **`ch69:280`** | Koh telefonierte *"in September"*. `ch48:66` datiert die zwei Anrufe auf den **11. und 13. August**, `ch48:70` nennt das abgesagte Essen *"a dinner he goes to every August"*. `ch48` ist verankert, `ch69` ist der Fehler |
| **`ch68:4/6`** | Kopfzeile *Monday 28 December*, Text *"he wrote down on the **Tuesday** morning"*, danach `:20` *"He telephoned on the Monday morning"*. Der erste Block gehoert zum 22. Dezember, also zum Tag von `ch67` |
| **`ch13:44/92`** (B1) | *"took him a day and a half"* ab Donnerstagmorgen endet Freitagabend, nicht *"By the Thursday evening"* |
| **`ch15:446`** (B1) | Annie: *"Four thousand two hundred. Do not lose that figure. **I am going to ask you for it again in a year.**"* Sie fragt nie. Gegenprobe ueber beide Baende: `four thousand two hundred` kommt in `chapters-2/` **kein einziges Mal** vor. Das ist der Kapiteltitel und die einzige Stelle, an der Georgij die Kosten seiner Arbeit in Menschen benennt |

---

## 3. Zwei Werkzeuge waren blind, und zwar genau dort, wo gesucht wurde

**`doppelt.py` wirft vor jedem Vergleich die 300 haeufigsten Wortformen weg.**
Es sieht damit jede Wiederholung, die aus seltenen Inhaltswoertern besteht, und
**keine einzige**, die aus Allerweltswoertern gebaut ist. Genau daraus besteht
die Dialogmaschinerie.

Beleg, von `doppelt.py` nicht gemeldet:

```
b2 31:80  "That is a good explanation," said Georgij. "It fits everything you
          can see from this chair, and I would have arrived at it myself, and
          it is wrong."
b2 69:84  "That is a good explanation," said Georgij. "It fits everything you
          can see from that chair, and I would have arrived at it myself, and
          it is wrong."
```

Die fehlende Messung ist nachgebaut worden: Wortfolgen ohne Fuellwortfilter.
Ergebnis bei zwoelf Woertern: **144 wortgleiche Folgen in zwei oder mehr
Kapiteln.** Aufgeteilt nach Kapitelabstand: 36 Folgen in 25 benachbarten Paaren
(Verdacht *Bericht zitiert die Szene*), 98 in 82 entfernten Paaren (eher Motiv
oder Rueckruf). Spitzenreiter der entfernten: **b2 31 + b2 69 mit drei Folgen.**

**`abendbericht.py` meldet 0 von 52 unter der Schwelle 0.45.** Auch bei 0.62 nur
zwei. Der Abendbericht ist also **nicht** das Problem, das `doc/23` in ihm
vermutet hat — die Doppelung sitzt eine Ebene tiefer, im einzelnen Beat.

---

## 4. Der Szenentrenner ist ab Kapitel 50 kaputt

Drei Lesegruppen haben das unabhaengig gemessen:

| Bereich | `* * *` je Kapitel | Ø Woerter je Block |
|---|---|---|
| Band 1, 1–34 | 0–2 | 638–3163 |
| Band 2, 1–49 | 0–4 | 510–3603 |
| Band 2, 50–68 | 8–15 | — |
| **Band 2, 69–83** | **18–32** | **64–277** |

Schaerfster Fall **`ch80`**: **32 Trenner fuer ein einziges Gespraech** von 2.092
Woertern. `ch60` hat 21 fuer vier Szenen, `ch53` 18 fuer drei. Einzige Kapitel ab
50, die die Disziplin halten: **`ch65`** (0) und **`ch71`** (3).

Gemessen: Block 48–59 hat 150 Bloecke fuer **53** Szenen, Block 60–71 176 fuer
**45**, Block 72–83 262 fuer **39**.

In Band 1 tritt der umgekehrte Fehler auf: `ch13` hat **einen** Trenner fuer
fuenf Szenen ueber zwei Tage, `ch20:24` trennt einen Orts- und
Besetzungswechsel nur mit `---`.

**Folge:** die Zahl **411 Szenen** aus der Uebergabe ist nicht vergleichbar
gezaehlt. Es sind rund **300**. Jede Suche nach "zu kurzen Szenen" liefert ab
`ch50` dutzendweise Falschtreffer.

---

## 5. Offene Faeden, die nie bezahlt werden

- `ch01:60` Annie: *"Then I will give one to Mrs Seo."*
- `ch02:178` Annie: *"two of them will be gone by June."*
- `ch44:222` Yeom: *"I am going to read the rest of them, and I am going to tell
  you what is in them"* — sein letzter Auftritt `ch46:16` sagt das Gegenteil
- `ch45:312-318` Klausel vier auf September vertagt, findet nicht statt
- `ch64` die Seite mit vierzehn Namen: mit Gewicht eingefuehrt, einmal benutzt,
  nie wieder erwaehnt
- `ch75:192` Baeks Termin bei der Law Society am 2. Maerz
- `ch79:324` Mrs Seo: *"in about a year I am going to tell you what it was"*
- **B1** `ch15:446` die 4.200 (siehe oben)
- **B1** `ch20:16` Ji-won kommt hier zum **letzten Mal im ganzen Manuskript** vor,
  nach vier Auftritten, ohne Abschluss

Die letzten zwei in Band 2 sind vermutlich Band-3-Haken.

### Drei Ladungen in Band 1, die zweimal scharf gestellt werden und nie feuern

**Die Glasreiniger.** `ch05:80-84` (im Gespraech mit Jang) und `ch05:184-188`
(in der Erzaehlerbilanz, hundert Zeilen spaeter, teilweise wortgleich): eine
Fremdkolonne, vier Maenner, einmal im Monat an Seilen an einer Wand ohne Tuer,
*"One of the four has never been the same man twice"* — und ausdruecklich
*"He put it at the top of what he was keeping for Jang, above the night man and
above everything else."* Gegenprobe ueber alle 117 Kanon-Dateien mit `cradle`,
`second Wednesday`, `Yeongdeungpo`, `roof anchors`: **kein einziger inhaltlicher
Treffer** nach `ch05` (die drei Fundstellen in Band 2 sind eine Telefongabel und
ein Stadtteil). Die am schaerfsten gestellte Waffe des Bandes wird nie
abgefeuert.

**Die Wohltaetigkeitsauktion, `ch08:204-262`, 618 Woerter.** Los neun ist ein
Mensch: Chef Bang, der neben der Kanzel steht und laechelt, waehrend
achthundert Leute entscheiden, was ein Abend von ihm wert ist. Georgij rechnet
gegen seinen Willen mit, und Annie dreht die ganze Minute vor dem Zuschlag den
Kopf nicht. Das ist der Titelvorgang des Buches, gespiegelt in der sauberen
Welt, und die **erste Schutzhandlung Annies ueberhaupt**. Gegenprobe ueber
beide Lesefassungen: `Chef Bang`, `lot nine`, `sixty-two million` kommen in
`book-band-2.md` **kein einziges Mal** vor, und in Band 1 nur an dieser Stelle.
Nichts zeigt je zurueck.

**Mr Yeo.** Derselbe Beat dreimal — `ch04:44`, `ch05:172-176` (elf Woerter
wortgleich mit ch04), `ch12:22`. Er sagt in beiden Baenden kein Wort, kommt nach
`ch12` nicht mehr vor und fehlt sogar in der Loyalitaetsliste `ch14:206`, in der
Mrs Seo, Mr Baek, Ji-won, Eun-ju, Jang und Bae einzeln aufgezaehlt werden.

**Diese drei sind keine Kuerzungsfrage, sondern eine Bauentscheidung:** entweder
sie fallen, oder sie brauchen eine Einloesung. Zweimal scharf stellen und nie
feuern ist teurer als beides.

**ENTSCHIEDEN am 28.08. Der Autor: *"das klingt wichtig. lassen."*** Alle drei
bleiben im Text. Damit ist die Frage nicht mehr, ob sie gestrichen werden,
sondern **wo sie eingeloest werden** - offen und ausdruecklich als Aufgabe
uebernommen. Bei der Wohltaetigkeitsauktion genuegt dafuer eine einzige spaetere
Zeile, in der jemand Annies Wegsehen benennt.

**EINGELOEST am 27.08. Alle drei. Siehe Abschnitt 10.**

---

## 6. Widerlegt — Meldungen, die die Gegenprobe nicht ueberstanden haben

- **Die sechs Aufdeckungsszenen `ch64` bis `ch69` sind nicht redundant.** Das war
  die Ausgangsvermutung dieses Durchgangs, weil dort sechsmal dieselbe
  Grundbewegung in vierzehn Erzaehltagen laeuft. Auf **jede einzelne** zeigt eine
  spaetere Stelle woertlich: `ch82:246` · `ch82:92` · `ch74:230` · `ch78:30` ·
  `ch82:126` · `ch79:168`. Die Vermutung ist gefallen.
- **`b1 30:274` / `b1 31:206`** stellen dieselbe Regel mit vertauschten Haelften
  auf. Sah nach Kontinuitaetsfehler aus. Ist keiner: in 30 spricht Georgij zu
  Ye-rin (*you* = Ye-rin, *her* = Annie), in 31 zu Annie (*you* = Annie,
  *her* = Ye-rin). Die Referenzen sind stabil, nur die Anrede kippt.
- **`ch29:214` / `ch27:322`** — wortgleich, aber als Rueckruf markiert
  (`ch29:216` *"He had written that on Saturday"*).
- **`ch79:138` / `ch81:68`** — wortgleich, aber das ist die Pointe des Abends:
  dieselben Fakten vor und nach dem Kippen des Raums.
- **`b1 24` + `b1 34`** haben 51 gemeinsame Achtergramme — und **jedes einzelne**
  ist im Text attribuiert (*"On the bridge I told you…"*). Kapitel 34 ist die
  Abrechnung der Bruecke.

---

## 6a. Ausgefuehrt am 28.08., auf Freigabe des Autors

**Sechzehn Dateien geaendert, Dateiname und Kopfzeile jeweils hochgesetzt.**
`check.py` danach: 117 Kapitel geprueft, **keine neue Verschuldung**. Die zwei
verbliebenen Fehlermeldungen stehen in `b1 ch06` und `b1 ch12`, beide nicht
angefasst und beide in der Basislinie verbucht. `build.py` laeuft durch.

Band 1: 101.196 auf **101.083** Woerter. Band 2: 222.959 auf **222.491**.

### Reparaturen

| Datei | Was |
|---|---|
| `ch47_v1_9` | *"Nobody paid a fee for hers"* auf die richtige Unterscheidung gestellt: die Gebuehr wurde gezahlt, nicht in Rechnung gestellt wurde das Los |
| `ch50_v1_10` | Der falsche Anker *"Woo had done that for him on a Sunday"* entfernt. Ein frueherer Woo-Sonntag existiert nicht; der Bezug stammt vermutlich aus einem der neun gestrichenen Kapitel |
| `ch57_v1_3` | Mrs Jeons Antwort und ihr Auflegen aus der Jang-Szene heraus und hinter Georgijs *"It was not difficult."* gesetzt |
| `ch69_v3_2` | *"telephoned two men in September"* auf **August** |
| `ch78_v3_2` | Die erfundene Dezember-Zuschreibung ersetzt durch den Satz, den Georgij im Dezember tatsaechlich sagt (`ch68:152`) |
| `ch82_v3_1` | *"the thing he said in October"* auf **December** |
| `ch83_v3_1` | *"twenty-third of April … a woman in Yeouido"* auf **thirtieth of April … a woman in Ulsan** |

### Schnitt

| Datei | Was |
|---|---|
| `ch52_v1_4` | Szene 1 und 2 gestrichen, also der ganze Erzaehltag Mittwoch 7. Oktober. Das Kapitel beginnt jetzt Freitag 9. Oktober. Der Kalender brauchte keine Aenderung, er fuehrt fuer Tag 369 keinen Eintrag |

### Kuerzungen

| Datei | Was |
|---|---|
| `ch06_v1_12` | Die Aufzaehlung in der Rede an Mrs Jeon gestrichen; sie sagte vierzig Zeilen spaeter noch einmal, was Szene 1 ausfuehrlich erzaehlt hatte |
| `ch31_v3_1` | Das Kapitelende gestrichen, das zusammenfasste, was `ch32:6-12` danach spielt |
| `ch45_v1_5` | Zwei der vier Schluessel-Nennungen entschaerft. Es bleiben das Ereignis, die Notizbuchliste und das Urteil |
| `ch48_v1_12` | Die erste der drei Negativlisten auf zwei Saetze. Die zweite (`:172`) bleibt vollstaendig, weil dort der Schluss kippt |
| `b1 ch05_v5_15` | Mr Yeos Beschreibung nicht zum zweiten Mal ausgeschrieben |
| `b1 ch15_v2_14` | Georgij sagte sechs Zeilen nach dem Erzaehler dasselbe noch einmal |
| `b1 ch16_v1_22` | Drei der vier Notizbuchzeilen gestrichen; alle drei werden im naechsten Kapitel woertlich an Annie wiederholt. *"He wrote four lines"* zu *"one line"* nachgezogen |
| `b1 ch18_v2_13` | Die dritte vollstaendige Nennung von *"Nine institutions … internal approval"* auf einen Satz |

### Zurueckgezogen, weil die Gegenprobe sie nicht ueberstanden hat

Fuenf Meldungen sind bei der Einzelpruefung gefallen. Sie stehen hier, damit
sie nicht ein zweites Mal aufgemacht werden:

- **`ch68`, angebliche falsche Datumszeile.** *"he wrote down on the Tuesday
  morning"* unter der Kopfzeile *Monday 28 December* ist eine Rueckblende, wie
  das Buch sie ueberall benutzt. Kein Fehler.
- **`b1 ch13`, angeblicher Zeitwiderspruch.** *"a day and a half"* und *"By the
  Thursday evening"* betreffen zwei verschiedene Straenge, die parallel laufen.
- **`ch40/2`.** Sieht wie ein Bestaetigungsbericht aus und ist keiner: Annie
  zwingt ihn, laut zu sagen, was er mit der Naht vorhat, und ruegt die
  aufgeraeumte Fassung (`:210`). Das steht sonst nirgends.
- **`b1 ch03:10`.** Markiert, dass er allein ist, und traegt damit die
  Neun-Sekunden-Inventur zwei Zeilen spaeter.
- **`b2 ch15/1`.** Die Kreuzung der Listen laeuft in eine Sackgasse, aber
  gescheiterte Arbeit zu zeigen ist der ausdrueckliche Grundsatz des Buches
  (`ch34`: *eine Liste, die nur zeigt, was uebrigbleibt, ist schlechter*).
  **Bleibt Autorenentscheidung.**

### Noch nicht ausgefuehrt

`b1 ch20/3`, `b1 ch07:182-188`, `b1 ch17:22/:26/:54`, `b1 ch05/5+6`,
`b2 ch22/2`, `b2 ch14/1:144-152`, die Maschinerie in `b2 ch69` und die erste
Haelfte von `b2 ch82/3`.

**Die zwei grossen Aufsagungsszenen sind ausgefuehrt**, siehe Abschnitt 8.

**Warnung fuer den, der die restlichen macht:** der Ersatztext aus dem
Pruefauftrag zu `b1 ch31/4` fuehrte an mehreren Stellen Material ein, das an der
Stelle nicht steht (eine Karte mit vier Zeilen, eine Annie-Replik ueber die
sechs). Er war **nicht** uebernehmbar und ist nicht uebernommen worden.
Kuerzungen an diesen Szenen muessen aus dem gebaut werden, was schon dasteht.

## 7. Regel, die aus diesem Durchgang folgt

**Ein Umbau, der ein Kapitel umdatiert, ist erst fertig, wenn jeder Verweis
darauf gesucht worden ist.** Fuenf der elf Fehler oben stammen aus einer
einzigen Umdatierung, bei der die Ursache verschoben und die Wirkung
stehengelassen wurde. Innerhalb des verschobenen Kapitels ist sauber gearbeitet
worden; ausserhalb hat niemand gesucht.

Die mechanische Probe dazu ist billig: nach der Umdatierung die Kernbegriffe des
verschobenen Kapitels ueber alle Kanon-Dateien greppen und jeden Treffer gegen
den neuen Tag legen.

## 8. Die zwei Aufsagungsszenen, ausgefuehrt

**229 Woerter aus vier Kapiteln.** Band 1 steht danach bei 100.872 statt 101.101.
`ch11` und `ch31` melden **sauber**, keine neue Verschuldung gegenueber der
Basislinie.

### Die Regel, nach der geschnitten wurde

**In einer Berichtsszene darf eine Tatsache benannt, aber nicht ein zweites Mal
beschrieben werden.** Benennen ist noetig, weil die Zuhoererin nicht dabei war.
Beschreiben ist der Rueckschritt, weil der Leser dabei war.

Daraus folgt der Schnitt, der beim Zaehlen zuerst auffaellt: **zwei von fuenf
Stellen liegen in Kapitel 10 und nicht in Kapitel 11.** Wo eine Entdeckung
zweimal steht, faellt sie nicht am zweiten Ort, sondern an dem, wo sie weniger
tut, und das war hier die Vorwegnahme.

### Gestrichen

| Datei | Stelle | W | Warum |
|---|---|---|---|
| `ch10_v2_7` | :66-68 | 42 | *"It would be one in the morning, in the dark, in the back of a car, before it occurred to him ..."* Die Erzaehlung kuendigt an, dass die Erkenntnis im Wagen kommt, und liefert sie dann selbst. Damit war `ch11:50`, wo Annie sie hoert, schon ausgegeben |
| `ch10_v2_7` | :126 | 7 | Hanas Warnung stand woertlich dreimal: gesprochen (`ch09:244`), erinnert (`ch10`), gebeichtet (`ch11:70`). Die mittlere behaelt den Takt und gibt das Zitat ab |
| `ch10_v2_7` | :276 | 62 | Der Erzaehler beweist, was Sang-hoon acht Zeilen vorher selbst gesagt hat (*"she has never had an adviser"*) und was Annie in `ch11:170` liefert, ehe Georgij ausgeredet hat |
| `ch11_v2_14` | :122 | 27 | Die stille Frau wird in `ch09:144` beobachtet; der zweite Satz war die woertliche Wiederholung |
| `ch11_v2_14` | :128-130 | 55 | Er beschreibt beide Kims, Annie sagt *"So you have two descriptions"*, und er beschreibt **beide noch einmal**. Die zweite Beschreibung zitierte ausserdem *"Paper gives you names"* aus `ch09:132` zurueck |
| `ch11_v2_14` | :186 | 12 | Sang-hoons Reaktion stand als Doppelzitat aus `ch10`. Das Lachen bleibt, weil es das einzige Ungemessene an dem Abend war |
| `ch11_v2_14` | :220 | 11 | *"which is not a thing a woman of that sort does"* ist die Deutung des Erzaehlers aus `ch09:296`. Annie kennt Hana seit zwoelf Jahren |
| `ch31_v1_12` | :126 | 30 | Ye-rins Argument stand in `ch30:254` im Wortlaut und hier fast vollstaendig noch einmal. Annie braucht die Pointe, nicht den Vortrag |
| `ch31_v1_12` | :188-194 | 15 | *"Du haettest koennen / warum nicht / weil"* ist genau der Dreischritt aus `ch30:362-368`. Neu war allein, **dass sie es herausfindet**; das bleibt |
| `ch31_v1_12` | :206 | 28 | Die Begruendung des Versprechens stand in `ch30:274` woertlich. Annie liefert das Urteil danach selbst (*"It is the only version that works"*), also braucht er es nicht vorher zu sagen |

### Was ausdruecklich stehengeblieben ist

**`ch31:272-278`, der grosse Preis, den er nicht nennt.** Das ist die woertliche
Wiederholung von `ch30:374-378` und sie bleibt, weil Annie sie **benennt**:
*"That is what you said to her." - "Word for word." - "Nearly."* Eine
Wiederholung, die die Figur bemerkt, ist keine Aufsagung mehr, sondern der
Gegenstand der Szene. Das ist das Muster, an dem sich die anderen messen lassen
muessen.

Ebenso `ch11:150` (Sang-hoons *"bring whatever it is you're going to bring"*),
weil Annie darauf antwortet und Georgij es umdeutet, und `ch11:208-234`, das
Gestaendnis der gebrochenen Regel, das in `ch09` nur passiert und hier zum
ersten Mal ausgesprochen wird.

### Vier Gegenproben vor dem Schnitt

1. **Kanonliste programmatisch gebaut**, nicht geraten: `ch09_v3_5`,
   `ch10_v2_6`, `ch11_v2_13`, `ch30_v1_15`, `ch31_v1_11`. In `chapters/` liegen
   sieben Altfassungen von `ch11` und fuenf von `ch31` daneben.
2. **Zeichenprobe.** Alle drei Dateien fuehren gerade Apostrophe und
   Anfuehrungszeichen, kein typografisches Zeichen, keine Gedankenstriche. Ein
   Ersatzstring mit dem falschen Apostroph findet nichts und meldet nichts.
3. **Jede Ersetzung mit Trefferzaehlung.** Neun Auftraege, neun Treffer, jeder
   genau einmal. Ein Auftrag, der nicht genau einmal trifft, ist falsch und
   nicht die Datei.
4. **Rueckbezugsprobe.** Vor jedem Schnitt geprueft, ob eine spaetere Stelle
   darauf zeigt. Ergebnis: **keine.** Alle Streichungen sind Paare zwischen
   `ch09`/`ch11` und `ch30`/`ch31` ohne dritte Stelle. Auch `doc/` zeigt auf
   keine davon; die Treffer dort (`16-motive.md:333`, `12-stimmen.md:2235`)
   zitieren Saetze, die im Kanon stehengeblieben sind.

**Der Fund, der beim Zaehlen herausfiel:** *"a quarter of a beat behind"* stand
**fuenfmal** - `ch09:146` als Beobachtung, `ch11:116` **und** `ch11:130` im
Bericht, `ch14:28` und `ch14:38` bei der Umdeutung. Kapitel 14 ist die Einloesung
(er lachte spaet, weil er auf etwas zwei Meter weiter hoerte, nicht aus
Schwaeche) und braucht die Pflanzung in `ch09`. Die doppelte Nennung im selben
Kapitel 11 war der Ueberschuss.

### Zwei Nachbesserungen nach dem ersten Durchgang

Beim Nachlesen der geschnittenen Stellen, was der zweite Durchgang immer noch
findet:

- `ch31:188` stand nach dem Schnitt als *"You could have taken all three."* /
  *"I could have taken all three ..."* da. Annies Zeile zurueck auf *"You could
  have taken it."*, damit die Steigerung wieder ihm gehoert.
- `ch11:128` bekam *"He turned his head."* als Beat, zehn Zeilen nach *"Annie
  turned her head."* Ersetzt durch *"The car went on."*, das der Kapitelidiomatik
  entspricht (fuenf Strassen-Beats in `ch11`).

## 9. Der Rest der Liste, 27.08.

**364 Woerter aus sieben Kapiteln.** Band 1 von 100.872 auf **100.587**, Band 2
von 224.461 auf **224.382**. `check.py`: 117 Kapitel, 2 mit Fehlern (die zwei
Basislinien-Eintraege in `b1 ch06` und `b1 ch12`, beide nicht angefasst), keine
neue Verschuldung. `build.py` laeuft durch.

### Ausgefuehrt

| Datei | W | Was |
|---|---|---|
| `ch05_v5_16` | 42 | Stuhl und der Dreiklang *Archiv, Plan, zwei Kameras* standen alle schon in der Jang-Szene derselben Kapitelhaelfte. Dazu zwei Fehler, siehe unten |
| `ch15_v2_16` | 49 | Zweiter Superlativ ueber dasselbe Dokument vier Zeilen nach dem ersten; und die Hanseong-Aufzaehlung, die in `ch14:64` steht und in `ch16:222` noch einmal gebraucht wird |
| `ch17_v12_20` | 49 | Das Seitenlesen und die Slot-Frage aus `ch16:262` und `ch16:290`; dazu zwei Wiederholungen in einer einzigen Replik (`ch16:208` und `ch18:172`) |
| `ch20_v1_12` | 145 | Acht Beats, jeder mit einer Nacherzaehlung von `ch19` um eine echte Annie-Reaktion herum |
| `ch14_v1_8` | 53 | Fuenf Firmenportraets, die Jang in `ch13:12-24` geliefert hat. Die Deutung, die `ch14` an jedes haengt, bleibt |
| `ch45_v1_6` | 13 | *"den Schluessel, ohne zu fragen"* stand viermal. Uebrig: der Vorgang und die Abrechnung am Schluss |
| `ch48_v1_13` | 13 | Die Negativliste zum dritten Mal, gegenueber Annie |

### Zwei Fehler, die unter der Kuerzung lagen

**`ch05:90` rechnet nicht auf.** Am **Tag 4** sagt Georgij, der Nachtmann habe
seine Runde *"in six days"* nicht veraendert. Er ist seit der Nacht auf Tag 1 im
Haus, hat also drei Naechte. Dieselbe Szene sagt vierzig Zeilen spaeter
*"inside two nights"*. Auf **drei Naechte** gestellt.

**`ch05:186` steht in der falschen Reihenfolge.** Am **Tag 6** legt er die
Glasreiniger *"at the top of what he was keeping for Jang"*. Er hat sie Jang am
**Tag 4** auf neun Blaettern uebergeben; Jang liest sie dort vor (`:80`) und
nimmt sie an (`:84`, *"That one is mine before anything else is"*). Umgestellt
auf *"He had put it in front of Jang on the Tuesday"*. Das Bild von den vier
Fremden an Seilen bleibt, die zweite Beschreibung faellt.

Beide sind die Klasse, die `CLAUDE.md` benennt: **Zahlen und Zeitangaben im
Fliesstext, die niemand nachrechnet.** Keine der beiden Stellen kann `check.py`
finden.

### Sechs Meldungen zurueckgezogen

Die Gegenprobe hat sie nicht ueberstanden. Alle sechs bleiben in der Tabelle
stehen, durchgestrichen und mit Grund, damit die naechste Pruefung sie nicht
erneut meldet.

- **`b2 22/2`.** Sagt kein einziges Mal auf. Ein Satz Zusammenfassung
  (*"in the same form he had used with Mrs Sunwoo"*), dann **benennt Annie die
  Wiederholung selbst**: *"you are standing at the corner of my own desk
  reciting my own dates back to me."* Danach zwei neue Gruende und der ganze
  Yeom-Faden.
- **`b2 82/3`.** `ch82:100` fasst eine Stunde und zehn Minuten in einen Satz und
  benennt danach in drei Saetzen, was gesagt wurde. Und `ch82:156` ist die
  **Umkehrung** von `ch68:132`, nicht deren Wiederholung: im Dezember sagt
  Georgij zu Sim *"And you were good at it"*, im Mai muss Sim fragen. *"It is
  the bill"* steht im ganzen Buch einmal.
- **`b1 16:334-340`.** Die Heft-Zeile wird in `b2 73:212` **woertlich
  zurueckgerufen**. Die Vier-Waende-Rechnung darunter steht nirgends sonst.
- **`b1 18:288`.** Drei verschiedene Dinge, nicht dreimal dasselbe: `ch12:68`
  der Fund, `ch13:94` die Verengung auf drei Genehmigungen, `ch18:288` ein
  Rueckruf von elf Woertern nach zwei Kapiteln.
- **`b1 07:182-188`.** `ch08:20` ist keine zweite Vorbereitung, sondern die
  Einloesung. Der geteilte Wortlaut ist die Wiedererkennung.
- **`b1 06/1`.** Kein reiner Uebergang: der Umschlag liegt an der Stelle, an der
  acht Tage lang die Fernbedienung lag.

### Was das ueber die Liste sagt

Von 21 Zeilen der Tabelle sind inzwischen **12 ausgefuehrt, 6 zurueckgezogen,
3 Autorenentscheidung.** Die Quote der Fehlmeldungen liegt bei knapp einem
Drittel, und sie hat ein Muster: **die Liste hat nicht unterschieden zwischen
einer Wiederholung, die niemand bemerkt, und einer, die der Text selbst
benennt.** Die zweite ist kein Fehler, sondern eine Bauform, und sie ist in
diesem Buch haeufig.

### Zwei Sachen fuer den Autor

**`b1 ch20` liegt jetzt bei 1909 Woertern und damit unter der Spanne.** Das ist
ein Hinweis und kein Fehler, aber es heisst, dass das Kapitel schon vorher
knapp war. Die empfohlenen 473 haetten es auf 1580 gebracht.

**`ch05:10` und `ch05:158` geben beide neunzehn Minuten** fuer eine Runde um das
Haus: einmal Jang an seinem ersten Morgen, einmal der Nachtmann. Das kann ein
Reim sein und kann eine Verwechslung sein. **Nicht angefasst**, weil es eine
Entscheidung und keine Rechnung ist.

## 10. Die drei Ladungen, eingeloest

Am 28.08. entschieden: **"das klingt wichtig. lassen."** Damit war die Frage
nicht mehr, ob sie fallen, sondern **wo sie feuern**. Am 27.08. ausgefuehrt,
alle drei klein und ohne neuen Faden. Keine erfindet einen Vorgang; jede zieht
nur die Folge dessen, was schon dasteht.

### Mr Yeo, `ch12_v1_14`

Vier Auftritte, kein Wort in beiden Baenden, und er fehlt sogar in der
Loyalitaetsliste `ch14:206`. `ch12:22` war zugleich sein **letzter Auftritt**
und die **dritte Fassung desselben Beats** (`ch04:44`, `ch05:172`). Damit
loesen sich beide Meldungen an einer Stelle.

Er sagt weiterhin nichts. Umgekehrt wird nur, wohin er sieht:

> Mr Yeo came in at twenty past for his coffee and **looked at his face instead
> of his throat, which he had not done since the first morning**, and took the
> coffee outside.

Es steht an dem Morgen, an dem das ganze Haus die Zeitung gesehen hat: Ji-won
spricht das Foto an, Eun-ju hat es gesehen und erwaehnt es acht Stunden lang
nicht. Der Kragen ist die Sache, um die es bei Yeo immer ging.

### Die Glasreiniger, `ch12_v1_14`

Jang nimmt sie am **Tag 4** an: *"That one is mine before anything else is."*
Der zweite Mittwoch im Oktober ist der **8.**, also der Tag nach seinem
Antritt. In `ch12`, am Tag 23, berichtet er unaufgefordert, was seine Art ist
und was er in derselben Szene mit den Kennzeichen schon getan hat.

Der Kern der Ladung war `ch05:82`: *"One of the four has never twice been the
same man."* Er kommt nicht wieder, sobald Namen verlangt werden, und es laesst
sich nichts beweisen:

> "Three. The three of them have been coming here six years and they did the
> south wall in a day and a half instead of a morning, and nobody telephoned to
> say why." **"I have their names for next month. I do not expect to need them."**

Das ist eine geschlossene Tuer und kein neuer Faden.

### Die Wohltaetigkeitsauktion, `ch34_v1_12`

`ch08:214-258`: Los neun ist ein Mensch, Georgij rechnet gegen seinen Willen mit
und bekommt dreieinhalb heraus, und Annie dreht die ganze Minute vor dem
Zuschlag den Kopf nicht. Gegenprobe: `Chef Bang`, `lot nine` und
`sixty-two million` zeigen nirgends zurueck.

Eingeloest an der einzigen Stelle im Buch, an der **wieder eine Zahl fuer ihn im
Raum steht** und sie dasselbe wieder tut, naemlich `ch34` nach Sang-hoons
Angebot ueber zwei Milliarden zweihundert Millionen:

> She had said the figure without looking at him. She did that once before, in
> October, in a room with eight hundred people in it. It was the minute in which
> a chef in his whites stood beside a lectern and was bid up to sixty-two.

Drei Saetze, im Erzaehler, ohne die Szene anzuhalten. Der Griff fuer den Leser
sechsundzwanzig Kapitel spaeter ist *a chef in his whites* und *sixty-two*.

### Was dabei nicht angefasst wurde

Der Schluss von `ch34` ab *"No, Mistress."* Dort haette die Einloesung besser
geklungen und schlechter gearbeitet.

---

## 11. Die zwei Zwillingsstellen zwischen `b2 31` und `b2 69`

**Autorenentscheid: Zufall.** Gemessen wurden vier woertlich geteilte
Achtwortfolgen. Zwei bleiben, zwei sind aufgeloest.

**Bleiben, weil Absicht:**

- Die Heft-Zeilen (`31:192` / `69:320`) zaehlen mit. *first* gegen *second*, elf
  Uhr gegen zehn Uhr. Das ist das Register und nicht die Doppelung.
- *"That is not a courtesy"* steht an sechs Stellen im Buch (`ch03`, `11`, `31`,
  `48`, `53`, `69`). Eine Formel der Erzaehlstimme.

**Aufgeloest:**

- `69:84` war Wort fuer Wort `31:80`, mit *this* gegen *that*. Es passte
  ausserdem schlechter: **Kohs Erklaerung ist Arithmetik ueber das eigene
  Alter, Ims ist ein Gestaendnis.** Auf ein Gestaendnis antwortet man nicht mit
  *"you cannot see past your chair"*. Neu: *"That is an honest explanation. It
  is also wrong, and it is wrong in the one place you stopped looking."*
- `31:132` bekommt eine eigene Formulierung fuer die weiche und die harte
  Fassung, weil `69:160` die entwickeltere ist (vierzehn Tage, drei Uhr
  morgens) und ein Leser die Steigerung in dieser Richtung braucht.

Nachgemessen: **zwei Fundstellenpaare statt vier.**

---

## 12. Die Beat-Regel, praezisiert

**Anlass: eine Korrektur des Autors am 27.08.** *"die Regel sollte nicht sein je
Zeile ein Beat. beats sollten da sein, wo eigentlich ein Charakter mehrmals
hintereinander spricht."*

Die Regel stand immer schon richtig da (`20-handwerk.md`, Abschnitt 5,
*"zwischen zwei Bloecken derselben Figur"*). Gefehlt hat die **Gegenrichtung**,
und die ist der haeufigere Fehler, weil ein Beat harmlos aussieht. Neu in
`20-handwerk.md`, Abschnitt 2g:

- **Gebraucht:** wenn dieselbe Figur zwei Redebloecke hintereinander hat.
- **Nicht gebraucht:** im Wechsel. A, B, A, B traegt sich selbst.
- **Schaedlich:** zwischen zwei Haelften einer Rede, die nur der Laenge wegen
  geteilt wurde.
- **Die Probe ist der Daumen.** Beat zudecken. Weiss man immer noch, wer
  spricht, gehoert er nicht dorthin.
- **Die Ausnahme:** ein Beat, der etwas **tut**, darf auch dort stehen, wo der
  Sprecher klar ist. Er bezahlt seinen Platz dann mit Arbeit statt mit
  Rhythmus.

Die Kurzfassung samt Daumenprobe steht jetzt auch in `CLAUDE.md` bei Regel 5,
damit sie jede Sitzung mitliest.

**Zwei eigene Fehler von diesem Tag sind als Beispiele dort vermerkt:** der
Kopfschwenk in `b1 ch11` zehn Zeilen nach Annies, und ein Beat, der in den
Jang-Einschub in `ch12` gesetzt werden sollte, wo sich die Sprecher ohnehin
abwechseln. Der zweite ist vor dem Einsetzen aufgefallen.

## 13. Das Tagesregister, 28.08.

**`werkzeug/register.py`, Ausgabe `erzeugt/REGISTER.md`.** Es liest nur die
Kapiteldateien und rechnet. Es entscheidet nichts.

**Wozu, in einem Satz:** `check.py` prueft eine Datumszeile, die dasteht. Es
kann nicht sehen, dass eine **fehlt**. Genau so lief `b2 ch22` zwei Erzaehltage
unter einer Zeile, und **Tag 223 kam im ganzen Buch nicht vor** - nicht in einem
Kapitel und nicht im Kalender.

### Stand nach dem Bau

- **117 Kapitel, 145 belegte Erzaehltage**, Tag 1 bis Tag 590, also 4. Oktober
  2025 bis 16. Mai 2027.
- **Datumszeilen gegen den Kalender: alle sauber.** Wochentag, Monatstag und
  Monat stimmen an jeder Zeile, Spannenkoepfe eingeschlossen.
- **Kein Tag steht in zwei nicht benachbarten Kapiteln.** Das waere ein Fehler.
- 24 Tage laufen ueber eine Kapitelgrenze. Das ist der Normalfall dieses Buches
  und keine Meldung.
- 445 der 590 Tage werden nicht erzaehlt. Auch das ist kein Befund, sondern ein
  Roman.

### Was das Register jetzt moeglich macht

Die 383 ausdruecklichen Datumsangaben im Fliesstext und die 929 Jahresspannen
sind damit **einzeln entscheidbar** statt schaetzbar: jedes Datum laesst sich
auf eine Tagnummer ziehen und gegen das Kapitel legen, das diesen Tag erzaehlt.
Das ist der naechste Arbeitsgang und er ist begrenzt.

---

## 14. Die Kapitelaufteilung, gemessen

Grundlage ist dieselbe Tabelle. **Die Form des Buches ist ein Erzaehltag und
2000 bis 2900 Woerter**, und die grosse Mehrheit der 117 Kapitel sitzt darin.

### Zu gross

| Kapitel | W | Tage | Was daran auffaellt |
|---|---|---|---|
| **b2 ch35** | **8004** | 270, 273, 276 | **Drei Termine, je drei Tage auseinander.** Das groesste Kapitel des Buches, und die drei Tage sind keine Strecke, sondern drei Gelegenheiten |
| **b2 ch29** | 7558 | 243 bis 245 | Drei aufeinanderfolgende Tage, 2519 W je Tag |
| **b2 ch26** | 6850 | 237 bis 238 | Zwei aufeinanderfolgende, 3425 W je Tag |
| b2 ch48 | 4410 | 319 | Ein Tag |
| **b1 ch34** | 4341 | 91, 145, 149 | **58 Tage Spanne.** Das einzige Band-1-Kapitel mit diesem Sprung, und es ist das letzte |
| b1 ch15 | 4152 | 41 | Ein Tag |
| b1 ch21 | 4099 | 49 | Ein Tag |
| b2 ch32 | 4077 | 257, 259 | Zwei Tage |
| b2 ch25 | 3966 | 236 | Ein Tag |

### Zu klein

`b2 ch38` 1889 · `b1 ch20` 1909 (durch die Kuerzung vom 27.08.) · `b2 ch21`
1985 · `b1 ch29` 1992 · `b2 ch15` 2001 · `b2 ch59` 2002 · `b2 ch03` 2016.

Alle sieben liegen knapp unter der Spanne, keines dramatisch.

### Was ausdruecklich richtig ist

**Die mehrteiligen Einzeltage.** Der Galaabend ist **sechs Kapitel** auf Tag 22
(`ch06` bis `ch11`, zusammen 17.266 Woerter). Das Essen auf Tag 531 ist **drei**
(`ch79` bis `ch81`, 7131 Woerter). Das ist die Methode des Buches fuer einen
langen Abend, und sie ist besser als ein Kapitel von siebzehntausend Woertern.
Wer nach zu langen Kapiteln sucht, darf diese beiden Ketten nicht als Fund
zaehlen.

### Der eine Vorschlag

**`b2 ch35` teilen.** Es ist das groesste Kapitel des Buches, es liegt 450
Woerter ueber dem naechsten, und seine drei Tage liegen je drei Tage
auseinander. Drei Gelegenheiten in einem Kapitel ist die Bauform, die dieses
Buch sonst nirgends benutzt: `ch34` in Band 1 springt zwar weiter, aber das ist
ein Schlusskapitel und der Sprung ist die Aussage.

Alles andere ist Groesse und keine Aufteilung. **Entscheidung des Autors, nicht
meine.**

## 15. Der Szenentrenner, nachgemessen am 28.08.

Abschnitt 4 hatte das aus drei Lesegruppen geschaetzt. Jetzt gezaehlt, ueber
alle 117 Kanon-Dateien:

| Bereich | `* * *` je Kapitel, Median | Spanne |
|---|---|---|
| Band 1, ch01 bis ch34 | **2** | 0 bis 4 |
| Band 2, ch01 bis ch49 | **1** | 0 bis 6 |
| Band 2, ch50 bis ch83 | **17** | 0 bis 32 |

**Siebzehnmal so viele Szenentrenner in derselben Geschichte.** Spitze ist
`ch80` mit **32 Trennern auf 2115 Woerter**, also einer alle sechsundsechzig
Woerter, fuer ein einziges Gespraech.

### Der Mechanismus ist sichtbar

`ch53` bis `ch59` fuehren 14 bis 18 Szenentrenner und **null bis einen**
Beat-Trenner:

| | `* * *` | `---` |
|---|---|---|
| ch53 | 17 | 0 |
| ch54 | 15 | 1 |
| ch55 | 15 | 1 |
| ch56 | 15 | 1 |
| ch57 | 14 | 1 |
| ch58 | 18 | 0 |
| ch59 | 15 | 0 |

**Die beiden Zeichen sind dort vertauscht.** Nachgesehen in `ch53`: die
Trenner stehen mitten in einem durchlaufenden Gespraech, gleicher Raum,
gleiche zwei Maenner, gleicher Vormittag, kein Orts- und kein Zeitsprung. Das
ist die Stelle eines `---`.

Ab `ch60` steigen dann **beide** Zaehler (ch60: 21 und 27, ch61: 21 und 21),
das heisst der Trenner wird zusaetzlich gesetzt statt ersetzt.

### Was das fuer die Aufteilung heisst

Nicht die Kapitel sind falsch geschnitten, sondern **das Innere der spaeten
Band-2-Kapitel**. Ein Leser, der von `ch49` nach `ch53` geht, wechselt ohne
Vorwarnung von einem Kapitel mit einer Szene in ein Kapitel mit siebzehn
angeblichen.

**Nicht angefasst.** Das sind ueber dreihundert Zeichen in vierunddreissig
Kapiteln, und ob ein Trenner ein Schnitt oder ein Beat ist, entscheidet der
Autor und nicht ein Zaehler.

## 16. Die Trenner in ch53 bis ch59, richtiggestellt

**Autorenentscheid am 28.08.: Stundenluecken sind Schnitte.** Damit war die
Regel entscheidbar:

> `* * *` wechselt den Ort **oder** springt um Stunden.
> `---` alles andere.
> Ein `* * *` unmittelbar vor einer `## Day`-Zeile faellt ganz weg, weil die
> Datumszeile selbst der Schnitt ist.

**Jeder der 109 Trenner ist einzeln angesehen worden**, mit zwei Zeilen davor
und zwei danach. Die Entscheidung steht als Liste im Auftrag, nicht als
Faustregel im Code.

| Kapitel | vorher | bleibt | auf `---` | faellt weg |
|---|---|---|---|---|
| ch53 | 17 | 2 | 15 | 0 |
| ch54 | 15 | 1 | 12 | 2 |
| ch55 | 15 | 2 | 13 | 0 |
| ch56 | 15 | 1 | 13 | 1 |
| ch57 | 14 | 2 | 10 | 2 |
| ch58 | 18 | **5** | 13 | 0 |
| ch59 | 15 | 3 | 11 | 1 |

**Von 109 bleiben 16.** `ch58` behaelt fuenf, weil es das einzige der sieben
ist, in dem sich wirklich etwas bewegt: Anreise am Sonntag, Rueckblende auf den
Donnerstag in der Werkstatt, Ankunft am Haus, Ankunft am Fluss um elf nach
drei, der Abend um sechs.

### Gemessen davor und danach

| | `* * *` | Woerter je Block |
|---|---|---|
| ch53 bis ch59, vorher | 14 bis 18 | 113 bis 146 |
| ch53 bis ch59, nachher | **1 bis 5** | **111 bis 161** |
| Band 1 zum Vergleich | 0 bis 4, Median 2 | Median 215 |

`check.py`: 117 Kapitel, zwei Fehler (die Basislinien-Eintraege in `b1 ch06`
und `b1 ch12`), **keine neue Verschuldung**. Das Tagesregister meldet weiter
alle Datumszeilen sauber und keine Kollision, also haben die zwei geloeschten
Trenner vor Datumszeilen nichts an der Tageszaehlung verschoben.

### Eine Gegenprobe im Skript

Vor jedem Loeschen prueft der Auftrag nach, ob hinter dem Trenner wirklich eine
Datumszeile steht, und bricht sonst ab. Sechs Loeschungen, sechs bestaetigte
Datumszeilen.

### Was offen bleibt

**`ch60` bis `ch83` sind nicht angefasst.** Der Median in Band 2 ab Kapitel 50
ist damit von 17 auf 13 gefallen und nicht auf 2. Die schaerfsten stehen noch:
`ch80` mit **32** Trennern auf 2115 Woerter, `ch81` mit 30, `ch83` mit 29,
`ch79` mit 28. Bei diesen ist der Befund allerdings ein anderer als bei 53 bis
59: dort steigen **beide** Zaehler, der Trenner wird also zusaetzlich gesetzt
statt vertauscht. Das ist ein eigener Arbeitsgang.

## 17. Die Trenner in ch60 bis ch83

**Andere Fehlerklasse als in ch53 bis ch59.** Dort waren die zwei Zeichen
vertauscht: viele `* * *`, fast keine `---`. Hier wechseln sie sich ab, als
waeren es zwei Pausenstaerken. `ch80` fuehrt **32 Szenentrenner und 38
Beat-Trenner auf 2115 Woerter**, in *einem* Gespraech in *einem* kleinen Raum.
Keines der beiden Zeichen tut dort, wofuer es da ist.

**411 Trenner, jeder einzeln angesehen: 57 bleiben, 3 fallen weg, 351 werden
`---`.**

### Die Praezisierung, die dabei noetig wurde

**Minutenschritte sind keine Stundenluecken.** Das entscheidet `ch79`, das
Essen: der Abend laeuft von zwanzig vor acht ueber drei nach acht, halb neun,
viertel vor neun, neun, elf nach neun bis halb zehn. Sieben Uhrzeiten, jede
zehn bis fuenfundzwanzig Minuten nach der vorigen. **Das ist der Takt des
Kapitels und nicht sein Bau.** Alle sieben werden Beats; von 28 Trennern
bleiben drei: der Montag davor, das Eintreffen um zwanzig vor acht, und der
Gang aus dem Esszimmer in den Korridor.

### Wo viel bleibt, und warum

| Kapitel | vorher | bleibt | warum |
|---|---|---|---|
| `ch63` | 8 | **6** | Yeongjong. Terminal, Buero am Ende des Schuppens, Wagen, Bruecke, Halle, Studie. Ein echtes Reisekapitel |
| `ch61` | 21 | 5 | Ankunft von Moon Hae-sook ueber vier Tage |
| `ch77` | 22 | 5 | Zwei Erzaehltage, der Wagen um elf, der Freitag, der Montag |
| `ch76` | 19 | 4 | Halb fuenf, sieben Uhr, Woos Haus, der Wagen |
| `ch60` | 21 | 4 | Studie, sechs Uhr, Abend |
| `ch70` | 18 | 4 | Werkstatt, Laden, Buergersteig, Studie |

### Wo fast nichts bleibt

`ch80` behaelt **einen von 32**: den Schritt aus dem Zimmer. `ch73` einen von
21. `ch82` einen von 24. `ch68` einen von 13. Das sind Kapitel, die aus einem
einzigen Gespraech bestehen, und ein Gespraech hat keine Szenenwechsel.

### Gemessen

| | `* * *` Median | Spanne |
|---|---|---|
| Band 1 | 2 | 0 bis 4 |
| Band 2 ch01 bis ch49 | 1 | 0 bis 6 |
| Band 2 ch50 bis ch83, **vorher** | **17** | 0 bis 32 |
| Band 2 ch50 bis ch83, **nachher** | **2** | 0 bis 11 |

`check.py`: 117 Kapitel, zwei Fehler (die Basislinien-Eintraege), **keine neue
Verschuldung**. Das Tagesregister meldet weiter alle Datumszeilen sauber und
keine Kollision, die drei geloeschten Trenner vor Datumszeilen haben also an
der Tageszaehlung nichts verschoben.

### Nicht angefasst

`ch65` (0 Trenner), `ch71` (3) und `ch72` (2) waren schon in Ordnung. Ausserhalb
des Auftrags liegen `ch50` (11) und `ch52` (10); das sind die zwei letzten
ueber der Spanne.

**Und die groessere Frage bleibt offen:** die Zahl der Trenner *insgesamt*.
`ch80` hat jetzt 69 Beat-Trenner auf 2115 Woerter, also einen alle dreissig
Woerter. Die Zeichen bedeuten wieder, was sie sollen, aber ob ein Kapitel so
viele Pausen braucht, ist eine Rhythmusfrage und keine Zeichenfrage. **Nicht
entschieden.**

## 18. Korrektur zu Abschnitt 17: `ch80` und `ch83` sind zurueckgenommen

**Autorenhinweis am 28.08.: *"Baue das so, wie es passt zum Kapitel, erzwinge
nix wegen einer Regel."*** Dazu vorher: *"Kapitel 80 kann wirklich ein
pacebreaker sein, das letzte Kapitel ist immer anders und ueberall."*

Beides ist berechtigt und beides trifft einen Fehler, den ich gemacht habe.

### Was falsch war

**Die Regel kannte zwei Arten von Schnitt, das Buch hat drei.** Ort und Zeit
standen im Auftrag. **Themenwechsel stand nicht drin.**

`ch83` ist ein einziger Erzaehltag, an dem eine Bilanz gezogen wird, und die
`* * *` trennen dort **verschiedene Faeden**: Baeks Papierspur, dann Sang-hoon
und Woo, dann der Zeitraum, dann der Raum in Cheongdam. Andere Leute, andere
Orte, ohne dass sich Uhrzeit oder Schauplatz der Erzaehlung ruehren. `---` sind
die Beats innerhalb jedes Fadens. **Das Kapitel benutzte beide Zeichen
richtig**, und die Umstellung hat 27 von 29 Markern zerstoert.

`ch80` ist der andere Fall: dort trennen die `* * *` tatsaechlich nichts, aber
der Wechsel der beiden Zeichen ist ein Tempomittel im Hoehepunktgespraech. Der
Autor sagt, das darf so sein.

**Beide Dateien sind geloescht, `ch80_v3_2` und `ch83_v3_2` sind wieder Kanon.**

### Die anderen halten, und jetzt weiss ich auch warum

Gegenprobe an den Kapiteln, in denen am wenigsten uebrigblieb:

| Kapitel | Datumszeilen | `* * *` danach | Bau |
|---|---|---|---|
| `ch64` | 2 | 1 | Sim und Mr Ok sind durch die Datumszeile getrennt |
| `ch66` | 3 | 1 | Annie, dann Mrs Has Zimmer nach der dritten Zeile |
| `ch70` | 4 | 4 | vier Tage, vier Gaenge |
| `ch73` | 2 | 1 | Sim am Montag, Sang-hoon am Dienstag |
| `ch82` | 4 | 1 | vier Besuche an vier Tagen |

**Dort machen die Datumszeilen die Szenentrennung.** Deshalb bleibt so wenig
uebrig, und deshalb ist es richtig. `ch83` war die Ausnahme, weil es an einem
Tag spielt und `* * *` das einzige verfuegbare Werkzeug war.

### Was daraus in `20-handwerk.md` steht

Der Szenentrenner hat jetzt **drei** Faelle statt zwei, und darueber der Satz,
der fehlte: **ein Kapitel wird gebaut, wie es zu ihm passt.** Die Regeln
beschreiben den Normalfall, sie erzwingen ihn nicht.

**Und die Probe, die ich nicht gemacht habe:** erst nachsehen, ob ein Kapitel
die zwei Zeichen **richtig** benutzt, bevor man zaehlt, wie viele es hat. Eine
hohe Zahl ist ein Anlass zum Hinsehen und kein Ergebnis. Genau davor warnt
`CLAUDE.md` seit Langem, an anderer Stelle: *Berichte werden nicht abgenommen.*
Eine Messung ist auch ein Bericht.

## 19. Nachpruefung aller achtundzwanzig, auf Fall 3

**Nicht achtzehn, achtundzwanzig.** Sieben aus dem ersten Durchgang (ch53 bis
ch59), neunzehn aus dem zweiten (ch60 bis ch82), zwei nachgereicht (ch50, ch52).

Jeder umgestellte Trenner noch einmal angesehen, diesmal mit **beiden** Seiten:
die letzte Zeile davor und die erste danach, gelesen aus den Fassungen vor dem
Eingriff. Ein Themenwechsel ist nur an beiden Seiten zu erkennen, und genau
deshalb hat der erste Durchgang ihn nicht gesehen: er hat nur nach vorn
geschaut.

### Ergebnis

| | Kapitel |
|---|---|
| **Ganz zurueckgenommen** | `ch61`, `ch79`, `ch80`, `ch81`, `ch83` |
| **Teilweise korrigiert** | `ch62`, `ch73` |
| **Bleiben, wie umgestellt** | die uebrigen 21 |

### Die Klasse, die dabei sichtbar wurde: das Montage-Kapitel

**Jedes der betroffenen Kapitel setzt zusammen, statt zu erzaehlen.** Das ist
keine Ausnahme, sondern eine eigene Bauform, und in ihr ist `* * *` das einzige
verfuegbare Werkzeug, weil sich weder Ort noch Uhrzeit ruehren:

- `ch83` die Bilanz: Baeks Papierspur, Sang-hoon und Woo, der Zeitraum, der
  Raum in Cheongdam.
- `ch61` die Ankunft: die Fahrt, die Flaschen, was sie mitbrachte, das Zimmer,
  wer sie ist, der Haushalt, Annie.
- `ch81` die Abgaenge: Mr Koh um zehn nach zehn, Sang-hoon um elf, die vier
  Spaeten um viertel nach, Nam Byung-hee um zwanzig nach. Vier Menschen, vier
  Absaetze.
- `ch79` das Essen: ein Abend, quer durch einen Raum gesehen, aus wechselnden
  Blickwinkeln.
- `ch73` der Katalog **K.**, **S.**, **H.**: drei Vorfaelle mit eigenen Daten,
  Orten und Menschen.
- `ch62` die Lieferung: der Fahrer, dann sie, dann die sechsunddreissig Tage,
  dann die Kontonummer.

`ch80` ist der siebte und ein anderer Fall: dort trennen die `* * *` nichts,
aber der Wechsel der beiden Zeichen bricht absichtlich das Tempo. **Autorenentscheid.**

### Die zwei Teilkorrekturen

`ch62` behaelt jetzt sechs von neun: die drei des Anfangsmosaiks kommen zu den
drei zurueck, die schon standen. Nur die drei im Annie-Gespraech sind Beats.

`ch73` behaelt vier von einundzwanzig: die drei Katalogblocke und den Wagen am
Schluss.

### Was von der Arbeit uebrig bleibt

Einundzwanzig Kapitel bleiben umgestellt, und die Gegenprobe dafuer steht in
Abschnitt 18: dort machen **Datumszeilen** die Szenentrennung, und die Kapitel
sind Gespraeche und keine Montagen.

`check.py`: 117 Kapitel, zwei Fehler (die Basislinien-Eintraege), keine neue
Verschuldung.

### Die Lehre, in einem Satz

**Bevor man zaehlt, wie viele Trenner ein Kapitel hat, sieht man nach, wozu es
sie benutzt.** Eine hohe Zahl ist ein Anlass zum Hinsehen und kein Befund, und
eine Messung ist auch nur ein Bericht.

## 20. Der Datumsdurchgang, 28.08.

`werkzeug/datumsprobe.py`, gegen `werkzeug/register.py`.

### Was gemessen wurde

**377 ausdrueckliche Datumsangaben** (Tag plus Monat) im Fliesstext beider
Baende, jede auf eine Tagnummer gezogen und im Register nachgeschlagen:

| | |
|---|---|
| **235** | zeigen auf einen Tag, den das Register kennt |
| **142** | zeigen auf einen Tag, den das Buch nicht erzaehlt: Ereignisse neben der Buehne |
| **5** | Rueckblick auf einen Monatstag, den es vorher im Fenster nicht gibt |

### Der Befund, der wehtut

**Die Hauptpruefung ist strukturell nicht ausloesbar, und die Gegenprobe hat es
aufgedeckt, bevor ich eine Null als Entwarnung gemeldet habe.**

Gesucht war der Rest jeder Umdatierung: ein Kapitel blickt auf ein Datum
zurueck, das ein **spaeteres** Kapitel erzaehlt. Das kann nur eintreten, wenn
die Kapitel nicht in Tagesreihenfolge stehen. **Sie stehen aber in
Tagesreihenfolge, alle 117, ohne eine einzige Ausnahme** - eigens nachgemessen.
Ein Rueckblick loest also immer auf ein frueheres Kapitel auf, und die Null
bedeutet nichts.

Das Skript sagt das jetzt selbst, in der ersten Zeile seiner Ausgabe, und die
Warnung steht oben im Kopf der Datei. **Die Pruefung wird scharf, sobald ein
Kapitel umdatiert wird** - also genau dann, wenn sie gebraucht wird. Bis dahin
ist ihr Wert, dass sie die Chronologie bewacht.

### Die fuenf von Hand

Alle fuenf angesehen, alle in Ordnung:

- `b1 ch19:226`, `ch19:230` und `b1 ch20:134`, dreimal **der siebzehnte
  September**: Woos zwei Besucher, die vor Tag 1 kamen. Vorgeschichte.
  **Und `ch19:226` behauptet, es sei ein Mittwoch gewesen. Der 17. September
  2025 war ein Mittwoch.** Nachgerechnet und richtig.
- `b2 ch07:186` *"Then on the first of April she writes again"*: vorwaerts und
  gewohnheitsmaessig, sie schreibt jedes Jahr am ersten April.
- `b2 ch51:286` *"I said I would telephone on the fourteenth of September"*:
  vorwaerts.

### Was der Durchgang NICHT geleistet hat

**Die 235 entscheidbaren Stellen sind nicht inhaltlich geprueft.** Das Register
sagt, welches Kapitel den genannten Tag erzaehlt; ob die Behauptung an dem
Datum zu dem passt, was dort steht, sagt es nicht. Das sind 235 Einzelurteile,
und sie sind jetzt **adressierbar**, weil zu jedem die Fundstelle und das
Zielkapitel feststehen. Vorher waren sie es nicht.

**Das ist der Unterschied zwischen "es ist pruefbar geworden" und "es ist
geprueft".** Der erste Schritt ist getan.

### Dritter stiller Lauf an einem Tag

Heute sind drei Pruefungen von mir daran gescheitert, dass sie nichts ansehen
konnten: die Wochentagsprobe (zielte auf 2 von 3051 Angaben), die
Datumsaufloesung in beide Richtungen (loeste alles irgendwo auf), und jetzt
diese. **Jede davon haette "kein Widerspruch" gemeldet.** Gefunden hat sie die
Gegenprobe, jedes Mal.

`CLAUDE.md` sagt: *Ein stiller Lauf beweist nichts.* Der Satz ist an einem Tag
dreimal eingetreten.

---

## 21. `b2 ch35` teilen: die Antwort ist thematisch, nicht metrisch

Gemessen, statt vermutet:

| Erzaehltag | Was | Woerter |
|---|---|---|
| Tag 270, Dienstag 30. Juni | Sang-hoon an einem Tisch statt in einem Raum | **3307** |
| Tag 273, Freitag 3. Juli | Jangs Anruf um halb eins, dann derselbe Tisch | **2406** |
| Tag 276, Montag 6. Juli | Annie um sieben, danach das Lesen bis drei Uhr morgens | **2275** |

**Drei Gelegenheiten, je drei Tage auseinander, jede mit eigenem Bogen.** Das
ist keine Szene, die zu lang geraten ist, sondern **drei Kapitel, die als eines
abgelegt wurden.**

Und die Wortzahlen entscheiden es mit: **alle drei liegen bereits einzeln in
der Spanne** des Buches (2000 bis 4300 bei einem Erzaehltag). Nach der Teilung
braucht kein Wort geschrieben und keines gestrichen zu werden.

**Entscheidung des Autors.**

## 22. `b2 ch35` geteilt, 28.08.

**Band 2 hat jetzt fuenfundachtzig Kapitel.**

| neu | Titel | Tag | Woerter |
|---|---|---|---|
| `ch35` v4.0 | *Built once, used twice* | 270, Di 30. Juni | 3321 |
| `ch36` v4.0 | *Two anchors* | 273, Fr 3. Juli | 2415 |
| `ch37` v4.0 | *Somebody in Seoul pays for it* | 276, Mo 6. Juli | 2291 |

Alt `ch36` bis `ch83` sind auf `ch38` bis `ch85` gerueckt, **alle 106 Dateien
mit allen Fassungen**, Dateiname und Kopfzeile zusammen. Nur die hoechste zu
verschieben haette eine Altfassung von `ch36` zum Kanon von `ch36` gemacht,
waehrend der Text nach `ch38` gewandert waere.

**Am Text ist nichts geaendert worden.** 3321 + 2415 + 2291 = 8027 gegen 8004
vorher; die Differenz sind die zwei zusaetzlichen Kopf- und Fassungszeilen
minus der eine Trenner, der beim Teilen an ein Kapitelende gefallen waere.

**Die Titel** stehen alle drei im eigenen Text. Der bisherige, *Somebody in
Seoul pays for it*, gehoert zu Teil 3: der Satz steht dort (alt Zeile 689).

### Geprueft danach

- Tagesregister: **145 Erzaehltage unveraendert**, alle Datumszeilen sauber,
  kein Tag in zwei nicht benachbarten Kapiteln.
- `check.py`: 119 Kapitel, zwei Fehler (die Basislinien-Eintraege in `b1 ch06`
  und `b1 ch12`), keine neue Verschuldung.
- `.check-baseline` neu gebaut: Band 2 jetzt ueber alle 85 Kapitel, weiterhin
  ueberall 0. Damit sind auch die 38 Warnungen *"steht nicht in der Basislinie"*
  weg, die seit dem 27.08. liefen.
- `build.py` laeuft durch.

### Und der Teil, der NICHT erledigt ist

**Die Kapitelverweise in `doc/` sind nicht nachgezogen.** Rund 1100 Stellen
nennen eine Kapitelnummer, die meisten ohne Bandangabe.

Beim Suchen ist dabei etwas Aelteres aufgefallen: in `15-kalender.md` und
`40-verworfen.md` stehen **Kapitel 87, 88 und 90**. Die hat Band 2 auch vor dem
28.08. nicht gehabt. **Die Umnummerierung vom 27.08. ist ebenfalls nie in die
Dokumente gelaufen.** Die Verweise tragen also bereits einen Versatz, und ein
pauschales Plus-Zwei wuerde die falschen Stellen mitverschieben.

**Darum nichts angefasst.** Stattdessen steht oben in `15-kalender.md` eine
Warnung mit einer Lesetabelle, und die eigentliche Arbeit gehoert zu
`archiv/VERWEISE-OFFEN.md`.

**Was nicht driften kann, sind `erzeugt/KAPITEL.md` und `erzeugt/REGISTER.md`.**
Beide werden aus den Kapitelkoepfen erzeugt. Wer eine Kapitelnummer braucht,
nimmt sie von dort und nicht aus einem Dokument.
