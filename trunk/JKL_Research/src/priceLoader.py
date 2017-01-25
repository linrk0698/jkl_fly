'''
Created on Aug 8, 2016

@author: kevin
'''
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib
import matplotlib.pyplot as plt

from pandas.io.data import Options

# Read S&P 500 Stock Tickers
tickerFile = '../data/list_SP500_test.csv'
sp500_list = pd.read_csv(tickerFile)
print (sp500_list['Ticker'])
goog = web.DataReader(sp500_list['Ticker'], data_source='google', start='1/1/2016', end='08/07/2016')
goog['Close'].fillna(0)

spOption_ggle= Options('aapl','yahoo')
optionData_ggle = spOption_ggle.get_all_data()
optionData_ggle.iloc[0:5,0:5]

from wallstreet import Stock, Call, Put
s = Stock('AAPL')
s.prices
s.change
s.last_trade
g = Call('GOOG',d=12,m=2,y=2016,strike=700)
g.price
g.implied_volatility()

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