#! /usr/bin/env python
# -*- coding: utf-8
from recursion import str_reverse, is_palindrome


def test_reverse():
    test_str = 'abc'
    assert 'cba' == str_reverse(test_str)


def test_is_palindrome():
    false_test_str = 'abc'
    assert False == is_palindrome(false_test_str)
    true_test_str_0 = 'abba'
    assert True == is_palindrome(true_test_str_0)
    true_test_str_1 = 'abcba'
    assert True == is_palindrome(true_test_str_1)
