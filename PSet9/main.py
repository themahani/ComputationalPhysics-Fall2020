#!/usr/bin/env python

""" run and store data in file """

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
            'init_vel': 1.5
            }

    system = MDSystem(**kargs)  # instantiating the system

    for _ in range(2000):
        system.timestep()

    num = 5000
    velocity = np.zeros((num, system.num_particle, system.dim))

    for i in range(num):
        print(f"\r[Info]:main: step {i} of {num}", end='')
        system.timestep()
        system.timestep()
        velocity[i] = system.dots[:, system.dim:]

    np.save(f"data/velocity{system.num_particle}_{num}.npy", velocity)


if __name__ == "__main__":
    main()
