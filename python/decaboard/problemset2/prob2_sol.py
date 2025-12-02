# prob2_sol.py

#
# Problem 2
#
# Make all the squares in the first five columns rotate clockwise, and all the
# squares in the last five columns rotate counterclockwise.
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    if col < 5:
        return 20 * elapsed_seconds
    else:
        return -20 * elapsed_seconds

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board_simple(angleIt, 1400, 200)
