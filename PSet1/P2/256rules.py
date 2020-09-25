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
    """Takes the rule and the state, and returns a boolean as choice"""
    return int(rule[st])

def evolve(rule, steps):
    """This function, creates a cell array of size 201,
       and calc.s its evolution for a specific number of steps"""
    # Initialize the array of cells
    first = [0] * 201
    first[100] = 1
    table = np.ndarray(shape=(steps + 1, 201), dtype=int, order='F')
    table[0] = first[:]

    # Find the evolution of the array for <steps> number of rounds
    for rnd in range(1, steps + 1):
        for i in range(200):
            if choice(state(table[rnd - 1], i), rule):
                table[rnd][i] = 1
            else:
                table[rnd][i] = 0
    return table


def figout(canvas, rule):
    """make a grid plot of the table and save it a image"""
    fig = plt.figure()
    ax = plt.axes()
    ax.pcolormesh(canvas, linewidth=0.2, edgecolor='k')

    # Labels and Titles
    ax.set_title('Evolution of Hats in a row')
    ax.set_xlabel("Hats")
    ax.set_ylabel("Rounds passed")
    fig.tight_layout()

    plt.savefig("Hats" + str(rule) + ".jpg", dpi=500, bbox_inches='tight')


def main():
    """The main body of this program"""
    # set the rules and the steps
    steps = 200
    rule1 = "01110110"
    rule2 = "01001011"

    # Print the table in a file
    figout(evolve(rule1, steps), rule1)
    figout(evolve(rule2, steps), rule2)


if __name__ == "__main__":
    main()
