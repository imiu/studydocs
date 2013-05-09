#!/usr/bin/env python
from random import shuffle


def partition(a, left_idx, right_idx):
    k = left_idx
    i = left_idx + 1
    j = right_idx
    while i <= j:
        if a[i] <= a[k]:
            i += 1
            continue
        elif a[j] >= a[k]:
            j -= 1
            continue
        else:
            a[i], a[j] = a[j], a[i]
    a[k], a[j] = a[j], a[k]
    return j


def quick_sort(a, left, right):
    if right <= left:
        return
    k = partition(a, left, right)
    print left, right, a
    quick_sort(a, left, k - 1)
    quick_sort(a, k + 1, right)


def quick_select(a, k):
    shuffle(a)
    left = 0
    right = len(a) - 1
    while left < right:
        j = partition(a, left, right)
        if j < k:
            left = j + 1
        elif j > k:
            right = j - 1
        else:
            return a[k]
    return a[k]
