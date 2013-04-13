#!/usr/bin/env python


def binary_search(arr, key):
    lo = 0
    hi = len(arr) - 1
    while (lo <= hi):
        mid = lo + (hi - lo) / 2
        if key < arr[mid]:
            hi = mid - 1
        elif key > arr[mid]:
            lo = mid + 1
        else:
            return mid
    return -1
