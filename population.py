"""
Holds a population of Organism instances (mutable)

Every Update:
1. Every member generates a mutant (doubling population size)
2. Self toxic organisms are culled
3. All produced colicins are used used to cull others
4. The population is sampled with replacement to fill to
    the original population size
"""
import random
from collections import OrderedDict


class Population(object):
    def __init__(self, init_pop):
        self.pop = list(init_pop)
        self.carrying_capacity = len(self.pop)

    def __len__(self):
        return len(self.pop)

    def replicate(self):
        """
        Add a mutant of each member of a population to the population
        """
        mutants = [org.mutate() for org in self.pop]
        self.pop += mutants

    def __iter__(self):
        return iter(self.pop)

    def remove_self_toxic(self):
        self.pop = [org for org in self.pop if not org.is_self_toxic()]

    def colicins_produced(self):
        for org in self:
            for colicin in org.colicins:
                yield colicin

    def cull_by_all_colicins(self):
        """
        Only allow orgs to live is they are resistant to all colicins

        Potential for extinction (two mutually incompatible organisms)
        """
        all_colicins = set(self.colicins_produced())

        def immune_to_all_colicins(org):
            return all(org.is_immune_to(colicin) for colicin in all_colicins)

        self.pop = [org for org in self.pop if immune_to_all_colicins(org)]

    def cull_by_single_colicin(self, colicin=None):
        """
        Chose a random colicin gene and kill all orgs not immune

        Potential for extinction (if argument colicin is toxic to all,
        or if self toxic orgs exist))
        """
        if colicin is None:
            colicin = random.choice(list(self.colicins_produced()))
        self.pop = [org for org in self.pop if org.is_immune_to(colicin)]

    def cull_by_iterative_colicin(self):
        """
        Randomly order the produced colicins (weighing is favor of popularity)
        For each colicin cull orgs not immune
        Stop when complete, or just before extinction
        """
        all_colicins = list(self.colicins_produced())
        random.shuffle(all_colicins)
        colicin_dict = OrderedDict((col, None) for col in all_colicins)
        for colicin in colicin_dict:
            pre_cull = self.pop[:]
            self.cull_by_single_colicin(colicin)
            if len(self) == 0:
                self.pop = pre_cull
                return

    def select_colicin(self):
        org = random.choice(self.pop)
        return random.choice(org.colicins)

    def sample_with_replacement(self):
        self.pop = [random.choice(self.pop)
                for _ in range(self.carrying_capacity)]

    def advance_generation(self, cull_method=None):
        if cull_method is None:
            cull_method = self.cull_by_iterative_colicin
        self.replicate()
        self.remove_self_toxic()
        cull_method()
        self.sample_with_replacement()
