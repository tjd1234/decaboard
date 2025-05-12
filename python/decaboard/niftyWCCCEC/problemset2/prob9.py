# prob9.py

#
# Problem 9
#
# ...
#

import decaboard

def angleIt(row, col, elapsed_seconds):
    if row == 4:
        elapsed_mills = int(1000 * elapsed_seconds) % 1000
        # Check if we're in the correct 100ms window for this column
        if col == elapsed_mills // 100:
            return 45
        
        # elapsed_mills = int(1000 * elapsed_seconds) % 1000
        # if elapsed_mills <= 100 and col == 0:
        #     return 45
        # elif 100 < elapsed_mills <= 200 and col == 1:
        #     return 45
        # elif 200 < elapsed_mills <= 300 and col == 2:
        #     return 45
        # elif 300 < elapsed_mills <= 400 and col == 3:
        #     return 45
        # elif 400 < elapsed_mills <= 500 and col == 4:
        #     return 45
        # elif 500 < elapsed_mills <= 600 and col == 5:
        #     return 45
        # elif 600 < elapsed_mills <= 700 and col == 6:
        #     return 45
        # elif 700 < elapsed_mills <= 800 and col == 7:
        #     return 45
        # elif 800 < elapsed_mills <= 900 and col == 8:
        #     return 45
        # elif 900 < elapsed_mills <= 1000 and col == 9:
        #     return 45
        
#
# (1400, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)
