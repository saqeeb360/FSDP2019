# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:10:15 2019

@author: Windows
"""

list1 = ["1221","-61","-5","14"]

positive=all([int(i)>0 for i in list1])

list2=[item[::-1]==item for item in list1]
palin=any(list2)
list3=[positive,palin]
print(all(list3))

#
#for n in list1:
#    if int(n) < 0:
#        print ("No is negative")
#        flag=False
#        break
#    
#if flag == True:        
#    for number in list1:
#        z=number[::-1]
#        if number==z:
#            print(True)
#            break
#        
