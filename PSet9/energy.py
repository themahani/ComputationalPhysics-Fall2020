#!/usr/bin/env python

""" analysis of the MD system """

from matplotlib import pyplot as plt
import numpy as np
from classes.md_system import MDSystem


def main():
    """ main body """
    # initial data
    size = 30
    num_particle = 100
    xs = np.repeat(np.linspace(0.1, 0.45, 10), 10)
    ys = np.tile(np.linspace(0.1, 0.9, 10), 10)
    init_pos = np.vstack((xs * size, ys * size))
    kargs = {
            'num': 100,
            'L': 30,
            'init_pos': init_pos.T,
            'init_vel': 0.5
            }

    system = MDSystem(**kargs)  # instaciating the system
    num = 10000

    kinetic = np.zeros(num)
    potential = np.zeros(num)
    left_side = np.zeros(num)

    for i in range(num):
        print(f"\r [Info]:main:timestep {i}", end='')
        system.timestep()   # evovle system
        left_side[i] = np.sum(system.dots[:, 0] < system.size / 2.0) # number of particles on the left side
        kinetic[i] = system.kinetic()   # kinetic energy of the system
        potential[i] = system.potential()   # potential energy of the system

    x_axis = np.linspace(1, num, num)
    # plot energies
    plt.plot(x_axis, potential, label=r'potential $V$')
    plt.plot(x_axis, kinetic, label=r'kinetic $K$')
    plt.plot(x_axis, kinetic + potential, label=r'energy $K + V$')
    plt.legend()
    plt.savefig(f"results/energy_conservation{system.num_particle}_{num}.jpg",
                dpi=200, bbox_inches='tight')
    plt.show()

    # plot particles on the left side of the system
    plt.plot(np.linspace(1, num, num), left_side)
    plt.xlabel(r'time ($10^{-3} \tau$)')
    plt.ylabel('number of particles on the left side of the box')
    plt.title(f"total number of particles = {system.num_particle}")
    plt.grid()
    plt.savefig(f"results/particles_on_left{system.num_particle}_{num}.jpg", dpi=200, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
