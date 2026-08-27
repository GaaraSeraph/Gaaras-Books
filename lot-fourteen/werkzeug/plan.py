# -*- coding: utf-8 -*-
"""Jedes Kapitel von Band 2 gegen seine Zielgroesse aus TEIL XII der CHOI-LISTEN.

TEIL XII Nr. N ist Kapitel N+24. Die Liste deckt 25 bis 83 ab; 1 bis 24 stehen
nicht darin und werden nicht bewertet.
"""
import io
import os
import re
import glob

LISTE = u'C:/Users/GeorgijBoguslawskij/Downloads/CHOI-LISTEN.md'
BUCH = u'C:/Users/GeorgijBoguslawskij/Downloads/Gaaras-Books/lot-fourteen'
NAME = re.compile(r'ch(\d+)_v(\d+)_(\d+)_en\.md$')
ZEILE = re.compile(r'^\|\s*(\d{1,2})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*([\d.]+)\s*\|')

# --- Zielgroessen aus TEIL XII
text = io.open(LISTE, encoding='utf-8').read().replace('\r\n', '\n')
teil12 = text.split(u'## SATZ I - DIE ERMITTLUNG')[1]
ziel = {}
for z in teil12.split('\n'):
    m = ZEILE.match(z)
    if not m:
        continue
    nr = int(m.group(1))
    w = m.group(4).replace('.', '')
    if not w.isdigit() or not 1 <= nr <= 59:
        continue
    kap = nr + 24
    if kap not in ziel:
        ziel[kap] = (int(w), m.group(2).replace('**', ''))

# --- tatsaechliche Groessen
best = {}
for p in glob.glob(os.path.join(BUCH, 'chapters-2', 'ch*_en.md')):
    m = NAME.search(os.path.basename(p))
    if not m:
        continue
    k, v = int(m.group(1)), (int(m.group(2)), int(m.group(3)))
    if k not in best or v > best[k][0]:
        best[k] = (v, p)

ist = {}
for k, (v, p) in best.items():
    t = io.open(p, encoding='utf-8').read().replace('\r\n', '\n')
    ist[k] = len('\n'.join(t.split('\n')[2:]).split())

zeilen = []
for k in sorted(ziel):
    if k not in ist:
        continue
    zeilen.append((ist[k] - ziel[k][0], k, ist[k], ziel[k][0], ziel[k][1]))

zeilen.sort(reverse=True)
print(u'%-5s %-34s %7s %7s %8s' % ('Kap', 'Titel', 'ist', 'Ziel', 'darueber'))
for d, k, i, z, titel in zeilen:
    if d <= 0:
        continue
    print(u'%-5d %-34s %7d %7d %+8d' % (k, titel[:34], i, z, d))

ueber = sum(d for d, k, i, z, t in zeilen if d > 0)
unter = sum(-d for d, k, i, z, t in zeilen if d < 0)
gesamt_ist = sum(ist[k] for d, k, i, z, t in zeilen)
gesamt_ziel = sum(z for d, k, i, z, t in zeilen)
print(u'\n%d Kapitel bewertet (25 bis 83).' % len(zeilen))
print(u'ueber Ziel: %d Woerter in %d Kapiteln' % (ueber, len([1 for d, a, b, c, e in zeilen if d > 0])))
print(u'unter Ziel: %d Woerter in %d Kapiteln' % (unter, len([1 for d, a, b, c, e in zeilen if d < 0])))
print(u'Summe ist %d, Summe Ziel %d, netto %d' % (gesamt_ist, gesamt_ziel, gesamt_ist - gesamt_ziel))
