# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:21:57 2017

@author: Kevin Lin
"""
from lxml.html import parse
from lxml import html
import requests

# get web content
base_url = 'http://finance.yahoo.com/q/op?s=XLK'
test_url = 'http://econpy.pythonanywhere.com/ex/001.html'
page = parse(base_url)
root = page.getroot()

# parse 

## parse expiry date
expDateNodes = root.xpath("//div[contains(@class,'Fl(start)')]")
#expDateNodes = root.xpath('//option')

#expDateNodes = root.xpath('//div[contains(@title,"buyer-name")]/text()')

#==============================================================================
# links = root.xpath('//*[@id="options_menu"]/form/select/option')
#==============================================================================
#==============================================================================
# //td[contains(@class, 'text')]
#==============================================================================
## parse prices

## parse strike price 


