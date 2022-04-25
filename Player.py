from DeckOfCards import DeckOfCards
from Card import Card
from random import choice


class Player:

    def __init__(self, name, cards_per_player=26):

        if type(name) != str:
            raise TypeError("Name must be str")
        if type(cards_per_player) != int:
            raise TypeError("Num_per_player must be int")

        if cards_per_player > 26 or cards_per_player < 10:
            raise ValueError("cards_per_player must be between 10 and 26")

        self.name = name
        self.hand = []
        self.cards_per_player = cards_per_player

    def __repr__(self):
        return f"(name={self.name}, hand={self.hand}, card_per_player{self.cards_per_player})"

    def set_hand(self, deck):
        """ Args: deck (DeckOfCards), Provide cards for player by number of cards."""

        if type(deck) != DeckOfCards:
            raise TypeError("Valid deck must be provided.")

        for i in range(self.cards_per_player):
            self.hand.append(deck.deal_one())

    def get_card(self):
        """ Pick one random card from player hand, Delete from hand. Return the pop card: (Card). """

        if self.hand:
            return self.hand.pop(self.hand.index(choice(self.hand)))

    def add_card(self, card):
        """ Args: card (Card), Add card to player hand. """

        if type(card) != Card:
            raise TypeError("The card must be type Card.")

        self.hand.append(card)


if __name__ == "__main__":

    player1 = Player("aviel", 12)
    deck = DeckOfCards()

    player1.set_hand(deck)



