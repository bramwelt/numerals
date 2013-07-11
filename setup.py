from setuptools import setup, find_packages

from numerals import __version__

setup(
    name="numerals",
    version='.'.join(__version__),
    url="http://github.com/bramwelt/numerals",
    author="Trevor Bramwell",
    author_email="trevor@bramwell.net",
    packages=find_packages(),
    test_suite="numerals.tests",
)
