import random
import sys


sys.setrecursionlimit(1000000)

possible_moves = ['roll', 'hold']
goal_score = 40
victories = [0, 0]
gamecounter = 0


class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
    	    self.memo[args] = self.fn(*args)
        return self.memo[args]

'''
    State is a namedtuple of (p, me, you, pending) where
    p: 'me' or 'you', indicating which player's turn it is
    me: my total score
    you: your total score
    pending: the number of pending points (accumulated on current turn)
'''


game_state = ["me", 0, 0, 0]
 # A strategy that ignores the state and chooses at random from possible moves.

def clueless(state):
    random_move = random.SystemRandom().choice(possible_moves)
    if random_move == "roll":
        if hold_at_x(state):
            print(state.__str__() + " has chosen hold all by itself")
            hold(state)
        else:
            print(state.__str__() + " has chosen roll")
            roll(state, roll_dice())
    elif random_move == "hold":
        print(state.__str__() + " has chosen hold")
        hold(state)


def just_play(state):
    check_victory(state)
    if state[0] == "me":
        if hold_at_x(state, 10):
            hold(state)
        else:
            roll(state, roll_dice())
    if state[0] == "you":
        if hold_at_x(state, 20):
            hold(state)
        else:
            roll(state, roll_dice())


'''
    Apply a die roll d to yield a new state:
    If d == 1, it's a pig-out, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn.
    If d > 1, add d to 'pending' points.
'''


def roll(state, d):
    if d == 1:
        if state[0] == "me":
            new_score = state[1] + d
            state[1] = new_score
            state[3] = 0
            state[0] = "you"
            return state
        elif state[0] == "you":
            new_score = state[2] + d
            state[2] = new_score
            state[3] = 0
            state[0] = "me"
            return state
    else:
        score = state[3] + d
        state[3] = score
        return state

'''
    Apply a hold to yield a new state: add the pending points to my total points and
    it becomes the other player's turn.
'''


# def decorator(d):
#     "Make function d a decorator: d wraps a function fn."
#
#     def _d(fn):
#         return update_wrapper(d(fn), fn)
#
#     update_wrapper(_d, d)
#     return _d
#
#
# @decorator
# def memo(f):
#     cache = {}
#
#     def _f(*args):
#         try:
#             return cache[args]
#         except KeyError:
#             cache[args] = result = f(*args)
#             return result
#         except TypeError:
#             return f(*args)
#
#     return _f

def hold(state):
    if state[0] == "me":
        new_score = state[3] + state[1]
        state[1] = new_score
        state[3] = 0
        state[0] = "you"
        return state
    elif state[0] == "you":
        new_score = state[3] + state[2]
        state[2] = new_score
        state[3] = 0
        state[0] = "me"
        return state


def hold_at_x(state, hold):
    if state[3] >= hold:
        return True


def legal_actions(state):
    # The legal actions from a state. If pending == 0 then we must roll
    if state[3] == 0:
        return ['roll']
    else:
        return ['roll', 'hold']


# # def p_win(me, you, pending):
# def p_win1(state):
#     me = state[1]
#     you = state[2]
#     pending = state[3]
#     return p_win1(me, you, pending)

def p_win(state):
    # print(me)
    # print(you)
    # print(pending)
    _, me, you, pending = state


    # def _Pwin(me, you, pending):
    # print(goal_score)
    # print(me)
    # print(you)
    # print(pending)
    if me + pending >= goal_score:
        return 1
    if you >= goal_score:
        return 0
    else:
        return max(ev_action(state, action, p_win) for action in legal_actions(state))

    #     Proll = (1 - _Pwin(you, me + 1, 0) +
    #                  sum(_Pwin(me, you, pending + i) for i in (2, 3, 4, 5, 6))) / 6.0
    #     return Proll if pending != 0 else max(1 - _Pwin(you, me + pending, 0), Proll)
    #
    # return _Pwin(me, you, pending)

def p_win(state):
    '''The utility of a state; here just the probability that an optimal
    player whose turn it is to make can win from the current state.'''
    _, me, you, pending = state

    @Memoize
    def _Pwin(me, you, pending):
        if me + pending >= goal_score:
            return 1
        if you >= goal_score:
            return 0

        total = 1 - _Pwin(you, me + 1, 0)
        for i in (2, 3, 4, 5, 6):
            total = total + _Pwin(me, you, pending + i)
        total = float(total/6)


        # Proll = (1 - _Pwin(you, me + 1, 0) +
        #          sum(_Pwin(me, you, pending + i) for i in (2, 3, 4, 5, 6))) / 6.
        return total if not pending else max(1 - _Pwin(you, me + pending, 0),
                                             total)
    return _Pwin(me, you, pending)


def best_action(state):
 # return the optimal action for a state
 # define key ev (exp. value) for max function

    def ev(action): return ev_action(state, action, p_win)
    return max(legal_actions(state), key=ev)

def ev_action(state, action, p_win):
    """The expected value of an action in this state.
     p_win is the utility function, i.e. the probability of winning: 1 point for winning and 0 points for loosing
    We will look into the possible future, consider all legal actions, until the goal is reached
    """
    if action == 'hold':
        # if we hold, our opponent will move, our probability of winning is 1 - p_win(opponent)
        return 1 - p_win(hold(state))
    if action == 'roll':
        # if d==1: it's a pig-out, our opponent will move, our probability of winning is 1 - p_win(opponent)
        # if d >1: get p_win for each value of d and calculate average
        # return (1 - p_win(roll(state, 1)) + sum(p_win(roll(state, d)) for d in (2,3,4,5,6))) / 6
        total = 1 - p_win(roll(state, 1))
        for d in (2, 3, 4, 5, 6):
            total = total + p_win(roll(state, d))
            # print(total)
        print(float (total/6))
        return float(total/6)

    raise ValueError








def check_victory(state):
    global gamecounter
    global game_state
    if state[1] >= goal_score:
        print(state.__str__() + "  me heeft gewonnen")
        victories[0] += 1
        game_state = ["you", 0, 0, 0]
        gamecounter += 1
    elif state[2] >= goal_score:
        print(state.__str__() + "  you heeft gewonnen")
        victories[1] += 1
        game_state = ["me", 0, 0, 0]
        gamecounter += 1


def roll_dice():
    roll_value = random.randint(1, 6)
    return roll_value


# while gamecounter < 100:
#     just_play(game_state)
# print(victories)

print(best_action(game_state))

game_state = ['me', 0,0,0]
print(p_win(game_state))
 #opgave c: hold at 20 is veel beter; die wint meer dan 2/3 keer