'''
Date:14_09_2022
C.U Registration No:012-1111-0753-20
C.U Roll No:203012-21-0080
Description:Debye model of specific heat(Test case copper)
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#constants
h=6.62606896E-34;hbar=h/(2*np.pi);Kb=1.3806504E-23
Na=6.02214076E23#Avogadro number
Mw=63.546#molecular weight of copper(gm/mole)
rho=8960.0#density of copper in(kg/m^3)
V_Transverse=2325.0#in m/sec
V_Longitudinal=4760.0#in m/sec
Vs=3**(1./3)*(2/V_Transverse**3+1/V_Longitudinal**3)**(-1./3)
nv=1000*Na*rho/Mw#N/V=rhoNa/Mw
omd=Vs*(6*np.pi**2*nv)**(1./3)#debye cutoff frequency
thD=(hbar*omd)/Kb#Debye temperature
T=np.arange(0.,thD,5)
T[0]=1
C=np.zeros(len(T))
CLT=np.zeros(len(T))
CHT=np.zeros(len(T))
for i in range(len(T)):
    xD=thD/(T[i])
    I=quad(lambda x:(x**4*np.exp(x))/((np.exp(x)-1)**2.0),0,xD)[0]
    C[i]=9*Na*Kb*((T[i]/thD)**3)*I
    CLT[i]=((12./5)*(np.pi**4)*Na*Kb*(T[i]**3))/thD**3
    CHT[i]=3*Na*Kb
plt.plot(T,CLT,label='Low temperature (approx)')
plt.plot(T,CHT,label='High Temperature (approx)')
plt.plot(T,C,label='Debye Heat Capacity At Constant Volume')
plt.xlabel(r'Temperature$\longrightarrow$',fontsize=15)
plt.ylabel(r'Heat Capacity$\longrightarrow$',fontsize=15)
plt.title("Debye Model Of Specific Heat(Test Case Copper)")
plt.legend(loc='best')
plt.ylim(0,50)
plt.grid()
plt.show()
