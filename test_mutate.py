import unittest
import mutate

from bitstring import Bitstring


class TestMutate(unittest.TestCase):

    def test_mutation_rate(self):
        mutate.mutation_rate = 0.0
        for _ in range(10):
            x = mutate.mutate(0)
            self.assertEqual(x, 0)
        mutate.mutation_rate = 1.0

    def test_mutate_int(self):
        for _ in range(10):
            x = mutate.mutate(0)
            self.assertIn(x, [-1, 1])

    def test_mutate_bitstring(self):
        for _ in range(10):
            b = Bitstring("1010101")
            mutant = mutate.shift_by_bit(b)
            self.assertEqual(b.hamming_distance(mutant), 1)

    def test_shift_by_one(self):
        for _ in range(10):
            x = mutate.shift_by_one(0)
            self.assertIn(x, [-1, 1])

    def test_shift_by_bit(self):
        for _ in range(10):
            b = Bitstring("1010101")
            mutant = mutate.shift_by_bit(b)
            self.assertEqual(b.hamming_distance(mutant), 1)
