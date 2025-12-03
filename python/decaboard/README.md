# Decaboard: Shader-style Programming with Squares

This is the Python code for the Decaboard, a digital toy for playing with
shader-style programming.

If you'd like to see the version used in WCCCE 2025, see
[decaboard_classic](decaboard_classic/README.md). That version is now
deprecated.

## Introduction

The basic idea is that Decaboard draws a 10 by 10 grid of squares, and using a
single function that is applied to each square, you can control the color,
position, size, angle, and so on of the squares. Since you apply the same one
function to all squares, it is similar to how shader programming works.

For instance, this program ([example.py](example.py)) makes an animated pattern
of rotating squares:

```python
import decaboard
import math

def angleIt(row, col, elapsed_seconds):
    return 30 * math.sin((row + col) * elapsed_seconds)

#
# (1300, 200) is the position of the window on the screen when the program
# starts. Change it to fit your screen.
#
decaboard.run_board_simple(angleIt, 1300, 200)
```

By re-writing `angleIt` function you can create many different patterns.

See [problemset1](problemset1/README.md) and
[problemset2](problemset2/README.md) for some beginner problems to solve.

## How to Use decaboard.run_board_simple

Download [decaboard.py](decaboard.py) and [example.py](example.py) to your
computer, and then run [example.py](example.py), e.g. `python example.py`. A
window of 100 squares should appear, each rotated according to the `angleIt`
function. Careful: the window might sometimes be hidden under other windows.

The `angleIt` always takes the same three parameters:

```python
def angleIt(row, col, elapsed_seconds)
```

`row` and `col` are the row and column of the square the function is being
applied to. Both start at 0 and go up to 9. `elapsed_seconds` is how long the
program has been running for (in seconds). If `angleIt` does not return a value
then a default angle of 0 is used (i.e. the square is not rotated).

Note that the function does *not* need to be called `angleIt`; you can call it
whatever you want. But it should always take the same three parameters.

See [problemset1](problemset1/README.md) and
[problemset2](problemset2/README.md) for more examples.

## How to Use decaboard.run_board

`decaboard.run_board` is a more advanced function that allows you to control the
color, position, size, angle, and so on of the squares. It also takes in the
position of the mouse pointer, so the user can interact with the squares.

For example, this makes colorful moving and rotating squares that change color
based on the mouse position:

```python
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
```

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
dictionary, and the following keys are available:

- `angle`: the angle of the square in degrees
- `fill_color`: the color of the square in 256-RGB format, e.g. `(255, 0, 0)`
  for red
- `edge_color`: the color of the edge of the square in 256-RGB format, e.g. `(0,
  0, 255)` for blue
- `edge_width`: the thickness of the edge of the square
- `dx`: the `x` offset of the center of the square
- `dy`: the `y` offset of the center of the square
- `size`: the edge length of the square

If a key is not present in the returned dictionary then a default value is used.
Unknown keys are ignored.

Note that the function does *not* need to be called `set_square`; you can call
it whatever you want. But it should always take the same five parameters.

`set_square` should be a **pure function**: it should only depend on the input
parameters and not on any global variables. Being pure is how the function can
be easily applied in parallel. While it is possible to make `set_square`
non-pure, that violates the spirit of the demo and is not recommended.

### A Note on Performance

Decaboard does *not* use a GPU shader, and the given function is applied to all
squares sequentially. Since there are only 100 squares, this is usually fast
enough with no noticeable lag.

An important feature of GPU shaders functions is they they are **pure**. A pure
function is one that returns a value that depends only on the input parameters,
and it does not read or write any values outside of the function. By being pure
a function can easily be applied in parallel. You make your Decaboard functions
pure.
