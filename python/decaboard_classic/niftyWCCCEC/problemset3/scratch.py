# scratch.py

import decaboard
import math

def step(edge, x):
    """
    Returns 0 if x is less than edge, and 1 if x is greater than, 
    or equal to, edge.
    """
    if x < edge:
        return 0
    else:
        return 1

def in_range(low, high, x):
    """
    Returns 1 if low <= x <= high, and 0 otherwise.
    """
    if low <= x <= high:
        return 1
    else:
        return 0

def clamp(low, high, x):
    if x < low:
        return low
    elif x > high:
        return high
    else:
        return x

# float smoothstep (float edge0, float edge1, float x) {
#    // Scale, and clamp x to 0..1 range
#    x = clamp((x - edge0) / (edge1 - edge0));
#    return x * x * (3.0f - 2.0f * x);
# }

def smoothstep(low, high, x):
    # scale x to the range [0, 1]
    x = clamp(0, 1, (x - low) / (high - low))
    return x * x * (3.0 - 2.0 * x)

# // Precise method, which guarantees v = v1 when t = 1. This method is monotonic only when v0 * v1 < 0.
# // Lerping between same values might not produce the same value
# float lerp(float v0, float v1, float t) {
#   return (1 - t) * v0 + t * v1;
# }

def lerp(x, y, t):
    return (1 - t) * x + t * y

def angleIt(row, col, elapsed_seconds):
    n = 10
    s = elapsed_seconds % n
    # t = 0.0
    # if s < 1:
    #     t = 0.25
    # elif s < 2:
    #     t = 0.5
    # elif s < 3:
    #     t = 0.75
    # else:
    #     t = 1.0
    return 20 * lerp(row, col, s/n)
    

#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)
