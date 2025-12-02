# prob7.py

#
# Problem 7
#

import decaboard

def clamp(low, high, x):
    if x < low:
        return low
    elif x > high:
        return high
    else:
        return x

def angleIt(row, col, elapsed_seconds):
    return 20 * clamp(3, 5, row * col)
#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)
