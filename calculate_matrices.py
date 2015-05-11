import scipy.sparse as sparse
import numpy as np

def calculate_AB(labda, kappa, c, b1, b2, dt, dx, n):

    mu = (kappa/(c*dx))**2
    nu = 2*b2*dt/dx**2
    
    a1 = -mu*labda**2/(1+b1*dt)
    a2 = (nu + (1+4*mu)*labda**2)/(1+b1*dt)
    a3 = (2 - 2*nu - (2+6*mu)*labda**2)/(1+b1*dt) 
    a4 = (b1*dt + 2* nu - 1)/(1+b1*dt) 
    a5 = -nu/(1+b1*dt) 
    
    A = a3*sparse.eye(n,n,0) + a2*(sparse.eye(n,n,-1) + sparse.eye(n,n,1)) \
        + a1*(sparse.eye(n,n,-2) + sparse.eye(n,n,2))
        
    B = a4*sparse.eye(n,n,0) + a5*(sparse.eye(n,n,-1) + sparse.eye(n,n,1))
    
    return A, B