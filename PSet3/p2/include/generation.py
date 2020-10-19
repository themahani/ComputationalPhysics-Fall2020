#!/usr/bin/env python

"""
Generate a grid of size L*L and give random binary values
"""

import numpy as np
from sys import argv


def gen_binary_rand():
    """return 1 with probability p, return 0 otherwise"""
    probability = 0.6
    rand = np.random.uniform()
    if rand > probability:
        return 1
    else:
        return 0


def randomize_sys(grid):
    """
    Take a grid and randomize it with probability p
    """
    # Loop over the block and randomize it
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Random block assignment
            grid[i, j] = gen_binary_rand()


def gen_rand_sys(size):
    """
    generate a grid with input size
    """
    # Initialize grid with size
    grid = np.zeros(shape=(size, size), dtype=int, order='F')
    # Randomize grid
    randomize_sys(grid)
    # return the generated table
    return grid

def main():
    """ Main body """
    # validate the input
    if len(argv) != 2:
        print("usage: python gen_rand_sys.py <size of grid>")
        return 1
    else:
        # get size from input
        size = int(argv[1])
        grid = gen_rand_sys(size)
        print(grid)


if __name__ == "__main__":
    main()
