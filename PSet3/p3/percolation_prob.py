#!/usr/bin/env python

"""
In this program, we iterate over the possible probabilities
and simulate percolation.
"""

import numpy as np
from include.generation import gen_rand_sys as grs
from colorize import colorize, is_percolated


def main():
    """Main body"""
    size = 10           # The size of our grid
    prob = 0            # probability of a cell being "on"
    data = np.zeros(shape=(21, ), dtype=int)

    for i in range(21):
        perc = 0            # The number of percolations in 100 tries
        for _ in range(100):
            print(prob)
            grid = grs(size, prob)
            c_grid = colorize(grid)
            if is_percolated(c_grid):
                perc += 1
        prob += 0.05
        data[i] = perc

    print(data)
    print(range(1, c_grid.shape[1] + 1))


if __name__ == "__main__":
    main()
