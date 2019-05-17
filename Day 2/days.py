# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:47:45 2019

@author: Saqeeb

Name   :  Days in a month

"""

def day_in_month(a):
    if a=="jan":
        print("days in jan = 31")
    elif a=="feb":
        print("feb = 28")
    elif a=="mar":
        print("mar = 31")
    else:
        print("Enter correct month")

x=input("Enter the month = ")
day_in_month(x)

