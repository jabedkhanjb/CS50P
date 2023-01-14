#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
# 0<n<2 * 10**5

def fizzBuzz(n):
    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
            continue
        elif i%3 ==0 and i%5 != 0:
            print("Fizz")
            continue
        elif i%5 == 0 and i%3 != 0:
            print("Buzz")
            continue
        elif i%3 != 0 and i%5 != 0:
            print(i)
            continue
    return None

if __name__ == '__main__':
    
    n = int(input().strip())

    fizzBuzz(n)
