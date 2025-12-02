# probChallenge1.py

#
# Problem Challenge 1
#
# Make all the tiles rotate in the row-wise pattern shown. 
# 
# Notice that the top row does not rotate at all, the second row rotates a
# little, the third row rotates a little bit faster, and so on down to the
# bottom row which rotates the fastest.
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    return 20 * elapsed_seconds * row

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
