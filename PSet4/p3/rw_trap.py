#!/usr/bin/env python

"""
simulate the random walk with traps at both sides and return
the mean life time
"""
import numpy as np
from matplotlib import pyplot as plt
from sys import setrecursionlimit

setrecursionlimit(100000)


class Drunk:
    """My random walker :)"""
    def __init__(self, pos):
        self.pos = pos
        self.lifetime = 0


    def die(self):
        return 0

    def topple(self):
        self.lifetime += 1
        # decided on right
        if np.random.uniform() < 0.5:
            # jumped to death
            if self.pos == 19:
                self.die()
            else:
                # keep toppling left and right and living
                self.pos += 1
                self.topple()
        # decided on left
        else:
            # jumped to death
            if self.pos == 0:
                self.die()
            else:
                # live a little more
                self.pos -= 1
                self.topple()


def main():
    """main body"""
    lifetimes = np.zeros((10000, 20), dtype=int)
    for pos in range(20):

        for rep in range(10000):
            my_man = Drunk(pos)
            my_man.topple()
            lifetimes[rep, pos] = my_man.lifetime

    mean_life = np.mean(lifetimes, axis=0)

    # plt.plot(np.linspace(0, 19, 20), mean_life, ls='', marker='o', color='y')
    # plt.xlabel('initial position')
    # plt.ylabel('mean lifetime')
    # plt.title('mean lifetime of drunk random walker over the initial position')
    # plt.savefig("drunk.jpg", bbox_inches='tight')
    # plt.show()


if __name__ == "__main__":
    import profile
    profile.run("main()")
