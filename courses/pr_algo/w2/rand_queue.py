#!/usr/bin/env python
from __future__ import print_function
import random as rnd


class RandomQueue(object):
    def __init__(self):
        self._queue = []

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

    def enqueue(self, data):
        self._queue.append(data)

    def dequeue(self):
        rand_idx = rnd.randint(0, self.size() - 1)
        return self._queue.pop(rand_idx)

    def sample(self):
        return rnd.choice(self._queue)

    def __iter__(self):
        return self._queue
