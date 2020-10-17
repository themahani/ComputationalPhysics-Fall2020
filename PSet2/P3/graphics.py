"""
Modules to draw the triangles
"""
from matplotlib import pyplot as plt


def draw_triangle(x_coord, y_coord):
    """
    Set the position of the turtle at Coordinates:
    x_coord (left / right), y_coord (up / down)
    """
    plt.fill(x_coord, y_coord, 'b')

    # Now draw with fill
