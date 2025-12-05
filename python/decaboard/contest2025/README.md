# A Decaboard Coding Contest!

This is a coding contest for the [decaboard shader-style programming
toy](decaboard.py) library.

## Rules

Write a function that takes `(row, col, elapsed_time, mouseX, mouseY)` and
returns a dictionary.

The input parameters are:

- `row`: the row of the square, 0 to 9
- `col`: the column of the square, 0 to 9
- `elapsed_time`: the number of seconds the program has been running
- `mouseX`: the `x` coordinate of the mouse pointer, 0 to 500
- `mouseY`: the `y` coordinate of the mouse pointer, 0 to 500

The return dictionary should contain one or more of the following keys:

- `angle`: the angle of the square in degrees
- `fill_color`: the color of the square in 256-RGB format, e.g. `(255, 0, 0)`
  for red
- `edge_color`: the color of the edge of the square in 256-RGB format, e.g. `(0,
  0, 255)` for blue
- `edge_width`: the thickness of the edge of the square
- `dx`: the `x` offset of the center of the square
- `dy`: the `y` offset of the center of the square
- `size`: the edge length of the square
- There are few things you CANNOT do:
  - You cannot import any modules other than `decaboard` and `math`. Imports
    like `random`, `turtle`, etc. are not allowed.
  - Your program cannot read or write any files or do things like access the
    internet.
  - You cannot make any changes to [decaboard.py](decaboard.py).

See [example1.py](example1.py), [example2.py](example2.py), and
[example3.py](example3.py) for some examples.

While the exact criteria for judging has not been finalized, it will be a
combination of how creative and interesting the patterns are, and the
size/complexity of the code.

## Submission

Submit the following:

- Your full name, school name, grade, and teacher's name.

- Your `.py` file. It should run with the command `python yourfile.py`, and
  we'll put a copy of decaboard.py in the same directory.

- An animated GIF showing a a few seconds of your program running.

- Answer the following questions (one sentence each is enough, but you can
  write more if you want):

  1. What was one thing you learned or figured out during this contest that
     you’re proud of?
  
  2. What was the most challenging part of the contest for you, and why?”
  
  3. If this contest ran again next year, what is one thing you would change or
     keep the same?

**Due Date**: no later than Wednesday December 17, 2025
