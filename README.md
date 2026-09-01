# Gaaras-Books

Manuskripte in Arbeit, Englisch geschrieben. Ein Ordner je Buch.

## Lot Fourteen

[`lot-fourteen/`](lot-fourteen/) · Band 1 und 2 abgeschlossen (124 Kapitel),
Band 3 begonnen · derzeit ca. 338.000 Woerter

Literarischer Roman, Suedkorea in der Gegenwart, Chaebol-Milieu. Auf einer
illegalen Schulduebernahme-Auktion wird ein Mann, seit seinem neunten Jahr
Eigentum und elfmal weitergereicht, von einer Frau aus dem Chaebol-Umfeld
gekauft. Er wird ihr Schatten: Begleiter, Beobachter, und was sonst nicht
ausgesprochen wird. Ein Kammerspiel um Macht und Kontrolle, getragen von einem,
der nie luegt.

## Transmigration into Freedom

[`transmigration-into-freedom/`](transmigration-into-freedom/) · Kapitel 1 bis 6, ca. 13.000 Woerter

Isekai-Roman. Ein ausgebrannter, verschuldeter Unternehmer von achtunddreissig
legt sich in seinem Buero schlafen und wacht mit neunzehn in einer
mittelalterlichen Welt wieder auf, ein Statusfenster am Rand des Blicks. Kein
Held, sondern ein kuehler Kopf mit einem Koerper, der zum ersten Mal
funktioniert, und der Chance, alles von vorn aufzubauen.

Wer an einem Projekt arbeitet, liest zuerst dessen `CLAUDE.md`.

## Automatik

Erzeugte Dateien werden nicht von Hand gepflegt. Zwei Mechanismen halten sie aktuell:

- **Hook vor jedem Commit.** Einmalig einschalten mit `git config core.hooksPath hooks`.
  Baut neu, legt das Ergebnis in den Commit und bricht bei einem Build-Fehler ab.
  Die Kapitelpruefung warnt nur.
- **Sperrklinke, optional.** `check.py --ratchet` meldet nur, wenn ein Kapitel
  **mehr** Fehler hat als in `.check-baseline` geduldet. Damit bleibt der
  Altbestand erlaubt und neue Verschuldung nicht. Im Hook einschalten mit
  `git config hooks.ratchet true`, Basislinie nachziehen mit
  `python3 check.py --baseline`.
- **GitHub Action bei jedem Push.** Netz darunter, greift auch bei Bearbeitungen
  direkt auf GitHub oder vom Handy.

## Rechte

(c) Gaara. Alle Rechte vorbehalten. Siehe LICENSE. Oeffentlich einsehbar bedeutet
nicht zur Nutzung freigegeben.
