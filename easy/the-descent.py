#!/usr/bin/python3
# https://www.codingame.com/training/easy/the-descent
import sys
import math



# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# game loop
while True:
    mounts = []
    for i in range(8):
        mounts.append(int(input()))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    print(mounts.index(max(mounts)))