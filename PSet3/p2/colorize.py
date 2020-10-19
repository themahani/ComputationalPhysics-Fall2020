#!/usr/bin/env python

"""
algorithm to find the clusters and colorize them and see if you have
Percolation
"""

import numpy as np
from include.generation import gen_rand_sys


def colorize():
    """ Colorize the grid """
    # Initialization
    grid = gen_rand_sys(30)
    length = grid.shape[0]
    init = np.ones(shape=(length, ))
    grid_colorize = np.hstack((init, grid))

    for i in range(length + 1):
        for j in range(length):
            print(grid_colorize[i, j])
