'''
Date:07_09_2022
C.U Registration No:012-1111-0753-20
C.U Roll No:203012-21-0080
Description:Specific heat using Einstein's model(test case copper)
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
#constants
h=6.62606896E-34;hbar=h/(2*np.pi);Kb=1.3806504E-23
Na=6.02214076E23#Avogadro number
Mw=63.546#molecular weight of copper(gm/mole)
rho=8960.0#density of copper in(kg/m^3)
nv=1000*Na*rho/Mw#(n/V=rhoNa/Mw)
Y=0.76E11#Youngs modulus of copper
Vs=np.sqrt(Y/rho)#velocity of sound in copper
ome=(Vs/2)*(nv)**(1./3)*2.0*np.pi#density of stats concept required
thE=(hbar*ome)/Kb
T=np.linspace(1,thE,50)
C=np.zeros(len(T));CLT=np.zeros(len(T));CHT=np.zeros(len(T))

for i in range(len(T)):
    xE=thE/T[i]
    C[i]=(3*Na*Kb)*xE**2*((np.exp(xE))/(np.exp(xE)-1)**2)
    CLT[i]=3*Na*Kb*xE**2*(np.exp(-xE))
    CHT[i]=3*Na*Kb

plt.plot(T,CLT,label='Low temperature (approx)')
plt.plot(T,CHT,label='High Temperature (approx)')
plt.plot(T,C,label='Einstein Heat Capacity At Constant Volume')
plt.xlabel(r'Temperature$\longrightarrow$',fontsize=15)
plt.ylabel(r'Heat Capacity$\longrightarrow$',fontsize=15)
plt.title("Specific heat using Einstein's model(test case copper)")
plt.legend(loc='best')
plt.grid()
plt.show()
