import random

possible_moves = ['roll', 'hold']
goal_score = 100
victories = [0, 0]
gamecounter = 0

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
        elif state[0] == "you":
            new_score = state[2] + d
            state[2] = new_score
            state[3] = 0
            state[0] = "me"
    elif d > 1:
        score = state[3] + d
        state[3] = score


'''
    Apply a hold to yield a new state: add the pending points to my total points and
    it becomes the other player's turn.
'''
def hold(state):
    if state[0] == "me":
        new_score = state[3] + state[1]
        state[1] = new_score
        state[3] = 0
        state[0] = "you"
        return tuple(state)
    elif state[0] == "you":
        new_score = state[3] + state[2]
        state[2] = new_score
        state[3] = 0
        state[0] = "me"
        return tuple(state)


def hold_at_x(state, hold):
    if state[3] >= hold:
        return True


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

#opgave c: hold at 20 is veel beter; die wint meer dan 2/3 keer


