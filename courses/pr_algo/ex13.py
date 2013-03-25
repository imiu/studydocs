#!/usr/bin/env python
from __future__ import print_function
import operator
# from linked_list import LinkedList


class Ex13(object):
    def math_evaluator(self, string):
        result = 0
        op_dict = {'+': operator.add, '-': operator.sub,
                   '*': operator.mul, '/': operator.div}
        opn_stack = []
        opr_stack = []
        for s in string:
            if s in ('+', '*', '/', '-'):
                opr_stack.append(s)
            elif s == '(':
                pass
            elif s == ')':
                op = opr_stack.pop()
                last_opn = opn_stack.pop()
                first_opn = opn_stack.pop()
                result = op_dict[op](first_opn, last_opn)
                opn_stack.append(result)
            else:
                opn_stack.append(int(s))
        return opn_stack.pop()

    def e3(self, string):
        brackets = []
        bracket_pair = {'(': ')', '{': '}', '[': ']'}
        for bracket in string:
            if bracket in bracket_pair:
                brackets.append(bracket)
            else:
                try:
                    stack_bracket = brackets.pop()
                except IndexError:
                    return False
                if (bracket_pair[stack_bracket] != bracket):
                    return False
        return True

    def e37(self, n, m):
        lst = list(range(n))
        while len(lst) > 1:
            for i in range(m - 1):
                lst.append(lst.pop(0))
            lst.pop(0)
        return lst[0]

    def e37_2(self, ln, skip):
        ls = range(ln)
        skip -= 1  # pop automatically skips the dead guy
        idx = skip
        while len(ls) > 1:
            print(ls.pop(idx))  # kill prisoner at idx
            idx = (idx + skip) % len(ls)
        print('survivor: ', ls[0])
        return ls[0]
