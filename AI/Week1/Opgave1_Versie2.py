from enum import Enum;


class MovingException(Exception):
    def __init__(self, message):
        self.message = message


class State(Enum):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"


class Movable:
    name = ''
    state = State

    def __init__(self, name, state):
        self.name = name
        self.state = state

    def move(self):
        if self.state == State.LEFT:
            self.state = State.RIGHT
        elif self.state == State.RIGHT:
            self.state == State.LEFT


class UsefulMethods:
    @staticmethod
    def make_state(farmer, cabbage, goat, wolf, river):
        left_side = []
        right_side = []
        whole_plane = []
        left_side.append(farmer) if farmer.state == State.LEFT else right_side.append(farmer)
        left_side.append(cabbage) if cabbage.state == State.LEFT else right_side.append(cabbage)
        left_side.append(goat) if goat.state == State.LEFT else right_side.append(goat)
        left_side.append(wolf) if wolf.state == State.LEFT else right_side.append(wolf)

        for movable in left_side:
            whole_plane.append(movable)

        whole_plane.append(river)

        for movable in right_side:
            whole_plane.append(movable)

        return whole_plane

    @staticmethod
    def check_if_goal_state_reached(current_state):
        for movable in current_state:
            if movable.state == State.RIGHT:
                return False
        return True

    @staticmethod
    def check_valid_state(current_state):
        left_side = []
        right_side = []
        for movable in current_state:
            if movable.state != State.CENTER:
                left_side.append(movable) if movable.state == State.LEFT else right_side.append(movable)
        if left_side.__contains__(Movable.name=='C') and left_side.__contains__(Movable.name=='G'):
            return False
        elif left_side.__contains__(Movable.name=='G') and left_side.__contains__(Movable.name=='W'):
            return False
        else:
            return True


    # def gets_eaten(o1, o2):
    #     if o1 == 'G' and o2.name == 'C':
    #         return True
    #     elif o1.name == 'W' and o2.name == 'G':
    #         return True
    #     else:
    #         return False

class Search:
    @staticmethod
    def possible_children(current_state):
        farmer_state = None
        every_item_farmer_side = []

        for movable in current_state:
            if movable.name == 'F':
                farmer_state = movable.state
                break

        for movable in current_state:
            if movable.state == farmer_state and movable.name != 'F':
                every_item_farmer_side.append(movable)

        # try:
        #     raise MovingException("oh mijn god",)
        # except MovingException:
        #     print("dat was het dan")
        #     raise
        # return None


class Move:
    @staticmethod
    def move_movables():
        None


class PrintToCLI:
    @staticmethod
    def print_all(list):
        state = ""

        for movable in list:
            state += movable.name

        print(state)


class Main:
    farmer = Movable('F', State.LEFT)
    cabbage = Movable('C', State.LEFT)
    goat = Movable('G', State.LEFT)
    wolf = Movable('W', State.LEFT)
    river = Movable('||', State.CENTER)

    current_state = UsefulMethods.make_state(farmer, cabbage, goat, wolf, river)

    # PrintToCLI.print_all(current_state)

    Search.possible_children(current_state)

    # Move.move_movables(current_state)

    # current_state = UsefulMethods.make_state(farmer, cabbage, goat, wolf, river)

    PrintToCLI.print_all(current_state)


    # UsefulMethods.gets_eaten(list_of_movables.__getitem__(0), list_of_movables.__getitem__(2))

    # UsefulMethods.check_goal_state(list_of_movables)

