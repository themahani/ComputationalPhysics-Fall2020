#!/usr/bin/env python


""" system of players """

import numpy as np
from matplotlib import pyplot as plt


class System:
    def __init__(self, r):
        self.N = 100
        self.r = int(r)
        self.indices = np.arange(self.N)
        self.fixed_players = np.random.choice(self.indices, size=self.r)
        self.states = np.random.choice([0, 1], size=self.N)

        self.Q = np.mean(self.states)


    def change_state(self, index):
        if index in self.fixed_players:
            pass
        else:
            self.states[index] = 1 - self.states[index]

    def system_play(self):
        """ players in the grid play in pairs """
        # make the playering in two groups
        indices = self.indices
        first = np.random.choice(indices, size=self.N // 2)
        second = []
        for i in indices:
            if i not in first:
                second.append(i)
        second = np.array(second)
        print(first)
        print(second)
        # groups play in pairs
        for i in range(self.N // 2):
            if self.states[first[i]] != self.states[second[i]]:
                self.change_state(first[i])
                self.change_state(second[i])

    def next_step(self):
        """ evolve the system one time step """
        self.system_play()
        # update Q
        self.Q = np.mean(self.states)


def test():
    """ test the class """
    # ############# Part A #############
    # end = 50
    # r = 0
    # Q = np.zeros(end)
    # state = np.zeros(end)
    # system = System(r)
    # for i in range(end):
    #     system.next_step()
    #     Q[i] = system.Q
    #     state[i] = system.states[50]

    # plt.plot(np.linspace(1, end, end), Q, 'o--')
    # plt.xlabel("time")
    # plt.ylabel("Q")
    # plt.title(f"Q over time for r = {r}")
    # plt.grid()
    # plt.savefig("results/Q.jpg", dpi=200, bbox_inches='tight')
    # plt.show()

    # plt.plot(np.linspace(1, end, end), state, 'o--')
    # plt.xlabel("t")
    # plt.ylabel("state of player 50")
    # plt.title("state of player 50 over time")
    # plt.savefig("results/state50.jpg", dpi=200, bbox_inches='tight')
    # plt.show()

    ############# Part B ###############
    r_list = np.linspace(0, 10, 11)
    end = 50
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    for r in r_list:
        system = System(r)
        Q = np.zeros(end)
        for i in range(end):
            system.next_step()
            Q[i] = system.Q

        ax.plot(np.linspace(1, end, end), Q, 'o--', label=f"r = {r}")

    plt.legend()
    plt.xlabel("time")
    plt.ylabel("Q")
    plt.title("Q over time for various r")
    plt.grid()
    plt.savefig("results/Q_r.jpg", dpi=200, bbox_inches='tight')
    plt.show()



if __name__ == "__main__":
    test()
