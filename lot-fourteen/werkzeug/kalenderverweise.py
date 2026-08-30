# -*- coding: utf-8 -*-
u"""Prueft die Kapitelverweise in `doc/15-kalender.md` gegen die Kapitel selbst.

**Warum es das gibt.** Am 30.08. hat der Autor gefragt, ob der Abstand zwischen
Vernichtung und Abendessen Absicht sei. Die Antwort stand im Kalender, aber
**sechs von sieben Kapitelverweisen in derselben Tabelle waren falsch** - alle
um vier verschoben, aus einer Umnummerierung, die niemand nachgezogen hatte.
Der Kalender selbst hatte recht, und trotzdem zeigte er ins Leere.

**Was es prueft, und es ist Form und nicht Bedeutung.** Jede Zeile, die mit
einer Erzaehltagszahl anfaengt und ein Kapitel nennt: haelt dieses Kapitel
diesen Tag? Es liest die Tage aus den `## Day ...`-Ueberschriften der jeweils
hoechsten Fassung und rechnet die englischen Zahlwoerter aus.

**Es eicht sich zuerst selbst.** Wenn *kein einziger* Verweis stimmt, ist nicht
der Kalender kaputt, sondern der Leser - dann bricht es ab und meldet gar
nichts. Das ist die Lehre aus `zuschreibung.py`.

**Was es nicht prueft:** Quellenangaben in Klammern wie
``(`b2 ch12`: *"The eighteenth of March."*)``. Die nennen, woher ein Zitat
kommt, und behaupten nichts ueber den Tag der Zeile.

    python3 werkzeug/kalenderverweise.py

Rueckgabewert 1, solange ein Verweis falsch ist.
"""
import io
import os
import re
import sys
import glob

HIER = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(HIER))

WORT = {u'zero': 0, u'one': 1, u'two': 2, u'three': 3, u'four': 4, u'five': 5,
        u'six': 6, u'seven': 7, u'eight': 8, u'nine': 9, u'ten': 10,
        u'eleven': 11, u'twelve': 12, u'thirteen': 13, u'fourteen': 14,
        u'fifteen': 15, u'sixteen': 16, u'seventeen': 17, u'eighteen': 18,
        u'nineteen': 19, u'twenty': 20, u'thirty': 30, u'forty': 40,
        u'fifty': 50, u'sixty': 60, u'seventy': 70, u'eighty': 80,
        u'ninety': 90, u'hundred': 100}


def zahl(s):
    u"""Five Hundred and Thirty-One -> 531."""
    n = 0
    for w in re.split(u'[\\s-]+', s.lower().replace(u'and', u' ')):
        if w in WORT:
            v = WORT[w]
            n = (n or 1) * 100 if v == 100 else n + v
    return n


def kanon():
    u"""Kapitelnummer -> Menge der Erzaehltage darin, je Band."""
    aus = {}
    for band, ordner in ((1, u'chapters'), (2, u'chapters-2'), (3, u'chapters-3')):
        hoechste = {}
        for f in glob.glob(os.path.join(ordner, u'ch*_en.md')):
            m = re.search(u'ch(\\d+)_v(\\d+)_(\\d+)_en\\.md$', f.replace(u'\\', u'/'))
            if not m:
                continue
            k, v = int(m.group(1)), (int(m.group(2)), int(m.group(3)))
            if k not in hoechste or v > hoechste[k][0]:
                hoechste[k] = (v, f)
        for k, (v, f) in hoechste.items():
            d = io.open(f, encoding='utf-8').read()
            aus[(band, k)] = set(
                zahl(m) for m in re.findall(u'^## Day ([A-Za-z \\-]+?) ·', d, re.M))
    return aus


def main():
    tage = kanon()
    z = io.open(u'doc/15-kalender.md', encoding='utf-8').read().split(u'\n')

    treffer, fehler = 0, []
    for l in z:
        m = re.match(u'\\|\\s*(\\d+)\\s*\\|', l)
        if not m:
            continue
        tag = int(m.group(1))
        for vor, bd, km in re.findall(u'(.?)`(?:b(\\d) )?ch(\\d+)`', l):
            if vor == u'(':
                continue                      # Quellenangabe, kein Tagesanspruch
            band = int(bd) if bd else 2
            k = int(km)
            if (band, k) in tage and tag in tage[(band, k)]:
                treffer += 1
            else:
                wo = [u'b%d ch%d' % (b, kk) for (b, kk) in sorted(tage)
                      if tag in tage[(b, kk)]]
                fehler.append((tag, band, k, u'/'.join(wo) or u'keinem Kapitel'))

    geprueft = treffer + len(fehler)
    if geprueft and not treffer:
        print(u'EICHUNG DURCHGEFALLEN: kein einziger Verweis stimmt.')
        print(u'Das ist kein Kalenderfehler, das ist ein Lesefehler. Nichts gemeldet.')
        return 2

    print(u'%d Verweise mit Tagesangabe geprueft, %d stimmen.' % (geprueft, treffer))
    for tag, band, k, wo in fehler:
        print(u'  Tag %-4d nennt b%d ch%-3d - Tag steht in %s' % (tag, band, k, wo))
    if fehler:
        print(u'%d falsch.' % len(fehler))
        return 1
    print(u'Kein Verweis zeigt ins Leere.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
