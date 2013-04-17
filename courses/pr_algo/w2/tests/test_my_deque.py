#!/usr/bin/env python
from my_deque import MyDeque
import pytest


@pytest.fixture
def md():
    return MyDeque()


class TestMyDeque(object):
    def test_is_empty(self, md):
        assert md.is_empty() is True
        md.add_last(1)
        assert md.is_empty() is False
        assert md.size() == 1

    def _add_first_three(self, _md):
        _md.add_first(1)
        _md.add_first(2)
        _md.add_first(3)

    def _add_last_three(self, _md):
        _md.add_last(1)
        _md.add_last(2)
        _md.add_last(3)

    def test_add_last(self, md):
        self._add_last_three(md)
        assert [1, 2, 3] == md.get_list()
        assert md.size() == 3

    def test_get_list(self, md):
        self._add_last_three(md)
        assert [1, 2, 3] == md.get_list()

    def test_remove_last(self, md):
        self._add_last_three(md)
        assert [1, 2, 3] == md.get_list()
        assert 3 == md.remove_last()
        assert 2 == md.remove_last()
        assert 1 == md.remove_last()
        with pytest.raises(IndexError) as e:
            md.remove_first()
            assert "deque is empty" == e.msg

    def test_add_first(self, md):
        self._add_first_three(md)
        assert [3, 2, 1] == md.get_list()

    def test_remove_first(self, md):
        self._add_first_three(md)
        assert 3 == md.remove_first()
        assert [2, 1] == md.get_list()
        assert 2 == md.remove_first()
        assert 1 == md.remove_first()
        assert True == md.is_empty()
        with pytest.raises(IndexError) as e:
            md.remove_first()
            assert "deque is empty" == e.msg

    def test_iterator(self, md):
        self._add_last_three(md)
        for idx, item in enumerate(md):
            for jdx, jtem in enumerate(md):
                assert jdx + 1 == jtem
            assert idx + 1 == item
