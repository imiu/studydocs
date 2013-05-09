#!/usr/bin/env python
from random import shuffle
from quick_sort import quick_sort, quick_select


class TestQuickSort(object):
    def test_unique(self):
        a = [2, 6, 4, 5, 1, 3]
        shuffle(a)
        quick_sort(a, 0, len(a) - 1)
        assert [1, 2, 3, 4, 5, 6] == a

    def test_repetitive(self):
        a = ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A']
        # shuffle(a)
        quick_sort(a, 0, len(a) - 1)
        assert False


class TestQuickSelect(object):
    def test_quick_select(self):
        a = [2, 6, 4, 5, 1, 3]
        assert 3 == quick_select(a, 2)
