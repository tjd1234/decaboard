# prob1.py

#
# Problem 1
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    return 10 * abs(row - col)

#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)
