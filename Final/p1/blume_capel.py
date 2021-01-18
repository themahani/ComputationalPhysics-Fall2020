#!/usr/bin/env python


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===============================================
# ============== The Ising Class ================
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


    def reset(self, beta):
        """ reset the to random data for new temp. """
        # self.data = np.random.choice([-1, 1], size=(self.size, self.size))
        self.beta = beta
        self.decision = np.exp(- beta * np.array([-8, -4, 0, 4, 8]))


    def distro(self, x):
        """boltzman distribution of energy"""
        if x > 0:
            return np.exp(- self.beta * x)
        return np.power(10, -24)


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
            for _ in range(100):
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
    energies = np.zeros(100)
    mag = np.zeros(100)
    spin_cor = np.zeros(100)
    for i in range(100):
        for _ in range(step):
            ising.metropolis()

        energies[i] = ising.energy()
        mag[i] = ising.magnetization()
        spin_cor[i] = ising.spin_cor()

    return np.mean(energies), np.var(energies), np.mean(mag), np.var(mag), np.mean(spin_cor), np.sqrt(np.var(spin_cor))

# =================================================
# =================== Simulation ==================
# =================================================


def simulate(length, betas):
    """ simulate in various temp.s for ising model of length L """
    # Initialize the Ising System
    ising = BlumeCapel(length, 2, 4)

    n = 80
    mean_energy_beta = np.zeros(n)
    var_energy_beta = np.zeros(n)
    mean_magnet_beta = np.zeros(n)
    var_magnet_beta = np.zeros(n)
    spin_correlation = np.zeros((n, 2))

    for index in range(len(betas)):
        ising.reset(betas[index])
        print("\n[Info]:main: beta =", betas[index])
        # equalie the system
        ising.equalize()

        # Find auto correlation length
        m = 100
        en = np.zeros(m)
        for i in range(m):
            ising.metropolis()
            en[i] = ising.energy()
        cor_len = corr_len(en)
        print("[Info]:main: corr_len =", cor_len)

        # get data
        mean_energy_beta[index], var_energy_beta[index], \
            mean_magnet_beta[index], var_magnet_beta[index], \
            spin_correlation[index, 0], \
            spin_correlation[index, 1] = get_data(ising, 10)

    # calculate ksi and heat capacity
    ksi = betas * var_magnet_beta
    heat_capacity = betas ** 2 * var_energy_beta

    return mean_energy_beta, mean_magnet_beta, \
        ksi, heat_capacity, spin_correlation

# =================================================
# ==================== Main =======================
# =================================================


def main():
    """Main body"""
    length = 10
    system = BlumeCapel(length, 0.2, 0.5)
    end = 200
    energy = np.zeros(end)

    for i in range(end):
        system.metropolis()
        energy[i] = system.energy()


    plt.plot(np.linspace(1, end, end), energy)
    plt.show()



if __name__ == "__main__":
    main()
