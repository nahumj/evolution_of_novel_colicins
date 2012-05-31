import unittest
import copy

from colicin import Colicin
from immunity import Immunity
from organism import Organism

from colicin_bitstring import Colicin as ColicinBit
from immunity_bitstring import Immunity as ImmunityBit
from bitstring import Bitstring


class TestOrganism(unittest.TestCase):

    def setUp(self):
        self.colicins = [Colicin(0), Colicin(-10)]
        self.immunities = [Immunity(0, 5), Immunity(-7, 4)]
        self.org = Organism(self.colicins, self.immunities)

    def test_init(self):
        self.assertSequenceEqual(self.org.colicins, self.colicins)
        self.assertSequenceEqual(self.org.immunities, self.immunities)

    def test_immune_to(self):
        same_colicin = Colicin(0)
        similar_colicin = Colicin(5)
        similar_colicin2 = Colicin(-5)
        different_colicin = Colicin(-20)
        self.assertTrue(self.org.is_immune_to(same_colicin))
        self.assertTrue(self.org.is_immune_to(similar_colicin))
        self.assertTrue(self.org.is_immune_to(similar_colicin2))
        self.assertFalse(self.org.is_immune_to(different_colicin))

    def test_is_self_toxic(self):
        self.assertFalse(self.org.is_self_toxic())
        org2 = Organism([Colicin(10)], [Immunity(0, 5)])
        self.assertTrue(org2.is_self_toxic())
        org2.colicins = []
        self.assertFalse(self.org.is_self_toxic())
        org2.immunities = []
        self.assertFalse(self.org.is_self_toxic())

    def test_eq(self):
        org2 = Organism([Colicin(10)], [Immunity(0, 5)])
        self.assertNotEqual(self.org, org2)
        org3 = Organism([Colicin(10)], [Immunity(0, 5)])
        self.assertEqual(org2, org3)

    def test_duplicate(self):
        org2 = self.org.duplicate()
        self.assertEqual(self.org, org2)
        org2.colicins.append(Colicin(12))
        self.assertNotEqual(self.org, org2)

    def test_mutate(self):
        mutant = self.org.mutate()
        self.assertNotEqual(self.org, mutant)
        self.assertEqual(len(mutant.colicins), len(self.org.colicins))
        self.assertEqual(len(mutant.immunities), len(self.org.immunities))


class TestOrganismBitstring(unittest.TestCase):
    def setUp(self):
        self.bit0 = Bitstring("0000")
        self.bit1 = Bitstring("1111")
        self.col0 = ColicinBit(self.bit0)
        self.col1 = ColicinBit(self.bit1)
        self.org0 = Organism([self.col0], [ImmunityBit(self.bit0, 1)])

    def test_is_immune_to(self):
        self.assertTrue(self.org0.is_immune_to(self.col0))
        self.assertFalse(self.org0.is_immune_to(self.col1))

    def test_is_self_toxic(self):
        org_toxic = Organism([self.col1], [ImmunityBit(self.bit0, 2)])
        self.assertFalse(self.org0.is_self_toxic())
        self.assertTrue(org_toxic.is_self_toxic())

    def test_mutate(self):
        mutant = self.org0.mutate()
        col_diff = mutant.colicins[0].id.hamming_distance(
                self.org0.colicins[0].id)
        self.assertEqual(col_diff, 1)
        imm_diff = mutant.immunities[0].id.hamming_distance(
                self.org0.immunities[0].id)
        self.assertEqual(imm_diff, 1)
