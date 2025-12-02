# example.py

import decaboard
import math


def set_square(row, col, elapsed_seconds, mouseX, mouseY):
    ec = (255, 0, 0)
    return {
        "angle": 5 * max(row, col) * elapsed_seconds,
        "fill_color": (255, int(mouseX / 2), int(mouseY / 2)),
        "edge_color": ec,
        "edge_width": 1 + min(row, col),
        "dx": -math.sin(elapsed_seconds) * 10,
        "dy": -math.cos(elapsed_seconds) * 10,
        "size": 10 + (elapsed_seconds % 100),
    }


#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(set_square, 1200, 200)
