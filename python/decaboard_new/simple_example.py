# simple_example.py

from decaboard import run_board_simple

def my_simple_pattern(row: int, col: int, elapsed_time: float) -> float:
    return row * 10 + elapsed_time * 30

run_board_simple(my_simple_pattern)
