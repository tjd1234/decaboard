# example.py

import decaboard
import math

def angleIt(row, col, elapsed_seconds):
    return 30 * math.sin((row + col) * elapsed_seconds)

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
