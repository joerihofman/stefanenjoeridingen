class Board:

    def __init__(self):
        self.board = [[1, 0, 0], [0, 5, 0], [0, 0, 9]]

    def print_board(self):
        for row in self.board:
            print(' '.join([str(letter) for letter in row]))

    def change_numbe(self, x, y):
        None

    def get_postition(self, number):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                print(self.board[row][col])
                if self.board[row][col] == number:
                    return((row, col))




class Main:
    @staticmethod
    def main():
        board = Board()
        board.print_board()

        print(board.get_postition(5))


Main.main()

