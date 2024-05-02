# Terminal-Python-Games
4 Games made in Python that can be played in the terminal: Blackjack, Bulls and Cows (word guessing game), missionX (math game), and the classic Snake game.

The instructions to play the games are printed when you run the code. The code can be run from the "main.py" file.

You can run the games on [Replit](https://replit.com/@WahhajKhan/Terminal-Games-in-Python?v=1).

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

## Some screenshots of the program:

Snake Game

![snake game](https://github.com/Apollo99-Games/Terminal-Python-Games/assets/163193765/e55a3d0b-916a-45e9-8e59-f1de9777d231)

Blackjack

![blackjack](https://github.com/Apollo99-Games/Terminal-Python-Games/assets/163193765/b01db311-3f4b-48ca-8558-b3b6af2bef89)


