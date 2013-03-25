#!/usr/bin/env python
from __future__ import print_function
from linked_list import LinkedList
from linked_list import ListNode


class TestLikedList(object):
    def setup_method(self, method):
        pass

    def test_add_node(self):
        lst = LinkedList()
        node = ListNode(1)
        lst.add_node(node)
        assert [1] == lst.get_as_list()
        lst.add_node(ListNode(2))
        lst.add_node(ListNode(3))
        assert [1, 2, 3] == lst.get_as_list()

    def test_add_data(self):
        lst = LinkedList()
        lst.add_data(1, 2, 3, 4, 5)
        assert [1, 2, 3, 4, 5] == lst.get_as_list()

    def test_get_as_list(self):
        l = LinkedList()
        l.add_data(1, 2, 3)
        assert [1, 2, 3] == l.get_as_list()

    def test_remove_at(self):
        l = LinkedList()
        l.add_data(1, 2, 3, 4, 5)
        l.remove_at(2)
        assert [1, 2, 4, 5] == l.get_as_list()
        l.remove_at(3)
        assert [1, 2, 4] == l.get_as_list()
        l.remove_at(0)
        assert [2, 4] == l.get_as_list()

    def test_remove_after(self):
        lst = LinkedList()
        lst.add_data(1, 2, 3, 4, 5)
        lst.remove_after(2)
        assert [1, 2, 4, 5] == lst.get_as_list()
        lst.remove_after(4)
        assert [1, 2, 4] == lst.get_as_list()

    def test_insert_after(self):
        lst = LinkedList()
        lst.add_data(1, 2, 3)
        lst.insert_after(2, 10)
        assert [1, 2, 10, 3] == lst.get_as_list()
        assert lst.tail.data == 3

        lst.insert_after(3, 11)
        assert [1, 2, 10, 3, 11] == lst.get_as_list()
        assert lst.tail.data == 11

    def test_remove_all(self):
        lst = LinkedList()
        lst.add_data(1, 2, 1, 3, 1, 4, 1, 1)
        lst.remove_all(1)
        assert [2, 3, 4] == lst.get_as_list()

    def test_max_elm(self):
        lst = LinkedList()
        assert 0 == lst.get_max_elm()
        lst.add_data(1, 4, 3, 8, 15, 3, 1)
        assert 15 == lst.get_max_elm()

    def test_reverse(self):
        lst = LinkedList()
        lst.add_data(1)
        lst.reverse()
        assert [1] == lst.get_as_list()
        lst = LinkedList()
        lst.add_data(1, 2, 3, 4, 5)
        lst.reverse()
        assert [5, 4, 3, 2, 1] == lst.get_as_list()
