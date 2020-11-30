#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 12:36:26 2020

@author: win_10
"""
import numpy as np
import random
import matplotlib.pyplot as plt
from numpy.random import choice


class rand_walk_1:
    def __init__(self, V_p, L):
        self.speed = V_p
        self.end = L
        self.pos = 0
        self.lifetime = 0

    def next(self):
        """one time step advancement"""
        # random walk
        self.pos += self.speed * choice([-1, 1])
        # one step still alive
        self.lifetime += 1
        # can't go lower that 0
        if self.pos < 0:
            self.pos = 0
        if self.pos >= self.end:
            # success
            return 1
        return 0


def init (grid,N):
    L = 10
    counter=0
    while counter<N:
        row=random.randint(0,L-1)
        col=random.randint(0,L-1)
        if grid[row,col]==0:
            grid[row,col]=-1
            counter+=1
        else:
            continue
    return grid


def car_mov(grid, v, N):
    L = 10
    for row in range(L):
        for col in range(L):
            if grid[row, col] == -1:
                if row - v > -1:
                    grid[row, col] = 0
                    grid[row - v, col] = -1
                else:
                    row_prime, col_prime = new_car(grid, N, L)
                    grid[row, col] = 0
                    grid[row_prime, col_prime] = -1
    return grid


def new_car(grid, N, L):
    while True:
        row_prime = random.randint(0, L-1)
        col_prime = random.randint(0, L-1)
        if grid[row_prime, col_prime] == 0:
            break
        else:
            continue
    return row_prime, col_prime



def death_check(drunk, grid, v):
    """check to see if drunk dies"""
    L = 10
    for i in range(L):
        if grid[i, int(drunk.pos)] == -1:
            if i + v < L:
                if i + v > L//2 > i:
                    return 1  #means dead
            else:
                if ((L//2) < ((i + v) % L) or (L // 2) > i):
                    return 1

    return 0 #means alive


def main():
    """define variables and simulate"""
    L = 10
    v = 40 #velocity of cars
    V_p = 2  #velocity of drunk man
    N_array = np.arange(1, 40, 1)  #N is number of cars in street
    sample_number = 10000

    cross_prob_array = np.zeros(len(N_array))  #says that considering an 'N', with what probability the drunk passes the street
    mean_life = np.zeros(len(N_array))
    n = 0
    while n < len(N_array):
        N = N_array[n]                  # How many cars in the street
        drunk = rand_walk_1(V_p, L)      # initialize drunk
        grid = np.zeros((L, L))
        grid = init(grid, N)             # Make the street
        # to calculate the mean life span of drunk
        sum_life = 0
        death_count = 0
        for i in range(sample_number):
            while True:
                # Evolve one time step
                temp = drunk.next()  #if temp==1,drunk has crossed the street
                grid = car_mov(grid, v, N)
                if temp == 1:
                    # reset drunk
                    drunk.pos = 0
                    drunk.lifetime = 0
                    # update cross probability
                    cross_prob_array[n] += 1
                    break
                if death_check(drunk, grid, v) == 1:
                    # update sum life and death count
                    death_count += 1
                    sum_life += drunk.lifetime
                    # reset drunk
                    drunk.pos = 0
                    drunk.lifetime = 0
                    break

        mean_life[n] = sum_life / death_count

        cross_prob_array[n] = cross_prob_array[n] / sample_number
        n += 1


    # Graphics
    plt.plot(N_array, cross_prob_array)
    plt.xlabel("Number of cars in the street")
    plt.ylabel("success rate")
    plt.savefig("success.jpg", bbox_inches='tight')
    plt.show()
    plt.plot(N_array, mean_life)
    plt.xlabel("Number of cars in the street")
    plt.ylabel("mean life time in unsuccessful attemps")
    plt.savefig("meanlife.jpg", bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
