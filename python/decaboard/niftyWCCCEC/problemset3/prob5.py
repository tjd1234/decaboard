# prob5.py

#
# Problem 5
#

import decaboard
import math
def step(edge, x):
    if x < edge:
        return 0
    else:
        return 1

def angleIt(row, col, elapsed_seconds):
    if step(3, row) == 1 and step(5, col) == 1:
        return 45 * math.sin(elapsed_seconds)

#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)
