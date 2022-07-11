from click import command
from objects.deck import Deck
from objects.player import Player
from objects.dealer import Dealer

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
print(len(game.cards))


player_name = input("Lets play blackjack tell me your name! ")
player = Player(player_name)
dealer = Dealer()

for i in range(0,2):
    game.deal(dealer)
    game.deal(player)
    print(i)

print (f"{dealer.hidden_card()}")
print(player.get_hand(), player.hand_value)

if dealer.hand[0].value.value == 'ace':
    command = input("Would you like insurance? [Yes:y, No:n]")
# Write out condition where player can insure upto half their bet if the dealer has blackjack

while player.hand_value < 1000000:
    command = input("What would you like to do? [Hit:h, Stay:s, Double:d, Split:ss] ")


    # Player has blackjack and is paid 3/2 their bet
    if player.hand_value == 21:
        print(f"{player.name} hit blackjack")
        break
        # player.reset_hand()

    # Player cards value above 21 losing their bet
    if player.hand_value > 21:
        print(f"{player.name} you busted at {player.hand_value}")
        # next_hand()
        break

    # Player receives another card
    if command.lower() == 'h':
        game.hit(player)
        print(player.get_hand(), player.hand_value)

    # Player receives another card without the option to Hit again and doubling their initial bet
    # if command.lower() == 'd':
    #     game.double(player)
    #     print(player.get_hand(), player.hand_value)
    #     break

    # Player Stands receiving no new cards
    if command.lower() == 's':
        break
    