from inputparameters import R, alpha, T0
from analyticaltemp import AnalyticalTemperature
import numpy as np
import matplotlib.pyplot as plt

n_elements = 20
delta_r = R/n_elements
r = np.linspace(0, R, n_elements+1)
delta_t = 0.1
t_max = 60
t = np.linspace(0, t_max, int(t_max/delta_t) + 1)

T = np.empty((len(r), len(t)))

b = alpha*delta_t/delta_r

#initial condition
T[:,0] = T0/2 * (1 - np.cos(np.pi * r / R))

for l in range(1, len(t)):
    #interior points
    for i in range(1, len(r)-1):
        T[i,l] = T[i,l-1] + b/delta_r * (T[i+1,l-1] - 2*T[i,l-1] + T[i-1,l-1]) + b/r[i] * (T[i+1,l-1] - T[i-1,l-1])
    
    #boundary points
    I = len(r) - 1
    T[0,l] = T[0,l-1] + 2*b/delta_r * (T[1,l-1] - T[0,l-1])
    T[I,l] = T[I,l-1] + 2*b/delta_r * (T[I-1,l-1] - T[I,l-1])

plt.plot(r, T[:,600])
plt.yticks(np.arange(0, 501, step=100))
plt.show() 








""" m_to_cm = 100
n_elements = 100
n_terms = 5
n_timestamps = 7
t_max = 60

r = np.linspace(0, R, n_elements)
t = np.linspace(0, t_max, n_timestamps)

analytical_temperature = AnalyticalTemperature()

#figure of seven cases
plt.figure(0)
plt.title("Analytical Temperature Distribution")
plt.xlabel("r (cm)")
plt.ylabel("T(r) (degC)")
legend_T_all = []

for i in range(n_timestamps):
    #create figure
    plt.figure(i+1)
    plt.title("Analytical Temperature Distribution at t = " + str(int(t[i])))
    plt.xlabel("r (cm)")
    plt.ylabel("T(r," + str(int(t[i])) + ") (degC)")
    legend_T = []

    #plot analytical temperature distribution for different number of terms in the summation
    for j in range(1, n_terms+1):
        T_anal = analytical_temperature.compute(r, t[i], j)
        plt.plot(r * m_to_cm, T_anal)
        legend_T.append("n = " + str(j))
    
    plt.yticks(np.arange(0, 501, step=100))
    plt.legend(legend_T)
    plt.savefig("T(r," + str(int(t[i])) + ").png", dpi = 400)
    plt.close(i+1)

    plt.figure(0)
    plt.plot(r * m_to_cm, T_anal)
    legend_T_all.append("t = " + str(int(t[i])))

plt.figure(0)
plt.legend(legend_T_all)
plt.yticks(np.arange(0, 501, step=100))
plt.savefig("T(r).png", dpi = 400)


 """