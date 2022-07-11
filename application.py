from click import command
from objects.deck import Deck
from objects.player import Player
from objects.dealer import Dealer

def next_hand():
    replay = input("Would you like to play again? [Yes:y, No:n]")
    if replay.lower() == "y":
        player.reset_hand()
        dealer.reset_hand()
        newGame()
    elif replay.lower() == "n":
        return

number_of_decks = input("How many decks would you like to play with?")
game = Deck()
game.shuffle()
# print(len(game.cards))



player_name = input("Lets play blackjack tell me your name! ")
player_balance = input(f"How much are we sitting at the table with today? $")
player = Player(player_name, int(player_balance))
dealer = Dealer()


def newGame():

    bet = int(input(f"\nHow much would you like to bet? $"))
    player.main_bet(bet=bet)

    for i in range(0,2):
        game.deal(dealer)
        game.deal(player)

    print (f"{dealer.hidden_card()}")
    print(player.get_hand(), player.hand_value)

    if dealer.hand[0].value.value == 'ace':
        command = input("Would you like insurance? [Yes:y, No:n]")
    # Write out condition where player can insure upto half their bet if the dealer has blackjack

    while player.hand_value < 1000000:

        # Player has blackjack and is paid 3/2 their bet
        if player.hand_value == 21:
            print(f"{player.name} hit blackjack")
            player.hand_blackJack()
            print(f"your new balance is {player.balance}")
            break
            # player.reset_hand()

        # Player cards value above 21 losing their bet
        if player.hand_value > 21:
            print(f"{player.name} you busted at {player.hand_value}")
            player.status = 'Bust'
            player.hand_lose()
            print(f"your new balance is {player.balance}")
            # next_hand()
            break

        command = input("What would you like to do? [Hit:h, Stay:s, Double:d, Split:ss] ")

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

    while dealer.hand_value < 5000:
        
        if dealer.hand_value > 21:
            print(f"Dealer BUST")
            dealer.status = 'Bust'
            player.hand_won()
            break
        
        if dealer.hand_value < 17:
            game.hit(dealer)
            print(dealer.get_hand(), dealer.hand_value)
        
        if dealer.hand_value >= 17:
            break

    if player.status == 'In-Play' and dealer.status == 'In-Play':
        if(player.hand_value == dealer.hand_value):
            print(f"{player.name} your hand Pushed!")
            player.hand_push()
            print(f"your new balance is {player.balance}")
        elif(player.hand_value > dealer.hand_value):
            print(f"{player.name} your hand Won!")
            player.hand_won()
            print(f"your new balance is {player.balance}")
        else:
            print(f"{player.name} your hand Lost! Dealer hand: {dealer.hand_value}")
            player.hand_lose()
            print(f"your new balance is {player.balance}")
        pass

    next_hand()

newGame()

        
    