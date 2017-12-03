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

        distance = len(line)/2 
        count = 0
        for i in range(distance):
            if line[i] == line[i+distance]:
                count += int(line[i])
        print count*2
