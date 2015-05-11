import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from update import *

# parameter imports
from parameters import a, l, n

A, B = calculate_AB()
x0 = a*l
x = np.linspace(0, l, n)
u = u_old = np.cos(10*np.pi*(x-x0))*(np.abs(x-x0) < .05)

ims = []
fig, ax = plt.subplots()
for i in range(10):

    # collect u for animation
    im, = plt.plot(x, u, 'b')
    ims.append([im])

    # update u
    u, u_old = update_displacement(u, u_old, A, B)

# do animation
animation = ArtistAnimation(fig, ims, interval=100, repeat_delay=500, blit=True)
plt.show()