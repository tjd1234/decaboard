# prob2.py

#
# Problem 2
#

import decaboard
import math

def angleIt(row, col, elapsed_seconds):
    return 45 * math.sin(elapsed_seconds)

#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)
