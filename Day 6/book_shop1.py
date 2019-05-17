# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:47:02 2019

@author: Windows
"""

list1=["34587 Learning Python, Mark Lutz  4 40.95"]
list2=["98762 Programming Python, Mark Lutz 5 56.80"]
list3=["77226 Head First Python, Paul Barry 3 32.95"]
list4=["88112 Einführung in Python3, Bernd Klein  3 24.99"]

list1=list1[0].split()
list2=list2[0].split()
list3=list3[0].split()
list4=list4[0].split()

list5=[list1,list2,list3,list4]
#
#list6=[]
#
#for list in list5:
#    x=float(list[-1])*float(list[-2]) 
#    if x < 100:
#        x=(float(list[-1])*float(list[-2]))+10
#    
#    list6.append((list[0],x))
#print(list6)  

def for_list(x):
    z=float(x[-1])*float(x[-2])
    if z < 100:
        z = float(x[-1])*float(x[-2])+10
    y=(x[0],z)
    return y

#list7=list(map(lambda x:(x[0],x[-1],x[-2]),list5))
#list7=list(map(lambda x: (x[0],float(x[-1])*float(x[-2])+10) if float(x[-1])*float(x[-2])<100 else (x[0],float(x[-1])*float(x[-2])) ,list5))

list7=list(map(for_list,list5))


