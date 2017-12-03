#!/usr/bin/env python
# Jamie Bodeau

# Imports -------------------------------------------------

import sys

# Classes -------------------------------------------------



# Functions -----------------------------------------------


# Main Execution ------------------------------------------

if __name__ == "__main__":
    total = 0
    for line in sys.stdin:
        line = map(int, line.split())
        maxi = max(line)
        mini = min(line)
        diff = maxi - mini

        total += diff
    print total
