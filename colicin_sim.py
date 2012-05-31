#!/usr/bin/env python3
"""
Simulation:
1) colicin-immunity interaction module

2) Bacterial Population module
"""

from colicin import Colicin
from immunity import Immunity
from organism import Organism
from population import Population


def average_colicin_id(population):
    ids = [col.id for col in population.colicins_produced()]
    return sum(ids) / float(len(ids))


def main():
    org = Organism([Colicin(0)], [Immunity(0, 5)])
    pop = Population(org for _ in range(5))

    for gen in range(1000):
        pop.advance_generation()
        average_id = average_colicin_id(pop)
        if gen % 100 == 0:
            print("{}\t{}".format(gen, average_id))

if __name__ == '__main__':
    print('start')
    main()
    print('done')
