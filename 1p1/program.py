#!/usr/bin/env python
# Jamie Bodeau

# Imports -------------------------------------------------

import sys

# Classes -------------------------------------------------



# Functions -----------------------------------------------

# Main Execution ------------------------------------------

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()

        lastChar = line[-1]
        
        count = 0
        for char in line:
            if char == lastChar:
                count += int(char)
            lastChar = char
        print count
