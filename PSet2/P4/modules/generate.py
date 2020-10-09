"""
Here lie methods to generate random deposition. R.I.P random XD
And also some errorbar calculations
"""

import numpy as np


def generate_dep(layer_count, mean_heights, height_var, ind):
    """
    generate the deposition once
    """
    # Initialize everything
    length = 200        # length of the surface
    canvas = np.zeros(shape=(500, length), dtype=int)   # The canvas
    # Store the particle height of every position on the surface.
    canvas_height = np.zeros(shape=(length,), dtype=int, order='F')
    color_map = 1   # The color of the particles. Changes every 2000 particles
    count = 0       # Count to see when we reach 2000 particles to change color
    index = 0       # Index of mean and variance in which array we store
    # Deposite <layer_count> layers on the surface
    for _ in range(layer_count * 10 * length):
        # Generate the random position to drop the particle
        rand = np.random.randint(0, length)
        # Take note of the new height of the pillar of particles
        canvas_height[rand] += 1
        count += 1
        # Smash the particle in place
        canvas[canvas_height[rand]][rand] = color_map
        # Change the color every 10 * length drops
        if count == length * 10:
            color_map = - color_map
            count = 0
            # Update list of mean heights
            mean_heights[ind, index] = np.mean(canvas_height)
            # take Root Mean Squared (RMS) as height unsteadiness
            height_var[ind, index] = np.sqrt(np.var(canvas_height))
            # next index for the next time we reach here
            index += 1

    return canvas, np.max(canvas_height), mean_heights, height_var


def generate_deposition(layers):
    """
    Takes the layer count to deposite on the surface
    and outputs a list of mean height.
    """
    # Initialize
    n = 10
    mean_heights = np.zeros((n, layers))
    height_var = np.zeros((n, layers))

    # Repeat the process for n times
    for i in range(n):
        canvas, max_height, mean_hei, hei_var = generate_dep(layers, mean_heights, height_var, i)


    return canvas, max_height, mean_hei, hei_var


def error(array):
    """
    return variance over the number of items as error
    """
    return np.var(array) / len(array)
