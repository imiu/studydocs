#!/usr/bin/env python
from __future__ import print_function
from ex14 import Ex14


class TestEx14(object):
    def setup_method(self, method):
        self.ex = Ex14()

    def test_e12(self):
        arr1 = [1, 2]
        arr2 = [1, 2, 3]
        assert [1, 2] == self.ex.e12(arr1, arr2)
        arr1 = [1, 2, 5, 8, 15, 32, 47, 48, 59]
        arr2 = [1, 3, 5, 6, 7, 8, 11, 15, 48]
        assert [1, 5, 8, 15, 48] == self.ex.e12(arr1, arr2)
