#!/usr/bin/env python
# Jamie Bodeau

# Imports -------------------------------------------------

import sys

# Classes -------------------------------------------------



# Functions -----------------------------------------------

def getKey(banks):
    return ",".join(map(str, banks))

def reallocate(banks):
    # Find max
    maxIndex = 0
    maxi = -1
    for index, num in enumerate(banks):
        if num > maxi:
            maxi = num
            maxIndex = index

    # Reset the one that had the most
    banks[maxIndex] = 0

    # Redistribute
    index = (maxIndex + 1) % len(banks)
    for i in range(maxi):
        # 
        #print "Putting one in {}".format(index)
        banks[index] += 1

        # Loop
        index += 1
        index = index % len(banks)


# Main Execution ------------------------------------------

Version = 2

if __name__ == "__main__":
    for line in sys.stdin:
        # Get input
        banks = []
        for word in line.split():
            banks.append(int(word))
        
        # State variables
        repeated = False
        pastStates = {}

        # Loop until we repeated state
        timesReallocated = 0
        while not repeated:
            # Check for repeat/record state
            key = getKey(banks)
            print key
            if key in pastStates:
                repeated = True
                break
            else:
                pastStates[key] = timesReallocated
            
            # Process this iteration
            reallocate(banks)
            timesReallocated += 1

        # Result
        if Version == 1:
            print timesReallocated
        elif Version == 2:
            print timesReallocated - pastStates[key]





