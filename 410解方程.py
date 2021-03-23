# -*- coding: utf-8 -*-
"""
Created on Wed Mar 3 17:25:37 2021

@author: YOSO_WANHH
"""
#a410: 解方程

x = input()

for s in x :
    if s.split() == '' : break
    try:
        a1, b1, c1, a2, b2, c2 = s.split()
        delta = int(a1) * int(b2) - int(a2) * int(b1)
        delta_x = int(c1) * int(b2) - int(b1) * int(c2)
        delta_y = int(a1) * int(c2) - int(c1) * int(a2)
        
        if delta == delta_x == delta_y:
            print("Too many")
        elif delta != "0":
            x = round(int(delta_x) / int(delta) , 2)
            y = round(int(delta_y) / int(delta) , 2)
            if (x * 100) % 100 != 0 or (y * 100) % 100 != 0:
                print("x=" + str(x) + "\ny=" + str(y))
            else:
                print("x=" + str(x) +"0\ny=" + str(y) + "0")
    except:
        print("No answer")
        break