# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:45:45 2021

@author: YOSO_WANHH
"""
#a095: 麥哲倫的陰謀

while True:
    N,M = input().split()
    N = int(N)
    M = int(M)
    if N > M:
        print(int(M)+1)
    elif N == M:
        print(int(M))
    else:
        break