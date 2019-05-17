# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:18:16 2019

@author: Windows
"""

import json

json_string="""
{
     "lecturer1":{
             "fname" : "Yogendra",
             "lname" : "Singh",
             "photo" : "url" ,
             "Department" : "CSE",
             "Research Areas" : "ML" 
            },
      "lecture2":{
             "fname" : "Pradeep",
             "lname" : "Natani",
             "photo" : "url" ,
             "Department" : "CSE",
             "Research Areas" : "Data Analysis" 
            }


}
"""

my_data = json.loads(json_string)
with open("faculty.json","w") as file1:
    json.dump(json_string,file1)
    

