'''
Q)Stimulate the tossing of 2 unbiased coins a million times and count the number of times we get double head and the probability
'''

import numpy as np

N=eval(input("Enter the number of set tossing have occured="))
T=100000
H=np.zeros(N)


for j in range(N):
          a=np.array(np.random.randint(0,2,T))
          b=np.array(np.random.randint(0,2,T))
          c=a+b
          h=0
          

          for i in range(T):
                    if (c[i]==2):
                              h=h+1
          H[j]=h
          

print("heads \n",H)
print('Avg heads:',np.mean(H))


