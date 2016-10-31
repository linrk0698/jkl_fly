# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:16:30 2016

@author: kevin
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.stats.diagnostic as ssd
import numpy as np
import math

plt.close()
# Data 1
filename = '../data/data_1_5.csv'
data1 = pd.read_csv(filename)
data1.plot(figsize=(7,5),title='data1')
data1.plot.scatter(figsize=(7,5),x='x',y='y',title='data1')

X = sm.add_constant(data1['x'])
y = data1['y']
res = sm.OLS(y,X).fit()
print(res.summary())
plt.plot(data1['x'],res.predict(),'r')
plt.figure(figsize=(7,5))
plt.scatter(data1.x**2,res.resid)
plt.title('X vs Resid')

# Test for Heteroskedacity - White test
white_tst = ssd.het_white(res.resid,X)
print ('White test LM is',white_tst[0])
## Data 2
#filename = '../data/data_1_2.csv'
#data2 = pd.read_csv(filename)
#data2.plot(title='data2')
#data2.plot.scatter(x='x',y='y',title='data2')
#
## Data 3
#filename = '../data/data_1_3.csv'
#data3 = pd.read_csv(filename)
#data3.plot(title='data3')
#data3.plot.scatter(x='x',y='y',title='data3')
#
## Data 4
#filename = '../data/data_1_4.csv'
#data4 = pd.read_csv(filename)
#data4.plot(title='data4')
#data4.plot.scatter(x='x',y='y',title='data4')
#
## Data 5
#filename = '../data/data_1_5.csv'
#data5 = pd.read_csv(filename)
#data5.plot(title='data5')
#data5.plot.scatter(x='x',y='y',title='data5')

