from eigenvalues import eigenvaluesEquation
import matplotlib.pyplot as plt
import numpy as np

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


