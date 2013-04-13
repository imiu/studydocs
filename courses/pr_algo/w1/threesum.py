#!/usr/bin/env python
from binary_search import binary_search as bsearch


def threesum_n3(arr):
    sums = set()
    for i in arr:
        for j in arr:
            for k in arr:
                if i + j + k == 0:
                    print i, j, k
                    sums.add(tuple(sorted([i, j, k])))
    return sums


def threesum_n2(arr):
    sums = set()
    arr.sort()
    for i in arr:
        for j in arr:
            k = bsearch(arr, - (i + j))
            if k != -1:
                sums.add(tuple(sorted([i, j, arr[k]])))
    print sums
    return sums
