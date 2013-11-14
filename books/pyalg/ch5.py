#! /usr/bin/env python
# -*- coding: utf-8
from ch5 import dfs
import pytest


@pytest.fixture
def g():
    return {'a': ['b', 'c', 'f', 'e', 'd'],
            'b': ['c', 'e'],
            'c': ['d'],
            'd': ['e'],
            'e': ['f'],
            'f': ['c', 'g', 'h'],
            'g': ['f', 'h'],
            'h': ['f', 'g']}


class TestCh5(object):
    def test_dfs(self, g):
        assert ['a', 'f', 'h', 'g', 'c', 'd', 'e', 'b'] == dfs(g, 'a')
