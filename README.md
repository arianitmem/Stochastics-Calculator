# Wahrscheinlichkeitsrechner

Dieses Projekt enthält einen einfachen Lotto-Simulator in Python.

## Beschreibung

Das Skript `stochastik.py` erlaubt dir, 6 Zahlen einzugeben. Anschließend zieht der Computer wiederholt zufällige Lottozahlen (6 aus 1-49) und zählt, wie viele Übereinstimmungen es gibt.

Das Programm endet, sobald alle 6 Zahlen übereinstimmen (Jackpot), und gibt die Anzahl der Versuche aus.

## Voraussetzungen

- Python 3.x

## Nutzung

1. Öffne ein Terminal im Ordner des Projekts.
2. Starte das Skript mit:

```bash
python stochastik.py
```

3. Gib nacheinander 6 Zahlen ein, wenn du dazu aufgefordert wirst.
4. Warte, bis die Simulation den Jackpot findet.

## Hinweise

- Die Wahrscheinlichkeit, den Jackpot zufällig zu treffen, ist sehr gering. Das Programm kann daher viele Iterationen dauern.
- Der Zufallsgenerator verwendet `random.sample`, um sechs unterschiedliche Zahlen aus dem Bereich 1 bis 49 zu ziehen.

## Verbesserungsmöglichkeiten

- Eingabevalidierung für Zahlenbereich und Duplikate.
- Begrenzung der Anzahl der Simulationen.
- Ausgabe von Teiltreffern (3, 4, 5 Richtige).