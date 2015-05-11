__author__ = 'Xicitos'

import scipy.sparse as sparse
import numpy as np
import matplotlib.pyplot as plt

def calculate_ABC(labda, n):

    a2 = labda**2
    a3 = 2 - 2*labda**2
    a4 = -1.

    A = a3*sparse.eye(n,n,0) + a2*(sparse.eye(n,n,-1) + sparse.eye(n,n,1))

    B = a4*sparse.eye(n,n,0)

    return A, B

def update_displacement(u, uprev, A, B):

    unext = A*u + B*uprev

    return unext, u

c = 100.
L = 10.
dt = 0.001

n = 100
dx = L/n
print(dx/c)
print(dt)
labda = c*dt/dx
print(labda)

A, B = calculate_ABC(labda, n)

x0 = 5.
x = np.linspace(0,L,n)
u = u_old = np.cos(1*np.pi*(x-x0))*(np.abs(x-x0) < .5)

for i in range(10):
    plt.figure()
    plt.plot(u)
    plt.show()
    u, u_old = update_displacement(u, u_old, A, B)
