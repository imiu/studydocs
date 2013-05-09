#!/usr/bin/env python
from merge_sort import merge_arrays, merge_sort, in_place_merge


class TestMergeArrays(object):
    def test_unique(self):
        a1 = [1, 3, 5]
        a2 = [2, 4, 6]
        assert [1, 2, 3, 4, 5, 6] == merge_arrays(a1, a2)

    def test_repetitive(self):
        a1 = [2, 6, 8, 13, 13]
        a2 = [1, 2, 8, 12, 13]
        assert [1, 2, 2, 6, 8, 8, 12, 13, 13, 13] == merge_arrays(a1, a2)

    def test_small(self):
        a1 = [1]
        a2 = [2]
        assert [1, 2] == merge_arrays(a1, a2)


class TestMergeSort(object):
    def test_unique(self):
        a = [2, 1, 6, 9, 7, 5, 4]
        assert [1, 2, 4, 5, 6, 7, 9] == merge_sort(a)

    def test_repetitive(self):
        a = [3, 2, 6, 3, 5, 1, 8]
        assert [1, 2, 3, 3, 5, 6, 8] == merge_sort(a)

    def test_7th(self):
        a = ['92', '54', '23', '64', '37', '74',
             '28', '95', '78', '84', '82', '80']
        merge_sort(a)


class TestInPlaceMerge(object):
    def test_merge(self):
        a1 = [2, 4, 6, 0, 0, 0, 0]
        a2 = [1, 3, 5, 7]
        assert [1, 2, 3, 4, 5, 6, 7] == in_place_merge(a1, a2)
