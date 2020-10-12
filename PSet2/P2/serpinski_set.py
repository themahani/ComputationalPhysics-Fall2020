#!/usr/bin/env python

"""
Draw the Serpinski Triangle set to the specified level
"""
from matplotlib import pyplot as plt
from serpinski_class import Serpinski


def main():
    """Main body of the program"""
    # Initialize the Serpinski set
    my_serpinski = Serpinski(400, 400, 1)
    for _ in range(2):
        my_serpinski.add_subset()
    # Draw Serpinski
    my_serpinski.draw_me()
    # Show image
    plt.show()


if __name__ == "__main__":
    main()
