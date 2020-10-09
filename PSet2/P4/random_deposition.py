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
    table, max_height, mean_heights, height_vars = generate_deposition(25)
    draw_canvas(table, max_height)
    draw_variance(height_vars)
    # Report mean and unsteadiness
    print("List of mean heights is as follows: ")
    print(mean_heights[0])
    print("List of surface unsteadiness is as follows: ")
    print(height_vars[0])


if __name__ == "__main__":
    main()
