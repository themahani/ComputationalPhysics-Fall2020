#!/usr/bin/env python

""" verlat numerical integration methods """

import numpy as np


def velocity_verlat(x_init, acc, step, time):
    """ the velocity verlat method """
    # finding count
    count = int(time / step)

    # initialization
    x = np.zeros(count)
    x_dot = np.zeros(count)
    x[0] = x_init
    x_dot[0] = 0

    for i in range(count - 1):
        x[i + 1] = x[i] + x_dot[i] * step + 0.5 * step ** 2 * acc(x[i])
        x_dot[i + 1] = x_dot[i] + 0.5 * (acc(x[i + 1]) + acc(x[i])) * step

    return x, x_dot, count


def verlat(x_init, acc, step, time):
    """ the original verlat method """
    # calc ing count
    count = int(time / step)

    # initialization
    x = np.zeros(count + 2)
    x_dot = np.zeros(count + 1)
    x[0:2] = x_init, x_init

    for i in range(1, count + 1):
        x[i + 1] = 2 * x[i] - x[i - 1] + acc(x[i]) * step ** 2
        x_dot[i] = (x[i + 1] - x[i - 1]) / (2 * step)

    # tidy up
    x = np.delete(x, [0, -1])
    x_dot = np.delete(x_dot, 0)

    return x, x_dot, count


def euler(x_init, acc, step, time):
    """ euer method """
    # finding count
    count = int(time / step)

    # initialization
    x = np.zeros(count)
    x_dot = np.zeros(count)
    x[0] = x_init

    for i in range(count - 1):
        x[i + 1] = x[i] + x_dot[i] * step
        x_dot[i + 1] = x_dot[i] + acc(x[i]) * step

    return x, x_dot, count


def euler_koomer(x_init, acc, step, time):
    """ euer method """
    # finding count
    count = int(time / step)

    # initialization
    x = np.zeros(count)
    x_dot = np.zeros(count)
    x[0] = x_init

    for i in range(count - 1):
        x_dot[i + 1] = x_dot[i] + acc(x[i]) * step
        x[i + 1] = x[i] + x_dot[i] * step

    return x, x_dot, count


def beeman(x_init, acc, step, time):
    """ beeman method """
    # find count
    count = int(time / step)
    # initialize
    x = np.zeros(count + 1)
    x_dot = np.zeros(count + 1)
    x[0:2] = x_init, x_init
    x_dot[0] = 0

    for i in range(1, count):
        x[i + 1] = x[i] + x_dot[i] * step + 1.0 / 6 \
            * (4 * acc(x[i]) - acc(x[i - 1])) * step ** 2

        x_dot[i + 1] = x_dot[i] + 1 / 6.0 \
                * ( 2 * acc(x[i + 1]) + 5 * acc(x[i]) - acc(x[i - 1])) * step

    # clean x and x_dot
    x = np.delete(x, 0)
    x_dot = np.delete(x_dot, 0)

    return x, x_dot, count
