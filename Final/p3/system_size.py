#!/usr/bin/env python


import numpy as np


def main():
    """ main body """
    perc = [0.4, 0.7, 0.8, 0.9, 1.0]
    data = {}
    for i in range(len(perc)):
        data[perc[i]] = np.sqrt(125 * np.pi * (0.5 ** 2 + 0.7 ** 2) / perc[i])

    print(data)


if __name__ == "__main__":
    main()
