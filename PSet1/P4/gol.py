#!/usr/bin/env python

""" This program models the game of life problem.  """

import numpy as np
import matplotlib.animation as ani


def situate(table, i, j):
    """Takes the table and coordinated of the item and gives the sum of
       its neighbors."""
    length = table.shape()[0]
    return np.sum(table[i - 1][j-1:(j+2) % length]) + np.sum(table[(i + 1)
                  % length][j - 1: (j+2) % length]) + table[i][j - 1] + table[i][(j + 1) % length]
    ### Possible Bug! ###


def choose(situation, state):
    """Uses the given rule to decide whether to be 1 or 0 in the next round"""
    if situation == 3 and state == 0:
        return 1
    elif situation in [2, 3] or state == 1:
        return 1
    elif situation not in [2, 3] and state == 1:
        return 0
    else:
        return state


def loaf():
    """Create the canvas with the initial values of the loaf"""
    canvas = np.zeros(shape=(6, 6), dtype=int, order='F')
    # make the loaf
    canvas[1][2] = 1
    canvas[1][3] = 1
    canvas[2][4] = 1
    canvas[3][4] = 1
    canvas[2][1] = 1
    canvas[3][2] = 1
    canvas[4][3] = 1
    return canvas


def beacon():
    """Create the canvas with the initial values of the beacon"""
    canvas = np.zeros(shape=(6, 6), dtype=int, order='F')
    # make the beacon
    canvas[1][1] = 1
    canvas[1][2] = 1
    canvas[2][1] = 1
    canvas[4][4] = 1
    canvas[3][4] = 1
    canvas[4][3] = 1
    return canvas


def glider():
    """Create the canvas with the initial values of the glider"""
    canvas = np.zeros(shape=(6, 6), dtype=int, order='F')
    # make the glider
    canvas[2][3] = 1
    canvas[3][3] = 1
    canvas[4][3] = 1
    canvas[4][2] = 1
    canvas[3][4] = 1
    canvas[3][1] = 1
    return canvas


def eater_glider():
    """Create the canvas with the initial values of eater and glider"""
    canvas = np.zeros(shape=(10, 10), dtype=int, order='F')
    # make the glider
    canvas[1][6] = 1
    canvas[2][5] = 1
    canvas[3][5] = 1
    canvas[3][6] = 1
    canvas[3][7] = 1
    # now the eater...
    canvas[5][3] = 1
    canvas[5][4] = 1
    canvas[6][4] = 1
    canvas[7][1] = 1
    canvas[7][2] = 1
    canvas[7][3] = 1
    canvas[8][1] = 1
    return canvas


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
