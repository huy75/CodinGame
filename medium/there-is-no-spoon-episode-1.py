#!/usr/bin/python3
# https://www.codingame.com/training/medium/there-is-no-spoon-episode-1
import sys
import math

# Don't let the machines win. You are humanity's last hope...

# 0 < width ≤ 30 | 0 < height ≤ 30
# the number of cells on the X axis
# the number of cells on the Y axis
width, height = (int(input()), int(input()))

# A dot . represents an empty cell.
# A zero 0 represents a cell containing a node.
lines = [input() for i in range(height)]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for y in range(height):
    for x in range(width):
        if lines[y][x] == "0":
            # node
            rx = ry = bx = by = -1
            
            # right
            for x1 in range(x+1, width):
                if (lines[y][x1] == "0"):
                    rx = x1
                    ry = y
                    break

            # bottom
            for y1 in range(y+1, height):
                if lines[y1][x] == "0":
                    bx = x
                    by = y1
                    break  

            # Three coordinates: a node, its right neighbor, its bottom neighbor
            # If there is no neighbor, the coordinates should be -1 -1
            print(f"{x}, {y}, {rx}, {ry}, {bx}, {by}")