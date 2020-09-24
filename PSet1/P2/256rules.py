#!/usr/bin/env python

"""This is the Program for generating CA models."""

from sys import argv
import numpy as np
import matplotlib.pyplot as plt


def state(row, i):
    """This function takes in the current row and the index of the item,
       and returns its state as and 0 =< integer =< 7 """
    if i == 200:
        return row[i - 1] * 4 + row[i] * 2 + row[0]
    else:
        return row[i - 1] * 4 + row[i] * 2 + row[i + 1]


def choice(st, rule):
    # Takes the rule and the state, and returns a boolean as choice
    return int(rule[-1 - st])


def figout(canvas):
    # make a grid plot of the table and save it a image
    fig = plt.figure()
    ax = plt.axes()

    ax.pcolormesh(canvas, linewidth=0.1, edgecolor='k')

    # Labels and Titles
    ax.set_title('Evolution of Hats in a row')
    ax.set_xlabel("Hats")
    ax.set_ylabel("Rounds passed")
    fig.tight_layout()

    plt.savefig("Hats" + str(canvas.shape[0] - 1) + ".jpg",
                dpi=500, bbox_inches='tight')


def main():
    if len(argv) != 3:
        print("Wrong input! Sorry mate! This just ain' your day!")
        return 1
    else:
        steps = int(argv[1])
        rule = argv[2]

    first = [0] * 201
    first[100] = 1
    # rule = "01101110"
    table = np.ndarray(shape=(steps + 1, 201), dtype=int, order='F')
    table[0] = first[:]

    for rnd in range(1, steps + 1):
        for i in range(200):
            if choice(state(table[rnd - 1], i), rule):
                table[rnd][i] = 1
            else:
                table[rnd][i] = 0

    figout(table)


if __name__ == "__main__":
    main()
