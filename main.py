from inputparameters import R
from analyticaltemp import AnalyticalTemperature
import numpy as np

import matplotlib.pyplot as plt

n_elements = 100
n_terms = 10
r = np.linspace(1e-10, R, n_elements)

analytical_temperature = AnalyticalTemperature()

T_anal = analytical_temperature.compute(r, 0, n_terms)
plt.plot(r, T_anal)
T_anal = analytical_temperature.compute(r, 2000, n_terms)
plt.plot(r, T_anal)
plt.show()





