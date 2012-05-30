import unittest
import copy

from organism import Organism
from colicin_immunity import Colicin, Immunity
from population import Population


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

    def test_cull(self):
        org_winner = Organism([Colicin(5)], [Immunity(0, 5)])
        self.pop.pop.append(org_winner)
        self.pop.cull()

        self.assertSequenceEqual(self.pop.pop, [org_winner])

    def test_colicins_produced(self):
        colicins = self.pop.colicins_produced()
        self.assertSetEqual({self.col}, colicins)

        other_colicin = Colicin(5)
        self.pop.pop.append(Organism([other_colicin], [Immunity(0, 5)]))
        colicins = self.pop.colicins_produced()
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
