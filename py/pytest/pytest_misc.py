#!/usr/bin/env python
import pytest


def test_unittest_assert():
    """docstring for test_case"""
    pytest.assertAlmostEqual(1.0 / 3, 0.3333, places=4)
    with pytest.raises(AssertionError):
        pytest.assertAlmostEqual(0.3333, 0.3444, places=4)


def test_my_assert():
    pytest.assert_almost_equal(0.3333, 0.3334, 0.001)
    with pytest.raises(AssertionError):
        pytest.assert_almost_equal(0.3333, 0.3444, 0.001)


@pytest.mark.parametrize(("a", "b"), [("1+1", 2), ("1+2", 3)])
def test_eval(a, b):
    assert eval(a) == b
