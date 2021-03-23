# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:41:22 2021

@author: YOSO_WANHH
"""
x = int(input())
sum = 0
for i in range(1,x+1):
    sum = sum + 1 + (x-1)* x / 2
print(int(sum))

