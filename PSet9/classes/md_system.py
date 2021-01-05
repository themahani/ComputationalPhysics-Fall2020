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

        # store relative position (x, y) of particles
        self.dist_data = np.zeros((self.num_particle, self.num_particle, 2))
        self.update_rel_pos()   # update dist_data

        self.init_vel = 3  # initial total velocity of the particles
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

    def update_rel_pos(self):
        """ calc relative x and y for each particle correlation """
        r_c = 2.5   # cutoff radius


        for i in range(2):  # find particle correlation within r_c for x and y
            for x_ind, x in enumerate(self.dots[:, i]):
                rel_pos = -self.dots[:, i] + x
                is_out = np.absolute(rel_pos) > r_c  # particle out of r_c
                reflection_out = np.absolute(rel_pos - self.size) > r_c # reflection out of r_c
                reflection_in = np.absolute(rel_pos - self.size) < r_c  # reflection inside r_c
                rel_pos[is_out & reflection_out] = 0    # if both the particle and its reflection out, then zeros
                rel_pos[np.all([is_out & reflection_in, rel_pos > 0], 0)] = \
                    rel_pos[is_out & reflection_in] - self.size
                rel_pos[np.all([is_out & reflection_in, rel_pos < 0], 0)] = \
                    rel_pos[is_out & reflection_in] + self.size
                self.dist_data[x_ind, :, i] = rel_pos   # update data for class

    def calc_accel(self):
        """ return the acceleration of the particles """
        self.update_rel_pos()
        # calculate distance r**2 = x**2 + y**2
        rel_dist = self.dist_data[:, :, 0] ** 2 + \
            self.dist_data[:, :, 1 ** 2]
        non_zero = rel_dist != 0    # non zeros values of distance
        accel = np.zeros((self.num_particle, 2))
        for i in range(2):
            for j in range(self.num_particle):
                accel[j] = np.sum(-4 * (-12 / rel_dist[j, non_zero[j]] ** 14 +
                                    6 / rel_dist[j, non_zero[j]] ** 8) * \
                    self.dist_data[j, non_zero[j], i])

        return accel


    def timestep(self):
        """ evolve the system by 1 time step using verlet """
        _h = 0.0001     # value of time step
        self.dots[:, :2] += self.dots[:, 2:] * _h + 0.5 * self.accel * _h ** 2   # update position
        self.dots[:, 2:] += self.accel * _h * 0.5   # update speed partially
        self.accel = self.calc_accel()  # update acceleration of particles
        self.dots[:, 2:] += 0.5 * self.accel * _h # update final speed

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
            for _ in range(100):
                self.timestep()
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


def print_system_info(md_sys):
    """ print rel pos and accel of particles """
    print('[Info]:main: md accel at time 0 is:\n', md_sys.accel)
    print('[Info]:main: md relative x, y in time 0 is:\n', md_sys.dist_data)


def test():
    """ test the class """
    md_sys = MDSystem()
    for _ in range(5000):
        md_sys.timestep()
    print_system_info(md_sys)
    md_sys.stabilize_system()
    # md_sys.animate_system()

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
