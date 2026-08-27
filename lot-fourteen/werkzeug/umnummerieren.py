# -*- coding: utf-8 -*-
"""Band 2 auf die Folge aus Teil XII bringen, durchnummeriert von 1.

Baut nach chapters-2-neu/ und fasst chapters-2/ nicht an. build.py sieht das
Staging nicht, weil in BANDS nur "chapters" und "chapters-2" stehen.

Was hier passiert und was NICHT:
  - Jedes Kapitel bekommt seine Nummer im fertigen Buch, in Dateiname UND
    Kopfzeile. Die Luecken bei 16, 27, 30, 34, 44, 59, 68, 79 fallen weg.
  - Vier Zusammenlegungen werden ausgefuehrt (28+29, 33+35, 38+39, 42+43).
    Nur die bekommen einen neuen Titel, weil zwei Kapitel nicht zwei behalten
    koennen. Alle anderen behalten ihren eigenen Titel; die Umbenennungen aus
    Teil XII sind eine eigene Entscheidung.
  - Die acht Kuerzungen ("gek.") werden NICHT gekuerzt. Sie ziehen ungekuerzt
    mit um und stehen unten in der Liste.
  - Nr. 60 bleibt leer. Das ist "Sie faehrt zurueck", und es ist nicht
    geschrieben. Der Platz wird reserviert, damit das Schreiben spaeter kein
    zweites Umnummerieren ausloest.
  - Die Fassungsnummern bleiben, wo der Text unveraendert ist. Nur die vier
    Zusammenlegungen bekommen v3.0, weil sich dort wirklich etwas aendert.
"""
import io, os, re, glob, shutil, sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALT = os.path.join(WURZEL, 'chapters-2')
NEU = os.path.join(WURZEL, 'chapters-2-neu')
MEIN = (r'C:\Users\GEORGI~1\AppData\Local\Temp\claude'
        r'\C--Users-GeorgijBoguslawskij-Downloads-devops'
        r'\9e81d74e-5f4b-4960-927a-b42ed462dadc\scratchpad')

NAME = re.compile(r'ch(\d+)_v(\d+)_(\d+)_en\.md$')


def hoechste(verz):
    best = {}
    for p in glob.glob(os.path.join(verz, 'ch*_en.md')):
        m = NAME.search(os.path.basename(p))
        if not m:
            continue
        k = int(m.group(1))
        v = (int(m.group(2)), int(m.group(3)))
        if k not in best or v > best[k][0]:
            best[k] = (v, p)
    return best


# (neue Nummer, Quelle)
#   ('alt', n)        - aus chapters-2, unveraendert bis auf die Nummer
#   ('alt2', a, b, t) - alt a und alt b zusammengelegt, neuer Titel t
#   ('mein', n)       - aus dem Scratchpad, schon v3.0
PLAN = []
# --- Block A: die ersten vierundzwanzig, Luecke bei 16 geschlossen
for i, k in enumerate([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25], start=1):
    PLAN.append((i, ('alt', k)))
# --- Block B: Teil XII Nr. 1 bis 37  ->  neu 25 bis 61
PLAN += [
    (25, ('alt', 26)),
    (26, ('alt2', 28, 29, 'She has a list')),
    (27, ('alt', 31)),
    (28, ('alt', 32)),
    (29, ('alt2', 33, 35, 'Two witnesses')),
    (30, ('alt', 36)),
    (31, ('alt', 37)),
    (32, ('alt2', 38, 39, 'The man kitchens talk to')),
    (33, ('alt', 40)),
    (34, ('alt', 41)),
    (35, ('alt2', 42, 43, 'Somebody in Seoul pays for it')),
    (36, ('alt', 45)),
    (37, ('alt', 46)),
    (38, ('alt', 47)),
    (39, ('alt', 48)),
    (40, ('alt', 49)),
    (41, ('alt', 50)),
    (42, ('alt', 51)),
    (43, ('alt', 52)),
    (44, ('alt', 53)),
    (45, ('alt', 54)),
    (46, ('alt', 55)),
    (47, ('alt', 56)),
    (48, ('alt', 58)),
    (49, ('alt', 60)),
    (50, ('alt', 63)),
    (51, ('alt', 64)),
    (52, ('alt', 80)),
    (53, ('alt', 81)),
    (54, ('alt', 82)),
    (55, ('alt', 83)),
    (56, ('alt', 84)),
    (57, ('alt', 85)),
    (58, ('alt', 86)),
    (59, ('alt', 87)),
    # 60 bleibt leer: NEU "Sie faehrt zurueck"
    (61, ('alt', 89)),
]
# --- Block C: Teil XII Nr. 38 bis 59  ->  neu 62 bis 83, in Tagesfolge
PLAN += [
    (62, ('mein', 38)), (63, ('mein', 39)), (64, ('mein', 43)), (65, ('mein', 40)),
    (66, ('mein', 41)), (67, ('mein', 44)), (68, ('mein', 42)), (69, ('mein', 45)),
    (70, ('mein', 46)), (71, ('mein', 47)), (72, ('mein', 48)), (73, ('mein', 49)),
    (74, ('mein', 50)), (75, ('mein', 51)),
    # 76 bleibt leer: Teil XII Nr. 52 "The only line out", aus alt ch78,
    # muss erst umdatiert und gekuerzt werden
    (77, ('mein', 53)), (78, ('mein', 54)), (79, ('mein', 55)), (80, ('mein', 56)),
    (81, ('mein', 57)), (82, ('mein', 58)), (83, ('mein', 59)),
]

KOPF = re.compile(r'^# Chapter (\d+): (.+)$')
VERS = re.compile(r'^\*Lot Fourteen\* \u00b7 Version (\d+)\.(\d+) \u00b7 EN$')


def lies(pfad):
    z = io.open(pfad, encoding='utf-8').read().replace(u'\r\n', u'\n').split(u'\n')
    mk = KOPF.match(z[0])
    mv = VERS.match(z[1])
    if not mk or not mv:
        raise SystemExit('Kopf unlesbar in %s: %r / %r' % (pfad, z[0], z[1]))
    return mk.group(2), (int(mv.group(1)), int(mv.group(2))), u'\n'.join(z[2:]).strip(u'\n')


def schreib(nr, titel, ver, rumpf):
    name = 'ch%02d_v%d_%d_en.md' % (nr, ver[0], ver[1])
    kopf = u'# Chapter %d: %s\n*Lot Fourteen* \u00b7 Version %d.%d \u00b7 EN\n\n' % (
        nr, titel, ver[0], ver[1])
    io.open(os.path.join(NEU, name), 'w', encoding='utf-8').write(kopf + rumpf + u'\n')
    return name


if os.path.isdir(NEU):
    shutil.rmtree(NEU)
os.makedirs(NEU)

alt = hoechste(ALT)
mein = hoechste(MEIN)
protokoll = []

for nr, quelle in PLAN:
    art = quelle[0]
    if art == 'alt':
        k = quelle[1]
        if k not in alt:
            raise SystemExit('alt ch%d fehlt' % k)
        t, v, r = lies(alt[k][1])
        n = schreib(nr, t, v, r)
        protokoll.append((nr, 'alt ch%d' % k, t, n))
    elif art == 'alt2':
        a, b, t = quelle[1], quelle[2], quelle[3]
        _, va, ra = lies(alt[a][1])
        _, vb, rb = lies(alt[b][1])
        n = schreib(nr, t, (3, 0), ra.rstrip(u'\n') + u'\n\n' + rb.lstrip(u'\n'))
        protokoll.append((nr, 'alt ch%d+ch%d' % (a, b), t, n))
    else:
        k = quelle[1]
        if k not in mein:
            raise SystemExit('mein ch%d fehlt' % k)
        t, v, r = lies(mein[k][1])
        n = schreib(nr, t, v, r)
        protokoll.append((nr, 'neu ch%d' % k, t, n))

print('%d Kapitel nach chapters-2-neu/ geschrieben.' % len(protokoll))
print('Nummern 1 bis %d, Platz 60 reserviert.' % max(n for n, _ in PLAN))
