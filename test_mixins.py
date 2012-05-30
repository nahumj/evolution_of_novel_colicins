import unittest

from mixins import Equalable, Printable, Duplicatable

class TestEquality(unittest.TestCase):

    def setUp(self):
        class X(Equalable):
            def __init__(self, value):
                self.value = value
        self.X = X
        self.x = X(1)
        self.x2 = self.X(2)

    def test_init(self):
        self.assertEqual(self.x, self.x)
        x_copy = self.X(1)
        self.assertEqual(self.x, x_copy)

        self.assertNotEqual(self.x, self.x2)

    def test_mutation(self):
        self.x2.value = 1
        self.assertEqual(self.x, self.x2)

class TestPrintable(unittest.TestCase):
    def test_printable(self):
        class X(Printable):
            pass
        repr_value = repr(X())
        self.assertEqual(repr_value[0], "<")
        self.assertEqual(repr_value[-1], ">")

class TestDuplicatable(unittest.TestCase):
    def test_duplicatable(self):
        class X(Duplicatable):
            def __init__(self, value):
                self.value = value
        x0 = X(0)
        x_dup = x0.duplicate()
        self.assertEqual(x0.value, x_dup.value)
        x_dup.value = 1
        self.assertNotEqual(x0.value, x_dup.value)
