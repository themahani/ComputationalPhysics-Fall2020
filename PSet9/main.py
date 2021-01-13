#!/usr/bin/env python

""" run and store data in file """

from classes.md_system import MDSystem
import numpy as np


def simulate_system(init_vel):
    """ simulate the system for init_vel and take temp. and energy"""
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
            'init_vel': init_vel
            }

    system = MDSystem(**kargs)  # instantiating the system

    # wait for system to reach equilibrium
    for _ in range(5000):
        system.timestep()

    energy = system.energy()
    temp = np.zeros(1000)
    for i in range(1000):
        for _ in range(10):
            system.timestep()
        temp[i] = system.temp()

    return energy, np.mean(temp), np.std(temp)


def main():
    """ main body """
    velocity = np.linspace(0.1, 2, 40)

    temps = np.zeros((40, 2))
    energies = np.zeros(40)

    for index, init_vel in enumerate(velocity):
        print(f"\r[Info]:main: Simulating for the {index + 1}th system of 40 ", end='')
        energies[index], temps[index, 0], temps[index, 1] = \
            simulate_system(init_vel)
        print(f" {temps[index, 0]}")

    np.save("data/temps_phase_transition.npy", temps)
    np.save("data/energies_phase_transition.npy", energies)


if __name__ == "__main__":
    main()
