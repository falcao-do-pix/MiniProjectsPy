import tkinter as tk
from tkinter import messagebox


class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Jogo da Velha")
        self.geometry("400x400")

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            btn = tk.Button(self, text="", font=("Arial", 24), width=5, height=2,
                            command=lambda i=i: self.on_button_click(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def on_button_click(self, index):
        if self.buttons[index]["text"] == "" and self.check_winner() is None:
            self.buttons[index]["text"] = self.current_player
            self.board[index] = self.current_player
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Fim de Jogo", f"O jogador {winner} venceu!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Fim de Jogo", "É um empate!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]  # Diagonais
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return self.board[combo[0]]
        return None

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button["text"] = ""
        self.current_player = "X"


if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()
