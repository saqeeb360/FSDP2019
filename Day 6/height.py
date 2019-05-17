# -*- coding: utf-8 -*-
"""
Created on Mon May 13 23:55:15 2019

@author: Windows
"""

people = [{'name': 'Mary', 'height': 160},{'name': 'Isla', 'height': 80},
          {'name':'Sam'}]
#
#height_total = 0
#height_count = 0
#for person in people:
#    if 'height' in person:
#        height_total += person['height']
#        height_count += 1
#
#if height_count > 0:
#    average_height = height_total / height_count
#
#    print (average_height)

list4=[]
def list_height(x):
    if 'height' in x:
        list4.append(x['height'])

list(map(list_height,people))      


#list3=list(map(lambda x:,people))


