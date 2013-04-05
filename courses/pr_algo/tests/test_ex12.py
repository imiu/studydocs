#!/usr/bin/env python
from __future__ import print_function
from ex12 import Ex12


class TestEx12(object):
    def setup_method(self, method):
        self.ex = Ex12()

    def setup(self):
        self.ex = Ex12()

    def test_is_palindrome(self):
        assert False == self.ex.is_palindrome("aaz")
        assert True == self.ex.is_palindrome("abba")

    def test_is_circular_rotation(self):
        assert True == self.ex.is_circular_rotation("ACTGACG", "TGACGAC")
        assert False == self.ex.is_circular_rotation("ACTGACG", "GGACGAC")
