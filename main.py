import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from update import *
np.set_printoptions(threshold=np.nan, precision=3)

# parameter imports
from parameters import l, n, n_t, x, n0, t, dt

animate = True
plot_waveform = True
plot_frequency = True


# calculate matrices
A, B = calculate_AB()
C = calculate_C()

# initialize eta and u
eta = update_eta(first_run=True)
u = u_old = 1.*np.zeros(n)
u_bridge = np.array([])

ims = []
if animate:
    fig, ax = plt.subplots()

for i in range(n_t):

    u_bridge = np.append(u_bridge, u[-1])

    # collect u for animation
    if i%(n_t/2000)==0 and animate:
        plt.axis((0, l, -.0001, .0005))
        im, = plt.plot(x, u, 'b')
        ims.append([im])

    if eta[1] > eta[0]:
        force = calculate_force(eta[1], u[n0])
        u, u_old = update_displacement(u, u_old, A, B, C, force)
        eta = update_eta(eta, force[n0])
    else:
        u, u_old = update_displacement(u, u_old, A, B)

if animate:
    animation = ArtistAnimation(fig, ims, interval=100, repeat_delay=500, blit=True)
    plt.show()

if plot_waveform:
    time_vector = np.linspace(0,t,n_t)
    plt.figure()
    plt.plot(time_vector[:1000],u_bridge[:1000])
    plt.show()

if plot_frequency:
    freq = np.linspace(0, 1/dt, n_t)
    spectrum = np.abs(np.fft.fft(u_bridge))
    plt.figure()
    plt.plot(freq[:n_t/160],spectrum[:n_t/160])
    plt.show()