# Mouse Point Example

To try these problems, download [decaboard.py](decaboard.py) and
[start.py](start.py) to your computer, and then run `python start.py`.

If you are brand new to shader-style programming,ou may want to look [problem
set 1](../problemset1/README.md) and [problem set 2](../problemset2/README.md)
for some simpler examples.

For each problem, write an `angleIt` function that draws the picture. It must
take in the following parameters:

- `row`: the row of the square, 0 to 9
- `col`: the column of the square, 0 to 9
- `elapsed_seconds`: the number of seconds the program has been running
- `mouseX`: the `x` coordinate of the mouse pointer, 0 to 500
- `mouseY`: the `y` coordinate of the mouse pointer, 0 to 500

`angleIt` should always return a dictionary with one or more of the following
keys (and an associated value):

- `angle`: the angle of the square in degrees
- `fill_color`: the color of the square in 256-RGB format, e.g. `(255, 0, 0)`
  for red
- `edge_color`: the color of the edge of the square in 256-RGB format, e.g. `(0,
  0, 255)` for blue
- `edge_width`: the thickness of the edge of the square
- `dx`: the `x` offset of the center of the square
- `dy`: the `y` offset of the center of the square
- `size`: the edge length of the square

Missing keys are given default values, and unknown keys are ignored.

For instance, to draw this:

<img src="start.png" width="400">

You would write this (see [start.py](start.py)):

```python
import decaboard

def angleIt(row, col, elapsed_seconds, mouseX, mouseY):
    return {
        "angle": 0
    }

decaboard.run_board(angleIt)
```

See [this PowerPoint presentation](pointingToTheMouse.pptx) for a step-by-step
guide on to make something point towards the mouse.
[mouse_point.py](mouse_point.py) is a fun application of this technique.
