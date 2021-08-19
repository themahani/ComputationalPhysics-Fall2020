# Percolation

## 1 -- Percolation
- Generate a $L \times L$ grid.
- Activate each cell of the grid with probability $p$.

## 2 -- Coloring Algorithm
- Add the coloring algorithm as a feature to the your code of problem 1.
- Illustrating the percolation grid on the screen.

## 3 -- Probability of the creation of an Infinite Cluster for a Finite Grid
- Use the program of problem 2 for length $L = 10$.
- Create a loop in the program to sweep the range $0 \le p \le 1$ with step length $\Delta = 0.05$ and 
run the program 100 times for each $p$ to find the value of $Q$ averaging over the times that percolation happens.
- Do the same thing to $L=100$ and $L=200$.
- Plot the results of $Q$ for the three networks on one figure with respect to $Q$.

## 4 -- Probability of attachment to the Infinite Cluster
- Complete the program of problem 3 such that it calculates the probability of attachment to the 
infinite cluster $Q_{\infty}$ in each run and report its average value.
- Run the program for $L = 10, 100, 200$ 
- Plot the results for all three networks in one figure with respect to $p$.

## 5 -- Correlation Length
- Complete the program for problem 4 such that it calculates the correlation length $\zeta$ in each run 
and report its mean value.
- Run this program for $L = \{10, 20, 40, 80, 160\}$.
- Draw the results of $\zeta$ for all the networks in for plot with respect to $p$.
- Near the critical point, run the program for smaller steps of $p$ to increase the accuracy of the plot about this point.
- The peak in the plot for $\zeta$ shows the critical value probability. As you can see from the results, this value is related
to the network length $p_c(L)$. Can you find the value of $p_c(\infty)$ using extrapolation?

## 6 -- Critical Exponent $\nu$
- We know that the value of $p_c$ for a square network is 0.5927. Using this information and the results of problem 5, find the value of $\nu$.

## 7 -- Fractal Dimension of Percolation Clusters
- Using the Cluster Growth Algorithm, Prepare a program for generating the percolation clusters in a 2-D square network.
- Grow clusters for the values $p = \{0.5, 0.55, 0.59\}$ and calculate the correlation length $\zeta$ and cluster surface area $s$ for them.
- Draw the results for $\zeta$ in one plot with respect to $p$.
- Draw the values of $log(s)$ with respect to $log(\zeta)$ for these clusters in one plot.
- Can you fit a line to these values?
