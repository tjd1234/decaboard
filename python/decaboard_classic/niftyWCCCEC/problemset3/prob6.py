# prob6.py

#
# Problem 6
#

import decaboard
import math

def in_range(low, high, x):
    """
    Returns 1 if low <= x <= high, and 0 otherwise.
    """
    if low <= x <= high:
        return 1
    else:
        return 0

def angleIt(row, col, elapsed_seconds):
    if in_range(1, 6, row) and in_range(1, 3, col):
        return 45 * math.sin(elapsed_seconds)
#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)
