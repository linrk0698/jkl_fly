# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:04:19 2016

@author: user
"""

import numpy as np
import pandas as pd

df = pd.DataFrame([10,20,30,40],columns = ['numbers'],index=['a','b','c','d'])
# Expand another columns. 
df['floats'] = (1.5,2.5,3.5,4.5)

# Another DataFrame object can be added to existing DataFrame object. 
df['names'] = pd.DataFrame(['Yves','Guido','Felix','Francesc'],index = ['d','a','b','c'])

# Append Data
# 1. If appending without specifying index, then the new dataframe object will not have original index. 
df = df.append(pd.DataFrame({'numbers':100,'floats':5.75,'names':'Henry'},index=['z']))

# Deal with missing data. 
df=df.join(pd.DataFrame([1,4,9,16,25],index=['a','b','c','d','y'],columns=['squares']),how='outer')

# Funciton with Missing Data
df[['numbers','squares']].mean()
df[['numbers','squares']].std()

