#!/usr/bin/env python
# Jamie Bodeau

# Imports -------------------------------------------------

import sys

# Classes -------------------------------------------------



# Functions -----------------------------------------------



# Main Execution ------------------------------------------

if __name__ == "__main__":
    # Track how many valid we have
    numValid = 0

    # Read input
    for words in map(str.split, sys.stdin):
        # No duplicates if the set is the same length
        words = ["".join(sorted(word)) for word in words]
        if len(set(words)) == len(words):
            numValid += 1
    
    # Output
    print numValid



