# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:29:18 2020

@author: YOSO_WANHH
"""
'''
print(bin(int(input())))
#會有'ob'
'''
'''
x = bin(int(input()))
print(x[2:])
'''
dec = int(input())
def dec_to_bin(dec):
    bin = []
    while (dec / 2 > 0):
        bin.append(str(dec % 2))
        dec = dec // 2
    bin.reverse()
    return ''.join(bin)
print(dec_to_bin(dec))

