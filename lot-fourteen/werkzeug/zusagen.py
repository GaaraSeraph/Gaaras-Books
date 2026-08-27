#!/usr/bin/env python3
"""zusagen.py - haelt fest, was im Text versprochen wurde, und was davon offen ist.

Zwei Zusagen sind in dieser Sitzung als ueberfaellig gefunden worden, beide
von Hand, beide Monate zu spaet: die fuenf Firmen aus Kapitel 12 (vier Monate
erzaehlte Zeit) und Annies "You will in about a month" aus Kapitel 5 (sechs
Monate). Beide standen im Text und in keiner Liste.

**Das Prinzip ist dasselbe wie ueberall hier: was geprueft wird, stimmt.
Was nicht geprueft wird, driftet.** Also wird es geprueft.

    python3 zusagen.py              Stand: ueberfaellig, offen, bezahlt
    python3 zusagen.py --neu        Zusagen im Text, die im Buch fehlen
    python3 zusagen.py --alle       auch die bezahlten einzeln

**Jede Zusage ist entweder zeitgebunden oder ereignisgebunden**, und `faellig
offen` gibt es nicht mehr. Eine Zusage ohne genannte Frist hat trotzdem einen
Ausloeser - *wenn sie herauskommt*, *wenn es vorbei ist*, *wenn er den Namen hat* -
und wer den nicht hinschreibt, kann spaeter nicht pruefen, ob er eingetreten ist.
`faellig bei <Ereignis>` ist die Form dafuer, und wer keins von beidem hinschreibt,
wird gemeldet.

Vier Zustaende: OFFEN, BEZAHLT, VERFALLEN und KEINE. **KEINE ist der wichtigste
von den vieren**, weil `--neu` sonst dieselben dreizehn Fundstellen bis in alle
Ewigkeit meldet und man nach der zweiten Woche aufhoert hinzusehen. Was einmal
geprueft und als Nichtzusage befunden wurde, steht mit Begruendung im Buch und
kommt nicht wieder.

**Und die Warnung, die am 27.08. dazugekommen ist, weil der Fall eingetreten
ist:** eine ueberfaellige Zusage ist ein **Befund und keine Anweisung**. Am
25.08. wurde die Zusage ueber die fuenf Firmen aus B2 12 als ueberfaellig
gemeldet, und bezahlt wurde sie, indem Szenen geschrieben wurden, in denen der
Anspruch erlassen wird. Der Kauf, den B2 20 mit Datum ankuendigt, ist nie
erzaehlt worden. **Wer eine Zeile gruen macht, indem er das Vermoegen
abschreibt, hat das Werkzeug gegen das Buch benutzt.** Siehe `doc/31-plan-band-2.md`.

Das Buch ist `doc/13-zusagen.md` und wird von Hand gefuehrt. Das Skript
entscheidet **nicht**, ob etwas eine Zusage ist - das ist Urteil. Es rechnet
Faelligkeiten gegen den Erzaehlkalender und meldet, was im Text steht und im
Buch fehlt.

**Die Grenze, und sie ist dieselbe wie bei stimmen.py:** `--neu` findet nur
Zusagen mit einer Zeitangabe im selben Satz. Eine Zusage ohne Frist
("I will have him") faellt durch und muss von Hand eingetragen werden. Ein
Detektor, der jeden Satz mit "I will" meldet, ist nach Regel 8 aus
doc/22-pruefen.md wertlos, und diese Fassung meldet lieber zu wenig.
"""
import os
import re
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUCH = os.path.join(WURZEL, "doc", "13-zusagen.md")

ZEILE = re.compile(
    r"^- \[(OFFEN|BEZAHLT|VERFALLEN|KEINE)\]\s+\*\*(B[12]) (\d+)\*\*\s+(.+?)\s+·\s+"
    r"gesagt Tag (\d+)\s+·\s+faellig (Tag (\d+)|bei (.+?)|offen)\s+·\s+(.+?)\s+·\s+(.+?)\s*$")

ZUSAGE = re.compile(r"\b(I will|I am going to|you will|I shall|I promise)\b")
FRIST = re.compile(
    r"\b(in about (a|two|three|four|six|eight) (day|days|week|weeks|month|months)"
    r"|by (Christmas|the end of|Friday|Monday|Tuesday|Wednesday|Thursday|Sunday)"
    r"|next (week|month|year|spring|autumn)"
    r"|on the (first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth"
    r"|eleventh|twelfth|thirteenth|fourteenth|twentieth)"
    r"|when (it|this) is over|before (Christmas|the end)"
    r"|within a (week|month|fortnight)|inside a (week|month|fortnight|year))\b", re.I)
ZITAT = re.compile(r'"([^"]{20,})"')


def kapitel():
    """Aktuelle Fassung jedes Kapitels, mit Band, Nummer und Tag."""
    aus = []
    for ordner, band in (("chapters", "B1"), ("chapters-2", "B2")):
        pfad = os.path.join(WURZEL, ordner)
        if not os.path.isdir(pfad):
            continue
        neuste = {}
        for name in sorted(os.listdir(pfad)):
            m = re.match(r"ch(\d\d)_v\d+_\d+_en\.md$", name)
            if m:
                neuste[int(m.group(1))] = name
        for num in sorted(neuste):
            with open(os.path.join(pfad, neuste[num]), encoding="utf-8") as f:
                text = f.read()
            tage = [int(t) for t in re.findall(r"Day (\d+) ·", text)]
            tage.append(_wort_zu_tag(text))
            tage = [t for t in tage if t]
            # Kapitel ohne Datumszeile gibt es in Band 1; sie bekommen Tag 0
            # und fallen aus der Erzaehlstandsrechnung heraus.
            aus.append((band, num, neuste[num], text, max(tage) if tage else 0))
    return aus


ZAHLWORT = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,
    "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
    "hundred": 100,
}


def _wort_zu_tag(text):
    """## Day Three Hundred and Forty-One · ... -> 341"""
    best = 0
    for m in re.finditer(r"## Days? ([A-Za-z\- ]+?) ·", text):
        wort = m.group(1).lower().replace("-", " ").replace(" and ", " ")
        wert, teil = 0, 0
        for w in wort.split():
            if w not in ZAHLWORT:
                continue
            z = ZAHLWORT[w]
            if z == 100:
                teil = max(teil, 1) * 100
            else:
                teil += z
        wert = teil
        best = max(best, wert)
    return best


def lies_buch():
    if not os.path.exists(BUCH):
        return [], "Es gibt kein doc/13-zusagen.md."
    eintraege = []
    im_block = False
    with open(BUCH, encoding="utf-8") as f:
        for i, zeile in enumerate(f, 1):
            # Das Formatbeispiel steht in einem Codeblock und ist keine Zusage.
            if zeile.startswith("```"):
                im_block = not im_block
                continue
            if im_block:
                continue
            m = ZEILE.match(zeile.rstrip())
            if m:
                eintraege.append({
                    "zeile": i, "status": m.group(1), "band": m.group(2),
                    "kap": int(m.group(3)), "wer": m.group(4),
                    "gesagt": int(m.group(5)),
                    "faellig": int(m.group(7)) if m.group(7) else None,
                    "ereignis": m.group(8),
                    "zitat": m.group(9).strip('*" '), "eingeloest": m.group(10),
                })
    return eintraege, None


def stand(alle=False):
    eintraege, fehler = lies_buch()
    if fehler:
        print(fehler)
        return 1
    kaps = kapitel()
    heute = max(k[4] for k in kaps) if kaps else 0
    letzte = [k for k in kaps if k[4] == heute]
    print(f"Erzaehlstand: Tag {heute} "
          f"({letzte[-1][0]} Kapitel {letzte[-1][1]})\n")

    ueberfaellig, offen, bezahlt, ereignis, ohne = [], [], [], [], []
    verfallen = []
    for e in eintraege:
        if e["status"] == "KEINE":
            continue
        # Eine gebrochene Zusage, die der Text kennt, ist ein Zustand und kein
        # offener Posten. Bis zum 25.08. lief sie in die Faelligkeitsrechnung
        # und stand am Bandende als ueberfaellig da, obwohl sie erledigt ist.
        if e["status"] == "VERFALLEN":
            verfallen.append(e)
        elif e["status"] == "BEZAHLT":
            bezahlt.append(e)
        elif e["faellig"] and e["faellig"] < heute:
            ueberfaellig.append(e)
        elif e["faellig"]:
            offen.append(e)
        elif e.get("ereignis"):
            ereignis.append(e)
        else:
            ohne.append(e)

    if ueberfaellig:
        print(f"UEBERFAELLIG ({len(ueberfaellig)})")
        for e in sorted(ueberfaellig, key=lambda x: x["faellig"]):
            tage = heute - e["faellig"]
            print(f"  {e['band']} {e['kap']:2d}  {tage:4d} Tage  {e['wer']}")
            print(f"          \"{e['zitat'][:96]}\"")
        print()

    if offen:
        print(f"OFFEN, ZEITGEBUNDEN ({len(offen)})")
        for e in sorted(offen, key=lambda x: x["faellig"]):
            wann = f"Tag {e['faellig']}, in {e['faellig'] - heute}"
            print(f"  {e['band']} {e['kap']:2d}  {wann:20s} {e['wer']}")
        print()

    if ereignis:
        print(f"OFFEN, EREIGNISGEBUNDEN ({len(ereignis)})")
        for e in sorted(ereignis, key=lambda x: x["ereignis"]):
            print(f"  {e['band']} {e['kap']:2d}  bei {e['ereignis']}")
            print(f"          {e['wer']}")
        print()

    # Eine Zusage ohne Tag und ohne Ereignis kann nie geprueft werden. Das ist
    # kein offener Faden, sondern ein unsichtbarer, und deshalb ist es ein Fehler.
    if ohne:
        print(f"OHNE FAELLIGKEIT ({len(ohne)}) - weder Tag noch Ereignis. "
              f"Jede davon bekommt eins oder wird geloescht.")
        for e in ohne:
            print(f"  Zeile {e['zeile']:4d}  {e['band']} {e['kap']:2d}  {e['wer']}")
        print()

    if verfallen:
        print(f"VERFALLEN ({len(verfallen)}) - gebrochen, und der Text weiss es")
        for e in verfallen:
            print(f"  {e['band']} {e['kap']:2d}  {e['wer']}")
            print(f"          \"{e['zitat'][:96]}\"")
        print()

    print(f"BEZAHLT ({len(bezahlt)})")
    if alle:
        for e in bezahlt:
            print(f"  {e['band']} {e['kap']:2d}  {e['wer']} -> {e['eingeloest']}")
    return 1 if (ueberfaellig or ohne) else 0


def neu():
    """Zusagen mit Frist, die im Buch nicht vorkommen."""
    eintraege, _ = lies_buch()
    bekannt = [e["zitat"][:40].lower() for e in eintraege]
    gefunden = 0
    for band, num, name, text, tag in kapitel():
        for zeile in text.split("\n"):
            for s in ZITAT.findall(zeile):
                if not (ZUSAGE.search(s) and FRIST.search(s)):
                    continue
                if any(k and k in s.lower() for k in bekannt):
                    continue
                gefunden += 1
                print(f"  {band} {num:2d} (Tag {tag})  \"{s[:110]}\"")
    if not gefunden:
        print("Keine Zusage mit Frist, die im Buch fehlt.")
    else:
        print(f"\n{gefunden} nicht im Buch. Eintragen oder begruenden, "
              f"warum es keine Zusage ist.")
    return 0


if __name__ == "__main__":
    if "--neu" in sys.argv:
        sys.exit(neu())
    sys.exit(stand("--alle" in sys.argv))
