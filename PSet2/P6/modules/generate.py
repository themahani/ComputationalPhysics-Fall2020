"""
Here lie methods to generate random deposition. R.I.P random XD
And also some errorbar calculations
"""

import numpy as np


def deposite_particle(table, table_hei, index, color):
    """
    Smash the particle using the additional relaxation rule
    """
    i_max = index
    length = len(table_hei)
    # Find the one of 3 pillars with min height
    if table_hei[index] < table_hei[(index + 1) % length]:
        i_max = (index + 1) % length
    elif table_hei[i_max] < table_hei[index - 1]:
        i_max = index - 1

    if i_max == index:
        # Update height of pillar
        table_hei[i_max] += 1
        # Smash particle inplace
        table[table_hei[i_max], i_max] = color
    else:
        # Update height of pillar
        table_hei[index] = table_hei[i_max]
        # Smash particle inpalce
        table[table_hei[index], index] = color


def generate_dep(length, layer_count, x_coord, mean_heights, height_var, ind):
    """
    generate the deposition once
    """
    # Initialize everything
    canvas = np.zeros(shape=(40 * layer_count, length), dtype=int)
    # Store the particle height of every position on the surface.
    canvas_height = np.zeros(shape=(length,), dtype=int, order='F')
    color_map = 1   # The color of the particles. Changes every 2000 particles
    count = 0       # Count to see when we reach 2000 particles to change color
    index = 0       # Index of mean and variance in which array we store
    # Deposite <layer_count> layers on the surface
    for _ in range(layer_count * 10 * length):
        # Generate the random position to drop the particle
        rand = np.random.randint(0, length)
        count += 1
        # Smash the particle in place
        deposite_particle(canvas, canvas_height, rand, color_map)
        # Change the color every 10 * length drops
        if count % (length * 10) == 0:
            color_map = - color_map

        if count == 2 ** (index + 1):
            # Update list of mean heights
            mean_heights[ind, index] = np.mean(canvas_height)
            # take Root Mean Squared (RMS) as height unsteadiness
            height_var[ind, index] = np.sqrt(np.var(canvas_height))
            # Take note of count
            x_coord[index] = count
            # next index for the next time we reach here
            index += 1

    return canvas, np.max(canvas_height),x_coord, mean_heights, height_var


def generate_deposition(length, layers):
    """
    Takes the layer count to deposite on the surface
    and outputs a list of mean height.
    """
    # Initialize
    n = 10
    size = int(np.log2(10 * length * layers))
    mean_heights = np.zeros((n, size))
    height_var = np.zeros((n, size))
    x_coord = np.zeros((size, ))

    # Repeat the process for n times
    for i in range(n):
        canvas, max_height, x_ax, mean_hei, hei_var = generate_dep(length, layers, x_coord, mean_heights, height_var, i)

    return canvas, max_height, x_ax, mean_hei, hei_var


def error(array):
    """
    return stdev of items as error
    """
    return np.sqrt(np.var(array))
