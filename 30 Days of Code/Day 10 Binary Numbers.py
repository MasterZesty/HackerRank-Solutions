#!/bin/python3

import math
import os
import random
import re
import sys


def dec_to_base(num,base):  #Maximum base - 36
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters
        num //= base
    base_num = base_num[::-1]  #To reverse the string
    return base_num


    
if __name__ == '__main__':
    n = int(input().strip())
    base_no = dec_to_base(n,2)
    print(max(map(len,base_no.split('0'))))
