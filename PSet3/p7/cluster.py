#!/usr/bin/env python

"""Make cluster with probability <prob>"""

import numpy as np
from sys import setrecursionlimit
from matplotlib import pyplot as plt

setrecursionlimit(1000000)


def gen_rand(prob):
    """Generate rand float and decide using prob"""
    rand = np.random.uniform()
    # print(rand)
    if rand < prob:
        return 1
    else:
        return 0


def cluster(index, prob, grid, i, j, area, gyro_rad):
    """Make cluster recursively"""
    # If already in cluster, don't do shit!
    if grid[i, j] == 1 or grid[i, j] == -1:
        return 0
    # Else, if randomly on, turn on and try neighbors
    elif gen_rand(prob):
        # turn cell on
        grid[i, j] = 1

        # add one unit to area
        area[0, index] += 1
        gyro_rad[0, index] += (i - 4999) ** 2 + (j - 4999) ** 2

        # Try the neighbors
        # for i_diff in range(-1, 2):
        #     for j_diff in range(-1, 2):
        #         # Ignore itself
        #         if i_diff == 0 and j_diff == 0:
        #             continue
        #         if grid[i + i_diff, j + j_diff] == 0:
        #             cluster(index, prob, grid,
        #                     i+i_diff, j+j_diff, area, gyro_rad)
        # return 0

        for i_diff in [-1, 1]:
            if grid[i + i_diff, j] == 0:
                cluster(index, prob, grid,
                        i+i_diff, j, area, gyro_rad)
        for j_diff in [-1, 1]:
            if grid[i, j + j_diff] == 0:
                cluster(index, prob, grid,
                        i, j+j_diff, area, gyro_rad)
        return 0

    else:
        grid[i, j] = -1
        return 0


def repeat_stuff():
    """ Repeat the process for probs """
    # probability
    probs = [0.5, 0.55, 0.587]
    size = 10000
    num = 150

    # Initialize area and rad
    areas = []
    gyros = []

    for prob in probs:
        area = np.zeros(shape=(1, num), dtype=float)
        gyro_rad = np.zeros(shape=(1, num), dtype=float)

        print("Looping for", prob)
        # Repeat num times
        for index in range(num):
            # make grid
            grid = np.zeros(shape=(size, size), dtype=bool)
            # make cluster
            # print(index)
            cluster(index, prob, grid, size // 2 - 1, size // 2 - 1,
                    area, gyro_rad)
            if area[0, index] != 0:
                gyro_rad[0, index] /= area[0, index]

        print(np.mean(area), np.mean(np.sqrt(gyro_rad)))

        areas.append(np.mean(area))
        gyros.append(np.mean(np.sqrt(gyro_rad)))

    return np.array(areas), np.array(gyros)


def main():
    """ Main Body """
    probs = np.array([0.5, 0.55, 0.587])
    l_area, l_gyro = repeat_stuff()

    # Fit data for the second plot
    p_opt, p_cov = np.polyfit(np.log10(l_gyro), np.log10(l_area), 1,
                              full=False, cov=True)
    slope = [p_opt[0], np.sqrt(np.diag(p_cov))[0]]
    print("Slope is %.5f" % slope[0], "(+/-) %.5f" % slope[1])

    print("==> Plotting")
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(probs, l_gyro, ls='-.', marker='o')
    ax1.set_xlabel("probability")
    ax1.set_ylabel("gyro mean")
    ax2.plot(np.log10(l_gyro), np.log10(l_area), ls='--',
             marker='^', label='data')

    ax2.set_xlabel("log10(ksi), ksi = gyro rad")
    ax2.set_ylabel("log10(s), s = area")
    print("==> Saving to jpg")
    plt.savefig("area-gyro.jpg", bbox_inches='tight', dpi=500)

    # # !!!! DEBUG !!!!
    # area = np.zeros((1, 1), dtype=int)
    # gyro_rad = np.zeros((1, 1), dtype=float)
    # grid = np.zeros((size, size), dtype=bool)
    # cluster(0, prob, grid, size // 2 - 1, size // 2 - 1, area, gyro_rad)

    # print(area, np.sqrt(gyro_rad))

    # plt.pcolor(grid)
    # plt.show()


if __name__ == "__main__":
    main()
