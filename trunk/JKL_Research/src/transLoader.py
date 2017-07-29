# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:23:47 2017

@author: Kevin Lin
"""

import pandas as pd
import os.path as op

dataPath = '../data/ExportData0630.csv'
budgetPath = '../data/budget.csv'
categoryMapPath = '../data/categoryMap.csv'
inflowCategoryPath = '../data/inflowCategory.txt'
transferCategoryPath = '../data/transferCategory.txt'

trxnFilePath = '../data/trxnMaster.csv'
data = pd.read_csv(dataPath)
data = data.drop(['Status','Split Type','Currency','User Description','Memo','Classification','Simple Description'],axis=1)
# read the budget file ()  
budgetData = pd.read_csv(budgetPath,sep=',',index_col=0)
expenseCategory = budgetData[['Category']]
expenseAmount = budgetData[['Budget']].astype(float)
# Read the inflow category and join together with expense category
inflowCategory = pd.read_csv(inflowCategoryPath,header=None,names=['Category'])
transferCategory = pd.read_csv(transferCategoryPath,header=None,names=['Category'])

budgetCategory = pd.concat([expenseCategory,inflowCategory,transferCategory],ignore_index = True)
# Read the category map. 
categoryMapData = pd.read_csv(categoryMapPath,sep=',',index_col=0)
# Replace invalid category based on category map. 
data = data.replace(to_replace=categoryMapData['Orig'].values,value=categoryMapData['Tgt'].values)
data['Id']=data['Date']+data['Original Description']+data['Amount']+data['Account Name']
data.set_index(['Id'],inplace=True)
# Print out warning on transactions that has invalid transaction which is also unmapped. 
dataInvalid = data.loc[~data['Category'].isin(budgetCategory['Category'].values)]
dataInvalidMatter = dataInvalid.loc[(dataInvalid['Amount'].replace('[\,]','',regex=True).astype(float)>1)|(dataInvalid['Amount'].replace('[\,]','',regex=True).astype(float)<-1)]

# Append the Transaction to output file. 

# Test if the data is ready to save
if dataInvalidMatter.empty:
    print('All Valid')
    if op.isfile(trxnFilePath):
        existingData = pd.read_csv(trxnFilePath)
        if ~existingData.empty:
            existingData['Id'] = existingData['Date']+existingData['Original Description']+existingData['Amount']+existingData['Account Name']
            existingData.set_index(['Id'],inplace=True)
            existingData.update(data)
            combinedData = existingData.combine_first(data)
            combinedData.to_csv(trxnFilePath,index=False)
        else: 
            data.to_csv(trxnFilePath,index=False)
    else:
        data.to_csv(trxnFilePath,index=False)
else: 
    print('There are {number} invlid entries.'.format(number=len(dataInvalidMatter))) 
