#!/usr/bin/env python
from __future__ import print_function


class Ex12(object):
    def is_palindrome(self, word):
        # return word == word[::-1]
        if len(word) == 0 or len(word) == 1:
            return True
        if word[0] != word[-1]:
            return False
        return self.is_palindrome(word[1:-1])

    def is_circular_rotation(self, word, phrase):
        if word in (phrase + phrase):
            return True
        return False
