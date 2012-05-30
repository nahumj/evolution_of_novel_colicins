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
        return {colicin for org in self for colicin in org.colicins}

    def cull(self):
        all_colicins = self.colicins_produced()

        def immune_to_all_colicins(org):
            return all(org.is_immune_to(colicin) for colicin in all_colicins)

        self.pop = [org for org in self.pop if immune_to_all_colicins(org)]

    def select_colicin(self):
        org = random.choice(self.pop)
        return random.choice(org.colicins)

    def sample_with_replacement(self):
        self.pop = [random.choice(self.pop)
                for _ in range(self.carrying_capacity)]

    def advance_generation(self):
        self.replicate()
        self.remove_self_toxic()
        self.cull()
        self.sample_with_replacement()
