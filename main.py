from inputparameters import R
from analyticaltemp import computeAnalyticalTempDistr
import numpy as np

import matplotlib.pyplot as plt

n_elements = 100
n_terms = 10
r = np.linspace(1e-10, R, n_elements)

T_anal = computeAnalyticalTempDistr(r, 10, n_terms)

plt.plot(r, T_anal)
plt.show()





