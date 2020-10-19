#!/usr/bin/env python

"""
algorithm to find the clusters and colorize them and see if you have
Percolation
"""

import numpy as np
from matplotlib import pyplot as plt
from include.generation import gen_rand_sys


def merge(grid, new, old):
    """ Merge the two clusters """
    length = grid.shape[0]
    for i in range(length):
        for j in range(1, length + 1):
            if grid[i, j] == old:
                grid[i, j] = new




def find_cluster(grid, i, j):
    """ Find the cluster the item belongs to """
    if i == 0:
        if grid[i, j - 1] != 0:
            # Same cluster so same color
            grid[i, j] = grid[i, j - 1]
        else:
            front[0] += 1
            grid[i, j] = front[0]
    else:
        cond_a = grid[i, j - 1] != 0
        cond_b = grid[i - 1, j] != 0
        # if cluster around
        if cond_a or cond_b:
            a = grid[i, j - 1]
            b = grid[i - 1, j]
            # if both are clusters, get the minimum one(sooner created)
            if cond_a and cond_b:
                grid[i, j] = min(a, b)
                # merge the min and max clusters
                merge(grid, min(a, b), max(a, b))
            else:
                # one of them is zero. So color is the other num
                grid[i, j] = max(a, b)
        else:
            front[0] += 1
            grid[i, j] = front[0]


def clusterize(grid):
    """
    Find clusters
    """
    length = grid.shape[0]
    global front
    front = [length + 1]
    # loop over the cluster
    for i in range(length):
        for j in range(1, length + 1):
            find_cluster(grid, i, j)


def colorize(grid):
    """ Colorize the grid """
    # Initialization
    length = grid.shape[0]
    init = np.ones(shape=(length, 1), dtype=int)
    for i in range(length):
        init[i, 0] = i + 1
    grid_color = np.hstack((init, grid))
    clusterize(grid_color)
    return grid_color



def main():
    """ Main body """
    # Initialization
    prob = 0.2
    grid = gen_rand_sys(30, prob)
    c_grid = colorize(grid)
    print(c_grid)



if __name__ == "__main__":
    main()
