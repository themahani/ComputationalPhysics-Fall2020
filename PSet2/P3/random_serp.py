#!/usr/bin/env python

"""
Draw the Serpinski Triangle set to the specified level
"""
from matplotlib import pyplot as plt
import numpy as np
from serpinski_class import Serpinski


def main():
    """Main body of the program"""
    # Initialize the Serpinski set
    print("==> Making serpinski set...")
    my_serpinski = Serpinski(400, 400, 0)
    num = 8
    print("==> Generating", num, "levels of subsets :)")
    for _ in range(9):
        my_serpinski.add_subset()
    # Draw Serpinski
    # print("==> Drawing the set. This might take quite some time!\
    #       Damn Inefficient!")
    # my_serpinski.draw_me()

    # Initialize Coordinates
    length = 50000      # Number of random dots
    x_coord = []
    y_coord = []
    index = 0

    # try length particles in serp set
    print("==> Randomly choosing", length, "dots...")
    while index < length:
        # Chech if dot in bound
        rand_y = np.random.uniform(low=400.0 - 200.0 * np.sqrt(3) / 2.0,
                                   high=400.0)
        # rand_x in triangle  // condition //
        diff = 400.0 - rand_y
        x_diff = diff / np.sqrt(3)
        rand_x = np.random.uniform(low=400.0 - x_diff,
                                   high=400 + x_diff)

        if my_serpinski.is_bound(rand_x, rand_y):
            x_coord.append(rand_x)
            y_coord.append(rand_y)
            index += 1

    # Draw image using scatter
    print("Scattering the dots ;)")
    plt.scatter(x_coord, y_coord, s=0.1)
    # Show image
    dpi = 600
    print("==> Saving to .jpg with dpi=", dpi)
    plt.savefig("fractalstuff.jpg", dpi=dpi, bbox_inches='tight')


if __name__ == "__main__":
    main()
