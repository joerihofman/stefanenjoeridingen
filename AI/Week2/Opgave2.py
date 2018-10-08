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


game_state = ["me", 0, 0, 0]


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
            new_score = state[2] + d
            reset_me(state, new_score)
            return state
        elif state[0] == "you":
            new_score = state[2] + d
            reset_you(state, new_score)
            return state
    else:
        score = state[3] + d
        state[3] = score
        return state

'''
    Apply a hold to yield a new state: add the pending points to my total points and
    it becomes the other player's turn.
'''


def hold(state):
    if state[0] == "me":
        new_score = state[3] + state[1]
        reset_me(state, new_score)
        return state
    elif state[0] == "you":
        new_score = state[3] + state[2]
        reset_you(state, new_score)
        return state


def reset_me(state, new_score):
    state[1] = new_score
    state[3] = 0
    state[0] = "you"


def reset_you(state, new_score):
    state[2] = new_score
    state[3] = 0
    state[0] = "me"


def hold_at_x(state, hold):
    if state[3] >= hold:
        return True


def legal_actions(state):
    # The legal actions from a state. If pending == 0 then we must roll
    if state[3] == 0:
        return ['roll']
    else:
        return ['roll', 'hold']


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

        return total if not pending else max(1 - _Pwin(you, me + pending, 0), total)
    return _Pwin(me, you, pending)


def best_action(state):
    def ev(action): return ev_action(state, action, p_win)
    return max(legal_actions(state), key=ev)


def ev_action(state, action, p_win):
    """The expected value of an action in this state.
     p_win is the utility function, i.e. the probability of winning: 1 point for winning and 0 points for loosing
    We will look into the possible future, consider all legal actions, until the goal is reached
    """
    if action == 'hold':
        return 1 - p_win(hold(state))
    if action == 'roll':
        total = 1 - p_win(roll(state, 1))
        for d in (2, 3, 4, 5, 6):
            total = total + p_win(roll(state, d))
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


while gamecounter < 100:
    just_play(game_state)
print(victories)

# print(best_action(game_state))

# game_state = ['me', 0,0,0]
# print(p_win(game_state))


'''
opgave c: hold at 20 is veel beter; die wint meer dan 2/3 keer

opgave d: de verwachte worp is gemiddeld 3,5; (1+2+3+4+5+6)/6
            je kan ongeveer 5x gooien voor dat je een 1 krijgt
            dus 5*3,5 = 17,5
'''

