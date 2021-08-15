# Fractals, Deposition and Fractal Growth

## 1 -- The Koch Set
Write a program to generate the `n`th Koch fractal. You can use Translation Matrices.

## 2 -- The Serpinski Triangle
Generate the Serpinski Triangle. Note that first you need to learn how
to draw a triangle knowing the coordinates of its vertices.

## 3 -- The Serpinski Triangle (Randomized Algorithm)
Generate the Serpinski Triangle using the randomized algorithm.
The algorithm is to choose a coordinate for a point randomly
within the bounds of the serpinski set and apply the functions on it.
By doing so for thousands of points, the serpinski set emerges.

## 4 -- Random Ballistic Deposition
- Simulate the Random Ballistic Deposition in 1 dimension.
In order to do so, assume a line of length 200 units as the
substrate and deposit the particles randomly on it.
- Show the dynamics of the system on the screen. For a
better understanding of the time-based dynamics of the growth,
it is suggested to change the color of the deposited particles
alternatively. (each L \* 10)
- Calculate the average height and roughness in different time ranges.
- Plot the changes in roughness with respect to time.
- Calculate the constant $\beta$ for RBD and report it.
- Do you have any idea of the accuracy of what you reported?

## 5 -- Ballistic Deposition with Relaxation (BDR)
- Simulate BDR in 1 dimension like the previous problem.
- Show the dynamics of the model on the screen. Then deactivate the graphics section.
- Calculate the average height and roughness. How many particles should we deposit to witness the saturation of roughness?
- Plot the changes in roughness with respect to time.
- Calculate and report $\alpha$, $\beta$ and $z$ for BDR.
- Do you have any idea of the accuracy of your reported numbers?

## 6 -- Ballistic Deposition
- Simulate the BD in 1 dimension.
- Show the dynamics of the system on the screen.
- Calculate the average height and roughness in different time ranges.
- Plot the changes in roughness with respect to time.
- Calculate and report $\alpha$, $\beta$ and $z$ for BDR.

##  7 -- Competitive Ballistic Deposition
- Generate and illustration of this Deposition
- Is the dynamics of this system similar to the Random Ballistic Deposition?
- Plot the furthest distance between the points on the right and left side of the branch with respect to time for different time ranges.
