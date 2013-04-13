#!/usr/bin/env python
from __future__ import print_function
import pytest
from ex11 import Ex11


@pytest.fixture
def ex():
    return Ex11()


class TestEx1(object):

    def test_e6(self, ex):
        assert 1 == ex.e6(1)
        assert 55 == ex.e6(10)

    def test_e11(self, ex):
        assert "*  *\n" == ex.e11([[True, False, False, True]])
        assert ("*  *\n ** \n" == ex.e11([[True, False, False, True],
                                          [False, True, True, False]]))

    def test_e13(self, ex):
        assert [[1, 4], [2, 5], [3, 6]] == ex.e13([[1, 2, 3], [4, 5, 6]])

    def test_e15(self, ex):
        assert [0, 2, 0, 1] == ex.e15([1, 3, 1])
        assert [1, 1, 2] == ex.e15([2, 0, 1, 2])

    def test_e18(self, ex):
        assert 20 == ex.e18(4, 5)
        assert 40 == ex.e18(5, 8)

    def test_gcd(self, ex):
        assert 4 == ex.gcd(16, 20)
        assert 1 == ex.gcd(9, 2)

    def test_bs(self, ex):
        assert 0 == ex.bs(0, [0])
        assert 2 == ex.bs(3, [0, 1, 3, 5, 7])

    def test_e30(self, ex):
        assert True == (ex.e30(10))[5][7]
        assert True == (ex.e30(10))[7][9]
        assert False == (ex.e30(10))[3][9]
