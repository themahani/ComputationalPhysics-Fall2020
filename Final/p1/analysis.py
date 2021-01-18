#!/usr/bin/env python


import numpy as np
import matplotlib.pyplot as plt


def main():
    """ main body """
    length = 10
    mean_mag = np.load(f"data/mean_mag_{length}.npy")
    var_mag = np.load(f"data/var_mag_{length}.npy")
    mean_n3 = np.load(f"data/mean_n3_{length}.npy")
    Js = np.linspace(2, 0.2, 10)
    Ds = np.linspace(4, 0.5, 10)

    # plot magnetization
    for j in range(mean_mag.shape[0]):
        plt.plot(Ds, mean_mag[j], 'o--', label=f"J = {Js[j]}")

    plt.xlabel("D")
    plt.ylabel(r"$<M>$")
    plt.title("mean magnetization vs. D for various J")
    plt.legend()
    plt.grid()
    plt.savefig(f"results/magnetization_{length}.jpg", dpi=200, bbox_inches='tight')
    plt.show()

    # plot n_3
    for j in range(mean_mag.shape[0]):
        plt.plot(Ds, mean_n3[j], 'o--', label=f"J = {Js[j]}")

    plt.xlabel("D")
    plt.ylabel(r"$<\hat{N}_3>$")
    plt.title(r"mean $\hat{N}_3$ vs. D for various J")
    plt.legend()
    plt.grid()
    plt.savefig(f"results/mean_n3_{length}.jpg", dpi=200, bbox_inches='tight')
    plt.show()

    # plot chi
    for j in range(mean_mag.shape[0]):
        plt.plot(Ds, var_mag[j], 'o--', label=f"J = {Js[j]}")

    plt.xlabel("D")
    plt.ylabel(r"$\chi$")
    plt.title(r"$\chi$ vs. D for various J")
    plt.legend()
    plt.grid()
    plt.savefig(f"results/chi_{length}.jpg", dpi=200, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
