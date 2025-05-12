# example.py

import decaboard_plus
import math

def dist(a, b, x, y):
    return math.sqrt((x - a) ** 2 + (y - b) ** 2)

def set_square(row, col, elapsed_seconds, mouseX, mouseY):
    ec = (255, 0, 0)
    cell_x, cell_y = decaboard_plus.center_of_cell(row, col)
    return {
        'angle': math.degrees(math.atan2(mouseY - cell_y, mouseX - cell_x)),
        "fill_color": (255, int(mouseX / 2), int(mouseY / 2)),
        "edge_color": ec,
        "edge_width": 1 + min(row, col),
        "dx": -math.sin(elapsed_seconds) * 10,
        "dy": -math.cos(elapsed_seconds) * 10,
        "size": 10 + (elapsed_seconds % 100)
    }

#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard_plus.run_board(set_square, 1200, 200)
