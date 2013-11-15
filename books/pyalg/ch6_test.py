#! /usr/bin/env python
# -*- coding: utf-8
from ch6 import skyline


class TestCh6(object):
    def test_skyline_one(self):
        inp = [(1, 11, 5), (2, 6, 7)]
        assert [(1, 11), (5, 6), (7, 0)] == skyline(inp)

    def test_skyline_one_and_a_half(self):
        inp = [(1, 11, 5), (2, 6, 7), (3, 13, 9)]
        assert [(1, 11), (3, 13), (9, 0)] == skyline(inp)

    def test_skyline_two(self):
        inp = [(1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16)]
        assert [(1, 11), (3, 13), (9, 0), (12, 7), (16, 0)] == skyline(inp)

    def test_skyline(self):
        inp = [(1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16), (14, 3, 25),
               (19, 18, 22), (23, 13, 29), (24, 4, 28)]
        assert [(1, 11), (3, 13), (9, 0), (12, 7), (16, 3), (19, 18), (22, 3),
                (23, 13), (29, 0)] == skyline(inp)
