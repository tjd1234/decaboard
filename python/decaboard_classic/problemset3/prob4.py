# prob4.py

#
# Problem 4
#

import decaboard

def step(edge, x):
    if x < edge:
        return 0
    else:
        return 1

def angleIt(row, col, elapsed_seconds):
    return 45 * step(col, row)

#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)
