# Decaboard+: Introduction to Shader Programming

## Introduction

**Shader programming** is a style of programming where you write a single
function, and that single function is called on each pixel in an image.
Decaboard+ is similar: you write one function called `set_square` that is then
applied to each cell on a 10 by 10 grid. You can control the squares color,
position, size, angle, and so on.

Here's an example ([intro_example.py](intro_example.py)) that draws slowly
expanding squares that angle themselves towards the mouse pointer:

```python
import decaboard_plus
import math

def dist(a, b, x, y):
    return math.sqrt((x - a) ** 2 + (y - b) ** 2)

def set_square(row, col, elapsed_time, mouse_x, mouse_y):
    cell_x, cell_y = decaboard_plus.center_of_cell(row, col)
    
    return {
        'angle': math.degrees(math.atan2(mouse_y - cell_y, mouse_x - cell_x)),
        'size': 10 + (elapsed_time % 100)
    }

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard_plus.run_board(set_square, 1400, 200)
```

By changing the `set_square` function you can create many different patterns.
This style of programming is similar to how
[shaders](https://en.wikipedia.org/wiki/Shader) work in graphics card. In a
graphics shader, a single function that returns a color is applied to each pixel
in an image. Modern graphics cards can run many instance of these functions at
the same time, resulting in extremely fast performance.

## How to Use It

Download [decaboard_plus.py](decaboard_plus.py) and
[intro_example.py](intro_example.py) to the same folder on your computer, and
then run [intro_example.py](intro_example.py), e.g. `python intro_example.py`.

To change the patterns change the `set_square(row, col, elapsed_seconds,
mouse_x, mouse_y)` function in [intro_example.py](intro_example.py).

The header of `set_square` is always this:

```python
def set_square(row, col, elapsed_seconds, mouse_x, mouse_y):
```

The input parameters are:

- `row`: the row of the square, 0 to 9
- `col`: the column of the square, 0 to 9
- `elapsed_seconds`: the number of seconds the program has been running
- `mouse_x`: the `x` coordinate of the mouse pointer, 0 to 500
- `mouse_y`: the `y` coordinate of the mouse pointer, 0 to 500

`set_square` is called once for each of the 100 squares and returns a
dictionary. Currently, the returned dictionary knows these keys:

- `angle`: the angle of the square in degrees
- `fill_color`: the color of the square in 256-RGB format, e.g. `(255, 0, 0)`
  for red
- `edge_color`: the color of the edge of the square in 256-RGB format, e.g. `(0,
  0, 255)` for blue
- `edge_width`: the thickness of the edge of the square
- `dx`: the `x` offset of the center of the square
- `dy`: the `y` offset of the center of the square
- `size`: the edge length of the square

If a key is not present in the return dictionary then a default value is used.
Unknown keys are ignored.

`set_square` should always be a **pure function**: it should only depend on the
input parameters and not on any global variables. Being pure is how the function
can be easily applied in parallel. While it is possible to make `set_square`
non-pure, it is not recommended.

There are also some helper functions available:

- `decaboard_plus.run_board(set_square, startx, starty)`: runs the board with
  the given `set_square` function, and starting at the given `startx` and
  `starty` coordinates on the screen. You call just
  `decaboard_plus.run_board(set_square)` then the window will open in a default
  location.
- `decaboard_plus.center_of_cell(row, col)`: returns the center of the cell at
  the given row and column.
- `decaboard_plus.clamp(value, min, max)`: returns `value` clamped to the range
  `min` to `max`.
