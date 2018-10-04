from itertools import permutations
import collections


index = (0, 1, 2, 3, 4, 5, 6, 7)

borders = [(0, 3, 5, 7), (1, 2, 3), (4, 5, 6)]


nodes_dict = {0: [3], 1: [2], 3: [0, 2, 5], 4: [2, 5], 5: [3, 4, 7, 6], 6: [5], 7:[5]}

board1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}



#
# def next_to(borders, x):
#     for i in borders:

def same_neighbor(board, nodes_dict, index, card):
    for key in nodes_dict[index]:
        print(key)
        print('value of key', board[key])
        if board[key] == card:
            print('true')
            return True
    print('same_neighbor = false')
    return False



def safe(board, index, card):
    list_of_values = list(board.values())
    if list_of_values.count(card) > 2:
        return False

    if same_neighbor(board, nodes_dict, index, card):
        return False

    if card == 1 and list_of_values.count(2) > 1:
        print(same_neighbor(board, nodes_dict, index, 2))
        if not same_neighbor(board, nodes_dict, index, 2):
            return False

    if card == 2 and list_of_values.count(3) > 1:
        if not same_neighbor(board, nodes_dict, index, 3):
            return False

    if card == 3 and list_of_values.count(3) == 1:
        if not same_neighbor(board, nodes_dict, index, 4):
            return False

    if card == 1 and list_of_values.count(3) > 1:
        if same_neighbor(board, nodes_dict, index, 3):
            return False

    return True


def dfs(board, index):
    if index >= 7:
        print(board)
        print('jajaj')
        return True

    for next in range(len(board)):
        for card in [1, 2, 3, 4]:
            print('card', card)

            if safe(board, index, card):
                board[index] = card
                if dfs(board, index+1):
                    return True

                board[index] = 0

    return False




        # print('true')

dfs(board1, 0)



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

counter = 0


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






