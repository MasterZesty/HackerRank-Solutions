#!/bin/python3

import math
import os
import random
import re
import sys

def countHourglass(arr, i, j):
    hg = 0
    hg += arr[i][j]
    hg += arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
    hg += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
    return hg
   
def getMaxHourglass(arr):
    maxHg = -999999
    for i in range(1, 5):
        for j in range(1, 5):
            hg = countHourglass(arr, i, j)
            maxHg = hg if hg > maxHg else maxHg
    return maxHg

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    #print(arr)
    print(getMaxHourglass(arr))
