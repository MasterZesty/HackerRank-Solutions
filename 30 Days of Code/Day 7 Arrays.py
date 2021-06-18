#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    out = ''
    for i in range(len(arr)-1,-1,-1):
        #print(arr[i])
        out += str(arr[i]) + ' '
    print(out)
