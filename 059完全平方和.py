# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:29:18 2021

@author: YOSO_WANHH
"""
from math import sqrt #開根號
#import math
n = int(input())

for i in range(n):
    a = int(input())
    b = int(input())
    
    # Current Square Number
    curSquare = 0
    
    # Minimal square root
    minRoot = int(sqrt(a))
    if minRoot * minRoot == a:
        curSquare = a
    else:
        minRoot = minRoot + 1
        curSquare = minRoot * minRoot
    squareSum = 0
    while curSquare <=b:
        squareSum += curSquare
        minRoot += 1
        curSquare = minRoot * minRoot
    
    print("Case " + str(i+1) + ":", squareSum)
