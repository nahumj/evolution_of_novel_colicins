import unittest

from colicin_immunity import Colicin, Immunity
from organism import Organism

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

