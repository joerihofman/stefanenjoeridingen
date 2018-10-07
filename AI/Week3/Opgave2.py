from itertools import permutations
import collections

counter = 0

index = (0, 1, 2, 3, 4, 5, 6, 7)

borders = [(0, 3, 5, 7), (1, 2, 3), (4, 5, 6), (2, 4)]

graph = {0: [3], 1: [2], 2:[1, 3, 4], 3: [0, 2, 5], 4: [2, 5], 5: [3, 4, 7, 6], 6: [5], 7: [5]}

board1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}


def print_board(board):
    print(' ', ' ', board[0])
    print(board[1], board[2], board[3])
    print(' ', board[4], board[5], board[6])
    print(' ',' ', board[7])


def same_neighbor(board, index, graph):

    for neighbor in graph[index]:
        if board[index] == board[neighbor]:
            return True

    return False


def neigbor_cards(board, index, graph, card1, card2):
    card1_list = []
    for index in range(index):
        if board[index] == card1:
            card1_list.append(index)

    if len(card1_list) > 0:
        for index_ace in card1_list:
            temp_list_neighbors = []
            for neighbor in graph[index_ace]:
                temp_list_neighbors.append(board[neighbor])

            if 0 not in temp_list_neighbors:
                if card2 not in temp_list_neighbors:
                    return False

        return True
    else:
        return True


def safe(board, index, card, graph):
    list_of_values = list(board.values())

    if list_of_values.count(card) > 2:
        return False

    if same_neighbor(board, index, graph):
        return False

    if not neigbor_cards(board, index, graph, 'A', 'K'):
        return False

    if not neigbor_cards(board, index, graph, 'K', 'Q'):
        return False

    if not neigbor_cards(board, index, graph, 'Q', 'J'):
        return False

    if not neigbor_cards(board, index, graph, 'A', 'Q'):
        return False

    return True


def dfs_backtracking(board, graph, number):
    # print_board(board)
    global counter
    counter = counter + 1
    if number >= 8:
        # print(board)
        print('uitslag', counter)
        print_board(board)
        return True
    for cel in range(len(board)):
        if board[cel] == 0:
            for card in ['A', 'K', 'Q', 'J']:
                board[cel] = card
                if safe(board, cel, card, graph):
                    if dfs_backtracking(board, graph, number+1):
                        return True
                board[cel] = 0
    return False


dfs_backtracking(board1, graph, 0)


def same_border(x, y):
    is_true = False
    for i in borders:
        print(i)
        print(is_true)
        if x in i and y in i:
            is_true = True
    return is_true


def neighbor(x, y):
    for i in borders:
        if x in i and y in i:
            index1 = i.index(x)
            index2 = i.index(y)
            if abs(index1 - index2) == 1:
                return True



# versie 1
# for a1, a2, k1, k2, q1, q2, j1, j2 in permutations(index):
#     if neighbor(a1, k1) or neighbor(a1, k2):
#         if neighbor(a2, k1) or neighbor(a2, k2):
#             if neighbor(k1, q1) or neighbor(k1, q2):
#                 if neighbor(k2, q1) or neighbor(k2, q2):
#                     if neighbor(q1, j1) or neighbor(q1, j2) or neighbor(q2, j1) or neighbor(q2, j2):
#                         if not neighbor(a1, q1) and not neighbor(a1, q2) and not neighbor(a2, q1) and not neighbor(a2, q2):
#                             if not neighbor(a1, a2):
#                                 if not neighbor(k1, k2):
#                                     if not neighbor(q1, q2):
#                                         if not neighbor(j1, j2):
#                                             counter = counter + 1
#                                             answers = ({a1: 'ace', a2: 'ace', k1: 'king', k2: 'king', q1: 'qeen', q2: 'queen', j1: 'jack', j2: 'jack'})
#                                             print(collections.OrderedDict(sorted(answers.items())))
# print('aantal mogelijkheden', counter)

# versie 2
def opdrachtA():
    #40230
    answers_list = []
    for a1, a2, k1, k2, q1, q2, j1, j2 in permutations(index):
        if neighbor(a1, k1) or neighbor(a1, k2):
            if neighbor(a2, k1) or neighbor(a2, k1):
                if neighbor(k1, q1) or neighbor(k1, q2):
                    if neighbor(k2, q1) or neighbor(k2, q2):
                        if neighbor(q1, j1) or neighbor(q1, j2):
                            if neighbor(q2, j1) or neighbor(q2, j2):
                                if not neighbor(a1, q1) and not neighbor(a1, q2):
                                    if not neighbor(a2, q1) and not neighbor(a2, q2):
                                        if not neighbor(a1, a2):
                                            if not neighbor(k1, k2):
                                                if not neighbor(q1, q2):
                                                    if not neighbor(j1, j2):
                                                        counter = counter + 1
                                                        answers = ({a1: 'ace', a2: 'ace', k1: 'king', k2: 'king', q1: 'queen', q2: 'queen', j1: 'jack', j2: 'jack'})
                                                        sorted_dict = (collections.OrderedDict(sorted(answers.items())))
                                                        if sorted_dict not in answers_list:
                                                            answers_list.append(sorted_dict)
    print('aantal mogelijkheden', counter)
    for i in answers_list:
        print(i)








