class Board:

    def __init__(self):
        self.board = [[1, 0, 0], [0, 5, 0], [0, 0, 9]]
        self.clues = []


    def print_board(self):
        for row in self.board:
            print(' '.join([str(letter) for letter in row]))
        print('')

    def change_number(self, row, col, new_value):
        if self.board[row][col] not in self.clues:
            self.board[col][row] = new_value
            return True
        return False

    def get_postition(self, number):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == number:
                    return row, col

    def get_clues(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] != 0:
                    self.clues.append(self.board[row][col])
        return self.clues





class Main:
    @staticmethod
    def main():
        board = Board()
        board.get_clues()


        board.print_board()

        board.change_number(0, 0, 3)
        board.print_board()


Main.main()

