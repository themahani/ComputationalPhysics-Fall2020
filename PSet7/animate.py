#!/usr/bin/env python

""" Here we animate the evolution of the Ising model in different beta s """

from ising import Ising
from matplotlib import pyplot as plt
from matplotlib import animation

def animate_ising(size, beta, frames):
    """ animate the ising model for specific conditions """
    ising = Ising(size, beta)
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1, 1, 1)


    def display():
        """ display funtion for animation """
        ax.axis('off')
        ax.pcolor(ising.data)

        return fig

    def animate(t):
        """ animate function for animation """
        ax.clear()
        print(t)

        ising.metropolis()
        fig = display()
        ax.set_title('beta= '+ str(beta) + ', t = ' + str(t))

        return fig

    ani = animation.FuncAnimation(fig, animate, save_count=frames)
    ani.save('ising'+str(beta)+'.GIF', writer='imagemagick', fps=1, dpi=300)


def main():
    """ main body """
    animate_ising(200, 0.3, 30)
    animate_ising(200, 0.5, 25)
    animate_ising(200, 0.6, 20)


if __name__ == "__main__":
    main()
