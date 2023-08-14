from deck import Deck
from player import Player
from random import choice

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    def play_game(self):
        print('Welcome to Blackjack!\n')
        gameplay_choice = input('Would you like to [p]lay, hear the [r]ules, or [q]uit? [p/r/q] ').lower()
        if gameplay_choice == 'p':
            print("Alright! Let's play some blackjack!")
            self.game_flow()
        elif gameplay_choice == 'r':
            self.rules()
        elif gameplay_choice == 'q':
            self.quit()
        
    
    def gameplay(self):
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0

        while len(self.player_hand) < 2:
            player_card = self.deck.deal_card()
            self.player_hand.append(player_card)
            # self.deck.remove(player_card)
            self.player_score += player_card.card_value
            self.player.print_hand(hidden=False)

            dealer_card = self.deck.deal_card()
            self.dealer_hand.append(dealer_card)
            # self.deck.remove(dealer_card)
            self.dealer_score += dealer_card.card_value
            self.dealer.print_hand(hidden=True)

        self.bust()

    def bust(self):
        self.player.print_hand(hidden=False)
        self.dealer.print_hand(hidden=False)
        if self.player_score > 21:
            print("You bust! Better luck next time!")
            self.quit()
        if self.dealer_score > 21:
            print("Dealer busts! Congrats!")
            self.quit()

    def game_flow(self):
        self.gameplay()
        while True:
            first_choice = input("What would you like to do: [H]it or [S]tand? [h/s] ").lower()
            try:
                if first_choice == 'h':
                    self.hit()
                elif first_choice == 's':
                    self.stand()
                else:
                    print("Please enter a valid choice [h/s]")
            except ValueError:
                print("Invalid input. Please enter a valid choice [h/s]")

    def hit(self):
        player_card = self.deck.deal_card()
        self.player_hand.append(player_card)
        self.deck.remove(player_card)
        self.player_score += player_card.card_value
        if self.player_score > 21:
            self.bust()
        else:
            print(f"You're sitting at a {self.player_score}.")
            self.game_flow()

    def stand(self):
        self.player.print_hand(hidden=False)
        self.dealer.print_hand(hidden=False)
        dealer_total = 21 - self.dealer_score
        player_total = 21 - self.player_score
        print(f"Dealer: {dealer_total}, You: {player_total}")
        if dealer_total < player_total:
            print(f"Dealer has a {dealer_total}. Dealer wins!")
        elif player_total < dealer_total:
            print(f"You have {player_total}; You win! Great job!")
        elif player_total == dealer_total:
            print("It's a push! [tie].")
        if dealer_total > 21:
            print("Dealer busts! Congrats!")
        self.quit()

    def rules(self):
        print("\nSounds good, let's learn about blackjack.\n\n")
        print("The Rules of Blackjack: \n The rules of blackjack are rather straightforward: simply try to get closer to 21 than the dealer without going over. If either you or the deal exceeeds 21, you Bust and lose the round. \n")
        print("Scoring:\nA player's score is the total value of the cards in their hand. Card values range from 1-11 with the Ace being worth 11 or 1, number cards being worth their respective number, and face cards being valued at 10.\n")
        print("Dealing: \n Two cards are dealt to each player: \n First: the dealer deals the player one card face up and then one card to themselves face up as well. \n Second: The dealer deals the player another card face up with the dealer too receives another card, but face down. In other words, the game starts once each player has two cards, two face-up cards for the player and one face-up and one face-down card.\n")
        print("Gameplay: \nOnce the player is dealt their cards they have a few options:\n   1. if they have a total of 21 after the initial dealing, the player scores Blackjack and automatically wins.\n   2. If the play is dissatisfied with their cards they can request an additional card by calling '[H]it'. The dealer must hit until their hand is greater than or equal to 17. The player can continue to hit as many times as they would like until they are satisfied or they have exceeded 21 and bust, losing the hand.\n   3. If the player is satisfied with their cards and is ready to see the results they can [S]tand which stops the round and forces the dealer to reveal their cards.\nThe round is decided by whoever is closer to 21 without exceeding it.")
        rules_input = input('Would you like to read the [r]ules again, [p]lay the game, or [q]uit? [r/p/q] ').lower()
        try:
            if rules_input == 'r':
                self.rules()
            elif rules_input == 'p':
                print("Let's play some blackjack!")
                self.gameplay()
            elif rules_input == 'q':
                self.quit()
        except ValueError:
            print("Sorry, I didn't catch that. Please try again using either [r]ules/[p]lay/[q]uit ")

    def quit(self):
        print("Please come and play again soon!")

if __name__ == '__main__':
    blackjack = Blackjack()
    blackjack.play_game()
