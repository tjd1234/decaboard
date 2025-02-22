# Problem Set 2

To try these problems, download [decaboard.py](decaboard.py) and
[start.py](start.py) to your computer, and then run `python start.py`.

For each problem, write an `angleIt` function that draws the picture. The number
returned by `angleIt` is the angle (in degrees) that the square should rotated
around its center.

For instance, to draw this:

<img src="start.png" width="400">

You would write this (see [start.py](start.py)):

```python
# example.py

import decaboard

def angleIt(row, col, elapsed_seconds):
    return 34

decaboard.run_board(angleIt)
```

You can control where the window opens by passing in the location of where to
put the window, e.g. `decaboard.run_board(angleIt, 1400, 200)` opens the window
in the right side of the screen, near the top.

You can put all your answers into [start.py](start.py), naming them like
`angleIt1`, `angleIt2`, etc. Then pass the function you want to use to
`decaboard.run_board`.

Problems are still under development: see [prob1_sol.py](prob1_sol.py),
[prob2_sol.py](prob2_sol.py), [prob3_sol.py](prob3_sol.py), ... for some
samples. Also see [probChallenge.py](probChallenge.py) and
[probChallenge2.py](probChallenge2.py) for some more challenging problems.
