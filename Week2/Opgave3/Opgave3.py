from Week2.Opgave3.Board import Board
from Week2.Opgave3.Board import BoardHelper
from Week2.Opgave3.Move import Move

board = Board()
board_helper = BoardHelper()

# board_helper.print_board(board)
print(board_helper.get_all_neighbors(board.board, 3, 3).__str__())
board_helper.amount_of_each_colour(board)
board_helper.print_board(board)
board.get_neighbors_of_opponent_for_making_a_move_by_the_current_player(3, 3)
