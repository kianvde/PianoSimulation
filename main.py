import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from update import *
import wave
import struct
np.set_printoptions(threshold=np.nan, precision=3)

# parameter imports
from parameters import l, n, n_t, x, n0, t, dt, f_s

animate = False
plot_waveform = False
plot_frequency = False
write_file = True

# calculate matrices
A, B = calculate_AB()
C = calculate_C()

# initialize eta and u
eta = update_eta(first_run=True)
u = u_old = 1.*np.zeros(n)
u_bridge = np.array([])

ims = []
for i in range(n_t):

    u_bridge = np.append(u_bridge, u[-1])

    # collect u for animation
    if i<1e4 and i%5==0 and animate:
        ims.append([u])

    if eta[1] > eta[0]:
        force = calculate_force(eta[1], u[n0])
        u, u_old = update_displacement(u, u_old, A, B, C, force)
        eta = update_eta(eta, force[n0])
    else:
        u, u_old = update_displacement(u, u_old, A, B)

if animate:

    fig = plt.figure()
    ax = plt.axes(xlim=(0, l), ylim=(-.0001, .0005))
    lines = [plt.plot([], [])[0], plt.plot([], [], 'r', lw=5)[0], plt.plot([], [], 'r')[0]]
    lines[1].linewidth = 5
    lines[1].color = 'r'
    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    def animate(i):
        lines[0].set_data(x, ims[i])
        lines[1].set_data([.25*l, l*(.25 + float(i)/(2*len(ims)))], [0.0004, 0.0004])
        lines[2].set_data([.25*l, .75*l], [0.0004, 0.0004])
        return lines

    an = FuncAnimation(fig, animate, init_func=init, frames=len(ims), interval=20, blit=True)
    plt.show()

if plot_waveform:
    time_vector = np.linspace(0,t,n_t)
    plt.figure()
    plt.plot(time_vector[-10000:],u_bridge[-10000:])
    plt.show()

if plot_frequency:
    freq = np.linspace(0, 1/dt, n_t)
    spectrum = np.abs(np.fft.fft(u_bridge))
    plt.figure()
    plt.plot(freq[:n_t/160],spectrum[:n_t/160])
    plt.show()

if write_file:
    w = wave.open("test.wav",'w')
    w.setparams((1, 2, 2*f_s, n_t, 'NONE', 'not compressed'))
    max_amplitude = 32767.0
    print max(abs(u_bridge))
    u_norm = u_bridge/(max(abs(u_bridge))) * max_amplitude
    samples = u_norm.astype(int)
    u_wav = samples.tostring()
    # print u_wav
    # u_wav = struct.pack('h', samples.tolist())
    w.writeframes(u_wav)
    w.close()