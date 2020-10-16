#!/usr/bin/env python

"""
Draw the Serpinski Triangle set to the specified level
"""
from matplotlib import pyplot as plt
from serpinski_class import Serpinski


def main():
    """Main body of the program"""
    # Initialize the Serpinski set
    my_serpinski = Serpinski(400, 400, 0)
    for _ in range(7):
        my_serpinski.add_subset()
    # Draw Serpinski
    my_serpinski.draw_me()
    # Show image
    plt.savefig("fractalstuff.jpg", dpi=500, bbox_inches='tight')


if __name__ == "__main__":
    main()
