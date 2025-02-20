# prob4.py

#
# Problem 4
#
# Make each square rotate clockwise at an angle that depends additively its row
# number.
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    return 20  * (elapsed_seconds + row)

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
