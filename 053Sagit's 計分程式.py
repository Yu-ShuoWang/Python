# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 18:06:27 2021

@author: YOSO_WANHH
"""

#a053: Sagit's 計分程式
while True:
    try:
        score = 0
        inputSrt = int(input().strip('\r'))
        if inputSrt >= 0 and inputSrt <= 10:
            score = 6 * inputSrt
        elif inputSrt>10 and inputSrt<=20:
            score= 60 + 2*(inputSrt-10)
        elif inputSrt>20 and inputSrt<=39:
            score= 80 + 1*(inputSrt-20)
        else:
            score= 100
        print(score)
    except EOFError:
        break      

