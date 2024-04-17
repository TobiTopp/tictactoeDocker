import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

def start_tictactoe():
    if "DISPLAY" not in os.environ:
        print("Kein Display verfügbar. Das Programm wird im Textmodus ausgeführt.")
        return

    root = tk.Tk()
 
def create_table():
    conn = sqlite3.connect('gewinner.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS gewinner
                 (id INTEGER PRIMARY KEY, gewinner TEXT)''')
    conn.commit()
    conn.close()

def insert_winner(winner):
    conn = sqlite3.connect('gewinner.db')
    c = conn.cursor()
    c.execute("INSERT INTO gewinner (gewinner) VALUES (?)", (winner,))
    conn.commit()
    conn.close()

def get_winners():
    conn = sqlite3.connect('gewinner.db')
    c = conn.cursor()
    c.execute("SELECT * FROM gewinner")
    winners = c.fetchall()
    conn.close()
    return winners

def start_tictactoe():
    def check_winner(board):
        for row in board:
            if len(set(row)) == 1 and row[0] != "":
                return row[0]
        for col in range(3):
            if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != "":
                return board[0][col]
        if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != "":
            return board[0][0]
        if len(set([board[i][2 - i] for i in range(3)])) == 1 and board[0][2] != "":
            return board[0][2]
        return None

    def on_click(row, col):
        nonlocal turn, board, winner
        if board[row][col] == "" and not winner:
            board[row][col] = turn
            buttons[row][col].config(text=turn, state="disabled", font=("Helvetica", 17, "bold"))
            if check_winner(board) == turn:
                messagebox.showinfo("Gewinner", f"{turn} hat gewonnen!")
                insert_winner(turn)
                winner = turn
                reset_game()  # Spielfeld zurücksetzen
            elif all(board[i][j] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Unentschieden", "Das Spiel endete unentschieden!")
                reset_game()  # Spielfeld zurücksetzen
            else:
                turn = "O" if turn == "X" else "X"
                label.config(text=f"Nächster Spieler: {turn}")

    def reset_game():
        nonlocal turn, board, winner
        for i in range(3):
            for j in range(3):
                board[i][j] = ""
                buttons[i][j].config(text="", state="normal", font=("Helvetica", 16))
        winner = None
        turn = "X"
        label.config(text="Nächster Spieler: X")

    root = tk.Tk()
    root.title("Tic Tac Toe")

    label = tk.Label(root, text="Nächster Spieler: X", font=("Helvetica", 20))
    label.grid(row=3, columnspan=3, pady=10)

    buttons = [[None, None, None] for _ in range(3)]
    board = [["" for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, command=lambda row=i, col=j: on_click(row, col), width=6, height=2,
                                      font=("Helvetica", 16), bg="#f0f0f0", activebackground="#dcdcdc")
            buttons[i][j].grid(row=i, column=j)

    reset_button = tk.Button(root, text="Neues Spiel", command=reset_game, font=("Helvetica", 14), bg="#4caf50", fg="white")
    reset_button.grid(row=4, columnspan=3, pady=10)

    winner = None
    turn = "X"

    root.mainloop()

def main_menu():
    create_table()
    while True:
        print("")
        print("")
        print("--Hauptmenü--")
        print("")
        print("1. Gewinner anzeigen")
        print("2. Tic Tac Toe spielen")
        print("3. Beenden")

        choice = input("Bitte wähle eine Option: ")

        if choice == "1":
            winners = get_winners()
            if winners:
                print("")
                print("")
                print("Bisherige Gewinner:")
                print("")
                for winner in winners:
                    print(winner[1])
            else:
                print("Es gibt noch keine Gewinner.")
        elif choice == "2":
            start_tictactoe()
        elif choice == "3":
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Option. Bitte wähle erneut.")


def safe_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        return None
    
def login():
    valid_password = "1234"
    while True:
        print("")
        print("")
        print("--Login--")
        print("")
        password = safe_input("Passwort: ")
        if password is None:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")
        elif password == valid_password:
            print("Login erfolgreich!")
            return True
        else:
            print("Ungültige Anmeldeinformationen. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    if login():
        main_menu()