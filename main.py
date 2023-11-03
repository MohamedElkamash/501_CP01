import plot
import export
from analyticaltemp import AnalyticalTemperature

import numpy as np
from inputparameters import R, alpha, T0
import matplotlib.pyplot as plt

#import finitedifference as fd

def relChange(x,y):
    return np.max(np.abs((x-y)/x)) 

#analytical_temperature = AnalyticalTemperature()

""" #Plotting and printing eigenvalues
plot.eigenvalues()
export.eigenvalues()  

#compute and export c_n
c_n = analytical_temperature.getCn()
export.cn(c_n)  """

#define timestamps and mesh
n_terms = 5
n_timestamps = 7
n_elements_analytical = 100
t_max = 60
timestamps = np.linspace(0, t_max, n_timestamps)
r_analytical = np.linspace(0, R, n_elements_analytical+1)
T_analytical = np.empty([n_elements_analytical+1, n_timestamps])
rel_change = np.empty([n_timestamps, n_terms - 1])
T_temp = 0

fig_analytical, axs = plt.subplots(3,3, figsize = (15.0,12.0))
plt.setp(axs, xlabel="r (cm)", xticks=np.arange(0,3.1,0.5), yticks=np.arange(0,501,100), xlim=(0,3), ylim=(0,500))
plt.setp(axs[0,0], ylabel = "T(r,0) ($^oC$)")
plt.setp(axs[0,1], ylabel = "T(r,10) ($^oC$)")
plt.setp(axs[0,2], ylabel = "T(r,20) ($^oC$)")
plt.setp(axs[1,0], ylabel = "T(r,30) ($^oC$)")
plt.setp(axs[1,1], ylabel = "T(r,40) ($^oC$)")
plt.setp(axs[1,2], ylabel = "T(r,50) ($^oC$)")
plt.setp(axs[2,1], ylabel = "T(r,60) ($^oC$)")
fig_analytical.delaxes(axs[2,0])
fig_analytical.delaxes(axs[2,2])
legend_T_analytical_individual = [] 



""" for i in range(n_timestamps):
    for j in range(1, n_terms+1):
        T_anal = analytical_temperature.compute(r_analytical, timestamps[i], j)
        if j != 1:
            rel_change[i,j-2] = relChange(T_temp, T_anal)
        T_temp = T_anal
    T_analytical[:,i] = T_anal  """

plt.savefig("fig.png", bbox_inches='tight', dpi = 400)


#export.relChange(rel_change)
        
""" for i in range(n_timestamps):
    for j in range(n_terms-1):
        print(rel_change[i,j]) """

        #plt.plot(r * m_to_cm, T_anal)
        #legend_T.append("n = " + str(j))
    
"""     plt.yticks(np.arange(0, 501, step=100))
    plt.legend(legend_T)
    plt.savefig("T(r," + str(int(t[i])) + ").png", dpi = 400)
    plt.close(i+1) """

"""     plt.figure(0)
    plt.plot(r * m_to_cm, T_anal)
    legend_T_all.append("t = " + str(int(t[i])))

plt.figure(0)
plt.legend(legend_T_all)
plt.yticks(np.arange(0, 501, step=100))
plt.savefig("T(r).png", dpi = 400) """






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











 