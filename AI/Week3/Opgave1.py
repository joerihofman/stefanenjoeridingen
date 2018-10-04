from itertools import permutations


floors = (0, 1, 2, 3, 4)


def puzzle(floors):
    for (H, K, L, P, R) in list(permutations(floors)):
        if H != 4:
            if K != 0:
                if L != 4 and L != 0:
                    if P > K:
                        if R - L != 1 and R - L != -1:
                            if L - K != 1 and L - K != -1:
                                return {H: 'h', K: 'k', L: 'l', P: 'p', R : 'r'}


list = puzzle(floors)
print(list)


