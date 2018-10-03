import random


class Move:
    @staticmethod
    def random_move(board, board_helper):
        list_of_things = board.get_neighbors_of_opponent_for_making_a_move_by_the_current_player()
        if len(list_of_things) != 0:
            random_index_for_list = random.randint(0, len(list_of_things)-1)
            item_start = list_of_things[random_index_for_list][0]
            for combination in list_of_things:
                if combination[0] == item_start:
                    board.flip_stones(combination[0], combination[1], combination[2])
        Move.do_things_after_move(board, board_helper)

    @staticmethod
    def negamax(board, board_helper):
        pass

    @staticmethod
    def do_things_after_move(board, board_helper):
        board.other_player_turn()
        board.print_board()
        print(board.current_player)
        board_helper.print_amount_of_each_colour(board)


