import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def generate(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        suits_values = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
        cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

        for suit in suits:
            for card in cards:
                self.cards.append(Card(suits_values[suit], card, cards_values[card]))

    def deal_card(self):
        if not self.cards:
            self.generate()  #Will regenerate the deck if empty
        return self.cards.pop(random.randint(0, len(self.cards) - 1))
    
    def print_cards(self, cards, hidden):
        def print_cards(cards, hidden):
            s = ""
            for card in cards:
                s = s + "\t ________________"
            if hidden:
                s += "\t ________________"
            print(s)
        
        
            s = ""
            for card in cards:
                s = s + "\t|                |"
            if hidden:
                s += "\t|                |"    
            print(s)
        
            s = ""
            for card in cards:
                if card.value == '10':
                    s = s + "\t|  {}            |".format(card.value)
                else:
                    s = s + "\t|  {}             |".format(card.value)  
            if hidden:
                s += "\t|                |"    
            print(s)
        
            s = ""
            for card in cards:
                s = s + "\t|                |"
            if hidden:
                s += "\t|      * *       |"
            print(s)    
        
            s = ""
            for card in cards:
                s = s + "\t|                |"
            if hidden:
                s += "\t|    *     *     |"
            print(s)    
        
            s = ""
            for card in cards:
                s = s + "\t|                |"
            if hidden:
                s += "\t|   *       *    |"
            print(s)    
        
            s = ""
            for card in cards:
                s = s + "\t|                |"
            if hidden:
                s += "\t|   *       *    |"
            print(s)    
        
            s = ""
            for card in cards:
                s = s + "\t|       {}        |".format(card.suit)
            if hidden:
                s += "\t|          *     |"
            print(s)    
        
            s = ""
            for card in cards:
                s = s + "\t|                |"
            if hidden:
                s += "\t|         *      |"
            print(s)    
        
            s = ""
            for card in cards:
                s = s + "\t|                |"
            if hidden:
                s += "\t|        *       |"
            print(s)
        
            s = ""
            for card in cards:
                s = s + "\t|                |"
            if hidden:
                s += "\t|                |"
            print(s)
        
            s = ""
            for card in cards:
                s = s + "\t|                |"
            if hidden:
                s += "\t|                |"
            print(s)    
        
            s = ""
            for card in cards:
                if card.value == '10':
                    s = s + "\t|            {}  |".format(card.value)
                else:
                    s = s + "\t|            {}   |".format(card.value)
            if hidden:
                s += "\t|        *       |"        
            print(s)    
                
            s = ""
            for card in cards:
                s = s + "\t|________________|"
            if hidden:
                s += "\t|________________|"
            print(s)        
        
            print()
