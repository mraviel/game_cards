from unittest import TestCase
from CardGame import CardGame
from DeckOfCards import DeckOfCards
from Card import Card


class TestCardGame(TestCase):

    def setUp(self):
        self.cardGame = CardGame("alon", "aviel", 20)

    def test__init__valid(self):
        """ Test valid """

        self.assertEqual(self.cardGame.player1.name, "alon")
        self.assertEqual(self.cardGame.player2.name, "aviel")
        self.assertEqual(self.cardGame.player1.cards_per_player, 20)
        self.assertEqual(self.cardGame.player2.cards_per_player, 20)

    def test__init__invalid_type(self):
        """ Test invalid type """

        with self.assertRaises(TypeError):
            CardGame(1, "aviel", 20)

        with self.assertRaises(TypeError):
            CardGame("alon", 1, 20)

        with self.assertRaises(TypeError):
            CardGame("alon", "aviel", "nofar")

    def test__init__invalid_value(self):
        """ Test invalid value """

        with self.assertRaises(ValueError):
            CardGame("alon", "aviel", 9)

        with self.assertRaises(ValueError):
            CardGame("alon", "aviel", 27)

    def test___new_game_valid(self):
        """ Test valid"""

        deck = DeckOfCards()  # Un-shuffled deck
        count = 0
        for i in range(3):
            if deck.cards == self.cardGame.deck.cards:
                count += 1

        # Is deck shuffled?
        self.assertNotEqual(count, 3)

        # Is player's hand have cards_per_player number of cards?
        self.assertEqual(len(self.cardGame.player1.hand), self.cardGame.player1.cards_per_player)  # 20
        self.assertEqual(len(self.cardGame.player2.hand), self.cardGame.player2.cards_per_player)  # 20

    def test___new_game_invalid(self):
        """ Test invalid """

        deck = DeckOfCards()  # Un-shffeld deck
        count = 0
        for i in range(3):
            if deck.cards == self.cardGame.deck.cards:
                count += 1

        # Is deck shuffled?
        with self.assertRaises(AssertionError):
            self.assertEqual(count, 3)

        with self.assertRaises(AssertionError):
            # Is player's hand have cards_per_player number of cards?
            self.assertNotEqual(len(self.cardGame.player1.hand), self.cardGame.player1.cards_per_player)  # 20
            self.assertNotEqual(len(self.cardGame.player2.hand), self.cardGame.player2.cards_per_player)  # 20

    def test_get_winner_valid_tie(self):
        """ Test valid, Check if both players with the same amount of cards, Equal """
        self.assertEqual(len(self.cardGame.player1.hand), len(self.cardGame.player2.hand))
        self.assertIsNone(self.cardGame.get_winner())

    def test_get_winner_valid_player1_win(self):
        """ Test valid Check that player1 have more cards than player2"""
        card = Card(4, "Dimond")
        self.cardGame.player1.add_card(card)
        self.assertGreater(len(self.cardGame.player1.hand), len(self.cardGame.player2.hand))
        self.assertEqual(self.cardGame.player1, self.cardGame.get_winner())

    def test_get_winner_valid_player2_win(self):
        """ Test valid Check that player2 have more cards than player1 """
        card = Card(4, "Dimond")
        self.cardGame.player2.add_card(card)
        self.assertGreater(len(self.cardGame.player2.hand), len(self.cardGame.player1.hand))
        self.assertEqual(self.cardGame.player2, self.cardGame.get_winner())

    def test_get_winner_invalid(self):
        """ Test invalid, Check if both players with the same amount of cards, Equal """
        with self.assertRaises(AssertionError):
            self.assertNotEqual(len(self.cardGame.player1.hand), len(self.cardGame.player2.hand))

        with self.assertRaises(AssertionError):
            self.assertIsNotNone(self.cardGame.get_winner())

    def test_get_winner_invalid_player1_win(self):
        """ Test invalid Check that player1 have more cards than player2 """
        card = Card(4, "Dimond")
        self.cardGame.player1.add_card(card)

        with self.assertRaises(AssertionError):
            self.assertLess(len(self.cardGame.player1.hand), len(self.cardGame.player2.hand))
        with self.assertRaises(AssertionError):
            self.assertNotEqual(self.cardGame.player1, self.cardGame.get_winner())

    def test_get_winner_invalid_player2_win(self):
        """ Test invalid Check that player2 have more cards than player1 """
        card = Card(4, "Dimond")
        self.cardGame.player2.add_card(card)

        with self.assertRaises(AssertionError):
            self.assertLess(len(self.cardGame.player2.hand), len(self.cardGame.player1.hand))
        with self.assertRaises(AssertionError):
            self.assertNotEqual(self.cardGame.player2, self.cardGame.get_winner())











