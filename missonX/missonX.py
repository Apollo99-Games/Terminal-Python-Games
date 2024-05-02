from missonX.missonX_utils import*


def run_missionX():
    """ () -> (Nonetype) 
    Runs the game so long as the user's input is not 3  
    """
    choice = 0
    # runs the code only if choice is lower than 3
    while choice < 3:
        # prints menu and gets user input
        print_menu()
        choice = get_input(3)
        # initializes the difficulty to 1
        Difficulty = 1
        # if the user choses 1, run the normal gamemode
        if choice == 1:
            # the code keeps running as long as the difficulty is lower
            # or equal the difficulty
            while Difficulty <= 5:
                # get the sum and product of a randomly generated passcode
                sum, product = get_code(Difficulty)
                # print the game menu with the sum and product of the passcode
                # also informing the user which level they are on
                game_menu(sum, product, Difficulty)
                # gets the sum and product of the code that the player guessed
                player_sum, player_product = player_code()
                # if the player guess equal the real code then print that they
                # guessed the right code and increase the difficulty by 1
                # otherwise tell them to try again
                if player_sum == sum and player_product == product:
                    print("You passed the system!")
                    Difficulty += 1
                else:
                    print("Wronge password try again!")
                # wait for the user to press enter
                press_enter()
            # once the loop ends tell the user that they have won
            print("Congratulations you passed all 5 levels!")
            # wait for the user to press enter
            press_enter()
        # if the user choses 2, run the hardcore gamemode
        elif choice == 2:
            # set lives to 5
            lives = 5
            # keep on runnning the game
            # as long as the user has more lives than
            while lives > 0:
                # get the sum and product of a randomly generated passcode
                sum, product = get_code(Difficulty)
                # print the game menu with the sum and product of the passcode
                # also informing the user which level they are on
                game_menu(sum, product, Difficulty, lives)
                # gets the sum and product of the code that the player guessed
                player_sum, player_product = player_code()
                # if the player guess equal the real code then print that they
                # guessed the right code and increase the difficulty by 1
                # otherwise tell them to try again and remove 1 life
                if player_sum == sum and player_product == product:
                    print("You passed the system!")
                    Difficulty += 1
                else:
                    print("Wronge password try again!")
                    lives -= 1
                    print("You have %d lives left." % (lives))
                # wait for the user to press enter
                press_enter()
            # tell the user they are out of lives
            # and print he level of difficulty they got to as their score
            print("You ran out of lives.")
            print("Your score was %d" % (Difficulty))
            # wait for the user to press enter
            press_enter()


if __name__ == "__main__":
    run_missionX()
