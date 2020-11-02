#!/usr/bin/enb python

"""
do whatever the question says
"""

import numpy as np
from matplotlib import pyplot as plt


class RandWalker:
    def __init__(self):
        self.x = 100
        self.y = 199

    def reset(self):
        """reset the position, instead of recreating particle"""
        self.x = 100
        self.y = 199

    def neighbor(self, grid):
        """if cell on in neighbor, return 1, else 0"""
        # check the major 4 directions as neighbors to be on/off
        if self.y > 198:
            return 0
        for diff in [-1, 1]:
            if grid[self.y + diff, self.x] != 0:
                return 1
            elif grid[self.y, (self.x + diff) % 201] != 0:
                return 1

        return 0

    def move(self):
        """2d rand. walk"""
        rand = np.random.uniform()
        if rand < 0.25:
            # go left
            self.x -= 1
        elif rand < 0.5:
            # go right
            self.x += 1
        elif rand < 0.75:
            # go up
            self.y += 1
        else:
            # go down
            self.y -= 1
        # check to see if out of buffer distance
        if self.y > 209:
            self.reset()
        # periodic conditions
        if self.x == 201:
            self.x = 0
        elif self.x == -1:
            self.x = 200

    def attach_par(self, grid, color):
        """random walk the particle and attach it"""
        while not self.neighbor(grid):
            self.move()

        grid[self.y, self.x] = color
        return grid


def main():
    """main body"""
    grid = np.zeros((200, 201), dtype=int)
    # turn the lowest row on as the seed
    grid[0, :] = 1
    counter = 0
    color = 1
    for _ in range(2000):
        if counter == 100:
            counter = 0
            color += 1

        particle = RandWalker()
        grid = particle.attach_par(grid, color)
        print("==> attached one particle", _)

    plt.pcolor(grid)
    plt.savefig("ald.jpg", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
