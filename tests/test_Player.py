from unittest import TestCase, mock
from Player import Player
from DeckOfCards import DeckOfCards
from Card import Card


class TestPlayer(TestCase):

    def setUp(self):
        self.player = Player("Alon", 15)

    def test__init__valid(self):
        """ Test valid name and num of cards per player """
        self.assertEqual(self.player.name, "Alon")
        self.assertEqual(self.player.cards_per_player, 15)
        self.assertEqual(self.player.hand, [])

    def test__init__invalid_name_type(self):
        """ Test invalid name type wrong"""
        with self.assertRaises(TypeError):
            player = Player(6, 17)

    def test__init__invalid_num_of_cards_type(self):
        """ Test invalid num of cards type """
        with self.assertRaises(TypeError):
            player = Player("ALON", "no")

    def test__init__invalid_num_of_cards_value_27(self):
        """ Test invalid too many cards per hand """
        with self.assertRaises(ValueError):
            player = Player("alon", 27)

    def test__init__invalid_num_of_cards_value_9(self):
        """ Test invalid too fewer cards per hand """
        with self.assertRaises(ValueError):
            player = Player("alon", 9)

    def test_set_hand_valid(self):
        """ Test valid """

        deck = DeckOfCards()
        self.player.set_hand(deck)
        self.assertEqual(len(self.player.hand), 15)
        self.assertEqual(len(deck.cards), 37)

    @mock.patch("DeckOfCards.DeckOfCards.deal_one", return_value=Card(2, "Dimond"))
    def test_set_hand_valid_is_card_from_deal_one_in_player_hand(self, mock_name):
        """ Test valid is card from deal_one in player hand """
        deck = DeckOfCards()
        self.player.set_hand(deck)
        self.assertIn(Card(2, "Dimond"), self.player.hand)

    def test_set_hand_invalid_deck_card(self):
        """ Test invalid deck is not type deck of cards """
        deck = 52
        with self.assertRaises(TypeError):
            self.player.set_hand(deck)

    def test_get_card_valid(self):
        """ Test valid """
        deck = DeckOfCards()
        self.player.set_hand(deck)

        card = self.player.get_card()
        self.assertEqual(len(self.player.hand), 14)
        self.assertNotIn(card, self.player.hand)

    def test_get_card_invalid(self):
        """ Test invalid """
        deck = DeckOfCards()
        self.player.set_hand(deck)

        card = self.player.get_card()

        with self.assertRaises(AssertionError):
            self.assertEqual(len(self.player.hand), 15)
            self.assertIn(card, self.player.hand)

    def test_add_card_valid(self):
        """ Test valid """
        card=Card(8, "Dimond")
        self.player.add_card(card)
        self.assertEqual(len(self.player.hand), 1)
        self.assertIn(card, self.player.hand)

    def test_add_card_invalid_card_type(self):
        """ Test invalid card type """
        with self.assertRaises(TypeError):
            card = 8
            self.player.add_card(card)

    def test_add_card_invalid_card_not_in_hand(self):
        """ Test invalid card not in hand """
        card = Card(8, "Dimond")
        with self.assertRaises(AssertionError):
            self.player.add_card(card)
            self.assertNotIn(card, self.player.hand)














