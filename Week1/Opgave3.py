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

    def get_neighbors(self, row, col):
        neighbors = []
        length = len(self.board) - 1

        positions = [(row-1, col), (row, col-1), (row, col+1), (row+1, col)]
        for pos in positions:
            row = pos[0]
            col = pos[1]
            if (row and col < length) and (row and col > 0):
                neighbors.append((row, col))
        return neighbors


class Main:
    @staticmethod
    def main():
        board = Board()
        board.print_board()

        print(board.get_neighbors(*board.get_postition(1)))


Main.main()

