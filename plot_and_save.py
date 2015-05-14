# plotting, animation and saving routines

import struct
import wave

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# parameter imports
from Parameters.parametersB5 import l, x, t, dt, n_t, f_s

# animate the string from the saved positions
def animate_string(ims):

    y_max = y_min = 0
    for [im] in ims:
        if max(im) > y_max:
            y_max = max(im)
        if min(im) < y_min:
            y_min = min(im)

    fig = plt.figure()
    ax = plt.axes(xlim=(0, l), ylim=(2*y_min, 2*y_max))
    lines = [plt.plot([], [])[0], plt.plot([], [], 'r', lw=5)[0], plt.plot([], [], 'r')[0]]
    lines[1].linewidth = 5
    lines[1].color = 'r'
    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    def animate(i):
        lines[0].set_data(x, ims[i])
        lines[1].set_data([.25*l, l*(.25 + float(i)/(2*len(ims)))], 1.5*y_max*np.ones(2))
        lines[2].set_data([.25*l, .75*l], 1.5*y_max*np.ones(2))
        return lines

    an = FuncAnimation(fig, animate, init_func=init, frames=len(ims), interval=20, blit=True)
    plt.show()

# plot u(t) at the bridge
def plot_u_bridge(u_bridge):
    time_vector = np.linspace(0,t,n_t)
    plt.figure()
    plt.plot(time_vector[-10000:],u_bridge[-10000:])
    plt.show()

# plot the frequency components at the bridge
def plot_frequency(u_bridge):
    freq = np.linspace(0, 1/dt, n_t)
    spectrum = np.abs(np.fft.fft(u_bridge))
    plt.figure()
    plt.ylim((0, 1.5*max(spectrum[int(n_t/1000):int(n_t/2)])))
    plt.plot(freq[:n_t/160],spectrum[:n_t/160])
    plt.show()

# save u(t) at the bridge to a <filename>.wav file
def save_to_wav(u_bridge, filename):
    w = wave.open(filename,'w')
    w.setparams((1, 2, f_s, n_t, 'NONE', 'not compressed'))
    max_amplitude = 32767.0
    u_norm = u_bridge/(max(abs(u_bridge))) * max_amplitude
    samples = u_norm.astype(int)
    NumElements = len(samples)
    u_wav = struct.pack('h'*NumElements,*samples)
    # print u_wav
    # u_wav = struct.pack('h', samples.tolist())
    w.writeframes(u_wav)
    w.close()