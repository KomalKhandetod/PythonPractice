# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:45:56 2024

@author: S23233991
"""

def timestable(x):
    for i in range(1, 13):
        print("%d times %d is %d" %(i, x, i*x))
        
def timestable_1(x):
    for i in range(1, 13):
        print("%4d" %(i*x), end=" ")