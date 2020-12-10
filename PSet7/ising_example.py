#!/usr/bin/env python

""" Here I make an Ising model and run metropolis 100 times. """

from ising import Ising
from matplotlib import pyplot as plt


def before_after(size, beta, file_name):
    """ simulate for size and beta """
    ising = Ising(size, beta)
    before = ising.data.copy()
    # do metropolis 100 times
    for _ in range(100):
        ising.metropolis()

    # draw
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))
    ax1 = axes[0]
    ax2 = axes[1]
    ax1.pcolor(before)
    ax1.set_title("before")
    ax2.pcolor(ising.data)
    ax2.set_title("after")
    plt.title("beta = " + str(beta))
    plt.savefig(file_name, dpi=300, bbox_inches='tight')
    plt.close()


def main():
    """main body"""
    before_after(200, 0.3, "ba3.jpg")
    before_after(200, 0.6, "ba6.jpg")


if __name__ == "__main__":
    main()
