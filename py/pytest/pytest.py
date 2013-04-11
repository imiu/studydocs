#!/usr/bin/env python
from __future__ import division
import py.test


def test_case():
    """docstring for test_case"""
    py.test.assert_almost_equal(first=0.3333, second=0.3333, prec=0.001)
