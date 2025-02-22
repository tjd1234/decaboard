# prob6.py

#
# Problem 6
#
# Rotate 34 degrees clockwise in column 0, column 2, ..., column 8 (all the
# even-numbered columns).
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    if col % 2 == 0:
        return 34

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
