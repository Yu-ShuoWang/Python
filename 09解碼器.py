# -*- coding: utf-8 -*-
"""
Created on Thu Nov 5 17:53:51 2020

@author: YOSO_WANHH
"""

trans = [ord(x) for x in input()]
trans = [x-7 for x in trans]

output = [chr(x) for x in trans]
print_="".join(output)
print(print_)
