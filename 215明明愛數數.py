# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 22:09:30 2021

@author: YOSO_WANHH
"""
#a215: 明明愛數數

while True:
  try:
    A,B = input().split()
    a = int(A)
    b = int(B)
    count = a
    xx = 1
    for i in range(1,10000,1):
      count = count+a+i
      
      if count>b:
        xx=i+1
        break
    
    print(xx)
  except:
    break
            
        
        