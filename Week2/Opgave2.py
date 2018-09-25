import random


class Players:
    current_score = 0
    victories = 0

    def __init__(self, name):
        self.name = name

    def reset_score(self):
        self.current_score = 0

    def add_to_victories(self):
        self.victories += 1

    def add_to_score(self, score):
        self.current_score += score

    def add_one(self):
        self.current_score += 1


class GameState:
    goal_score = 100

    pending_score = 0

    game_counter = 0
    hold_at_20 = 20
    hold_at_x_other = 10

    def __init__(self, me, you):
        self.me = me
        self.you = you
        self.current_player = me

    def change_player(self):
        if self.current_player == self.me:
            self.current_player = self.you
        elif self.current_player == self.you:
            self.current_player = self.me

    def game_to_list(self):
        return [self.me.current_score, self.you.current_score, self.pending_score]

    def reset_scores(self):
        self.game_counter += 1
        self.me.reset_score()
        self.you.reset_score()
        self.pending_score = 0
        self.change_player()

    def add_to_score(self):
        if self.current_player == self.me:
            self.me.add_to_score(self.pending_score)
        elif self.current_player == self.you:
            self.you.add_to_score(self.pending_score)

    def clear_pending_score(self):
        self.pending_score = 0

    def rolled_one(self):
        if self.current_player == self.me:
            self.me.add_one()
            self.clear_pending_score()
            self.change_player()
        elif self.current_player == self.you:
            self.you.add_one()
            self.clear_pending_score()
            self.change_player()

    def check_victory(self):
        if self.me.current_score >= self.goal_score:
            print(self.game_to_list().__str__() + "  me heeft gewonnen")
            self.me.add_to_victories()
            self.reset_scores()

        elif self.you.current_score >= self.goal_score:
            print(self.game_to_list().__str__() + "  you heeft gewonnen")
            self.you.add_to_victories()
            self.reset_scores()


class Moves:
    @staticmethod
    def roll(game, d):
        if d == 1:
            game.rolled_one()
        elif d > 1:
            game.pending_score += d

    @staticmethod
    def hold(game):
        game.add_to_score()
        game.clear_pending_score()
        game.change_player()

    @staticmethod
    def hold_at_x(game, hold):
        if game.pending_score >= hold:
            return True


class Strategies:
    @staticmethod
    def roll_dice():
        roll_value = random.randint(1, 6)
        return roll_value

    @staticmethod
    def clueless(game):
        possible_moves = ['roll', 'hold']
        random_move = random.SystemRandom().choice(possible_moves)
        if random_move == "roll":
            if Moves.hold_at_x(game, game.hold_at_20):
                Moves.hold(game)
            else:
                Moves.roll(game, Strategies.roll_dice())
        elif random_move == "hold":
            Moves.hold(game)

    @staticmethod
    def play_smart(game):
        game.check_victory()
        if game.current_player == game.me:
            if Moves.hold_at_x(game, game.hold_at_x_other):
                Moves.hold(game)
            else:
                Moves.roll(game, Strategies.roll_dice())
        if game.current_player == game.you:
            if Moves.hold_at_x(game, game.hold_at_20):
                Moves.hold(game)
            else:
                Moves.roll(game, Strategies.roll_dice())

    @staticmethod
    def legal_actions(game):
        if game.pending_score == 0:
            return "roll"
        else:
            return "hold"

    @staticmethod
    def win_probability(game):
        possible_moves = ['roll', 'hold']
        if game.current_player.current_score + game.pending_score >= game.goal_score:
            return 1
        elif game.other_player.current_score >= game.goal_score:
            return 0
        else:
            return max(Strategies.ev_action(game, Strategies.legal_actions(), Strategies.win_probability) for action in possible_moves)
    # The value of a state: the probability that an optimal player whose turn it is
    # can win from the current state.

    @staticmethod
    def best_action(game):
        # return the optimal action for a state
        # define key ev (exp. value) for max function
        def ev(action): return Strategies.ev_action(game, action, Strategies.win_probability(game))
        return max(Strategies.legal_actions(game), key=ev)

    @staticmethod
    def ev_action(game, action, p_win):
        """The expected value of an action in this state.
        p_win is the utility function, i.e. the probability of winning: 1 point for winning and 0 points for loosing
        We will look into the possible future, consider all legal actions, until the goal is reached
        """
        if action == "hold":
            # if we hold, our opponent will move, our probability of winning is 1 - p_win(opponent)
            return 1 - p_win(Moves.hold(game))
        if action == "roll":
            # if d==1: it's a pig-out, our opponent will move, our probability of winning is 1 - p_win(opponent)
            # if d >1: get p_win for each value of d and calculate average
            return (1 - p_win(Moves.roll(game, 1)) + sum(p_win(Moves.roll(game, Strategies.roll_dice())) for Strategies.roll_dice() in (2,3,4,5,6))) / 6.0
        raise ValueError


new_game = GameState(Players("me"), Players("you"))

while new_game.game_counter < 100:
    Strategies.play_smart(new_game)
print("me heeft " + new_game.me.victories.__str__() + " keer gewonnen, en you " + new_game.you.victories.__str__())


'''
opgave c: hold at 20 is veel beter; die wint meer dan 2/3 keer

opgave d: de verwachte worp is gemiddeld 3,5; (1+2+3+4+5+6)/6
            je kan ongeveer 5x gooien voor dat je een 1 krijgt
            dus 5*3,5 = 17,5
'''

