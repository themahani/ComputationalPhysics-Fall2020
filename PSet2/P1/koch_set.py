#!/usr/bin/env python

"""
This program draws the koch fractal set to the level
specified by the user. Normally as much as it is distinguishable
in account for the screen resolution. about level 4 or 5. :)
"""

import turtle
from sys import argv

class Koch:
    """
    The class to represent the koch fractal set
    """
    def __init__(self, level, max_level):
        self.subset = []
        self.level = level
        self.max_level = max_level
        self.add_subtree()

    def add_subtree(self):
        """add a subtree only if level isn't 0"""
        if self.level > 0:
            for _ in range(4):
                self.subset.append(Koch(self.level - 1, self.max_level))

    def draw(self, pen):
        """Draw the koch set recursively"""
        length = 800.0 / 3 ** self.max_level
        if self.level != 0:
            self.subset[0].draw(pen)
            pen.left(60)
            self.subset[1].draw(pen)
            pen.right(120)
            self.subset[2].draw(pen)
            pen.left(60)
            self.subset[3].draw(pen)
        else:
            pen.forward(length)


def draw_koch(level, screen):
    """
    Draw the koch fractal set to the specified level
    """
    size = screen.screensize()
    koch = turtle.Turtle()
    # koch.shape('arrow')
    koch.penup()
    koch.setpos(- size[0] + 1, - size[1] + 1)
    koch.pendown()
    koch.color('cyan')
    koch.pensize(1)
    koch.speed(10)
    my_koch = Koch(level, level)
    my_koch.draw(koch)


def main():
    """
    The main body of the program
    """
    depth = int(argv[1])
    scr = turtle.Screen()
    scr.bgcolor('black')
    draw_koch(depth, scr)
    turtle.done()


if __name__ == "__main__":
    main()
