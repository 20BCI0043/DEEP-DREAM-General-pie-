# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 10:33:51 2020

@author: 91852
"""

# Import libraries 
from matplotlib import pyplot as plt 

# Creating dataset
print('enter number of entries')
i=int(input())


s={}        #To update the further entries
j=1

while j<=i:
    print("enter name and value")
    d={input():int(input())}
    j+=1
    s.update(d)

#generating list
k=list(s.keys())
v=list(s.values())


# Creating plot 
fig = plt.figure(figsize =(10, 7)) 
plt.pie(v, labels = k) 

# show plot 
plt.show() 

