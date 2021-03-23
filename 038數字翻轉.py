# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:41:01 2020

@author: YOSO_WANHH
"""
'''
x=input()
'''

x = input()
x = list(x)
x.reverse()

try:
    while x[0]=='0':
        del x[0]
    #另一種寫法 
    #while x[0] == '0':  #變成空字串
        #x[:0] == []
except:
    x = ['0']

for i in x:
    print(i, end = '')
print()
    
