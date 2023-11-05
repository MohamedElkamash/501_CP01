import numpy as np
from inputparameters import R

n_terms = 5
n_timestamps = 7
n_elements_analytical = 100
t_max = 60
#timestamps = np.linspace(0, t_max, n_timestamps)
timestamps = np.array([0, 5, 10, 15, 20, 40, 60])
r_analytical = np.linspace(0, R, n_elements_analytical+1)
T_analytical = np.empty([n_elements_analytical+1, n_timestamps])
m_to_cm = 100