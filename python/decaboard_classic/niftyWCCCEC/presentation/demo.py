# demo.py

import decaboard
import math

def angleIt(row, col, elapsed_seconds):
    return 25 * abs(math.sin(elapsed_seconds))

decaboard.run_board(angleIt, 1200, 200)
