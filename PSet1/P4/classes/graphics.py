"""
This Library contains functions to create
an animation for the Game of Life (GoL)
"""
import matplotlib.pyplot as plt
from .operations import situate, choose


def animate(canvas, c_type):
    """Animates the table and saves the file as a gif"""
    l = canvas.shape[0]
    new_canvas = canvas.copy()
    for _ in range(20):
        fig, ax = plt.subplots(1, figsize=(4, 4))
        ax.pcolor(canvas, linewidth=0.2, edgecolor='k')
        plt.savefig(c_type + "/im" + str(_) + ".jpg", dpi=100)
        plt.close()
        for i in range(l):
            for j in range(l):
                situation = situate(canvas, i, j)
                if choose(situation, canvas[i][j]):
                    new_canvas[i][j] = 1
                else:
                    new_canvas[i][j] = 0
        canvas = new_canvas.copy()
