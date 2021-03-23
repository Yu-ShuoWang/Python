# -*- coding: utf-8 -*-
"""
Created on Sun Nov 1 21:03:03 2020

@author: YOSO_WANHH
"""
'''
month = input("月份: ")
date  = input("日期: ")
month = int(month)
date  = int(date)
function = (month*2+date)%3
if(function==0):
    print("普通")
elif(function==1):
    print("吉")
else:
    print("大吉")
'''

month = int(input("月份: "))
date  = int(input("日期: "))

function = (month*2+date)%3
if(function==0):
    print("普通")
elif(function==1):
    print("吉")
else:
    print("大吉")
