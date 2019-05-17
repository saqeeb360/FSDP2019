# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:09:42 2019

@author: Windows
"""

import csv
#
#with open("population.csv","rt") as file1:
#    file2=(csv.reader(file1,delimiter=","))
#    next(file2)
#    for row in file2:
#        print (row)
def checker(x):
    if str1 in x.values():
        xyz= True 
    else:
        xyz= False
    return xyz


dict1={}
list_total=[]
       
with open("population.csv","r") as file1:
    file2=(csv.reader(file1,delimiter=","))
    next(file2)
    for list1 in file2:
        flag=True
        str1=list1[-1]
        
        if len(list_total)==0:
            dict1["key"]=list1[-1]
            
            popul=list1[-2]
            pop_list=popul.split(",")
            popul2=""
            for item in pop_list:
                popul2=popul2+item
            popul2=int(popul2)
            
            
            dict1["value"]=popul2
            list_total.append(dict1.copy())
            flag=False
            
            
        
        if flag==True:
            list2=list(map(checker,list_total))
            found = any(list2)
            if not found:
                dict1["key"]=list1[-1]
                
                popul=list1[-2]
                pop_list=popul.split(",")
                popul2=""
                for item in pop_list:
                    popul2=popul2+item
                popul2=int(popul2)
                
                
                dict1["value"]=popul2
                
                list_total.append(dict1.copy())
                
                
            else:
                popul=list1[-2]
                pop_list=popul.split(",")
                popul2=""
                for item in pop_list:
                    popul2=popul2+item
                popul2=int(popul2)
                
                
                
                for dictx in list_total:
                    if list1[-1] in dictx.values():
                        
                        dictx["value"]=dictx["value"]+popul2
                                     
                
                
#                
#                dict1["key"]=list2[-1]
#                print(dict)
#                dict1["value"]=dict["value"] + popul2
#                list_total_append(dict1)
                            
            
#            list_total.append(dict1)
#            print(list_total)
#            
            



#dict1["key"]="India , "+ list1[-1]
#list_total.append(dict1)
#z=list1[-2]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            