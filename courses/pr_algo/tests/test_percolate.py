#!/usr/bin/env python
from __future__ import print_function
from percolate import Percolation


class TestPercolation(object):
    def setup_method(self, method):
        pass

    def test_init(self):
        p = Percolation(3)
        p.print_perc_arr()
        assert [9, 9, 9, 3, 4, 5, 10, 10, 10, 9, 10] == p.get_perc_arr()

    def test_open(self):
        p = Percolation(3)
        p.open_(0, 2)
        p.open_(1, 2)
        p.open_(2, 2)
        assert True == p.is_percolative()
        p = Percolation(3)
        p.open_(0, 2)
        p.open_(1, 2)
        p.open_(1, 1)
        p.open_(2, 1)
        assert True == p.is_percolative()
        p = Percolation(3)
        p.open_(0, 0)
        p.open_(1, 1)
        p.open_(1, 2)
        p.open_(1, 0)
        p.open_(2, 2)
        assert True == p.is_percolative()
