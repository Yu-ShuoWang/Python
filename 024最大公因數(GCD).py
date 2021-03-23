# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:13:29 2020

@author: YOSO_WANHH
a,b,c,d=input().split()
"""

a,b=input().split()
a = int(a)
b = int(b)
while (b != 0):
    c = a%b
    a = b
    b = c
print(a)

'''
為何不可?
import sys
for line in sys.stdin:
    (a,b) = line.split()
    a = int(a)
    b = int(b)
    while b != 0:
        c = a%b
        a = b
        b = c
    print(a)
'''
'''
def GCD(int(input(a,b))
    if(a%b !=0):
        return GCD(b, a%b)
'''