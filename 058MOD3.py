# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:19:42 2021

@author: YOSO_WANHH
"""

#a058: MOD3
while True:
    try:
        b = 0
        c = 0
        d = 0
        inputSize = int(input().strip('\r'))
        for i in range(0,inputSize,1):    
            a=int(input().strip('\r'))
            if a%3==0:
                b += 1
            elif a%3==1:
                c += 1
            else:
                d += 1
        print('%d %d %d' % (b, c, d))
    except EOFError:
        break  