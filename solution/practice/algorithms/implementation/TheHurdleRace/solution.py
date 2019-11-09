#!/bin/python3

import sys

def hurdleRace(k, height):
    temp = max(height)-k 
    if (temp > 0):
        return temp
    else:
        return 0
    
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
