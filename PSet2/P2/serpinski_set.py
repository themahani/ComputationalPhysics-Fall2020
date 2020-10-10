#!/usr/bin/env python

"""
Draw the Serpinski Triangle set to the specified level
"""
import turtle
from serpinski_class import Serpinski


def main():
    """Main body of the program"""
    # Make screen adjustments
    my_board = turtle.Screen()
    my_board.bgcolor('black')
    s_screen = my_board.screensize()
    # start up the turtle pen
    my_trt = turtle.Turtle()
    my_trt.fillcolor('cyan')
    my_trt.speed(10)

    # Initialize the Serpinski set
    my_serpinski = Serpinski(0, s_screen[0], 1, my_trt)
    for _ in range(3):
        my_serpinski.add_subset()
    # Draw Serpinski
    my_serpinski.draw_me()
    # wait to give input to close
    turtle.done()


if __name__ == "__main__":
    main()
