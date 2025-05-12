# prob8.py

#
# Problem 8
#

import decaboard

def clamp(low, high, x):
    if x < low:
        return low
    elif x > high:
        return high
    else:
        return x

def smoothstep(low, high, x):
    # scale x to the range [0, 1]
    x = clamp(0, 1, (x - low) / (high - low))
    return x * x * (3.0 - 2.0 * x)

def angleIt(row, col, elapsed_seconds):
    return 20 * smoothstep(2, 5, row)

#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)
