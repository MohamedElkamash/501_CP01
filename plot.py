from eigenvalues import eigenvaluesEquation
import matplotlib.pyplot as plt
import numpy as np
from data import *

def eigenvalues():
    x = np.linspace(0, 1400, 1000)
    y = eigenvaluesEquation(x)
    fig_eigen, ax_eigen = plt.subplots()
    ax_eigen.set_xlabel("$\lambda (m^{-1})$", fontsize = 11)
    ax_eigen.set_ylabel('tan($\lambda$R)-$\lambda$R', fontsize = 11)
    ax_eigen.set_xticks(np.arange(0,1201,200))
    ax_eigen.set_yticks(np.arange(-40,41,20))
    ax_eigen.set_xlim(0,1200)
    ax_eigen.set_ylim(-40,40)
    ax_eigen.tick_params(axis = 'both', labelsize = 11)
    ax_eigen.plot(x,y)
    ax_eigen.axhline(0, color = 'r')
    plt.savefig("Eigen.png", bbox_inches='tight', dpi = 400)
    plt.close()

def analytical(T_analytical):
    fig_analytical, ax_analytical = plt.subplots()
    ax_analytical.set_xlabel("r (cm)", fontsize = 11)
    ax_analytical.set_ylabel('T(r,t) ($^oC$)', fontsize = 11)
    ax_analytical.set_xticks(np.arange(0,3.1,0.5))
    ax_analytical.set_yticks(np.arange(0,501,100))
    ax_analytical.set_xlim(0,3)
    ax_analytical.set_ylim(0,500)
    ax_analytical.tick_params(axis = 'both', labelsize = 11)
    legend_T_analytical = []
    for i in range(len(timestamps)):
        ax_analytical.plot(r_analytical*m_to_cm, T_analytical[:,i])
        legend_T_analytical.append("t = " + str(int(timestamps[i])) + "s")
    plt.legend(legend_T_analytical)
    plt.savefig("analytical.png", bbox_inches='tight', dpi = 400)
    plt.close()

def seven_subplots():
    fig_T, axs = plt.subplots(3,3, figsize = (15.0,12.0))
    axs_list = [axs[0,0], axs[0,1], axs[0,2], axs[1,0], axs[1,1], axs[1,2], axs[2,1]]
    plt.setp(axs, xlabel="r (cm)", xticks=np.arange(0,3.1,0.5), yticks=np.arange(0,501,100), xlim=(0,3), ylim=(0,500))
    legend_T_analytical_individual = []
    for i in range(len(timestamps)):
        plt.setp(axs_list[i], ylabel = "T(r," + str(int(timestamps[i])) + ") ($^oC$)")
    fig_T.delaxes(axs[2,0])
    fig_T.delaxes(axs[2,2])
    return fig_T, axs, axs_list


