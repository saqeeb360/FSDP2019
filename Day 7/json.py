# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:51:56 2019

@author: Windows
"""

import requests
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Udaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url = url1+url2+url3
print(url)

response = requests.get(url)
response.content

print(jsondata["coord"]["lat"])
print(jsondata["coord"]["lon"])
print(jsondata["sys"]["sunrise"])
