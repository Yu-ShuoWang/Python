# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:40:12 2021

@author: YOSO_WANHH
"""
#a224: 明明愛明明

while True:
    for i in range(0,26):
        count[i] = 0
        index = 0
        while (str[index] != '\n'):
        
            #小寫轉大寫 符號忽略 進統計
            if('a'<=str[index] and str[index]<='z'):
                str[index] -= 32
            
            if('A'<=str[index] and str[index]<='Z'):
                count = count[str[index]-65]+1