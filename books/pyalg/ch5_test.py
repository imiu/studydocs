#! /usr/bin/env python
# -*- coding: utf-8
from ch5 import top_sort, bfs
import pytest


@pytest.fixture
def graph():
    return {0: [1, 2, 5],
            1: [4],
            2: [],
            3: [2, 4, 5, 6],
            4: [],
            5: [2],
            6: [0, 4]}


class TestCh5(object):
    def test_top_sort(self, graph):
        assert [3, 6, 0, 5, 2, 1, 4] == top_sort(graph)

    def test_bfs(self, graph):
        assert [0, 1, 4] == bfs(graph, 0, 4)
