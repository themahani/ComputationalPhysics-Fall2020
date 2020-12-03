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
        self.data = np.random.choice([-1, 1], size=(self.size, self.size))
        self.beta = beta


    def ditro(self, x):
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


# =================================================
# ==================== Main =======================
# =================================================


def main():
    """Main body"""
    n = eval(input("[Input]:main: Enter the number of rounds: "))
    beta = eval(input("[Input]:main: Enter beta: "))

    ising = Ising(100, beta)
    energies = np.zeros(n, dtype=float)

    for i in range(n):
        ising.metropolis()
        energies[i] = ising.energy()

    print("[Info]:main: Correlation Length =", corr_len(energies))
    # n = 300
    # for beta in [0.1, 0.3, 0.45, 0.5, 0.6]:
    #     ising = Ising(100, beta)
    #     energies = np.zeros(n, dtype=float)

    #     for i in range(n):
    #         ising.metropolis()
    #         energies[i] = ising.energy()

    #     plt.plot(np.linspace(1, n, n), energies, label="beta="+str(beta))

    plt.plot(np.linspace(1, n, n), energies, label="beta="+str(beta))
    plt.xlabel("unit time (one metropolis run)")
    plt.ylabel("Energy E")
    plt.tight_layout()
    plt.grid()
    plt.legend()
    plt.savefig("energy_plot.jpg", bbox_inches='tight')
    plt.show()

    plt.pcolor(ising.data)
    plt.tight_layout()
    plt.savefig("ising.jpg", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
