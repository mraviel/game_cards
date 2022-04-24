from Card import Card
from Player import Player
from CardGame import CardGame
from DeckOfCards import DeckOfCards

if __name__ == "__main__":

    name1 = input("Player1 name: ")
    name2 = input("Player2 name: ")

    cardGame = CardGame(name1, name2, 26)



    # player1 = Player(name1)
    # player2 = Player(name2)
    #
    print(f"player1 name is {cardGame.player1.name} \n{cardGame.player1.hand}")
    print(f"player2 name is {cardGame.player2.name} \n{cardGame.player2.hand}")

    for i in range(10):

        player1_card = cardGame.player1.get_card()
        player2_card = cardGame.player2.get_card()

        print(f"player1 throw:{player1_card}\nplayer2 throw:{player2_card}")

        if player1_card > player2_card:
            cardGame.player1.add_card(player1_card)
            cardGame.player1.add_card(player2_card)
        else:
            cardGame.player2.add_card(player1_card)
            cardGame.player2.add_card(player2_card)

    print(cardGame.get_winner())

