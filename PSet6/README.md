# Problem Set 6 -- Complex Networks and Monte Carlo

## 1 -- Erdos-Renyi Network
- Make an Erdos-Renyi network with $N = 500$ vertices and mean edge per vertex of $<k> = 0.8$.
Illustrate the network. (You can use third-party packages such as ``networkx``)

- Repeat the previous part for mean edge values of $<k>=1.0$ and $<k>=8.0$.
- Compare the distribution function of the vertex degrees and clustering for these 3 networks.
- For each network, make an approximate of the memory use of neighboring matrix, neighboring list, and edge list.

## 2 -- Monte Carlo Integration
- Integrate $\int_0^2 \exp{-x^2}$ dx using simple and smart sampling. For smart sampling use the equation $g(x) = e^{-x}$.
- Compare the integration value, statistical error, real error, and runtime for various sample numbers in a table.
- **Bonus Question**: Use a different equation instead of $g(x)$, like $g_2(x)$ and repeat the previous section. Also 
compare the resulting integrated functions using these two functions.

## 3 -- Multi-variable Integration
- The mass density of a sphere decreases linearly in the vertical axis from top to bottom in a way that
the lowest density is half of that at the densest part. Where is the Center of Mass of this sphere? (Use computers, not paper!)

## 4 -- The Metropolis Algorithm
- Make a random number generator with a Gaussian distribution using the Metropolis algorithm.
- choose the steps so that the sample acception value is [0.1, 0.2, ..., 0.9]
- Calculate the correlation length for all the sample acception values above.

