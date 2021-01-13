#!/usr/bin/env python

""" plot the energy vs. temperature plot and find the phase transitions """

import numpy as np
from matplotlib import pyplot as plt


def main():
    """ main body """
    temps = np.load("data/temps_phase_transition.npy")
    energy = np.load("data/energies_phase_transition.npy")
    print(temps)

    plt.errorbar(x=temps[:, 0], y=energy)
    plt.show()


if __name__ == "__main__":
    main()
