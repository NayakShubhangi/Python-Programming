#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    f = [0, 0, 0, 0, 0, 0]
    for bird_id in arr:
        f[bird_id] += 1
    max_freq = 0
    max_id = 1
    for i in range(1, 6):
        if f[i] > max_freq:
            max_freq = f[i]
            max_id = i
    return max_id

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()