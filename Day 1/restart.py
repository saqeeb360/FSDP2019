# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:48:55 2019

@author: Saqeeb

Name    :Replacing of character

"""

str1="RRWIRIHIRFHWIHRHART"
pos= str1.find("R")             
str2=str1[pos+1::1]
str3=str2.replace("R","%")
print(str1[0:pos+1]+str3)  
print(str1[0:pos+1]+str1[pos+1::1].replace("R","%"))      #code in one line