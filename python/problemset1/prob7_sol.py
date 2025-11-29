# prob7.py

#
# Problem 7
#
# Rotate 34 degrees clockwise all the squares in the 4 x 5 rectangle of squares
# whose upper-left square is column 5, row 3, and whose lower-right square is
# column 8, row 7.
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    if 5 <= col <= 8 and 3 <= row <= 7:
        return 34

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
