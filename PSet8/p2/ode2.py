#!/usr/bin/env python

""" trying different integration methods """

import numpy as np
import matplotlib.pyplot as plt
from ODEs import *


def acc(x):
    return -x


def main():
    """ main body """
    # constants
    x_init = 1
    step = 0.01
    end = 60

    # initialize data dict.
    data = {}

    # simulate for different methods
    *data['euler'], _ = euler(x_init, acc, step, end)
    *data['euler_koomer'], _ = euler_koomer(x_init, acc, step, end)
    *data['verlat'], _ = verlat(x_init, acc, step, end)
    *data['velocity_verlat'], _ = velocity_verlat(x_init, acc, step, end)
    *data['beeman'], count = beeman(x_init, acc, step, end)

    time = np.linspace(0, 10, count)

    for method in data:
        plt.plot(time, data[method][0], ls='--', label=method)

    plt.xlabel('time')
    plt.ylabel('x')
    plt.title("solution for d^2 x / dt^2 = - x using different methods")
    plt.legend()
    plt.savefig("ode2_plots.jpg", bbox_inches='tight')
    plt.show()

    for method in data:
        plt.plot(data[method][0], data[method][1], label=method)
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('x_dot')
        plt.title(" x_dot vs. x")
        plt.savefig(method+'.jpg', bbox_inches='tight')
        plt.show()


if __name__ == "__main__":
    main()
