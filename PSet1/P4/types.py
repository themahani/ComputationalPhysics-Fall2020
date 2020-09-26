"""Define the types of Game of Life (GoL) initial conditions"""

import numpy as np


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
