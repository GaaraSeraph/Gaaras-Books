# Gaaras-Books

Manuskripte in Arbeit. Ein Ordner je Buch.

| Projekt | Stand | Umfang |
|---|---|---|
| [`lot-fourteen/`](lot-fourteen/) | Kapitel 1 bis 17 | ca. 50.000 Woerter |

Wer an einem Projekt arbeitet, liest zuerst dessen `CLAUDE.md`.

## Automatik

Erzeugte Dateien werden nicht von Hand gepflegt. Zwei Mechanismen halten sie aktuell:

- **Hook vor jedem Commit.** Einmalig einschalten mit `git config core.hooksPath hooks`.
  Baut neu, legt das Ergebnis in den Commit und bricht bei einem Build-Fehler ab.
  Die Kapitelpruefung warnt nur.
- **GitHub Action bei jedem Push.** Netz darunter, greift auch bei Bearbeitungen
  direkt auf GitHub oder vom Handy.

## Rechte

(c) Gaara. Alle Rechte vorbehalten. Siehe LICENSE. Oeffentlich einsehbar bedeutet
nicht zur Nutzung freigegeben.
