#!/usr/bin/env python


""" system of players """

import numpy as np
from matplotlib import pyplot as plt


class Player:
    def __init__(self):
        self.state = np.random.choice([0, 1])
        self.utility = 0


    def play(self, other_list, utility_matrix):
        """ play by the rules of the utility matrix """
        self.utility = calculate_utility(self.state, other_list, utility_matrix)
        # other_utility = calculate_utility(np.abs(self.state - 1), other_list, utility_matrix)

        # if current_utility > other_utility:
        #     self.future_state = self.state
        #     self.future_utility = current_utility
        # else:
        #     self.future_state = np.abs(self.state - 1)
        #     self.future_utility = other_utility

        # print(f"Future state will be: {self.future_state}")


def calculate_utility(state, opponent_list, utility_matrix):
    """ calculate utility based on given states """
    utility = 0
    for opponent in opponent_list:
        utility += utility_matrix[state, opponent.state]
    print(utility)
    return utility


class System:
    def __init__(self, beta, matrix, p_revolution):
        self.L = 10
        self.N = self.L ** 2

        self.grid = []
        for _ in range(self.L):
            row = []
            for _ in range(self.L):
                row.append(Player())
            self.grid.append(row)

        self.utility_matrix = matrix
        self.beta = beta
        self.p_rev = p_revolution

        self.Q = 0
        for i in range(self.L):
            for j in range(self.L):
                self.Q += self.grid[i][j].state
        self.Q /= self.N


    def system_play(self):
        """ players in the grid play with beighbors """
        for i in range(self.L):
            for j in range(self.L):
                print(f"[Info]:system_play: coords are {i}, {j}")
                self.grid[i][j].play([self.grid[i - 1][j],
                                      self.grid[(i + 1) % self.L][j],
                                      self.grid[i][ j - 1],
                                      self.grid[i][(j + 1) % self.L]],
                                      self.utility_matrix)


    def random_selection(self):
        """
        each player chooses a random player and follow strategy on conditions
        """
        for i in range(self.L):
            for j in range(self.L):
                player = self.grid[i][j]
                coords = np.array([i, j])
                # choose idol
                random = i * self.L + j
                while random == i * self.L + j:
                    random = np.random.choice(np.arange(self.N))
                idol = self.grid[random // self.L][random % self.L]

                if np.random.random() < self.p_rev:     # revolt with p_rev
                    player.state = np.abs(player.state - 1)
                else:   # if didn't revolt, check idol
                    if player.utility < idol.utility:
                        player.state = idol.state
                    elif np.random.random() < np.exp(-self.beta * (player.utility - idol.utility)):
                        player.state = idol.state


    def next_step(self):
        """ evolve the system one time step """
        self.system_play()
        self.random_selection()
        # update Q
        self.Q = 0
        for i in range(self.L):
            for j in range(self.L):
                self.Q += self.grid[i][j].state
        self.Q /= self.N


    def visualize(self):
        """ visualize the system usign plt.pcolor """
        grid = np.zeros((self.L, self.L))

        for i in range(self.L):
            for j in range(self.L):
                grid[i, j] = self.grid[i][j].state

        plt.pcolor(grid)
        plt.show()

def simulate_system(beta, end, matrix, p_rev):
    """ show the evolution of the system for <end> timesteps """
    system = System(beta, matrix, p_rev)

    Q = np.zeros(end)
    for i in range(end):
        Q[i] = system.Q
        system.next_step()
    return Q


def test():
    """ test the class """
    end = 10
    data = np.zeros((10, end))
    betas = np.linspace(0.1, 1, 10)
    for index, beta in enumerate(betas):
        data[index] = simulate_system(beta, end)

    for i in range(10):
        plt.plot(np.linspace(1, end, end), data[i], 'o--', label=f"beta = {betas[i]}")
    plt.xlabel("time")
    plt.ylabel("Q")
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    test()
