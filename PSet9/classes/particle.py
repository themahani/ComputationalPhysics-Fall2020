#!/usr/bin/env python

""" Implementing particle in the MD system """

import numpy as np

class Particle:
    """ particle """
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.x_vel = np.random.uniform(-3, 3)
        self.y_vel = np.random.uniform(-3, 3)

    def leonard_jones(self, other):
        return

    def velocity_verlat(self, *other):
        
