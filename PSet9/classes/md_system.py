#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.spatial.distance import squareform, pdist


class MDSystem:
    """ a class containing everything about the MD system """
    def __init__(self):
        self.dim = 2
        self.num_particle = 100     # number of particles in the system
        self.dots = np.random.rand(self.num_particle, 4)
        self.size = 30      # size of the box containing the particles

        # make the particles to be in the left half of the box in order
        xs = np.repeat(np.linspace(0.1, 0.45, 10), 10)
        ys = np.tile(np.linspace(0.1, 0.9, 10), 10)
        # xs = np.array([0.05, 0.1, 0.05, 0.1])
        # ys = np.array([0.05, 0.05, 0.1, 0.1])
        self.dots[:, 0] = xs.copy()
        self.dots[:, 1] = ys.copy()
        self.dots[:, :self.dim] = self.size * self.dots[:, :self.dim]
        print(self.dots[:, :self.dim])

        # store relative position (x, y) of particles
        self.dist_data = np.zeros((self.num_particle, self.num_particle,
                                   self.dim))
        self.update_rel_pos()   # update dist_data

        self.init_vel = 3 # initial total velocity of the particles
        # random direction for the velocity of the particles
        self.dots[:, 2] = self.init_vel * np.cos(2 * np.pi * self.dots[:, 3])
        self.dots[:, 3] = self.init_vel * np.sin(2 * np.pi * self.dots[:, 3])
        self.stabilize_system() # Make sure that the system is stationary in LAB frame

        self.accel = self.calc_accel()  # calculate the acceleration of particles

    def vel_center(self):
        """ return the velocity of CoM """
        return np.mean(self.dots[:, self.dim:], axis=0)

    def stabilize_system(self):
        """ make speed of CoM to be zero """
        vel_center = self.vel_center()
        print(f'[Info]:MD:Stabilize system: CoM velocity = {vel_center}')
        self.dots[:, self.dim:] -= vel_center

    def update_rel_pos(self):
        """ calc relative x and y for each particle correlation """
        r_c = 2.5   # cutoff radius


        for i in range(self.dim):  # find particle correlation within r_c for x and y
            for x_ind, x in enumerate(self.dots[:, i]):
                rel_pos = -self.dots[:, i] + x      # take distance of particles
                rel_pos = (rel_pos + r_c) % self.size - r_c # minimum distance of particles and reflections
                self.dist_data[x_ind, :, i] = rel_pos   # update data for class

    def calc_accel(self):
        """ return the acceleration of the particles """
        r_c = 2.5   # cutoff radius
        self.update_rel_pos()
        # print('[Info]:MD:calc_accel: rel pos is:\n', self.dist_data)
        # calculate distance r**2 = x**2 + y**2
        rel_dist_sq = np.zeros((self.num_particle, self.num_particle))
        for i in range(self.dim):
            rel_dist_sq += self.dist_data[:, :, i] ** 2

        non_zero = rel_dist_sq != 0    # non zeros values of distance

        is_in = np.all(np.absolute(self.dist_data) < r_c, axis=2)

        # print(non_zero)
        accel = np.zeros((self.num_particle, self.dim))
        for i in range(self.dim):
            for j in range(self.num_particle):
                accel[j, i] = np.sum(-4 * (-12 / rel_dist_sq[j, non_zero[j] & is_in[j]] ** 7 +
                                    6 / rel_dist_sq[j, non_zero[j] & is_in[j]] ** 4) * \
                    self.dist_data[j, non_zero[j] & is_in[j], i])
        # print('[Info]:MD:calc_accel: accel is: \n', accel)

        return accel


    def timestep(self):
        """ evolve the system by 1 time step using verlet """
        _h = 0.001     # value of time step
        dim = self.dim
        self.dots[:, :dim] += self.dots[:, dim:] * _h + 0.5 * self.accel * _h ** 2   # update position
        self.dots[:, dim:] += self.accel * _h * 0.5   # update speed partially
        self.accel = self.calc_accel()  # update acceleration of particles
        self.dots[:, dim:] += 0.5 * self.accel * _h # update final speed

        # masking
        cross_right = self.dots[:, 0] > self.size
        cross_left = self.dots[:, 0] < 0
        cross_up = self.dots[:, 1] > self.size
        cross_down = self.dots[:, 1] < 0

        # box boundary conditions
        # self.dots[cross_right, 0] = self.size
        # self.dots[cross_left, 0] = 0
        # self.dots[cross_up, 1] = self.size
        # self.dots[cross_down, 1] = 0

        # self.dots[cross_down | cross_up, 3] *= -1
        # self.dots[cross_right | cross_left, 2] *= -1

        # periodic boundary conditions
        self.dots[cross_right, 0] = 0
        self.dots[cross_left, 0] = self.size
        self.dots[cross_up, 1] = 0
        self.dots[cross_down, 1] = self.size

    def kinetic(self):
        """ return the total kinetic energy of the system """
        return 0.5 * np.sum(self.dots[:, 2] ** 2 + self.dots[:, 3] ** 2)

    def energy(self):
        """ return the total energy of the system of particles """
        # find the distance matrix of the particles
        # dist_mat = squareform( pdist(self.dots[:, :2], 'euclidean' )) # Distance matrix

        dist_mat = np.zeros((self.num_particle, self.num_particle))
        for i in range(self.dim):
            dist_mat += self.dist_data[:, :, i] ** 2
        dist_mat = np.sqrt(dist_mat)
        r_c = 2.5
        is_in = np.all(np.absolute(self.dist_data) < r_c, axis=2)

        return self.kinetic() + \
            np.sum(potential(dist_mat[dist_mat != 0 & is_in])) / 2

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
    print('[Info]:main: md particle data :\n', md_sys.dots)
    print('[Info]:main: md accel at time 0 is:\n', md_sys.accel)
    print('[Info]:main: md relative x, y in time 0 is:\n', md_sys.dist_data)


def test():
    """ test the class """
    # Preloading
    end = 1000
    md_sys = MDSystem()

    center_vels = np.zeros((end, md_sys.dim))
    energy = np.zeros(end)
    for i in range(end):
        for _ in range(10):
            md_sys.timestep()
        center_vels[i] = md_sys.vel_center()
        energy[i] = md_sys.energy()

    plt.plot(np.linspace(1, end, end), center_vels[:, 0], label=r'$v_x$')
    plt.plot(np.linspace(1, end, end), center_vels[:, 1], label=r'$v_y$')
    plt.legend()
    plt.savefig("CoM_vel.jpg", dpi=200, bbox_inches='tight')
    plt.show()

    plt.plot(np.linspace(1, end, end), energy, label='energy')
    plt.legend()
    plt.savefig("energy.jpg", dpi=200, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    test()