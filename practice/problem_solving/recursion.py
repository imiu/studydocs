#! /usr/bin/env python
# -*- coding: utf-8


def str_reverse(string):
    if len(string) == 1:
        return string
    return string[-1:] + str_reverse(string[:-1])


def is_palindrome(string):
    if len(string) <= 1:
        return True
    return (string[0] == string[-1]) and is_palindrome(string[1:-1])


