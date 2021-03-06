import unittest

from numerals import to_numeral


class NumeralTestCase(unittest.TestCase):
    """
    Tests related to converting integers to numerals
    """

    def test_index_error_raised_for_zero(self):
        self.assertRaises(IndexError, to_numeral, 0)

    def test_index_error_raised_for_neg(self):
        self.assertRaises(IndexError, to_numeral, -10)

    def test_one(self):
        self.assertEqual('I', to_numeral(1))

    def test_two(self):
        self.assertEqual('II', to_numeral(2))

    def test_three(self):
        self.assertEqual('III', to_numeral(3))

    def test_four(self):
        self.assertEqual('IV', to_numeral(4))

    def test_five(self):
        self.assertEqual('V', to_numeral(5))

    def test_six(self):
        self.assertEqual('VI', to_numeral(6))

    def test_seven(self):
        self.assertEqual('VII', to_numeral(7))

    def test_eight(self):
        self.assertEqual('VIII', to_numeral(8))

    def test_nine(self):
        self.assertEqual('IX', to_numeral(9))

    def test_ten(self):
        self.assertEqual('X', to_numeral(10))

    def test_fifty(self):
        self.assertEqual('L', to_numeral(50))

    def test_one_hundred(self):
        self.assertEqual('C', to_numeral(100))

    def test_five_hundred(self):
        self.assertEqual('D', to_numeral(500))

    def test_one_thousand(self):
        self.assertEqual('M', to_numeral(1000))
