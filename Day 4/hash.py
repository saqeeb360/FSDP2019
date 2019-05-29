# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:32:51 2019

@author: Windows
"""

import hashlib
def hash_file(filename):    
    fil1 = open(filename, "rb")
    # make a hash object
    h = hashlib.sha1()
    
    # loop till the nd of the file
    
    chunk = 0
    while chunk != b'':
        chunk = fil1.read(1024)
        h.update(chunk)
    
    # Print hex representation
    print(h.hexdigest())




