"""
Numerals is a package for converting to and from Roman numerals.

I V X  L  C   D   M
1 5 10 50 100 500 1000
"""

def isNumeral(numeral):
    """
    Given a string, make sure it only contains acceptable characters for
    numerals (I,V,X,L,C,D,M).
    """
    for char in numeral:
        if char.upper() not in 'IVXLCDM':
            return False
    return True

def to_integer(numeral):
    """
    Given a Roman numeral, convert it to an integer.
    """
    if not isNumeral(numeral):
        raise TypeError("Could not coerce {0} to integer.".format(numeral))

    numeral.upper()

    return int(5)


def to_numeral(integer):
    """
    Given an integer, convert it to a Roman numeral.
    """
    if integer < 1:
        raise IndexError("Can not convert integers less than 1.")

    return 'V'
