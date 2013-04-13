#!/usr/bin/env python
from threesum import threesum_n3, threesum_n2
import pytest


@pytest.fixture
def arr():
    return [30, -40, -20, -10, 40, 0, 10, 5]


class TestThreesum(object):
    def test_n3(self, arr):
        assert 8 == len(threesum_n3(arr))

    def test_n2(self, arr):
        assert 8 == len(threesum_n2(arr))
