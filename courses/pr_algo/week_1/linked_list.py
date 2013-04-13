#!/usr/bin/env python


class ListNode(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node(self, node):
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def add_data(self, *data):
        for d in data:
            node = ListNode(d)
            self.add_node(node)

    def get_as_list(self):
        node = self.head
        values = []
        while node is not None:
            values.append(node.data)
            node = node.next
        return values

    def remove_at(self, idx):
        if idx >= self.length:
            return False
        if idx == 0:
            self.remove(self.head)
        else:
            node = self.head
            for i in range(idx - 1):
                node = node.next
            del_node = node.next
            self.remove(del_node)

        return True

    def remove(self, node):
        prev_node = None
        cur_node = self.head
        while cur_node is not None and cur_node != node:
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node is not None:
            if cur_node is self.head:
                self.head = cur_node.next
            else:
                prev_node.next = cur_node.next
            if cur_node is self.tail:
                self.tail = prev_node
        self.length -= 1

    def remove_after(self, value):
        cur_node = self.head
        while cur_node is not None and cur_node.data != value:
            cur_node = cur_node.next
        if cur_node is not None and cur_node.next is not None:
            self.remove(cur_node.next)

    def insert_after(self, after_data, data):
        cur_node = self.head
        while cur_node is not None and cur_node.data != after_data:
            cur_node = cur_node.next
        if cur_node is not None:
            ins_node = ListNode(data)
            ins_node.next = cur_node.next
            cur_node.next = ins_node
            if cur_node is self.tail:
                self.tail = ins_node
            return True
        return False

    def remove_all(self, value):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == value:
                next_node = cur_node.next
                self.remove(cur_node)
                cur_node = next_node
            else:
                cur_node = cur_node.next

    def get_max_elm(self):
        cur_node = self.head
        max_elm = 0
        while cur_node is not None:
            if cur_node.data > max_elm:
                max_elm = cur_node.data
            cur_node = cur_node.next

        return max_elm

    def reverse(self):
        current = self.head
        prev = None
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.data)
            node = node.next
        return str(values)
