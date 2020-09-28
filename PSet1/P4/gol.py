#!/usr/bin/env python

""" This program models the game of life problem.  """

from classes.types import loaf, beacon, glider, eater_glider
from classes.graphics import animate


# quad.set_array(c_glider.ravel())
# return quad,


def main():
    """Main body of the program"""
    c_loaf = loaf()
    c_beacon = beacon()
    c_glider = glider()
    c_eater_glider = eater_glider()
    animate(c_beacon, "beacon")
    animate(c_loaf, "loaf")
    animate(c_glider, "glider")
    animate(c_eater_glider, "eater_glider")


if __name__ == "__main__":
    main()
