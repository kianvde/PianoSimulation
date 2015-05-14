import numpy as np
# in this file the parameters used in the simulation are set

# string parameters
f1 = 98.22            # fundamental string frequency
l = 1.660                 # string length
rho = 7734.             # linear string density
d = 1.091e-3            # diameter
A = (np.pi*d**2)/4  # Cross section
m_s = l*A*rho         # total string mass
rho = m_s/l
t_e = rho * 4. * l**2 * f1**2
print t_e
b1 = 1.1                # air damping coefficient
b2 = 2.7e-4             # string internal friction coefficient
I = (np.pi * d**4)/(64) # Moment of inertia

E = 2.02e11
epsilon = I/A * (E * A)/(t_e*l**2)       # string stiffness parameter
print epsilon

c = (t_e/rho)**.5       # wave velocity
print c
kappa = epsilon*(c**2)*(l**2)   # string stiffness coefficient

# sampling parameters
t = 3.                  # simulation time
f_s = 4*44.1e3          # sampling frequency
m = 140                 # number of string segments
dx = l/m                # spatial grid distance
dt = 1/f_s              # time step
n_t = int(t/dt)         # number of time steps
labda = c*dt/dx         # cfl number
n = m+1

# hammer parameters
m_h = 9.83e-3           # hammer mass
p = 2.285                 # hammer felt stiffness exponent
b_h = 1.e-4             # fluid damping coefficient
k = 6.466e8               # hammer felt stiffness
a = 0.12                # relative striking position
v_h = 5.                # initial hammer velocity
x0 = a*l                # hammer impact point
n0 = int(a*n)           # hammer impact index

# boundary parameters
zeta_l = 1.e20          # left end normalized impedance
zeta_b = 1000.          # bridge normalized impedance

x = np.linspace(0, l, n)                            # spatial grid points
g = np.cos(25*np.pi*(x-x0))*(np.abs(x-x0) < .02)    # hammer impact window

print "stable?", labda < 0.8, "=> labda:", labda
print f1
print c / (2*l)