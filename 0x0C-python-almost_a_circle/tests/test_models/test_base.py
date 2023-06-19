from unittest import TestCase
from models.base import Base

class TestBase(TestCase):
    """ Test cases for the Base class"""

    def setUp(self):
        """ set up the test"""
        Base.__nb_objects = 0

    def test_default_id(self):
        """ test if no given id, increment __nb_objects and assign
            the new value to the id attribute."""
        new_obj = Base()
        self.assertEqual(new_obj.id, 1)

    def test_id(self):
        """ test assigning the given id to the attribute."""
        new_obj = Base(2)
        self.assertEqual(new_obj.id, 2)

    def test_nb_objects(self):
        """ test number of objects."""
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_mix_ids(self):
        """ test mix of serial and given ids."""
        obj1 = Base()
        obj2 = Base(100)
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 100)
        self.assertEqual(obj3.id, 2)

    def test_str_id(self):
        """ test if the given string id is set as string."""
        obj1 = Base('1')
        self.assertEqual(obj1.id, '1')

    def test_more_args_than_id(self):
        """ test if the __init__ were given args
            more than id."""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_privacy(self):
        """ test accessing private attributes."""
        with self.assertRaises(AttributeError):
            b = Base()
            print(b.__nb_objects)
