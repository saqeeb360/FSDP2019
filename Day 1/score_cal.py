# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:45:47 2019

@author: Saqeeb

Name     :     Weighted score calculator

"""
A1_max = 100 #max assignment marks 
A2_max = 100
A3_max = 100

E1_max = 100 #max exam marks
E2_max = 100

A1 = 20
A2 = 20
A3 = 20

E1 = 90
E2 = 90

Weighted_score = ((A1+A2+A3)/(A1_max+A2_max+A3_max)*30 ) + ((E1+E2)/(E1_max+E2_max)*70)
print("Weighted score",Weighted_score)
