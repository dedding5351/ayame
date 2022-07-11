from click import command
from objects.deck import Deck
from objects.player import Player

def next_hand():
    replay = input("Would you like to play again? Type play or quit")
    if replay.lower() == "play":
        player.reset_hand()
        game.deal(player)
        print(player.get_hand(), player.hand_value)
    elif replay.lower() == "quit":
        return

number_of_decks = input("How many decks would you like to play with?")
game = Deck()
game.shuffle()
# print(game.cards)


player_name = input("Lets play blackjack tell me your name!")
player = Player(player_name)

game.deal(player)
print(player.get_hand(), player.hand_value)
while player.hand_value < 1000000:
    command = input("Would you like to hit?")

    if command.lower() == 'y':
        game.hit(player)
        print(player.get_hand(), player.hand_value)
    
    if player.hand_value > 21:
        print(f"{player.name} you busted at {player.hand_value}")
        next_hand()

    if player.hand_value == 21:
        print(f"{player.name} hit blackjack")
        player.reset_hand()
        break