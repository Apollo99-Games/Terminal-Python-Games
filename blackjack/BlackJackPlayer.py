from blackjack.BlackJack_Utils import*
import random


class player:
    def __init__(self, player_id = 0, dealer = False) -> None:
        """(self, int, bool) 
        Creates a class of 'self' which can be a player or dealer and creates
        player deck, and sets everything to 0 or false.
        """
        #initialize player variables 
        self.deck_def = CreateDeck()
        self.cards = []
        self.points = 0
        self.ace = 0
        self.dealer = dealer
        self.won = "False"
        self.in_game = False
        self.player_id = player_id

    def calcu_points(self, card):
        """(self, lst) -> (NoneType)
        Calculates how many points the user/player has, according to the cards the 'self' has
        Deals with Ace cards, making them a seperate variable. 
        """
        #get the value of the card from the deck and add it to points
        self.points += self.deck_def[card]
        #if the card is an Ace, add a Ace to the player's Ace variable
        if card[0] == "A":
            self.ace += 1
        #if the points are greater than 21 
        #and the player's has one or more Aces  
        #subtract the points by 10 and remove one Ace from the player's Ace
        # variable 
        if self.points > 21 and self.ace > 0:
            self.ace -= 1
            self.points -= 10

    def add_cards(self, num, deck):
        """(self, int, lst) -> (dict) 
        Adds cards to the players deck and calculates players points after 
        adding or removing cards
        """
        #repeat this num times
        for x in range(num):
            #pick a random card from the deck
            card = random.choice(deck)
            #add the card to the player's card list
            self.cards.append(card)
            # remove the card from the deck
            deck.remove(card)
            # calculate the player's points after the card is added
            self.calcu_points(card)
        return deck

    def print_cards(self):
        """(self) -> (NoneType)
        If the player is not the dealer it prints out the visuals of the cards in
        your deck and prints dealer and player's points.
        
        """
        if self.dealer == False:
            print("Your cards are: ")
        else:
            print("\n\nDealer's cards are: ")
        # initialize the list that will hold the card visuals
        visual = ["", "", "", "", "", "", ""]
        #loop through, adding each of the players card to the visual list
        for card in self.cards:
            visual = card_formate(card[:2], card[-1], visual)
        #printing the visual cards
        for row in visual:
            print(row)
        if self.dealer == False:
            print("Your total points: %d" % (self.points))
        else:
            print("Dealer's points are: %d." % (self.points))
# ///////////////// Ask her tmrw how to do sample call 
    def player_bust(self):
        """(self) -> (bool)
        Checks is player has Won or Bust(lost) if the player has 21 points they win, 
        if they have more they loose.
        """
        #if points equal 21, tell the player they won and set self.won to true
        if self.points == 21:
            print("You Won!")
            self.won = "True"
            press_enter()
            return True
        #if the points go over 21, tell the player they lost and set self.won
        #to false
        elif self.points > 21:
            print("Your cards are above 21. BUST ... You're out")
            self.won = "False"
            press_enter()
            return True
        #if all else false, return false
        else:
            return False

    def play_game(self, deck):
        """(self) -> (dict)
        Starts the game and runs, unless the users point are 21 or over 21
        then program quits 
        """
        # puts the player in the match
        self.in_game = True
        choice = 0
        BustOrWin = False
        #only runs this if points are lower than 21
        #otherwise see if the player bust or won
        if self.points < 21: 
            #keeps one running this until the player choses option 2, or
            # the player wins or busts
            while choice < 2 and BustOrWin == False:
                print("1. To hit")
                print("2. To Stand")
                # get valid player input
                choice = get_input(2)
                #if player picks hit
                if choice == 1:
                    #give the player a random card
                    deck = self.add_cards(1, deck)
                    #print the player's cards
                    self.print_cards()
                    #see if the player bust or won
                    BustOrWin = self.player_bust()
        else:
            self.player_bust()
        return deck

    def did_win(self, dealer):
        """(self, ?) -> (bool)
        Checks if player has won, tied or lost against the dealer 
        """
        #only run this is the player's points are under 21
        if self.points < 21:
            #if player's points equal the dealer, it's a tie
            if self.points == dealer.points:
                self.won = "Tie"
            #otherwise if player's points are greater than the dealer
            #player wins
            elif self.points > dealer.points:
                self.won = "True"
            # if the drealer goes bust the player wins
            elif dealer.points > 21:
                self.won = "True"

    def dealer_endgame(self):
        """(self) -> NoneType
        Runs if dealer has won, lost or tied with any players 
        Prints out the outcomes and finishes the round 
        """
        #if dealer got a black Jack
        if self.points == 21:
            print("\nThe dealer got a Black Jack")
            print("All remaining players have lost.")
        # The dealer has bust
        elif self.points > 21:
            print("\nThe dealer has Bust.")
            print("All remaining players have won too.")
        # the dealer's point's are under 21
        elif self.points < 21:
            print("\nThe players who scored higher than the dealer")
            print("have won, but those who scored lower have lost\n")

    def player_endgame(self):
        """(self) -> NoneType
        Runs if player(s) has won, lost or tied with the dealer
        Prints the winning, losing and tied message along with
        which player(s) have won or lost. 
        """
        # only runs if the player is in game
        if self.in_game == True:
            # if player won tell them they won
            if self.won == "True":
                print("Player %d has won" % (self.player_id))
            # if the player tied with the dealer 
            # tell them they that it was a "push"
            elif self.won == "Tie":
                print("Push: the dealer and player %d have tied"
                %(self.player_id))
            #otherwise the player has lost
            else:
                print("Player %d has lost" %(self.player_id))
