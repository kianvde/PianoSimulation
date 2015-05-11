import scipy.sparse as sparse
import numpy as np

def calculate_ABC(labda, kappa, c, rho, zetab, zetal, b1, b2, dt, dx, n):

    mu = (kappa/(c*dx))**2
    nu = 2*b2*dt/dx**2
    
    a1 = -mu*labda**2/(1+b1*dt)
    a2 = (nu + (1+4*mu)*labda**2)/(1+b1*dt)
    a3 = (2 - 2*nu - (2+6*mu)*labda**2)/(1+b1*dt) 
    a4 = (b1*dt + 2* nu - 1)/(1+b1*dt) 
    a5 = -nu/(1+b1*dt)
    af = (dt**2/rho)/(1+b1*dt)
    
    A = a3*sparse.eye(n,n,0) + a2*(sparse.eye(n,n,-1) + sparse.eye(n,n,1)) \
        + a1*(sparse.eye(n,n,-2) + sparse.eye(n,n,2))

    B = a4*sparse.eye(n,n,0) + a5*(sparse.eye(n,n,-1) + sparse.eye(n,n,1))

    # BC's
    A[-2,n-2] = a3-a1
    A[-2,n-1] = 2*a1+a2
    A[1,1] = a3-a1
    A[1,0] = 2*a1+a2

    br1 = 2.-(2*mu-2)*labda**2 / (1 + b1*dt + zetab*labda)
    br2 = (4*mu+2)*labda**2 / (1 + b1*dt + zetab*labda)
    br3 = -2*mu*labda**2 / (1 + b1*dt + zetab*labda)
    br4 = (-1 + b1*dt + zetab*labda)/(1 + b1*dt + zetab*labda)
    brf = (dt**2/rho)/(1 + b1*dt + zetab*labda)

    bl1 = 2.-(2*mu-2)*labda**2 / (1 + b1*dt + zetal*labda)
    bl2 = (4*mu+2)*labda**2 / (1 + b1*dt + zetal*labda)
    bl3 = -2*mu*labda**2 / (1 + b1*dt + zetal*labda)
    bl4 = (-1 + b1*dt + zetal*labda)/(1 + b1*dt + zetal*labda)
    blf = (dt**2/rho)/(1 + b1*dt + zetal*labda)

    A[-1,-1] = br1
    A[-1,-2] = br2
    A[-1,-3] = br3
    B[-1,-1] = br4
    B[-1,-2] = 0.

    A[0,0] = bl1
    A[0,1] = bl2
    A[0,2] = bl3
    B[0,0] = bl4
    B[0,1] = 0.

    Cpre = np.zeros(n)
    Cpre[0] = blf
    Cpre[-1] = brf
    C = af*sparse.diags(Cpre,0)

    return A, B, C