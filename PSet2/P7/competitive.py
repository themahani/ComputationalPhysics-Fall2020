#!/usr/bin/env python

"""
This is for Problem 7
"""

import numpy as np
import matplotlib.pyplot as plt
from modules.graphics import draw_canvas, plot_dist
from modules.generate import generate_deposition


def main():
    """
    Main body of our program
    """
    print("==> Generating Deposition...\n")
    table, max_height, dist_data, x_coord = generate_deposition(200, 4)
    print("==> Drawing canvas and saving to .jpg\n")
    draw_canvas(table, max_height)

    plot_dist(dist_data, x_coord)


if __name__ == "__main__":
    main()
