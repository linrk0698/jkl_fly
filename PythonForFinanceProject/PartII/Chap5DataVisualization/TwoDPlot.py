# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:38:29 2016

@author: kevin
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(2000)
y = np.random.standard_normal((20,2)).cumsum(axis=0)

plt.figure(figsize=(9,4))
plt.subplot(121)
plt.plot(y[:,0],lw=1.5,label='1st')
plt.plot(y[:,0],'ro')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('1st Data Set')
plt.subplot(122)
plt.bar(np.arange(len(y)),y[:,1],width=0.5,color ='g',label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.title('2nd Data Set')
# Scatter Plot
y = np.random.standard_normal((1000,2))
plt.figure(figsize=(7,5))
plt.plot(y[:,0],y[:,1],'ro')
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')

# Scatter Plot. matplotlib specific function. 
plt.figure(figsize=(7,5))
plt.scatter(y[:,0],y[:,1],marker='o')
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scater Plot')
