import numpy as np
# in this file the parameters used in the simulation are set

# string parameters
f1 = 262.1895           # fundamental string frequency
l = 0.62                # string length
m_s = 3.934e-3          # total string mass
t_e = 670.              # string tension
b1 = 1.1                # air damping coefficient
b2 = 2.7e-4             # string internal friction coefficient
epsilon = 3.82e-5       # string stiffness parameter
rho = m_s/l             # linear string density
c = (t_e/rho)**.5       # wave velocity
kappa = epsilon*(c**2)*(l**2)   # string stiffness coefficient

# sampling parameters
t = 3.                 # simulation time
f_s = 4*44.1e3          # sampling frequency
m = 140                 # number of string segments
dx = l/m                # spatial grid distance
dt = 1/f_s              # time step
n_t = int(t/dt)         # number of time steps
labda = c*dt/dx         # cfl number
n = m+1                 # number of gridpoints

# hammer parameters
m_h = 2.97e-3           # hammer mass
p = 2.5                 # hammer felt stiffness exponent
b_h = 1.e-4             # fluid damping coefficient
k = 4.5e9               # hammer felt stiffness
a = 0.12                # relative striking position
v_h = 5.                # initial hammer velocity
x0 = a*l                # hammer impact point
n0 = int(a*n)           # hammer impact index

# boundary parameters
zeta_l = 1.e20          # left end normalized impedance
zeta_b = 1000.          # bridge normalized impedance

x = np.linspace(0, l, n)                          # spatial grid points
g = np.cos(50*np.pi*(x-x0))*(np.abs(x-x0) < .01)    # hammer impact window

print "stable?", labda < 0.8, "=> labda:", labda
print x[1] - x[0]
print dx