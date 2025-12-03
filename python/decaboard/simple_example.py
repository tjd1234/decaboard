# simple_example.py

import decaboard 

def angleIt(row, col, elapsed_time):
    return row * 10 + elapsed_time * 30

decaboard.run_board_simple(angleIt)
