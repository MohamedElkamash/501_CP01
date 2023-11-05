import plot
import export
import finitedifference as fd
from analyticaltemp import AnalyticalTemperature
from inputparameters import T0, R
from data import *

import numpy as np
import matplotlib.pyplot as plt

#function to calculate relative change
def relChange(x,y):
    return np.max(np.abs((x-y)/x))

""" #create analytical temperature object
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
rel_change = np.zeros([n_timestamps, n_terms-1])
T_temp = 0
for i in range(n_timestamps):
    for j in range(1, n_terms+1):
        T_anal = analytical_temperature.compute(r_analytical, timestamps[i], j)
        T_analytical[:,i] = T_anal
        axs_analytical_list[i].plot(r_analytical*m_to_cm, T_analytical[:,i])
        if j != 1:
            rel_change[i,j-2] = relChange(T_temp, T_analytical[:,i])
            if i==0 and j == 3:
                print(T_temp)
                print("hey")
                print(T_analytical[:,i])
        T_temp = T_anal

export.relChange(rel_change) 
plt.legend(legend_T_analytical_individual, loc = "center", bbox_to_anchor = (1.6, 0.5), fontsize = 15)
plt.savefig("Cn.png", bbox_inches='tight', dpi = 400)
plt.close()

#plotting analytical temperature
plot.analytical(T_analytical)  """ 


#Grid Refinment
fig_grid_ref, axs_grid_ref, axs_grid_ref_list = plot.seven_subplots()
legend_grid = []
n_elements = 2
delta_r = 0
n_grid_trials = 5
delta_t = 0.1
t = np.linspace(0, t_max, int(t_max/delta_t) + 1)
T_converged = 0

for i in range(n_grid_trials):
    r = np.linspace(0, R, n_elements+1)
    delta_r = R/n_elements
    T_numerical = np.empty([len(r), len(t)])
    T_numerical = fd.computeT(r, t, delta_r, delta_t)
    
    #plot
    for j in range(len(timestamps)):
        axs_grid_ref_list[j].plot(r*m_to_cm, T_numerical[:,int(timestamps[j]/delta_t)])
    exp = i+1
    legend_grid.append("$\Delta$" + "r =" + "$3\\times2^{-}$" rf"$^{exp}$" + " (cm)")
    n_elements *= 2
    
plt.legend(legend_grid, loc = "center", bbox_to_anchor = (1.6, 0.5), fontsize = 15)
plt.savefig("grid_ref.png", bbox_inches='tight', dpi = 400)
plt.close()


#time step study
n_elements = 32
delta_r = R/n_elements
r = np.linspace(0, R, n_elements+1)

#bad time step
plt.figure()
delta_t = 0.2
t = np.linspace(0, t_max, int(t_max/delta_t) + 1)
T_numerical = np.empty([len(r), len(t)])
T_numerical = fd.computeT(r, t, delta_r, delta_t)
plt.xlabel("r (cm)")
plt.ylabel("T(r,10) ($^oC$)")
plt.plot(r*m_to_cm, T_numerical[:, 50])
plt.savefig("bad time_step.png", bbox_inches='tight', dpi = 400)
plt.close()

#good time step
fig_time_step, axs_step, axs_time_step_list = plot.seven_subplots()
legend_time_step = []
delta_t_list = np.array([0.1, 0.05])

for i in range(len(delta_t_list)):
    delta_t = delta_t_list[i]
    t = np.linspace(0, t_max, int(t_max/delta_t) + 1)
    T_numerical = np.empty([len(r), len(t)])
    T_numerical = fd.computeT(r, t, delta_r, delta_t)

    #plot
    for j in range(len(timestamps)):
        axs_time_step_list[j].plot(r*m_to_cm, T_numerical[:,int(timestamps[j]/delta_t)])
    legend_time_step.append("$\Delta$" + "t = " + str(delta_t) + " (s)")

plt.legend(legend_time_step, loc = "center", bbox_to_anchor = (1.6, 0.5), fontsize = 15)
plt.savefig("time_step.png", bbox_inches='tight', dpi = 400)
plt.close()

