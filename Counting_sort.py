#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    lists = [0] * (100)
    for i in range(len(arr)):
        lists[arr[i]] += 1
    # print(lists)
    listo = []
    for i in range(len(lists)):
        if i == 0:
            listo.append(lists[i])
        else:
            listo.append(lists[i]+listo[-1])
    # print(listo)
    listings = [0] * (len(arr))
    # print(listings)
    for i in range(len(arr)):
        listings[listo[arr[i]]-1] = arr[i]
        listo[arr[i]] = listo[arr[i]] - 1
    # print(listings)
    return lists

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
