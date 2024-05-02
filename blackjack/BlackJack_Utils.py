def get_input(max):
    valid_input = False
    # keep on running until user puts in vaild input
    while valid_input == False:
        # try to get input as int, if can't return error
        try:
            # gets user input as a int
            user_input = int(input("Please enter your choice: "))
            # checks if it is in a certain range, else prints error
            if user_input <= max and user_input >= 1:
                return user_input
            else:
                print("Invaild Input")
        except:
            print("Invaild Input")

def press_enter():
    """() -> NoneType
    lets user continue the game by pressing the 'enter' key 
    """
    print("Press enter to continue")
    # ask for input, forces user to press enter, but anything typed in
    # is not stored anywhere
    input()

def options():
    """ () -> Nonetype
    Prints which game mode the user would like to play
    """
    print("1. For single player")
    print("2. For two players")
    print("3. For three players")
    print("4. For four players")
    print("5. to exit")

def card_formate(value, suit, card):

    """ (str)(str)(lst) -> (lst)
    Creates a visual representation of a standard playing card
    
    """
    #put the card value and suit in the card visual 
    # and put all that into the "card" list
    card[0] +=  '┌───────┐     '
    card[1] += f'| {value.strip():<2}    |     '
    card[2] +=  '|       |     '
    card[3] += f'|   {suit}   |     '
    card[4] +=  '|       |     '
    card[5] += f'|    {value.strip():>2} |     '
    card[6] +=  '└───────┘     '

    return card


def CreateDeck():
    """ () -> (dict) 
    Creates a dictionary of cards, resembling a deck of 52 playing cards
    Assigning a value between 1-11 to 52 different suits.
   
    """
    suit_list = ["  ♥", "  ♦", "  ♣", "  ♠"]
    Court_cards = ["J", "K", "Q"]
    deck = {}

    #loops through, creating the noraml cards and the Ace cards
    #also gives them their value
    for card in range(1, 11):
        for suit in suit_list:
            #if the card is 1 it is a Ace so the "1" is replaced with A
            #and the default value is set to 11
            #for the other cards their vaule is just their card number
            if card == 1:
                deck["A" + suit] = 11
            else:
                deck[str(card) + suit] = card
    #loops through, creating the Court cards
    #also gives them their value
    for suit in suit_list:
        for card in Court_cards:
            #gives all Court cards a value of 10
            deck[card + suit] = 10

    return deck