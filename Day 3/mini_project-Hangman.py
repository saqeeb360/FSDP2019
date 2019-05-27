# -*- coding: utf-8 -*-
"""
Created on Mon May 27 08:53:41 2019

@author: Windows
"""
list1=["Ashamim","Bsaqeeb","Csabina","Dshaista","Eshaheen","Fanimul"]
import random
index=random.randint(0,1)

flag = True

for alphabet in list1[index]:
        i=0
        while i<3:
            if flag == False:
                break
            flag = True
            print("remaining chance : ",3-i)
            user_input=input("> ")
            if not user_input:
                print("Game Over")
                flag = False
                break
            if flag == True:
                if len(user_input) > 1:
                    print("Enter a Letter")
                elif user_input==alphabet:
                    print("correct")
                    flag = False
                else:
                    print("wrong")
            
            i=i+1
                
            
            
                
                
                
                
                
                
                
                
                
                
                
                
    

                