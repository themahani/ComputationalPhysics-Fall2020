#!/usr/bin/env python

"""
simulate a 2d random walker with equal probability to move in any
of the 4 major directions. then prove the equation in question 5
"""

import numpy as np
from matplotlib import pyplot as plt


class Drunk:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0

    def topple(self):
        """topple in the major directions"""
        rand = np.random.uniform()

        if rand < 0.25:
            # go left
            self.x_pos -= 1
        elif rand < 0.5:
            # go right
            self.x_pos += 1
        elif rand < 0.75:
            # go up
            self.y_pos += 1
        else:
            # go down
            self.y_pos -= 1

    def get_rad_sq(self):
        """return radius squared"""
        return self.x_pos ** 2 + self.y_pos ** 2


def main():
    """main body"""
    rads = np.zeros((1000, 10), dtype=float)
    # loop 1000 times to mean over later
    for rep in range(1000):
        my_girl = Drunk()

        for time in range(10):
            for _ in range(100):
                my_girl.topple()
            rads[rep, time] = my_girl.get_rad_sq()

    my_girl_mean = np.mean(rads, axis=0)

    plt.plot(np.linspace(1, 10, 10), my_girl_mean,
             ls='', marker='o', color='y')
    plt.xlabel('time')
    plt.ylabel('mean radius squared < r^2 >')
    plt.title('mean squared radius over time (intervals of 100)')
    plt.savefig("2d_girl.jpg", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
