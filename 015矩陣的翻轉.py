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

       
'''
while True :
    print('输入大小')
    a = input()#横
    b = input()#竖
    m=[]
    try :
        int(a)
        int(b)
    except :
        print('不是整数哦')
    else :
        print('开始输入矩阵')
        a=int(a)
        b=int(b)
        m1 = [[0 for x in range(a)] for y in range(b)]
        m2 = [[0 for x in range(b)] for y in range(a)]
        for x in range(b) :
            print('第' , x + 1 , '行')
            for y in range(a) :
                m1[x][y] = int(input())
        for x in range(b) :
            for y in range(a) :
                m2[y][x]=m1[x][y]
        for x in range(b) :
                print(m1[x])
        for x in range(a) :
                print(m2[x])

      
        
        
