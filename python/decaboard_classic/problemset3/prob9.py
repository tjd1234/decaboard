# prob9.py

#
# Problem 9
#

import decaboard
import math

def lerp(x, y, t):
    return (1 - t) * x + t * y

def angleIt(row, col, elapsed_seconds):
    return 20 * lerp(row, col, abs(math.sin(elapsed_seconds)))

#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)
