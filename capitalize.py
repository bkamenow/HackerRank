#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    rng = s.split(' ')
    res = ''
    for i in rng:
        i = i.capitalize()
        res = res + i + ' '
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
