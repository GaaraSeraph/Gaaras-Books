# -*- coding: utf-8 -*-
"""Welcher Abendbericht zahlt auf die Jagd ein und welcher wiederholt nur.

Die Haelfte der Kapitel endet damit, dass Georgij Annie erzaehlt, was in dem
Kapitel geschehen ist. `doc/23-kuerzen.md` nennt das als dritten Eingriff -
*Abendbericht wird Halbsatz* - und als den am wenigsten ausgefuehrten.

Der Eingriff braucht ein Kriterium, und das Kriterium ist nicht die Laenge. Es
ist: **kommt in dem Bericht etwas vor, das vorher nicht dastand?** Ein Bericht,
in dem Annie urteilt, entscheidet oder etwas beitraegt, was Georgij nicht hat,
traegt das Kapitel. Ein Bericht, der die Szene noch einmal in denselben
Substantiven aufzaehlt, ist der Halbsatz-Kandidat.

Gemessen wird:

  neu      Anteil der seltenen Woerter im Schluss, die im Kapitel vorher nicht
           vorkommen. Niedrig heisst: es steht nichts Neues drin.
  urteil   Faellt in dem Schluss eine Anweisung oder eine Entscheidung? Gesucht
           werden Annies Imperative und die Formeln, in denen sie festlegt.
  choi     Kommt die Jagd darin vor - Choi, das Haus, der Trust, eine der
           gedrehten Figuren, ein Datum? Der Autor am 27.08.: **die
           Abendberichte muessen auf die Choi-Jagd einzahlen.**

Das Werkzeug entscheidet nichts. Es sortiert die Kandidaten nach oben.
"""
import io
import os
import re
import sys
import glob
import math
import collections

NAME = re.compile(r'ch(\d+)_v(\d+)_(\d+)_en\.md$')

URTEIL = re.compile(
    r'\bsaid Annie\b|"(?:Say|Tell|Get|Go|Do not|Then|Give|Take|Find|Bring|Write|Ask)\b'
    r'|\bAnnie (?:did not|does not|said|decided|put|picked|stood|looked|turned)\b'
    r'|Yes, Mistress|No, Mistress', re.I)
JAGD = re.compile(
    r'\bChoi\b|\btrust\b|\bBaek\b|\bSim\b|\bHwang\b|\bWoo\b|\bSang-hoon\b|\bYeom\b'
    r'|\bNam\b|\bJeon\b|\boxygen\b|\bregister\b|\bclause\b|\blot\b|\bconsign'
    r'|\bthe house\b|\bMrs Ha\b|\bMr Ok\b|\bMr Koh\b|\bMr Im\b', re.I)


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
for _v in ('chapters', 'chapters-2', 'chapters-3'):
    for _k, _p in kapitel(_v).items():
        gesamt += 1
        dfz.update(set(woerter(rumpf(_p))))


def selten(w):
    return math.log(gesamt / (1.0 + dfz[w])) > 1.6


def schluss(t):
    """Der letzte Abschnitt, wenn Annie darin vorkommt."""
    teile = re.split(r'\n\* \* \*\n', t)
    for k in range(len(teile) - 1, max(len(teile) - 4, -1), -1):
        s = teile[k].strip()
        if re.search(r'\bAnnie\b|\bMistress\b', s) and len(woerter(s)) >= 60:
            return s, '\n'.join(teile[:k])
    return None, None


def zeile(n, pfad):
    t = rumpf(pfad)
    s, vorher = schluss(t)
    if s is None:
        return None
    sw = set(x for x in woerter(s) if selten(x))
    vw = set(x for x in woerter(vorher) if selten(x))
    if not sw:
        return None
    neu = len(sw - vw) / float(len(sw))
    return (neu, len(woerter(s)), n,
            bool(URTEIL.search(s)), len(JAGD.findall(s)),
            s.replace('\n', ' ')[:96])


if __name__ == '__main__':
    kap = kapitel('chapters-2')
    zeilen = [z for z in (zeile(n, p) for n, p in sorted(kap.items())) if z]
    zeilen.sort(key=lambda x: (x[0], -x[1]))
    print('%-5s %-6s %-6s %-7s %-5s  %s'
          % ('Kap', 'neu', 'Woerter', 'Urteil', 'Jagd', 'Schluss'))
    grenze = float(sys.argv[1]) if len(sys.argv) > 1 else 0.45
    n_kand = 0
    for neu, w, n, urteil, jagd, txt in zeilen:
        if neu > grenze:
            continue
        n_kand += 1
        print('%-5d %-6.2f %-6d %-7s %-5d  %s'
              % (n, neu, w, 'ja' if urteil else '-', jagd, txt))
    print('\n%d von %d Abendberichten unter %.2f neu.' % (n_kand, len(zeilen), grenze))
    print('Wenig neu **und** kein Urteil **und** Jagd null: das sind die Halbsatz-Kandidaten.')
