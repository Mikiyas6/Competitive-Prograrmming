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
    counter = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j] < a[i] :
                counter += 1
                a[i], a[j] = a[j], a[i]
    
    print("Array is sorted in {} swaps.".format(counter))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))

    


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
