import tkinter as tk
from tkinter import messagebox
import numpy as np


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Initialize the board and player
        self.board = initialize_board()
        self.turn = "X"

        # Create a frame for the game board
        self.frame = tk.Frame(root, bg="lightblue")
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        # Create buttons with colors
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c] = tk.Button(self.frame, text="", font=("Helvetica", 24, "bold"), width=6, height=3,
                                               command=lambda r=r, c=c: self.make_move(r, c), bg="white", fg="black")
                self.buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game, font=("Helvetica", 16),
                                      bg="lightgray", fg="black")
        self.reset_button.grid(row=1, column=0, pady=10)

    def reset_game(self):
        self.board = initialize_board()
        self.turn = "X"
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", state=tk.NORMAL, bg="white", fg="black")

    def make_move(self, r, c):
        if self.board[r][c] == '':
            self.board[r][c] = self.turn
            if self.turn == "X":
                self.buttons[r][c].config(text="X", bg="lightcoral", fg="white")
            else:
                self.buttons[r][c].config(text="O", bg="lightseagreen", fg="white")
            self.buttons[r][c].config(state=tk.DISABLED)
            if check_win(self.board, self.turn):
                self.show_popup(f"{self.turn} wins!", "Congratulations!")
                self.disable_buttons()
            elif is_draw(self.board):
                self.show_popup("It's a draw!", "Game Over")
                self.disable_buttons()
            else:
                self.turn = "O" if self.turn == "X" else "X"
                if self.turn == "O":
                    ai_move = best_move(self.board)
                    if ai_move:
                        self.board[ai_move[0]][ai_move[1]] = "O"
                        self.buttons[ai_move[0]][ai_move[1]].config(text="O", bg="lightseagreen", fg="white",
                                                                    state=tk.DISABLED)
                        if check_win(self.board, "O"):
                            self.show_popup("AI wins!", "Game Over")
                            self.disable_buttons()
                        elif is_draw(self.board):
                            self.show_popup("It's a draw!", "Game Over")
                            self.disable_buttons()
                        else:
                            self.turn = "X"

    def disable_buttons(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(state=tk.DISABLED)

    def show_popup(self, message, title):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("300x150")
        popup.configure(bg="lightyellow")
        label = tk.Label(popup, text=message, font=("Helvetica", 16, "bold"), bg="lightyellow")
        label.pack(pady=20)
        ok_button = tk.Button(popup, text="OK", font=("Helvetica", 12), command=popup.destroy, bg="lightgray",
                              fg="black")
        ok_button.pack(pady=10)


def initialize_board():
    return np.full((3, 3), '')


def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def is_draw(board):
    return all([cell != '' for row in board for cell in row])


def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == '']


def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -np.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = ''
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = np.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = ''
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def best_move(board):
    best_val = -np.inf
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'
        move_val = minimax(board, 0, False, -np.inf, np.inf)
        board[move[0]][move[1]] = ''
        if move_val > best_val:
            best_val = move_val
            best_move = move
    return best_move


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="lightblue")
    game = TicTacToe(root)
    root.mainloop()
