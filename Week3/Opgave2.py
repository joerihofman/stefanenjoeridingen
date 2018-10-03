from itertools import permutations


index = (0, 1, 2, 3, 4, 5, 6, 7)

borders = [(0, 3, 5, 7), (1, 2, 3), (4, 5, 6)]

#
# def next_to(borders, x):
#     for i in borders:

def same_border(x, y):
    is_true = False
    for i in borders:
        print(i)
        print(is_true)
        if x in i and y in i:
            is_true = True
    return is_true


def neighbor(x, y):
    is_true = False
    for i in borders:
        if x in i and y in i:
            index1 = i.index(x)
            index2 = i.index(y)
            if abs(index1 - index2) == 1:
                return True




# neigbor(2, 1)



#
# for a1, a2, k1, k2, q1, q2, j1, j2 in permutations(index):
#     if neighbor(a1, k1):
#         if neighbor(a2, k2):
#             if neighbor(k1, q1):
#                 if neighbor(k2, q2):
#                     if neighbor(q1, j1):
#
#                     if not neighbor(a1, a2):
#                         if not neighbor(q1, q2):
#                             if not neighbor(k1, k2):
#                                 if not neighbor(j1, j2):
#                                     print([a1, a2, k1, k2, q1, q2, j1, j2])
#
#
# for a1, a2, k1, k2, q1, q2, j1, j2 in permutations(index):

# orderings = list(permutations(index))

for (a1, a2, k1, k2, q1, q2, j1, j2) in permutations(index):
    if not neighbor(a1, a2):
        if not neighbor(k1, k2):
            if not neighbor(q1, q2):
                if not neighbor(j1, j2):
                    print([a1, a2, k1, k2, q1, q2, j1, j2])





