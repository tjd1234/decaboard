# prob10.py

#
# Problem 10
#
# Rotate 34 degrees clockwise all the squares in a ring as shown.
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    if row == 1 and 0 < col < 9:
        return 34
    if row == 8 and 0 < col < 9:
        return 34
    if col == 1 and 0 < row < 9:
        return 34
    if col == 8 and 0 < row < 9:
        return 34


#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
