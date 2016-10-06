# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:10:15 2016

@author: kevin
"""

from option_bsm import bsm_call_value

S0 = 100.
K = 105.
T = 1.0
r = 0.05
sigma = 0.2
a = bsm_call_value(S0,K,T,r,sigma)