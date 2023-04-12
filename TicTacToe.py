from colorama import Fore  # Console text colors.
from time import sleep  # Delay for game.


class TTT(object):

    def __init__(self):
        # Maybe improve the int to str things?
        self.board = [None, '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.its_X_turn = True
        self.did_game_end = False
        self.turn_count = 0

        self.start_game()

    def start_game(self):
        self.clear_board()
        self.print_board()
        while not self.did_game_end:
            self.player_turn()
            self.print_board()
            self.check_for_winner()

    def player_turn(self):
        if self.its_X_turn:
            player = "X"
        else:
            player = "O"

        while True:
            try:
                player_move = int(input(Fore.BLUE + f"Select a tile ({player}): "))
            except ValueError:
                continue
            # is it okay to compare strings with ==?
            if (0 < player_move < 10) and (self.board[player_move] == " "):
                self.board[player_move] = player
                break

        self.its_X_turn = not self.its_X_turn
        self.turn_count += 1

    def check_for_winner(self):
        # Did X win?
        if (
                # Horizontally.
                ((self.board[1] == "X") and (self.board[2] == "X") and (self.board[3] == "X")) or
                ((self.board[4] == "X") and (self.board[5] == "X") and (self.board[6] == "X")) or
                ((self.board[7] == "X") and (self.board[8] == "X") and (self.board[9] == "X")) or
                # Diagonally.
                ((self.board[1] == "X") and (self.board[5] == "X") and (self.board[9] == "X")) or
                ((self.board[3] == "X") and (self.board[5] == "X") and (self.board[7] == "X")) or
                # Vertically.
                ((self.board[1] == "X") and (self.board[4] == "X") and (self.board[7] == "X")) or
                ((self.board[2] == "X") and (self.board[5] == "X") and (self.board[8] == "X")) or
                ((self.board[3] == "X") and (self.board[6] == "X") and (self.board[9] == "X"))):
            print(Fore.RED + "\nX won the game!" + Fore.WHITE)
            self.did_game_end = True

            # Did O win?
        elif (
                # Horizontally.
                ((self.board[1] == "O") and (self.board[2] == "O") and (self.board[3] == "O")) or
                ((self.board[4] == "O") and (self.board[5] == "O") and (self.board[6] == "O")) or
                ((self.board[7] == "O") and (self.board[8] == "O") and (self.board[9] == "O")) or
                # Diagonally.
                ((self.board[1] == "O") and (self.board[5] == "O") and (self.board[9] == "O")) or
                ((self.board[3] == "O") and (self.board[5] == "O") and (self.board[7] == "O")) or
                # Vertically.
                ((self.board[1] == "O") and (self.board[4] == "O") and (self.board[7] == "O")) or
                ((self.board[2] == "O") and (self.board[5] == "O") and (self.board[8] == "O")) or
                ((self.board[3] == "O") and (self.board[6] == "O") and (self.board[9] == "O"))):
            print(Fore.GREEN + "\nO won the game!" + Fore.WHITE)
            self.did_game_end = True

        # Is it a tie?
        elif self.turn_count == 9:
            print(Fore.YELLOW + "\nIt's a tie!" + Fore.WHITE)
            self.did_game_end = True

    def print_board(self):
        print(Fore.LIGHTBLACK_EX +
              f"""
 {self.board[1]} | {self.board[2]} | {self.board[3]}
-----------
 {self.board[4]} | {self.board[5]} | {self.board[6]}
-----------
 {self.board[7]} | {self.board[8]} | {self.board[9]}
""" + Fore.WHITE)

    def clear_board(self):
        self.board.clear()
        self.board.append(None)
        # Use ine liner!!!!
        for i in range(9):
            self.board.append(" ")

    @staticmethod
    def rules():
        print(
            """
hello to the tic tac toe game!

Here are the rules:
1. X starts the game.
2. According to the board below choose your tile (1-9).
3. Exchange turns until the game ends.

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

Have fun! :)

------------------------------------""")


TTT.rules()
while True:
    TTT()
    sleep(1.5)
