#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, inp):
    out = n
    curr_i = 0
    while curr_i < n:
        factorial_count = 0
        next_i = curr_i + 1
        if next_i >= n:
            break
        if next_i < n and inp[curr_i] == inp[next_i]:
            # strings like aa aaaa fall here
            while next_i < n and inp[curr_i] == inp[next_i]:
                factorial_count += 1
                next_i += 1
            # we already count every single letter on exit
            while factorial_count > 0:
                # aaaa = 4+3+2+1 = 10
                # aaaaa = 5+4+3+2+1 = 15
                out += factorial_count
                factorial_count -= 1
            # import pdb; pdb.set_trace()
            curr_i = next_i
        else:
            prev_i = curr_i - 1
            if prev_i < 0 or prev_i == curr_i:
                curr_i += 1
                continue
            elif (
                prev_i >= 0 and
                inp[prev_i] == inp[next_i] and
                inp[curr_i] != inp[prev_i]
            ):
                # import pdb; pdb.set_trace()
                mirrored_char = inp[next_i]
                while (
                    next_i < n and prev_i >= 0 and
                    inp[prev_i] == inp[next_i] and
                    inp[prev_i] == mirrored_char
                ):
                    # aba aabaa aaabaaa
                    # the lefthand side of the mirrored string is counted
                    out += 1
                    prev_i -= 1
                    next_i += 1
            curr_i += 1
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
