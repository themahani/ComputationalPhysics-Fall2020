#!/usr/bin/env python

"""
In this program, we iterate over the possible probabilities
and simulate percolation.
"""

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

from include.generation import gen_rand_sys as grs
from colorize import colorize, is_percolated


def iter_prob(size):
    """ Iterate over the probability and return the Percolation Probability """
    data = np.zeros(shape=(20, ), dtype=int)
    prob = 0            # probability of a cell being "on"

    for i in range(20):
        prob += 0.05
        perc = 0            # The number of percolations in 100 tries
        for _ in range(100):
            grid = grs(size, prob)
            c_grid = colorize(grid)
            if is_percolated(c_grid):
                perc += 1
        data[i] = perc

    return data



def main():
    """Main body"""
    size = [10, 100, 200]
    # size = [10]
    for i in range(len(size)):
        # Iterate for this size
        # LOG
        print("==> Iterating for size", size[i])
        my_data = iter_prob(size[i])

        # Make dataframe and save to csv
        print("==> Making DataFrame and saving to csv")
        my_df = pd.DataFrame(data=my_data)
        my_df.to_csv("my_data" + str(size[i]) + ".csv", index=False)





    # x_dummy = np.linspace(0.05, 1, 20)
    # plt.plot(x_dummy, data, ls='', marker='o')
    # plt.show()

    # grid = grs(size, 0.5)
    # c_grid = colorize(grid)
    # while not is_percolated(c_grid):
    #     grid = grs(size, 0.5)
    #     c_grid = colorize(grid)
    # print(c_grid)



if __name__ == "__main__":
    main()
