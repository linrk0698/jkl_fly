'''
Created on Aug 8, 2016

@author: kevin
'''
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib
import matplotlib.pyplot as plt
from datetime import date,datetime, timedelta
from pandas_datareader.data import Options
import math

cols = ['Last','Bid','Ask','Vol','Open_Int','IV']
tickerList = pd.read_csv('../data/list_option_ticker.csv')
indexSym = tickerList['ticker']
underlying = tickerList['underlying']
isIndex  = tickerList['index']
steps = tickerList['step']

for counter in range (0,len(indexSym)):
    curIndexSym = indexSym[counter]
    curUnderlying = underlying[counter]
    curSteps = float(steps[counter])
    filename = '../data/optionData.csv'
    curIsIndex = bool(isIndex[counter])
    print('Processing '+curIndexSym)
    if curIsIndex:
        option= Options('^'+curIndexSym,'yahoo')
        indexData = web.DataReader('^'+curUnderlying,'yahoo',start,end)
    else:
        option = Options(curIndexSym,'yahoo')
        indexData = web.DataReader(curUnderlying,'yahoo',start,end)
    optionData = option.get_all_data()
    optionData = optionData.loc[:,cols]
    
    # Select price/index level around which we will save the price. 
    LEVEL = 0.07
    today = date.today() - timedelta(1)
    if today.isoweekday() == 7:
        start = today-timedelta(2)
    elif today.isoweekday() == 6:
        start = today-timedelta(1)
    else:
        start = today
    end = start
    lowerBnd = max (indexData['Close'][0] - indexData['Close'][0]*0.07,0)
    upperBnd = indexData['Close'][0]+indexData['Close'][0]*0.07
    lowerBnd = math.floor(lowerBnd/curSteps)*curSteps
    upperBnd = math.ceil(upperBnd/curSteps)*curSteps
    idxx = optionData.index.get_level_values(level='Strike')
    mask = (idxx>=lowerBnd) & (idxx <=upperBnd)
    idx = pd.IndexSlice
    optionData2 = optionData.loc[idx[mask,:,:,:],:]

    # Add another layer to the index. 
    optionData2['Dates'] = today.strftime('%Y%m%d')
    optionData2.set_index('Dates',append=True,inplace=True)
    optionData2=optionData2.reorder_levels(['Dates','Symbol','Strike','Expiry','Type'])
    # Write out file
    optionData2.to_csv(filename,mode='a',header=False)
print('Finished all')