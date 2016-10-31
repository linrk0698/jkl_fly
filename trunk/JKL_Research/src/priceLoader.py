'''
Created on Aug 8, 2016

@author: kevin
'''
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Read S&P 500 Stock Tickers
    sp500_list = pd.read_csv('list_SP500_test.csv')
    print (sp500_list['Ticker'])
    goog = web.DataReader(sp500_list['Ticker'], data_source='google', start='1/1/2016', end='08/07/2016')
    goog['Close'].replace(to_replace=0,method='ffill')
#     goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
#     goog['Volatility'] = goog['Log_Ret'].rolling(window=252,center=False).std()*np.sqrt(252)
#     goog['Log_Ret'].to_csv('log_ret.csv')
#     goog['Volatility'].to_csv('vol.csv')
#     goog['Log_Ret'].plot(subplots=True)
#     plt.plot(goog[['Close','Volatility']])
#     ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
#     ts = ts.cumsum()
#     ts.plot()
#     plt.show()