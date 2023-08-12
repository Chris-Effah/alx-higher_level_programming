#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_integer([10, 20, 30]), 30)
        self.assertEqual(max_integer([30, 20, 10]), 30)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-3, -2, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 2]), 2)
        self.assertEqual(max_integer([2, 0, -1]), 2)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_parameter(self):
        self.assertEqual(max_integer([30]), 30)

if __name__ == '__main__':
    unitest.main()
