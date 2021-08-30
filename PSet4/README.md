# Problem Set 4 -- Random Walk

## 1 -- Standard Deviation
- Prove the following equation: $\sigma^2 = <x^2> - <x>^2 = \frac{4l^2}{\tau}pqt$

## 2 -- Random Walk
- Write a program for random walk in 1 dimension and check for equation 1 and the following one
for various values of $p$. One of these values must be $p = 0.5$

$<x(t)> = <\frac{l}{\tau}(p - q)t>$

## 3 -- Random Walk with Traps
- Devise trapped boundary conditions for the previous problem and 
run the program until the wanderer is trapped. Calculate the mean value of the lifetime of the 
wanderer in this system by taking average over many runs. Assume that the system has 20 cells.
- Find the relation of the mean lifetime with the initial position.

## 4 -- Random Walk with Traps (Deterministic Algorithm)
- Use the previous problem using the headcount method. Compare the results and the runtime of the two programs.

## 5 -- 2-D Random Walk
- Write a 2-D random walk program on a square grid. Assume that the probability of stepping in each 
direction is equal.
- check the correction of the following equation: $<r^2> = 2dDt$

## 6 -- Aggregation Limited Diffusion
- Write a program to generate aggregation limited diffusion clusters in 2 dimensions with a linear seed.
- take the initial conditions of the cluster (the seed) to be a line of length 200
- release a random  walker from a height higher than that of the cluster and let 
it wander in the plane. If it collides with the cluster, let it stick to that position.
- Show the process on the screen. Use color coding to illustrate the dynamics of the system.

