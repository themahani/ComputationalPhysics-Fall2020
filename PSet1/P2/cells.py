"""This module provides the things we need for the evolution of cells"""

import numpy as np


def state(row, i):
    """This function takes in the current row and the index of the item,
       and returns its state as and 0 =< integer =< 7 """
    length = len(row)
    return row[i - 1] * 4 + row[i] * 2 + row[(i + 1) % length]


def choice(m_state, rule):
    """Takes the rule and the state, and returns a boolean as choice"""
    return int(rule[-1 - m_state])


def evolve(rule, steps):
    """This function, creates a cell array of size 201,
       and calc.s its evolution for a specific number of steps"""
    # Initialize the array of cells
    first = [0] * 201
    first[100] = 1
    table = np.zeros(shape=(steps + 1, 201), dtype=int, order='F')
    table[0] = first.copy()

    # Find the evolution of the array for <steps> number of rounds
    for rnd in range(1, steps + 1):
        for i in range(201):
            if choice(state(table[rnd - 1], i), rule):
                table[rnd][i] = 1
            else:
                table[rnd][i] = 0
    return table
