# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:41:18 2021

@author: YOSO_WANHH
"""

def prtResult(n):
    if n==10:
        print("BNZ")
    elif n==1:
        print("AMW")
    elif n==2:
        print("KLY")
    elif n==3:
        print("JVX")
    elif n==4:
        print("HU")
    elif n==5:
        print("AMW")
    elif n==6:
        print("GT")
    elif n==7:
        print("FS")
    elif n==8:
        print("DOQ")
    elif n==9:
        print("CIP")
    else:
        print("Error")
while 1:
    num = input().split()
    sum = 0
    for i in range(1,len(num)):
        sum += num[i] * (8-i)
    y = int(num)
    sum += (y(len(y) -1));  
    tar = 10 - (sum % 10);
    x = int(tar)
    prtResult(x);    
    

    