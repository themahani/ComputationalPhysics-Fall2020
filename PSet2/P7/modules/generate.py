"""
Here lie methods to generate random deposition. R.I.P random XD
And also some errorbar calculations
"""

import numpy as np


def find_dist(table_hei):
    i_min = 0
    while table_hei[i_min] == 0:
        i_min += 1
    i_max = i_min
    while table_hei[i_max] != 0 and i_max < 199:
        i_max += 1
    return i_max - i_min


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

    if table_hei[i_max] == 0:
        return 0
    else:
        # Update height of pillar
        table_hei[index] = table_hei[i_max] + 1
        # Smash particle inpalce
        table[table_hei[index], index] = color
        return 1


def generate_dep(length, layer_count, dist, x_coord, ind):
    """
    generate the deposition once
    """
    # Initialize everything
    canvas = np.zeros(shape=(100 * layer_count, length), dtype=int)
    canvas[0, length // 2 + 1] = -1
    # Store the particle height of every position on the surface.
    canvas_height = np.zeros(shape=(length,), dtype=int, order='F')
    canvas_height[length // 2 + 1] += 1
    color_map = 1   # The color of the particles. Changes every 2000 particles
    count = 0       # Count to see when we reach 2000 particles to change color
    index = 0       # Index of mean and variance in which array we store
    # Deposite <layer_count> layers on the surface
    while count < layer_count * 10 * length:
        # Generate the random position to drop the particle
        rand = np.random.randint(0, length)
        # Smash the particle in place
        if deposite_particle(canvas, canvas_height, rand, color_map):
            count += 1
            # Change the color every 10 * length drops
            if count % (length * 10) == 0:
                color_map = - color_map

            if count == 200 * (index + 1):
                # Update longest dist
                dist[ind, index] = find_dist(canvas_height)
                # Update x_coord
                x_coord[index] = count
                index += 1

    return canvas, np.max(canvas_height), dist, x_coord


def generate_deposition(length, layers):
    """
    Takes the layer count to deposite on the surface
    and outputs a list of mean height.
    """
    # Initialize
    n = 10
    size = int(10 * layers * length / 200)
    x_coord = np.zeros((size, ))
    dist = np.zeros((n, size), dtype=int, order='F')

    # Repeat the process for n times
    for i in range(n):
        canvas, max_height,distance, x_ax = generate_dep(length, layers, dist,
                                                          x_coord, i)

    return canvas, max_height, distance, x_ax

def error(array):
    """
    return stdev of items as error
    """
    return np.sqrt(np.var(array))
