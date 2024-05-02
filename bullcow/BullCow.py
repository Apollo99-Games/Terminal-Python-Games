from bullcow.Word_list import *
from bullcow.BullCow_utils import *
import random

def run_bullcow():
    DebugMode = True
    #get all the vaildWords and put them in a list
    VaildWords = GetVaildWords(word_list)
    #prints the rules
    print_rules()
    #gets the players choice  
    choice = get_input()
    #if the choice is 1 run the game otherwise don't
    while choice != "1":
        #pick a random word from the VaildWords list
        hidden_word = random.choice(VaildWords)
        #set the health of the user according to the lengh of the hidden word
        health = (len(hidden_word)*2) -1
        #if the health is greater or equals to 1 continue the game
        while health >= 1:
            #print the game menu 
            game_menu(hidden_word, health, DebugMode)
            #get the players guess
            guess = get_guess()
            #Process the Guess to see if it is right 
            # and return the value of health, which will depend if the player
            #gets the rightor wronge answer
            health = ProcessGuess(hidden_word, guess, health)
        #get the user inout to see if they would like to continue playing
        print_rules()
        choice = get_input()


if __name__ == "__main__":
    run_bullcow()
        
