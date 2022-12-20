'''
Date:31_08_2022
C.U Registration No:012-1111-0753-20
C.U Roll No:203012-21-0080
Description:Random walk in 2D
'''
from random import choice
import numpy as np
import matplotlib.pyplot as plt

"""
x,y=0,0
X,Y=[x],[y]
for i in range(5000):
    dx,dy=choice([(1,0),(-1,0),(0,1),(0,-1)])
    x,y=x+dx,y+dy
    X.append(x)
    Y.append(y)
plt.plot(X,Y)
plt.show()
"""

#generation of random walk RMS value
def walks(steps):
    x,y=0,0
    pos=[]
    for i in range(steps):
        dx,dy=choice([(1,0),(-1,0),(0,1),(0,-1)])
        x,y=x+dx,y+dy
        pos.append(np.sqrt(x**2+y**2))
    return pos

# create set of walks
steps,config=1000,1000
walks=np.array([walks(steps) for i in range(config)])

#Mean
m_walk=np.mean(walks,axis=0)

#Time Scale Mean distance in log scale
t= np.log(range(1,steps+1))
r=np.log(m_walk)

# to fit data in linear scale
import numpy.polynomial.polynomial as poly
coeffs=poly.polyfit(t,r,1)
rfit=poly.polyval(t,coeffs)
print (coeffs)

#plot
plt.plot(t,r,'o',label='Root Mean Square Position(sampled)')
plt.plot(t,rfit,'-',label='Root Mean Square Position(fitted)')
plt.legend(loc='best')
plt.xlabel(r'log(time)$\longrightarrow$',fontsize=10)
plt.ylabel(r'log($R_{rms}$)$\longrightarrow$',fontsize=10)
plt.title('Random walk in 2D',fontsize=15)
plt.show()
