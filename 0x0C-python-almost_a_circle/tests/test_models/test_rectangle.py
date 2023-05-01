#!/usr/bin/python3

"""test_rectangle module"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """TestRectangle class to run tests on Rectangle"""

    def setUp(self):
        """Setup Rectangle"""

        self.rect = Rectangle(10, 10, 10, 10, 3)

    def test_id(self):
        """Test Rectangle id value"""

        self.assertEqual(self.rect.id, 3)

    def test_width(self):
        """Test Rectangle width value"""

        self.assertEqual(self.rect.width, 10)

    def test_height(self):
        """Test Rectangle height value"""

        self.assertEqual(self.rect.height, 10)

    def test_x(self):
        """Test x value"""

        self.assertEqual(self.rect.x, 10)

    def test_y(self):
        """Test y value"""

        self.assertEqual(self.rect.y, 10)

    def test_area(self):
        """Test area value"""

        self.assertEqual(self.rect.area(), 100)

    def test_update(self):
        """Test update"""

        self.rect.update(10, 1, 1, 0, 0)
        self.assertIs(self.rect.id, 10)
        self.assertIs(self.rect.width, 1)
        self.assertIs(self.rect.height, 1)
        self.assertIs(self.rect.x, 0)
        self.assertIs(self.rect.y, 0)
