# -*- coding: utf-8 -*-
"""
Created on Tue Nov 3 21:37:48 2020

@author: YOSO_WANHH
"""
a,b,c,d=input().split()
x = int(a)
y = int(b)
z = int(c)
r = int(d)
#print(type(x))   轉型成功與否之檢查
if y-x==z-y : 
    print(x,y,z,r,r+(r-z))
else:
    print(x,y,z,r,r*int(r/z))
