#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    
    prefix_sum = [0] * (n+1)
    
    for l,r,value in queries:
        
        prefix_sum[l-1] += value
        prefix_sum[r] -= value
    
    prefix_sum = prefix_sum[:n]
    cumulative = 0
    max_value = 0
    
    for value in prefix_sum:
        
        cumulative += value
        max_value = max(max_value,cumulative)
    
    return max_value
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
