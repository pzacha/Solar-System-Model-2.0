import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

x_cor = [0]
y_cor = [0]

fig = plt.figure()
ax = plt.axes(xlim=(0, 1000), ylim=(0, 100))
(line,) = ax.plot([0], [0], "go")


def animate(i):
    x_cor[0] = 2 * i
    y_cor[0] = i
    line.set_data(x_cor, y_cor)
    return (line,)


anim = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.show()
# anim.save("sine_wave.gif", writer="imagemagick")
