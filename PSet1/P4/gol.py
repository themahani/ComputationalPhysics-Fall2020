#!/usr/bin/env python

""" This program models the game of life problem.  """

from types import loaf, beacon, glider, eater_glider
from operations import situate, choose


def main():
    """Main body of the program"""
    c_loaf = loaf()
    c_beacon = beacon()
    c_glider = glider()
    c_eater_glider = eater_glider()


def animate(canvas):
    """Animates the table and saves the file as a gif"""
    for i in range(6):
        for j in range(6):
            situation = situate(canvas, i, j)
            choose(situation, canvas[i][j])


if __name__ == "__main__":
    main()
