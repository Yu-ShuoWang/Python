# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:07:52 2021

@author: YOSO_WANHH
"""
#b294: 經濟大恐荒

n = int(input('輸入數字： '))

bread = list(map(int,input().split()))
sum = 0
for i in range(1,n+1):
    sum = bread[i-1] * i + sum
print(sum)
    
    

