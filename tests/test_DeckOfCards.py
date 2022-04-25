from unittest import TestCase
from DeckOfCards import DeckOfCards
from Card import Card


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck = DeckOfCards()

    def test__init__valid(self):
        """ Test valid """

        # Check that there are 52 cards.
        self.assertEqual(len(self.deck.cards), 52)

        # Check that all cards are exits.
        for value in range(1, 14):
            for suit in ["Dimond", "Club", "Spade", "Heart"]:
                self.assertIn(Card(value, suit), self.deck.cards)

    def test__init__invalid(self):
        """ Test invalid """

        # Check that there are 52 cards.
        with self.assertRaises(AssertionError):
            self.assertNotEqual(len(self.deck.cards), 52)

        # Check that all cards are exits.
        with self.assertRaises(AssertionError):
            for value in range(1, 14):
                for suit in ["Dimond", "Club", "Spade", "Heart"]:
                    self.assertNotIn(Card(value, suit), self.deck.cards)

    def test_cards_shuffle_valid(self):
        """ Test valid """
        deck_cards = self.deck.cards.copy()
        self.deck.cards_shuffle()
        count = 0
        for i in range(3):
            if deck_cards == self.deck.cards:
                count += 1

        self.assertNotEqual(count, 3)

    def test_cards_shuffle_invalid(self):
        """ Test invalid """
        deck_cards = self.deck.cards.copy()
        self.deck.cards_shuffle()
        count = 0
        for i in range(3):
            if deck_cards == self.deck.cards:
                count += 1

        with self.assertRaises(AssertionError):
            self.assertEqual(count, 3)

    def test_deal_one_valid(self):
        """ Test valid """

        card = self.deck.deal_one()

        # Check that 1 card has been deleted.
        self.assertEqual(len(self.deck.cards), 51)

        # Is the card in deck cards?
        self.assertNotIn(card, self.deck.cards)

    def test_deal_one_invalid(self):
        """ Test invalid """

        card = self.deck.deal_one()

        with self.assertRaises(AssertionError):
            # Check that 1 card has been deleted.
            self.assertNotEqual(len(self.deck.cards), 51)

            # Is the card in deck cards?
            self.assertIn(card, self.deck.cards)










