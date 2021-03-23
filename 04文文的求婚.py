# -*- coding: utf-8 -*-
"""
Created on Mon Nov 2 21:23:05 2020

@author: YOSO_WANHH
"""

    
    

while True:
    try:
        y = int(input())
    
        if ((y%4==0) and (y%100!=0)) or (y%400==0):
            print("閏年")
        else:
            print("平年")
    except:
        break