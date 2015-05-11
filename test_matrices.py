import calculate_matrices as calc
from update import *
import numpy as np
import matplotlib.pyplot as plt

#C4 string parameters
f1 = 262.1895
L = 0.62
Ms = 3.93*10**(-3)
Te = 670
b1 = 1.1
b2 = 2.7*10**(-4)
eps = 3.82*10**(-5)
Mh = 2.97*10**(-3)
p = 2.5
bh = 1.*10**(-4)
K = 4.5*10**9
a = 0.12
zetal = 1.*10**20
zetab = 1000.
fs = 4*44.1
M = 140

rho = Ms/L
c = np.sqrt(Te/rho)
kappa = eps*(c**2)*(L**2)

n = 1000
dx = L/n
dt = 1/fs
labda = c*dt/dx
n0 = a*n

A, B, C = calc.calculate_ABC(labda, kappa, c, rho, zetab, zetal, b1, b2, dt, dx, n)

u = np.zeros(n)
uprev = np.zeros(n)
u_x0 = u[n0-1]
v_init = 5.
eta = np.array([-v_init*dt, 0])
F = K*np.abs(eta[-1] - u_x0)**p * np.zeros(n)

u, uprev = update_displacement(u,uprev,F,A,B,C)

for i in range(4):
    u_x0 = u[n0-1]
    eta = update_eta(eta, u_x0, bh, Mh, K, p, dt)
    F = K*np.abs(eta[-1] - u_x0)**p * np.ones(n)
    u, uprev = update_displacement(u,uprev,F,A,B,C)


print u
plt.figure()
plt.plot(u)
plt.show()
