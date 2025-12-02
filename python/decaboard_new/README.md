# Decaboard: Introduction to Shader-style Programming

## Introduction

**Shader-style programming** is a style of programming where you write a single
function and then apply single function to each pixel in an image. Decaboard is
similar: you write one function called `set_square` that is then applied to each
cell on a 10 by 10 grid. You can control the squares color, position, size,
angle, and so on. While it does not use an actual GPU shader, it shows the kinds
of programming puzzles that arise when doing shader programming.

Here's an example ([intro_example.py](intro_example.py)) that draws slowly
expanding squares that angle themselves towards the mouse pointer:

```python
import decaboard
import math

def dist(a, b, x, y):
    return math.sqrt((x - a) ** 2 + (y - b) ** 2)

def set_square(row, col, elapsed_time, mouse_x, mouse_y):
    cell_x, cell_y = decaboard.center_of_cell(row, col)
    
    return {
        'angle': math.degrees(math.atan2(mouse_y - cell_y, mouse_x - cell_x)),
        'size': 10 + (elapsed_time % 100)
    }

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(set_square, 1400, 200)
```

The `set_square` function is applied to each of the 100 squares on the board. By
changing the `set_square` function you can create many different patterns. This
style of programming is similar to how graphics card
[shaders](https://en.wikipedia.org/wiki/Shader) work. In a graphics shader, a
single function that returns a color is applied to each pixel in an image.
Modern graphics cards can run many instance of these functions at the same time,
resulting in extremely fast performance.

## How to Use It

Download [decaboard.py](decaboard.py) and [intro_example.py](intro_example.py)
to the same folder on your computer, and then run
[intro_example.py](intro_example.py), e.g. `python intro_example.py`.

Modify `set_square(row, col, elapsed_seconds, mouse_x, mouse_y)` in
[intro_example.py](intro_example.py) to change try new patterns.

The header of `set_square` is this:

```python
def set_square(row, col, elapsed_seconds, mouse_x, mouse_y):
```

The input parameters are:

- `row`: the row of the square, 0 to 9
- `col`: the column of the square, 0 to 9
- `elapsed_seconds`: the number of seconds the program has been running
- `mouse_x`: the `x` coordinate of the mouse pointer, 0 to 500
- `mouse_y`: the `y` coordinate of the mouse pointer, 0 to 500

`set_square` is called once for each of the 100 squares and should return a
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

`set_square` should be a **pure function**: it should only depend on the input
parameters and not on any global variables. Being pure is how the function can
be easily applied in parallel. While it is possible to make `set_square`
non-pure, that violates the spirit of the demo and is not recommended.

### The run_board_simple function

The `run_board_simple` function takes a simpler function as input, one that only
returns the angle of the square, and takes the row, column, and elapsed time as
input. If you are new to programming, this is a good starting point, since it's
easier to use and understand. 

Here's an example ([simple_example.py](simple_example.py)):

```python
import decaboard 

def angleIt(row, col, elapsed_time):
    return row * 10 + elapsed_time * 30

decaboard.run_board_simple(angleIt)
```

[Problem set 1](problemset1/README.md) and [Problem set
2](problemset2/README.md) both use this simpler funciton.

### Helper Functions

There are also some helper functions:

- `decaboard.run_board(set_square, startx, starty)`: runs the board with the
  given `set_square` function, and starting at the given `startx` and `starty`
  coordinates on the screen. You call just `decaboard.run_board(set_square)`
  then the window will open in a default location.
- `decaboard.center_of_cell(row, col)`: returns the center of the cell at the
  given row and column.
- `decaboard.clamp(value, min, max)`: returns `value` clamped to the range `min`
  to `max`.
