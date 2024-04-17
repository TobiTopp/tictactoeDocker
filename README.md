# Tic Tac Toe Spiel mit Tkinter GUI

Dies ist ein Tic Tac Toe Spiel mit einer grafischen Benutzeroberfläche, das mit Python und dem Tkinter-Modul erstellt wurde. Das Spiel ermöglicht es einem Benutzer, gegen einen anderen Benutzer zu spielen.

# main.py

Dieses Python-Skript enthält den Quellcode für das Tic Tac Toe Spiel sowie Funktionen zum Verwalten von Gewinnern in einer SQLite-Datenbank.

# Datenbank 

Zu dem main.py File ist eine Datenbank connected mit der Tabelle gewinner.db. In dieser Tabelle werden die Gewinner jedes mal nach einer gewonnenen Runde eingetragen.  

# Benutzung

Um das Spiel auszuführen, führe das Skript `main.py` aus. Es wird ein Hauptmenü angezeigt, das die folgenden Optionen enthält:

1. **Gewinner anzeigen:** Zeigt eine Liste der bisherigen Gewinner aus der Datenbank an.
2. **Tic Tac Toe spielen:** Startet das Tic Tac Toe Spiel mit grafischer Benutzeroberfläche.
3. **Beenden:** Beendet das Programm.

Bevor du das Spiel spielen kannst, wirst du aufgefordert, dich mit einem Passwort anzumelden.

Passwort: 1234

# Dockerfile

Das Dockerfile dient dazu, das Tic Tac Toe Spiel in einem Docker-Container auszuführen. Es verwendet das offizielle Python-Image als Basis und installiert die erforderlichen Abhängigkeiten, einschließlich Tkinter für die GUI und SQLite für die Datenbank.

# Verwendung

Um das Docker-Image zu erstellen, führe den folgenden Befehl im Verzeichnis aus, das das Dockerfile und die Dateien `main.py` und `gewinner.db` enthält:

"docker build -t python-tictactoe ."


Um das Spiel im Docker-Container auszuführen, verwende den folgenden Befehl:

"docker run -it python-tictactoe"


Stelle sicher, dass Docker auf deinem System installiert ist und dass du die erforderlichen Berechtigungen hast, um Docker-Befehle auszuführen.

### Wichtiger Hinweis!

Stelle sicher, dass du ein funktionierendes Display hast, wenn du das Spiel mit der grafischen Benutzeroberfläche spielen möchtest. Andernfalls wird das Spiel im Textmodus ausgeführt.

Bei Fragen oder Problemen wende dich bitte an Cem Akkaya oder Tobias Topp.