from blackjack.BlackJackPlayer import *

def run_blackjack():
    
    print("\n\n\nWelcome to Black Jack")
    #prints the player options and gets input
    options()
    choice = get_input(5)
    #only runs the game if input is lower than 5
    while choice < 5:
        # creates a deck and converts it to a list
        deck = list(CreateDeck().keys())
        # creates each aplayer object
        player1 = player(1)
        player2 = player(2)
        player3 = player(3)
        player4 = player(4)
        # puts all the players into a list
        player_list = [player1, player2, player3, player4]
        # creates dealer object
        dealer = player(0, True)

        # gives the dealer one randome card and removes it from the deck
        deck = dealer.add_cards(1, deck)
        # prints the card
        dealer.print_cards()
        # gives the dealer one randome card and removes it from the deck
        deck = dealer.add_cards(1, deck)
        print("The dealer's other card is hidden.")

        # if the dealer's cards are lower than 17, keep giving it another card
        # unitl the dealer's points are over 16
        while dealer.points <= 16:
            if dealer.points <= 16:
                deck = dealer.add_cards(1, deck)

        #loop throught the number of players that are playing
        for x in range(choice):
            # give the player 2 random cards and remove them from the deck
            deck = player_list[x].add_cards(2, deck)
            # print out the player name
            print("\n\nPlayer %d: " %(player_list[x].player_id))
            # print out the player cards
            player_list[x].print_cards()
            # start the player's game
            deck = player_list[x].play_game(deck)
            # see if the player won
            player_list[x].did_win(dealer)

        #print the dealer's cards
        dealer.print_cards()
        # see if the dealer bust or got black Jack
        dealer.dealer_endgame()
        # loop through the player and print if the players who won or lost
        print("\nPlayers who won or lost: ")
        for x in range(choice):
            player_list[x].player_endgame()
        
        # wait for the user to press enter
        press_enter()

        # print options and get user input
        print("\n\nTo play again please select the player amount: \n")
        options()
        choice = get_input(5)

if __name__ == "__main__":
    run_blackjack()
