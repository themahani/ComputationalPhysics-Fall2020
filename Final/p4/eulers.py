#!/usr/bin/env python

""" implementations of the euler and reverse euler methods """

import numpy as np


def euler(x_init, x_dot_func, step, time):
    """ euer method """
    # finding count
    count = int(time / step) + 1

    # initialization
    x = np.zeros(count)
    x_dot = np.zeros(count)
    time = np.zeros(count)
    x[0] = x_init
    x_dot[0] = x_dot_func(x[0], time[0])


    for i in range(count - 1):
        x[i + 1] = x[i] + x_dot[i] * step
        x_dot[i + 1] = x_dot_func(x[i], time[i])
        time[i + 1] = time[i] + step

    return x, x_dot, time, count


def backward_euler(x_init, x_dot_func, step, time):
    """ euer method """
    # finding count
    count = int(time / step) + 1

    # initialization
    x = np.zeros(count)
    x_dot = np.zeros(count)
    time = np.zeros(count)
    x[0] = x_init
    x_dot[0] = x_dot_func(x[0], time[0])


    for i in range(count - 1):
        x_dot[i + 1] = x_dot_func(x[i], time[i])
        x[i + 1] = x[i] + x_dot[i + 1] * step
        time[i + 1] = time[i] + step

    return x, x_dot, time, count
