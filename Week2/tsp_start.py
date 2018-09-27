from collections import namedtuple

import matplotlib.pyplot as plt
import random
import time
import itertools
import math


City = namedtuple('City', 'x y')


def distance(point_a, point_b):
    return math.hypot(point_a.x - point_b.x, point_a.y - point_b.y)


def try_all_tours(cities):
    "Generate and test all possible tours of the cities and choose the shortest tour."
    tours = all_tours(cities)
    return min(tours, key=tour_length)


def all_tours(cities):
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

    random.seed()  # the current system time is used as a seed
    # note: if we use the same seed, we get the same set of cities

    return frozenset(City(random.randrange(width), random.randrange(height))
                     for c in range(n))


def nearest_neighbors(cities, path=None, start=None):
    if path is None and start is None:
        start = next(iter(cities))
        path = [start]
    if len(cities) == len(path):
        return path
    else:
        min_value = None
        for i in cities:
            if i not in path:
                if not min_value or distance(start, i) < distance(start, min_value):
                    min_value = i
        path.append(min_value)
        start = min_value
        return nearest_neighbors(cities, path[:], start)


def intersection(city_1, city_2, city_3, city_4):
    variables = [city_1, city_2, city_3, city_4]
    if len(set(variables)) == len(variables):

        def line(a, b):
            A = (a.y - b.y)
            B = (b.x - a.x)
            C = ((a.x*b.y) - (b.x * a.y))
            return A, B, -C

        line1 = line(city_1, city_2)
        line2 = line(city_3, city_4)

        D = line1[0] * line2[1] - line1[1] * line2[0]
        Dx = line1[2] * line2[1] - line1[1] * line2[2]
        Dy = line1[0] * line2[2] - line1[2] * line2[0]
        if D != 0:
            x = Dx / D
            y = Dy / D

            if min(city_1.x, city_2.x) <= x <= max(city_2.x, city_1.x) and min(city_3.x, city_4.x) <= x <= max(city_4.x, city_3.x) and \
                                    min(city_1.y, city_2.y) <= y <= max(city_2.y, city_1.y) and min(city_3.y, city_4.y) <= y <= max(city_4.y, city_3.y):
                return True

        else:
            return False

    else:
        return False


def two_opt_alg(tour, i, k):
    tour[i:k] = reversed(tour[i:k])
    return tour


def remove_crossings(tour):
    changes = False
    for i in range(len(tour)):
        for j in range(len(tour)):
            # print(j)
            if intersection(tour[i], tour[i-1], tour[j], tour[j-1]):
                tour = two_opt_alg(tour, i, j)
                changes = True
    if changes:
        return remove_crossings(tour)
    else:
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

    tour = remove_crossings(tour)

    print("{} city tour with length {:.1f}"
          .format(len(tour), tour_length(tour)))

    print("Start plotting ...")
    plot_tour(tour)


plot_tsp(nearest_neighbors, make_cities(100))


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
