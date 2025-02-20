# prob5.py

#
# Problem 5
#
# Make each square rotate clockwise at a rate that depends additively on its
# column number.
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    return (20 + col) * elapsed_seconds

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
