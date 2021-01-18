#!/usr/bin/env python

""" plot mean neighbors for various area coverage """

import numpy as np
import matplotlib.pyplot as plt
from md import LangevinHarmonic


def main():
    """ main body """
    # doing both part B and C
    lengths = [26.95, 20.37, 19.06, 17.97, 17.05]     # corresponding lengths of the system
    area_percentage = [0.4, 0.7, 0.8, 0.9, 1.0]     # coverage percentage

    ############ Part A ############
    for length_index, length in enumerate(lengths):
        model = LangevinHarmonic(length, 250, 1, 1, 10, 0, (0.5, 0.7), 0.01)
        data = model.render(6000)
        mean_neighbors = data.get_mean_neighbor_values()
        times = np.arange(data.sample_numbers) * data.saving_period * data.h

        plt.plot(times, mean_neighbors, label=f"area% = {area_percentage[length_index]}")
    plt.xlabel(r"Time $(\times \tau)$")
    plt.ylabel(r'Mean Neighbors')
    plt.legend()
    plt.grid()
    plt.savefig(f"results/mean_neighbors.jpg", dpi=200, bbox_inches='tight')
    plt.show()
    plt.close()

    ################# Part B ################
    num = 10    # number of runs to mean over
    eq_mean_neighbors = np.zeros((len(lengths), num))

    for length_index, length in enumerate(lengths):
        for i in range(num):
            model = LangevinHarmonic(length, 250, 1, 1, 10, 0, (0.5, 0.7), 0.01)
            data = model.render(5000)  # simulate system and store data
            eq_mean_neighbors[length_index, i] = data.get_mean_neighbor_values()[-1]

    # plot equalized mean neighbors over area percentage // Part C of the Problem
    plt.errorbar(x=area_percentage, y=np.mean(eq_mean_neighbors, axis=1),
                 yerr=np.std(eq_mean_neighbors, axis=1), ls='-.', marker='o')
    plt.xlabel("Area Percentage")
    plt.ylabel("Equalized mean neighbors")
    plt.grid()
    plt.savefig("results/eq_mean_neighbors.jpg", dpi=200, bbox_inches='tight')
    plt.show()
    plt.close()


if __name__ == "__main__":
    main()
