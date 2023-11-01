from inputparameters import T0, R, alpha
from eigenvalues import computeEigenvalues
from sympy import *
from sympy.utilities.lambdify import implemented_function
import numpy as np

#steady state temperature
Tss = T0*(0.5 + 3/pi**2)

#computes the constants of the summation
def computeCn(eigenvalues):

    r = Symbol('r')
    #y represents the letter lambda because it doesn't exist in python and the word lambda is reserved
    y = Symbol('y')

    f_I = implemented_function('f_I', lambda y: integrate(r * sin(y*r) * (T0/2 * (1 - cos(np.pi*r/R))), (r, 0, R)))
    I = lambdify(y, f_I(y))

    f_N = implemented_function('f_N', lambda y: R/2 - sin(2*R*y) / (4*y))
    N = lambdify(y, f_N(y))

    n_eigenvalues = len(eigenvalues)
    c = np.empty(n_eigenvalues)

    for i in range(n_eigenvalues):
        c[i] = float(I(eigenvalues[i]) / N(eigenvalues[i]))
    
    return(c)

def computeAnalyticalTempDistr(r, t, n):
    y = computeEigenvalues()
    c = computeCn(y)
    #sum = np.zeros(len(r))
    sum = 0

    for i in range(n):
        sum = sum + c[i] * np.sin(y[i]*r) / r * np.exp(-alpha * y[i] * t)
    T = Tss + sum
    return T








