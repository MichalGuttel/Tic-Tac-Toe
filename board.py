class Board:
    def __init__(self):
        self.board_game = [' '] * 9

    def __str__(self):
        return (
            f"\n|{self.board_game[0]}|{self.board_game[1]}|{self.board_game[2]}|\n------\n|{self.board_game[3]}|{self.board_game[4]}|{self.board_game[5]}|\n------\n|{self.board_game[6]}|{self.board_game[7]}|{self.board_game[8]}|\n------\n")

    # def is_empty(self, place):
    #     if self.board_game[place] != ' ':
    #         raise ValueError

    # def make_move(self, player, place):
    #
    #     if self.board_game[place] != ' ':
    #         raise ValueError
    #     else:
    #         self.board_game[place] = player.marker

    def make_move(self, player, place):
        if self.board_game[place] != ' ':
            raise ValueError
        if place>8 and place<0:
            raise IndexError
        self.board_game[place] = player.marker

    def is_winner(self,marker):
        for i in range(3):
            if self.board_game[0 + i * 3] == marker and self.board_game[1 + i * 3] == marker and  self.board_game[2 + i * 3] == marker:
                return True
            elif self.board_game[0 + i] == marker and self.board_game[3 + i] == marker and marker == self.board_game[6+i]:
                return True
        if self.board_game[4] == marker:
            if self.board_game[0] == self.board_game[4] and self.board_game[4] == self.board_game[8]:
                    return True
            elif self.board_game[2] == self.board_game[4] and self.board_game[4] == self.board_game[6]:
                    return True
        return False


    def is_draw(self):
        return ' ' not in self.board_game
