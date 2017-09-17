# find the megapixel possibilities given an input total resolution

# 18 megapixels

from math import sqrt, ceil

match_mp = 18
max_iter = int(floor(sqrt(18)))
output = []
for i in xrange(0, match_mp+1):
    for j in xrange(0, max_iter+1):
        if floor(i*j) == match_mp:
            output.append((i, j))




00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18
01                                                     x
02                          x
03                 x
04




05
06
07
08
09
10
11
12
13
14
15
16
17
18
