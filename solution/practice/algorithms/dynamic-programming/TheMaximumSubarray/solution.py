#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    sub_array_sum = -sys.maxsize
    sub_sequ_sum = arr[0]
    current_sum=0    
    
    for i in arr:
        current_sum += i
        if sub_array_sum < current_sum:
            sub_array_sum = current_sum
        if current_sum < 0:
            current_sum=0
    for i in range(1, len(arr)):
        if arr[i] > 0 and sub_sequ_sum >= 0 :
            sub_sequ_sum += arr[i]
        elif sub_sequ_sum < 0 and sub_sequ_sum < arr[i]:
            sub_sequ_sum = arr[i]
    return [sub_array_sum,sub_sequ_sum]

    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
