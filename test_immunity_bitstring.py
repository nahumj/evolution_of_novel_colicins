import unittest
from unittest import TestCase as TC

from immunity_bitstring import Immunity
from colicin_bitstring import Colicin
from bitstring import Bitstring


class TestImmunityBitstring(TC):
    def setUp(self):
        self.value = Bitstring("10101")
        self.binding_range = 2
        self.i = Immunity(self.value, self.binding_range)

    def test_init(self):
        self.assertEqual(self.value, self.i.id)
        self.assertEqual(self.binding_range, self.i.binding_range)

    def test_can_bind(self):
        c = Colicin(self.value)
        self.assertTrue(self.i.can_bind(c))

    def test_mutate(self):
        i2 = self.i.mutate()
        self.assertNotEqual(self.i, i2)
