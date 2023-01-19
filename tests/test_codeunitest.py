import unittest
from extra.codeunitest import check


class TestEvenNumberFunction(unittest.TestCase):

    def test_even(self):
        self.assertEqual(check(4),'even')

    def test_odd(self):
        self.assertEqual(check(5),'odd')

if __name__ == '__main__':
    unittest.main()
