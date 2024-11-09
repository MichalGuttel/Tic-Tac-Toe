from board import Board
from player import Player


class Game:
    def __init__(self, player1, player2):
        self._board = Board()
        self.player1 = player1
        self.player2 = player2
        self.turns = player1

    def play(self):
        bool = True
        while bool:
            i = int(input(f"{self.turns._name} enter place between 0-8"))
            while True:
                try:
                    self._board.make_move(self.turns, i)
                except IndexError:
                    print("the index is not between 0-8")
                except ValueError:
                    print("this place is full")
                else:
                    break
                i = int(input(f"{self.turns._name} enter place between 0-8"))
            print(self._board)
            if self._board.is_winner(self.turns.marker):
                print(f"{self.turns._name} is the winner")
                bool = False
            if self._board.is_draw():
                print("game over")
                bool = False
            if self.player1 == self.turns:
                self.turns = self.player2
            else:
                self.turns = self.player1
