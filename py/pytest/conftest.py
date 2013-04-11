def pytest_namespace():
    """Make unittest assert methods available.
    This is useful for floating point checks with assertAlmostEqual"""

    import unittest
    import inspect

    class Dummy(unittest.TestCase):
        def dummy(self):
            pass

    def _assert_almost_equal(first, second, prec):
        if (abs(first - second) > prec):
            raise AssertionError("Even almost not equal")

    obj = Dummy('dummy')
    names = {name: member
             for name, member in inspect.getmembers(obj)
             if name.startswith('assert') and '_' not in name}

    names.update({"assert_almost_equal": _assert_almost_equal})
    return names
