import plot
import export
from analyticaltemp import AnalyticalTemperature

""" from inputparameters import R, alpha, T0

import finitedifference as fd
 """


#Plotting and printing eigenvalues
plot.eigenvalues()
export.eigenvalues()

#compute and export c_n
analytical_temperature = AnalyticalTemperature()
c_n = analytical_temperature.getCn()
export.cn(c_n)





""" y = computeEigenvalues()
print(y) """


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
plt.savefig("2.png") """











 