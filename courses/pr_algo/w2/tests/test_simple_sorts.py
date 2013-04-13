#!/usr/bin/env python
from simple_sorts import selection_sort, insertion_sort
import pytest


@pytest.fixture
def ar_unsorted():
    return [0, 9, 3, 5, 2, 3, 15, 27, 7, 33, 1, 13, 15]


@pytest.fixture
def ar_repetitive():
    return [0, 9, 1, 5, 2, 3, 15, 15, 7, 33, 1, 13, 9]


@pytest.fixture
def ar_sorted():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def pytest_generate_tests(metafunc):
    funcarglist = metafunc.cls.params
    argnames = list(funcarglist[0])
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames]
                                    for funcargs in funcarglist])


class TestSorts(object):
    params = [dict(func=selection_sort),
              dict(func=insertion_sort)]

    def test_unsorted(self, func, ar_unsorted):
        result = sorted(ar_unsorted)
        assert result == func(ar_unsorted)

    def test_repetitive(self, func, ar_repetitive):
        result = sorted(ar_repetitive)
        assert result == func(ar_repetitive)

    def test_sorted(self, func, ar_sorted):
        assert ar_sorted == func(ar_sorted)
