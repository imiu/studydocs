#!/usr/bin/env python
from __future__ import print_function
from ex11 import Ex11


class TestEx1(object):
    def setup_method(self, method):
        self.ex = Ex11()

    def test_e6(self):
        assert 1 == self.ex.e6(1)
        assert 55 == self.ex.e6(10)

    def test_e11(self):
        assert "*  *\n" == self.ex.e11([[True, False, False, True]])
        assert ("*  *\n ** \n" == self.ex.e11([[True, False, False, True],
                                               [False, True, True, False]]))

    def test_e13(self):
        assert [[1, 4], [2, 5], [3, 6]] == self.ex.e13([[1, 2, 3], [4, 5, 6]])

    def test_e15(self):
        assert [0, 2, 0, 1] == self.ex.e15([1, 3, 1])
        assert [1, 1, 2] == self.ex.e15([2, 0, 1, 2])

    def test_e18(self):
        assert 20 == self.ex.e18(4, 5)
        assert 40 == self.ex.e18(5, 8)

    def test_gcd(self):
        assert 4 == self.ex.gcd(16, 20)
        assert 1 == self.ex.gcd(9, 2)

    def test_bs(self):
        assert 0 == self.ex.bs(0, [0])
        assert 2 == self.ex.bs(3, [0, 1, 3, 5, 7])

    def test_e30(self):
        assert True == (self.ex.e30(10))[5][7]
        assert True == (self.ex.e30(10))[7][9]
        assert False == (self.ex.e30(10))[3][9]
