#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    # Write your code here
    # Apporch 1
    '''
    # wriiten on 11/06/2021
    # Time limit exceeded msg for test cases 8 & 9
    # Note : must reduce time complexity 
    # Read A Juggling Algorithm (https://www.geeksforgeeks.org/array-rotation/)
    def rot_left_by_unit(array,n):
        temp = array[0]
        for i in range(n-1):
            array[i] = array[i+1]
        array[n-1] = temp
    
    for move in range(d):
        rot_left_by_unit(a,len(a))
    return a
    '''
    # Apporch 2
    def rev_arr(arr):
        #print('arr:',arr)
        up_lim = len(arr)-1
        low_lim = 0
        while True:
            #print('limits: ',up_lim,low_lim)
            if up_lim == low_lim:
                break
            elif up_lim+1 == low_lim:
                break
            temp = arr[low_lim]
            arr[low_lim] = arr[up_lim]
            arr[up_lim] = temp
            up_lim -= 1
            low_lim += 1
        #print('rev array: ',arr)
        return arr
    first_half = a[:d]
    second_half = a[d:]
    rev_arr(first_half)
    rev_arr(second_half)
    res = first_half + second_half
    return rev_arr(res)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
