# -*- coding: utf-8 -*-
"""Welcher Absatz sagt noch einmal, was ein frueherer schon gesagt hat.

Nicht woertlich. Eine Wiederholung sagt dasselbe im Buch fast nie mit denselben
Woertern - sie erzaehlt den Vorgang und traegt ihn danach Annie vor, oder das
zweite Kapitel zaehlt auf, was im ersten geschehen ist.

Gemessen wird deshalb ueber **seltene** Woerter, und selten heisst zweifach:

  - selten im Buch, ueber alle 117 Kapitel. Damit faellt der Gang des Buches
    heraus ("did not say anything"), der keine Doppelung ist.
  - selten **in diesem Kapitel**. Ein Name, der im Kapitel zwanzigmal steht,
    ist kein Beleg dafuer, dass zwei Absaetze dasselbe sagen. Das war der
    Fehler der ersten Fassung: jedes Paar mit "Mr Hwang" darin kam auf 1.00.

Der Wert ist Dice, also symmetrisch. Ein kurzer Absatz, dessen Woerter zufaellig
alle in einem langen vorkommen, kommt damit nicht mehr durch.

Aufruf:
    python3 werkzeug/doppelt-im-kapitel.py 26 29 32 35
    python3 werkzeug/doppelt-im-kapitel.py --alle
"""
import io
import os
import re
import sys
import glob
import math
import collections

NAME = re.compile(r'ch(\d+)_v(\d+)_(\d+)_en\.md$')
SCHWELLE = 0.22
MINDESTWOERTER = 18


def kapitel(verz):
    best = {}
    for p in glob.glob(os.path.join(verz, 'ch*_en.md')):
        m = NAME.search(os.path.basename(p))
        if not m:
            continue
        k = int(m.group(1))
        v = (int(m.group(2)), int(m.group(3)))
        if k not in best or v > best[k][0]:
            best[k] = (v, p)
    return {k: v[1] for k, v in best.items()}


def rumpf(p):
    return '\n'.join(io.open(p, encoding='utf-8').read()
                     .replace('\r\n', '\n').split('\n')[2:])


def woerter(t):
    return re.findall(r"[a-z']+", t.lower())


dfz = collections.Counter()
gesamt = 0
for _verz in ('chapters', 'chapters-2', 'chapters-3'):
    for _k, _p in kapitel(_verz).items():
        gesamt += 1
        dfz.update(set(woerter(rumpf(_p))))


def absaetze(t):
    lokal = collections.Counter(woerter(t))
    out = []
    for roh in re.split(r'\n\s*\n', t):
        s = roh.strip()
        if not s or s in ('---', '* * *') or s.startswith('## Day'):
            continue
        w = woerter(s)
        if len(w) < MINDESTWOERTER:
            continue
        g = {}
        for x in set(w):
            im_buch = math.log(gesamt / (1.0 + dfz[x]))
            if im_buch <= 1.2:
                continue
            g[x] = im_buch / (1.0 + math.log(lokal[x]))
        if g:
            out.append((s, g))
    return out


def pruefe(n, pfad):
    ab = absaetze(rumpf(pfad))
    treffer = []
    for i in range(len(ab)):
        for j in range(i + 1, len(ab)):
            a, b = ab[i][1], ab[j][1]
            gem = set(a) & set(b)
            if len(gem) < 3:
                continue
            oben = 2 * sum(min(a[w], b[w]) for w in gem)
            unten = sum(a.values()) + sum(b.values())
            if unten and oben / unten >= SCHWELLE:
                treffer.append((oben / unten, i, j, ab[i][0], ab[j][0], sorted(gem)))
    treffer.sort(key=lambda x: -x[0])
    print('ch%-3d %d Absaetze, %d Paare ueber %.2f' % (n, len(ab), len(treffer), SCHWELLE))
    for q, i, j, sa, sb, gem in treffer[:10]:
        print('   %.2f  Absatz %d und %d   [%s]' % (q, i + 1, j + 1, ' '.join(gem[:9])))
        print('      A  %s' % sa.replace('\n', ' ')[:116])
        print('      B  %s' % sb.replace('\n', ' ')[:116])
    print()


if __name__ == '__main__':
    kap = kapitel('chapters-2')
    ziel = sorted(kap) if '--alle' in sys.argv else [int(a) for a in sys.argv[1:] if a.isdigit()]
    for n in ziel:
        pruefe(n, kap[n])
