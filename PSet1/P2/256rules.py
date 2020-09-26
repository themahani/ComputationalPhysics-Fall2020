#!/usr/bin/env python

"""This is the Program for generating CA models."""

from cells import evolve
from graphics import figout


def main():
    """The main body of this program"""
    # set the rules and the steps
    steps = 200
    rule1 = "01101110"
    rule2 = "01001011"

    # Print the table in a file
    figout(evolve(rule2, steps), rule2)
    figout(evolve(rule1, steps), rule1)


if __name__ == "__main__":
    main()
