import random
import string
import collections


class Boggle():

    def makeBoard(size):

        grid = [[random.choice(string.ascii_lowercase) for c in range(size)] for r in range(size)]

        return grid





    board = makeBoard(5)
    for line in board:
        print(line)



