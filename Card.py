
class Card:

    def __init__(self, value, suit):
        """ Args: value (int), suit (str). Init the card. """

        # Check type
        if type(value) != int:
            raise TypeError("Value must be number")
        if type(suit) != str:
            raise TypeError("Suit must be str")

        # Value between 1 - 13
        if value < 1 or value > 13:
            raise ValueError("Card value must be between 1 to 13")

        # Suit is in the list_of_suits
        list_of_suits = ["Dimond", "Heart", "Club", "Spade"]
        if suit not in list_of_suits:
            raise ValueError("Suit must be Dimond OR heart OR Club OR Spade")

        self.value = value
        self.suit = suit

    def __eq__(self, other):
        """ Check for identical card. """
        if type(other) != Card:
            raise TypeError("Must be type Card")

        return self.value == other.value and self.suit == other.suit

    def __gt__(self, other):
        """ Card will be greater by value. """

        # Check type
        if type(other) != Card:
            raise TypeError("Must be type Card")

        if self.value != other.value:

            # 1 is the greatest of all cards
            if self.value == 1 or other.value == 1:
                return other.value > self.value

            return self.value > other.value

        else:

            # Dimond is the lowest And Club is highest.
            cards_type = ["Dimond", "Spade", "Heart", "Club"]

            self_location = cards_type.index(self.suit)
            other_location = cards_type.index(other.suit)

            if self_location == other_location:
                raise ValueError("Can not be two similar cards from same suit")

            return self_location > other_location

    def __repr__(self):
        special_values = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

        if self.value in special_values.keys():
            return f"(value={special_values[self.value]}, suit={self.suit})"
        else:
            return f"(value={self.value}, suit={self.suit})"


if __name__ == "__main__":

    card1 = Card(1, "Dimond")
    card2 = Card(2, "Dimond")

    print(card1 > card2)

    print(card1)


