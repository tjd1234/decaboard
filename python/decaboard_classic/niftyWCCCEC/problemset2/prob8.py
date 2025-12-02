# prob8.py

#
# Problem 8
#
# ...
#

import decaboard

def dist(a, b, x, y):
    """
    Return the distance between the point (a, b) and the point (x, y).
    """
    return ((a - x) ** 2 + (b - y) ** 2) ** 0.5

def angleIt(row, col, elapsed_seconds):
    return dist(row, col, 4, 4) * elapsed_seconds

#
# (1400, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)
