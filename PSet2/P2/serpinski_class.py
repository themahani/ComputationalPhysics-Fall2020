""" Contains the serpinski class"""

from math import sqrt
from graphics import draw_triangle

class Serpinski:
    """
    Class that contains the Serpinski set
    """
    def __init__(self, x, y, level, drawer):
        """Initializer"""
        self.x_pos = x
        self.y_pos = y
        self.subset = []
        self.level = level
        self.drawer = drawer

    def add_subset(self):
        """
        Create a subset of Serpinski
        """
        # BUG FOUND BELLOW!!!!!!!!!!!!!!!!!!!!!
        side_leng = 200.0 / self.level
        x_diff = side_leng / 2
        y_diff = side_leng * sqrt(3) / 2
        # BUG FOUND ABOVE!!!!!!!!!!!!!!!!!!!!!!
        if self.subset != []:
            for item in self.subset:
                item.add_subset()
        else:
            self.subset.append(Serpinski(self.x_pos + x_diff,
                                         self.y_pos - y_diff,
                                         self.level + 1, self.drawer))
            self.subset.append(Serpinski(self.x_pos - x_diff,
                                         self.y_pos - y_diff,
                                         self.level + 1, self.drawer))
            self.subset.append(Serpinski(self.x_pos,
                                         self.y_pos,
                                         self.level + 1, self.drawer))

    def draw_me(self):
        """Draw the set recursively"""
        if self.subset != []:
            for item in self.subset:
                item.draw_me()
        else:
            draw_triangle(self.drawer, self.x_pos, self.y_pos, self.level)
