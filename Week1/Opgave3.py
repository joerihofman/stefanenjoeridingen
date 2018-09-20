class Board:

    def __init__(self):
        self.board = [[7, 0, 3, 0, 1, 0, 59, 0, 81],
                      [0, 0, 0, 33, 34, 57, 0, 0, 0],
                      [9, 0, 31, 0, 0, 0, 63, 0, 79],
                      [0, 29, 0, 0, 0, 0, 0, 65, 0],
                      [11, 12, 0, 0, 39, 0, 0, 66, 77],
                      [0, 13, 0, 0, 0, 0, 0, 67, 0],
                      [15, 0, 23, 0, 0, 0, 69, 0, 75],
                      [0, 0, 0, 43, 42, 49, 0, 0, 0],
                      [19, 0, 21, 0, 45, 0, 47, 0, 73]
                      ]
        self.clues = []

    def print_board(self):
        for row in self.board:
            print(' '.join([str(letter) for letter in row]))
        print('')

    def change_number(self, row, col, new_value):
        if self.board[row][col] not in self.clues:
            self.board[row][col] = new_value
            return True
        return False

    def get_position(self, number):
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
            if 0 <= pos[0] <= length and 0 <= pos[1] <= length:
                neighbors.append((pos[0], pos[1]))
        return neighbors

    def dfs(self, row, col, number, path=None):
        if number == (len(self.board) * len(self.board)):
            self.print_board()
            return True

        if path is None and number == 1:
            path = [(row, col)]

        else:
            path.append((row, col))

            if number in self.clues:
                if self.board[row][col] == number:
                        self.print_board()
                else:
                    rrow = path[-1][0]
                    rcol = path[-1][1]
                    self.change_number(rrow, rcol, 0)
                    self.print_board()
                    return
            else:
                self.change_number(row, col, number)
                self.print_board()

        for child in self.get_neighbors(row, col):
            if child not in path and self.dfs(child[0], child[1], number+1, path[:]):
                return True
        return False

    def solve(self, number):
        row = self.get_position(number)[0]
        col = self.get_position(number)[1]
        self.dfs(row, col, number)


class Main:
    @staticmethod
    def main():
        board = Board()
        board.get_clues()

        print(board.clues)

        board.solve(1)
        board.print_board()


Main.main()

