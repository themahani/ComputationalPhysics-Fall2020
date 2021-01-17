#!/usr/bin/env python

""" main module """

import time
import numpy as np
from matplotlib import pyplot as plt
from eulers import *


def my_method(x_init, x_dot_func, step, time):
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
        time[i + 1] = time[i] + step
        k = x_dot_func(x[i], time[i]) * step
        x_dot[i + 1] = x_dot_func(x[i] + k, time[i] + 0.5 * step)
        x[i + 1] = x[i] + (x_dot[i + 1] + x_dot[i]) * 0.5 * step
        x_dot[i + 1] = x_dot_func(x[i + 1], time[i + 1])

    return x, x_dot, time, count


def real(t):
    return 1 / 20.0 * (np.exp(-t) - np.exp(-21 * t))


def x_dot(x, t):
    """ x_dot function """
    return -21 * x + np.exp(-t)


def main():
    """ main body """
    x_init = 0
    end = 4
    steps = np.array([0.01, 0.02, 0.04, 0.06, 0.08, 0.1])
    runtime = np.zeros((2, len(steps)))

    ######## Part A #########
    x = [None] * len(steps)
    x_dots = [None] * len(steps)
    time0 = [None] * len(steps)
    count = [None] * len(steps)

    for i, step in enumerate(steps):
        start = time.time()
        x[i], x_dots[i], time0[i], count[i] = euler(x_init, x_dot, step, end)
        runtime[0, i] = time.time() - start

    for i in range(len(steps)):
        plt.plot(time0[i], x[i], '-', label=f"h = {steps[i]}")
        plt.xlabel("t")
        plt.ylabel("y")
        plt.grid()
        plt.legend()
        plt.title(f"h = {steps[i]}, euler method")
        plt.savefig(f"results/euler_{steps[i]}.jpg", dpi=200, bbox_inches='tight')
        plt.close()

    ######## Part B ###########
    x1 = [None] * len(steps)
    x_dots1 = [None] * len(steps)
    time1 = [None] * len(steps)
    count1 = [None] * len(steps)

    for i, step in enumerate(steps):
        start = time.time()
        x1[i], x_dots1[i], time1[i], count1[i] = backward_euler(x_init, x_dot, step, end)
        runtime[1, i] = time.time() - start

    for i in range(len(steps)):
        plt.plot(time1[i], x1[i], '-', label=f"h = {steps[i]}")
        plt.xlabel("t")
        plt.ylabel("y")
        plt.grid()
        plt.title(f"h = {steps[i]}, backward euler")
        plt.legend()
        plt.savefig(f"results/backward_euler_{steps[i]}.jpg", dpi=200, bbox_inches='tight')
        plt.close()

    ########### Part C #############
    print("===============Euler===========")
    for i in range(len(steps)):
        error = x[i][-1] - real(time0[i][-1])
        print(f"h = {steps[i]},\t error = {error},\t runtime = {runtime[0, i]}")

    print("============= Backward Euler==========")
    for i in range(len(steps)):
        error = x1[i][-1] - real(time1[i][-1])
        print(f"h = {steps[i]},\t error = {error},\t runtime = {runtime[1, i]}")

    ######### Part D ###########
    x = [None] * len(steps)
    x_dots = [None] * len(steps)
    time0 = [None] * len(steps)
    count = [None] * len(steps)

    for i, step in enumerate(steps):
        start = time.time()
        x[i], x_dots[i], time0[i], count[i] = my_method(x_init, x_dot, step, end)
        runtime[0, i] = time.time() - start

    for i in range(len(steps)):
        plt.plot(time0[i], x[i], '-', label=f"h = {steps[i]}")
    plt.legend()
    plt.show()

    print("===============Euler===========")
    for i in range(len(steps)):
        error = x[i][-1] - real(time0[i][-1])
        print(f"h = {steps[i]},\t error = {error},\t runtime = {runtime[0, i]}")


if __name__ == "__main__":
    main()
