#!/usr/bin/env python
import pytest
import random as rnd
from rand_queue import RandomQueue


@pytest.fixture
def rq():
    return RandomQueue()


class TestRandomQueue(object):
    def setup_method(self, method):
        rnd.seed(2128506)

    def test_is_emtpy(self, rq):
        assert True == rq.is_empty()

    def test_size(self, rq):
        assert 0 == rq.size()

    def test_enqueue(self, rq):
        rq.enqueue(1)
        assert 1 == rq.size()

    def test_dequeue(self, rq):
        rq.enqueue(1)
        assert 1 == rq.dequeue()
        rq.enqueue(2)
        rq.enqueue(3)
        rq.enqueue(4)
        assert 4 == rq.dequeue()
        assert 2 == rq.dequeue()

    def test_sample(self, rq):
        rq.enqueue(1)
        assert 1 == rq.sample()
        rq.enqueue(2)
        rq.enqueue(3)
        assert 3 == rq.sample()
        assert 2 == rq.sample()
