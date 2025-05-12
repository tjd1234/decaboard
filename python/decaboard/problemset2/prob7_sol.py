# prob7.py

#
# Problem 7
#
# Make all the squares rotate smoothly back and forth, i.e. they rotate
# clockwise a little bit, slow down and top, and then rotate counterclockwise,
# slow down and stop, and so on.
#

import decaboard
import math

def angleIt(row, col, elapsed_seconds):
    return math.sin(elapsed_seconds) * 20

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
