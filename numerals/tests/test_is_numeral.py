"""
Tests for isNumeral
"""

import unittest

from numerals import isNumeral


class IsNumeralTestCase(unittest.TestCase):
    """
    Make sure isNumeral works correctly for a range of characters.
    """

    def test_non_string(self):
        """
        A TypeError should be raised when the function tries to iterate
        over an integer.
        """
        self.assertRaises(TypeError, isNumeral, 543)

    def test_invalid_input(self):
        """
        'cats' contains the invalid characters 'ats'.
        """
        self.assertFalse(isNumeral('cats'))

    def test_invalid_input_beginning(self):
        """
        'ZIVLD' contains the invalid character 'Z' at the beginning.
        """
        self.assertFalse(isNumeral('ZIVLD'))

    def test_invalid_input_middle(self):
        """
        'VIIUI' contains the invalid character 'U' in the middle.
        """
        self.assertFalse(isNumeral('VIIUI'))

    def test_invalid_input_end(self):
        """
        'MMXLDCB' contains the invalid character 'B' at the end.
        """
        self.assertFalse(isNumeral('MMXLDCB'))

    def test_valid_false_input(self):
        """
        This string, though not a real numeral, is still valid.
        """
        self.assertTrue(isNumeral('LDVIVVIDLCMD'))

    def test_case_insensitivity(self):
        self.assertTrue(isNumeral('mmxivi'))
        self.assertTrue(isNumeral('MMXIVI'))
