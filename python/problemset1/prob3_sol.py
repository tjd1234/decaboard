# prob3.py

#
# Problem 3
#
# Make just the squares in the fifth row (row 4) rotated 34 degrees.
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    if row == 4:
        return 34

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
