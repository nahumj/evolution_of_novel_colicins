import unittest
from unittest import TestCase as TC

from colicin_bitstring import Colicin
from bitstring import Bitstring


class TestColicinBitstring(TC):
    def setUp(self):
        self.value = Bitstring("10101")
        self.c = Colicin(self.value)

    def test_init(self):
        #write what we want to check
        self.assertEqual(self.value, self.c.id)

    def test_mutate(self):
        d = self.c.mutate()
        self.assertNotEqual(self.c.id, d.id)
