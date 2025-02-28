# Example live data 

import time
import matplotlib.pyplot as plt
import numpy as np

PLOT_TITLE = "Plot title"
AXIS_TITLE_X = "X Axis title"
AXIS_TITLE_Y = "Y Axis title"
PLOT_WIDTH = 12
PLOT_HEIGHT = 6 

# How much wavyness do you want:
SCALE = 1
LENGTH = 100
RANDOMNESS = 2

NUMBER_OF_ITERATIONS = 20

def plot_data(x, y):
    line1.set_ydata(y)
    fig.canvas.draw()
    fig.canvas.flush_events()
    return line1

with plt.xkcd(scale=SCALE, length=LENGTH, randomness=RANDOMNESS):
    plt.ion()

    fig, ax = plt.subplots(figsize=(PLOT_WIDTH, PLOT_HEIGHT))
    fig.suptitle(PLOT_TITLE)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xlabel(AXIS_TITLE_X)
    ax.set_ylabel(AXIS_TITLE_Y)
    ax.set_ylim(0, 10)
    ax.set_xlim(0, 10)

    x = np.linspace(-10, 10, 200)
    y = [n for n in x]
    line1, = ax.plot(x, y, linewidth=3)

    for i in range(NUMBER_OF_ITERATIONS):

        y = [n**2 / (i+1) for n in x]
        plot_data(x, y)

        plt.pause(0.1)
