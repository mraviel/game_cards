from Player import Player
from DeckOfCards import DeckOfCards


class CardGame:

    def __init__(self, player1_name, player2_name, cards_per_player):
        """ Init, Create new game. """

        if type(player1_name) != str:
            raise TypeError("the Player name must be str")
        if type(player2_name) != str:
            raise TypeError("the Player name must be str")
        if type (cards_per_player) != int:
            raise TypeError("the num of the cards per player must be int")

        if cards_per_player > 26 or cards_per_player < 10:
            raise ValueError("the cards per player must be between 10 and 26.")

        self.deck = DeckOfCards()

        self.player1 = Player(player1_name, cards_per_player)
        self.player2 = Player(player2_name, cards_per_player)

        self.__new_game()

    def __new_game(self):
        """ New game, Shuffle provide cards for each player. """

        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)

    def get_winner(self):
        """ Check for winner, Return: player (Player) OR None if equal. """

        if len(self.player1.hand) == len(self.player2.hand):
            return None
        elif len(self.player1.hand) > len(self.player2.hand):
            return self.player1
        else:
            return self.player2


if __name__ == "__main__":

    player = Player("aviel", 15)

    game = CardGame("aviel", "alon", 15)
    print(game)

    # game.__new_game()
