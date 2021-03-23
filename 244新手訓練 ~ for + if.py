# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:32:11 2021

@author: YOSO_WANHH
"""
#a244: 新手訓練 ~ for + if
    
for i in range(int(input())):

    a = list(map(int,input().split()))

    if a[0]==1:

        print(a[1]+a[2])

    elif a[0]==2:

        print(a[1]-a[2])

    elif a[0]==3:

        print(a[1]*a[2])

    else:

        print(int (a[1]/a[2]))


