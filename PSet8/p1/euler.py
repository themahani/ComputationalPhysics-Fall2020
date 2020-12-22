#!/usr/bin/env python

""" implement the euler method for numerical integration """

import numpy as np
import matplotlib.pyplot as plt


def x_dot(x):
    return -x


def euler(x_init, func, step, time):
    """ euler method """
    # find count
    count = int(time / step)

    # initializations
    x = np.zeros(count)
    x[0] = x_init

    # evolve
    for i in range(count - 1):
        x[i + 1] = x[i] + step * func(x[i])

    return x, count


def analytical_sol(x):
    # the correct form of Q
    return 0.00001 * (1 - np.exp(-x))


def main():
    # constants
    x_init = -1 / 300.0
    step = 0.01
    end = 1 / 6.0

    # ================================
    # =========== Part A =============
    # ================================

    # integrate
    record, count = euler(x_init, x_dot, step, end)
    # return to Q since we simulated x (more details in report)
    record = 0.003 * (record + 1 / 300)
    print(record)
    # time axis
    time = np.linspace(0, end, count, endpoint=False)

    plt.plot(time, record, ls='-.', label='simulation')
    plt.plot(time, analytical_sol(time), ls='--', label='analytical sol.')
    plt.xlabel('tau')
    plt.ylabel('charge Q')
    plt.legend()
    plt.savefig("capacitor.jpg", bbox_inches='tight')
    plt.show()

    # =================================
    # =========== Part B ==============
    # =================================

    # list of steps to find delta
    steps = np.power(10, np.linspace(-5, -1, 30))
    # find the expected value of Q using the analytical solution
    x_end = analytical_sol(end)

    # stores the difference in the numeric and analytic solutions
    delta = []

    # data aquisition
    for step in steps:
        print('[Info]:main:Part B: step =', step)
        record, _ = euler(x_init, x_dot, step, 100 * end)
        # return to Q since we simulated x (more details in report)
        record[-1] = 0.003 * (record[-1] + 1 / 300)
        delta.append(np.absolute(x_end - record[-1]))
    print(delta)

    # fit line to data
    # popt, pcov = np.polyfit(steps, delta, deg=1, full=False, cov=True)

    # plot the data and the fit line
    plt.plot(np.log10(steps), np.log10(delta), 'ro-.', label='data')
    # plt.plot(steps, popt[1] + popt[0] * np.array(steps),
    #          'g-.', label='fit line')
    plt.xlabel('time step log(h)')
    plt.ylabel('error log(delta)')
    plt.legend()
    plt.savefig('error.jpg', bbox_inches='tight')
    plt.show()

    # find slope of the line
    # print("slope is:", popt[0], "(+/-)", np.sqrt(np.diag(pcov))[0])

if __name__ == "__main__":
    main()
