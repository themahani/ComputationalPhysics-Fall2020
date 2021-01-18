#!/usr/bin/env python


""" system of players """

import numpy as np
from matplotlib import pyplot as plt


class System:
    def __init__(self):
        self.N = 100

        self.states = np.random.choice([0, 1], size=self.N)

        self.Q = np.mean(self.states)


    def change_state(self, index):
        self.states[index] = 1 - self.states[index]

    def system_play(self):
        """ players in the grid play in pairs """
        indices = np.arange(self.N)
        first = np.random.choice(indices, size=self.N // 2)
        second = []
        for i in indices:
            if i not in first:
                second.append(i)
        second = np.array(second)
        print(first)
        print(second)

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
    end = 10
    Q = np.zeros((10, end))
    system = System()
    for i in range(end):
        system.next_step()
        Q[i] = system.Q

    plt.plot(np.linspace(1, end, end), Q, 'o--')
    plt.xlabel("time")
    plt.ylabel("Q")
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    test()
