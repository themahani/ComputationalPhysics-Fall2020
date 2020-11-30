#!/usr/bin/env python

"""
here we make classes of 1D and 2D drunk random walkersl
"""
from numpy.random import choice

class rand_walk_1:
    def __init__(self, V_p, L):
        self.speed = V_p
        self.end = L
        self.pos = 0
        self.lifetime = 0

    def next(self):
        """one time step advancement"""
        # random walk
        self.pos += self.speed * choice([-1, 1])
        # one step still alive
        self.lifetime += 1
        # can't go lower that 0
        if self.pos < 0:
            self.pos = 0
        if self.pos > self.end:
            # success
            return 1
        return 0


class rand_walk_2:
    def __init__(self, V_p, L):
        self.x = 0      # horizontal pos
        self.y = L // 2      # vertical pos
        self.end = L    # where it all ends
        self.speed = V_p    # speed at which the random walkers moves
        self.lifetime = 0   # life span of drunk guys and girls :)

    def next(self):
        """ one time step forward """
        # choose horizontal or vertical direction to topple to
        if choice([-1, 1]) == 1:
            # vertical
            self.y += self.speed * choice([-1, 1])
        else:
            # horizontal
            self.x += self.speed * choice([-1, 1])
        if self.x < 0:
            # not less than 0
            self.x = 0
        elif self.y > self.end:
            # periodic boundary condition along the road
            self.y = self.y % self.end

        # one tiem step still alive
        self.lifetime += 1

        # report success
        if self.x > self.end:
            return 1
        # still running
        return 0


def main():
    """ main body """
    my_man = rand_walk_1(1, 10)
    for i in range(20):
        my_man.next()
        print(my_man.lifetime)
        print(my_man.pos, "\n")


if __name__ == "__main__":
    main()
