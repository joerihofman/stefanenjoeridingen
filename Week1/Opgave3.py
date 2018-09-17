class Board:
    @staticmethod
    def print_board(board):
        for row in board:
            print(row)


class Main:
    def main(self):
        board = [[1, 0, 0], [0, 5, 0], [0, 0, 9]]
        Board.print_board(board)

