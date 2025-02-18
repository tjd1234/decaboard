# prob4.py

#
# Problem 4
#
# Rotate 34 degrees clockwise just the square in row 4, column 1.
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    if row == 4 and col == 1:
        return 34

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
