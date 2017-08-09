import random

class RackO:

    def __init__(self, deck_size=50, hand_size=10, hands_up=False, deck=None):
        # parameters from input
        self.deck_size = deck_size
        self.hand_size = hand_size
        self.hands_up = hands_up
        if deck:
            self.deck = deck
        else:
            self.deck = range(1, deck_size + 1)
            random.shuffle(self.deck)

        # game state initialization
        self.player_turn = 0
        self.num_players = 2
        self.hands = [[] for i in range(self.num_players)]
        self.discard = []

        # start the game
        self.deal_hands()
        self.discard.append(self.deck.pop())

    def deal_hands(self):
        for i in range(self.num_players):
            for j in range(self.hand_size):
                self.hands[i].append(self.deck.pop())

    def check_deck(self):
        return self.deck[-1]

    def draw_from_deck(self, hand_position):
        self.hands[self.player_turn].insert(hand_position, self.deck.pop())

    def check_discard(self):
        return self.discard[-1]

    def draw_from_discard(self, hand_position):
        self.hands[self.player_turn].insert(hand_position, self.discard.pop())

    def game_over(self):
        for i in range(self.num_players):
            hand_won = True
            for j in range(1, self.hand_size):
                if self.hands[i][j] < self.hands[i][j - 1]:
                    hand_won = False
            if hand_won:
                return True
        return False

    def game_loop(self):
        pass

    def print_state(self):
        print(self.deck)
        print(self.discard)
        print(self.hands)


if __name__ == '__main__':
    rack_o = RackO(deck_size=10, hand_size=3, deck=[3, 1, 9, 6, 4, 7, 2, 10, 8, 5])
    # rack_o.print_state()
    # print rack_o.check_deck()
