#!/usr/bin/env python

merge_cnt = 0


def merge_arrays(a1, a2):
    a = []
    i = 0
    j = 0
    a1_len = len(a1)
    a2_len = len(a2)
    while i < a1_len or j < a2_len:
        if i == a1_len:
            a.append(a2[j])
            j += 1
        elif j == a2_len:
            a.append(a1[i])
            i += 1
        elif a2[j] < a1[i]:
            a.append(a2[j])
            j += 1
        else:
            a.append(a1[i])
            i += 1
    print a
    return a


def merge_sort(a):
    if len(a) <= 1:
        print a
        return a
    res = merge_arrays(merge_sort(a[:len(a)/2]), merge_sort(a[len(a)/2:]))
    return res


def in_place_merge(a1, a2):
    n = sum(1 for x in a1 if x != 0)
    i = n - 1
    m = len(a2)
    j = m - 1
    x = m + n - 1
    while (i >= 0 or j >= 0) and x >= 0:
        if i < 0:
            a1[x] = a2[j]
            j -= 1
        elif j < 0:
            a1[x] = a1[i]
            i -= 1
        elif a1[i] > a2[j]:
            a1[x] = a1[i]
            i -= 1
        else:
            a1[x] = a2[j]
            j -= 1
        x -= 1
    return a1
