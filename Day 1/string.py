# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:39:07 2019

@author: Saqeeb

Name    : string handling

"""
str1="Sylvester Fernandes"
pos=str1.find(" ")
print(pos)
y=str1[pos+1:]+ " " +str1[0:pos]
print(y)
