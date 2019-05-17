# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:33:21 2019

@author: Windows
"""

from bs4 import BeautifulSoup
import requests

url="https://bidplus.gem.gov.in/bidlists"

web_content=requests.get(url).text
with open("samp.html","w") as f:
    f.write(web_content)

soup=BeautifulSoup(web_content,"lxml")


xyz=soup.findAll("div",{"class":"border block "})
bid_no=[]
items=[]
list1=[]

for row in xyz:
    bid_no.append(row.div.p.text)
    items=row.findAll("div",class_="col-block")
    list1.append(items)
    print(items)
    break
#    x=row.find("p")
#    cells = row.findAll("div",class_="col-block")
#    print()


#data_box=soup.findAll('dir',{"class":"block_header")
#print(data_box)
