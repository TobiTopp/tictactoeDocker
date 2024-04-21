

```markdown
# Tic Tac Toe Spiel mit Tkinter GUI

## Übersicht
Dieses Projekt umfasst ein Tic Tac Toe Spiel, das in Python mit dem Tkinter-Modul entwickelt wurde. Es bietet eine grafische Benutzeroberfläche und ermöglicht es zwei Spielern, gegeneinander anzutreten.

## Hauptskript (main.py)
Das Skript `main.py` enthält den gesamten Quellcode des Spiels sowie Funktionen zur Verwaltung einer SQLite-Datenbank (`gewinner.db`), die dazu dient, die Gewinner jeder Runde zu speichern.

## Datenbank
Die Datenbank `gewinner.db` ist mit dem Hauptskript verbunden und speichert die Namen der Gewinner nach jedem Spiel.

## Installation und Verwendung
Um das Spiel zu starten, muss zuerst das Skript `main.py` ausgeführt werden. Das Hauptmenü bietet folgende Optionen:

- **Gewinner anzeigen**: Listet alle gespeicherten Gewinner aus der Datenbank auf.
- **Tic Tac Toe spielen**: Startet das Spiel mit der grafischen Benutzeroberfläche.
- **Beenden**: Schliesst die Anwendung.

### Passwortschutz
Bevor das Spiel gestartet wird, ist die Eingabe des folgenden Passworts erforderlich:
```
Passwort: 1234
```

## Docker-Konfiguration
Das Dockerfile im Repository setzt das offizielle Python-Image als Basis ein und installiert alle erforderlichen Abhängigkeiten, einschliesslich Tkinter und SQLite.

### Erstellen des Docker-Images
Führe den folgenden Befehl im Verzeichnis mit dem Dockerfile und den Dateien `main.py` und `gewinner.db` aus:
```bash
docker build -t python-tictactoe .
```

### Ausführen des Docker-Containers
Um das Spiel im Docker-Container zu starten, verwende:
```bash
docker run -it python-tictactoe
```

Stelle sicher, dass Docker auf deinem System korrekt installiert ist und du die notwendigen Rechte zur Ausführung von Docker-Befehlen hast.

## Wichtige Hinweise
Für die Nutzung der grafischen Benutzeroberfläche ist ein funktionierendes Display notwendig. Fehlt ein solches, wird das Spiel im Textmodus ausgeführt.

## Support
Bei Fragen oder Problemen zu diesem Projekt kannst du dich jederzeit an Cem Akkaya oder Tobias Topp wenden.
```

