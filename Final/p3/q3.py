import numpy as np
import matplotlib.pyplot as plt
from .md import SingleAtomMD


def q3():
    model = SingleAtomMD(10, 250, 1, 1, 10, 1, (0.5, 0.7), 1)
    data = model.render(10000)
    data.plot_temperature()
    data.plot_mean_neighbors()
    data.animate()
