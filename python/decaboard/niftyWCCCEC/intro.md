# Decaboard: Introduction to Shader Programming

## GPUs and Shaders

In addition to their CPU (central processing unit), most modern computers also
have processing unit called *GPU*s that is designed specifically for doing
computer graphics. A single GPU can have thousands of *cores*, i.e. small
processing units designed specifically to graphics operation quickly. 

For example, the NVIDIA GeForce RTX 4090 GPU has 16,384 cores that can run in
parallel. It could, for instance, compute lighting effects (shading) in a video
game in *real time*. While the main CPU could do the same calculations, it would
not be able to do them as fast, and so in practice a GPU is necessary for
real-time graphics. 

But there's a programming problem: how do you program thousands of cores? How do
you tell them what to do? How do you divide a problem into 16,000 sub-problems?
The answer we'll explore here is [shader
programming](https://en.wikipedia.org/wiki/Shader), a style of programming
designed specifically for working with thousands of cores.

The key idea is simple: you, the programmer, write a *single function* that sets
the color of a *single pixel*, and then that function is applied to all the
pixels in an image in parallel.

At first this might seem *too* simple. How can you do anything useful by writing
*one* function that sets the color of *one* pixel? The input to this function is
typically the row and column of the pixel, and the time that has elapsed since
the program started. That's enough information to compute a wide variety of
things, including shapes, animation, lighting effects, and much more.

It takes a bit of practice to get the hang of shaders. Some things that are easy
to do in regular programming might require some cleverness to implement as a
shader.

Shaders are typically written in a **shader language** designed specifically for
the task. For instance, [GLSL](https://en.wikipedia.org/wiki/GLSL) is a popular
C-like language for writing shaders. If you are interested in learning more,
[The Shader Book](https://thebookofshaders.com/) is a good start that has many
interactive examples. [ShaderToy](https://www.shadertoy.com/) is another great
resource that shows many amazing examples of what shaders can do.

## Decaboard: An Introduction to Shader Programming

**Decaboard** introduces shader-style programming using a 10 x 10 grid of
squares. Instead of setting colors as you would with a GPU shader, you set the
rotation angle of each square. You write one function that is applied to all the
squares at the same time. 

To try decaboard, you need Python installed on your computer with turtle
graphics working. Then download [decaboard.py](decaboard.py) and
[example.py](example.py) to the same directory, and run `example.py`, e.g. with
the command `python example.py`. A window of 100 rotated squares should pop up:

<img src="example1.png" width="200">

Here is [example.py](example.py):

```python
# example.py

import decaboard

def angleIt(row, col, elapsed_seconds):
    return 41

decaboard.run_board(angleIt)
```


All decaboard programs have this same structure: the programmer must write the
`angleIt` function, and `angleIt` is passed to `decaboard` and applied to all
100 squares.

Decaboard does not actually use a GPU shader, it just simulates the shader style
programming using regular Python.

To learn more, try these problems:

- [Problem Set 1](problemset1/README.md). In these problems you're given a
  picture of the board, and must write an `angleIt` function to make that
  picture.
- [Problem Set 2](problemset2/README.md). These problems give you an `angleIt`
  function, and ask you to draw the picture it makes. These show how to animate
  the squares, and how even simple functions can make interesting and unexpected
  patterns.
- [Problem Set 3](problemset3/README.md). These introduce a number mathematical
  "utility" functions, and has the same question style as Problem Set 2.