# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:25:31 2016

@author: kevin
"""

import pandas.io.data as web

SPX = web.DataReader(name='^GSPC',data_source = 'yahoo',start = '2000-1-1')

#Plot is easy.
SPX['Close'].plot(figsize=(7,4))
SPX['Return'] = np.log(SPX['Close']/SPX['Close'].shift(1))
SPX[['Close','Return']].tail()

#rolling mean
SPX['42d'] = pd.rolling_mean(SPX['Close'],window=42)
SPX['252d'] = pd.rolling_mean(SPX['Close'],window=252)
SPX[['Close','42d','252d']].tail()

#rolling vol
import math
SPX['Mov_vol'] = pd.rolling_std(SPX['Return'],window=252)*math.sqrt(252)
SPX[['Close','Mov_vol','Return']].plot(subplots=True,style='b',figsize=(8,7))
