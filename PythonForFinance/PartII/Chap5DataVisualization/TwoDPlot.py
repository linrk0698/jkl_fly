# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:23:23 2016

@author: user
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#%matplotlib inline


np.random.seed(1000)
y = np.random.standard_normal(20)

x = range(len(y))
plt.plot(x,y)
plt.plot(y.cumsum())
plt.grid(True)
plt.axis('tight')
plt.title('Hello')

plt.figure(figsize=(7,4))
plt.plot(y.cumsum(),'b',lw=1.5)
plt.plot(y.cumsum(),'ro')
plt.grid(True)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A simple plot')

np.random.seed(2000)
y = np.random.standard_normal((20,2)).cumsum(axis = 0)
plt.figure(figsize=(7,4))
plt.plot(y,lw=1.5)
plt.plot(y,'ro')
plt.grid(True)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')

# Add Legend
plt.figure(figsize = (8,5))
plt.plot(y[:,0],lw = 1.5, label = '1st')
plt.plot(y[:,1],lw = 1.5, label = '2nd')
plt.plot(y,'ro')
plt.grid(True)
plt.legend(loc = 0)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')

# Two y-axis
fig,ax1 = plt.subplots()
plt.plot(y[:,0],'b',lw = 1.5,label = '1st')
plt.plot(y[:,0],'ro')
plt.grid(True)
plt.legend(loc=8)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value 1st')
plt.title('A Simple Plot')
ax2 = ax1.twinx()
plt.plot(y[:,1],'g',lw = 1.5, label = '2nd')
plt.plot(y[:,1],'ro')
plt.legend(loc = 0)
plt.ylabel('value 2nd')

# Two Subplots
plt.figure(figsize=(7,5))
plt.subplot(211)
plt.plot(y[:,0],'b',lw = 1.5,label = '1st')
plt.plot(y[:,0],'ro')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')
plt.subplot(212)
plt.plot(y[:,1],'g',lw = 1.5,label = '2nd')
plt.plot(y[:,1],'ro')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')