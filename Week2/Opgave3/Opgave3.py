from Week2.Opgave3.Board import Board
from Week2.Opgave3.Board import BoardHelper
from Week2.Opgave3.Move import Move

board = Board()
board_helper = BoardHelper()

# board_helper.print_board(board)
# print(board_helper.get_all_neighbors(board.board, 3, 3).__str__())
# board_helper.print_amount_of_each_colour(board)
board_helper.print_board(board)
Move.get_all_possible_moves(board)
# board_helper.flip()


"""
moet krijgen:
(3,2)
(2,3)
(4,5)
(6,4)
(7,6)
"""