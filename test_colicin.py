import unittest
from unittest import TestCase as TC

from colicin import Colicin


class TestColicin(TC):
    #inherits from TestCase
    def setUp(self):
        self.value = 7
        self.c = Colicin(self.value)

    def test_init(self):
        #write what we want to check
        self.assertEqual(self.value, self.c.id)

    def test_mutate(self):
        d = self.c.mutate()
        self.assertNotEqual(self.c.id, d.id)
