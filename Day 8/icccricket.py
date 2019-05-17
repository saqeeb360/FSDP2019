# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:31:31 2019

@author: Windows
"""

from bs4 import BeautifulSoup
import requests
url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
saqeeb=requests.get(url).text
soup =BeautifulSoup(saqeeb,"lxml")
#all_tables=soup.find_all('table')
right_table=soup.find('table', class_='table')
print(right_table)
A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
import pandas as pd
from collections import OrderedDict

col_name = ["Rank","Country","Weighted Match","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")










#with open("samp.html","w") as f:
#    f.write(saqeeb)


