"""Provides to tools to print out the table to a file.
   !!! Depends on matplotlib.pyplot !!!"""

import matplotlib.pyplot as plt


def figout(canvas, rule):
    """make a grid plot of the table and save it a image"""
    fig = plt.figure()
    ax = plt.axes()
    ax.pcolormesh(canvas, linewidth=0.2, edgecolor='k')

    # Labels and Titles
    ax.set_title('Evolution of Cells in a row with rule ' + str(rule))
    ax.set_xlabel("Cells")
    ax.set_ylabel("Rounds passed")
    fig.tight_layout()

    plt.savefig("Hats" + str(rule) + ".jpg", dpi=300, bbox_inches='tight')
