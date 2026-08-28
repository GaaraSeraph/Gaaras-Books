# -*- coding: utf-8 -*-
u"""Saetze, die zwei Daten nennen und den Abstand zwischen ihnen behaupten.

**Warum so eng.** Am 28.08. lief eine weite Fassung: jede Spanne in Tagen
oder Wochen, verglichen mit dem Abstand zum Kapiteltag. Sie meldete
dreiunddreissig Stellen, und siebenundzwanzig davon waren Unsinn, weil die
Spanne gar nicht bis zum Kapiteltag laeuft - "on the page, in her coat, for
twelve days" misst zwischen zwei Ereignissen, von denen keines der heutige
Tag ist. Eine Liste, in der vier von fuenf Meldungen falsch sind, wird nach
zwei Durchgaengen nicht mehr gelesen, und dann faengt sie nichts mehr.

Uebrig bleibt die Sorte, die sich selbst vorrechnet: **beide Enden stehen im
Satz.** Davon gibt es wenige, und jede einzelne ist entscheidbar.

    "The fourth of November is five weeks before the tenth of December."

Der Rest - 1.400 Spannen ohne zweites Ende - braucht einen Leser, und dieses
Skript behauptet nicht, ihn zu ersetzen. Es sagt nur, wie viele es sind.

    python werkzeug/spanne.py
    python werkzeug/spanne.py --probe
"""
import contextlib
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
with contextlib.redirect_stdout(io.StringIO()):
    import register as REG                                 # noqa: E402
    import datumsprobe as DP                               # noqa: E402
    import wochentag as W                                  # noqa: E402

EINER = u'''zero one two three four five six seven eight nine ten eleven twelve
thirteen fourteen fifteen sixteen seventeen eighteen nineteen'''.split()
ZEHNER = {u'twenty': 20, u'thirty': 30, u'forty': 40, u'fifty': 50,
          u'sixty': 60, u'seventy': 70, u'eighty': 80, u'ninety': 90}
WORT = u'|'.join(EINER + list(ZEHNER) + [u'hundred'])

SPANNE = re.compile(
    r'\b((?:%s|\d+)(?:[- ](?:and[- ])?(?:%s))*)\s+(days?|weeks?)\b'
    % (WORT, WORT), re.I)
# Nur Formulierungen, die die beiden Daten wirklich gegeneinander stellen.
BEZUG = re.compile(r'\b(before|after|apart|later|earlier|between)\b', re.I)


def zahl(s):
    s = s.lower().replace(u'-', u' ').replace(u' and ', u' ')
    n, teil = 0, 0
    for w in s.split():
        if w.isdigit():
            teil += int(w)
        elif w in EINER:
            teil += EINER.index(w)
        elif w in ZEHNER:
            teil += ZEHNER[w]
        elif w == u'hundred':
            teil = max(1, teil) * 100
            n, teil = n + teil, 0
        else:
            return None
    return n + teil


def lauf(kaputt=None):
    treffer, ohne_zweites = [], 0
    for band, k, pfad, name in REG.kanon():
        zeilen = io.open(pfad, encoding='utf-8').read().split(u'\n')
        if kaputt and kaputt[0] == (band, k):
            zeilen = list(zeilen) + [u''] * kaputt[1]
            zeilen[kaputt[1] - 1] = kaputt[2]
        tage = []
        for e in REG.kopfzeilen(zeilen):
            if e[0]:
                tage.extend(e[0])
        if not tage:
            continue
        erster, letzter = REG.datum(min(tage)), REG.datum(max(tage))

        for i, z in enumerate(zeilen, 1):
            if z.strip().startswith(u'#') or REG.KOPF.match(z.strip()):
                continue
            s = SPANNE.search(z)
            if not s or not BEZUG.search(z):
                continue
            n = zahl(s.group(1))
            if n is None:
                continue
            soll = n * (7 if s.group(2).lower().startswith(u'week') else 1)
            daten = [W.aufloesen(z, m.group(0), erster, letzter)
                     for m in DP.DATUM.finditer(z)]
            daten = sorted(set(d for d in daten if d))
            if len(daten) < 2:
                ohne_zweites += 1
                continue
            ist = (daten[-1] - daten[0]).days
            treffer.append((band, k, i, s.group(0), soll, ist,
                            daten[0], daten[-1], z.strip()))
    return treffer, ohne_zweites


if __name__ == u'__main__':
    if u'--probe' in sys.argv:
        # b1 ch05 spielt im Oktober 2025. Vom vierten Oktober bis zum elften
        # sind es sieben Tage; die Probe behauptet einmal sieben und einmal
        # neun, und nur die zweite darf melden.
        def melden(satz):
            t, _ = lauf(((1, 5), 60, satz))
            return [x for x in t if (x[0], x[1], x[2]) == (1, 5, 60)
                    and x[4] != x[5]]
        richtig = u'The fourth of October was seven days before the eleventh of October.'
        falsch = u'The fourth of October was nine days before the eleventh of October.'
        fehlt = []
        if not melden(falsch):
            fehlt.append(u'die falsche Spanne wird nicht gemeldet')
        if melden(richtig):
            fehlt.append(u'die richtige Spanne wird gemeldet')
        # und ein Satz ohne zweites Datum darf gar nicht erst hineingeraten
        t, _ = lauf(((1, 5), 60, u'He had waited nine days after the fourth of October.'))
        if [x for x in t if (x[0], x[1], x[2]) == (1, 5, 60)]:
            fehlt.append(u'ein Satz mit nur einem Datum wird gerechnet')
        print(u'Gegenprobe: %s' % (u'faengt die falsche, laesst die richtige, '
                                   u'ignoriert die einseitige' if not fehlt
                                   else u'LUECKE - ' + u'; '.join(fehlt)))
        sys.exit(1 if fehlt else 0)

    treffer, ohne = lauf()
    print(u'%d Saetze nennen beide Enden und sind damit entscheidbar.' % len(treffer))
    print(u'%d weitere Spannen haben nur ein Ende im Satz und brauchen einen '
          u'Leser.\n' % ohne)
    schief = 0
    for band, k, i, roh, soll, ist, a, b, z in treffer:
        gut = soll == ist
        schief += 0 if gut else 1
        print(u'%s b%d ch%02d:%-4d "%s" = %d Tage, %s bis %s sind %d'
              % (u'  ' if gut else u'!!', band, k, i, roh, soll,
                 a.isoformat(), b.isoformat(), ist))
        if not gut:
            print(u'      %s' % z[:180])
    print(u'\n=== Spannen, die nicht aufgehen: %d' % schief)
