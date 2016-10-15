# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:28:06 2016

@author: kevin
"""

import pandas as pd
import numpy as np
import urllib.request as urlreq
import datetime as dt
import matplotlib.pyplot as plt

es_url = 'http://www.stoxx.com/download/historical_values/hbrbcpe.txt'
vs_url = 'http://www.stoxx.com/download/historical_values/h_vstoxx.txt'

urlreq.urlretrieve(es_url,'./data/es.txt')
urlreq.urlretrieve(vs_url,'./data/vs.txt')

lines = open('./data/es.txt','r').readlines()
lines = [line.replace(' ','') for line in lines]

for line in lines[3883:3890]:
    print(line[41:])

# Clean up the file
#1. Generate a new text file
#2. Delete unneeded header lines
#3. Write an approriate new header line to the new file. 
#4. Add a helper column, DEL (To catch trailing semicolons). 
#5. Write all data rows to the new file. 

# Open a new file.
new_file = open('./data/es50.txt','w')

# Writes the corrected third line of the original file as first line of new file. 
new_file.writelines('date'+ lines[3][:-1] + ';DEL' + lines[3][-1])

# Writes the remaining lines of the original file. 
new_file.writelines(lines[4:])

##Close
new_file.close()

new_lines = open('./data/es50.txt','r').readlines()
new_lines[:5]

# Read it using read_csv fn. 
es = pd.read_csv('./data/es50.txt',index_col = 0,parse_dates = True,sep = ';',dayfirst=True)
np.round(es.tail())

del es['DEL']
es.info()

vs = pd.read_csv('./data/vs.txt',index_col = 0,header=2,parse_dates=True,sep=',',dayfirst=True)
vs.info()

data = pd.DataFrame({'EUROSTOXX':es['SX5E'][es.index>dt.datetime(1999,1,1)]})
data = data.join(pd.DataFrame({'VSTOXX' :vs['V2TX'][vs.index>dt.datetime(1999,1,1)]}),how='inner')
data = data.fillna(method='ffill')
data.info()
data.tail()
data.plot(subplots=True,grid=True,style='b',figsize=(8,6))

rets = np.log(data/data.shift(1))
rets.head()
rets.plot(subplots = True,grid=True,style='b',figsize=(8,6))

xdat = rets['EUROSTOXX']
ydat = rets['VSTOXX']
model = pd.ols(y=ydat,x=xdat)
model

plt.plot(xdat,ydat,'r.')
ax = plt.axis()
x = np.linspace(ax[0],ax[1]+0.01)
plt.plot(x,model.beta[1]+model.beta[0]*x,'b',lw = 2)
plt.grid(True)
plt.axis('tight')
plt.xlabel('Euro Stoxx 50 Returns')
plt.ylabel('Vstoxx returns')

# Correlation
rets.corr()
pd.rolling_corr(rets['EUROSTOXX'],rets['VSTOXX'],window = 252).plot(grid=True,style='b')