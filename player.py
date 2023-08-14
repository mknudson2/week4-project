from deck import Deck

class Player:
    def __init__(self, is_dealer, deck):
        self.hand = []
        self.score = 0
        self.is_dealer = is_dealer
        self.deck = deck

    def deal_initial_cards(self):
        for _ in range(2):
            card = self.deck.deal_card()
            self.hand.append(card)
            self.score += card.card_value

    def hit(self):
        card = self.deck.deal_card()
        self.hand.append(card)
        self.score += card.card_value

    def print_hand(self, hidden):
        self.deck.print_cards(self.hand, hidden)

    def check_blackjack(self):
        return self.score == 21

    def check_bust(self):
        return self.score > 21
