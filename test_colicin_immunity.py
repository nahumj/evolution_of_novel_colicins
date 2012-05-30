import unittest
from unittest import TestCase as TC

from colicin_immunity import Colicin
from colicin_immunity import Immunity

class TestColicin(TC):
    #inherits from TestCase
    def setUp(self):
        self.value = 7
        self.c = Colicin(self.value)

    def test_init(self):
        #write what we want to check
        self.assertEqual(self.value, self.c.id) #check if something is true

    def test_mutate(self):
        d = self.c.mutate()
        self.assertNotEqual(self.c.id, d.id)

class TestImmunity(TC):
    #inherits from TestCase
    def setUp(self):
        self.value, self.range = 7, 2
        self.i = Immunity(self.value, self.range)

    def test_init(self):
        #write what we want to check
        self.assertEqual(self.value, self.i.id) #check if something is true
        self.assertEqual(self.range, self.i.binding_range)

    def test_can_bind(self):
        c = Colicin(self.value)
        self.assertTrue(self.i.can_bind(c))

    def test_mutate(self):
        i2 = self.i.mutate()
        self.assertNotEqual(self.i, i2)

