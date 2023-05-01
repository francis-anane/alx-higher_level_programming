#!/usr/bin/python3

"""test_base module"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestBase class to run tests on Base"""

    def test_None(self):
        """Test None Value to Base"""

        self.assertEqual(Base().id, 1)

    def test_str(self):
        """Test string Value to Base"""

        self.assertEqual(Base("string").id, "string")

    def test_ten(self):
        """Test Value 10 to Base"""

        self.assertEqual(Base(10).id, 10)
