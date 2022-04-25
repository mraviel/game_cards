from unittest import TestCase
from Card import Card


class TestCard(TestCase):

    def test__init__valid(self):
        """ Test valid init """
        card = Card(8, "Spade")
        self.assertEqual(card.value, 8)
        self.assertEqual(card.suit, "Spade")

    def test__init__invalid_value_type(self):
        """ Test invalid value type """
        with self.assertRaises(TypeError):
            card = Card("8s", "Spade")

    def test__init__invalid_value_error(self):
        """ Test invalid value is 14 """
        with self.assertRaises(ValueError):
            card = Card(14, "Spade")

    def test__init__invalid_value_error_0(self):
        """ Test invalid value 0 """
        with self.assertRaises(ValueError):
            card = Card(0, "Spade")

    def test__init__invalid_suit_type(self):
        """ Test invalid suit type """
        with self.assertRaises(TypeError):
            card = Card(8, 6)

    def test__init__invalid_suit_value(self):
        """ Test invalid suit value """
        with self.assertRaises(ValueError):
            card = Card(-1, "Lemon")

    def test__gt__valid_higher_card(self):
        """ Test valid card1 is greater than card2 """

        card1 = Card(7, "Spade")
        card2 = Card(2, "Dimond")

        self.assertGreater(card1, card2)

    def test__gt__valid_same_suit(self):
        """ Test valid card1 is greater than card2 with same suit """

        card1 = Card(7, "Dimond")
        card2 = Card(2, "Dimond")

        self.assertGreater(card1, card2)

    def test__gt__valid_same_value(self):
        """ Test valid, card1 is greater than card2 with same value """

        card1 = Card(7, "Spade")
        card2 = Card(7, "Dimond")

        self.assertGreater(card1, card2)

    def test__gt__valid_ace_win_always(self):
        """ Test valid, Ace card always wins no meeter what  """

        card1 = Card(1, "Spade")
        card2 = Card(7, "Dimond")

        self.assertGreater(card1, card2)

    def test__gt__invalid_same_card(self):
        """ Test invalid, card1 is greater than card2 with same value and suit """

        card1 = Card(7, "Dimond")
        card2 = Card(7, "Dimond")
        with self.assertRaises(ValueError):
            self.assertGreater(card1, card2)

    def test__gt__invalid_different_type_card(self):
        """ Test invalid, Can not be compared to something that is not card """

        card1 = Card(7, "Dimond")

        with self.assertRaises(TypeError):
            self.assertGreater(card1, 7)

    def test__eq__valid_same_card(self):
        """ Test valid, card1 is equal to card2 """

        card1 = Card(7, "Dimond")
        card2 = Card(7, "Dimond")

        self.assertEqual(card1, card2)

    def test__eq__invalid_different_type_card(self):
        """ Test invalid, Can not be compared to something that is not card """

        card1 = Card(7, "Dimond")

        with self.assertRaises(TypeError):
            self.assertEqual(card1, 7)













