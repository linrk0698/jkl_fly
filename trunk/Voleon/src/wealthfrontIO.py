# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:06:01 2016

Wealthfront Interview Question 3. 

@author: kevin
"""
import pandas as pd
from pandas.tseries.offsets import *
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from pandas.stats.api import ols
import numpy as np
import math

# Load and Plot Data
path = '../data/wealthfront.xls'
data = pd.read_excel(path,sheetname=0)
data.index = pd.to_datetime(data.index,format='%Y%m%d')
data.plot(subplots=True)

# Calculate Rolling Average 
sp500 = data['SP500']
tbill = data['1M T-bill']
sp500_3m = pd.rolling_mean(sp500,window=3)
sp500_3m.columns = 'SP500_3m'

sp_total = pd.concat([sp500,sp500_3m],axis=1)
sp_total.columns = ['SP500','SP500_3m']
sp_total.plot(figsize=(7,3))

# Calculate Mean and Volatility
sp_mean = sp_total.mean()*12
sp_std  = sp_total.std()*math.sqrt(12)
# Calculate Sharpe Ratio
sp_excess = sp_total.subtract(tbill,axis=0)
sp_excess_mean = sp_excess.mean()*12
sr = sp_excess_mean.divide(sp_std)

# Calculate CAPM Alpha and Beta
capm_model = ols (y=sp_excess['SP500_3m'],x=sp_excess['SP500'])
capm_model