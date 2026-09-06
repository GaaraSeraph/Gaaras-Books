# -*- coding: utf-8 -*-
"""Das Geruest eines Kapitels: Tag, Szene, Umfang, Aufhaenger.

Eine Szene ist ein Block zwischen zwei "* * *" innerhalb eines Erzaehltags.
Die "---" darin sind Beats und keine Szenen.

Gedacht fuer die Frage, die beim Kuerzen zaehlt und die kein Zaehlwerkzeug
beantworten kann: **was tut diese Szene fuer die Jagd?** Das Geruest sagt nur,
wo die Szenen sind und wie schwer sie wiegen.
"""
import io, os, re, sys, glob
NAME = re.compile(r'ch(\d+)_v(\d+)_(\d+)_en\.md$')

def kapitel():
    # --band N waehlt das Verzeichnis. Vorgabe 2, wie bisher.
    _d = {'1': 'chapters', '2': 'chapters-2', '3': 'chapters-3'}[
        sys.argv[sys.argv.index('--band') + 1] if '--band' in sys.argv else '2']
    best = {}
    for p in glob.glob(_d + '/ch*_en.md'):
        m = NAME.search(os.path.basename(p))
        k = int(m.group(1)); v = (int(m.group(2)), int(m.group(3)))
        if k not in best or v > best[k][0]: best[k] = (v, p)
    return {k: v[1] for k, v in best.items()}

def geruest(n, p):
    roh = io.open(p, encoding='utf-8').read().replace('\r\n', '\n')
    t = '\n'.join(roh.split('\n')[2:])
    ges = len(re.findall(r"[a-z']+", t.lower()))
    print('=== ch%-3d %-34s %5d Woerter' % (n, roh.split('\n')[0][12:46], ges))
    s = 0
    for block in re.split(r'(?=^## Day)', t, flags=re.M):
        if not block.strip(): continue
        m = re.match(r'## Day ([A-Za-z\s-]+?) · (.+)', block)
        tag = m.group(2) if m else '(ohne Kopf)'
        rest = re.sub(r'^## Day.*$', '', block, flags=re.M)
        for teil in re.split(r'\n\* \* \*\n', rest):
            txt = teil.strip()
            if not txt: continue
            s += 1
            w = len(re.findall(r"[a-z']+", txt.lower()))
            erste = re.sub(r'\s+', ' ', re.sub(r'^-+$', '', txt, flags=re.M).strip().split('\n')[0])
            print('  %2d  %-18s %4dW  %s' % (s, tag, w, erste[:96]))
    print()

if __name__ == '__main__':
    kap = kapitel()
    _roh = sys.argv[1:]
    if '--band' in _roh:
        _i = _roh.index('--band')
        _roh = _roh[:_i] + _roh[_i + 2:]
    if '--alle' in _roh:
        _roh = [str(k) for k in sorted(kap)]
    for a in _roh:
        geruest(int(a), kap[int(a)])
