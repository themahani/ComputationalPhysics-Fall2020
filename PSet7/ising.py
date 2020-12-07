#!/usr/bin/env python


import numpy as np
import matplotlib.pyplot as plt

# ===============================================
# ============== The Ising Class ================
# ===============================================

class Ising:
    """ The ising platform that ising simulation happens """
    def __init__(self, L, beta):
        self.data = np.random.choice([-1, 1], size=(L, L))
        self.beta = beta
        self.size = L
        self.decision = np.exp(- beta * np.array([-8, -4, 0, 4, 8]))


    def reset(self, beta):
        """ reset the to random data for new temp. """
        # self.data = np.random.choice([-1, 1], size=(self.size, self.size))
        self.beta = beta


    def distro(self, x):
        """boltzman distribution of energy"""
        if x > 0:
            return np.exp(- self.beta * x)
        return np.power(10, -24)


    def decide(self, vert, horz):
        """metropolis decision with periodic boundary conditions"""
        # calculate delta E
        delta_e = 2 * self.data[vert][horz] * (
            self.data[vert - 1][horz] +
            self.data[(vert + 1) % self.size][horz] +
            self.data[vert][horz - 1] +
            self.data[vert][(horz + 1) % self.size]
            )

        # find the index of delta E for self.decision
        decision_index = (delta_e + 8) // 4

        # report for debugging
        # print("[info]:decide: ", delta_e,
        #       self.decision[decision_index], "\n")
        # decide
        return np.random.uniform(0, 1) < self.decision[decision_index]


    def metropolis(self):
        """ evolve using metropolis """
        # every cell has chance to flip (ammortized)
        for _ in range(self.size ** 2):
            vert = np.random.randint(0, self.size)
            horz = np.random.randint(0, self.size)
            if self.decide(vert, horz):
                self.data[vert][horz] *= -1


    def energy(self):
        """ calculate and return the energy of the ising model """
        energy = 0
        for vert in range(self.size):
            for horz in range(self.size):
                # sum of sigma_i and sigma_j in the neighborhood
                energy += -1 * self.data[vert][horz] * (
                    self.data[vert - 1][horz] +
                    self.data[(vert + 1) % self.size][horz] +
                    self.data[vert][horz - 1] +
                    self.data[vert][(horz + 1) % self.size]
                    )

        return energy / 2.0


    def equalize(self):
        """ evolve the system to equilibrium """
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
            if auto_cor < threshold:
                relaxed = True
                print("[Info]:equalize: System Relaxed")

        return np.array(en)


    def magnetization(self):
        return np.sum(self.data) / self.size ** 2


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
# =================== energies =====================
# ==================================================

def get_energies(ising, step):
    """ take data about energies in the step length of cor_len """
    energies = np.zeros(100)
    for i in range(100):
        for _ in range(step):
            ising.metropolis()

        energies[i] = ising.energy()

    return np.mean(energies), np.var(energies)

# =================================================
# ==================== Main =======================
# =================================================


def main():
    """Main body"""
    # n = eval(input("[Input]:main: Enter the number of rounds: "))
    # beta = eval(input("[Input]:main: Enter beta: "))

    # Initialize the Ising System
    ising = Ising(50, 0.1)
    # make a linear space of beta
    betas = np.linspace(0.1, 0.7, 40)

    mean_energy_beta = np.zeros(40)
    var_energy_beta = np.zeros(40)

    for index in range(len(betas)):
        ising.reset(betas[index])

        # equalie the system
        ising.equalize()

        # Find auto correlation length
        n = 100
        en = np.zeros(n)
        for i in range(n):
            ising.metropolis()
            en[i] = ising.energy()
        cor_len = corr_len(en)

        # get data
        mean_energy_beta[index], var_energy_beta[index] = get_energies(ising,
                                                                       cor_len)

    plt.plot(betas, mean_energy_beta, ls='--', marker='o')
    plt.xlabel("beta")
    plt.ylabel("Energy E")
    plt.tight_layout()
    plt.grid()
    plt.savefig("energy_plot.jpg", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
