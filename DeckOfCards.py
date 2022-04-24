from Card import Card
from random import shuffle, choice


class DeckOfCards:

    def __init__(self):
        """ Init cards to have all values and suit for card. """

        self.cards = []
        for value in range(1, 14):
            for suit in ["Dimond", "Spade", "Heart", "Club"]:
                card = Card(value, suit)
                self.cards.append(card)

    def __repr__(self):
        return f"{self.cards}"

    def cards_shuffle(self):
        """ Shuffle the deck of the cards. """

        shuffle(self.cards)

    def deal_one(self):
        """ Pick one random card from cards, Delete from cards. Return the pop card: (Card). """

        return self.cards.pop(self.cards.index(choice(self.cards)))


if __name__ == "__main__":

    deck = DeckOfCards()

    deck.cards_shuffle()

    a = deck.deal_one()
    print(a)
