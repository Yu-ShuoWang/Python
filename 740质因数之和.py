# -*- coding: utf-8 -*-
"""
Created on Tue Mar 9 10:51:44 2021

@author: YOSO_WANHH
"""
#a740: 质因数之和

from math import sqrt
while 1:
    n=int(input('请输入整数：'))
    print ("%d = " %n , end = '')
    while 1:
        for i in range(2,int(sqrt(n)+1)):
            if n%i==0:
                print('%d*' %i,end='')
                n=int(n/i)
                break
        else:
            print(n)
            break