#!/usr/bin/env python
from __future__ import print_function


class ListNode(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class MyDeque(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def add_first(self, data):
        item = ListNode(data)
        item.next = self._head
        self._head = item
        if self._tail is None:
            self._tail = item
        self._size += 1

    def add_last(self, data):
        item = ListNode(data)
        if self._tail:
            self._tail.next = item
        if not self._head:
            self._head = item
        self._tail = item
        item.next = None
        self._size += 1

    def remove_first(self):
        if self._size == 0:
            raise IndexError("deque is empty")
        item = self._head
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._head = item.next
        self._size -= 1
        return item.data

    def remove_last(self):
        if self._size == 0:
            raise IndexError("dequeu is empty")
        if self._size == 1:
            item = self._head
            self._head = None
            self._tail = None
        else:
            tmp_item = self._head
            while tmp_item.next != self._tail:
                tmp_item = tmp_item.next
            item = self._tail
            tmp_item.next = None
            self._tail = tmp_item
        self._size -= 1
        return item.data

    def __iter__(self):
        self.__current = self._head
        return self

    def next(self):
        if self.__current is not None:
            item = self.__current
            self.__current = item.next
            return item.data
        else:
            raise StopIteration("no more elements")

    def __str__(self):
        item = self._head
        if item is not None:
            str_rep = []
            while item:
                str_rep.append(str(item.data))
                item = item.next
            str_rep.append("None")
            str_head = "\n head - " + str(self._head.data)
            str_tail = "\n tail - " + str(self._tail.data)
            return " -> ". join(str_rep) + str_head + str_tail
        else:
            return "deque is empty"

    def get_list(self):
        item = self._head
        res = []
        while item:
            res.append(item.data)
            item = item.next
        return res
