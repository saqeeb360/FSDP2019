# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:31:35 2019

@author: Shamim and Saqeeb
Name :   Fizz Buzz

"""
i=0

while(i<100):
    i=i+1
    if(i%3==0 and i%15!=0):
        print("Fuzz")
    elif(i%5==0 and i%15!=0):
        print("Buzz")
    elif(i%15==0):
        print("FizzBuzz")
    else:
        print(i)
        