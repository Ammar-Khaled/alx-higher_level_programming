from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(TestCase):
    """ test rectangle cases."""
    def setUp(self):
        """ set up the test"""
        Base.__nb_objects = 0

    def test_new_rect(self):
        """ test instantiating new rectangle."""
        new_rect = Rectangle(4, 8)
        self.assertEqual(new_rect.width, 4)
        self.assertEqual(new_rect.height, 8)
        self.assertEqual(new_rect.x, 0)
        self.assertEqual(new_rect.y, 0)
        self.assertEqual(new_rect.id, 1)

    def validate_width(self):
        """ validates that width is a positive integer."""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

        with self.assertRaises(TypeError):
            r = Rectangle(1.1, 2)
