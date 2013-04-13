#!/usr/bin/env python
from binary_search import binary_search
import pytest


@pytest.fixture
def arr():
    return [1, 4, 7, 11, 24, 38, 55, 87, 91]


class TestBinarySearch(object):
    def test_existing_value(self, arr):
        assert arr.index(4) == binary_search(arr, 4)

    def test_nonexisting_value(self, arr):
        assert -1 == binary_search(arr, 25)

    def test_boundaries(self, arr):
        assert arr.index(1) == binary_search(arr, 1)
        assert arr.index(91) == binary_search(arr, 91)
