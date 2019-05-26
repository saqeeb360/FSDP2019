# -*- coding: utf-8 -*-
"""
Created on Sat May 25 23:30:32 2019

@author: Windows
"""
#import csv
#
#with open("mailing.txt") as file1:
#    file2=csv.reader(file1,delimiter=",")
#    next(file2)
#    for row in file2:
#        print(row)

# list of those emails which are not present in new list
difference_email_list = list(set(old_list).difference(new_list))

print(difference_email_list)



