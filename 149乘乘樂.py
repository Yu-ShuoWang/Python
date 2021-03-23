# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:09:55 2021

@author: YOSO_WANHH
"""
#a149: 乘乘樂

amount = int(input())
for i in range(amount):
    x = 1
    num = input()
    for j in num:
        j = int(j)
        x = x*j
    print(x)