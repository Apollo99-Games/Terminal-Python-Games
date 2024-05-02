import curses
import random

# initializes the keyboard keys the program will use
ESC = 27

# works on VS code
RIGHT_KEY = 454
LEFT_KEY = 452
DOWN_KEY = 456
UP_KEY = 450

# works on replit
# RIGHT_KEY = curses.KEY_RIGHT
# LEFT_KEY = curses.KEY_LEFT
# DOWN_KEY = curses.KEY_DOWN
# UP_KEY = curses.KEY_UP


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
    print("Press enter to continue")
    # ask for input, forces user to press enter, but anything typed in
    # is not stored anywhere
    input()


def print_menu():
    """() -> NoneType
    Prints menu for game
    """
    print("\n\n\nWelcome to Snakes.")
    print("Your goal is to eat as many apples as you can!")
    print("Make sure to not hit a wall or yourslef. If you do you're out!")
    print("If you're going in a direction, do not switch to the opposite one")
    print("You you will slither over yourself and lose")
    print("You can hit Esc to exit at anytime")
    print("DISCLAIMER: You need the curses and emoji library to play")
    print("\n Here are your options: ")
    print("1. Play")
    print("2. Quit")


def set_display():
    # sets up curses
    curses.initscr()
    # creates a 15 by 50 display. Its (y, x) in curses
    win = curses.newwin(15, 50, 0, 0)
    # initializes keyboard
    win.keypad(1)
    # disables echo mode for the current display
    curses.noecho()
    # hides cursor
    curses.curs_set(0)
    # draws screen border
    win.border(0)
    win.nodelay(1)
    return win


def get_arrow_key(win, key):

    old_key = key
    try:
        # gets what key the user pressed
        key_pressed = win.getch()
        # -1 here means no input.. so it just checks for if there is any input
        # if there is any key = key_pressed, else key = old_key
        if key_pressed != -1:
            key = key_pressed
        else:
            key = old_key

        # checks if any arrow keys are pressed, if so return key
        # if not just return the right arrow key
        if key not in [RIGHT_KEY, LEFT_KEY, DOWN_KEY, UP_KEY, ESC]:
            return RIGHT_KEY
        else:
            return key
    except:
        return old_key

# need to do assert and testing/////////////////////////////////////
def process_keys(key, snake):
    """ (int, lst) -> (int, int)
    
    
    
    """    
    y = snake[0][0]
    x = snake[0][1]

    # checks which key is pressed and updates cords accordingly
    if key == DOWN_KEY:
        y += 1
    elif key == UP_KEY:
        y -= 1
    elif key == LEFT_KEY:
        x -= 1
    elif key == RIGHT_KEY:
        x += 1

    return y, x

def collision(snake):
    """(lst) -> (bool)
    
    """
    # converts snake's front into seperate x, y cords
    y = snake[0][0]
    x = snake[0][1]

    # check if snake hit the border
    if y == 0:
        return True
    elif y == 15-1:
        return True
    elif x == 0:
        return True
    elif x == 50 - 1:
        return True

    # checks if snake runs over itself
    elif snake[0] in snake[1:]:
        print("bumped")
        return True
    else:
        return False


def draw_new_apple(window, snake):
    # empty's the apple's cords
    apple = ()
    # repeats unitl apple has a new cord
    while apple == ():
        # gives apple a random cord
        apple = (random.randint(1, 15-2), random.randint(1, 50 - 2))
        # checks if the new apple cord is already in the snake, if so
        # erase the apple cords and find a new cord
        if apple in snake:
            apple = ()
    # draw a new apple on the new cord
    window.addch(apple[0], apple[1], '#')
    # return the new apple cords
    return apple


def draw_snake(window, snake, add=True):
    # if add is turn, draw a '@' at the front of the snake
    # else remove a '@' at the back of the snake
    if add == True:
        window.addch(snake[0][0], snake[0][1], '@')
    else:
        last = snake.pop()
        window.addch(last[0], last[1], ' ')
