#!/usr/bin/env python3.2
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

	def test_repr(self):
		expected = 'Colicin(7)'
		self.assertEqual(expected, repr(self.c))

	def test_duplicate(self):
		d = self.c.duplicate()
		self.assertEqual(self.c.id, d.id)

	def test_mutate(self):
		d = self.c.duplicate()
		self.c.mutate()
		self.assertNotEqual(d.id, self.c.id)

class TestImmunity(TC):
	#inherits from TestCase
	def setUp(self):
		self.value, self.range = 7, 2
		self.i = Immunity(self.value, self.range)

	def test_init(self):
		#write what we want to check
		self.assertEqual(self.value, self.i.id) #check if something is true
		self.assertEqual(self.range, self.i.binding_range)

	def test_repr(self):
		expected = 'Immunity(7, 2)'
		self.assertEqual(expected, repr(self.i))

	def test_can_bind(self):
		c = Colicin(self.value)
		self.assertTrue(self.i.can_bind(c))

	def test_duplicate(self):
		d = self.i.duplicate()
		self.assertEqual(self.i.id, d.id)
		self.assertEqual(self.i.binding_range, d.binding_range)

if __name__ == '__main__':
	unittest.main()


