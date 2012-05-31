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

from colicin_bitstring import Colicin as ColicinBit
from immunity_bitstring import Immunity as ImmunityBit
from bitstring import Bitstring
import mutate


def average_colicin_int(population):
    ids = [col.id for col in population.colicins_produced()]
    return average(ids)


def average(nums):
    return sum(nums) / float(len(nums))


def average_colicin_bitstring_distance(population, ancestor_col):
    dists = [ancestor_col.id.hamming_distance(col.id)
            for col in population.colicins_produced()]
    return average(dists)


def colicin_int_demo():
    org = Organism([Colicin(0)], [Immunity(0, 5)])
    pop = Population(org for _ in range(5))
    for gen in range(1000):
        pop.advance_generation()
        average_id = average_colicin_int(pop)
        if gen % 100 == 0:
            print("{}\t{}".format(gen, average_id))


def colicin_bitstring_demo():
    mutate.mutation_rate = 0.05
    bit = Bitstring("0000000000000000000")
    bit2 = Bitstring("1000000000000000000")
    col = ColicinBit(bit)
    imm = ImmunityBit(bit2, 1)
    org = Organism([col], [imm, imm])
    pop = Population(org for _ in range(100))
    for gen in range(101):
        pop.advance_generation()
        if gen % 10 == 0:
            average_dist = average_colicin_bitstring_distance(pop, col)
            print("{}\t{}".format(gen, average_dist))


def main():
    colicin_bitstring_demo()

if __name__ == '__main__':
    print('start')
    main()
    print('done')
