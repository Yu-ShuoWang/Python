# -*- coding: utf-8 -*-
"""
Created on Tue Fri 26 13:17:04 2021

@author: YOSO_WANHH
"""
#a225: 明明愛排列

while True:
    try:
        n = int(input())
        n = [int(i) for i in input().strip().split(' ')]
        n.sort(reverse = True)
        n.sort(key = lambda x : x % 10 )
        print(' '.join([str(i) for i in n]))

    except:
        break