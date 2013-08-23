import unittest

from numerals import to_numeral


class NumeralTestCase(unittest.TestCase):
    """
    Tests related to converting integers to numerals
    """

    def test_five(self):
        """
        'V' == 5
        """
        self.assertEqual('V', to_numeral(5))
