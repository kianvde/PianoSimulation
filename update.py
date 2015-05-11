import numpy as np
np.set_printoptions(threshold=np.nan, precision=3)


def update_eta(eta, x0, b_h, m_h, k, p, dt):
    
    f0 = k*np.abs(eta[-1] - x0)**p
    d1 = 2/(1+b_h*dt/(2*m_h))
    d2 = (b_h*dt/(2*m_h)-1)/(1+b_h*dt/(2*m_h))
    d_f = (-dt**2/m_h)/(1+b_h*dt/(2*m_h))
            
    eta = np.append(eta, d1*eta[-1]+d2*eta[-2]+d_f*f0)
    return eta
            
eta = np.array([0, 0])

for i in range(10):
    eta = update_eta(eta, .5, 8., 3., 2., 2.3, 0.01)
    
print(eta)