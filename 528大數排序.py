# -*- coding: utf-8 -*-
"""
Created on Fri Mar 5 22:33:30 2021

@author: YOSO_WANHH
"""
#a528: 大數排序

while True:
    try:
        n = int(input())
        a = []
        for i in range(n):
            a.append(int(input()))
            a.sort()
        for j in range(n):
            print(a[j])
    except EOFError:
        pass
    
