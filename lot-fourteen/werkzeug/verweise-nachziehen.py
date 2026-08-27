# -*- coding: utf-8 -*-
"""Die Kapitelverweise in doc/ auf die neue Nummerierung ziehen.

Angefasst wird nur, was beweisbar Band 2 ist:
  - "b2 KNN" traegt das Band im Verweis.
  - blankes "KNN" mit NN groesser als 34 kann nicht Band 1 sein, weil Band 1
    vierunddreissig Kapitel hat.
  - "Band 2, Kapitel N" im Fliesstext.

Nicht angefasst wird:
  - "b1 KNN" und "Band 1, Kapitel N".
  - blankes "KNN" mit NN bis 34. Das kann beides sein, und es sind
    zweihundertsechsundsechzig Stellen. Sie stehen in der Restliste.

Drei Sorten Verweis bekommen kein neues Ziel, sondern ein "alt" davor:
  - die neun gestrichenen Kapitel 69 bis 77. Ihre alten Nummern gehoeren jetzt
    anderen Kapiteln, ein stehengelassenes K72 fuehrte also in den falschen
    Text. Das ist der Grund, warum hier markiert und nicht ignoriert wird.
  - die zwei geteilten: das alte 67 steckt in 66 und 68, das alte 90 in
    69, 73 und 83. Welche Haelfte gemeint ist, entscheidet der Satz.
  - was in keiner Liste steht.

Die Listeneintraege in 05-continuity werden uebersprungen, die sind schon
richtig.
"""
import io
import os
import re
import glob
import shutil

ERSETZT = {57: 63, 61: 71, 62: 72, 65: 65, 66: 66, 88: 80, 89: 61, 78: 76}
GETEILT = {67, 90}
WEG = set(range(69, 78))

src = io.open('werkzeug/umnummerieren.py', encoding='utf-8').read()
ns = {'__file__': os.path.abspath('werkzeug/umnummerieren.py')}
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

KURZ = re.compile(r'\b(b2\s*)?K(\d{2})\b')
LANG = re.compile(r'\bBand 2, Kapitel (\d+)\b')

zaehl = {'umgehaengt': 0, 'als alt markiert': 0, 'uebersprungen': 0}
offen = []


def kurz(m, datei, zeile, text):
    hat_b2 = bool(m.group(1))
    n = int(m.group(2))
    if not hat_b2 and n <= 34:
        zaehl['uebersprungen'] += 1
        offen.append((datei, zeile, 'blank K%02d, Band unklar' % n, text))
        return m.group(0)
    if n in MAP:
        zaehl['umgehaengt'] += 1
        return 'b2 K%02d' % MAP[n]
    grund = ('Kapitel entfallen' if n in WEG else
             'Kapitel geteilt' if n in GETEILT else 'nicht in der Folge')
    zaehl['als alt markiert'] += 1
    offen.append((datei, zeile, 'alt K%02d: %s' % (n, grund), text))
    return 'alt K%02d' % n


def lang(m, datei, zeile, text):
    n = int(m.group(1))
    if n in MAP:
        zaehl['umgehaengt'] += 1
        return 'Band 2, Kapitel %d' % MAP[n]
    grund = ('entfallen' if n in WEG else
             'geteilt' if n in GETEILT else 'nicht in der Folge')
    zaehl['als alt markiert'] += 1
    offen.append((datei, zeile, 'Band 2, Kapitel %d: %s' % (n, grund), text))
    return 'frueheres Kapitel %d' % n


if not os.path.isdir('archiv/doc-vor-umnummerierung'):
    shutil.copytree('doc', 'archiv/doc-vor-umnummerierung')
    print('doc/ gesichert nach archiv/doc-vor-umnummerierung/')

for f in sorted(glob.glob('doc/*.md')):
    name = os.path.basename(f)
    z = io.open(f, encoding='utf-8').read().replace('\r\n', '\n').split('\n')
    for i, l in enumerate(z):
        if l.startswith('- **Band 2, Kapitel '):
            continue
        neu = KURZ.sub(lambda m: kurz(m, name, i + 1, l.strip()[:90]), l)
        neu = LANG.sub(lambda m: lang(m, name, i + 1, l.strip()[:90]), neu)
        z[i] = neu
    io.open(f, 'w', encoding='utf-8', newline='\n').write('\n'.join(z))

for k, v in zaehl.items():
    print('%-18s %5d' % (k, v))

zeilen = [u'# Verweise, die von Hand entschieden werden muessen\n',
          u'Beim Umhaengen der Kapitelverweise am 27.08. sind %d Stellen liegen'
          u' geblieben. Sie sind im Text erkennbar: entweder als `alt KNN` und'
          u' `frueheres Kapitel N`, oder sie stehen unveraendert da, weil das'
          u' Band nicht aus dem Verweis hervorgeht.\n' % len(offen)]
nach_grund = {}
for datei, zeile, grund, text in offen:
    nach_grund.setdefault(grund.split(':')[0], []).append((datei, zeile, grund, text))
for g in sorted(nach_grund, key=lambda x: -len(nach_grund[x])):
    zeilen.append(u'## %s - %d Stellen\n' % (g, len(nach_grund[g])))
    for datei, zeile, grund, text in nach_grund[g][:40]:
        zeilen.append(u'- `%s:%d` %s' % (datei, zeile, text))
    if len(nach_grund[g]) > 40:
        zeilen.append(u'- ... und %d weitere' % (len(nach_grund[g]) - 40))
    zeilen.append(u'')
io.open('archiv/VERWEISE-OFFEN.md', 'w', encoding='utf-8', newline='\n').write(u'\n'.join(zeilen))
print('archiv/VERWEISE-OFFEN.md: %d Stellen' % len(offen))
