# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:27:00 2019

@author: Windows
"""

import requests
url="http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=27ee76c60533b2f01fa5"
saqeeb = requests.get(url)

number=int(input("Enter a value in $ "))
print("$ "+ str(number)+" = Rs " + str(number*rate["USD_INR"]))



