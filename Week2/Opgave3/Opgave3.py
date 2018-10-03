from Week2.Opgave3.Board import Board
from Week2.Opgave3.Board import BoardHelper
from Week2.Opgave3.Move import Move

board = Board()
board_helper = BoardHelper()

# print(board_helper.get_all_neighbors(board.board, 3, 3).__str__())
board.print_board()
while not board.check_end_state():
    Move.random_move(board, board_helper)

