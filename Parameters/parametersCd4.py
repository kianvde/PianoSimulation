import numpy as np
# in this file the parameters used in the simulation are set

# string parameters
f1 = 277.81          # fundamental string frequency
l = 0.622               # string length
d = 0.999e-3
rhoV = 7850.
A = np.pi * (d/2.)**2
m_s = A * l * rhoV          # total string mass
print m_s
b1 = 1.1                # air damping coefficient
b2 = 2.7e-4             # string internal friction coefficient
rho = m_s/l             # linear string density
t_e = rho * 4. * l**2 * f1**2
c = (t_e/rho)**.5       # wave velocity
E = 2.02e11
S = np.pi * (d/2.)**2
I = np.pi * d**4 / 64.
epsilon = (I/A) * (E*S) / (t_e*l**2)
print epsilon
kappa = epsilon*(c**2)*(l**2)   # string stiffness coefficient

# sampling parameters
t = 3.                  # simulation time
f_s = 8*44.1e3          # sampling frequency
m = 140                 # number of string segments
dx = l/m                # spatial grid distance
dt = 1/f_s              # time step
n_t = int(t/dt)         # number of time steps
labda = c*dt/dx         # cfl number
n = m+1                 # number of gridpoints

# hammer parameters
m_h = 8.64e-3           # hammer mass
p = 2.430                 # hammer felt stiffness exponent
b_h = 1.e-4             # fluid damping coefficient
k = 6.599e9               # hammer felt stiffness
a = 0.12                # relative striking position
v_h = 5.                # initial hammer velocity
x0 = a*l                # hammer impact point
n0 = int(a*n)           # hammer impact index

# boundary parameters
zeta_l = 1.e20          # left end normalized impedance
zeta_b = 1000.          # bridge normalized impedance

x = np.linspace(0, l, n)                          # spatial grid points
g = np.cos(50*np.pi*(x-x0))*(np.abs(x-x0) < .005)    # hammer impact window

print "stable?", labda < 0.8, "=> labda:", labda
print f1
print c / (2*l)
