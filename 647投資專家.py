# -*- coding: utf-8 -*-
"""
Created on Sat Mar 6 10:21:30 2021

@author: YOSO_WANHH
"""
#a647: 投資專家

n = int(input())
for i in range(n):
    num = input().split()
    x = (int(num[1]) - int(num[0])) / int(num[0]) * 100
    if x > 10 or x <= -7:
        print('%.2f'%x + '%', 'dispose')
    else:
        print('%.2f'%x + '%', 'keep')