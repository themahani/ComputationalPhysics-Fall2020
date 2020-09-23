#!/usr/bin/env python

"""
    This program takes the number of steps to make a 2-D array to
    show the evolution of the hat row with time. The user enters
    the number of steps.
"""
import numpy as np
import matplotlib.pyplot as plt

# Make first row to act as the Initiallizer
first = [0] * 201
first[100] = 1

# Number of steps for the program to run
steps = 10

canvas = np.ndarray(shape=(steps + 1, 201), dtype=int, order='F')
canvas[0] = first[:]

for rnd in range(1, steps + 1):
    for index in range(201):
        if index == 200:
            if canvas[rnd - 1][index - 1] + canvas[rnd - 1][0] == 1:
                canvas[rnd][index] = 1
            else:
                canvas[rnd][index] = 0
        else:
            if canvas[rnd - 1][index - 1] + canvas[rnd - 1][index + 1] == 1:
                canvas[rnd][index] = 1
            else:
                canvas[rnd][index] = 0

print(canvas[10])
