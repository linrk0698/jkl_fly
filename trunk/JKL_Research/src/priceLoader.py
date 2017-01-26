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

spOption_ggle= Options('aapl','yahoo')
optionData_ggle = spOption_ggle.get_all_data()
optionData_ggle.iloc[0:5,0:5]
#
#from wallstreet import Stock, Call, Put
#s = Stock('AAPL')
#g = Call('GOOG',d=17,m=3,y=2017,strike=700)
#g.price
#g.implied_volatility()

