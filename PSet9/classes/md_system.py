#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.spatial.distance import squareform, pdist


class MDSystem:
    """ a class containing everything about the MD system """
    def __init__(self):
        self.num_particle = 100     # number of particles in the system
        self.dots = np.random.rand(self.num_particle, 4)
        self.size = 30      # size of the box containing the particles

        # make the particles to be in the left half of the box in order
        xs = np.repeat(np.linspace(0.1, 0.45, 10), 10)
        ys = np.tile(np.linspace(0.1, 0.9, 10), 10)
        self.dots[:, 0] = xs.copy()
        self.dots[:, 1] = ys.copy()
        self.dots[:, :2] = self.size * self.dots[:, :2]

        self.dist_mat = None    # Define the distance matrix for the particles

        # euclidean distance matrix for the particles
        self.dist_mat = squareform( pdist(self.dots[:, :2], 'euclidean' )) # Distance matrix

        self.init_vel = 0.05  # initial total velocity of the particles
        # random direction for the velocity of the particles
        self.dots[:, 2] = self.init_vel * np.cos(2 * np.pi * self.dots[:, 3])
        self.dots[:, 3] = self.init_vel * np.cos(2 * np.pi * self.dots[:, 3])
        self.stabilize_system() # Make sure that the system is stationary in LAB frame

        self.accel = self.calc_accel()  # calculate the acceleration of particles

    def stabilize_system(self):
        """ make speed of CoM to bee zero """
        vel_center = np.sum(self.dots[:, 2:], axis=0)
        print(f'[Info]:MD:Stabilize system: CoM velocity = {vel_center}')
        self.dots[:, 2:] -= vel_center

    def calc_accel(self):
        """ return the acceleration of the particles """
        # find the distance matrix of the particles
        self.dist_mat = squareform( pdist(self.dots[:, :2], 'euclidean' )) # Distance matrix

        r_c = 2.5   # cutoff radius

        for x_ind, x in enumerate(self.dots[:, 0]):
            rel_pos = self.dots[:, 0] - x
            rel_pos[rel_pos < self.size / 2] += self.size
        return 0

    def timestep(self):
        """ evolve the system by 1 time step using verlet """
        _h = 0.0001     # value of time step
        self.dots[:, :2] += self.dots[:, 2:] * _h + 0.5 * self.accel * _h ** 2   # update position
        self.dots[:, 2:] += self.accel * _h * 0.5   # update speed partially
        self.accel = self.calc_accel()  # update acceleration of particles
        self.dots[:, 2:] += 0.5 * self.accel() * _h # update final speed

        # periodic boundary conditions
        cross_right = self.dots[:, 0] > self.size
        cross_left = self.dots[:, 0] < 0
        cross_up = self.dots[:, 1] > self.size
        cross_down = self.dots[:, 1] < 0

        self.dots[cross_right, 0] = 0
        self.dots[cross_left, 0] = self.size
        self.dots[cross_up, 1] = 0
        self.dots[cross_down, 1] = self.size

    def collision(self):
        """ simulate the interaction of the particles to update the velocities """
        # find the distance matrix of the particles
        self.dist_mat = squareform( pdist(self.dots[:, :2], 'euclidean' )) # Distance matrix

        ind1, ind2 = np.where(self.dist_mat < 0.5)
        # make unique
        unique = ( ind1 < ind2 )
        ind1 = ind1[unique]
        ind2 = ind2[unique]

        for i1, i2 in zip(ind1, ind2):
            self.dots[i1, 2:] *= -1
            self.dots[i2, 2:] *= -1
        # collided = dist_mat < 0.2
        # collided = np.sum(collided, axis=1) > 1

    def kinetic(self):
        """ return the total kinetic energy of the system """
        return 0.5 * np.sum(self.dots[:, 2] ** 2 + self.dots[:, 3] ** 2)

    def energy(self):
        """ return the total energy of the system of particles """
        return self.kinetic() + \
            np.sum(potential(self.dist_mat[self.dist_mat != 0])) / 2

    def animate_system(self):
        """ animate the MD simulation and present it """
        def animate(i):
            """ function to animate """
            self.timestep()
            self.collision()
            line.set_data(x_particles, y_particles)
            ax.set_title('step = %s' % i)
            return line,

        fig, ax = plt.subplots()

        ax.set_xlim(0, self.size)
        ax.set_ylim(0, self.size)

        x_particles = self.dots[:, 0]
        y_particles = self.dots[:, 1]

        line, = ax.plot([], [], 'b.', ms=8)

        ani = animation.FuncAnimation(fig, animate, interval=20, blit=False)

        plt.show()


def potential(dist):
    """ take distance r of particles and return the leonard-jones potential """
    return 4 * ( 1 / dist ** 12 - 1 / dist ** 6 )


def test():
    """ test the class """


    md_sys = MDSystem()
    md_sys.animate_system()

    # end_time = 1000

    # energy = np.zeros(end_time)
    # kinetic = np.zeros(end_time)

    # for i in range(end_time):
    #     md_sys.timestep()
    #     md_sys.collision()
    #     energy[i] = md_sys.energy()
    #     kinetic[i] = md_sys.kinetic()

    # plt.plot(np.linspace(1, end_time, end_time), energy)
    # plt.show()

if __name__ == "__main__":
    test()
