'''
Date:31_08_2022
C.U Registration No:012-1111-0753-20
C.U Roll No:203012-21-0080

Q.Consider a random walker performs 2D random walk from the origin
(a) Calculate mean square displacement(end to end distance) of the random walker for 50 random steps averaged of 1000 independent
random walks. (1 random walk consists of 50 random steps)
(b)Plot the mean square displacement Vs no of steps and find the slope
'''


from random import choice
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

def walks(steps):
    x,y=0,0
    pos_sq=[]
    for i in range(steps):
        dx,dy=choice([(1,0),(-1,0),(0,1),(0,-1)])
        x,y=x+dx,y+dy
        pos_sq.append((x**2+y**2))
    return pos_sq

#creating det of walks
steps,samples=50,1000
walks=np.array([walks(steps) for i in range(samples)])

#mean square displacement
m_sq_walk=np.mean(walks,axis=0)
s=range(1,steps+1)
print('Mean squared displacement after 50 steps:',m_sq_walk[-1])

#time scale mean distance in log scale 
t= np.log(s)
r=np.log(m_sq_walk)

#to fit data in linear scale
coeffs=poly.polyfit(t,r,1)
rfit=poly.polyval(t,coeffs)

#plotting
plt.title('Mean Squared displacement vs Step')
plt.plot(t,r,'o',label='mean square displacement(sampled)')
plt.plot(t,rfit,'-',label='mean square displacement(fitted)')
plt.xlabel(r'Steps$\longrightarrow$')
plt.ylabel(r'Mean Squared displacement$\longrightarrow$')
plt.legend(loc='best')
plt.grid()
plt.show()
print('slope of mean square displacement vs step curve:',coeffs[1])
