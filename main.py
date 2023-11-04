import plot
import export
from analyticaltemp import AnalyticalTemperature
from data import *

import numpy as np
import matplotlib.pyplot as plt

#import finitedifference as fd

#function to calculate relative change
def relChange(x,y):
    return np.max(np.abs((x-y)/x))

#Cn figure preparation
fig_analytical, axs = plt.subplots(3,3, figsize = (15.0,12.0))
axs_list = [axs[0,0], axs[0,1], axs[0,2], axs[1,0], axs[1,1], axs[1,2], axs[2,1]]
plt.setp(axs, xlabel="r (cm)", xticks=np.arange(0,3.1,0.5), yticks=np.arange(0,501,100), xlim=(0,3), ylim=(0,500))
legend_T_analytical_individual = []
for i in range(len(timestamps)):
    plt.setp(axs_list[i], ylabel = "T(r," + str(int(timestamps[i])) + ") ($^oC$)")
for i in range(1,n_terms+1):
    legend_T_analytical_individual.append("n = " + str(i))
fig_analytical.delaxes(axs[2,0])
fig_analytical.delaxes(axs[2,2])

#create analytical temperature object
analytical_temperature = AnalyticalTemperature()

#Plotting and printing eigenvalues
plot.eigenvalues()
export.eigenvalues()  

#compute and export c_n
c_n = analytical_temperature.getCn()
export.cn(c_n) 

#convergence 
for i in range(n_timestamps):
    for j in range(1, n_terms+1):
        T_anal = analytical_temperature.compute(r_analytical, timestamps[i], j)
        axs_list[i].plot(r_analytical*m_to_cm, T_anal)
        if j != 1:
            rel_change[i,j-2] = relChange(T_temp, T_anal)
        T_temp = T_anal
    T_analytical[:,i] = T_anal

export.relChange(rel_change) 
plt.legend(legend_T_analytical_individual, loc = "center", bbox_to_anchor = (1.6, 0.5), fontsize = 15)
plt.savefig("Cn.png", bbox_inches='tight', dpi = 400)

#plotting analytical temperature
plot.analytical(T_analytical)




""" n_elements = 2
delta_r = R/n_elements
n_grid_trials = 6
delta_t = 0.1
t_max = 60
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
legend_T2 = []

delta_t = 0.028
for i in range(3):
    t = np.linspace(0, t_max, int(t_max/delta_t) + 1)
    T = fd.computeT(r, t, delta_r, delta_t)
    plt.plot(t, T[int(len(r)/2),:])
    legend_T2.append("delta_t = " + str(delta_t))
    delta_t /= 2

plt.yticks(np.arange(0, 501, step=100))
plt.legend(legend_T2)
plt.savefig("2.png")  """











 