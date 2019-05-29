# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:16:43 2019

@author: Windows
"""
def jpeg_res(filename):
    file1 = open(filename, "rb")
    file1.tell()
    file1.seek(163,0)
    # calculation of the height
    x = file1.read(2)
    print("Height is",(x[0]<<8)+x[1])
    
    # calculation of the width
    y = file1.read(2)
    print("Width is",(y[0]<<8)+y[1])
    file1.close()
jpeg_res("sample1.jpg")
