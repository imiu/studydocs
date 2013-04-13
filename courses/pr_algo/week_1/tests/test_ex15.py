#!/usr/bin/env python
from __future__ import print_function
from ex15 import UfQf
from ex15 import UfQu
from ex15 import UfWqu


class TestUF(object):
    def setup_method(self, method):
        pass

    def test_ufqf(self):
        uf = UfQf(10)
        uf.union(9, 0)
        uf.union(3, 4)
        uf.union(5, 8)
        uf.union(7, 2)
        uf.union(2, 1)
        uf.union(5, 7)
        uf.union(0, 3)
        uf.union(4, 2)
        assert [1, 1, 1, 1, 1, 1, 6, 1, 1, 1] == uf.ids

    def test_ufqf2(self):
        # 5-0 1-9 5-3 8-3 5-2 7-5
        uf = UfQf(10)
        uf.union(5, 0)
        uf.union(1, 9)
        uf.union(5, 3)
        uf.union(8, 3)
        uf.union(5, 2)
        uf.union(7, 5)
        assert [2, 9, 2, 2, 4, 2, 6, 2, 2, 9] == uf.ids

    def test_ufqu(self):
        uf = UfQu(10)
        uf.union(9, 0)
        uf.union(3, 4)
        uf.union(5, 8)
        uf.union(7, 2)
        uf.union(2, 1)
        uf.union(5, 7)
        uf.union(0, 3)
        uf.union(4, 2)
        assert [4, 1, 1, 4, 1, 8, 6, 2, 1, 0] == uf.ids

    def test_ufwqu(self):
        uf = UfWqu(10)
        uf.union(9, 0)
        uf.union(3, 4)
        uf.union(5, 8)
        uf.union(7, 2)
        uf.union(2, 1)
        uf.union(5, 7)
        uf.union(0, 3)
        uf.union(4, 2)
        assert [9, 7, 7, 9, 3, 7, 6, 7, 5, 7] == uf.ids

    def test_ufwqu2(self):
        # 1-9 4-3 3-9 7-5 0-5 5-2 0-9 3-8 4-6
        uf = UfWqu(10)
        uf.union(1, 9)
        uf.union(4, 3)
        uf.union(3, 9)
        uf.union(7, 5)
        uf.union(0, 5)
        uf.union(5, 2)
        uf.union(0, 9)
        uf.union(3, 8)
        uf.union(4, 6)
        assert [7, 4, 7, 4, 7, 7, 7, 7, 7, 1] == uf.ids
