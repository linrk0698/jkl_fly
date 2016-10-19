# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:47:54 2016

@author: kevin
"""

# Writing Objects to Disk
path = './flash/data/'
import numpy as np
from random import gauss

a = [gauss(1.5,2) for i in range (1000000)]


import pickle
pkl_file = open(path+'data.pkl','w')

# not working
pickle.dump(a,pkl_file)

pkl_file.close()

# Reading and Writing Text Files 
rows = 5000
a = np.random.standard_normal((rows,5))
a.round(4)

import pandas as pd
t = pd.date_range(start = '2014/1/1',periods = rows,freq = 'H')
t

csv_file = open(path+'data.csv','w')
header = 'date,no1,no2,no3,no4,no5\n'
csv_file.write(header)

for t_,(no1,no2,no3,no4,no5) in zip(t,a):
    s = '%s,%f,%f,%f,%f,%f\n' % (t_,no1, no2, no3, no4,no5)
    csv_file.write(s)
csv_file.close()

csv_file = open(path+'data.csv','r')
for i in range(5):
    print(csv_file.readline())
csv_file.close()

# SQL Databases
import sqlite3 as sq3
query = 'CREATE TABLE NUMBS (Date date, No1 real, No2 real)'
con = sq3.connect(path + 'numbs.db')
con.execute(query)
con.commit()

import datetime as dt
con.execute('INSERT INTO NUMBS VALUES(?,?,?)',(dt.datetime.now(),0.12,7.3))
data = np.random.standard_normal((10000,2)).round(5)
for row in data:
    con.execute('INSERT INTO numbs VALUES(?,?,?)',
                (dt.datetime.now(),row[0],row[1]))

con.commit()

con.execute('SELECT * FROM numbs').fetchmany(10)

## IO with pandas
data = np.random.standard_normal((1000000,5)).round(5)
data = pd.DataFrame(data)
%time data.to_csv(filename+'.csv')

%%time
pd.read_csv(filename+'.csv').hist(bins = 20)