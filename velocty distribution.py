'''
Date:09.11.2022
CU Registation No:012-1111-0753-20
CU Roll No:203012-21-0080
Description:Plotting Maxwell-Boltzmann Velocity Distribution Functions
'''
import  numpy as np
import matplotlib.pyplot as plt

m = 28*1.66E-27
k = 1.38E-23

Temp = [100,200,300,500]

def f(v,T):
    return ((m/(2*np.pi*k*T))**(3/2))*4*np.pi*(v**2)*np.exp((-m*(v**2))/(2*k*T))


v = np.linspace(0,10000,1000000)
y= np.zeros(len(v))

for j in range(len(Temp)):
    y = f(v,Temp[j])
    plt.plot(v,y,label='T=%i'%Temp[j])

plt.legend()
plt.xlim(0,1500)
plt.xlabel(r'T$\longrightarrow$')
plt.ylabel(r'f(v)$\longrightarrow$')
plt.grid()
plt.legend()
plt.title('Maxwell Boltzmann Velocity Distribution function')
plt.show()
