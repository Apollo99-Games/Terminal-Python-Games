import doctest

def get_guess():
    """() -> NoneType
    Takes in user input, the users guess as to what the hiddenword is.
    """
    while True:
        try:
            choice = input("Please enter your choice ").strip().lower()
            return choice
        except:
            print("Invalid Input. Only letters allowed")

def print_rules():
    """ () -> NoneType
    Prints the rules for the game. 
    """

    print("\n\n\nWelcome to BullCow, a game in which you will guess a \n\
        randomly selected word from a ist of over 250 words!")
    print("You have bulls and cows, which you use as hints to guess what \n\
        your word is")
    print("You get a bull for having the correct letter in the correct place")
    print("For example, if the word is jack and you guess back, you'd \n\
        get 3 bulls")
    print("You get a cow for having the correct letter but in the \n\
        wrong place")
    print("If the word is bee and you guess sea, you'd get 1 cow. ")
    print ("There are no letter that repeat, so there are only Isograms \n\
        meaning no words with 2 repeating letters")
    print ("For example, add, banana, apples, cheese, totally, coconut etc.")
    print("\nPress enter to start the game")
    print("Press 1 to quit game")

def press_enter():
    print("Press enter to continue")
    #ask for input, forces user to press enter, but anything typed in
    #is not stored anywhere
    input()

def game_menu(HiddenWord, Health, DebugMode):
    """(bool,int,int) -> (Nonetype) 
    Tells user how much health they have ie. number of guesses and 
    the length of the word they have to guess. If debugmode is set to true, 
    it will tell the user what the hiddenword is. 
    """
    print("")
    if DebugMode == True:
        print("The hidden word is: %s" % (HiddenWord))  # debug line
    print("You have %d lives" % (Health))
    print("Guess the %d letter word" % (len(HiddenWord)))



def get_input():
    """()-> (Nonetype)
    Starts off the game by asking user their choice, 
    if user enter 1 program quits. 
    """
    # continues to ask for input until the input is a 1 or blank
    while True:
        choice = input("Please enter your choice ").strip()
        if choice in "1 ":
            return choice
        else:
            print("Invalid Input")



def IsIsogram(Word):

    """
    (str) -> (bool)
    Checks to see if a letter is repeated twice in a word, if so return false. 
    otherwise return true.
    >>> IsIsogram("little")
    False
    >>> IsIsogram("big")
    True
    >>> IsIsogram("chicken")
    False
    """
    #loops through the letters word, comparing them
    #if any match each other, then return false, else return true 
    for GuessIndex in range(len(Word)):

        for comparison in range(GuessIndex + 1 ,len(Word)):

            if Word[GuessIndex] == Word[comparison]:
                return False
    return True



def GetBullCow(Guess, HiddenWord):

    """(str, str) -> (int, int)
    Counts how many bulls and how many cows the player has. 

    >>> GetBullCow("bee", "sea")
    (1, 1)
    >>> GetBullCow("jack", "flap")
    (0, 1)
    >>> GetBullCow("jack", "back")
    (3, 0)
    """
    #initialize bulls and cows
    Bulls = 0
    Cows = 0
    #loop through the guess word
    for GuessIndex in range(len(Guess)):
        #if the a letter in the guess word is in the same spot as in the  
        # hidden word then add a bulland skip the rest of the loop
        if Guess[GuessIndex] == HiddenWord[GuessIndex]:
            Bulls += 1
            continue
        #loop through the hiddem word to see if there is a same letter 
        #in the hidden word and the guess word, if so add a cow
        #and end the loop
        for HiddenIndex in range(len(HiddenWord)):
            if Guess[GuessIndex] == HiddenWord[HiddenIndex]:
                Cows += 1
                break
    return Bulls, Cows



def GetVaildWords(WordList):
    """(lst)->(lst)
    Loops over Word_list file and adds words to the list ValidWords which are
    more than 4 letter long and less then 8 and are not Isograms.
    
    >>> GetVaildWords(['cake', 'Buger', 'Water', 'Cream', 'Chips'])
    ['cake', 'Buger', 'Water', 'Cream', 'Chips']
    >>> GetVaildWords(["apples", "bananas", "tree", "potato", "cups"])
    ['cups']
    >>> GetVaildWords(["apples", "bananas", "tree", "potato", "mom"])
    []
    >>> GetVaildWords(["beer", "lollipop", "cubs", "sandy"])
    ['cubs', 'sandy']
    """
    #initialize Valid Words list
    ValidWords = []

    #loop throught the words in the WordList to see there length is in
    #a specifc range and to see if the word is a Isogram
    #if both of thses are ture add the word to the Valid Words list
    for Word in WordList:
        if len(Word) >= 4 and len(Word) <= 8 and IsIsogram(Word):
            ValidWords.append(Word)
    return ValidWords



def ProcessGuess(HiddenWord, Guess, health):

    """(str, str, int,) -> (int)
    Takes in the guess, hiddenword and health of the user 
    and lowers the health of the player everytime they guess incorrectly 

    >>> ProcessGuess("park", "park", 7)
    <BLANKLINE>
    You win!!!
    To play again Press enter to continue
    0
    >>> ProcessGuess("park", "dark", 7)
    <BLANKLINE>
    Incorrect answer.
    You have 6 lives left
    The word has 4 letters
    You have 3 bulls and 0 cows.
    Press enter to continue
    6
    """
    #if the player guesses the right word tell them that they won
    #and return lives as 0
    if HiddenWord == Guess:
        print("\nYou win!!!")
        print("To play again ", end = "")
        press_enter()
        return 0

    #if the player guess is not the dame length as the Hidden Word
    #tell them their guess is not the right number of letters
    #return the original amount of health
    if (len(Guess) != len(HiddenWord)):
        print("\nThe word is %d letters long.\nTry again!"%(len(HiddenWord)))
        press_enter()
        return health

    #if the player guess is not a isogram, let them know and 
    #return the original amount of health
    if IsIsogram(Guess) == False:
        print("\nNo repeating letters, guess again")
        press_enter()
        return health

    #if all the previous is false subract 1 from health
    health -= 1

    #if health is 0, let the player know they lost and print the hidden word
    #otherwise tell them their answer is wronge and print their remaing lives
    #and the length of the word
    if (health <= 0):
        print("\nIncorrect answer.")
        print("You have no lives left.")
        print("The Hidden word was %s" % (HiddenWord))
        press_enter()
        return 0
    else:
        print("\nIncorrect answer.")
        print("You have %d lives left" % (health))
        print("The word has %d letters" % (len(HiddenWord)))
    #print the number of bull cows they have
    Bulls, Cows = GetBullCow(Guess, HiddenWord)
    print("You have %d bulls and %d cows." % (Bulls, Cows))
    press_enter()
    return health

if __name__ == '__main__':
    doctest.testmod()


