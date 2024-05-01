# Terminal-Python-Games
4 Games made in Python that can be played in the terminal: Blackjack, Bulls and Cows (word guessing game), missionX (math game), and the classic Snake game.

The instructions to play the games are printed when you run the code. The code can be run from the "main.py" file.

You can run the games on Replit.

Note the curses library appears to detect keys differently on different compilers. You can switch between these two options to see what works for you:
```python
# location is in snakes -> snakes_utils -> after line 6

# works on VS code
RIGHT_KEY = 454
LEFT_KEY = 452
DOWN_KEY = 456
UP_KEY = 450

# works on replit
RIGHT_KEY = curses.KEY_RIGHT
LEFT_KEY = curses.KEY_LEFT
DOWN_KEY = curses.KEY_DOWN
UP_KEY = curses.KEY_UP

```

##Some screenshots of the program:

