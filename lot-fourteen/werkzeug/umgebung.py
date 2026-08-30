#!/usr/bin/env python3
"""umgebung.py - jede Sprechbefehl-Stelle mit ihren Nachbarzeilen.

Beim Ersetzen ist die Zuordnung aus `sprechbefehl.py` nicht genug: sie rutscht
an Szenenkanten, und beim Lesen sind schon sechs Fehlmeldungen aufgefallen -
drei angebliche Woo-Stellen gehoerten Georgij, eine angebliche Jang-Stelle
gehoerte Sang-hoon. **Wer eine Zeile aendert, ohne die Nachbarzeilen zu sehen,
legt sie irgendwann der falschen Figur in den Mund.**

Dieses Skript druckt deshalb je Fund die Replik davor und die Antwort danach.
Zwei Zeilen reichen fast immer, um zu sehen, wer spricht.

    python3 umgebung.py b2 36 43        Kapitel 36 bis 43 aus Band 2
    python3 umgebung.py b1 20 28
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sprechbefehl as sb


def dump(band, von, bis):
    ziel = set('%s %02d' % (band, n) for n in range(von, bis + 1))
    treffer = [s for s in sb.stellen() if s[0] in ziel]
    if not treffer:
        print('Keine Stelle in %s %02d bis %02d.' % (band, von, bis))
        return 0

    ordner = {'b1': 'chapters', 'b2': 'chapters-2', 'b3': 'chapters-3'}[band]
    cache = {}
    letzte_marke = None
    for marke, datei, nr, wer, replik in treffer:
        if datei not in cache:
            with open(os.path.join(sb.WURZEL, ordner, datei), encoding='utf-8') as f:
                cache[datei] = f.read().split('\n')
        zeilen = cache[datei]
        if marke != letzte_marke:
            print('\n######## %s   %s' % (marke, datei))
            letzte_marke = marke

        def nachbar(start, schritt):
            """Die naechste nichtleere Zeile, die kein Trenner ist."""
            i = start + schritt
            while 0 <= i < len(zeilen):
                s = zeilen[i].strip()
                if s and s not in ('---', '* * *'):
                    return s
                i += schritt
            return ''

        print('  Z%-4d [%s]' % (nr, wer))
        print('     vor : %s' % nachbar(nr - 1, -1)[:150])
        print('     >>>   %s' % zeilen[nr - 1].strip()[:150])
        print('     nach: %s' % nachbar(nr - 1, 1)[:150])
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    sys.exit(dump(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))
