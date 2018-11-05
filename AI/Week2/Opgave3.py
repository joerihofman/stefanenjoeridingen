import copy
import random
from enum import Enum
import time


class Tile(Enum):
    BLACK = 'B'
    WHITE = 'W'
    EMPTY = '.'


board_size = 8

board = [[Tile.EMPTY for x in range(board_size)] for y in range(board_size)]

board[3][3] = Tile.WHITE
board[4][4] = Tile.WHITE
board[3][4] = Tile.BLACK
board[4][3] = Tile.BLACK

current_player = Tile.BLACK
opponent = Tile.WHITE

minimum_heuristic_val = -1
maximum_heuristic_val = board_size * board_size + 4 * board_size + 4 + 1


def other_player_turn():
    global current_player
    global opponent
    if current_player == Tile.BLACK:
        current_player = Tile.WHITE
        opponent = Tile.BLACK
    else:
        current_player = Tile.BLACK
        opponent = Tile.WHITE


def print_board(printable_board):
    print('')
    for row in printable_board:
        print(' '.join([colour.value for colour in row]))
    print('')


def print_amount_of_each_colour():
    global board
    whites = 0
    blacks = 0
    for row in board:
        for column in row:
            if column == Tile.BLACK:
                blacks += 1
            elif column == Tile.WHITE:
                whites += 1
    print("Black: " + blacks.__str__() + " - White: " + whites.__str__())


def flip_stones(board, current_player, begin, end, direction, change):
    new_board = board
    x = begin[0]
    y = begin[1]
    if direction[0] == 0:
        while y != end[1]:
            new_board[x][y] = current_player
            y += direction[1]
    elif direction[1] == 0:
        while x != end[0]:
            new_board[x][y] = current_player
            x += direction[0]
    else:
        while x != end[0] and y != end[1]:
            new_board[x][y] = current_player
            x += direction[0]
            y += direction[1]
    if change:
        if current_player == Tile.BLACK:
            new_player = Tile.WHITE
        else:
            new_player = Tile.BLACK
        return new_board, new_player
    return new_board


def end_state_reached():
    global board
    for row in board:
        for column in row:
            if column == Tile.EMPTY:
                return False
    return True


def look_up_all_empty_spots():
    global board
    empty_places = []
    for row in range(len(board)):  #kan niet met for row in board omdat de lege gelijk is aan index 0
        for column in range(len(board.__getitem__(row))):
            if board[row][column] == Tile.EMPTY:
                empty_places.append((row, column))
    return empty_places


def get_all_neighbors(board, x, y):
    neighbors = []
    length = len(board) - 1

    positions = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]
    for pos in positions:
        if 0 <= pos[0] <= length and 0 <= pos[1] <= length:
            neighbors.append((pos[0], pos[1]))
    return neighbors


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


def possible_moves():
    mogelijke_begin_en_eind = []
    spots_with_opponent_neighbors = []
    empty_places = look_up_all_empty_spots()
    filtered_list = []

    for spot in empty_places:
        # Spot = (x, y)
        neighbors = get_all_neighbors(board, *spot)
        opponent_neighbors = []
        for neighbor in neighbors:
            if board[neighbor[0]][neighbor[1]] == opponent:
                opponent_neighbors.append((neighbor[0], neighbor[1]))
                spots_with_opponent_neighbors.append((spot, opponent_neighbors))

    for combination in spots_with_opponent_neighbors:
        # combination = ((x_begin, y_begin), [(x_eind, y_eind)])
        try:
            if filtered_list.index(combination):
                pass
        except ValueError:
            filtered_list.append(combination)

    empty_places_with_directions = replace_neighbors_with_their_direction(filtered_list)

    for couple in empty_places_with_directions:
        # combination = ((x_begin, y_begin), [(x_eind, y_eind)])
        for direction in couple[1]:
            x_of_own, y_of_own = look_for_own_stones_with_empty_and_direction(board, couple[0], direction, current_player)
            if x_of_own != -1:
                mogelijke_begin_en_eind.append(((couple[0]), (x_of_own, y_of_own), (direction)))

    return mogelijke_begin_en_eind


def random_move():
    global board

    list_of_possible_moves = possible_moves()
    if len(list_of_possible_moves) != 0:
        random_index_for_list = random.randint(0, len(list_of_possible_moves) - 1)
        item_start = list_of_possible_moves[random_index_for_list][0]
        for combination in list_of_possible_moves:
            # combination = ((x_begin, y_begin), (x_eind, y_eind), (x_richting, y_richting))
            if combination[0] == item_start:
                flip_stones(board, current_player, combination[0], combination[1], combination[2], False)
                other_player_turn()
    else:
        other_player_turn()


def heuristic_value():
    global board
    global current_player

    value = 0
    board_len = len(board)
    board_range = range(board_len)
    for x in board_range:
        for y in board_range:
            if board[x][y] == current_player:
                if (x == 0 or x == board_len - 1) and (y == 0 or y == board_len - 1):
                    value += 4  # hoek
                elif (x == 0 or x == board_len - 1) or (y == 0 or y == board_len - 1):
                    value += 2  # zijkant
                else:
                    value += 1
    return value


def negamax_controller(board):
    global current_player
    max_points = 0
    move_to_make = []
    valid_moves = possible_moves()
    timer = time.time()
    for move in valid_moves:
        if time.time() - timer < 20:
            # move = ((x_begin, y_begin), (x_eind, y_eind), (x_richting, y_richting))
            tempboard, temp_player = flip_stones(copy.deepcopy(board), copy.deepcopy(current_player), move[0], move[1], move[2], True)
            points = negamax(tempboard, temp_player, depth=4, colour=1)
            if points > max_points:
                max_points = points
                move_to_make = [move[0], move[1], move[2]]
    if len(move_to_make) != 0:
        flip_stones(board, current_player, move_to_make[0], move_to_make[1], move_to_make[2], False)
        other_player_turn()
    else:
        other_player_turn()


def negamax(board, current_player, depth, colour):
    if depth == 0:
        return colour * heuristic_value()
    value = -1
    valid_moves = possible_moves()
    for move in valid_moves:
        # move = ((x_begin, y_begin), (x_eind, y_eind), (x_richting, y_richting))
        tempboard, temp_player = flip_stones(copy.deepcopy(board), copy.deepcopy(current_player), move[0], move[1], move[2], True)
        val = -negamax(tempboard, temp_player, depth-1, -colour)
        value = max(value, val)
    return value


def negamax_prune_controller(board):
    max_points = 0
    move_to_make = []
    valid_moves = possible_moves()
    timer = time.time()
    for move in valid_moves:
        if time.time() - timer < 20:
            # move = ((x_begin, y_begin), (x_eind, y_eind), (x_richting, y_richting))
            tempboard, temp_player = flip_stones(copy.deepcopy(board), copy.deepcopy(current_player), move[0], move[1], move[2], True)
            points = negamax_prune(tempboard, temp_player, depth=4, colour=1, alpha=minimum_heuristic_val, beta=maximum_heuristic_val)
            if points > max_points:
                max_points = points
                move_to_make = [move[0], move[1], move[2]]
    if len(move_to_make) != 0:
        flip_stones(board, current_player, move_to_make[0], move_to_make[1], move_to_make[2], False)
        other_player_turn()
    else:
        other_player_turn()


def negamax_prune(board, temp_player, depth, colour, alpha, beta):
    if depth == 0:
        return colour * heuristic_value()
    value = -1
    valid_moves = possible_moves()
    for move in valid_moves:
        # move = ((x_begin, y_begin), (x_eind, y_eind), (x_richting, y_richting))
        tempboard, temp_player = flip_stones(copy.deepcopy(board), temp_player, move[0], move[1], move[2], True)
        val = -negamax_prune(tempboard, temp_player, depth-1, -colour, -beta, -alpha)
        value = max(value, val)
        alpha = max(alpha, val)
        if alpha >= beta:
            break
    return value


def user_playing():
    valid_moves = possible_moves()
    print("Possibilities:")
    if len(valid_moves) != 0:
        for move in valid_moves:
            print(move[0])
        x = input("Which X do you choose? ")
        y = input("Which Y do you choose? ")
        user_coord = (int(x), int(y))
        for move in valid_moves:
            if move[0] == user_coord:
                flip_stones(board, current_player, move[0], move[1], move[2], False)
                other_player_turn()
                return
        print("please use valid x and y coordinates")
        user_playing()
    else:
        print("You can not play")
        other_player_turn()


while not end_state_reached():
    print_board(board)
    if current_player == Tile.BLACK:
        # negamax_controller(board)
        negamax_prune_controller(board)
    else:
        random_move()
        # print("YOU ARE WHITE")
        # user_playing()
    print_board(board)
    print_amount_of_each_colour()

print_board(board)
print_amount_of_each_colour()
