import calculate_matrices as calc
from update import *
import numpy as np
import matplotlib.pyplot as plt

#C4 string parameters
f1 = 262.1895
L = 0.62
Ms = 3.93*10**(-3)
Te = 670
b1 = 0. #1.1
b2 = 0. #2.7*10**(-4)
eps = 0. #3.82*10**(-5)
Mh = 2.97*10**(-3)
p = 2.5
bh = 1.*10**(-4)
K = 4.5*10**9
a = 0.5
zetal = 1.*10**20
zetab = 1000.
fs = 4*44.1*1000.
M = 140

rho = Ms/L
c = np.sqrt(Te/rho)
kappa = eps*(c**2)*(L**2)

n = 100
dx = L/n
dt = 1/fs
print(dx/c)
print(dt)
labda = c*dt/dx
n0 = a*n

A, B = calc.calculate_ABC(labda, kappa, c, rho, zetab, zetal, b1, b2, dt, dx, n)

x0 = a*L
x = np.linspace(0,L,n)
u_old = np.cos(10*np.pi*(x-x0))*(np.abs(x-x0) < .05)
x0 = a*L
u = np.cos(10*np.pi*(x-x0))*(np.abs(x-x0) < .05)

for i in range(10):
    plt.figure()
    plt.plot(u)
    plt.show()
    u, u_old = update_displacement(u, u_old, 0, A, B, 0)

