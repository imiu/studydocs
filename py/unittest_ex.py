import unittest


class TestIntegr(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_basic(self):
        result = '1, 3, 4'.split(', ')
        self.assertEquals(result, ['1', '3', '4'])

if __name__ == '__main__':
    unittest.main()
