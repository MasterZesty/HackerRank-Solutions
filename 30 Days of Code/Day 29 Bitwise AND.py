#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    '''
    #my logic exceeds time limit
    max_val = 0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            #print(i,j)
            bitwise_and = i&j
            #print('bitwise_and:',bitwise_and,'K:',K)
            if bitwise_and < K:
                if bitwise_and > max_val:
                    max_val = bitwise_and
    #print('---------------------')
    #print('max_val:',max_val)
    return max_val
    '''
    return(K-1 if ((K-1) | K) <= N else K-2)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
