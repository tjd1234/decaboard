# decaboard.py

import turtle
import time

version = "1.0.1"

# dimensions of the window
WIN_WIDTH = 500
WIN_HEIGHT = 500

# the size of the cells and gap between them
CELL_SIZE = 40
GAP = 5

# center of the top-left cell
X_START = 40
Y_START = 40

# background color and line color
BG_COLOR = (0, 0, 0)
LINE_COLOR = (255, 0, 0)

start_time = None

def _turtle_setup(startx, starty):
    #
    # start_time records when the program starts so that the elapsed time can be
    # calculated later
    #
    global start_time
    start_time = time.time()

    #
    # set up the turtle screen
    #
    # (startx, starty) is the position of the window on the screen when the program
    # starts
    #
    turtle.setup(width=WIN_WIDTH, height=WIN_HEIGHT, startx=startx, starty=starty)
    turtle.colormode(255)  # color mode 255 for RGB values
    turtle.bgcolor(BG_COLOR)

    #
    # set the coordinates so that (0, 0) is the top left corner of the board and
    # (WIN_WIDTH, WIN_HEIGHT) is the bottom right corner of the board
    #
    # (0, WIN_HEIGHT) is the top left corner of the board
    # (WIN_WIDTH, 0) is the bottom right corner of the board
    #
    turtle.setworldcoordinates(0, WIN_HEIGHT, WIN_WIDTH, 0)

    #
    # initialize the turtle so it is hidden and moves as fast as possible
    #
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(0)
    turtle.tracer(0, 0)
    turtle.color(LINE_COLOR)

def run_board(angleIt, startx=None, starty=None):
    """
    Runs the board with the given angleIt function. Pass it a function called
    angleIt that takes a row, column, and elapsed time as input, and return the
    angle to draw the square at that position.
    """
    _turtle_setup(startx, starty)
    _main_loop(angleIt)

def _main_loop(angleIt):
    """
    Runs the board with the given angleIt function. Pass it a function called
    angleIt that takes a row, column, and elapsed time as input, and return the
    angle to draw the square at that position.
    """
    while True:
        turtle.clear()
        # (x, y) is the center of the cell
        x = X_START
        y = Y_START
        for row in range(10):
            for col in range(10):
                turtle.penup()
                turtle.goto(x, y)
                
                # get the angle of the square from angleIt
                elapsed_time = time.time() - start_time
                angle = angleIt(row, col, elapsed_time)
                if angle is None:
                    angle = 0
                turtle.setheading(angle) # 0=east, 90=north
                
                # "drive" to the starting corner of the square
                turtle.forward(CELL_SIZE / 2)
                turtle.left(90)
                turtle.forward(CELL_SIZE / 2)
                
                # draw the square
                turtle.pendown()
                turtle.left(90)
                turtle.forward(CELL_SIZE)
                turtle.left(90)
                turtle.forward(CELL_SIZE)
                turtle.left(90)
                turtle.forward(CELL_SIZE)
                turtle.left(90)
                turtle.forward(CELL_SIZE)
                
                x += CELL_SIZE + GAP
            y += CELL_SIZE + GAP
            x = X_START
        turtle.update() # re-draws the screen
        
# #
# # returns angle of the turtle based on the row and column of the square,
# # and the elapsed seconds since the start of the program
# #
# def angleIt(row, col, elapsed_seconds):
#     """
#     Returns the angle of the turtle (in degrees) based on the row and column of
#     the square, and the elapsed seconds since the start of the program.
#     """
#     if row == 0:
#         return elapsed_seconds * 30
#     elif col == 0:
#         return elapsed_seconds * 45
#     else:
#         return elapsed_seconds * 60

# run_board(angleIt)
# turtle.done()  # keep the window open
