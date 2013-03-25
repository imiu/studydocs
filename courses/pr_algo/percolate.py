#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
import random
import math
from itertools import chain
from ex15 import UfWqu


class Percolation(object):
    def __init__(self, n):
        """ Initialize N-by-N grid """
        self.size = n * n + 2
        self.perc = UfWqu(self.size)
        self.n = n
        self.opened = [[0] * self.n for i in range(self.n)]
        # Virtual point
        for i in range(n):
            self.perc.union(self.size - 2, i)
            self.perc.union(self.size - 1, self.size - 1 - i - 2)

    def open_(self, i, j):
        """ Open site (i, j) if it's not open yet """
        self.opened[i][j] = 1
        adj_candidates = ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1))
        adj_idxs = [(ti, tj) for ti, tj in adj_candidates
                    if (0 <= ti <= self.n - 1 and 0 <= tj <= self.n - 1)]
        for (idx, jdx) in adj_idxs:
            if self.is_open(idx, jdx):
                self.perc.union(i * self.n + j, idx * self.n + jdx)

    def is_open(self, i, j):
        """ Probe if site (i, j) is open """
        return (self.opened[i][j] == 1)

    def is_percolative(self):
        """ Do we percolate already? """
        return (self.perc.is_connected(self.size - 1, self.size - 2))

    def get_perc_arr(self):
        return self.perc.get_arr()

    def print_perc_arr(self):
        for idx, elm in enumerate(self.perc.get_arr()):
            if ((idx + 1) % self.n == 0):
                print(str(elm).ljust(2), end="\n")
            else:
                print(str(elm).ljust(2), end=" ")
        print("\n")

    def print_opened_arr(self):
        for lines in self.opened:
            for elm in lines:
                print(elm, end=" ")
            print()
        print("\n")


class PercolateStats(object):
    def __init__(self, n, t):
        """ perform t experiments with n-by-n grid """
        self.n = n
        self.t = t
        self.mean_val = None
        self.stddev_val = None
        self.stats = []

    def run(self):
        for i in range(self.t):
            self.perform()

    def perform(self):
        """ Perform one experiment with n-by-n grid """
        p = Percolation(self.n)
        opened_sites = 0
        while True:
            ran_i = random.randint(0, self.n - 1)
            ran_j = random.randint(0, self.n - 1)
            p.open_(ran_i, ran_j)
            if p.is_percolative():
                opened_sites = sum(list(chain.from_iterable(p.opened)))
                self.stats.append(opened_sites / (self.n * self.n))
                break

    def mean(self):
        """ Sample mean of percolation threshold """
        if self.mean_val is None:
            self.mean_val = sum(self.stats) / self.t
        return self.mean_val

    def stddev(self):
        """ Standard deviation of percolation threshold """
        if self.stddev_val is None:
            mean = self.mean()
            self.stddev_val = math.sqrt(
                sum((x - mean) ** 2 for x in self.stats) / self.t)
        return self.stddev_val

    def confidence_lo(self):
        """ Lower bound of 95% confidence """
        return self.mean() - (1.96 * self.stddev() / math.sqrt(self.t))

    def confidence_hi(self):
        """ Upper bound of 95% confidence """
        return self.mean() + (1.96 * self.stddev() / math.sqrt(self.t))

if __name__ == '__main__':
    ps = PercolateStats(20, 50)
    print("--- Running --- ")
    ps.run()
    print(" --- Stats --- ")
    print("mean   = {}".format(ps.mean()))
    print("stddev = {}".format(ps.stddev()))
    print("95%    = {}, {}".format(ps.confidence_lo(), ps.confidence_hi()))
