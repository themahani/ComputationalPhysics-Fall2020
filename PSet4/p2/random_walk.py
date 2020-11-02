#!/usr/bin/env python

"""
generate a random walk to prove the equation.
"""
import numpy as np
from matplotlib import pyplot as plt


def gen_rand(prob):
    """ Decide where to go """
    if np.random.uniform() < prob:
        return 1        # move right
    else:
        return -1       # move left


def rw_next(cur_pos, probability):
    """evolve"""
    return cur_pos + gen_rand(probability)


def rw_simul(prob):
    """simulate RW for prob as probability of going left"""
    x_pos = np.zeros((10000, 10))

    for i in range(10000):
        pos = 0

        for j in range(10):
            for _ in range(100):
                pos = rw_next(pos, prob)

            x_pos[i, j] = pos

    x_mean = np.mean(x_pos, axis=0)
    sigma = np.mean(x_pos ** 2, axis=0) - x_mean

    return x_mean, sigma


def main():
    """main body"""
    sigmas = np.zeros((3, 10), dtype=float)
    x_means = np.zeros((3, 10), dtype=float)

    probs = [0.2, 0.35, 0.5]
    time = np.linspace(10, 1000, 10)

    for i in range(3):
        print("==> simulating for", probs[i])
        x_means[i], sigmas[i] = rw_simul(probs[i])

    print("==> plotting graphs")
    plt.plot(time, x_means[0], ls='', marker='o', color='b', label='p = 0.2')
    plt.plot(time, x_means[1], ls='', marker='o', color='r', label='p = 0.35')
    plt.plot(time, x_means[2], ls='', marker='o', color='g', label='p = 0.5')
    plt.xlabel('time')
    plt.ylabel('<x>')
    plt.title('mean of x over time for different p')
    plt.legend()
    plt.savefig("x_means.jpg", bbox_inches='tight')
    plt.close()

    plt.plot(time, sigmas[0], ls='', marker='^', color='b', label='p = 0.2')
    plt.plot(time, sigmas[1], ls='', marker='^', color='r', label='p = 0.35')
    plt.plot(time, sigmas[2], ls='', marker='^', color='g', label='p = 0.5')
    plt.xlabel('time')
    plt.ylabel('sigmas')
    plt.title('mean of x over time for different p')
    plt.legend()
    plt.savefig("sigmas.jpg", bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    main()
