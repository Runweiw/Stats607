# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:40:55 2018

@author: Runwei
"""

#Problem 1
#2.
import math
#define percentile function
def percentile(N, percent):
    k = (len(N)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return N[int(k)]
    else:
        return N[int(c)]
#Input:
#N: list
#percent: folat
#Output: 
#out: int
        
