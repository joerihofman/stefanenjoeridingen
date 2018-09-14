import random
import string


class Board():

    filled_board = []

    def __init__(self, size):
        self.filled_board = [[random.choice(string.ascii_lowercase) for c in range(size)] for r in range(size)]

    def get_board(self):
        return self.filled_board


class Boggle():

    board = Board(5)
    for line in board.get_board():
        print(line)

