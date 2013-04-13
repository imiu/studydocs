#!/usr/bin/env python

import math


def xy_ratio(val, prev_val):
    return val / prev_val


def log_ratio(pairs):
    print pairs
    ratio = []
    prev = pairs.pop(0)
    for pair in pairs:
        print pair
        base = xy_ratio(pair[0], prev[0])
        dx = math.log(pair[0], base) - math.log(prev[0], base)
        dy = math.log(pair[1], base) - math.log(prev[1], base)
        ratio.append(dy / dx)
        prev = pair
    return ratio

x = (1296, 7776, 46656)
y = (0.19, 20.96, 2286.26)

pairs = zip(x, y)
print log_ratio(pairs)
