#!/usr/bin/env python
from __future__ import print_function


class Ex14(object):
    def e12(self, arr1, arr2):
        result = []
        idx1 = 0
        idx2 = 0
        while True:
            if arr1[idx1] == arr2[idx2]:
                result.append(arr1[idx1])
                idx1 += 1
                idx2 += 1
            elif arr1[idx1] > arr2[idx2]:
                idx2 += 1
            elif arr1[idx1] < arr2[idx2]:
                idx1 += 1

            if idx1 == len(arr1) or idx2 == len(arr2):
                break
        return result
