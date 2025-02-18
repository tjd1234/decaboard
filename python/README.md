# Decaboard: The Art of Square Patterns

## Introduction

The program [example.py](example.py) draws a grid of 100 squares, and rotates
each square according to the angle returned by the `angleIt(row, col,
elapsed_seconds)` function. The same `angleIt` it function is run on all 100
squares:

```python
# example.py

import decaboard
import math

def angleIt(row, col, elapsed_seconds):
    return 30 * math.sin((row + col) * elapsed_seconds)

#
# (1300, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1400, 200)
```

By changing the `angleIt` function you can create many different patterns. This
style of programming is similar to how
[shaders](https://en.wikipedia.org/wiki/Shader) work in graphics card. In a
graphics shader, you write a single function that sets the color of all the
pixels in an image. Modern graphics cards can run many instance of these
functions at the same time, resulting in extremely fast performance.

See [problemset1](problemset1/README.md) for a set of beginner problems to
solve.

## How to Use It

Download `decaboard.py` and [example.py](example.py) to your computer, and then
run [example.py](example.py). Depending on the values the `angleIt` function
returns, different patterns of squares should appear.

To change the patterns change the `angleIt(row, col, elapsed_seconds)` function
in [example.py](example.py). `angleIt` is called once for each of the 100
squares on the board.

`row` and `col` are the row and column of the square the function is being
applied to, and `elapsed_seconds` is how long the program has been running for
(in seconds). Rows and columns start at 0, and if `angleIt` does not return a
value for a square a default angle of 0 is used (i.e. the square is not
rotated).


## Examples

This draws all squares rotated 45 degrees:

```python
def angleIt(row, col, elapsed_seconds):
    return 45
```

This draws the square in the first row and column at 45 degrees, and all other
squares at 0 degrees:

```python
def angleIt(row, col, elapsed_seconds):
    if row == 0 and col == 0:
        return 45
```

The value 45 is returned for the square in the first row and column.  

This sets the upper-left and lower-right squares at 45 degrees, and all other
squares at 0 degrees:

```python
def angleIt(row, col, elapsed_seconds):
    if row == 1 and col == 1:
        return 45
    if row == 10 and col == 10:
        return 45
```

This rotates just the squares on the main diagonal:

```python
def angleIt(row, col, elapsed_seconds):
    if row == col:
        return 45
```

This draws a nice pattern by setting the squares angle according to their
position:

```python
def angleIt(row, col, elapsed_seconds):
    return row * col
```

This draws another interesting pattern:

```python
def angleIt(row, col, elapsed_seconds):
    return 5 * row + 10 * col
 ```

You can use other functions to compute the angle. The sine function of often
interesting:

```python
def angleIt(row, col, elapsed_seconds):
    return 25 * math.sin(5 * row + 10 * col)
```

The `%` operator is the modulo (remainder) operator, and this sets every other
square to 45 degrees, sort of checkerboard pattern:

```python
def angleIt(row, col, elapsed_seconds):
    if (row + col) % 2 == 0:
        return 45
```

Using `elapsed_seconds` you get patterns that change over time. This makes all
the squares rotate in unison:

```python
def angleIt(row, col, elapsed_seconds):
    return elapsed_seconds * 30
```

Change the 30 to different values to make it speed up or slow down.

This makes each row of squares rotate at different speeds:

```python
def angleIt(row, col, elapsed_seconds):
    return row * elapsed_seconds * 30
```

Using the `math.sin` function makes the squares rotate back and forth:

```python
def angleIt(row, col, elapsed_seconds):
    return 30 * math.sin(elapsed_seconds)
```

Notice how the squares *don't* turn at a constant rate: they accelerate a bit
when they start, and decelerate a bit when they end. This gives the rotation a
nice and smooth appearance.

It's not hard to come up with interesting patterns, e.g.:

```python
def angleIt(row, col, elapsed_seconds):
    return 30 * math.sin((row + col) * elapsed_seconds)
```
