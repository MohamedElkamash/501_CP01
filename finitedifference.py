from inputparameters import T0, R, alpha
import numpy as np

def computeT(r, t, delta_r, delta_t):
    
    #define constant b to make equations more concise
    b = alpha*delta_t/delta_r
    #define temperature matrix
    T = np.empty((len(r), len(t)))
    #apply initial condition
    T[:,0] = T0/2 * (1 - np.cos(np.pi * r / R))

    for l in range(1, len(t)):
        #update interior points
        for i in range(1, len(r)-1):
            T[i,l] = T[i,l-1] + b/delta_r * (T[i+1,l-1] - 2*T[i,l-1] + T[i-1,l-1]) + b/r[i] * (T[i+1,l-1] - T[i-1,l-1])
        
        #update boundary points
        I = len(r) - 1
        T[0,l] = T[0,l-1] + 2*b/delta_r * (T[1,l-1] - T[0,l-1])
        T[I,l] = T[I,l-1] + 2*b/delta_r * (T[I-1,l-1] - T[I,l-1])
    
    return T