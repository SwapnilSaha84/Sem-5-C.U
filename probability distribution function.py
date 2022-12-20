'''
Date:09.11.2022
CU Registation No:012-1111-0753-20
CU Roll No:203012-21-0080
Description:Plotting Maxwell-Boltzmann,Fermi-Dirac, Bose-Einstein Distribution Functions
'''


import  numpy as np
import matplotlib.pyplot as plt

mu = 7.1
k = 8.6E-5
Temp = [100,200,300,500]

#Maxwell Boltzmann Distribution function
def f(e,T):
    return 1/(np.exp((e-mu)/(k*T)))

E = np.linspace(1,10,5000)
y= np.zeros(len(E))

for j in range(len(Temp)):
    y = f(E,Temp[j])
    plt.subplot(1,3,1)
    plt.plot(E,y,label='T=%i'%Temp[j])

plt.legend()
plt.xlim(7.00,7.35)
plt.ylim(0,1)
plt.xlabel(r'E(in eV)$\longrightarrow$')
plt.ylabel(r'f(E)$\longrightarrow$')
plt.grid()
plt.legend()
plt.title('Maxwell Boltzmann Distribution function')

#Fermi Dirac Distribution function
def f(e,T):
    return 1/(np.exp((e-mu)/(k*T))+1)

E = np.linspace(0,10,5000)
y= np.zeros(len(E))

for j in range(len(Temp)):
    y = f(E,Temp[j])
    plt.subplot(1,3,2)
    plt.plot(E,y,label='T=%i'%Temp[j])

plt.legend()
plt.xlim(7.00,7.35)
plt.ylim(0,1)
plt.xlabel(r'E(in eV)$\longrightarrow$')
plt.ylabel(r'f(E)$\longrightarrow$')
plt.legend()
plt.grid()
plt.title('Fermi Dirac Distribution function')

#Bose Einstein Distribution function
def f(e,T):
    return 1/(np.exp((e-mu)/(k*T))-1)

E = np.linspace(0,10,5000)
y= np.zeros(len(E))

for j in range(len(Temp)):
    y = f(E,Temp[j])
    plt.subplot(1,3,3)
    plt.plot(E,y,label='T=%i'%Temp[j])

plt.legend()
plt.xlim(7.00,7.35)
plt.ylim(0,1.5)
plt.xlabel(r'E(in eV)$\longrightarrow$')
plt.ylabel(r'f(E)$\longrightarrow$')
plt.legend()
plt.grid()
plt.title('Bose Einstein Distribution function')

plt.show()
