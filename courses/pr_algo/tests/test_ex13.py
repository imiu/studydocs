#!/usr/bin/env python
from __future__ import print_function
from ex13 import Ex13


class TestEx13(object):
    def setup_method(self, method):
        self.ex = Ex13()

    def setup(self):
        self.ex = Ex13()

    def test_math_evaluator(self):
        assert True == (1 / 0)
        assert 2 == self.ex.math_evaluator("(1+1)")
        assert 12 == self.ex.math_evaluator("((((1+1)-1)+5)*2)")
        assert 2 == self.ex.math_evaluator("(((((1+1)-1)+5)*2)/6)")

    def test_e3(self):
        assert True == self.ex.e3("()")
        assert False == self.ex.e3("()}")
        assert True == self.ex.e3("[()]{}{[()()]()}")

    def test_e37(self):
        assert 3 == self.ex.e37(7, 3)
        assert 6 == self.ex.e37(7, 2)

    def test_e37_2(self):
        assert 3 == self.ex.e37_2(7, 3)
        assert 6 == self.ex.e37_2(7, 2)
