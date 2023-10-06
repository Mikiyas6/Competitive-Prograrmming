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
    n = len(arr)
    for i in range(n-1,0,-1):
        
        j = i - 1
        key = arr[i]
        
        while j >=0 and key < arr[j]:
            
            arr[j+1] = arr[j]
            j -= 1
            
            string = list(map(str,arr))
            print(" ".join(string))
            
        arr[j+1] = key
        
    string = list(map(str,arr))
    print(" ".join(string))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
