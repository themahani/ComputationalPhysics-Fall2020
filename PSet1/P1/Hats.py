#!/usr/bin/env python

"""
    This program takes the number of steps to make a 2-D array to
    show the evolution of the hat row with time. The user enters
    the number of steps.
"""
import numpy as np
import matplotlib.pyplot as plt
from sys import argv

def put_hats(rounds):
    # Make first row to act as the Initiallizer
    first = [0] * 201
    first[100] = 1

    # Number of steps for the program to run
    steps = rounds

    canvas = np.ndarray(shape=(steps + 1, 201), dtype=int, order='F')
    canvas[0] = first[:]

    # At every round, look at the previous row and decide to be 0 or 1
    for rnd in range(1, steps + 1):
        for index in range(201):
            # If you're at the end, your right neighbor is index = 0
            # If you're at index = 0, you use index -1 for the left neighbor
            # that points to the end of the row
            if index == 200:
                if canvas[rnd - 1][index - 1] + canvas[rnd - 1][0] == 1:
                    canvas[rnd][index] = 1
                else:
                    canvas[rnd][index] = 0
            # Otherwise, it's normal procedure...
            else:
                if canvas[rnd - 1][index - 1] + canvas[rnd - 1][index + 1] == 1:
                    canvas[rnd][index] = 1
                else:
                    canvas[rnd][index] = 0
    return canvas


def figout(canvas, steps):
    """draws canvas using pcolormesh and outputs it to an image file"""
    # Output canvas as an Image
    fig = plt.figure()
    ax = plt.axes()

    ax.pcolormesh(canvas)

    # Labels and Titles
    ax.set_title('Evolution of Hats in a row')
    ax.set_xlabel("Hats")
    ax.set_ylabel("Rounds passed")
    fig.tight_layout()
    # Save the image into a file
    plt.savefig("Hats" + str(steps) + ".jpg", dpi=500, bbox_inches='tight')


def main():
    """The main body"""
    rounds = 200

    figout(put_hats(rounds), rounds)


if __name__ == "__main__":
    main()
