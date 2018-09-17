class Board:
    @staticmethod
    def print_board(board):
        # print('[%s]' % ', '.join(map(str, board)))
        for row in board:
            print(row)


class Main:
    def main(self):
        board = [[1, 0, 0], [0, 5, 0], [0, 0, 9]]
        # board = Board.board
        Board.print_board(board)

