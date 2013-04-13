#!/usr/bin/env python


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
    i = 0
    while i < len(arr):
        for j in range(i, len(arr)):
            min_idx = i
            if arr[j] < arr[min_idx]:
                min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        i += 1
    return arr


def insertion_sort(arr):
    i = j = 0
    while i < len(arr):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j += 1
        i += 1
    return arr
