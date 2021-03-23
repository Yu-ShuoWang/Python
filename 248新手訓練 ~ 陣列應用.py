# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:47:28 2021

@author: YOSO_WANHH
"""

#a248: 新手訓練 ~ 陣列應用

while True:
  try:
    a,b,N=map(int,input().split())
  except:
    break
  answer=str(10**N*a//b)
  n=len(answer)
  if N>=n:
    print('0.'+'0'*(N-n)+answer[-N:])
  else:
    print(answer[:-N]+'.'+answer[-N:])
