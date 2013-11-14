#! /usr/bin/env python
# -*- coding: utf-8


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, *args):
        for data in args:
            current = Node(data)
            current.next = self.head
            self.head = current
            if self.tail is None:
                self.tail = current

    def clear(self):
        self.head = None
        self.tail = None

    def append_head(self, *args):
        current = self.head
        if self.head is not None:
            while current.next is not None:
                current = current.next

        for data in args:
            node = Node(data)
            if self.head is None:
                self.head = node
            else:
                current.next = node
            current = node

    def append(self, *args):
        for data in args:
            node = Node(data)
            if self.head is None:
                self.head = node
            else:
                self.tail.next = node
            self.tail = node

    def length(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next

        return length

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next

        return False

    def remove(self, data):
        if self.search(data) is not True:
            return False

        current = self.head
        prev = None
        while current.data != data:
            prev = current
            current = current.next

        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
            if current.next is None:
                self.tail = prev

        return True

    def as_list(self):
        current = self.head
        l = []
        while current is not None:
            l.append(current.data)
            current = current.next
        return l
