# -*- coding: utf-8 -*-
"""
Created on Sat May 11 02:56:02 2019

@author: Windows
"""

import csv 
i=0
list1=[]
list2=[]
letter={}
with open("romeo.txt", "rt") as file1:
    file2=csv.reader(file1,delimiter=" ")
    for row in file2:
        i=i+1
        list1=list1+row
    print("No of sentences is  "+str(i))
    print("No of words is   "+ str(len(list1)))
    for word in list1:
        word="$".join(word)
        temp_list=word.split("$")
        list2=temp_list+list2
    print("No of char is  " + str(len(list2)))
    
    for le in temp_list:    #no of unique char
            if le not in letter:    
                letter[le]=1
            else:
                x=letter[le]
                letter[le]=x+1
        
        
            
        
        
        
    
        
    
       