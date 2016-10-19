# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:36:54 2016

@author: kevin
"""

#Approximation
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + 0.5*x

x = np.linspace(-2*np.pi,2*np.pi,50)
plt.plot(x,f(x),'b')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

# Regression
reg = np.polyfit(x,f(x),deg=1)
ry= np.polyval(reg,x)

plt.plot(x,f(x),'b',label = 'f(x)')
plt.plot(x,ry,'r.',label='regression')
plt.legend(loc=0)
plt.rid(True)
plt.xlabel('x')
plot.ylabel('f(x)')

# Convex Optimization
def fm((x,y)):
    return (np.sin(x) + 0.05 * x **2
            +np.sin(y) + 0.05 * y ** 2) 
            
x = np.linspace(-10, 10,50)
y = np.linspace (-10,10,50)
X,Y = np.meshgrid(x,y)
Z = fm((X,Y))

fig = plt.figure(figsize = (9,6))
ax = fig.gca(projection = '3d')
surf = ax.plot_surface(X,Y,Z,restride = 2, cstride = 2,cmap = mpl.cm.coolwarm,
                       linewidth = 0.5,antialiased = True)
ax.set_xlabel('x)
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
fig.colorbar(surg,shrink = 0.5,aspect = 5)