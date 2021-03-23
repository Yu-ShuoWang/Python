# -*- coding: utf-8 -*-
"""
Created on Mon Mar 8 21:38:04 2021

@author: YOSO_WANHH
"""
#a738: 最大公约数
'''
#方法一
def GCD(x,y):
    if x % y == 0:
        return y
    else:
        return GCD(y, x%y) 

a,b = input().split()
a = int(a)
b = int(b)
print(GCD(a,b))
'''

#方法二
'''
import math
a=input()
while a:
  try:
    b=a.split(' ')
    b=[int(i) for i in b]
    print(math.gcd(b[0],b[1]))
    a=input()
  except:
    break;
'''

import math
while 1:
  try:
    x, y = [int(i) for i in input().split()]
    print(math.gcd(x, y))
  except:
    break;

