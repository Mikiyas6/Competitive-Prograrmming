#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    # Array is sorted in 3 swaps.
    # First Element: 1
    # Last Element: 3
    
    n = len(a)
    counter = 0
    for i in range(n):
        
        swapped = False
        
        for j in range(0,n-i-1):
            if a[j+1] < a[j]:
                counter += 1
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        
        if not swapped:
            break
        
    print("Array is sorted in {} swaps.".format(counter))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
        
    
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
