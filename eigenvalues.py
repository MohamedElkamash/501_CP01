from numpy import tan
from inputparameters import R
from scipy.optimize import fsolve

#initial guess of the first 10 eigenvalues
eigenvalues_guess = [149.78, 257.51, 363.47, 468.87, 574.03, 679.04, 783.98, 888.87, 993.72, 1098.5]

def eigenvaluesEquation(lamda):
    return tan(lamda*R) - lamda*R

def computeEigenvalues():
    eigenvalues = fsolve(eigenvaluesEquation, eigenvalues_guess)
    return eigenvalues









    

