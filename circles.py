import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as colors
def squeeze(x: float) -> float:
    return 1 / (1 + np.exp(-1))

duration = 10
framerate = 60
frames = framerate * duration

fig = plt.figure()
X = list(np.random.uniform(low=0, high=1, size=3))
Y = list(np.random.uniform(low=0, high=1, size=3))
def init():
    return
def animate(i):
    x = np.random.uniform(low=0, high=1, size=1)
    y = np.random.uniform(low=0, high=1, size=1)
    for element in x:
        X.append(element)
    for element  in y:
        Y.append(element)
    plt.cla()
  
    C = [colors.to_rgb(np.random.uniform(0, 1, 3)) for element in X]

    plt.scatter(x=X, y=Y, facecolors="none", edgecolors=C, s=500 - i * (500 / frames), alpha=1 - i / frames)

animation = FuncAnimation(fig=fig, func=animate, frames=frames, init_func=init, interval=1000 / framerate)
animation.save("animations/circles.mp4")
