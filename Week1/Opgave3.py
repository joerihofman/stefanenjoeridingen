class Board:

    def __init__(self):
        self.board = [[1, 0, 0], [0, 5, 0], [0, 0, 9]]

    def print_board(self):
        for row in self.board:
            print(' '.join([str(letter) for letter in row]))
        print('')

    def change_number(self, x, y, new_value):
        if self.board[x][y] == 0:
            self.board[x][y] = new_value
            return True
        return False

    def get_postition(self, number):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == number:
                    return row, col


class Main:
    @staticmethod
    def main():
        board = Board()
        board.print_board()


Main.main()

