# -*- coding: utf-8 -*-
"""
Created on Mon Nov 9 20:29:41 2020

@author: YOSO_WANHH
"""

def tran_to_number(char):
    num = ord(char)
    # A ~ H, 65 ~  72 -> -55
    if num >= 65 and num <= 72:
        num = num - 55
    # I ,73 -> 34
    elif num == 73:
        num = 34
    # J ~ N, 74 ~ 78 -> -56
    elif num >= 74 and num <= 78:
        num = num - 56
    # O, 79 -> 35
    elif num == 79:
        num = 35
    # P ~ V, 80 ~ 86 -> -57
    elif num >= 80 and num <= 86:
        num = num - 57
    # W -> 32
    elif num == 87:
        num = 32
    # X -> 30
    elif num == 88:
        num = 30
    # Y -> 31
    elif num == 89:
        num = 31
    # Z -> 33
    elif num == 90:
        num = 33

    return num % 10 * 9 + num // 10

while 1:
    try:
        x = input()
    except:
        break
    char_num = tran_to_number(x[0])

    #full_add = char_num + x[1] * 1 + x[2] *  2 + ... + x[8] * 8
    full_add = char_num
    for i in range(1, 9):

        # print(int(x[i]))
        full_add += (int(x[i]) * (9 - i))

    full_add += int(x[9])


    if full_add % 10 == 0:
        print("real")
        break
    else:
        print("fake")
        break
    
    