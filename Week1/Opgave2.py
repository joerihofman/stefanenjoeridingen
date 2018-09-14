import random
import string


class Board():

    filled_board = []

    def __init__(self, size):
        self.filled_board = [[random.choice(string.ascii_lowercase) for c in range(size)] for r in range(size)]

    def get_board(self):
        return self.filled_board

class Testboard():

    filled_board = []

    def __init__(self):
        line_one = ['a', 'c', 'h', 't', 'x', 'x', 'o']
        line_two = ['o', 'g', 'e', 'n', 'x', 'x', 'l']
        line_three = ['c', 'e', 's', 'k', 'p', 'a', 'i']
        line_four = ['x', 'x', 'x', 'o', 'x', 'x', 'e']
        line_five = ['x', 'x', 'h', 'x', 'x', 'x', 'x']
        line_six = ['x', 'c', 'x', 'o', 'x', 'x', 'x']
        line_seven = ['s', 'x', 'x', 'x', 'm', 'x', 'x']

        self.filled_board = [line_one, line_two, line_three, line_four, line_five, line_six, line_seven]

    def get_board(self):
        return self.filled_board


class Boggle():

    board = Testboard()
    for line in board.get_board():
        print(line)

    with open('words.txt', 'rt', encoding='utf-8') as f:
        print(f.read())