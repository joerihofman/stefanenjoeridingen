from Week2.Opgave3.Board import BoardHelper


class Move:
    @staticmethod
    def get_all_possible_moves(board):
        own_stones, opponent_stones = board.get_neighbors_of_opponent_for_making_a_move_by_the_current_player()
        for own_stone in own_stones:
            for opponent_stone in opponent_stones[own_stones.index(own_stone)]:
                x_direction, y_direction = BoardHelper.calculate_direction(own_stone, opponent_stone)
                next_x = opponent_stone[0] - x_direction
                next_y = opponent_stone[1] - y_direction
                print(next_x.__str__(), next_y.__str__())
        exit(1)

