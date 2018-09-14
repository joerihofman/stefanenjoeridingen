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

# class Search():
#     @staticmethod
#     def look_for_neighbors(x_letter, y_letter):


board = Testboard().get_board()
# for line in board:
#     print(line)

X=7
Y=7

neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                           for y2 in range(y-1, y+2)
                           if (-1 < x <= X and
                               -1 < y <= Y and
                               (x != x2 or y != y2) and
                               (0 <= x2 <= X) and
                               (0 <= y2 <= Y))]

print(neighbors(2,2))


    # with open('words.txt', 'rt', encoding='utf-8') as f:
    #     print(f.read())