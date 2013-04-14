#!/usr/bin/env python
import random


# moar pythonic approach
def selection_sort_pythonic(arr):
    a = arr[:]
    result = []
    idx = 0
    while len(a):
        min_elm = a[idx]
        for tmp_elm in a:
            if tmp_elm < min_elm:
                min_elm = tmp_elm
        result.append(min_elm)
        a.remove(min_elm)
    return result


# classic approach
def selection_sort(arr):
    a = arr[:]
    i = 0
    while i < len(a):
        min_idx = i
        for j in range(i, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        i += 1
    return a


def insertion_sort(arr):
    a = arr[:]
    i = j = 0
    while i < len(a):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j - 1], a[j] = a[j], a[j - 1]
            j += 1
        i += 1
    return a


def shell_sort(arr):
    a = arr[:]
    h = 1
    n = len(a)
    while h < n / 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, n):
            for j in range(i, h - 1, (- h)):
                if a[j] < a[j - h]:
                    a[j], a[j - h] = a[j - h], a[j]
        h = h / 3
        print a
    return a


def knuth_shuffle(arr):
    a = arr[:]
    for idx in range(0, len(a)):
        r = random.randint(0, idx + 1)
        a[idx], a[r] = a[r], a[idx]
    return a
