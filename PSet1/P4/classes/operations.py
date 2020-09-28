"""Define the set of operations on the cells"""

import numpy as np


def situate(table, i, j):
    """Takes the table and coordinated of the item and gives the sum of
       its neighbors."""
    length = table.shape[0]
    situation = table[i-1, j-1]
    situation += table[i-1, j]
    situation += table[i-1, (j+1) % length]
    situation += table[i, j-1]
    situation += table[i, (j+1) % length]
    situation += table[(i+1) % length, j-1]
    situation += table[(i+1) % length, j]
    situation += table[(i+1) % length, (j+1) % length]

    return situation


def choose(situation, state):
    """Uses the given rule to decide whether to be 1 or 0 in the next round"""
    if situation == 3 and state == 0:
        return 1
    elif situation in [2, 3] and state == 1:
        return 1
    elif situation not in [2, 3] and state == 1:
        return 0
    else:
        return state
