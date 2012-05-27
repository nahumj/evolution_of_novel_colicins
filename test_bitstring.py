#!/usr/bin/env python2.7
"""
This module tests the bitstring class.
"""
import unittest

import bitstring
from bitstring import Bitstring

class TestBitstring(unittest.TestCase):

    def test_init(self):
        b = Bitstring("10")
        self.assertEqual(True, b[1])
        self.assertEqual(False, b[0])
        self.assertEqual(2, len(b))

    def test_iter(self):
        b = Bitstring("10")
        for pos, expected in zip(b, [False, True]):
            self.assertEqual(pos, expected)

    def test_eq(self):
        b = Bitstring("10")
        b2 = Bitstring("10")
        b3 = Bitstring("100")
        b4 = Bitstring("11")
        self.assertTrue(b == b2)
        self.assertTrue(b != b3)
        self.assertTrue(b != b4)

    def test_hamming_distance(self):
        b = Bitstring("10101")
        b2 = Bitstring("10101")
        b3 = Bitstring("01010")
        self.assertEqual(b.hamming_distance(b2), 0)
        self.assertEqual(b.hamming_distance(b3), 5)

    def test_repr(self):
        b = Bitstring("10")
        b_as_str = repr(b)
        b2 = eval(b_as_str)
        self.assertEqual(b, b2)


class TestModule(unittest.TestCase):

    def test_from_iterable(self):
        b = Bitstring("1000")
        b2 = bitstring.from_iterable([0, 0, 0, 1])
        b3 = bitstring.from_iterable([False, False, False, True])
        self.assertEqual(b, b2)
        self.assertEqual(b, b3)


if __name__ == "__main__":
    unittest.main()
