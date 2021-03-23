# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:18:42 2021

@author: YOSO_WANHH
"""
#a148: You Cannot Pass?!

try:
    while True:
        a = list(map(int,input().split()))
        b = 0
        for i in range(1,len(a)):
            b = b + a[i]
        if b > 59 * a[0]:
            print("no")
        else:
            print("yes")
except EOFError:
    pass
