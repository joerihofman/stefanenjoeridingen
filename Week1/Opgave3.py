class Board:

    def __init__(self):
        self.board = [[1, 0, 0], [0, 5, 0], [0, 0, 9]]

    def print_board(self):
        for row in self.board:
            print(' '.join([str(letter) for letter in row]))

    def change_number(self, x, y):
        None


class Main:
    @staticmethod
    def main():
        board = Board()
        board.print_board()


Main.main()

