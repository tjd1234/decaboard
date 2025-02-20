# prob3.py

#
# Problem 3
#
# Make all the tiles rotate in the row-wise pattern shown. 
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    return 20 * (elapsed_seconds + row * col)

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
