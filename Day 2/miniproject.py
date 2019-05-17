# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:20:16 2019

@author: Windows
"""
list=[]

print ("What should we pick up at the store ?")
print ("Enter 'DONE' to stop adding items.")

while True:
    item=input("> ")
    if item == "DONE" or item == "Done" or item == "done":
        break
    if item == "SHOW" or item == "Show" or item == "show":
        for item in list:
            print(item)
            item=""
    elif item == "HELP" or item == "Help" or item == "help":
        print("list of command \nHELP \nDONE\nSHOW\nCLEAN")
        item=""
    elif item == "CLEAN" or item == "Clean" or item == "clean":
        list.clear()
        item=""
        
        
    list.append(item)

"""def show():
    for item in list:
    print(item)
"""

i=0
print("Here’s your list")
for item in list:
    i=i+1
    print (str(i) +". " + item )
    
    
    
