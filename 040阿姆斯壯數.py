# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 16:17:57 2020

@author: YOSO_WANHH
"""

def spreadNum(num):
    '''enter a string (integer) and returns the split ('3000' -> ['3', '0', '0', '0']) (list)'''
    
    list1 = list(num)
    return list1
    

def calSpread(list1):
    '''input: a list which is splitted (['3', '0', '0']) (list)      
       output: the calculation of the num (integer)'''
    ans = 0
    for i in list1:
        ans = ans + int(i) ** len(list1)
    return ans

while 1:
    try:
        q = input()
    except:
        break

    q = q.split()
    button = int(q[0])
    top = int(q[1])

    ifTrue = False
    for i in range(button, top-1):
        
        if calSpread(spreadNum(str(i))) == i:
            print(i, end=" ")
            ifTrue = True
        
    if ifTrue == False:
            print("none")
    
    print()

            
       
   