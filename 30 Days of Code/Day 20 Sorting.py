#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    num_swaps = 0
    for i in range(len(a)-1,0,-1):
        
        for j in range(i):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                num_swaps+=1
    print('Array is sorted in %d swaps.'%num_swaps)
    print('First Element:',a[0])
    print('Last Element:',a[-1])
        
