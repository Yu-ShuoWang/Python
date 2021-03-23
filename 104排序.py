# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:25:14 2021

@author: YOSO_WANHH
"""
#a104: 排序


n = input("number:")   #不嚴謹，未做實質檢查
sortList = input()
sortList = list(sortList)
sortList = sorted(sortList)
print(sortList)

'''
#a104: 排序
import sys
for sortNum in sys.stdin:
    output = ''
    output2 = ''
    if len(sortNum.split()) > 1:
        output = sorted(sortNum.split())
        i = 0
        for a in output:  
            if i==0:
                output2 += a
            else :
                output2 +=  ' ' + a
            i +=1 
        print(output2)
        
while 1:
    try:
        input()
        list1 = input().strip('\r').split(' ')
        list2 = [int(x) for x in list1]
        list2.sort()
        for y in list2:
            print(y,end=' ')
        print()
    except EOFError:
        break
'''
'''
# 定義函數

def find_smallest(data):
    smallest = data[0]                           # 以串列索引值0的數值為目前的最小值
    smallest_index = 0

    for i in range(1, len(data)):                # 從串列索引值1開始搜尋整個串列
        if data[i] < smallest:                   # 如果目前的數值比目前的最小值還小時
            smallest = data[i]                   # 將該數值存入最小值變數中
            smallest_index = i                   # 同時也記錄最小值在串列中的索引值

    return smallest_index


def selection_sort(data):
    sorted_data = []

    for i in range(0, len(data)):                # 執行 n 次循序搜尋
        smallest = find_smallest(data)           # 搜尋該回合最小的數值
        sorted_data.append(data.pop(smallest))   # 將最小的數值存入「已排序」的串列中

    return sorted_data


# 呼叫函數
data = input().split()
print(data)
print(selection_sort(data))
'''