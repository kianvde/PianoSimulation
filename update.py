import numpy as np
np.set_printoptions(threshold=np.nan, precision=3)


def update_eta(eta, u_x0, b_h, m_h, k, p, dt):
    
    f0 = k*np.abs(eta[-1] - u_x0)**p
    print f0
    d1 = 2/(1+b_h*dt/(2*m_h))
    print d1
    d2 = (b_h*dt/(2*m_h)-1)/(1+b_h*dt/(2*m_h))
    print d2
    d_f = (-dt**2/m_h)/(1+b_h*dt/(2*m_h))
    print d_f
            
    eta = np.append(eta, d1*eta[-1]+d2*eta[-2]+d_f*f0)
    print eta
    return eta


def update_displacement(u, uprev,  F, A, B, C):
    unext = A*u + B*uprev #+ C*F
    return unext, u



