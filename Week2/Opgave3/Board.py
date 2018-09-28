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
        if BoardHelper().is_legal_move(self.board, x, y):
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
    @staticmethod
    def calculate_direction(original, new):
        x_direction = int(original[0]) - int(new[0])
        y_direction = int(original[1]) - int(new[1])

        return x_direction, y_direction

    @staticmethod
    def get_possible_moves_considering_opponent(board, current_player, opponent):
        current_player_stones = []
        opponent_player_stones = []
        new_list = []
        one_list = []
        other_fckn_list = []

        for row in board:
            for column in row:
                if column == current_player:
                    current_player_stones.append((board.index(row), row.index(column)))

        for stone in current_player_stones:
            opponent_player_stones.append(BoardHelper.get_opponent_neighbors(board, *stone, opponent))

        for stone_here in opponent_player_stones:
            for stone in stone_here:
                new_list.append(BoardHelper.get_opponent_neighbors(board, *stone, opponent))

        for l in new_list:
            for point in l:
                one_list.append(point)

        print(one_list)

        for point in one_list:
            for liste in opponent_player_stones:
                for list_WAAROM_MOET_DIT in opponent_player_stones:
                    if point not in liste and point not in list_WAAROM_MOET_DIT:
                        other_fckn_list.append(point)

        print("other :   " + other_fckn_list.__str__())

        print("opponent initial: " + opponent_player_stones.__str__())
        and_a_new_fckn_list = list(set(other_fckn_list))

        print(and_a_new_fckn_list)
        exit(1)

        return current_player_stones, opponent_player_stones

    @staticmethod
    def get_opponent_neighbors(board, x, y, opponent):
        all_neighbors = BoardHelper.get_all_neighbors(board, x, y)
        neighboring_opponent_stones = []
        for neighbor in all_neighbors:
            for row in board:
                for column in row:
                    if column == opponent and (board.index(row), row.index(column)) == neighbor:
                        neighboring_opponent_stones.append((board.index(row), row.index(column)))
        return neighboring_opponent_stones

    @staticmethod
    def get_all_neighbors(board, x, y):
        neighbors = []
        length = len(board) - 1

        positions = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y),
                     (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]
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
    def is_legal_move(board, x, y):
        if board[x][y] == Tile.EMPTY:
            return True
        else:
            return False

