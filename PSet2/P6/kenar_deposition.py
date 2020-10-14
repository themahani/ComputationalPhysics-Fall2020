#!/usr/bin/env python

"""
This is for Problem 4
"""

import numpy as np
import matplotlib.pyplot as plt
from modules.graphics import draw_canvas, draw_variance
from modules.generate import generate_deposition


def main():
    """
    Main body of our program
    """
    print("==> Generating Deposition...\n")
    table, max_height, x_coord, mean_heights, height_vars = generate_deposition(50)
    # print("==> Drawing canvas and saving to .jpg\n")
    # draw_canvas(table, max_height)
    print("==> Drawing plot for beta and saving to .jpg\n")
    params, errors = draw_variance(x_coord, height_vars)
    # Report mean and unsteadiness
    print("List of mean heights is as follows: ")
    print(mean_heights[0])
    print("List of surface unsteadiness is as follows: ")
    print(height_vars[0])
    print("List of x_axis is as follows:")
    print(x_coord)
    # Report beta
    print("The value for beta is: %.2f " % params[0], "(+/-) %.2f" % errors[0])


if __name__ == "__main__":
    main()
