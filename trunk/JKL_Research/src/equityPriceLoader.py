'''
Created on Aug 8, 2016

@author: kevin
'''
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib
import matplotlib.pyplot as plt

# Read S&P 500 Stock Tickers
tickerFile = '../data/list_SP500_test.csv'
sp500_list = pd.read_csv(tickerFile)
print (sp500_list['Ticker'])
goog = web.DataReader(sp500_list['Ticker'], data_source='yahoo', start='1/1/2016')

goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
goog['Volatility'] = goog['Log_Ret'].rolling(window=252,center=False).std()*np.sqrt(252)
print ('Processed \n',sp500_list['Ticker'])
#goog['Log_Ret'].plot(subplots=True)
#plt.plot(goog['Volatility'])
