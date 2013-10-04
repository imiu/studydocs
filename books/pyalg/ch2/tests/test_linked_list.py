#! /usr/bin/env python
# -*- coding: utf-8
from linked_list import LinkedList
import pytest


@pytest.fixture
def ll():
    return LinkedList()


class TestLinkedList(object):

    def test_add(self, ll):
        ll.add(1, 2, 3)
        assert [3, 2, 1] == ll.as_list()
        assert 3 == ll.head.data
        assert 1 == ll.tail.data

    def test_length(self, ll):
        ll.add(1, 2, 3)
        assert 3 == ll.length()

    def test_search(self, ll):
        ll.add(1, 2, 3)
        assert False == ll.search(4)
        assert True == ll.search(3)

    def test_remove(self, ll):
        ll.add(1, 2, 3, 4, 5)
        assert False == ll.remove(7)
        assert 1 == ll.tail.data
        assert 5 == ll.head.data
        ll.remove(2)
        assert [5, 4, 3, 1] == ll.as_list()
        assert 5 == ll.head.data
        assert 1 == ll.tail.data
        ll.remove(1)
        assert [5, 4, 3] == ll.as_list()
        assert 5 == ll.head.data
        assert 3 == ll.tail.data
        ll.remove(5)
        assert [4, 3] == ll.as_list()
        assert 4 == ll.head.data
        assert 3 == ll.tail.data
        ll.remove(4)
        assert [3] == ll.as_list()
        assert 3 == ll.head.data
        assert 3 == ll.tail.data

    def test_clear(self, ll):
        ll.append(1, 2, 3)
        assert [1, 2, 3] == ll.as_list()
        ll.clear()
        assert [] == ll.as_list()

    def test_append(self, ll):
        ll.append(1, 2, 3)
        assert [1, 2, 3] == ll.as_list()
        assert 1 == ll.head.data
        assert 3 == ll.tail.data

    def test_add_append(self, ll):
        ll.add(1)
        ll.append(2, 3)
        assert [1, 2, 3] == ll.as_list()
        assert 1 == ll.head.data
        assert 3 == ll.tail.data
