'''
Date:24_08_2022
C.U Registration No:012-1111-0753-20
C.U Roll No:203012-21-0080
Description:Random walk in 1D
'''
import numpy as np
import matplotlib.pyplot as plt

N,T=10000,1000#N=ensembles,T=total time steps
t=range(1,T+1)#time scale

#2D array:Time axis along row,each row is a configuration
walks=2*np.random.randint(2,size=(N,T))-1

#compute configuration average
positions=np.cumsum(walks,axis=1)
pos_sq=positions**2
mean_pos_sq=np.mean(pos_sq,axis=0)
rms=np.sqrt(mean_pos_sq)#rms distance

#value in log scale
t=np.log(t)
rms=np.log(rms)

#to fit
import numpy.polynomial.polynomial as poly
coeffs=poly.polyfit(t,rms,1)
rmsfit=poly.polyval(t,coeffs)
print(coeffs)

#plotting
plt.plot(t,rms,'o',label='Root Mean Square Position(sampled)')
plt.plot(t,rmsfit,'-',label='Root Mean Square Position(fitted)')
plt.legend(loc='best')
plt.xlabel(r'log(time)$\longrightarrow$',fontsize = 15)
plt.ylabel(r'log($R_{rms}$)$\longrightarrow$',fontsize = 15)
plt.title('Random Walk In 1D',fontsize = 20)
plt.show()
