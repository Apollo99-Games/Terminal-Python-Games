import random

def get_num_input():
    valid_input = False
    #keep on running until user puts in vaild input
    while valid_input == False:
        #try to get input as int, if can't return error
        try:
            user_input = int(input())
            return user_input
        except:
            print("Invaild Input. Try Again!")

def get_input(max):
    valid_input = False
    #keep on running until user puts in vaild input
    while valid_input == False:
        #try to get input as int, if can't return error
        try:
            #gets user input as a int
            user_input = int(input("Please enter your choice: "))
            #checks if it is in a certain range, else prints error
            if user_input <= max and user_input >= 1:
                return user_input
            else:
                print("Invaild Input")
        except:
            print("Invaild Input")

def press_enter():
    print("Press enter to continue")
    #ask for input, forces user to press enter, but anything typed in
    #is not stored anywhere
    input()

def print_menu():
    """() -> Nonetype 
    Prints the menu for the game 
    """
    print("\n\n\nWelcome to missionX")
    print("Your a CIA agent trying to break onto a stronghold")
    print("You must enter a three digit password")
    print("The three digits add up to and mutiply to specific numbers")
    print("\nPick your game mode: ")
    print("1. Normal - 5 levels of diffuclty and infinite lives")
    print("2. Hardcore - infinite levels of diffuclty, but only have 5 lives")
    print("3. Quit")

def get_code(Difficulty):
    """() -> (int, int)
    Returns the code based on the difficulty level, Normal or Hardcore.
    """
    #picks 3 random numbers from 1 to the value Difficulty added 3 times
    a = random.randint(1, Difficulty + Difficulty + Difficulty)
    b = random.randint(1, Difficulty + Difficulty + Difficulty)
    c = random.randint(1, Difficulty + Difficulty + Difficulty)
    #adds the numbers and multiplies the numbers
    sum = a + b + c
    product = a * b * c
    print(a, b, c) #debug line////////////////////(remove in final version)
    return sum, product

def game_menu(sum, product, Difficulty, lives = 0):
    """ (int, int, int, int) -> (NoneType)
    Tells the user the difficulty level, the password threy have to guess and, 
    how many lives they have. 
    """
    #prints the level you are on
    print("\nYour in a stronghold with a level %d security system" 
    %(Difficulty))
    print("The passcode to by pass the system has 3 numbers")
    #prints the sum and product of the passcode
    print("They add up to %d and multiply to %d." % (sum, product))
    #if hardcore mode is enabled you will have lives, and will print them
    #if they are above 0
    if lives > 0:
        #prints out lives
        print("You have %d lives left." % (lives))
    print("Please enter the three digits: ")

def player_code():
    """
    (int, int, int) -> (int, int)
    Processes the user's guess to the password and returns the sum and 
    product of theose 3 numbers.  
     
    """
    #gets the player's guess of the 3 numbers for the passcode
    print("\nNumber 1: ")
    a = get_num_input()
    print("Number 2: ")
    b = get_num_input()
    print("Number 3: ")
    c = get_num_input()
    #adds the numbers and multiplies the numbers
    player_sum = a + b + c
    player_product = a * b * c

    return player_sum, player_product





