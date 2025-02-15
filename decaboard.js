// decaboard.js

//
// Inspired by shaders, and the game Replicube (search for it on Steam).
//

//
// Bugs to fix:
// - ...
//

//
// To do:
// - in addition to color, let the use set the angle/scale of the squares
//

//
// helper code
//
function dotAt(x, y, size, color) {
    push();
    fill(color);
    noStroke();
    ellipse(x, y, size, size);
    pop();
}

function redDotAt(x, y) {
    dotAt(x, y, 5, "red");
}

function greenDotAt(x, y) {
    dotAt(x, y, 5, "green");
}

// call randColor(true) to get a random color with a random alpha as well
function randColor(randAlpha = false) {
    return [
        random(0, 255),
        random(0, 255),
        random(0, 255),
        randAlpha ? random(0, 255) : 255,
    ];
}

//
// main code
//

const BOARD_WIDTH = 455;
const BOARD_HEIGHT = 455;
const GAP = 5;
const CELL_SIZE = 40;

const WIDTH = 500;
const HEIGHT = 500;
const MARGIN = (WIDTH - BOARD_WIDTH) / 2;

const FRAME_COLOR = 175;
const BOARD_COLOR = 0;
const LINE_COLOR = 255;
const LINE_WIDTH = 1;

const DEFAULT_COLOR = [255, 0, 0];

// grid is a 10x10 matrix of colors, initially all 0s
// a color is [red, green, blue, alpha]
const grid = Array(10)
    .fill()
    .map(() =>
        Array(10)
            .fill()
            .map(() => ({ color: DEFAULT_COLOR, angle: 0, scale: 1 }))
    );

function randomGridColors() {
    for (let r = 0; r < 10; r++) {
        for (let c = 0; c < 10; c++) {
            grid[r][c].color = randColor();
        }
    }
}

function setup() {
    const canvas = createCanvas(WIDTH, HEIGHT);
    canvas.parent('canvas-container');
    angleMode(DEGREES);

    // randomGridColors();
} // setup

function draw() {
    // draw frame and board
    background(FRAME_COLOR);
    noStroke();
    fill(BOARD_COLOR);
    rect(MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN);

    // apply the colorIt function to the grid
    for (let r = 0; r < 10; r++) {
        for (let c = 0; c < 10; c++) {
            const angle = angleIt(r, c, frameCount);
            grid[r][c].angle = angle;
        }
    }

    // draw a grid of 10 by 10 squares, each square fitting perfectly in the
    // grid so that lines can still be seen
    // noStroke();
    noFill();
    let x = MARGIN + GAP;
    let y = MARGIN + GAP;
    for (let r = 0; r < 10; r++) {
        for (let c = 0; c < 10; c++) {
            const square = grid[r][c];
            push();
            rectMode(CENTER);
            translate(x + CELL_SIZE / 2, y + CELL_SIZE / 2);
            rotate(square.angle);
            scale(square.scale);
            // fill(square.color);
            stroke(square.color);
            strokeWeight(2);
            rect(0, 0, CELL_SIZE, CELL_SIZE);
            pop();
            x += CELL_SIZE + GAP;
        }
        y += CELL_SIZE + GAP;
        x = MARGIN + GAP;
    }
} // draw

//
// angleIt functions for (x, y, time)
//

// rotate all squares by 45 degrees
function angleIt(r, c, time) {
    if ((r + c) % 2 === 1) {
        return c + 0.5 * r * time;
    } else {
        return -(r + time);
    }
}

// // rotate all squares by 45 degrees
// function angleIt(r, c, time) {
//     if ((r + c) % 2 === 1) {
//         return c + 0.5 * r * time;
//     } else {
//         return -(r + time);
//     }
// }

// // rotate all squares by 45 degrees
// // rotate all squares by 45 degrees
// function angleIt(r, c, time) {
//     const d = dist(r, c, 0, 0);
//     return d * 10 + time;
// }

// // rotate all squares by 45 degrees
// // rotate all squares by 45 degrees
// function angleIt(r, c, time) {
//     return Math.sin((r + time) / 300) * 360 - c;
// }

// // rotate all squares by 45 degrees
// function angleIt(r, c, time) {
//     return time - r + c;
// }

// // rotate all squares by 45 degrees
// function angleIt(r, c, time) {
//     return r * c;
// }

// // rotate all squares by 45 degrees
// function angleIt(r, c, time) {
//     return 5 * r;
// }

// // rotate all squares by 45 degrees
// function angleIt(r, c, time) {
//     return 35;
// }

//
// colorIt functions for (x, y, time)
//

// // color depends on distance from a cell along the diagonal, that changes over
// // time
// function colorIt(row, col, time) {
//     time /= 10;
//     // try commenting out the next line
//     time = map(Math.sin(time), -1, 1, 0, 9);

//     const x = Math.abs(row - time) % 10;
//     const y = Math.abs(col - time) % 10;
//     const d = dist(row, col, x, y);
//     const r = map(d, 0, 10, 0, 255);
//     return [r, 0, 255 - r];
// }

// // color depends on distance from a cell along the diagonal, that changes over
// // time
// function colorIt(row, col, time) {
//     time = time / 20;
//     // time = time % speed;
//     // const t = map(time, 0, speed, 0, 9);
//     const r = map(Math.abs(row - time) % 10 + Math.abs(col - time) % 10, 0, 18, 0, 255);
//     return [r, 0, 255 - r];
// }

// // pulsing
// function colorIt(row, col, time) {
//     const r = map(Math.sin(time / (row + col + 5)), -1, 1, 0, 255);
//     const g = map(Math.cos(time / (row + 10)), -1, 1, 0, 255);
//     const b = map(Math.sin(time / (col + 5)), -1, 1, 0, 255);
//     return [r, g, b, 255];
// }

//
// colorIt functions for (x, y)
//

// // an unexpected pattern
// function colorIt(row, col) {
//     if (Math.abs(row - col) % 10 === row) {
//         return [255, 0, 0];
//     }
// }

// // color depends on distance from (0, 0)
// function colorIt(row, col) {
//     const r = map(Math.abs(row) + Math.abs(col), 0, 18, 0, 255);
//     return [r, 0, 0, 255];
// }

// // checkerboard pattern
// function colorIt(r, c) {
//     if ((r + c) % 2 === 0) {
//         return [255, 0, 0, 255];
//     }
// }

// // alternating columns
// function colorIt(r, c) {
//     if (c % 2 === 0) {
//         return [255, 0, 0, 255];
//     }
// }

// // ring around the board
// function colorIt(r, c) {
//     if (r === 0 || r === 9 || c === 0 || c === 9) {
//         return [255, 0, 0, 255];
//     }
// }

// // just the 8th column
// function colorIt(r, c) {
//     if (c === 7) {
//         return [255, 0, 0, 255];
//     }
// }

// // just the 5th row
// function colorIt(r, c) {
//     if (r === 4) {
//         return [255, 0, 0, 255];
//     }
// }

// // diagonal from top right to bottom left
// function colorIt(r, c) {
//     if (r === 9 - c) {
//         return [255, 0, 0, 255];
//     }
// }

// // diagonal from top left to bottom right
// function colorIt(r, c, t) {
//     if (r === c) {
//         return [255, 0, 0];
//     }
// }

// // lower right triangle
// function colorIt(r, c) {
//     if (r > c) {
//         return [255, 0, 0];
//     }
// }

// // upper right triangle
// function colorIt(r, c) {
//     // console.log(`r: ${r}, c: ${c}, condition: ${r + c <= 9}`);
//     if (c === 2) {
//         return [255, 255, 0];
//     }
// }

// // all pixels the same color
// function colorIt(r, c) {
//     return [100, 50, 200];
// }

function updateAngleIt() {
    const editor = document.getElementById('function-editor');
    const functionBody = editor.value;
    try {
        // Create new function from the editor content
        angleIt = new Function('r', 'c', 'time', 
            `return (${functionBody})(r, c, time);`);
    } catch (error) {
        console.error('Error in function:', error);
        alert('Error in function: ' + error.message);
    }
}
