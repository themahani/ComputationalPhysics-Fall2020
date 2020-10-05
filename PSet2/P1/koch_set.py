#!/usr/bin/env python

"""
This program draws the koch fractal set to the level
specified by the user. Normally as much as it is distinguishable
in account for the screen resolution. about level 4 or 5. :)
"""

import turtle
from sys import argv



def next_level(drawer, current, level):
    """
    go to the next level of the fractal and draw it.
    """
    if current < level:
        drawer.left(60)
        drawer.forward(100 // 2 ** level)
        next_level(drawer, current + 1, level)
        drawer.right(120)
        drawer.forward(100 // 2 ** level)


def draw_koch(level):
    """
    Draw the koch fractal set to the specified level
    """
    koch = turtle.Turtle()
    koch.shape('arrow')
    koch.penup()
    # koch.setpos(100, 100)
    koch.pendown()
    koch.color('cyan')
    koch.pensize(1)
    koch.speed(1)
    koch.forward(100 // 2 ** level)
    next_level(koch, 0, level)
    koch.left(60)
    koch.forward(100 // 2 ** level)
    input(">>> Done!")


def main():
    """
    The main body of the program
    """
    depth = int(argv[1])
    turtle.Screen()
    draw_koch(depth)

if __name__ == "__main__":
    main()
