#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.spatial.distance import squareform, pdist


def timestep():
    dots[:, :2] += dots[:, 2:]

    cross_right = dots[:, 0] > 1
    cross_left = dots[:, 0] < 0
    cross_up = dots[:, 1] > 1
    cross_down = dots[:, 1] < 0

    dots[cross_right | cross_left, 2] *= -1
    dots[cross_up | cross_down, 3] *= -1

    dots[cross_right, 0] = 1
    dots[cross_left, 0] = 0
    dots[cross_up, 1] = 1
    dots[cross_down, 1] = 0

def collision():
    dist_mat = squareform( pdist(dots[:, :2], 'euclidean' )) # Distance matrix

    ind1, ind2 = np.where(dist_mat < 0.01)
    # make unique
    unique = ( ind1 < ind2 )
    ind1 = ind1[unique]
    ind2 = ind2[unique]

    for i1, i2 in zip(ind1, ind2):
        dots[i1, 2:] *= -1
        dots[i2, 2:] *= -1
    # collided = dist_mat < 0.2
    # collided = np.sum(collided, axis=1) > 1


def animate(i):
    timestep()
    collision()
    line.set_data(xs, ys)
    ax.set_title('step = %s' %i)
    return line,


num_particle = 100
dots = np.random.rand(num_particle, 4)

v0 = 0.01

dots[:, 2] = v0 * np.cos(2 * np.pi * dots[:, 3])
dots[:, 3] = v0 * np.cos(2 * np.pi * dots[:, 3])


fig, ax = plt.subplots()


ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

xs = dots[:, 0]
ys = dots[:, 1]

line, = ax.plot([], [], 'b.', ms=8)

ani = animation.FuncAnimation(fig, animate, interval=20, blit=False)

plt.show()
