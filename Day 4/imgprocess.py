# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:00:30 2019

@author: Windows
"""

from PIL import Image

img = Image.open("sample1.jpg")

img_m = img.convert(mode = "L")
img_m.show()

img_r = img.transpose(Image.ROTATE_270)
img_r.show()

crop_img = img.crop( box = (10,50,140,600))
crop_img.show()

print(img.size)
thumb = img
thumb.thumbnail((10,30))
thumb.show()

