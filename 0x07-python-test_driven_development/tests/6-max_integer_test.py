#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_4(self):
        """ Test that 4 is the maximum integer """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_6(self):
        """ Test that 6 is the maximum integer """

        self.assertEqual(max_integer([6, 2, -6, -1]), 6)

    def test_neg1(self):
        """ Test that -1 is the maximum integer """

        self.assertEqual(max_integer([-1, -2, -3, -445]), -1)

    def test_490(self):
        """ Test that 490 is the maximum integer """

        self.assertEqual(max_integer([1, 2, 490, 14, 78]), 490)

    def test_100000(self):
        """ Test that 100000 is the maximum integer """

        self.assertEqual(max_integer([1, 870, 100000, 490, 14, 78]), 100000)

    def test_4000000(self):
        """ Test that 4000000 is the maximum integer """

        self.assertEqual(max_integer([2000000, 4000000, -1, 78]), 4000000)

    def test_0(self):
        """ Test that 0 is the maximum integer """

        self.assertEqual(max_integer([-1, 0, -4, -8, -4, -80]), 0)

    def test_1000000000(self):
        """ Test that 1000000000 is the maximum integer """

        self.assertEqual(max_integer([1000000000, 100000, 10000]), 1000000000)

    def test_empty(self):
        """ Test empty list """
        self.assertIsNone(max_integer([]), None)

    def test_one_element(self):
        """ Test one element """
        self.assertEqual(max_integer([9]), 9)
