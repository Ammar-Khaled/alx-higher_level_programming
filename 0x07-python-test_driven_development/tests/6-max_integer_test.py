#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Test for max_integer function. """

    def test_None(self):
        self.assertEqual(max_integer(), None)

    def test_zero_len(self):
        self.assertEqual(max_integer([]), None)

    def normal_test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negtive(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_repeated(self):
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_floats(self):
        self.assertEqual(max_integer([50.1, 50.2, 49]), 50.2)

    def test_operations(self):
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def test_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_zeros(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_only_one(self):
        self.assertEqual(max_integer([1]), 1)

    def test_str(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_num(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def max_at_the_end(self):
        self.assertEqual(max_integer([1, 4, 3, 4]), 4)
