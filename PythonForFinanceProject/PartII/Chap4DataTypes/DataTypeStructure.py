# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:03:26 2016

@author: user
"""

a = 10
type (a)

t = (1,2.5,'data')
type (t)

t = 1,2.5,'data'
type(t)

l = [1,2.5,'data']
type(l)

l = [1,2,3,4,5,6]
l[0:5:3] = [9,10,11]
l.sort(reverse=True)
l

a = range(0,8,1)
type(a)

reduce(lambda x,y:x+y,range(3))

import numpy as np
a = np.array([0,0.5,1.0,1.5,2.0])
type(a)
a.sum()
a.cumsum()

c = np.zeros((2,3),dtype='i',order = 'C')
c.shape()

import random 
I = 5000
%time mat = [[random.gauss(0,1) for j in range(I)]for i in range (I)] 

%time mat=np.random.standard_normal((I,I))
%time mat.sum()

# Structured Arrays that allow us to have different numpy data types per column. 
dt = np.dtype([('Name','S10'),('Age','i4'),('Height','f'),('Children/Pets','i4',2)])
s = np.array([('Smith',45,1.83,(0,1)),
              ('Jones',53,1.72,(2,2))],dtype=dt)
s

# Memory Allocation
x = np.random.standard_normal((5,10000000))
y = 2 * x + 3 
C = np.array((x,y),order = 'C')
F = np.array((x,y),order = 'F')
x = 0.0; y = 0.0 # Memory cleanup
%timeit C.sum()
%timeit F.sum()

