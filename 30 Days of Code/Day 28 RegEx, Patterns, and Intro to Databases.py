#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    data = list()
    regex_s = '@gmail.com$'
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        x = re.findall(regex_s, emailID)
        if x:
            data.append(firstName)
    data = sorted(data)
    print(*data,sep='\n')
    
