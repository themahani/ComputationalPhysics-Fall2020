"""
Modules to draw the triangles
"""
import turtle


def draw_triangle(trt, x_coord, y_coord, level):
    """
    Set the position of the turtle at Coordinates:
    x_coord (left / right), y_coord (up / down)
    """
    # Set the cursor at the top vertex
    trt.up()
    trt.setpos(x_coord, y_coord)
    trt.down()
    length = 200.0 / level

    # Now draw with fill
    trt.right(60)
    trt.begin_fill()
    for _ in range(3):
        trt.forward(length)
        trt.right(120)
    trt.end_fill()
    trt.left(60)
