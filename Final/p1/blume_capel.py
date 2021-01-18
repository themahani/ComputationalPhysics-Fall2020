#!/usr/bin/env python


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===============================================
# ============== The BlumeCapel Class ================
# ===============================================


class BlumeCapel:
    """ The ising platform that ising simulation happens """
    def __init__(self, L, J, D):
        self.spins = np.array([-1, 0, 1])
        self.data = np.random.choice(self.spins, size=(L, L))
        self.beta = 1
        self.size = L
        self.J = J
        self.D = D


    def reset(self, J, D):
        """ reset the to random data for new temp. """
        # self.data = np.random.choice([-1, 1], size=(self.size, self.size))
        self.J = J
        self.D = D


    def decide(self, vert, horz, option):
        """metropolis decision with periodic boundary conditions"""
        # calculate delta E
        current_state = self.data[vert][horz]
        self.data[vert][horz] = option
        energy = self.energy()
        self.data[vert][horz] = current_state
        delta_e = energy - self.energy()
        # find the index of delta E for self.decision
        if delta_e < 0:
            return 1
        elif np.random.random() < np.exp(-delta_e):
            return 1
        else:
            return 0


    def metropolis(self):
        """ evolve using metropolis """
        # every cell has chance to flip (ammortized)
        for _ in range(self.size ** 2):
            vert = np.random.randint(0, self.size)
            horz = np.random.randint(0, self.size)
            option = np.random.choice(self.spins[self.spins != self.data[vert][horz]])

            if self.decide(vert, horz, option):
                self.data[vert][horz] = option


    def energy(self):
        """ calculate and return the energy of the ising model """
        energy = 0
        for vert in range(self.size):
            for horz in range(self.size):
                # sum of sigma_i and sigma_j in the neighborhood
                energy += -self.J * self.data[vert][horz] * (
                    self.data[vert - 1][horz] +
                    self.data[(vert + 1) % self.size][horz] +
                    self.data[vert][horz - 1] +
                    self.data[vert][(horz + 1) % self.size]
                    )
                energy += self.D * self.data[vert][horz] ** 2   # the second term
        return energy / 2.0


    def equalize(self):
        """ evolve the system to equilibrium """
        # for _ in range(100):
        #     self.metropolis()
        en = []
        relaxed = False
        threshold = np.exp(-3)
        while not relaxed:
            # evolve 100 times
            for _ in range(20):
                self.metropolis()
                en.append(self.energy())

            # calculate auto_correlation for the j_th distance
            en_array = np.array(en)
            j = len(en_array) // 10
            auto_cor = (np.dot(en_array, np.roll(en_array, j)) / len(en_array)
                - np.mean(en_array) ** 2) / np.var(en_array)

            print("[Info]:equalize: auto_cor =", auto_cor)
            # if auto_cor is less than exp(-5), we have reached equilibrium
            if np.absolute(auto_cor) < threshold:
                relaxed = True
                print("[Info]:equalize: System Relaxed")

        return np.array(en)

    def magnetization(self):
        """ return absolute value of mean magnetization per spin """
        return np.sum(self.data) / self.size ** 2


    def n_hat3(self):
        """ return hat(N)_3 """
        return np.sum(1 - self.data ** 2) / self.size ** 2

    def spin_cor(self):
        """
            calculate the spatial auto-correlation of spins on
            on the grid and its error
        """
        cor_lens = np.zeros(self.size)
        for i in range(self.size):
            cor_lens[i] = corr_len(self.data[i])

        return np.mean(cor_lens)

# =================================================
# ============= Auto Correlation Length ===========
# =================================================


def corr_len(array):
    """ take 1-D array and return auto-correlation length """
    n = len(array) // 10
    auto_cor = np.zeros(n)

    for j in range(n):
        # compute auto correlation for j
        auto_cor[j] = (np.dot(array, np.roll(array, j)) / len(array)
            - np.mean(array) ** 2) / np.var(array)

    # return the first j for which the auto_cor goes under exp(-1)
    return len(auto_cor[auto_cor > np.exp(-1)]) + 1

# ==================================================
# ================= data acquisition ===============
# ==================================================


def get_data(ising, step):
    """ take data about energies in the step length of cor_len """
    mag = np.zeros(100)
    N3 = np.zeros(100)
    for i in range(100):
        for _ in range(step):
            ising.metropolis()

        mag[i] = ising.magnetization()
        N3[i] = ising.n_hat3()

    return np.mean(mag), np.var(mag), np.mean(N3)

# =================================================
# =================== Simulation ==================
# =================================================


def simulate(length, Js, Ds):
    """ simulate in various temp.s for ising model of length L """
    # Initialize the Ising System
    ising = BlumeCapel(length, 2, 4)

    n = len(Js)
    m = len(Ds)
    mean_magnet_beta = np.zeros((n, m))
    var_magnet_beta = np.zeros((n, m))
    mean_n3 = np.zeros((n, m))
    ksi = np.zeros((n, m))

    for j in range(len(Js)):
        for k in range(len(Ds)):
            ising.reset(Js[j], Ds[k])
            print(f"\n[Info]:main: J = {Js[j]}, D = {Ds[k]}")
            # equalie the system
            ising.equalize()

            # get data
            mean_magnet_beta[j, k], var_magnet_beta[j, k],\
                mean_n3[j, k] = get_data(ising, 1)


    return mean_magnet_beta, var_magnet_beta, mean_n3

# =================================================
# ==================== Main =======================
# =================================================


def main():
    """Main body"""
    length = 20
    system = BlumeCapel(length, 2, 4)
    Js = np.linspace(2, 0.2, 10)
    Ds = np.linspace(4, 0.5, 10)

    mean_mag, var_mag, mean_n3 = simulate(length, Js, Ds)

    np.save(f"data/mean_mag_{length}.npy", mean_mag)
    np.save(f"data/var_mag_{length}.npy", var_mag)
    np.save(f"data/mean_n3_{length}.npy", mean_n3)



if __name__ == "__main__":
    main()
