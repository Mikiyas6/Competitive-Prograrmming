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
        for j in range(len(a)):
            if j == len(a) - i -1:
                break
            elif (a[j+1] < a[j]):
                counter += 1
                swap(a,j,j+1)
    print("Array is sorted in "+str(counter)+" swaps.")
    print("First Element: "+ str(a[0]))
    print("Last Element: " + str(a[-1]))
def swap(a,x,y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp
    


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
