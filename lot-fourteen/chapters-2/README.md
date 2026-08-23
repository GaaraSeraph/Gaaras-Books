# Band 2

Hier liegen die Kapitel des zweiten Bandes, und sie fangen wieder bei **01** an.

**Die Bandnummer steht in keiner Kapiteldatei.** Sie kommt aus dem Ordner, in
dem die Datei liegt, und wird von `build.py` in die Titelzeile geschrieben:

    chapters-2/ch01_v1_0_en.md
    # Chapter 1: ...              <- so steht es in der Datei
    # Book Two . Chapter 1: ...   <- so steht es in book.md, paste/ und read/

**Warum nicht in die Datei.** Sonst muessten vierunddreissig Kapitel des ersten
Bandes eine Fassung hochsetzen, damit oben ein Wort mehr steht - und die
Bandnummer koennte gegen den Ordner driften, in dem die Datei tatsaechlich
liegt. Was abgeleitet werden kann, wird abgeleitet.

Alles andere gilt unveraendert: Dateiname und Kopfzeile tragen dieselbe Fassung,
`build.py` nimmt je Kapitel die hoechste und bricht bei Abweichung ab.

Der Kalender laeuft weiter. Band 1 endet an **Tag 149, Sonntag 1. Maerz**;
Band 2 faengt an **Tag 150, Montag 2. Maerz** an, und `check.py` rechnet die
Datumszeilen ueber die Bandgrenze hinweg nach.
