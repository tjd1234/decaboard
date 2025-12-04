# simple_example.py

#
# With the decaboard.run_board_simple function, you pass it with a function that
# takes (row, col, elapsed_time) and returns a float (the angle of the square in
# degrees).
#

import decaboard 

def angleIt(row, col, elapsed_time):
    return row * 10 + elapsed_time * 30

decaboard.run_board_simple(angleIt)
