# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:36:19 2019

@author: Saqeeb

Name    :    Cost calculator


"""

km =int(input("Enter distance travelled in a day : ")) #distance travelled daily
mileage = 18 #vehicle mileage km/litre
fuel_cost = 80 #cost of fuel per litre
driving_cost = (km/mileage*fuel_cost )  #average daily driving cost
print ("Driving cost = Rs",driving_cost)

