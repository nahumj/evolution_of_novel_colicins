import unittest
import mutate


class TestMutate(unittest.TestCase):

    def test_mutate_int(self):
        for _ in range(10):
            x = mutate.mutate(0)
            self.assertIn(x, [-1, 1])


class TestShiftByOne(unittest.TestCase):

    def test_shift_by_one(self):
        for _ in range(10):
            x = mutate.shift_by_one(0)
            self.assertIn(x, [-1, 1])
