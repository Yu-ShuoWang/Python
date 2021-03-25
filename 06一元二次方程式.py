# -*- coding: utf-8 -*-
'''
Created on Wed Nov 4 11:48:39 2020

@author: YOSO_WANHH
'''

import cmath

a,b,c = input().split()
A = float(a)
B = float(b)
C = float(c)

d = (B**2)- (4*A*C)
sol1 = (-B-cmath.sqrt(d))/(2*A)
sol2 = (-B+cmath.sqrt(d))/(2*A)
if d > 0:
    print("Two different roots x1=",sol1,"x2=",sol2)
elif d < 0:
    print("No real root")
else:
    
    print("Two same roots x=", sol1)

    
'''
import math
def quadratic(a,b,c):
    p=b*b-4*a*c
    if p>=0 and a!=0:#一元二次方程有解的条件
        x1=(-b+math.sqrt(p))/(2*a)
        x2=(-b-math.sqrt(p))/(2*a)
        return x1,x2
    elif a==0:#a=0的情况下为一元一次方程
    	x1=x2=-c/b
    	return x1
    else:
        return('Wrong Number！')
 
a=float(input('Please input a='))
b=float(input('Please input b='))
c=float(input('Please input c='))
print(quadratic(a,b,c))
'''


