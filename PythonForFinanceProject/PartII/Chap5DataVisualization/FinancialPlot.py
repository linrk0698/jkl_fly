# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:30:14 2016

@author: kevin
"""

import matplotlib.finance as mpf
import matplotlib.pyplot as plt

start = (2014,5,1)
end   = (2014,6,30)

quotes = mpf.quotes_historical_yahoo_ohlc('^GDAXI',start,end)

plt.figure(figsize = (8,5))
plt.candle