from Week2.Opgave3.Tile import Tile


class Board:
    def __init__(self):
        self.current_player = Tile.BLACK
        self.opponent = Tile.WHITE
        self.board = [[Tile.EMPTY for x in range(8)] for y in range(8)]

        self.board[3][3] = Tile.WHITE
        self.board[4][4] = Tile.WHITE
        self.board[3][4] = Tile.BLACK
        self.board[4][3] = Tile.BLACK

    def other_player_turn(self):
        if self.current_player == Tile.BLACK:
            self.current_player = Tile.WHITE
            self.opponent = Tile.BLACK
        else:
            self.current_player = Tile.BLACK
            self.opponent = Tile.WHITE

    def get_neighbors_of_opponent_for_making_a_move_by_the_current_player(self):
        return BoardHelper().get_possible_moves_considering_opponent(self.board, self.current_player, self.opponent)

    def print_board(self):
        print('')
        for row in self.board:
            print(' '.join([colour.value for colour in row]))
        print('')

    def flip_stones(self, begin, end, direction):
        x = begin[0]
        y = begin[1]
        if direction[0] == 0:
            while y != end[1]:
                self.board[x][y] = self.current_player
                y += direction[1]
        elif direction[1] == 0:
            while x != end[0]:
                self.board[x][y] = self.current_player
                x += direction[0]
        else:
            while x != end[0] and y != end[1]:
                self.board[x][y] = self.current_player
                x += direction[0]
                y += direction[1]

    def check_end_state(self):
        for row in self.board:
            for column in row:
                if column == Tile.EMPTY:
                    return False
        return True


class BoardHelper:
    @staticmethod
    def get_possible_moves_considering_opponent(board, current_player, opponent):
        mogelijk_begin_en_eind = []

        filtered_empty_places_with_opponent_neighbors = \
            BoardHelper.filter_empty_places_with_opponent_neighbors_for_duplicates(
                BoardHelper.check_empty_spots_for_opponent_neighbors(
                    board, BoardHelper.look_up_all_empty_spots(board), opponent
                )
            )

        empty_places_with_directions = BoardHelper.replace_neighbors_with_their_direction(filtered_empty_places_with_opponent_neighbors)

        for couple in empty_places_with_directions:
            for direction in couple[1]:
                x_of_own, y_of_own = BoardHelper.look_for_own_stones_with_empty_and_direction(board, couple[0], direction, current_player)
                if x_of_own != -1:
                    mogelijk_begin_en_eind.append(((couple[0]), (x_of_own, y_of_own), (direction)))

        return mogelijk_begin_en_eind

    @staticmethod
    def filter_empty_places_with_opponent_neighbors_for_duplicates(empty_places_with_opponent_neighbors):
        filtered_list = []
        for combination in empty_places_with_opponent_neighbors:
            try:
                if filtered_list.index(combination):
                    pass
            except ValueError:
                filtered_list.append(combination)

        return filtered_list

    @staticmethod
    def look_for_own_stones_with_empty_and_direction(board, empty_place, direction, current_player):
        new_x = empty_place[0] + direction[0]
        new_y = empty_place[1] + direction[1]

        while 0 <= new_x < len(board) and 0 <= new_y < len(board):
            if board[new_x][new_y] == current_player:
                return new_x, new_y
            else:
                new_x += direction[0]
                new_y += direction[1]

        return -1, -1

    @staticmethod
    def look_up_all_empty_spots(board):
        empty_places = []
        for row in range(len(board)):  #kan niet met for row in board omdat de lege gelijk is aan index 0
            for column in range(len(board.__getitem__(row))):
                if board[row][column] == Tile.EMPTY:
                    empty_places.append((row, column))
        return empty_places

    @staticmethod
    def check_empty_spots_for_opponent_neighbors(board, empty_places, opponent):
        spots_with_opponent_neighbors = []
        for spot in empty_places:
            neighbors = BoardHelper.get_all_neighbors(board, *spot)
            opponent_neighbors = []
            for neighbor in neighbors:
                if board[neighbor[0]][neighbor[1]] == opponent:
                    opponent_neighbors.append((neighbor[0], neighbor[1]))
                    spots_with_opponent_neighbors.append((spot, opponent_neighbors))
        return spots_with_opponent_neighbors

    @staticmethod
    def replace_neighbors_with_their_direction(filtered_empty_places_with_opponent_neighbors):
        list_with_stones_and_directions = []
        for combination in filtered_empty_places_with_opponent_neighbors:
            directions = []
            for neighbor in combination[1]:
                x_direction = int(neighbor[0] - combination[0][0])  #combi example: ((6, 4), [(5, 4), (6, 5)]); combi[0] = (6,4) combi[1] = [(5, 4),(6, 5)]
                y_direction = int(neighbor[1] - combination[0][1])  #neighbor = (5, 4) & (6,5)
                directions.append((x_direction, y_direction))

            list_with_stones_and_directions.append((combination[0], directions))
        return list_with_stones_and_directions

    @staticmethod
    def get_all_neighbors(board, x, y):
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

"""
kijk bij alle lege vakken
kijk voor elke vak of het mogelijk is om er iets te leggen
in welke richting kom je stenen van de tegenstander tegen
"""
