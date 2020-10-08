#!/usr/bin/env python

"""
This is for Problem 4
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_deposition(length):
    """
    Takes the length of the 1-D surface and outputs a list of mean height.
    """
    # Initialize
    mean_heights = np.zeros((10, 25))
    height_var = np.zeros((10, 25))

    # Do 50000 random particle drops
    for i in range(10):
        canvas = np.zeros(shape=(500, length), dtype=int)
        canvas_height = np.zeros(shape=(length,), dtype=int, order='F')
        color_map = 1
        count = 0
        index = 0
        for _ in range(50000):
            # Change the color every 10 * length drops
            if count == length * 10:
                color_map = - color_map
                count = 0
                mean_heights[i, index] = np.mean(canvas_height)
                height_var[i, index] = np.var(canvas_height)
                index += 1
            # Generate the random position to drop the particle
            rand = np.random.randint(0, length)
            # Take note of the new height of the pillar of particles
            canvas_height[rand] += 1
            count += 1
            # smash the particle in place
            canvas[canvas_height[rand]][rand] = color_map

    return canvas, np.max(canvas_height), mean_heights, height_var


def draw_canvas(canvas, max_height):
    """
    Draw the given table
    """
    fig, ax = plt.subplots(1, 1)
    ax.pcolor(canvas)
    ax.set_ylim(0, np.max(max_height) + 10)
    plt.show()


def draw_variance(variance):
    """
    Plot the variance after finding the error bars :)
    """
    # Find the error bars. Take variance of the data as the error
    yerr = []
    means = []
    for _ in range(variance.shape[1]):
        yerr.append(np.var(variance[:, _]))
        means.append(np.mean(variance[:, _]))
    x_coord = np.linspace(0, 2000, variance.shape[1])
    fig, ax = plt.subplots(1, 1)
    ax.errorbar(x_coord, means, yerr=yerr, ls = '--')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


def main():
    """
    Main body of our program
    """
    table, maxhei, mean_heights, height_vars = generate_deposition(200)
    draw_canvas(table, maxhei)
    draw_variance(height_vars)
    print(mean_heights)
    print(height_vars)


if __name__ == "__main__":
    main()
