#!/usr/bin/env python
from __future__ import print_function


class UfQf(object):
    def __init__(self, n):
        self.ids = [i for i in range(n)]
        self.count = n

    def union(self, p, q):
        q_id = self.find(q)
        p_id = self.find(p)

        if (q_id == p_id):
            return True

        for idx, tmp_id in enumerate(self.ids):
            if tmp_id == p_id:
                self.ids[idx] = q_id
        self.count -= 1

    def find(self, p):
        return self.ids[p]

    def is_connected(self, p, q):
        return self.find(q) == self.find(p)


class UfQu(object):
    def __init__(self, n):
        self.ids = [i for i in range(n)]
        self.count = n

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if q_root == p_root:
            return True
        self.ids[p_root] = q_root
        self.count -= 1

    def find(self, p):
        while p != self.ids[p]:
            p = self.ids[p]
        return p

    def is_connected(self, p, q):
        return self.find(q) == self.find(p)


class UfWqu(object):
    def __init__(self, n):
        self.ids = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]
        self.count = n

    def root(self, p):
        while p != self.ids[p]:
            p = self.ids[p]
        return p

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return True
        if self.sizes[i] < self.sizes[j]:
            self.ids[i] = j
            self.sizes[j] += self.sizes[i]
        else:
            self.ids[j] = i
            self.sizes[i] += self.sizes[j]
        self.count -= 1

    def is_connected(self, p, q):
        return self.root(q) == self.root(p)

    def get_arr(self):
        return self.ids
