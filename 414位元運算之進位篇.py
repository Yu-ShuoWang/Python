# -*- coding: utf-8 -*-
"""
Created on Thu Mar 4 18:26:59 2021

@author: YOSO_WANHH
"""
#a414: 位元運算之進位篇

while True:
    n = int(input())
    if n<=0:
        break
    count = 0
    while (n % 2):
        count += 1
        n //= 2
        
    print(count)    