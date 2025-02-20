# prob3.py

#
# Problem 3
#
# Make the inner 2x2 set of four squares rotate clockwise. Also, make the four
# corner squares rotate counterclockwise at twice the rate of the inner squares.
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    if 4 <= row <= 5 and 4 <= col <= 5:
        return 20 * elapsed_seconds
    elif row in [0, 9] and col in [0, 9]:
        return -40 * elapsed_seconds

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
