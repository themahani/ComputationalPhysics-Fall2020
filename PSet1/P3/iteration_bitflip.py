#!/usr/bin/env python

"""This is the Program for generating CA models."""

from cells import evolve
from graphics import figout


def bit_flip(bit):
    """Do a bit flip"""
    if bit == '1':
        return '0'
    else:
        return '1'


def iterate(rule):
    """Iterate over the rule and do a bit flip for each element."""
    for i in range(len(rule)):
        new_rule = rule[:i] + bit_flip(rule[i]) + rule[i + 1:]
        # Default number of steps is 200
        figout(evolve(new_rule, 300), new_rule)


def main():
    """The main body of this program"""
    # set the rules and the steps
    rule100 = "01101110"

    # Print the table in a file
    iterate(rule100)


if __name__ == "__main__":
    main()
