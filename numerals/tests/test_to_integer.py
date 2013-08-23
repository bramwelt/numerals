import unittest

from numerals import to_integer


class IntegerTestCase(unittest.TestCase):
    """
    Tests related to converting numerals to integers
    """

    def test_type_error_raised_for_bad_input(self):
        self.assertRaises(TypeError, to_integer, 'cats')

    def test_one(self):
        self.assertEqual(1, to_integer('I'))

    def test_two(self):
        self.assertEqual(2, to_integer('II'))

    def test_three(self):
        self.assertEqual(3, to_integer('III'))

    def test_four(self):
        self.assertEqual(4, to_integer('IV'))

    def test_five(self):
        self.assertEqual(5, to_integer('V'))

    def test_six(self):
        self.assertEqual(6, to_integer('VI'))

    def test_seven(self):
        self.assertEqual(7, to_integer('VII'))

    def test_eight(self):
        self.assertEqual(8, to_integer('VIII'))

    def test_nine(self):
        self.assertEqual(9, to_integer('IX'))

    def test_ten(self):
        self.assertEqual(10, to_integer('X'))

    def test_fifty(self):
        self.assertEqual(50, to_integer('L'))

    def test_one_hundred(self):
        self.assertEqual(100, to_integer('C'))

    def test_five_hundred(self):
        self.assertEqual(500, to_integer('D'))

    def test_one_thousand(self):
        self.assertEqual(1000, to_integer('M'))
