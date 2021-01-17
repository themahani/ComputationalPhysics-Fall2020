#!/usr/bin/env python

""" main module """

import numpy as np
import matplotlib.pyplot as plt
from classes.system import System, simulate_system


def main():
    """ main body """
    utility_matrix = np.array([[2, 10], [0, 8]])
    end = 10
    data = np.zeros((10, end))
    betas = np.linspace(0.1, 1, 10)
    for index, beta in enumerate(betas):
        data[index] = simulate_system(beta, end, utility_matrix.T, 0)

    # plot Q vs. beta
    for i in range(10):
        plt.plot(np.linspace(1, end, end), data[i], 'o--', label=f"beta = {betas[i]}")
    plt.xlabel("time")
    plt.ylabel("Q")
    plt.grid()
    plt.legend()
    plt.savefig("results/Q_t_betas_inverted.jpg", dpi=200, bbox_inches='tight')
    plt.show()

    # get betas for rev
    end = 30
    p_rev = 0.05
    data = np.zeros((10, end))
    for index, beta in enumerate(betas):
        data[index] = simulate_system(beta, end, utility_matrix, p_rev)

    # plot Q vs. beta
    for i in range(10):
        plt.plot(np.linspace(1, end, end), data[i], 'o--', label=f"beta = {betas[i]}")
    plt.xlabel("time")
    plt.ylabel("Q")
    plt.grid()
    plt.legend()
    plt.savefig("results/Q_t_betas_rev_1.jpg", dpi=200, bbox_inches='tight')
    plt.show()

    # now part 2 of rev
    data = np.zeros((10, end))
    for index, beta in enumerate(betas):
        data[index] = simulate_system(beta, end, utility_matrix.T, p_rev)

    # plot Q vs. beta
    for i in range(10):
        plt.plot(np.linspace(1, end, end), data[i], 'o--', label=f"beta = {betas[i]}")
    plt.xlabel("time")
    plt.ylabel("Q")
    plt.grid()
    plt.legend()
    plt.savefig("results/Q_t_betas_rev_2.jpg", dpi=200, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
