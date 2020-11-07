#!/usr/bin/env python

"""Here we simulate the deterministic trapped RW"""

from matplotlib import pyplot as plt
import numpy as np


def go_til_death(index):
    """find mean life if start from index in path"""
    lifetime = 0
    mean_lifetime = 0
    # Initialize path
    path_prob = np.zeros(shape=(22, ), dtype=float)
    path_prob[index + 1] = 1
    # while not alive prob is more than 0.01:
    while path_prob[0] + path_prob[21] < 0.99:
        lifetime += 1
        # initialize tmp
        tmp = [0] * 22
        tmp[0] = path_prob[0]
        tmp[21] = path_prob[21]
        # loop over the list to find prob of next move
        for i in range(1, len(path_prob) - 1):
            tmp[i - 1] += path_prob[i] * 0.5
            tmp[i + 1] += path_prob[i] * 0.5
        # refresh path_prob
        path_prob = tmp.copy()
        mean_lifetime += np.sum(path_prob[1:21])
    return mean_lifetime



def main():
    """main body"""
    mean_lifes = np.zeros((20, ))

    for i in range(20):
        mean_lifes[i] = go_til_death(i)


    plt.plot(np.linspace(1, 20, 20), mean_lifes, ls='', marker='o')
    plt.xlabel('index in path')
    plt.ylabel('mean lifetime')
    plt.title('mean life over index in deterministic alg')
    plt.savefig('rw_trap.jpg', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    import profile
    profile.run("main()")
