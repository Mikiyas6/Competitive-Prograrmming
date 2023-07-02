#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    value = arr[-1]
    arr.pop()
    for i in range(n-2,-1,-1): 
        if value < arr[i]:
            arr.insert(i+1,arr[i])
            print(" ".join(str(x) for x in arr))
            arr.pop(i)
            if i == 0:
                arr.insert(i,value)
                print(" ".join(str(x) for x in arr))
                break
        else:
            arr.insert(i+1,value)
            print(" ".join(str(x) for x in arr))
            break
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
