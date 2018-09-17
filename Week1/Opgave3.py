import numpy

class Board:

    def __init__(self):
        # self.board = [[1, 2, 0],
        #               [0, 5, 0],
        #               [0, 0, 9]]

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
        # print(row.__str__() + "  " + col.__str__())
        neighbors = []
        length = len(self.board) - 1

        positions = [(row-1, col), (row, col-1), (row, col+1), (row+1, col)]
        for pos in positions:
            if 0 <= pos[0] <= length and 0 <= pos[1] <= length:
                neighbors.append((pos[0], pos[1]))
        return neighbors

    def is_valid_path(self, paths):
        lastNumber = 0
        for path in paths:
            nextNumber = self.board[path[0]][path[1]]
            if nextNumber == lastNumber + 1:
                lastNumber = nextNumber
            else:
                print('invalid path')
                self.change_number(path[0], path[1], 0)
                return 0
            return 1

    def safe_state(self, list_of_number, path):
        # print(numbers)
        # if numbers[-1] == len(numbers):
        if len(list_of_number) == len(path):
            return True
        else:
            return False

    def dfs(self, row, col, number, path=None, list_of_numbers=None):

        if number == 81:
            self.print_board()
            return True


        if path is None and number == 1:
            path = [(row, col)]
            # print('-------------------path', path)
            list_of_numbers = [number]

        else:
            path.append((row, col))
            # print('-------------------path', path)
            # self.change_number(row, col, number)
            # if number not in list_of_numbers:
            list_of_numbers.append(number)
            # print('----------------', list_of_numbers)

            # self.change_number(row, col, number)


            if number in self.clues:
                print(number)
                # if number == 7:
                    # print(self.board[row][col])
                # if self.board[row][col] != 0:
                if self.board[row][col] == number:
                        # print(path)
                        self.print_board()
                else:
                    # print(path)
                    # print(path[-1])

                    rrow = path[-1][0]
                    rcol = path[-1][1]
                    self.change_number(rrow, rcol, 0)
                    self.print_board()

                    return
            else:
                self.change_number(row, col, number)
                self.print_board()



            # if number in self.clues:
            #     print(self.board[row][col])
            #     # self.change_number(row, col, number)
            #     if self.safe_state(list_of_numbers, path):
            #         if self.board[row][col] != number:
            #             list_of_numbers.pop()
            #             return
            #         else:
            #             self.change_number(row, col, number)
            #             self.print_board()
            #     else:
            #         list_of_numbers.pop()
            #         return
            #
            #
            #
            # else:
            #     if self.safe_state(list_of_numbers, path):
            #         print('')
            #         self.change_number(row, col, number)
            #     else:
            #         list_of_numbers.pop()
            #         return
            #         # self.change_number(row, col, 0)
            #         print

                # self.change_number(row, col, number)

                # if self.safe_state(list_of_numbers, path):

                    # self.change_number(row, col, number)
                    # self.print_board()
                # else:
                #     list_of_numbers.pop()
                #     return



        for child in self.get_neighbors(row, col):
            if child not in path:
                # print('@@@@@@@@@@@@@@', number + 1)

                # print('!!!!!!!!!!!--_________________---------------', number)
                if self.dfs(child[0], child[1], number+1, path[:], list_of_numbers):
                    return True
        return False

    # def dfs(self, path=None, row, col, number):

        # if number > self.board
    def solve(self, number):
        row = self.get_postition(number)[0]
        # print(row)
        col = self.get_postition(number)[1]
        # print(col)
        self.dfs(row, col, number)


class Main:
    @staticmethod
    def main():
        board = Board()
        # board.print_board()

        # paths = [(0,0), (1,0), (0,1), (0,2)]
        # numbers = [1, 2, 3]
        # print(board.safe_state(numbers))

        board.get_clues()
        print(board.clues)
        # print(board.get_neighbors(*board.get_postition(5)))
        # print(paths)
        # board.is_valid_path(paths)
        board.solve(1)
        board.print_board()

        # print(board[0][0])
        # print(board[0][1])
        # print(board[0][2])
        # print(board.board[0][0])
        # print(board.board[0][1])
        # print(board.board[0][2])
        # print(board.board[1][0])
        # print(board.board[1][1])
        # print(board.board[1][2])


Main.main()

