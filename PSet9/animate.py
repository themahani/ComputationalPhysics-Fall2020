#!/usr/bin/env python

""" animate the MD system in the Gas, Liquid, and Crystal phases """

from classes.md_system import MDSystem
import numpy as np


def main():
    """ main body """
    # initial data
    size = 30
    num_particle = 100
    xs = np.repeat(np.linspace(0.1, 0.45, 10), 10)
    ys = np.tile(np.linspace(0.1, 0.9, 10), 10)
    init_pos = np.vstack((xs * size, ys * size))
    kargs = {
            'num': num_particle,
            'L': size,
            'init_pos': init_pos.T,
            'init_vel': 3
            }

    system = MDSystem(**kargs)  # instantiating the system
    for _ in range(2000):
        system.timestep()

    print("[Info]:main: Start animating system")
    system.animate_system("animations/gas_phase")



if __name__ == "__main__":
    main()
