# -*- coding: utf-8 -*-
"""
Created on Sun Mar 7 11:43:17 2021

@author: YOSO_WANHH
"""
#a693: 吞食天地
while True:
    try:
        n,m = input().split()
        n = int(n)
        m = int(m)
        
        food = []
        
        #一次全加好
        food = list(map(int,input().split()))
        for i in range(1,n+1):
            food[i] += food[i-1]
        
            #全部扣掉前面不吃就是答案
            for j in range(0,m):
                l,r = input().split()
                l = int(l)
                r = int(r)
                print(food[r] - food[l-1])
            
        
        
        
        
        
        
        
    except:
        break

