#!/usr/bin/python3
# https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()] # starting position

maxX = w
minX = 0
maxY = 0
minY = h

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if (bomb_dir == "U" ):
        minY = y0
        y0 = (minY + maxY)/2
        
    if (bomb_dir == "UR" ):
        minX = x0
        x0 = (minX + maxX)/2
        minY = y0
        y0 = (minY + maxY)/2

    if (bomb_dir == "R" ):
        minX = x0
        x0 = (minX + maxX)/2

    if (bomb_dir == "DR" ):
        minX = x0
        x0 = (minX + maxX)/2
        maxY = y0
        y0 = (minY + maxY)/2

    if (bomb_dir == "D" ):
        maxY = y0
        y0 = (minY + maxY)/2

    if (bomb_dir == "DL" ):
        maxX = x0
        x0 = (minX + maxX)/2
        maxY = y0
        y0 = (minY + maxY)/2

    if (bomb_dir == "L" ):
        maxX = x0
        x0 = (minX + maxX)/2

    if (bomb_dir == "UL" ):
        maxX = x0
        x0 = (minX + maxX)/2
        minY = y0
        y0 = (minY + maxY)/2

    # the location of the next window Batman should jump to.
    print(f"{str(int(x0))} {str(int(y0))}")