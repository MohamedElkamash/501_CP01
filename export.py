from eigenvalues import computeEigenvalues
import numpy as np
import csv

def eigenvalues():
    y = computeEigenvalues()
    np.savetxt("eigenvalues.csv", y, delimiter = ',')

def cn(c_n):
    np.savetxt("cn.csv", c_n, delimiter = ',')
    