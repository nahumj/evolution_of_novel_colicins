import unittest
import copy

from organism import Organism
from colicin import Colicin
from immunity import Immunity
from population import Population

from colicin_bitstring import Colicin as ColicinBit
from immunity_bitstring import Immunity as ImmunityBit
from bitstring import Bitstring


class TestPopulation(unittest.TestCase):
    def setUp(self):
        self.col = Colicin(0)
        self.imm = Immunity(-5, 5)
        self.org = Organism([self.col], [self.imm])
        self.pop = Population([self.org.duplicate() for _ in range(10)])

    def test_len(self):
        self.assertEqual(len(self.pop), 10)

    def test_replicate(self):
        self.pop.replicate()
        self.assertEqual(self.pop.pop.count(self.org), 10)
        self.assertEqual(len(self.pop), 20)

    def test_iter(self):
        for org in self.pop:
            self.assertEqual(org, self.org)
        else:
            return
        self.fail()

    def test_remove_self_toxic(self):
        org_toxic = Organism([Colicin(0)], [Immunity(10, 5)])
        org_not_toxic = Organism([Colicin(0)], [Immunity(0, 5)])
        self.pop.pop = [org_not_toxic, org_toxic]
        self.assertEqual(len(self.pop), 2)

        self.pop.remove_self_toxic()
        self.assertEqual(len(self.pop), 1)
        self.assertSequenceEqual(self.pop.pop, [org_not_toxic])

    def test_cull_by_all_colicins(self):
        org_winner = Organism([Colicin(5)], [Immunity(0, 5)])
        self.pop.pop.append(org_winner)
        self.pop.cull_by_all_colicins()
        self.assertSequenceEqual(self.pop.pop, [org_winner])

    def test_cull_by_all_colicins_extinction(self):
        org_other = Organism([Colicin(5)], [Immunity(10, 5)])
        self.pop.pop.append(org_other)
        self.pop.cull_by_all_colicins()
        self.assertEqual(len(self.pop), 0)

    def test_cull_by_single_colicin(self):
        org_other = Organism([Colicin(100)], [Immunity(100, 5)])
        self.pop.pop.extend(org_other for _ in range(10))
        self.pop.cull_by_single_colicin()
        self.assertEqual(len(self.pop), 10)

    def test_cull_by_single_colicin_extinction(self):
        self.pop.cull_by_single_colicin(Colicin(5))
        self.assertEqual(len(self.pop), 0)

    def test_cull_by_iterative_colicin(self):
        org_winner = Organism([Colicin(5)], [Immunity(0, 5)])
        self.pop.pop.append(org_winner)
        self.pop.cull_by_iterative_colicin()
        self.assertSequenceEqual(self.pop.pop, [org_winner])

    def test_cull_by_iterative_colicin_extinction(self):
        org_other = Organism([Colicin(5)], [Immunity(10, 5)])
        self.pop.pop.extend(org_other for _ in range(10))
        self.pop.cull_by_iterative_colicin()
        self.assertEqual(len(self.pop), 10)

    def test_colicins_produced(self):
        colicins = set(self.pop.colicins_produced())
        self.assertSetEqual({self.col}, colicins)

        other_colicin = Colicin(5)
        self.pop.pop.append(Organism([other_colicin], [Immunity(0, 5)]))
        colicins = set(self.pop.colicins_produced())
        self.assertSetEqual({self.col, other_colicin}, colicins)

    def test_sample_with_replacement(self):
        self.pop.pop.extend(self.org for _ in range(20))
        self.assertEqual(len(self.pop), 30)
        self.pop.sample_with_replacement()
        self.assertEqual(len(self.pop), 10)

        self.pop.pop = self.pop.pop[::2]
        self.assertEqual(len(self.pop), 5)
        self.pop.sample_with_replacement()
        self.assertEqual(len(self.pop), 10)

        self.assertEqual(self.pop.carrying_capacity, 10)

    def test_advance_generation(self):
        self.pop.advance_generation()
        self.assertEqual(len(self.pop), 10)


class TestPopulationBitstring(unittest.TestCase):
    def setUp(self):
        bit0 = Bitstring("0000")
        bit1 = Bitstring("1111")
        col0 = ColicinBit(bit0)
        col1 = ColicinBit(bit1)
        org = Organism([col0], [ImmunityBit(bit0, 2)])
        self.pop = Population([org for _ in range(5)])

    def test_replicate(self):
        self.assertEqual(len(self.pop), 5)
        self.pop.replicate()
        self.assertEqual(len(self.pop), 10)

    def test_remove_self_toxic(self):
        self.assertEqual(len(self.pop), 5)
        self.pop.remove_self_toxic()
        self.assertEqual(len(self.pop), 5)

    def test_cull_by_iterative_colicin(self):
        self.assertEqual(len(self.pop), 5)
        self.pop.cull_by_iterative_colicin()
        self.assertEqual(len(self.pop), 5)

    def test_advance_generation(self):
        self.pop.advance_generation()

    def test_sample_with_replacement(self):
        self.pop.sample_with_replacement()
