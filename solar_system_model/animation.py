import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from models import 


class Animation:
    def __init__(self):
        self.x_cor = [0]
        self.y_cor = [0]

        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0, 1000), ylim=(0, 100))
        self.line = None
        (self.line,) = self.ax.plot([0], [0], "go")

    def animate(self, i):
        self.x_cor[0] = 2 * i
        self.y_cor[0] = i
        self.line.set_data(self.x_cor, self.y_cor)
        return (self.line,)

    def run(self):
        anim = FuncAnimation(self.fig, self.animate, frames=100, interval=50, blit=True)
        plt.show()


# a = Animation()
# a.run()
# anim.save("sine_wave.gif", writer="imagemagick")
