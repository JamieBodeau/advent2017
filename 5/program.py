#!/usr/bin/env python
# Jamie Bodeau

# Imports -------------------------------------------------

import sys

# Classes -------------------------------------------------



# Functions -----------------------------------------------



# Main Execution ------------------------------------------

if __name__ == "__main__":
    nums = []
    for line in sys.stdin:
        for num in line.split():
            nums.append(int(num))

    index = 0;
    steps = 0;
    while index >= 0 and index < len(nums):
        if nums[index] >= 3:
            nums[index] -= 1
            index += nums[index] + 1
        else:
            nums[index] += 1
            index += nums[index] - 1


        steps += 1

    print steps
