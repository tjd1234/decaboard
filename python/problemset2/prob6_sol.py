# prob6.py

#
# Problem 6
#
# Combine problems 5 and 6 so that the squares both rotate at a rate that
# depends additively on the column number, and the angle depends additively on
# the row number.
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    return (20 + col) * (elapsed_seconds + row)

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
