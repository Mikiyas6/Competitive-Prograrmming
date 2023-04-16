#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
lists = []
def gradingStudents(grades):
    # Write your code here
    for each_score in grades:
        if (each_score < 38):
           lists.append(each_score)
        else:
            if(each_score %5 >= 3):
                lists.append((5 - each_score%5)+each_score) 
            else:
                lists.append(each_score)
    return lists

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
