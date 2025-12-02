# intro_example.py

import decaboard
import math


def dist(a, b, x, y):
    return math.sqrt((x - a) ** 2 + (y - b) ** 2)


def set_square(row, col, elapsed_time, mouse_x, mouse_y):
    cell_x, cell_y = decaboard.center_of_cell(row, col)

    return {
        "angle": math.degrees(math.atan2(mouse_y - cell_y, mouse_x - cell_x)),
        "size": 10 + (elapsed_time % 100),
    }


#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(set_square, 1200, 200)
