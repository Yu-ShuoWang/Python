# -*- coding: utf-8 -*-
"""
Created on Sun Nov 8 18:13:27 2020

@author: YOSO_WANHH
"""
'''
while True:
 n = int(input('Please input a number:\n'))
 sn = list(map(int,input('Please input some numbers:\n').split()))
 print(n)
 print(sn,'\n')
'''
import sys

for s in sys.stdin:
    print(eval(s.replace("/", "//")))
