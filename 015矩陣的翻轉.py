# -*- coding: utf-8 -*-
"""
Created on Sat Nov 7 16:22:30 2020

@author: YOSO_WANHH
"""

mat = [[0] * 100 for i in range(100) ]   #宣告二維矩陣

m, n = input().split()
m = int(m)
n = int(n)
for i in range(m):  #輸入陣列
    list = input().split()
    for j in range(n):
        mat[i][j] = list[j]
for i in range(n):  #輸出順序改變就會達成轉置矩陣
    for j in range(m):
        print(mat[j][i]," ",sep="",end="")
    print()

        
