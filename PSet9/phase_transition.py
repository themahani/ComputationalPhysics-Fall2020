#!/usr/bin/env python

""" plot the energy vs. temperature plot and find the phase transitions """

import numpy as np
from matplotlib import pyplot as plt


def main():
    """ main body """
    temps = np.load("data/temps_phase_transition.npy")
    energy = np.load("data/energies_phase_transition.npy")
    print(temps)
    pressure = np.load('data/pressure_phase_transition.npy')

    plt.errorbar(x=temps[:, 0], y=energy, xerr=temps[:, 1])
    plt.xlabel("T")
    plt.ylabel("E")
    plt.title("E vs. T plot to see phase transition")
    plt.savefig("results/phase_transition.jpg", dpi=200, bbox_inches='tight')
    plt.show()

    plt.errorbar(x=temps[:, 0], y=pressure[:, 0], xerr=temps[:, 1], yerr=pressure[:, 1], ls='-.', c='g', marker='o')
    plt.xlabel("T")
    plt.ylabel("P")
    plt.title("Pressure vs. Temp.")
    plt.savefig("results/pressure_temp.jpg")
    plt.show()


if __name__ == "__main__":
    main()
