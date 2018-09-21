import tkinter as tk
from tkinter import ttk

import heapq
import sched
import time
import threading
import random

# assuming a resulution of 1920 x 1080 = 16 : 9

# global color scheme
bgc = '#FDF6E3'
gridc = '#542437'
blockc = 'red'
pathc = 'blue'
startc = '#C7F464'
goalc = 'yellow'

# global vars
PAUSE_STATUS = True
PROB = 0.3  # probability blocking node
SIZE = 25  # the nr of nodes=grid crossings in a row (or column)

s = sched.scheduler(time.time, time.sleep)


# global var: pixel sizes
CELL = 35  # size of cell/square in pixels
W = (SIZE-1) * CELL  # width of grid in pixels
H = W  # height of grid
TR = 10  # translate/move the grid, upper left is 10,10

grid = [[0 for x in range(SIZE)] for y in range(SIZE)]
start = (0, 0)
goal = (SIZE-1, SIZE-1)


class PriorityQueue:
    # to be use in the A* algorithm
    # a wrapper around heapq (aka priority queue), a binary min-heap on top of a list
    # in a min-heap, the keys of parent nodes are less than or equal to those
    # of the children and the lowest key is in the root node
    def __init__(self):
        # create a min heap (as a list)
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    # heap elements are tuples (priority, item)
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    # pop returns the smallest item from the heap
    # i.e. the root element = element (priority, item) with highest priority
    def get(self):
        return heapq.heappop(self.elements)[1]


def get_neighbors(board, position):
    neighbors = []
    length = len(board) - 1
    print(position)

    (row, col) = position

    positions = [(row-1, col), (row, col-1), (row, col+1), (row+1, col)]
    for pos in positions:
        if 0 <= pos[0] <= length and 0 <= pos[1] <= length:
            if board[pos[0]][pos[1]] != 'b':
                neighbors.append((pos[0], pos[1]))
    return neighbors


def bernoulli_trial():
    return 1 if random.random() < PROB else 0


def set_grid_value(node, value):
    # node is a tuple (x, y), grid is a 2D list [x][y]
    grid[node[0]][node[1]] = value


def make_grid(c):
    # vertical lines
    for i in range(0, W+1, CELL):
        c.create_line(i+TR, 0+TR, i+TR, H+TR, fill=gridc)

    # horizontal lines
    for i in range(0, H+1, CELL):
        c.create_line(0+TR, i+TR, W+TR, i+TR, fill=gridc)


def init_grid(c):
    for x in range(SIZE):
        for y in range(SIZE):
            node = (x, y)
            # start and goal cannot be bloking nodes
            if bernoulli_trial() and node != start and node != goal:
                set_grid_value(node, 'b')  # blocked
                plot_node(c, node, color=blockc)
            else:
                set_grid_value(node, -1)  # init costs, -1 means infinite


def plot_line_segment(c, x0, y0, x1, y1):
    c.create_line(x0*CELL+TR, y0*CELL+TR, x1*CELL+TR, y1*CELL+TR, fill=pathc, width=2)


def plot_node(c, node, color):
    # size of (red) rectangle is 8 by 8
    x0 = node[0] * CELL - 4
    y0 = node[1] * CELL - 4
    x1 = x0 + 8 + 1
    y1 = y0 + 8 + 1
    c.create_rectangle(x0+TR, y0+TR, x1+TR, y1+TR, fill=color)


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


print(heuristic((0, 0), (24, 24)))


def dijkstra_search(start, goal):
    queue = PriorityQueue()
    queue.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not queue.empty():
        current = queue.get()

        if current == goal:
            break

        for next in get_neighbors(grid, current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                queue.put(next, priority)
                time.sleep(0.05)
                plot_line_segment(canvas, current[0], current[1], next[0], next[1])
                canvas.update()
                came_from[next] = current

    return came_from, cost_so_far


def a_star_search(start_for_search, goal_for_search):
    queue = PriorityQueue()
    queue.put(start_for_search, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start_for_search] = None
    cost_so_far[start_for_search] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal_for_search:
            break
        print(current)
        for next in get_neighbors(grid, current):
            new_cost = cost_so_far[current] + 1

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal_for_search, next)
                queue.put(next, priority)

                time.sleep(0.05)
                plot_line_segment(canvas, current[0], current[1], next[0], next[1])
                canvas.update()
                came_from[next] = current

    return came_from, cost_so_far


start, goal = (0,0), (24,24)

int_i = 0


def control_panel():
    mf = ttk.LabelFrame(right_frame)
    mf.grid(column=0, row=0, padx=8, pady=4)
    mf.grid_rowconfigure(2, minsize=10)

    def start():
        global PAUSE_STATUS
        global int_i
        PAUSE_STATUS = False

        if bt_alg.get() == 'UC':
            dijkstra_search((0, 0), (24, 24))
        if bt_alg.get() == 'A*':
            a_star_search((0, 0), (24, 24))

        pause_button.configure(background='SystemButtonFace')
        start_button.configure(background='green')

    def pause():
        global PAUSE_STATUS
        PAUSE_STATUS = True

        pause_button.configure(background='red')
        start_button.configure(background='SystemButtonFace')

    start_button = tk.Button(mf, text="Start", command=start, width=10)
    start_button.grid(row=1, column=1, sticky='w', padx=5, pady=5)

    pause_button = tk.Button(mf, text="Pause", command=pause, width=10)
    pause_button.grid(row=2, column=1, sticky='w', padx=5, pady=5)

    def sel():
        print('algorithm =', bt_alg.get())

    r1_button = tk.Radiobutton(mf, text='UC', value='UC', variable=bt_alg, command=sel)
    r2_button = tk.Radiobutton(mf, text='A*', value='A*', variable=bt_alg, command=sel)
    bt_alg.set('UC')

    r1_button.grid(row=3, column=1, columnspan=2, sticky='w')
    r2_button.grid(row=4, column=1, columnspan=2, sticky='w')

    def box_update1():
        print('speed is set to:', box1.get())

    def box_update2():
        print('prob. blocking is set to:', box2.get())

    lf = ttk.LabelFrame(right_frame, relief="sunken")
    lf.grid(column=0, row=1, padx=5, pady=5)

    ttk.Label(lf, text="Speed ").grid(row=1, column=1, sticky='w')
    box1 = ttk.Combobox(lf, textvariable=speed, state='readonly', width=6)
    box1.grid(row=2, column=1, sticky='w')
    box1['values'] = tuple(str(i) for i in range(10))
    box1.current(5)
    box1.bind("<<ComboboxSelected>>", box_update1)

    ttk.Label(lf, text="Prob. blocking").grid(row=3, column=1, sticky='w')
    box2 = ttk.Combobox(lf, textvariable=prob, state='readonly', width=6)
    box2.grid(row=4, column=1, sticky='ew')
    box2['values'] = tuple(str(i) for i in range(10))
    box2.current(3)
    box2.bind("<<ComboboxSelected>>", box_update2)

    def draw_line_on_grid(canvas, i):
        if PAUSE_STATUS is False:
            plot_line_segment(canvas, i, i, i, i+1)
            plot_line_segment(canvas, i, i+1, i+1, i+1)

            threading.Timer(int(box1.get()), draw_line_on_grid, [canvas, i+1]).start()

    def print_something_for_testing():
        if PAUSE_STATUS is False:
            threading.Timer(int(box1.get()), print_something_for_testing).start()


root = tk.Tk()
root.title('A* demo')

speed = tk.StringVar()
prob = tk.StringVar()
bt_alg = tk.StringVar()
left_frame = ttk.Frame(root, padding="3 3 12 12")
left_frame.grid(column=0, row=0)

right_frame = ttk.Frame(root, padding="3 3 12 12")
right_frame.grid(column=1, row=0)

canvas = tk.Canvas(left_frame, height=H+4*TR, width=W+4*TR, borderwidth=-TR, bg = bgc)
canvas.pack(fill=tk.BOTH, expand=True)

make_grid(canvas)
init_grid(canvas)

# show start and goal nodes
plot_node(canvas, start, color=startc)
plot_node(canvas, goal, color=goalc)

column_for_printing_in_cli = []
row_for_printing_in_cli = []

for row in grid:
    row_for_printing_in_cli = []
    for o in row:
        if o == -1:
            row_for_printing_in_cli.append(' ')
        elif o == 'b':
            row_for_printing_in_cli.append('B')
    column_for_printing_in_cli.append(row_for_printing_in_cli)

for row in column_for_printing_in_cli:
    print(row)

control_panel()

root.mainloop()

