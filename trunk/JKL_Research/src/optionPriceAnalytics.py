# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:04:11 2017

@author: Kevin Lin
"""

import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib
import matplotlib.pyplot as plt

optionFile = '../data/optionData.csv'
optionTickerFile = '../data/list_option_ticker.csv'
# Read Option Price Data
optionData = pd.read_csv(optionFile,index_col=[0,1,2,3,4])
tickerList = pd.read_csv('../data/list_option_ticker.csv')

indexSym = tickerList['ticker']
underlying = tickerList['underlying']

# for each unique ticker symbol, calculate price return using the average of 
# bid and ask price, and last price only. 

