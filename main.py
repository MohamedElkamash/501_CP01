import plot
import export
import finitedifference as fd
from analyticaltemp import AnalyticalTemperature
from data import *

import numpy as np
import matplotlib.pyplot as plt

#import finitedifference as fd

#function to calculate relative change
def relChange(x,y):
    return np.max(np.abs((x-y)/x))

#create analytical temperature object
analytical_temperature = AnalyticalTemperature()

#Plotting and printing eigenvalues
plot.eigenvalues()
export.eigenvalues()

#Cn figure
fig_T_analytical, axs_analytical, axs_analytical_list = plot.seven_subplots()
legend_T_analytical_individual = []
for i in range(1,n_terms+1):
    legend_T_analytical_individual.append("n = " + str(i))

#compute and export c_n
c_n = analytical_temperature.getCn()
export.cn(c_n) 

#analytical convergence 
for i in range(n_timestamps):
    for j in range(1, n_terms+1):
        T_anal = analytical_temperature.compute(r_analytical, timestamps[i], j)
        axs_analytical_list[i].plot(r_analytical*m_to_cm, T_anal)
        if j != 1:
            rel_change[i,j-2] = relChange(T_temp, T_anal)
        T_temp = T_anal
    T_analytical[:,i] = T_anal

export.relChange(rel_change) 
plt.legend(legend_T_analytical_individual, loc = "center", bbox_to_anchor = (1.6, 0.5), fontsize = 15)
plt.savefig("Cn.png", bbox_inches='tight', dpi = 400)
plt.close()

#plotting analytical temperature
plot.analytical(T_analytical) 

#T numerical figure
fig_grid_ref, axs_grid_ref, axs_grid_ref_list = plot.seven_subplots()
plt.savefig("new.png", bbox_inches='tight', dpi = 400)

""" #numerical temperature evaluation
n_elements = 2
delta_r = R/n_elements
n_grid_trials = 5
delta_t = 0.1
t = np.linspace(0, t_max, int(t_max/delta_t) + 1)
plt.figure(0)
legend_T = []

for i in range(n_grid_trials):
    delta_r = R/n_elements
    r = np.linspace(0, R, n_elements+1)
    T = fd.computeT(r, t, delta_r, delta_t)
    plt.plot(r, T[:,50])
    legend_T.append("n = " + str(n_elements))
    n_elements *= 2

plt.yticks(np.arange(0, 501, step=100))
plt.legend(legend_T)
plt.savefig("1.png")

plt.figure(1)
legend_T2 = [] """

""" delta_t = 0.028
for i in range(3):
    t = np.linspace(0, t_max, int(t_max/delta_t) + 1)
    T = fd.computeT(r, t, delta_r, delta_t)
    plt.plot(t, T[int(len(r)/2),:])
    legend_T2.append("delta_t = " + str(delta_t))
    delta_t /= 2

plt.yticks(np.arange(0, 501, step=100))
plt.legend(legend_T2)
plt.savefig("2.png") """  