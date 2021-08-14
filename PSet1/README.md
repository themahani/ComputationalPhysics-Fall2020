# Problem Set 1 -- Cellular Automata

## 1 -- The Hat Rule
We want to investigate the behavior in a system. Assume a row of 201 people.
The person in the middle is wearing a hat and the rest aren't (t = 0).
Each person in the next time step wears a hat, only if 1 person around them
is wearing a hat. (If both of neither of the people around them are wearing, 
then they won't wear a hat either)
Investigate how the people in this row will follow this fashion with respect to time.
In one plot, show the spread of this fashion in society. (x-axis representing the people
in the row, and the y-axis representing time.)

## 2 -- The 256 Rules
Imagine a 1-D Cellular Automata (CA) of length 201. Assume that in the beginning (t=0)
only the cell in the middle is on (active) and the rest are off (inactive).
If this system follows the 110 rule (01110110) and continues for 200 time steps, 
plot the dynamics of the system. Now do the same for a system that follows the 
75 (01001011) rule. 

### Bonus Problem: Memory Optimization
introduce a method to minimize the memory usage in problem 2

## 3 -- Wolfram Classification
As you may know, we can write the 256 rules as a 8-bit number.
Using 1 bit flip in the binary representing of the 110 rule, we
can come up with 8 images. Generate these images. 
(take the length of the system to be 201 and simulate for 300 
time steps.). Explain how these CAs are classified according
to the Wolfram Classification.

## 4 -- Game of Life
In the game of life, the cells follow to rules below:
**birth**: If an inactive (0 or off) cell has 3 active (1 or on)
neighbors, it will turn active in the next time step.

**survival**: If an active cell 2 or 3 active neighbors, it will stay
active in the next time step.

**death**: If an active cell has less than 2 or more and 3 active neighbors,
it will turn inactive in the next time step.

Also in Game of Life (GoL), some of the initial conditions result in specific behavior
of the system. Four of these are *loaf*, *beacon*, *glider*, and *eater and glider*.
Simulate the dynamics of these 4 classes for 10 time steps in separate videos.

## Useful Links
- [Wolfram Mathworld - Elementary Cellular Automaton](https://mathworld.wolfram.com/ElementaryCellularAutomaton.html)
- [LifeWiki - Beacon](https://www.conwaylife.com/wiki/Beacon): You can also search for the other GoL classes.
