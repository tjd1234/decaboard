# decaboard.py

"""
Decaboard - A visual programming toy for creating patterns on a 10x10 grid.

This module provides a turtle-based graphical interface for displaying and animating patterns
on a grid. It supports multiple pattern types, mouse interaction, and various display options.

Features:
- Multiple pattern types (wave, spiral, ripple)
- Mouse interaction to show cell positions
- FPS display
- Grid display
- Pause/resume animation
- Pattern switching with number keys

Usage:
    from decaboard import run_board, wave_pattern
    run_board(wave_pattern)
"""

import turtle
import time
import math
import random
from typing import Dict, Callable, Any, Tuple, Optional

VERSION = "Decaboard v2.2"

# dimensions of the window
WIN_WIDTH = 500
WIN_HEIGHT = 500

# the size of the cells and gap between them
CELL_SIZE = 40
GAP = 5

# board dimensions
BOARD_SIZE = 10  # 10x10 grid

# center of the top-left cell
X_START = 40
Y_START = 40

# background color and line color
BG_COLOR = (0, 0, 0)
LINE_COLOR = (255, 0, 0)
GRID_COLOR = (255, 255, 255)  # White grid lines
TEXT_COLOR = (255, 255, 255)  # White text for cell position

# canvas for mouse position
_canvas = turtle.getcanvas()

PAUSED = False
SHOW_FPS = False
SHOW_GRID = False
SHOW_TIME = False
CELL_POS = None  # Current cell position (row, col) when mouse is down

# Performance tracking variables
_frame_count = 0
_last_fps_time = 0
_current_fps = 0

# Pattern registry
PATTERNS: Dict[int, Callable] = {}
CURRENT_PATTERN: Optional[Callable] = None


def clamp(value: float, lo: float, hi: float) -> float:
    """
    Clamps a value between a lower and upper bound.
    """
    if value < lo:
        return lo
    if value > hi:
        return hi
    return value


def _get_mouse_position_relative() -> Tuple[float, float]:
    """
    Get mouse position in screen coordinates, i.e. 0, 0 is the top left corner of
    the window.
    """
    # Get mouse position in screen coordinates
    screen_x = _canvas.winfo_pointerx()
    screen_y = _canvas.winfo_pointery()

    # Get canvas position in screen coordinates
    canvas_x = _canvas.winfo_rootx()
    canvas_y = _canvas.winfo_rooty()

    # Subtract to get position relative to canvas
    rel_x = screen_x - canvas_x
    rel_y = screen_y - canvas_y

    return clamp(rel_x, 0, WIN_WIDTH), clamp(rel_y, 0, WIN_HEIGHT)


def center_of_cell(row: int, col: int) -> Tuple[float, float]:
    """
    Returns the center of the cell at the given row and column.
    """
    x = X_START + col * (CELL_SIZE + GAP) + CELL_SIZE / 2
    y = Y_START + row * (CELL_SIZE + GAP) + CELL_SIZE / 2
    return x, y


# timing variable for elapsed second calculation
_start_time = 0


def _turtle_setup(startx: Optional[int] = None, starty: Optional[int] = None) -> None:
    #
    # _start_time records when the program starts so that the elapsed time can be
    # calculated later
    #
    global _start_time
    _start_time = time.time()

    #
    # set up the turtle screen
    #
    # (startx, starty) is the position of the window on the screen when the program
    # starts
    #
    turtle.setup(width=WIN_WIDTH, height=WIN_HEIGHT, startx=startx, starty=starty)
    turtle.title(VERSION)
    turtle.colormode(255)  # color mode 255 for RGB values
    turtle.bgcolor(BG_COLOR)

    #
    # set the coordinates so that (0, 0) is the top left corner of the board and
    # (WIN_WIDTH, WIN_HEIGHT) is the bottom right corner of the board
    #
    # (0, WIN_HEIGHT) is the top left corner of the board (WIN_WIDTH, 0) is the
    # bottom right corner of the board
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

    # Add key bindings
    turtle.onkey(toggle_pause, "space")
    turtle.onkey(toggle_fps_display, "f")
    turtle.onkey(toggle_grid_display, "g")
    turtle.onkey(toggle_time_display, "t")

    # Add number key bindings for patterns
    for i in range(1, 10):
        # Create a function that captures the current value of i
        def make_key_handler(num: int) -> Callable[[], None]:
            return lambda: switch_pattern(num)

        turtle.onkey(make_key_handler(i), str(i))

    # Add mouse event handler
    turtle.onscreenclick(handle_mouse_click)

    turtle.listen()


def handle_mouse_click(x: float, y: float) -> None:
    """Handle mouse click event to show cell position"""
    global MOUSE_POS, CELL_POS
    MOUSE_POS = (x, y)
    CELL_POS = get_cell_at_position(x, y)

    # If we're on a cell, print the position to the console
    if CELL_POS is not None:
        row, col = CELL_POS
        print(f"Cell position: ({row}, {col})")


def get_cell_at_position(x: float, y: float) -> Optional[Tuple[int, int]]:
    """
    Returns the (row, col) of the cell at the given position.
    Returns None if the position is not within any cell's grid area.
    """
    # Debug print to see what coordinates we're getting
    # print(f"Click at: ({x}, {y})")

    # The turtle coordinate system has (0,0) at the top-left corner
    # and (WIN_WIDTH, WIN_HEIGHT) at the bottom-right corner

    # Calculate the offset to center the grid lines over the center points of the squares
    # This is the same offset used in the draw_grid function
    offset = CELL_SIZE / 2

    # Calculate the board boundaries with the offset
    board_left = X_START - offset
    board_right = X_START + BOARD_SIZE * (CELL_SIZE + GAP) - offset
    board_top = Y_START - offset
    board_bottom = Y_START + BOARD_SIZE * (CELL_SIZE + GAP) - offset

    # Check if the click is within the board boundaries
    if x < board_left or x > board_right or y < board_top or y > board_bottom:
        print("Outside board boundaries")
        return None

    # Calculate the relative position within the board
    rel_x = x - board_left
    rel_y = y - board_top

    # Calculate row and column based on relative position
    # Each cell is CELL_SIZE + GAP wide/tall
    col = int(rel_x / (CELL_SIZE + GAP))
    row = int(rel_y / (CELL_SIZE + GAP))

    # Ensure row and col are within valid range
    if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
        print(f"Invalid row/col: ({row}, {col})")
        return None

    # print(f"Cell position: ({row}, {col})")
    return (row, col)


def print_instruction() -> None:
    print("space - pause/resume animation")
    print("    f - toggle FPS display")
    print("    g - toggle grid display")
    print("    t - toggle elapsed time display")
    print("Click on a cell to see its position")
    print("Press 1-4 to switch patterns")


def run_board(
    set_square: Callable, startx: Optional[int] = None, starty: Optional[int] = None
) -> None:
    """
    Runs the board with the given set_square function. Pass it a function called
    set_square that takes a row, column, and elapsed time as input, and return
    the angle to draw the square at that position.
    """
    global CURRENT_PATTERN

    # Register the initial pattern
    register_pattern(1, set_square)
    CURRENT_PATTERN = set_square

    _turtle_setup(startx, starty)
    print_instruction()
    _main_loop()


def _main_loop() -> None:
    """
    Runs the board with the current pattern function.
    """
    global _frame_count, _last_fps_time, _current_fps

    while True:
        try:
            if PAUSED:
                turtle.update()
                time.sleep(0.1)  # Reduce CPU usage while paused
                continue

            turtle.clear()
            x = X_START
            y = Y_START
            # get mouse position
            mouse_x, mouse_y = _get_mouse_position_relative()

            # get properties from the set_square function
            elapsed_time = time.time() - _start_time

            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    # set default values
                    angle: float = 0.0
                    fill_color: Tuple[int, int, int] = BG_COLOR
                    edge_color: Tuple[int, int, int] = LINE_COLOR
                    edge_width: int = 1
                    dx: float = 0.0
                    dy: float = 0.0
                    size: float = CELL_SIZE

                    # Make sure CURRENT_PATTERN is not None
                    if CURRENT_PATTERN is None:
                        # Default to a simple pattern if none is set
                        d = {"fill_color": BG_COLOR}
                    else:
                        try:
                            d = CURRENT_PATTERN(
                                row, col, elapsed_time, mouse_x, mouse_y
                            )
                        except Exception as e:
                            print(f"Error in pattern function: {e}")
                            d = {"fill_color": BG_COLOR}  # Fallback to default

                    if d is not None:
                        if "angle" in d and isinstance(d["angle"], (int, float)):
                            angle = float(d["angle"])
                        if (
                            "fill_color" in d
                            and isinstance(d["fill_color"], tuple)
                            and len(d["fill_color"]) == 3
                        ):
                            fill_color = d["fill_color"]
                        if (
                            "edge_color" in d
                            and isinstance(d["edge_color"], tuple)
                            and len(d["edge_color"]) == 3
                        ):
                            edge_color = d["edge_color"]
                        if "edge_width" in d and isinstance(
                            d["edge_width"], (int, float)
                        ):
                            edge_width = int(d["edge_width"])
                        if "dx" in d and isinstance(d["dx"], (int, float)):
                            dx = float(d["dx"])
                        if "dy" in d and isinstance(d["dy"], (int, float)):
                            dy = float(d["dy"])
                        if "size" in d and isinstance(d["size"], (int, float)):
                            size = float(d["size"])

                    # draw the square
                    turtle.penup()
                    turtle.goto(x + dx, y + dy)
                    turtle.setheading(angle)  # 0=east, 90=north
                    turtle.color(edge_color, fill_color)
                    turtle.width(edge_width)

                    # "drive" to the starting corner of the square
                    turtle.forward(size / 2)
                    turtle.left(90)
                    turtle.forward(size / 2)

                    # draw the square
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.left(90)
                    turtle.forward(size)
                    turtle.left(90)
                    turtle.forward(size)
                    turtle.left(90)
                    turtle.forward(size)
                    turtle.left(90)
                    turtle.forward(size)
                    turtle.end_fill()

                    x += CELL_SIZE + GAP
                y += CELL_SIZE + GAP
                x = X_START

            # Draw the grid if enabled
            if SHOW_GRID:
                draw_grid()

            # Display cell position if a cell was clicked
            if CELL_POS is not None:
                row, col = CELL_POS
                cell_x, cell_y = center_of_cell(row, col)

                # Draw a white circle at the cell center
                turtle.penup()
                turtle.goto(cell_x - CELL_SIZE / 2, cell_y - CELL_SIZE / 2)
                turtle.color(TEXT_COLOR)
                turtle.dot(5)

                # Display the (row, col) text centered above the cell
                turtle.penup()
                turtle.goto(cell_x - 20, cell_y - 20)  # Position above the cell
                turtle.color(TEXT_COLOR)
                turtle.write(
                    f"({row}, {col})", align="center", font=("Arial", 12, "bold")
                )

            # Update FPS counter
            _frame_count += 1
            current_time = time.time()
            if current_time - _last_fps_time >= 1.0:  # Update FPS every second
                _current_fps = _frame_count
                _frame_count = 0
                _last_fps_time = current_time

            # Display FPS if enabled
            if SHOW_FPS:
                turtle.penup()
                turtle.goto(0, 10)  # Position in top-left corner
                turtle.color(TEXT_COLOR)
                turtle.write(f"{_current_fps} fps", font=("Arial", 10, "normal"))

            # Display elapsed time if enabled
            if SHOW_TIME:
                turtle.penup()
                turtle.goto(
                    WIN_WIDTH / 2 + 10, WIN_HEIGHT - 10
                )  # Position in top-right corner
                turtle.color(TEXT_COLOR)
                turtle.write(
                    f"Elapsed time: {elapsed_time:.1f}s",
                    align="right",
                    font=("Arial", 11, "normal"),
                )

            turtle.update()  # re-draws the screen
        except (turtle.Terminator, Exception):
            # Window was closed or turtle terminated, exit gracefully without error
            return


def run_board_simple(
    set_square: Callable[[int, int, float], float],
    startx: Optional[int] = None,
    starty: Optional[int] = None,
) -> None:
    """
    Runs the board with a simpler set_square function.

    The set_square function should take (row, col, elapsed_time) and return
    just the angle (a float) instead of a full dictionary.

    Args:
        set_square: Function that takes (row, col, elapsed_time) and returns angle
        startx: Optional x position for window
        starty: Optional y position for window
    """

    def wrapped_set_square(
        row: int, col: int, elapsed_time: float, mouse_x: float, mouse_y: float
    ) -> Dict[str, Any]:
        """Wrapper that converts simple function to full dictionary format"""
        angle = set_square(row, col, elapsed_time)
        return create_pattern(angle=angle)

    # Use the existing run_board with the wrapped function
    run_board(wrapped_set_square, startx, starty)


def draw_grid() -> None:
    """
    Draws a static grid of white lines showing all cell boundaries.
    The grid lines are centered over the center points of the squares.
    Also draws row and column numbers.
    """
    # Set up for drawing the grid
    turtle.penup()
    turtle.color(GRID_COLOR)
    turtle.width(1)

    # Calculate the offset to center the grid lines over the center points of the squares
    offset = CELL_SIZE / 2

    # Draw horizontal lines
    for row in range(BOARD_SIZE + 1):  # BOARD_SIZE + 1 lines for BOARD_SIZE cells
        y = Y_START + row * (CELL_SIZE + GAP) - offset
        turtle.goto(X_START - offset, y)
        turtle.pendown()
        turtle.goto(X_START + BOARD_SIZE * (CELL_SIZE + GAP) - offset, y)
        turtle.penup()

    # Draw vertical lines
    for col in range(BOARD_SIZE + 1):  # BOARD_SIZE + 1 lines for BOARD_SIZE cells
        x = X_START + col * (CELL_SIZE + GAP) - offset
        turtle.goto(x, Y_START - offset)
        turtle.pendown()
        turtle.goto(x, Y_START + BOARD_SIZE * (CELL_SIZE + GAP) - offset)
        turtle.penup()

    # Draw row numbers (0-9) on the left side
    for row in range(BOARD_SIZE):
        # Calculate the center of each cell
        cell_x = X_START - offset - 5  # Position to the left of the grid
        cell_y = Y_START + row * (CELL_SIZE + GAP) + CELL_SIZE / 2 - offset + 10

        # Draw the row number
        turtle.penup()
        turtle.goto(cell_x, cell_y)
        turtle.color(GRID_COLOR)
        turtle.write(str(row), align="right", font=("Arial", 11, "normal"))

    # Draw column numbers (0-9) on the top
    for col in range(BOARD_SIZE):
        # Calculate the center of each cell
        cell_x = X_START + col * (CELL_SIZE + GAP) + CELL_SIZE / 2 - offset + 5
        cell_y = Y_START - offset - 5  # Position above the grid

        # Draw the column number
        turtle.penup()
        turtle.goto(cell_x, cell_y)
        turtle.color(GRID_COLOR)
        turtle.write(str(col), align="center", font=("Arial", 11, "normal"))


def toggle_pause() -> None:
    global PAUSED
    PAUSED = not PAUSED
    print("Animation", "paused" if PAUSED else "resumed")


def toggle_fps_display() -> None:
    """Toggle the FPS display on/off"""
    global SHOW_FPS
    SHOW_FPS = not SHOW_FPS
    print("FPS display", "enabled" if SHOW_FPS else "disabled")


def toggle_grid_display() -> None:
    """Toggle the grid display on/off"""
    global SHOW_GRID
    SHOW_GRID = not SHOW_GRID
    print("Grid display", "enabled" if SHOW_GRID else "disabled")


def toggle_time_display() -> None:
    """Toggle the elapsed time display on/off"""
    global SHOW_TIME
    SHOW_TIME = not SHOW_TIME
    print("Elapsed time display", "enabled" if SHOW_TIME else "disabled")


def register_pattern(pattern_id: int, pattern_func: Callable) -> None:
    """
    Register a pattern function with a specific ID.
    """
    global PATTERNS
    PATTERNS[pattern_id] = pattern_func
    # print(f"Pattern {pattern_id} registered")


def switch_pattern(pattern_id: int) -> None:
    """
    Switch to a different pattern by ID.
    """
    global CURRENT_PATTERN
    if pattern_id in PATTERNS:
        CURRENT_PATTERN = PATTERNS[pattern_id]
        print(f"Switched to pattern {pattern_id}")
    else:
        print(f"Pattern {pattern_id} not found")


def get_random_color() -> Tuple[int, int, int]:
    """Returns a random RGB color"""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def create_color(r: int, g: int, b: int) -> Tuple[int, int, int]:
    """
    Creates an RGB color tuple with values clamped to 0-255 range.

    Args:
        r: Red component (0-255)
        g: Green component (0-255)
        b: Blue component (0-255)

    Returns:
        A tuple of (r, g, b) with values clamped to 0-255
    """
    return (int(clamp(r, 0, 255)), int(clamp(g, 0, 255)), int(clamp(b, 0, 255)))


def wave_pattern(
    row: int, col: int, elapsed_time: float, mouse_x: float, mouse_y: float
) -> Dict[str, Any]:
    # Create a wave pattern that moves across the board
    wave_speed = 2.0
    wave_frequency = 0.5

    # Calculate wave value based on position and time
    wave_value = math.sin(row * wave_frequency + elapsed_time * wave_speed)

    # Map wave value to angle (-30 to 30 degrees)
    angle = wave_value * 30

    # Map wave value to color (blue to red)
    r = int(128 + wave_value * 127)
    b = int(128 - wave_value * 127)
    color = create_color(r, 0, b)

    return create_pattern(angle=angle, fill_color=color)


def spiral_pattern(
    row: int, col: int, elapsed_time: float, mouse_x: float, mouse_y: float
) -> Dict[str, Any]:
    # Create a spiral pattern that rotates
    center_row, center_col = 5, 5

    # Calculate angle and distance from center
    dx = col - center_col
    dy = row - center_row
    angle = math.atan2(dy, dx)
    distance = math.sqrt(dx * dx + dy * dy)

    # Rotate based on time
    rotation_speed = 1.0
    rotated_angle = angle + elapsed_time * rotation_speed

    # Calculate color based on distance and time
    hue = (distance * 0.2 + elapsed_time * 0.1) % 1.0
    r = int(128 + 127 * math.sin(hue * 2 * math.pi))
    g = int(128 + 127 * math.sin(hue * 2 * math.pi + 2 * math.pi / 3))
    b = int(128 + 127 * math.sin(hue * 2 * math.pi + 4 * math.pi / 3))

    return create_pattern(
        angle=math.degrees(rotated_angle), fill_color=create_color(r, g, b)
    )


def ripple_pattern(
    row: int, col: int, elapsed_time: float, mouse_x: float, mouse_y: float
) -> Dict[str, Any]:
    # Create ripple effect from mouse position
    cell_x, cell_y = center_of_cell(row, col)
    dx = mouse_x - cell_x
    dy = mouse_y - cell_y
    distance = math.sqrt(dx * dx + dy * dy)

    # Create ripples that expand from mouse
    ripple_speed = 3.0
    ripple_frequency = 0.1
    ripple_value = math.sin(distance * ripple_frequency - elapsed_time * ripple_speed)

    # Map ripple value to size (80% to 120% of normal)
    size_factor = 0.8 + 0.4 * (ripple_value + 1) / 2

    # Map ripple value to color
    r = int(128 + ripple_value * 127)
    g = int(128 - ripple_value * 127)
    color = create_color(r, g, 0)

    return create_pattern(size=CELL_SIZE * size_factor, fill_color=color)


def create_pattern(
    angle: float = 0.0,
    fill_color: Tuple[int, int, int] = BG_COLOR,
    edge_color: Tuple[int, int, int] = LINE_COLOR,
    edge_width: int = 1,
    dx: float = 0.0,
    dy: float = 0.0,
    size: float = CELL_SIZE,
) -> Dict[str, Any]:
    """
    Creates a pattern dictionary with the given parameters.

    Args:
        angle: Rotation angle in degrees
        fill_color: RGB color tuple for the fill
        edge_color: RGB color tuple for the edge
        edge_width: Width of the edge line
        dx: X offset from the cell center
        dy: Y offset from the cell center
        size: Size of the cell

    Returns:
        A dictionary with the pattern parameters
    """
    return {
        "angle": angle,
        "fill_color": fill_color,
        "edge_color": edge_color,
        "edge_width": edge_width,
        "dx": dx,
        "dy": dy,
        "size": size,
    }


# Register the additional patterns
register_pattern(2, wave_pattern)
register_pattern(3, spiral_pattern)
register_pattern(4, ripple_pattern)
