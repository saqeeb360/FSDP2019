# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:02:09 2019

@author: Saqeeb
Name Bricks
"""
x=int(input( "no of small bricks "))
y=int(input("no of big bricks ") )
z=int(input("required length "))
list=[x,y,z]
def brick(list):
    temp=list[0]+(list[1]*5)
    if temp < list[2] :
        print("False")
    else :
        print("True")
        
brick(list)
