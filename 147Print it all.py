# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:55:17 2021

@author: YOSO_WANHH
"""
#a147: Print it all
while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(" ".join([str(n) for n in range(0,n) if n % 7 != 0]))