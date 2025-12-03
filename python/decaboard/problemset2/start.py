# start.py

#
# The angleIt function returns a number that is the angle to rotate the square.
#

import decaboard
import math

def dist(a, b, x, y):
    """
    Return the distance between the point (a, b) and the point (x, y).
    """
    return ((a - x) ** 2 + (b - y) ** 2) ** 0.5

def angleIt(row, col, elapsed_seconds):
    if row == 4:
        elapsed_mills = int(1000 * elapsed_seconds) % 1000
        if col == elapsed_mills // 100:
            return 45

#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board_simple(angleIt, 1200, 200)
