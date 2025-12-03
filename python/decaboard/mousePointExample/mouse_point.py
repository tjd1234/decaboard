# mouse_point.py

import decaboard
import math


def set_square(row, col, elapsed_time, mouse_x, mouse_y):
    center_x, center_y = decaboard.center_of_cell(row, col)

    return {
        #
        # atan2 is like the regular atan (arctangent) function, but it takes the
        # y-coordinate and x-coordinate of the other point, and works correctly
        # in any quadrant (and also when x is 0)
        "angle": math.degrees(math.atan2(mouse_y - center_y, mouse_x - center_x)),
        #
        # for fun, the size of the square depends on the distance between it and the mouse
        "size": math.dist((mouse_x, mouse_y), (center_x, center_y)) / 5,
    }


#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(set_square, 1200, 200)
