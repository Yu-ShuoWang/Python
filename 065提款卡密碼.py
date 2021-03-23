# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:14:01 2021

@author: YOSO_WANHH
"""
#a065: 提款卡密碼

while True:
    output = ''
    try:
        x = input().strip('\r')
        x2 = list(x)
        
        y = [ord(x3) for x3 in x2]          # ascii code
        for i in range(0, len(y)-1):
            output += str(abs(y[i+1]-y[i])) #abs 取絕對值
        print(output)
    except EOFError:
        break       
