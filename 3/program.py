#!/usr/bin/env python
# Jamie Bodeau

# Imports -------------------------------------------------

import sys
import math

# Classes -------------------------------------------------



# Functions -----------------------------------------------

def getLevel(n):
    square = int(math.ceil(n**0.5))

    if square % 2 == 0:
        square += 1

    level = (square - 1) / 2
    return level 

def getRoot(level):
    return level * 2 + 1

def getCorners(level):
    root   = getRoot(level)
    square = root**2
    
    corners = [square]

    for i in range(3):
        corners.append(corners[-1] - level*2)

    return corners

# Main Execution ------------------------------------------

if __name__ == "__main__":
    for num in map(int, sys.stdin):
        level = getLevel(num)
        corners = getCorners(level)
        
        corners = [corner - level for corner in corners]
        distanceFromClosest = min([abs(num-corner) for corner in corners])

        distance = distanceFromClosest + level

        print distance


