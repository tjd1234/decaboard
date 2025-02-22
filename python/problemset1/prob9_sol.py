# prob9.py

#
# Problem 9
#
# Rotate 34 degrees clockwise all the squares not on the main left-to-right
# diagonal.
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    if row != col:
        return 34

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
