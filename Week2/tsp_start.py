import matplotlib.pyplot as plt
import random
import time
import itertools
import math
from collections import namedtuple
import sys

sys.setrecursionlimit(100000)

# Based on Peter Norvig's IPython Notebook on the TSP

City = namedtuple('City', 'x y')
# c1 = City(4,0)
# c2 = City(0,3)


def distance(A, B):
    return math.hypot(A.x - B.x, A.y - B.y)


def try_all_tours(cities):
    "Generate and test all possible tours of the cities and choose the shortest tour."
    tours = alltours(cities)
    return min(tours, key=tour_length)


def alltours(cities):
    # Return a list of tours (a list of lists), each tour a permutation of cities, but
    # each one starting with the same city.
    start = next(iter(cities))  # cities is a set, sets don't support indexing
    return [[start] + list(rest)

            for rest in itertools.permutations(cities - {start})]


def tour_length(tour):
    # The total of distances between each pair of consecutive cities in the tour.
    return sum(distance(tour[i], tour[i-1]) 
               for i in range(len(tour)))


def make_cities(n, width=1000, height=1000):
    # Make a set of n cities, each with random coordinates within a rectangle (width x height).

    random.seed(66)  # the current system time is used as a seed
    # note: if we use the same seed, we get the same set of cities

    return frozenset(City(random.randrange(width), random.randrange(height))
                     for c in range(n))



def neirest_neighbors(cities, path=None, start=None):
    if path is None and start is None:
        start = next(iter(cities))
        path = [start]
    if len(cities) == len(path):
        return path
    else:
        min_value = None
        for i in cities:
            if i not in path:
                if not min_value:
                    min_value = i
                elif distance(start, i) < distance(start, min_value):
                    min_value = i
        path.append(min_value)
        start = min_value
        return neirest_neighbors(cities, path[:], start)


# def lineIntersection(pointA, pointB, pointC, pointD):
#
#     print(pointA)
#     print(pointB)
#     print(pointC)
#     print(pointD)
#
#     a1 = pointB.y - pointA.y
#     b1 = pointA.x - pointB.x
#     c1 = a1*(pointA.x) + b1*(pointA.y)
#
#     a2 = pointD.y - pointC.y
#     b2 = pointC.x - pointD.x
#     c2 = a2*(pointC.x) + b2*(pointD.y)
#
#     determinant = (a1*b2) - (a2*b1)
#     print(determinant)
#
#     if determinant < 0:
#         print('reeeeeeeeeeeeeeeeeeeeeeee')
#     else:
#
#         print('er is een intersectie')



tour = neirest_neighbors(make_cities(100))




# lineIntersection(tour[0], tour[1], tour[8], tour[9])

#
# def line(a, b):
#     A = (a.y - b.y)
#     B = (b.x - a.x)
#     C = ((a.x*b.y) - (b.x * a.y))
#     return A, B, -C

#
# def intersection(L1, L2):
#     D  = L1[0] * L2[1] - L1[1] * L2[0]
#     Dx = L1[2] * L2[1] - L1[1] * L2[2]
#     Dy = L1[0] * L2[2] - L1[2] * L2[0]
#     if D != 0:
#         x = Dx / D
#         y = Dy / D
#
#
#         return x,y
#     else:
#         return False

def intersection(pA, pB, pC, pD):

    variables = [pA, pB, pC, pD]
    if len(set(variables)) == len(variables):


        def line(a, b):
            A = (a.y - b.y)
            B = (b.x - a.x)
            C = ((a.x*b.y) - (b.x * a.y))
            return A, B, -C

        line1 = line(pA, pB)
        line2 = line(pC, pD)

        D  = line1[0] * line2[1] - line1[1] * line2[0]
        Dx = line1[2] * line2[1] - line1[1] * line2[2]
        Dy = line1[0] * line2[2] - line1[2] * line2[0]
        if D != 0:
            x = Dx / D
            y = Dy / D
            # if pA.x <= x <= pB.x or pB.x <= x <= pA.x and pC.y <= y <= pD.y or pD.y <= y <= pC.y \
            #         and pA.y <= y <= pB.y or pB.y <= x <= pA.y and pC.x <= x <= pD.x or pD.x <= x <= pC.x:
            # print(pA)
            # print(pB)
            # print(pC)
            # print(pD)
            #
            # print(x, y)
            # print(pA.x <= x <= pB.x)
            # print(pC.x >= x >= pD.x)
            # print(pA.y <= y <= pB.y)
            # print(pC.y <= y <= pD.y)
            #
            # print(line1)
            # print(line2)
            if min(pA.x, pB.x) <= x <= max(pB.x, pA.x) and min(pC.x, pD.x) <= x <= max(pD.x, pC.x) and min(pA.y, pB.y) <= y <= max(pB.y, pA.y) and min(pC.y, pD.y) <= y <= max(pD.y, pC.y):



                # print('er is een crossing hooooor')
                return True
        else:
            # print('lijnen lopen paralel')
            return False
    else:
        # print('waarden met de zelfde punten gevonden')
        return False




# for i in range(len(tour)):1
#     print('line1', tour[i], tour[i-1])
#     for j in range(len(tour)):
#         if tour[i]



def rc(tour):
    changes = False
    nr = 0
    for i in range(len(tour)):
        for j in range(len(tour)):
            # print(j)
            if intersection(tour[i], tour[i-1], tour[j], tour[j-1]):
                # temptour = tour[i-1]
                nr += 1
            # temptour2 = tour[i-1]
            #     tour[i-1] = tour[j-1]
            #     tour[j-1] = temptour
            #     changes = True
    if changes == True:
        return rc(tour)
    else:
        print(nr)
        return tour








def plot_tour(tour): 
    # Plot the cities as circles and the tour as lines between them.
    points = list(tour) + [tour[0]]
    plt.plot([p.x for p in points], [p.y for p in points], 'bo-')
    plt.axis('scaled') # equal increments of x and y have the same length
    plt.axis('off')
    plt.show()


def plot_tsp(algorithm, cities):
    # Apply a TSP algorithm to cities, print the time it took, and plot the resulting tour.
    t0 = time.clock()
    tour = algorithm(cities)
    t1 = time.clock()
    print("{} city tour with length {:.1f} in {:.3f} secs for {}"
          .format(len(tour), tour_length(tour), t1 - t0, algorithm.__name__))
    print("Start plotting ...")
    plot_tour(tour)


plot_tour(tour)

rc(tour)





# plot_tour(tour)



# plot_tsp(neirest_neighbors, make_cities(100))

# plot_tsp(neirest_neighbors, make_cities(10))
'''
a)
seed = 66

try_all_tours:
10 city tour with length 2683.0 in 4.782 secs for try_all_tours

neirest_neighbors:
10 city tour with length 3166.9 in 0.000 secs for neirest_neighbors

=(2683−3166.9/(2683+3166.9/2))×100
=(−483.9/5849.9/2)×100
=(483.9/2924.95)×100
=0.165439×100
=16.5439%difference
'''

'''
b)
100 city tour with length 10147.1 in 0.028 secs for neirest_neighbors
'''


# plot_tsp(neirest_neighbors, make_cities(100))

# b)    100 city tour length 10219.2  in 0.019 seconden



# plot_tsp(try_all_tours, make_cities(10))

