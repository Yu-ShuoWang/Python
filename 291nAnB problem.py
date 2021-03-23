# -*- coding: utf-8 -*-
"""
Created on Tue Mar 2 10:44:51 2021

@author: YOSO_WANHH
"""
#a291: nAnB problem
#https://www.youtube.com/watch?v=ehIWuSVUk7I&list=PLSRyNAP4ghHf1Hptij4sppujoMXCad-jE&index=11
# NEED DEBUG 

while True:
    try:
        ans = list(map(int,input().split()))
    
        N = int(input())
        for i in range(0,N):
            A = 0
            B = 0
            temp_ans = ans
            
            guess = list(map(int,input().split()))
        
            #計算A
            for j in range(0,N):
                if(temp_ans[j] == guess[j]):
                    A += 1
                    temp_ans[j] = -1
                    guess[j] = -1
         
            #計算B
            for j in range(0,N):
                if(temp_ans[j] == -1):
                    continue
                for k in range(0,N):
                    if(temp_ans[j] == guess[k]):
                        B += 1
                        temp_ans[j] = -1
                        guess[k] = -1
                        break
            print('%dA%dB'%(A,B))
            
                
    
    
    except:
        break    
    
    
    
    