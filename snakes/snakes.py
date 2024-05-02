from snakes.snakes_utils import*

def run_snakes():
    #prints menu
    print_menu()
    #gets input
    choice = get_input(2)

    #if the input is less than two kepp playing the game
    while choice < 2:

        #create the display
        window = set_display()

        #create the snake by inputing its starting cords
        snake = [(4, 4), (4, 3), (4, 2)]
        #drawing an apple at a random position 
        apple = draw_new_apple(window, snake)

        #initiating the score to 0 and the default arrow key
        score = 0
        key = RIGHT_KEY

        #keep on running game until player presses escape
        while key != ESC:
            #print Score and "Snakes! - A Classic" on top of screen
            window.addstr(0, 2, "Score %d " % score)
            window.addstr(0, 17, "Snakes! - A Classic")
            #sets the frame rate of the display 
            #gets faster everytime your snake grows larger
            window.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120)
            #gets the arrow key the player pressed
            key = get_arrow_key(window, key)

            #takes the arrow key and sees which one is pressed
            #then returns the snakes next cords depending on the key type
            y, x = process_keys(key, snake)

            #inserts the new cords of the snake at the front of the snake
            snake.insert(0, (y, x)) 

            #checks to see if snake hits anything, if so end game
            if collision(snake) == True:
                break
            
            #checks if snake head touches apple cord
            if snake[0] == apple:
                #increase score by one
                score += 1
                #draw a new apple 
                apple = draw_new_apple(window, snake)
            else:
                #otherwise remove the end of the snake
                draw_snake(window, snake, False)
            #draw the front of the snake
            draw_snake(window, snake)

        #close the window
        curses.endwin()
        print("\n\nYou lose!")
        #print score
        print("Final score: %d" %(score))
        #wait for player to press enter
        press_enter()
        
        #print menu and get input
        print_menu()
        choice = get_input(2)

if __name__ == "__main__":
    run_snakes()
