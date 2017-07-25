# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:44:18 2017

@author: Kevin Lin
"""

import pandas as pd
import numpy as np
import os.path as path
import datetime as dt
from pandas.tseries.offsets import *

trxnPath = '../data/trxnMaster.csv'
budgetPath = '../data/budget.csv'
inflowCategoryPath='../data/inflowCategory.txt'
transferCategoryPath='../data/transferCategory.txt'
budgetArchivePath='../data/budgetArchive/'

outputBudgetFilePath='../data/budgetMaster.csv'
# Read in budget amount and category
budgetData = pd.read_csv(budgetPath,sep=',',index_col=0)
expenseCategory = budgetData[['Category']]
budgetData['Budget'] = budgetData['Budget'].astype(float)
inflowCategory = pd.read_csv(inflowCategoryPath,header=None,names=['Category'])
transferCategory = pd.read_csv(transferCategoryPath,header=None,names=['Category'])

budgetCategory = pd.concat([expenseCategory,inflowCategory,transferCategory],ignore_index = True)


trxn = pd.read_csv(trxnPath)
trxn['Amount'] = trxn['Amount'].replace('[\,]','',regex=True).astype(float)
trxn['Date'] = pd.to_datetime(trxn['Date'],format='%m/%d/%Y')
maxDate = trxn[['Date']].max().iloc[0]
minDate = trxn[['Date']].min().iloc[0]
monthRange = pd.date_range(start=minDate,end=maxDate,freq = 'MS')

# Refactor the following to a function to calculate budget. 
output = pd.DataFrame(data=[],index=monthRange,columns=budgetCategory.values[:,0])
trxn.loc[:,'DateMonth'] = trxn['Date'].apply(lambda x:x.strftime('%Y%m'))
trxnPivot = pd.pivot_table(trxn,values='Amount',columns=['Category'],index=['DateMonth'],aggfunc=np.sum)
trxnPivot = trxnPivot.set_index(pd.to_datetime(trxnPivot.index,format='%Y%m'))
output.update(trxnPivot)
outputInflow = output.loc[:,output.columns.isin(inflowCategory['Category'])]
outputTransfer = output.loc[:,output.columns.isin(transferCategory['Category'])]
outputExpense = output.loc[:,output.columns.isin(expenseCategory['Category'])]         
output['TotalExpense'] = outputExpense.sum(axis=1)
output['TotalInflow'] = outputInflow.sum(axis=1)
output['TotalTransfer'] = outputTransfer.sum(axis=1)
summary = output.iloc[:,len(output.columns)-3:len(output.columns)]
output  = summary.join(output.iloc[:,0:len(output.columns)-3])
output.round(2)

# Print out the output

if path.isfile(outputBudgetFilePath):
    existingBudget = pd.read_csv(outputBudgetFilePath,index_col=0)
    existingBudget.round(2)
    existingBudget.update(output)
    existingBudget = existingBudget.combine_first(output)
    existingBudget.to_csv(outputBudgetFilePath,header=True,mode='w',index=True,float_format='%.2f')
else:
    output.to_csv(outputBudgetFilePath,header=True,float_format='%.2f',mode='w',index=True)
    
for n in range(len(output.index)):
    curMonth = output.index[n].strftime('%Y%m')
    curOutput = output.iloc[n,:].transpose()
    curOutput.to_csv(budgetArchivePath+curMonth+'.csv',float_format='%.2f')
    print(curMonth)


