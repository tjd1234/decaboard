# demo_sol.py

import decaboard
import math

def angleIt(row, col, elapsed_seconds):
    if (row + col) % 2 == 0:
        return 25 * math.sin(elapsed_seconds)
    else:
        return -50 * math.sin(elapsed_seconds)

# def angleIt(row, col, elapsed_seconds):
#     return 25 * abs(math.sin(elapsed_seconds))

# def angleIt(row, col, elapsed_seconds):
#     return 25 * math.sin(elapsed_seconds)

# def angleIt(row, col, elapsed_seconds):
#     if col == 7:
#         return 25 * elapsed_seconds

# def angleIt(row, col, elapsed_seconds):
#     if row == 4 or col == 7:
#         return 25 * elapsed_seconds

# def angleIt(row, col, elapsed_seconds):
#     if row == 4 and col == 7:
#         return 25 * elapsed_seconds

# def angleIt(row, col, elapsed_seconds):
#     return 25 * elapsed_seconds

# def angleIt(row, col, elapsed_seconds):
#     return 5 * (row + col)

# def angleIt(row, col, elapsed_seconds):
#     return 5 * row

# def angleIt(row, col, elapsed_seconds):
#     return 34

decaboard.run_board(angleIt, 1200, 200)
