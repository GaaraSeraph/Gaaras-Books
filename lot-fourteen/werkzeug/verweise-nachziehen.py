# -*- coding: utf-8 -*-
"""Die Kapitelverweise in doc/ auf die Nummerierung vom 27.08. ziehen.

Band 2 ist an dem Tag von 82 Kapiteln mit Nummern bis 90 auf 83 Kapitel mit
Nummern 1 bis 83 umgestellt worden. Die Zuordnung steht in
archiv/UMNUMMERIERUNG.md und wird hier aus werkzeug/umnummerieren.py gelesen,
damit es nur eine Quelle gibt.

Angefasst wird nur, was beweisbar Band 2 ist:
  - "b2 KNN" traegt das Band im Verweis.
  - blankes "KNN" mit NN groesser als 34 kann nicht Band 1 sein, weil Band 1
    vierunddreissig Kapitel hat. Es wird dabei auf "b2 KNN" normalisiert,
    damit dieselbe Frage nicht ein zweites Mal gestellt werden muss.
  - "Band 2, Kapitel N" im Fliesstext.

Nicht angefasst:
  - "b1 KNN" und "Band 1, Kapitel N".
  - blankes "KNN" bis 34. Das kann beides sein. Diese Stellen stehen in
    archiv/VERWEISE-OFFEN.md und brauchen ein Auge.
  - **doc/protokoll/ als Ganzes.** Ein Protokoll ist ein Bericht von einem
    Tag. Wer die Zahlen darin nachzieht, faelscht den Bericht. Die Regel steht
    in doc/protokoll/LIESMICH.md, und dort steht seit dem 27.08. auch, dass
    Kapitelnummern in Protokollen vor der Umstellung gelesen werden muessen.

Drei Sorten Verweis bekommen kein neues Ziel, sondern ein "alt" davor:
  - die neun gestrichenen Kapitel 69 bis 77. Ihre alten Nummern gehoeren jetzt
    anderen Kapiteln, ein stehengelassenes K72 fuehrte also in den falschen
    Text. Das ist der Grund, warum hier markiert und nicht ignoriert wird.
  - die zwei geteilten: das alte 67 steckt in 66 und 68, das alte 90 in
    69, 73 und 83. Welche Haelfte gemeint ist, entscheidet der Satz.
  - was in keiner Liste steht.
"""
import io
import os
import re
import glob

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERSETZT = {57: 63, 61: 71, 62: 72, 65: 65, 66: 66, 88: 80, 89: 61, 78: 76}
GETEILT = {67, 90}
WEG = set(range(69, 78))

src = io.open(os.path.join(WURZEL, 'werkzeug', 'umnummerieren.py'),
              encoding='utf-8').read()
ns = {'__file__': os.path.join(WURZEL, 'werkzeug', 'umnummerieren.py')}
exec(compile(src.split('KOPF = re.compile')[0].replace('if os.path.isdir(NEU)', 'if False'),
             'plan', 'exec'), ns)
MAP = {}
for nr, q in ns['PLAN']:
    if q[0] == 'alt':
        MAP[q[1]] = nr
    elif q[0] == 'alt2':
        MAP[q[1]] = nr
        MAP[q[2]] = nr
MAP.update(ERSETZT)

KURZ = re.compile(r'\b(b1\s*|b2\s*)?K(\d{2})\b')
LANG = re.compile(r'\bBand (1|2), Kapitel (\d+)\b')

zaehl = {'umgehaengt': 0, 'als alt markiert': 0, 'liegengelassen': 0}
offen = []


def grund(n):
    return ('Kapitel entfallen' if n in WEG else
            'Kapitel geteilt' if n in GETEILT else 'nicht in der Folge')


def kurz(m, datei, zeile, text):
    band, n = (m.group(1) or '').strip(), int(m.group(2))
    if band == 'b1':
        return m.group(0)
    if not band and n <= 34:
        zaehl['liegengelassen'] += 1
        offen.append((datei, zeile, 'blank K%02d, Band unklar' % n, text))
        return m.group(0)
    if n in MAP:
        zaehl['umgehaengt'] += 1
        return 'b2 K%02d' % MAP[n]
    zaehl['als alt markiert'] += 1
    offen.append((datei, zeile, 'alt K%02d: %s' % (n, grund(n)), text))
    return 'alt K%02d' % n


def lang(m, datei, zeile, text):
    if m.group(1) == '1':
        return m.group(0)
    n = int(m.group(2))
    if n in MAP:
        zaehl['umgehaengt'] += 1
        return 'Band 2, Kapitel %d' % MAP[n]
    zaehl['als alt markiert'] += 1
    offen.append((datei, zeile, 'Band 2, Kapitel %d: %s' % (n, grund(n)), text))
    return 'frueheres Kapitel %d' % n


for f in sorted(glob.glob(os.path.join(WURZEL, 'doc', '*.md'))):
    name = os.path.basename(f)
    z = io.open(f, encoding='utf-8').read().replace('\r\n', '\n').split('\n')
    for i, l in enumerate(z):
        vorher = l
        l = KURZ.sub(lambda m: kurz(m, name, i + 1, vorher.strip()[:90]), l)
        z[i] = LANG.sub(lambda m: lang(m, name, i + 1, vorher.strip()[:90]), l)
    io.open(f, 'w', encoding='utf-8', newline='\n').write('\n'.join(z))

for k, v in zaehl.items():
    print('%-18s %5d' % (k, v))

nach_grund = {}
for datei, zeile, g, text in offen:
    nach_grund.setdefault(g.split(':')[0], []).append((datei, zeile, g, text))
zeilen = [u'# Verweise, die von Hand entschieden werden muessen\n',
          u'Beim Umhaengen der Kapitelverweise auf die Nummerierung vom 27.08. sind'
          u' %d Stellen liegen geblieben. Sie sind im Text erkennbar: entweder als'
          u' `alt KNN` und `frueheres Kapitel N`, oder sie stehen unveraendert da,'
          u' weil das Band nicht aus dem Verweis hervorgeht.\n' % len(offen),
          u'**`doc/protokoll/` ist nicht angefasst worden** und steht auch nicht in'
          u' dieser Liste. Ein Protokoll ist ein Bericht von einem Tag, und die'
          u' Kapitelnummern darin sind die von dem Tag.\n']
for g in sorted(nach_grund, key=lambda x: -len(nach_grund[x])):
    zeilen.append(u'## %s - %d Stellen\n' % (g, len(nach_grund[g])))
    for datei, zeile, gg, text in nach_grund[g][:40]:
        zeilen.append(u'- `%s:%d` %s' % (datei, zeile, text))
    if len(nach_grund[g]) > 40:
        zeilen.append(u'- ... und %d weitere' % (len(nach_grund[g]) - 40))
    zeilen.append(u'')
io.open(os.path.join(WURZEL, 'archiv', 'VERWEISE-OFFEN.md'), 'w',
        encoding='utf-8', newline='\n').write(u'\n'.join(zeilen))
print('archiv/VERWEISE-OFFEN.md: %d Stellen' % len(offen))
