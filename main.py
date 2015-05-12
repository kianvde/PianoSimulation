import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from update import *
from plot_and_save import *
import wave
import struct
np.set_printoptions(threshold=np.nan, precision=3)

# parameter imports
from parameters import n, n_t, n0

animate = True
plot = True
write_file = True

# calculate matrices
A, B = calculate_AB()
C = calculate_C()

# initialize eta and u
eta = update_eta(init=True)
u = u_old = 1.*np.zeros(n)

ims = []
u_bridge = np.array([])
for i in range(n_t):

    u_bridge = np.append(u_bridge, u[-1])

    # collect u for animation
    if i%10==0 and animate:
        ims.append([u])

    if eta[1] > eta[0]:
        force = calculate_force(eta[1], u[n0])
        u, u_old = update_displacement(u, u_old, A, B, C, force)
        eta = update_eta(eta, force[n0])
    else:
        u, u_old = update_displacement(u, u_old, A, B)

# animate, plot and save
if animate: animate_string(ims)
if plot:
    plot_u_bridge(u_bridge)
    plot_frequency(u_bridge)
if write_file: save_to_wav(u_bridge, "test.wav")