"""
Simulation:
1) colicin-immunity interaction module

2) Bacterial Population module
"""

from colicin_immunity import Colicin
from colicin_immunity import Immunity
from organism import Organism
from population import Population


def all_colicins(population):
    for org in population:
        for colicin in org.colicins:
            yield colicin


def average_colicin_id(population):
    ids = [col.id for col in all_colicins(population)]
    return sum(ids) / float(len(ids))


if __name__ == '__main__':
    print('start')
    org = Organism([Colicin(0)], [Immunity(0, 5)])
    pop = Population(org for _ in range(50))

    for gen in range(1000):
        pop.advance_generation()
        average_id = average_colicin_id(pop)
        if gen % 100 == 0:
            print("{}\t{}".format(gen, average_id))

    print('done')
