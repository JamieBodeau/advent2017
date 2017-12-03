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
        found = False
        
        for num1 in line:
            for num2 in line:
                if num1 == num2:
                    continue

                maxi = max(num1, num2)
                mini = min(num1, num2)
                
                if maxi % mini == 0:
                    found = True
                    quotient = maxi/mini
                    
            if found:
                break
        if not found:
            print "error"
        

        total += quotient
    print total
