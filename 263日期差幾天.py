# -*- coding: utf-8 -*-
"""
Created on Mon Mar 1 10:01:06 2021

@author: YOSO_WANHH
"""
#a263: 日期差幾天

import datetime
y1, m1, d1 = map(int,(input().split()))
y2, m2, d2 = map(int,(input().split()))
date1 = datetime.datetime(y1, m1, d1)
date2 = datetime.datetime(y2, m2, d2)
print(abs((date1-date2).days))