# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:09:30 2019

@author: Windows
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area

Scrap the data from State/Territory and National Share (%) columns for top 6 states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""

from selenium import webdriver
from time import sleep
from collections import OrderedDict
from bs4 import BeautifulSoup
import requests

url ="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
browser = webdriver.Chrome("C:/Users/Windows/Desktop/Machine learning/chromedriver.exe")
browser.get(url)
sleep(2)
right_table = browser.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]')
print(right_table)
#wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#source = requests.get(wiki).text
#soup = BeautifulSoup(source,"lxml")
#right_table=soup.find('table', class_='wikitable')

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    if len(cells) == 7:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
















