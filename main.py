from utils import*
from blackjack.BlackJack import run_blackjack
from bullcow.BullCow import run_bullcow
from missonX.missonX import run_missionX
from snakes.snakes import run_snakes

# ===========================================================================
 #Title: Game Table
 #Description: This program ...
# ===========================================================================



choice = 0
#only runs the program if player's choice is less than 5
while choice < 5:
    print("\n\n\nWelcome to game table here are the games you can play.")
    print("1. Bull and Cows - A word guessing game")
    print("2. Blackjack - A card game")
    print("3. Mission X - A math game")
    print("4. Snake game - A classic")
    print("5. Quit")
    #gets input and checks if it's vaild 
    choice = get_input(5)
    print("\n\n\n")
    #each if statement will start a different game, 
    #depending on the user input
    if choice == 1:
        run_bullcow()
    elif choice == 2:
        run_blackjack() 
    elif choice == 3:
        run_missionX()
    elif choice == 4:
        run_snakes()

