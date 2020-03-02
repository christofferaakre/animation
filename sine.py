import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
plot = fig.add_subplot(111)
plot.set_xlim([0, 2 * np.pi])
plot.set_ylim([-1, 1])
X = np.linspace(0, 2 * np.pi, 10000)
Y = np.sin(X)

def init():
    plot.plot(X, Y)

def animate(i):
    Y = np.sin(X - 0.01 * i)
    plt.cla()
    plot.plot(X, Y)
    print(i)

animation = FuncAnimation(fig=fig, func=animate, frames=600, init_func=init, interval=16.67)
animation.save("animations/sine.mp4")