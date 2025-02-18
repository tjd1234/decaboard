# user.py

import decaboard
import math

def angleIt(row, col, elapsed_seconds):
    return 30 * math.sin((row + col) * elapsed_seconds)
    
decaboard.run_board(angleIt)
