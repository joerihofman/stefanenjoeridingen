from Week2.Opgave3.Tile import Tile


class Board:
    board = []

    def __init__(self):
        self.current_player = Tile.BLACK
        self.opponent = Tile.WHITE
        self.board = [[Tile.EMPTY for x in range(8)] for y in range(8)]

        self.board[3][3] = Tile.WHITE
        self.board[4][4] = Tile.WHITE
        self.board[3][4] = Tile.BLACK
        self.board[4][3] = Tile.BLACK
        self.board[5][4] = Tile.WHITE
        self.board[6][5] = Tile.WHITE

    def make_move(self, x, y):
        if BoardHelper().is_legal_direction(self.board, x, y):
            self.board[x][y] = self.current_player
            self.other_player_turn()

    def other_player_turn(self):
        if self.current_player == Tile.BLACK:
            self.current_player = Tile.WHITE
            self.opponent = Tile.BLACK
        else:
            self.current_player = Tile.BLACK
            self.opponent = Tile.WHITE

    def get_neighbors_of_opponent_for_making_a_move_by_the_current_player(self):
        return BoardHelper().get_possible_moves_considering_opponent(self.board, self.current_player, self.opponent)


class BoardHelper:
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    @staticmethod
    def get_possible_moves_considering_opponent(board, current_player, opponent):
        current_player_stones = []
        direct_opponent_neighbors = []

        for row in board:
            for column in row:
                if column == current_player:
                    current_player_stones.append((board.index(row), row.index(column)))

        BoardHelper.do_things_for_directions(board, current_player_stones, opponent)

        # for stone in current_player_stones:
        #     direct_opponent_neighbors.append(BoardHelper.get_opponent_neighbors(board, stone[0], stone[1], opponent))

        # for i in range(len(current_player_stones)):
        #     neighbors = current_player_stones[i]
        #     for j in direct_opponent_neighbors[i]:
        #         print(BoardHelper.calculate_direction(neighbors, j))

        print("current player: " + current_player_stones.__str__())
        print("opponent stones: " + direct_opponent_neighbors.__str__())
        exit(1)

        return current_player_stones

    @staticmethod
    def do_things_for_directions(board, own_stones, opponent):
        for stone in own_stones:
            for direction in BoardHelper.directions:
                direction_x = stone[0] - direction[0]
                direction_y = stone[1] - direction[1]

                BoardHelper.weer_een_nieuwe(board, direction_x, direction_y, stone, opponent)



    @staticmethod
    def weer_een_nieuwe(board, direction_x, direction_y, start_stone, opponent):
        empty_location = 0
        if board[direction_x][direction_y]:
            new_x = start_stone[0] - direction_x
            new_y = start_stone[1] - direction_y

            new_stone_x = 0
            new_stone_y = 0


            if BoardHelper.is_legal_direction(board, direction_x, direction_y, opponent):
                new_stone_x =

                new_stone = (new_stone_x, new_stone_y)
                    BoardHelper.weer_een_nieuwe(board, direction_x, direction_y, new_stone, opponent)
            else:
                return False
        return empty_location

    @staticmethod
    def calculate_direction(original, new):
        x_direction = int(original[0]) - int(new[0])
        y_direction = int(original[1]) - int(new[1])

        return x_direction, y_direction

    @staticmethod
    def get_all_directions(board, x, y):
        neighbors = []
        length = len(board) - 1

        positions = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]
        for pos in positions:
            if 0 <= pos[0] <= length and 0 <= pos[1] <= length:
                neighbors.append((pos[0], pos[1]))
        return neighbors

    @staticmethod
    def print_amount_of_each_colour(board):
        whites = 0
        blacks = 0
        for row in board.board:
            for column in row:
                if column == Tile.BLACK:
                    blacks += 1
                elif column == Tile.WHITE:
                    whites += 1
        print("Black: " + blacks.__str__() + " - White: " + whites.__str__())

    @staticmethod
    def print_board(board):
        for row in board.board:
            print(' '.join([colour.value for colour in row]))
        print('')

    @staticmethod
    def is_legal_direction(board, x, y, opponent):
        #mag niet leeg zijn en moet opponent zijn
        if board[x][y] != Tile.EMPTY and board[x][y] == opponent:
            return True
        else:
            return False

