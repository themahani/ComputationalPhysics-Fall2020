#!/usr/bin/env python

"""
    calculate the velocity auto-correlation of the system and find the
    relaxation time
"""

import numpy as np
from matplotlib import pyplot as plt


def auto_correlation(arr, tau):
    """ return auto correlation of particles for a seperation value tau """
    auto_cor = np.mean(np.sum(arr[:-tau] * arr[tau:], axis=2))
    auto_cor /= np.mean(np.sum(arr[:-tau] ** 2, axis=2))
    return auto_cor


def main():
    """ main body """
    # velocity = np.fromfile("data/velocity100_5000.txt", sep=", ")
    # velocity = velocity.reshape((5000, 100, 2))
    velocity = np.load('data/velocity100_5000.npy')
    end = np.exp(-1)

    tau = 0
    vel_cor = [auto_correlation(velocity, tau + 1)]
    while vel_cor[-1] > end:
        print(f"\r ==> tau = {tau}", end='')
        tau += 1
        vel_cor.append(auto_correlation(velocity, tau + 1))

    cutoff = tau
    for _ in range(400):
        tau += 1
        vel_cor.append(auto_correlation(velocity, tau + 1))

    print(f"\n\n ==> system relaxation time is: {2 * cutoff}")

    num = len(vel_cor)
    plt.plot(np.linspace(1, num, num), vel_cor, label=r"$C_v(\tau)$")
    plt.plot(np.linspace(1, num, num), [end] * num, label=r"$e^{-1}$")
    plt.xlabel(r"time $(unit = 2 \times 10^{-3})$")
    plt.legend()
    plt.savefig("results/velocity_correlation.jpg")
    plt.show()

if __name__ == "__main__":
    main()
