""" Contains the serpinski class"""

from math import sqrt
from matplotlib import pyplot as plt
from graphics import draw_triangle


class Serpinski:
    """
    Class that contains the Serpinski set
    """
    def __init__(self, x, y, level):
        """Initializer"""
        self.subset = []
        self.level = level
        # Calculate for vertex positions
        leng = 200.0 / 2 ** level
        y_diff = leng * sqrt(3) / 2
        x_diff = leng / 2
        # Add vertices: [top, left, right]
        self.x_pos = [x, x - x_diff, x + x_diff]
        self.y_pos = [y, y - y_diff, y - y_diff]

    def add_subset(self):
        """
        Create a subset of Serpinski
        """
        if self.subset != []:
            for item in self.subset:
                item.add_subset()
        else:
            # Calculate for vertex positions
            leng = 200.0 / 2 ** (self.level + 1)
            y_diff = leng * sqrt(3) / 2
            x_diff = leng / 2
            # Make one at top
            self.subset.append(Serpinski(self.x_pos[0],
                                         self.y_pos[0],
                                         self.level + 1))
            # One at bottum left
            self.subset.append(Serpinski(self.x_pos[0] - x_diff,
                                         self.y_pos[0] - y_diff,
                                         self.level + 1))
            # One at bottum right
            self.subset.append(Serpinski(self.x_pos[0] + x_diff,
                                         self.y_pos[0] - y_diff,
                                         self.level + 1))

    def draw_me(self):
        """Draw the set recursively"""
        if self.subset != []:
            for item in self.subset:
                item.draw_me()
        else:
            draw_triangle(self.x_pos, self.y_pos)
