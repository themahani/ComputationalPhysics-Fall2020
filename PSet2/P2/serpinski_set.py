#!/usr/bin/env python

"""
Draw the Serpinski Triangle set to the specified level
"""
from matplotlib import pyplot as plt
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
    print("==> Drawing the set. This might take quite some time!\
          Damn Inefficient!")
    my_serpinski.draw_me()
    # Show image
    dpi = 600
    print("==> Saving to .jpg with dpi=", dpi)
    plt.savefig("fractalstuff.jpg", dpi=dpi, bbox_inches='tight')


if __name__ == "__main__":
    main()
