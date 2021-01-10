#!/usr/bin/env python

""" Analyze the Temperature and Pressure of the MD system. """

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
            'init_pos': init_pos.T
            }

    system = MDSystem(**kargs)  # instantiating the system
    num = 10000

    # temp = np.zeros(num)
    pressure = np.zeros(num)

    for i in range(num):
        print(f"\r [Info]:main:timestep {i}", end='')
        system.timestep()
        # temp[i] = system.temp()
        pressure[i] = system.pressure()

    x_axis = np.linspace(1, num, num)   # time axis
    # plot temp
    # plt.plot(x_axis, temp)
    # plt.xlabel("time")
    # plt.ylabel('temperature T')
    # plt.title(f"number of particles = {system.num_particle}")
    # plt.grid()
    # plt.savefig(f"results/temp{system.num_particle}_{num}.jpg",
    #             dpi=200, bbox_inches='tight')
    # plt.show()

    # plot pressure
    plt.plot(x_axis, pressure)
    plt.xlabel("time")
    plt.ylabel('pressure P')
    plt.title(f"number of particles = {system.num_particle}")
    plt.grid()
    plt.savefig(f"results/pressure{system.num_particle}_{num}.jpg",
                dpi=200, bbox_inches='tight')
    plt.show()



if __name__ == "__main__":
    main()
