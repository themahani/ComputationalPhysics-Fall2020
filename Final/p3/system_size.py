#!/usr/bin/env python


def main():
    """ main body """
    perc = [0.4, 0.7, 0.8, 0.9, 1.0]
    data = {}
    for i in range(len(perc)):
        data[perc[i]] = eval(f"(50 * (0.7 ** 2 + 0.5 ** 2) / {perc[i]}) ** 0.5")

    print(data)


if __name__ == "__main__":
    main()
