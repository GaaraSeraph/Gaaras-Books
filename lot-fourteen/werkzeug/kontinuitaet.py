# -*- coding: utf-8 -*-
"""Kontinuitaetspruefungen ueber beide Baende, die check.py nicht macht.

check.py sieht ein Kapitel auf einmal. Das hier legt die Kapitel nebeneinander.

  A  Woertlich gleiche Saetze in verschiedenen Kapiteln. So ist herausgekommen,
     dass 61 und 82 dieselben Szenen erzaehlt haben.
  B  Zahlen, die an einem Gegenstand haengen. "sechzig Einladungen" darf nicht
     an einer Stelle zweiundsechzig und an einer anderen vierundsechzig sein.
  C  Altersangaben je Figur.
  D  Datumsangaben im Fliesstext, die einen Wochentag mitnennen.

Aufruf: python3 werkzeug/kontinuitaet.py [a|b|c|d]
"""
import io
import os
import re
import sys
import glob
import datetime
import collections

DAY1 = datetime.date(2025, 10, 4)
NAME = re.compile(r'ch(\d+)_v(\d+)_(\d+)_en\.md$')


def kapitel():
    """Alle Kapitel beider Baende, jeweils die hoechste Fassung."""
    out = []
    for band, d in ((1, 'chapters'), (2, 'chapters-2')):
        best = {}
        for p in glob.glob(os.path.join(d, 'ch*_en.md')):
            m = NAME.search(os.path.basename(p))
            if not m:
                continue
            k = int(m.group(1))
            v = (int(m.group(2)), int(m.group(3)))
            if k not in best or v > best[k][0]:
                best[k] = (v, p)
        for k in sorted(best):
            z = io.open(best[k][1], encoding='utf-8').read().replace('\r\n', '\n')
            out.append((band, k, z))
    return out


def satzliste(text):
    for zeile in text.split('\n'):
        if zeile.startswith('#') or zeile.startswith('*Lot Fourteen*'):
            continue
        for s in re.split(r'(?<=[.?!])\s+', zeile.strip()):
            yield s.strip().strip('"“”*')


def a_doppelt(kap):
    wo = collections.defaultdict(list)
    for band, k, t in kap:
        for s in satzliste(t):
            if len(s.split()) >= 9:
                wo[s].append('b%d/%d' % (band, k))
    treffer = [(s, sorted(set(v))) for s, v in wo.items() if len(set(v)) > 1]
    treffer.sort(key=lambda x: -len(x[1]))
    print('%d Saetze stehen in mehr als einem Kapitel\n' % len(treffer))
    for s, v in treffer:
        print('  %s' % ', '.join(v))
        print('    %s\n' % s[:150])


# Gegenstand -> Regex, der die Zahl einfaengt
KONSTANTEN = {
    'Einladungen zur Hochzeit': r'(\w+[- ]?\w*) (?:people were invited|invitations)',
    'Tische mit Blumen':        r'(\w+) tables',
    'Hochzeiten Mrs Ha':        r'(\w+ \w+ and \w+) weddings',
    'Kaeufer des Hefts':        r'(\w+ \w+ and \w+) buyers',
    'Namen auf der Seite':      r'(\w+[- ]?\w*) names on a page',
    'Leute bei Sang-hoon':      r'(\w+ \w+) people and a habit',
    'Jahre am Tisch':           r'(\w+[- ]?\w*) years (?:ago there was a customs|arranging)',
}


def b_konstanten(kap):
    for was, pat in KONSTANTEN.items():
        gef = collections.defaultdict(list)
        for band, k, t in kap:
            for m in re.finditer(pat, t):
                gef[m.group(1).lower()].append('b%d/%d' % (band, k))
        if len(gef) > 1:
            print('%s -- %d verschiedene Werte' % (was, len(gef)))
            for wert in sorted(gef, key=lambda x: -len(gef[x])):
                print('    %-28s %2dx  %s' % (wert, len(gef[wert]),
                                              ', '.join(sorted(set(gef[wert])))[:70]))
            print()
        elif gef:
            wert = list(gef)[0]
            print('%s -- einheitlich: %s (%dx)' % (was, wert, len(gef[wert])))


ALTER = re.compile(
    r'([A-Z][a-z]+(?: [A-Z][a-z]+(?:-[a-z]+)?)?|Mrs [A-Z][a-z]+|Mr [A-Z][a-z]+|Chairman Woo)'
    r'[^.]{0,60}?\bis (\w+(?:-\w+)?)\b(?![ ]a )')
ICHALTER = re.compile(r'I am (\w+-\w+|\w+)\b')
ZAHLWORT = set('''twenty thirty forty fifty sixty seventy eighty ninety'''.split())


def c_alter(kap):
    gef = collections.defaultdict(lambda: collections.defaultdict(list))
    for band, k, t in kap:
        for m in ALTER.finditer(t):
            wer, wert = m.group(1), m.group(2).lower()
            if wert.split('-')[0] in ZAHLWORT:
                gef[wer][wert].append('b%d/%d' % (band, k))
    for wer in sorted(gef):
        if len(gef[wer]) > 1:
            print('%-22s %s' % (wer, ' | '.join(
                '%s (%s)' % (w, ', '.join(sorted(set(gef[wer][w])))) for w in gef[wer])))
    print()
    print('Wer sagt "I am <Zahl>":')
    ich = collections.defaultdict(list)
    for band, k, t in kap:
        for m in ICHALTER.finditer(t):
            if m.group(1).lower().split('-')[0] in ZAHLWORT:
                ich[m.group(1).lower()].append('b%d/%d' % (band, k))
    for w in sorted(ich, key=lambda x: -len(ich[x])):
        print('  %-16s %2dx  %s' % (w, len(ich[w]), ', '.join(sorted(set(ich[w])))[:80]))


MONATE = {m: i for i, m in enumerate(
    'January February March April May June July August September October '
    'November December'.split(), 1)}
TAGWORT = {'first':1,'second':2,'third':3,'fourth':4,'fifth':5,'sixth':6,'seventh':7,
 'eighth':8,'ninth':9,'tenth':10,'eleventh':11,'twelfth':12,'thirteenth':13,
 'fourteenth':14,'fifteenth':15,'sixteenth':16,'seventeenth':17,'eighteenth':18,
 'nineteenth':19,'twentieth':20,'twenty-first':21,'twenty-second':22,
 'twenty-third':23,'twenty-fourth':24,'twenty-fifth':25,'twenty-sixth':26,
 'twenty-seventh':27,'twenty-eighth':28,'twenty-ninth':29,'thirtieth':30,
 'thirty-first':31}
WOCHENTAG = re.compile(
    r'\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b[^.]{0,30}?'
    r'\bthe (' + '|'.join(TAGWORT) + r') of (' + '|'.join(MONATE) + r')\b')
UMGEKEHRT = re.compile(
    r'\bthe (' + '|'.join(TAGWORT) + r') of (' + '|'.join(MONATE) + r')\b[^.]{0,20}?'
    r'\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b')


def d_wochentage(kap):
    """Datumsangaben im Fliesstext, die einen Wochentag mitnennen.

    Das Jahr ist nicht sicher bestimmbar - der Kalender laeuft ueber zwei
    Jahre und die Kapitel wissen ihr Jahr nicht. Geprueft wird deshalb gegen
    beide Jahre, und gemeldet wird nur, was in keinem von beiden aufgeht."""
    n = schlecht = 0
    for band, k, t in kap:
        for pat, gruppen in ((WOCHENTAG, (1, 2, 3)), (UMGEKEHRT, (3, 1, 2))):
            for m in pat.finditer(t):
                tag_name = m.group(gruppen[0])
                tag = TAGWORT[m.group(gruppen[1])]
                monat = MONATE[m.group(gruppen[2])]
                n += 1
                passt = False
                for jahr in (2025, 2026, 2027):
                    try:
                        if datetime.date(jahr, monat, tag).strftime('%A') == tag_name:
                            passt = True
                    except ValueError:
                        pass
                if not passt:
                    schlecht += 1
                    print('  b%d/%-3d %s' % (band, k, m.group(0)[:80]))
    print('\n%d Datumsangaben mit Wochentag geprueft, %d gehen in keinem Jahr auf'
          % (n, schlecht))


if __name__ == '__main__':
    was = (sys.argv[1] if len(sys.argv) > 1 else 'a').lower()
    kap = kapitel()
    print('%d Kapitel geladen (Band 1: %d, Band 2: %d)\n'
          % (len(kap), sum(1 for b, _, _ in kap if b == 1),
             sum(1 for b, _, _ in kap if b == 2)))
    {'a': a_doppelt, 'b': b_konstanten, 'c': c_alter, 'd': d_wochentage}[was](kap)
