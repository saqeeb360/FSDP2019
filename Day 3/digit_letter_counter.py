# -*- coding: utf-8 -*-
"""
Created on Fri May 10 00:42:36 2019

@author: Windows
"""
# METHOD 1
#str1=input("Enter string : ")
#str1=" ".join(str1)
#str1=str1.lower()
#
#list1=str1.split()
#
#abc="asdfghjklqwertyuiopzxcvbnm"
#dict1={}
#i=0
#j=0
#for k in list1:     
#    if k in "1234567890":
#        j=j+1
#        dict1["Digits"]=j
#    elif k in abc:
#        i=i+1
#        dict1["Letters"]=i
#for key in dict1:
#    print(key,dict1[key])
    
# METHOD 2

dict1={}

str1=input("Enter String : ")
for char in str1:
    if char.isalpha():
        dict1["Letters"]=dict1.get("Letters",0) +1
    elif char.isdigit():
        dict1["Digits"]=dict1.get("Digits",0) +1
        
print(dict1)


        
        