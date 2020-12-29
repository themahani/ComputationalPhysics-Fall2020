#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.spatial.distance import squareform, pdist


class MD_system:
    def __init__(self):
        self.num_particle = 100
        self.dots = np.random.rand(self.num_particle, 4)

        # make the particles to be in the left half of the box in order
        xs = np.repeat(np.linspace(0.1, 0.45, 10), 10)
        ys = np.tile(np.linspace(0.1, 0.9, 10), 10)
        self.dots[:, 0] = xs.copy()
        self.dots[:, 1] = ys.copy()

        self.v0 = 0.05  # initial total velocity of the particles
        # random direction for the velocity of the particles
        self.dots[:, 2] = self.v0 * np.cos(2 * np.pi * self.dots[:, 3])
        self.dots[:, 3] = self.v0 * np.cos(2 * np.pi * self.dots[:, 3])

    def timestep(self):
        self.dots[:, :2] += self.dots[:, 2:]

        cross_right = self.dots[:, 0] > 1
        cross_left = self.dots[:, 0] < 0
        cross_up = self.dots[:, 1] > 1
        cross_down = self.dots[:, 1] < 0

        self.dots[cross_right | cross_left, 2] *= -1
        self.dots[cross_up | cross_down, 3] *= -1

        self.dots[cross_right, 0] = 1
        self.dots[cross_left, 0] = 0
        self.dots[cross_up, 1] = 1
        self.dots[cross_down, 1] = 0

    def collision(self):
        # find the distance matrix of the particles
        dist_mat = squareform( pdist(self.dots[:, :2], 'euclidean' )) # Distance matrix

        ind1, ind2 = np.where(dist_mat < 0.01)
        # make unique
        unique = ( ind1 < ind2 )
        ind1 = ind1[unique]
        ind2 = ind2[unique]

        for i1, i2 in zip(ind1, ind2):
            self.dots[i1, 2:] *= -1
            self.dots[i2, 2:] *= -1
        # collided = dist_mat < 0.2
        # collided = np.sum(collided, axis=1) > 1

def test():
    """ test the class """

    def animate(i):
        """ function to animate """
        md.timestep()
        md.collision()
        line.set_data(xs, ys)
        ax.set_title('step = %s' %i)
        return line,


    md = MD_system()

    fig, ax = plt.subplots()


    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    xs = md.dots[:, 0]
    ys = md.dots[:, 1]

    line, = ax.plot([], [], 'b.', ms=8)

    ani = animation.FuncAnimation(fig, animate, interval=20, blit=False)

    plt.show()

if __name__ == "__main__":
    test()
