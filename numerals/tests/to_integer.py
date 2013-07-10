import unittest

from numerals import to_integer


class IntegerTestCase(unittest.TestCase):
    """
    Tests related to converting numerals to integers
    """

    def test_five(self):
        """
        5 == 'V'
        """
        self.assertEqual(5, to_integer('V'))
