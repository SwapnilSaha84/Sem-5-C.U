'''
Date:
Q)Write a python code to stimulate single unbiased coin tossing experiment to numerically verify the probability of apperance of head and tails
'''

import numpy as np


N=eval(input("Enter the number of set tossing have occured="))
T=eval(input("Enter the number of time tossing has been done="))

head=np.zeros(N)
tail=np.zeros(N)


for j in range (N):
    a=np.random.randint(0,2,T)
    head[j]=sum(a)
    tail[j]=T-sum(a)

#print("No of heads \n",head);print("No of tails \n",tail)
print("Probability of heads=",np.mean(head))
print("Probability of tails=",np.mean(tail))
