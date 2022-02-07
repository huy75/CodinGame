#!/usr/bin/python3
# https://www.codingame.com/training/easy/temperatures
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temperatures = input().split()
tMin = -273
tMax = 5526
minT = 0 if len(temperatures) == 0 else int(temperatures[0])

for i in temperatures:
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if (t >= tMin and t <= tMax):
        if (t >= 0 and t <= abs(minT)):
            minT = t
        elif (t < 0):
            if abs(t) < abs(minT):
                minT = t
        
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(minT)

    